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
<img src="https://cdn4.telesco.pe/file/od7rhwn4pb3imgYzHwz97_ZwLjesEqXRjYM_6Hd4r0w6g6MN92a9UqZWtkGZwamyyylAOA2VGTZriR-sliCZ7lJN8ITVi3m25pbUb9Xmbl200Mzohxyzp6Vz9d3uj-c5rIchLklorfQS-8Th9v6_NELuRAUX_If0MLczspCI2hwKg6pBCxih3hW4XyUkCbptPl1Vop3H35GRHRVDLpk0MSB4FTOWAgIe9bXLmq9Rcg8Nvw-JUfFu77ZcI4Ue9jvv8CVlA2of6XyNDc9EKtkTlpCn6oxEEGsrJ-uzhLFhWxSP2nDOX2uywl0vAD_TYy0yv8DUw0XuRAU6gzeE0J0PTw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 252K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 10:35:22</div>
<hr>

<div class="tg-post" id="msg-76031">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇷
إعادة انتخاب محمد باقر قاليباف رئيسا للبرلمان الإيراني</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/naya_foriraq/76031" target="_blank">📅 10:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76030">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cff109ec.mp4?token=NH9ozKbJMRV6L7B0P9VMlKUXbC4YqwkHQuEQUTPI7RH1V1-8EG5-VflQ9HNHTq0Atte3kGHMCg2jrg2qDI3DrKhfDdwc9ctI6ppErj1T_JKulYu0vW4Bc6Yj8WGWZcoWmrXnPXP3vnTRp3FcmZbUhC0-J8bJy2za-R_GAM_pBTPwsRQoMikRPTnIIxjvZs2EOym9HX68R32kxlJbitAlz98li0eNiQr9GpvisLo8a4z53RPqd_hjsnKiFvd4dxIm0_j3sfXT66-bc32K1IU38sWMMSZaiOnIO5vkK7FlYMyIR8qmFddbPCfOQrcPYd0f9ewPp5L4rVMpljzwgIC51Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cff109ec.mp4?token=NH9ozKbJMRV6L7B0P9VMlKUXbC4YqwkHQuEQUTPI7RH1V1-8EG5-VflQ9HNHTq0Atte3kGHMCg2jrg2qDI3DrKhfDdwc9ctI6ppErj1T_JKulYu0vW4Bc6Yj8WGWZcoWmrXnPXP3vnTRp3FcmZbUhC0-J8bJy2za-R_GAM_pBTPwsRQoMikRPTnIIxjvZs2EOym9HX68R32kxlJbitAlz98li0eNiQr9GpvisLo8a4z53RPqd_hjsnKiFvd4dxIm0_j3sfXT66-bc32K1IU38sWMMSZaiOnIO5vkK7FlYMyIR8qmFddbPCfOQrcPYd0f9ewPp5L4rVMpljzwgIC51Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
دبابة ميركافا صهيونية تشتعل بصواريخ حزب الله جنوب لبنان.</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/naya_foriraq/76030" target="_blank">📅 10:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76029">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🏴‍☠️
دبابة ميركافا صهيونية تشتعل بصواريخ حزب الله جنوب لبنان.</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/naya_foriraq/76029" target="_blank">📅 09:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76028">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEeTnEn9f7CWMZ0cnUiLG7e9E8kI7j2DoXgglNcya__QPRBdzZAezw0nZZJh9GdA8iaCZHF7YAHivERIl5hmsE4NRF8epFLxA5_bRm6PmBb6VUT-UMOLeHlJh4ZuiPxbtlz2q1-jSwmQodD9B2HDIxf92MPNeJV9tX2Mr6_fBLGVG7dVEqzsw4kPwgos3G3Fc_OgBMVu-gVfjLm2XmMHJ8r5w7pgx-6oiaycGR3rMe0YWKsUXRmxjlTEq7cHrTStTQmcB-c980l5iRxNpWjgoXb46Dk44oE9IFR8bzySaJN4pfF4qAsROclIFEpKANUGSFkQbzqC9h3yOaDHCsj6tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أنباء اولية تتحدث عن شهيد وثلاث جرحى كحصيلة اولية من قوات الحشد الشعبي</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/naya_foriraq/76028" target="_blank">📅 09:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76027">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">انفجار يهز محافظة صلاح الدين شمال غرب العراق</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/76027" target="_blank">📅 00:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76026">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انفجار يهز محافظة صلاح الدين شمال غرب العراق</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/76026" target="_blank">📅 00:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76025">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">انفجار يهز محافظة صلاح الدين شمال غرب العراق</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/76025" target="_blank">📅 00:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76024">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع:
لا تشعر إيران بأي ثقة تجاه الولايات المتحدة، ويراعي تبادل الرسائل عبر الوسيط الباكستاني باستمرار حالة التشاؤم تجاه الحكومة الأمريكية.  حتى الآن، لم يتم التوصل إلى تفاهم نهائي، ولا يزال التحدي قائماً في بعض البنود، ولكن حتى في حال التوصل إلى تفاهم مبدئي، فإن ذلك لا يعني أن إيران ستغير موقفها من أمريكا ولن تضمن وفاء هذه الحكومة بالتزاماتها. أن للأمريكيين سجلاً سيئاً للغاية في المفاوضات، مما يعزز حالة التشاؤم ويزيدها رسوخاً؛ ولذلك، حتى في حال التوصل إلى تفاهم، ستراقب إيران تحركات الولايات المتحدة خلال العملية بعد إعلان الاتفاق، وإذا أخلت الولايات المتحدة بتعهداتها في تلك المرحلة، فستحتفظ إيران بموقفها الرافض لها.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/76024" target="_blank">📅 00:03 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76023">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpBPJRznJmENhgdscasw-t3siKQkjKPpjQuoYwHOMKBvnymkgMYv5ngx6ZbIu3QN_QHK1LAk9gRB6hn_oM6SUtmuqIZol2h1BdaNND10PfLBDGbrbDfAWSlNEk1RPsdNh3dhxVOLsGA6JxflyxTovd97DCFfHYhWb3An6rC87GF6289jJBRlQ2u7j0uNHVtEDXxChilgixl17P39eltDk3pidHhzwg-3x5bBKWyjdW7GiIB2miInEBZTs0LQ6AvAQAzRS-Qm83sh5fVMpPWaVpQ3bvY76iJ5zy-oyJAbHGeMItd7X1GjD0WNyxtjVlKLEwXsdIV-ikcTJKT0p8UCaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب ينشر على حسابه الشخصي.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/76023" target="_blank">📅 23:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76022">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7EWTGTIOla1FX10HVgS_gIeS7lnvBnoV0MGhBf8fVOa60EI_8lYlBFRWdMYXVEPeq-y3mF_SbdAtAt9_ckAJUVbczv6YgOxQSho99K_EpYokK8fqX2yEKs6-JSAxrSU3vjdKao4mHmwvZQ3Y8px55ej1H7B3lQFZ2UHjCWgCtMmH6Cp0gvYNskJZPZ_M4EedpvC5_27Mng8pwNCstrfdojA5Y2OZuYhfgKodh0ItBYchRib6eBitnYaEAiYDUqfY3fQDyXUOF73_0B_Toab0ZzDmYFtcEOZMMvziS5RvZqxFaEA930mIoFvcCcG00XuSX782x6P_C4t6opFncKOKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: حدث أمني صعب جداً في جنوب لبنان.. مقتل جندي وإصابة أخرين من الجيش الإسرائيلي جراء استهدافهم بمحلقة انقضاضية.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/76022" target="_blank">📅 23:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76021">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي: قضايا مثل مخزون إيران الصاروخي وتخصيب اليورانيوم ستناقش بمفاوضات لاحقة.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/76021" target="_blank">📅 22:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76020">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من استهداف المقاومة الإسلامية عبر سلسلة عمليات لقوات جيش العدو الإسرائيلي في بلدة رشاف جنوبيّ لبنان بسربٍ من محلّقات أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/76020" target="_blank">📅 22:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76019">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🌟
🏴‍☠️
لبيك يانصرالله..
حزب الله يعلن عن إستهداف طائرة حربية إسرائيلية في سماء جنوب لبنان بصاروخ أرض جو.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/76019" target="_blank">📅 22:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76018">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOnGkp40nxAWSqcTJh7-_giI7Aw0haeMbAjQ8_ldeGFKslRFkpodoIWE8DqNwiI2KkS8iYniUPNvMPfyl1Ddb6EhYGrUyazrKybjh1m8grLniAzFSBYGW5S-hCwR68HRCxwchAUWv1vvWv42Ie7ZQsqy3jEfT5Z_rfdacjij6cO2zOLVKGKvhnQaOJ7Xq87bZJesMgcce88Io65iWPAdDDFqi0VaQ2KGFc4HZWwC6I7ZTJDfZ3Z9-TlIv9uxRQupHhAjvB3IW2Ar5I4SlOjSv2vXtIYS2zx8TcFnZ9avyVGdMsSJAwTKgfnI3n0lRIFlt3s__kInlPF0VF1bh5Iefw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
إذا أبرمت صفقة مع إيران، فستكون صفقة جيدة ومناسبة، وليست مثل تلك التي أبرمها أوباما، والتي أعطت إيران كميات ضخمة من النقد، ومسارًا واضحًا ومفتوحًا نحو السلاح النووي.
صفقتنا هي عكس ذلك تمامًا، لكن لم يرها أحد، أو يعرف ما هي. لم يتم التفاوض عليها بالكامل حتى الآن. لذا لا تستمع إلى الخاسرين، الذين ينتقدون شيئًا لا يعرفون شيئًا عنه.
على عكس من سبقني الذين كان يجب أن يحلوا هذه المشكلة منذ سنوات عديدة، أنا لا أبرم صفقات سيئة!</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/76018" target="_blank">📅 21:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76017">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a74538399.mp4?token=oZEGnLlLuPd8626eKyJuDAaZNP3g3jsupzWTXw-essjKDwkpGKP-cZZHcFloW6fK1WyplSodDZtaJLdqpD_QxdwHDz5EkQpDOUTwaA6XSEgo_oIZS1Gmg4fyG8ubbom20Oys76RxU7ER7-3HAxMOa0rLrNsoK8YZwLCO_uNaphdePcE9PvZJWpZtlBZIeebDaVChZ_v24PLPoUW05F1oz_RVswW9D3NtWPvv522RK7Gk97BSbYIRmIFaPCKXbhRwXONJjFrFcgcxOTZyigdrkg4FBrwT1QMg-3Jxb_gWCQj10xKF6-U0fT_CONKrQFxyLJ24TStT2Wqoi7jDLJJdBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a74538399.mp4?token=oZEGnLlLuPd8626eKyJuDAaZNP3g3jsupzWTXw-essjKDwkpGKP-cZZHcFloW6fK1WyplSodDZtaJLdqpD_QxdwHDz5EkQpDOUTwaA6XSEgo_oIZS1Gmg4fyG8ubbom20Oys76RxU7ER7-3HAxMOa0rLrNsoK8YZwLCO_uNaphdePcE9PvZJWpZtlBZIeebDaVChZ_v24PLPoUW05F1oz_RVswW9D3NtWPvv522RK7Gk97BSbYIRmIFaPCKXbhRwXONJjFrFcgcxOTZyigdrkg4FBrwT1QMg-3Jxb_gWCQj10xKF6-U0fT_CONKrQFxyLJ24TStT2Wqoi7jDLJJdBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
إندلاع اشتباكات عنيفة بين عصابات الجولاني وأهالي منطقة ترحين بمحافظة حلب السورية.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76017" target="_blank">📅 21:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76016">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف وإحراق دبابة ميركافا تابعة لجيش الإحتلال الصهيوني في بلدة الطيبة بجنوب لبنان.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76016" target="_blank">📅 21:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76015">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف وإحراق دبابة ميركافا تابعة لجيش الإحتلال الصهيوني في بلدة الطيبة بجنوب لبنان.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76015" target="_blank">📅 21:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76014">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⭐️
لمعرفة تفاصيل أصوات الإنفجارات التي سمعت في جزيرة كيش الإيرانية
👈🏻
إضغط هنا</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/76014" target="_blank">📅 20:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76013">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع:
إن الولايات المتحدة لا تزال تعرقل بعض بنود التفاهم، بما في ذلك مسألة الإفراج عن الأصول الإيرانية المجمدة، ولم يتم التوصل إلى حل لهذه المسائل حتى الآن. وبناءً على ذلك، لا يزال هناك احتمال لإلغاء التفاهم في الوقت الراهن، وقد أكدت إيران أنها لن تتراجع عن خطوطها الحمراء لتحقيق حقوق الشعب.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/76013" target="_blank">📅 19:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76012">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🏴‍☠️
رئيس الأركان الصهيوني:
مستعدون للعودة للقتال المكثف فورا لإضعاف نظام الإرهاب الإيراني.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/76012" target="_blank">📅 19:43 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76011">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🌟
الشيخ نعيم قاسم:
سنبقى حملة راية الحق حتى تسليمها للإمام المهدي (عجل الله تعالى فرجه الشريف).
ستدافع المقاومة عن الأرض والشعب والشرف وكل من يواجهنا مع "اسرائيل" نواجهه والسلاح سيبقى.
خسائر إسرائيل كبيرة جدا وما يحدث في الجنوب اللبناني سيكون سببا في زوالها.
حصرية السلاح في هذه المرحلة استهداف للمقاومة وخدمة لإسرائيل.
المفاوضات المباشرة مرفوضة بالكامل.
سنعلن التحرير الثالث قريبا بإذن الله تعالى.
من حق الشعب أن ينزل إلى الشارع ويسقط الحكومة في مواجهة المشروع الأميركي الإسرائيلي الذي يستهدف مؤسساتنا.
لدينا أعظم مقاومة أذلت العدو الإسرائيلي فاستفيدوا منها.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/76011" target="_blank">📅 19:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76010">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2993zbJ4i-5ksSpThsAA-x3V5J4OIF_7f7Nc75nJUmlTyk3kZG7gHZVJduEuNVFUEEDszsP-yIcVtQmVy8Xj-sn9av5IVfSCYgZLSzQr21ycUCZdCJAxOJbZfL62ElrYugwquS1YEzQjoSPKfoWr8L-yKPsbZHGbFvLx7gweSVDINUHm5eUWAr19z7mwQmwqY790GvmOkGgvwZ0fdwVtgntJ2w4cevDAWmagDTGG7myn8aUM3M0SRRS36Jv7mky7p4KiXGjLPZZbImzxKY2ROROl0YpExfweP2BGVNTE19CNclKEtCLbfUToZu-8LCQ5ht9AVT8kVhK3enGIvfaIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: حدث أمني صعب جداً في جنوب لبنان.. مقتل جندي وإصابة أخرين من الجيش الإسرائيلي جراء استهدافهم بمحلقة انقضاضية.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/76010" target="_blank">📅 19:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76009">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇺🇸
مسؤول بالإدارة الأمريكية: سنقدم تنازلات بشأن تخفيف العقوبات إن تنازلت طهران بمسألة التخصيب.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76009" target="_blank">📅 19:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76008">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇺🇸
مسؤول بالإدارة الأمريكية:
سنقدم تنازلات بشأن تخفيف العقوبات إن تنازلت طهران بمسألة التخصيب.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76008" target="_blank">📅 18:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76007">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: حدث أمني صعب جداً في جنوب لبنان..
مقتل جندي وإصابة أخرين من الجيش الإسرائيلي جراء استهدافهم بمحلقة انقضاضية.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76007" target="_blank">📅 18:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76006">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATrnIPoEBO7PCCSy-DDVOTgTaolQ2XJVnfYFJv3PpSur6NzSqPqCDRXxK8COcJRj6-C-P7RRzbTGWfjzIPFTRYCDiwlSQGMmYIF8Iqmmu1ArN_hAOAn7UyEkLE8Gkou7er_-OxJLOwu7WL4ktG4USHRh_R7MI8TeD2pI-_TLEu7_oR0nm_uJry5G_ymJdRatLy285cBd0w9SdJsTgZ-OLbITWRWiUv5M6E3OMUUHKN-IwnJ-HsqCz3_cbKlJGSRzapmBxyDGfh2oQNSNWhSt45rOXU6fh4gvgruRtV1ZZcJ5rfIgVaRt1jp0MsZgmKrapvOEvPpV35ywvNAkhFHoZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب: كانت إحدى أسوأ الصفقات التي أبرمتها بلادنا على الإطلاق هي الاتفاق النووي الإيراني، الذي طرحه ووقعه باراك حسين أوباما والهواة في إدارة أوباما. لقد كان طريقًا مباشرًا لتطوير إيران سلاحًا نوويًا. ليس الأمر كذلك مع الصفقة التي تتفاوض عليها إدارة ترامب…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76006" target="_blank">📅 18:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76005">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51e83ce1a0.mp4?token=UWPsCfdR8xSu0Ut5FqLdyCtR-_tK4s_iPLqLjuAUfm1ovLU7_HV3DYT0ZtggZ3Zshbr9Xhx51OOETTYQL9HalRkx3ak4pnK04NkcxAS6kPZOPuOA1JfPFnLl9RxuIM0Qx1Ag86OOC9pGUisRDLtLxtqh1RuH8BGt8t_lT78sErOqguGpB5AFII-kOtcr20x4eZIXsIAQuVZ52qu71zGH452F3urXkPzWLSbhaTkpQQ9rsgY-9vtu7nzZbnkcR_0C8I2WeDnHYfbI5boV7kVVfSppS1JPiwP_4ATz3fTazElf6DOwbNcfzC2FLXyMD9fr-zSB6CyfmB4Mp8s6O7a6rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51e83ce1a0.mp4?token=UWPsCfdR8xSu0Ut5FqLdyCtR-_tK4s_iPLqLjuAUfm1ovLU7_HV3DYT0ZtggZ3Zshbr9Xhx51OOETTYQL9HalRkx3ak4pnK04NkcxAS6kPZOPuOA1JfPFnLl9RxuIM0Qx1Ag86OOC9pGUisRDLtLxtqh1RuH8BGt8t_lT78sErOqguGpB5AFII-kOtcr20x4eZIXsIAQuVZ52qu71zGH452F3urXkPzWLSbhaTkpQQ9rsgY-9vtu7nzZbnkcR_0C8I2WeDnHYfbI5boV7kVVfSppS1JPiwP_4ATz3fTazElf6DOwbNcfzC2FLXyMD9fr-zSB6CyfmB4Mp8s6O7a6rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اندلاع حريق وارتفاع اعمدة الدخان في منطقة جبلية حدودية مع إيران بمحافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76005" target="_blank">📅 18:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76004">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b63f2c0f5a.mp4?token=mNH5eEvWU3cTJXWdUjGIcRliPjqreF99m08HwC9dFoRw-yaqH2iK3RjXp4TJzxiEc7p-v3gQg7aDCjrudANkRznOdwpBW_QFoNgbKBEJtbPdKfBmdwc2irAYLtxT6Uh_Br6hBwRXqC6AxYTx4jDeTDxLUZy3bDesh0vcNhM3BVR0dgz2nUqUGWbYQITzMt8x3teohcObCk5ZrbEgSzqIzq7BiFklXLAm4ynRB2-kfQgTFuN1CEpj5NBTmSQf_RML9MK5AqyqFt-GP3WDLDu2G_ewsyCcKlNPd7I82fFkiH-TG801PLrgHnBhnKfme7pStviX2wvDSjO9zHKwh7Qemg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b63f2c0f5a.mp4?token=mNH5eEvWU3cTJXWdUjGIcRliPjqreF99m08HwC9dFoRw-yaqH2iK3RjXp4TJzxiEc7p-v3gQg7aDCjrudANkRznOdwpBW_QFoNgbKBEJtbPdKfBmdwc2irAYLtxT6Uh_Br6hBwRXqC6AxYTx4jDeTDxLUZy3bDesh0vcNhM3BVR0dgz2nUqUGWbYQITzMt8x3teohcObCk5ZrbEgSzqIzq7BiFklXLAm4ynRB2-kfQgTFuN1CEpj5NBTmSQf_RML9MK5AqyqFt-GP3WDLDu2G_ewsyCcKlNPd7I82fFkiH-TG801PLrgHnBhnKfme7pStviX2wvDSjO9zHKwh7Qemg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 22-05-2026 أحد جنود جيش العدو الإسرائيلي في موقع المنارة عند الحدود اللبنانية الجنوبية بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/76004" target="_blank">📅 17:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76003">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-FJBQidRrpecGGgBs-ibiTuJW5ZPEfSFP957utvACPUmO_rg5OdU_-GnF_ZgiEsrJsrM-vLJloks_SUB9KKkiZY3zLGu_VglljShYDZnkuUsRio6yiwL2YNY9pS9Fd6wADF4kWFk_WixDqN_ygHivnzATz0hIDcWkX_wr2moNJYnNJ7ryaewKol2LIQXKN1x335_x3uV7ktkKK_m8RF5u5aZ16gN3VW1GZTdvpeYtvA_xeFiTz4OMyDyIlmDVLeufvSfMIoKQZZP6O6QZCDmq6OapyJK2-Ey_x1f0_TDlf1FPip-2VWSpMAJfv-q7oX3RecBPxzVM1CahQC1HK51w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب
:
كانت إحدى أسوأ الصفقات التي أبرمتها بلادنا على الإطلاق هي الاتفاق النووي الإيراني، الذي طرحه ووقعه باراك حسين أوباما والهواة في إدارة أوباما. لقد كان طريقًا مباشرًا لتطوير إيران سلاحًا نوويًا. ليس الأمر كذلك مع الصفقة التي تتفاوض عليها إدارة ترامب حاليًا مع إيران - بل العكس تمامًا! المفاوضات تسير بطريقة منظمة وبناءة، وقد أبلغت ممثليّ بعدم التسرع في إبرام صفقة لأن الوقت في صالحنا. سيظل الحصار ساريًا ونافذًا بالكامل حتى يتم التوصل إلى اتفاق واعتماده وتوقيعه. يجب على كلا الجانبين التريث والتأكد من صحة الاتفاق. لا مجال للأخطاء! علاقتنا مع إيران أصبحت أكثر احترافية وإنتاجية. ومع ذلك، يجب أن يفهموا أنهم لا يستطيعون تطوير أو الحصول على سلاح أو قنبلة نووية أود أن أتقدم بالشكر الجزيل لجميع دول الشرق الأوسط على دعمها وتعاونها، والذي سيتعزز ويتوطد بانضمامها إلى دول اتفاقيات إبراهيم التاريخية، وربما ترغب جمهورية إيران الإسلامية بالانضمام أيضًا! شكرًا لكم على اهتمامكم بهذا الأمر. الرئيس دونالد جيه. ترامب</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76003" target="_blank">📅 17:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76002">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKCLT3nDkJ_Jct10L28C1A9HKQF_ProXkgBwEOkKxUmdumVK_-gLMfkA-62J6iNuwllDK_uhMUUq17xuXEiDjoBXtrBc3O1RYA068cN-RL0X1bi0Rk1ExYE6AD05w4BWtU5j7bRLQOvL5M6mbZZnKustv5wZd6g_Z-4XlRX07W83ezpOkDVJigtwY8CzztvVvVrqaY9X71di1AoN7bpkURWTJ3icmElYlVGvOAhacVNxfMp6VhOx2RT0HQ23nOzAO0FoII8cBBzj09EdowOnklhTl4Qaq1tMg1gTHRhrFRvHftyOBJhPai9gvrOC0tHfjlE9I3kMreNmJ5Sq931AqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
فاينانشال تايمز:
يُزعم أن قوات الحرس الثوري الإيراني استخدمت شركة مقرها في الإمارات العربية المتحدة لشراء معدات اتصالات عبر الأقمار الاصطناعية الصينية مرتبطة ببرامج الطائرات بدون طيار والصواريخ الخاصة بها.
ويُقال إن المعدات انتقلت عبر دبي ورأس الخيمة قبل وصولها إلى إيران عبر سفينة إيرانية بدا أنها قامت بتزييف موقع GPS الخاص بها لإخفاء عملية التسليم.
وكانت الشحنة مرتبطة بشركات مرتبطة بقوة الفضاء التابعة للحرس الثوري الإيراني على الرغم من العقوبات الأمريكية القائمة على الكيانات ذات الصلة.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/76002" target="_blank">📅 17:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76001">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfS4etVGI9xswT-T0y0hs90gN7E9JKib4s6BK8-yPWhEtlsEX81d0hh1w_Iga_q9ndqx1iJLIdlnLNExRBxTTxBuOdbvlTyn3XOt1lRZCEkMOO_EWxqyBkvFuBDnGh4fnELKYX-72zWALg79XLxVom5-IBftuccgpIi_gOaLoR6Bd4qsS_T8aPMXBndW3OwA75Z57lzat4uN4FlG3SDVQZp0W_KEm2P9oCh0nzwfOCgHstf5gmccf2DQvDaxUMqRgg7KvY7KQpk1MjZHZfZQDk9mbIy_lYQUjMIgwREp1sRaUyNxKvb2MEmbEWGuzjgNrFqvm-f7_gJsk8DpnHE0rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
حزب الله ينشر:
بعد قليل...
الضاهر تركضلي تركضلي..
😄</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/76001" target="_blank">📅 17:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76000">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6uUFwnQpBVaBguyo91cG2BYcmlGG4wpw93hUpo4e-QL7FOtPXc05H9PUoD8-83VZmsOJRS9WCiEPMsufuRmjg91algUnYDYKSPd5RyRPk4C0nmTXjaZNqnBsxLLhtnuO_KyaTIl3pjKzUkfWWg8jMBge5ZJ2h1qc6k4OBaeT13xmkbBXXY_4BIUQ69Su2Rt7hJDSVfyyPThZuPoVFtwSLdrAPxPpwcTTYcNliovUmM-VfJKeNvipBvZ4sQaD1QvZil2Bg4sbJ4nQ65YQt5sWVdIgrZLrb8jPr1it5xCAUOAabBzfgQicPBBEBq1Q7B_gKwhuGt8ljn1L4cpJSwUbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
نتنياهو يغرد:
لن تمتلك ايران سلاح نووي.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76000" target="_blank">📅 17:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75999">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
‏الاتحاد الأوروبي
: توسيع نطاق العقوبات على إيران بسبب إغلاق مضيق هرمز</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/75999" target="_blank">📅 17:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75998">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4bbaeabc5.mp4?token=OEagbdiDJtxb2THrSjtCaH3O1qHXT_h_FO7ydI-_jy9I7p482Q4MdspKxF_NaRg_MJhxWVTbuBgb4-CTX3ECRcZdvcrFK3WgxEW78Frfq_6M9gxHEyRErUBw7N6IIbioko5p2yVFzPHmnnx_TmSK3drYV_0iWsirOwefsx0RlPCuGc3kyf16tbUvEL3qCzlKPuKorygimz4ovogSI3HnXEYixCE02t5V-CRqftdUxWJHTOJb0FZ0CRE92ucfoDhJKiDDRIp-0S-pe-zULUkMUGL-y7mUN_PG6kUFjnCugsFRPIRc5YQFwpAN7la81KucGqDG9SmZatm0dU_7tB2_IhsBCTZELrLggjhZgoF3FUXQnqzmUtanEw8Uji2AjAJiRzIObrOIdOgfFreUMmAJscrcw084HHEyk9Nea2pDwbjWT6mvQUwZF-nGf7hOjLhlGqkYIp_WQHjep1MZAYC0GtG4O6zwa-y1LoFBVncJAkqH8w2TtIaF2vutDg0-TnorEx-PUuWaaqhGkmjp47RfrfEsYZ9HNZmxKNMrJpiSZYXLHfKAmh-4G8hAdYr65s8ote_EdOs8Kql_Kr7yiZu99YjvCc_77jyV_f6yIoRWPF4PG1JKSGY1An4Md5s3ZIp5EEqiC8HktwH0bcY7krdtuqtF-WCwU8BAy5EeMaPuU3s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4bbaeabc5.mp4?token=OEagbdiDJtxb2THrSjtCaH3O1qHXT_h_FO7ydI-_jy9I7p482Q4MdspKxF_NaRg_MJhxWVTbuBgb4-CTX3ECRcZdvcrFK3WgxEW78Frfq_6M9gxHEyRErUBw7N6IIbioko5p2yVFzPHmnnx_TmSK3drYV_0iWsirOwefsx0RlPCuGc3kyf16tbUvEL3qCzlKPuKorygimz4ovogSI3HnXEYixCE02t5V-CRqftdUxWJHTOJb0FZ0CRE92ucfoDhJKiDDRIp-0S-pe-zULUkMUGL-y7mUN_PG6kUFjnCugsFRPIRc5YQFwpAN7la81KucGqDG9SmZatm0dU_7tB2_IhsBCTZELrLggjhZgoF3FUXQnqzmUtanEw8Uji2AjAJiRzIObrOIdOgfFreUMmAJscrcw084HHEyk9Nea2pDwbjWT6mvQUwZF-nGf7hOjLhlGqkYIp_WQHjep1MZAYC0GtG4O6zwa-y1LoFBVncJAkqH8w2TtIaF2vutDg0-TnorEx-PUuWaaqhGkmjp47RfrfEsYZ9HNZmxKNMrJpiSZYXLHfKAmh-4G8hAdYr65s8ote_EdOs8Kql_Kr7yiZu99YjvCc_77jyV_f6yIoRWPF4PG1JKSGY1An4Md5s3ZIp5EEqiC8HktwH0bcY7krdtuqtF-WCwU8BAy5EeMaPuU3s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 18-05-2026 آلية هندسيّة تابعة لجيش العدو الإسرائيلي عند خلة الراج في بلدة دير سريان جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/75998" target="_blank">📅 17:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75997">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🌟
‏
يديعوت أحرونوت:
إذا تم توقيع الاتفاق بصيغته الحالية فستكون هذه كارثة على إسرائيل.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75997" target="_blank">📅 16:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75996">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/117e266d3d.mp4?token=fiF2pFuP8JbkM60j6awue7l_XoTjm8TmggDPtRT3q3CCyMQZPkMh_QSEQxuGKuM1PuJCJuQOm1f9N7CeeU93A2rFR9X6AtMuJpfv8OR8W2Gm9074ZmMuW8twejYaHXaLa5XW0b50Vq2xN6tnEf3YpkSdDoLuoGkKyaQa8C1Du2BkxaDdbTv_WqcA1y3YDbQQUYPV_kESgdd7DLU-fRW6e68Naf_rgFcnDJ63NenEw20CImBC--cT1ajtnOau-5g9aayMOgwnLVYdoSpyI4n5jh4RLfZx2HX2Z8YxOcibtd3WUyb0WvoUOIEysloMYw7AaD6ekSWj_dUsoKTZqv3U0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/117e266d3d.mp4?token=fiF2pFuP8JbkM60j6awue7l_XoTjm8TmggDPtRT3q3CCyMQZPkMh_QSEQxuGKuM1PuJCJuQOm1f9N7CeeU93A2rFR9X6AtMuJpfv8OR8W2Gm9074ZmMuW8twejYaHXaLa5XW0b50Vq2xN6tnEf3YpkSdDoLuoGkKyaQa8C1Du2BkxaDdbTv_WqcA1y3YDbQQUYPV_kESgdd7DLU-fRW6e68Naf_rgFcnDJ63NenEw20CImBC--cT1ajtnOau-5g9aayMOgwnLVYdoSpyI4n5jh4RLfZx2HX2Z8YxOcibtd3WUyb0WvoUOIEysloMYw7AaD6ekSWj_dUsoKTZqv3U0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب مستعينا بالذكاء الصناعي   كون الحقيقة مؤلمة جدا</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/75996" target="_blank">📅 16:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75995">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNoBczEFGayelEUwSSCCcKZWx5kDcyvQj_Tj7wIGyEPO_T3MxmI5OM0263XcWMUAfg3s0vgpMNHKf-Zq6VaJWs89St8XuamYmsQtqt47H6LsIlZjw1MDgKNtJnB4R_JNe9XwIHbSvKumHYPjQgpmaIHF3zHCQ2xmb2mAP8KWh9dvAd0cr4nwGhmKHWy1kH_wfxbiMcb0-SFOoFywI9qO49UFULrsZG6qbAFK6nU1DPenWfIp4BqrUy5Im79q5up9XJp7vUFITJv3y9Hfmf9M5SZhpu64C4XYdtfeecL57sK0w3m86KPshWOd0-Amrq8iPndbuX_q3HkL0VTeHSj5yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترمب ينشر مجموعة من ساسة الحزب الديمقراطي يرتدون زي المساجين!</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75995" target="_blank">📅 16:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75994">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea9114205.mp4?token=ZHqZyzMuRKvkPCindcU7YIoiRNRmG5mjIUU-jZ89-U6WNSfnpTeyour9JCdatUNEIyXSqEP9yH22h3WGjyUMrKcK7mUWJPCc99aLGTYbuR1aF_WGwvIlbc_h0QT8rN2AdPZJL3pAyJKRTVfyIQht0nZJr0OMgBsHDzmaF_6wYcHri6KH9a7D4ZjQXYH5is4qW1PHz-4PK69WxfycfJ7tuRzCKNlaMfWUyNmEj7lb7YZFUrQ-wVJLYriQzKvtd4fhf6zZDYfa87wteR4LFL4RotIhZfDL4ger0-wSUpIJHq0zjwsT0Y0OR6ku9u43F8EnqjcSkGvZUKd8C1rrOp8pEAqscEXRhYT4lhaXtELNov1xdMBWRk9QRx9eYN_zmE0BkkknOxk4Tu0K10TPllvzvkBi-VQe_-amzRchZNhc_BevwVgdE8wYeKcF2NwT1rfbzGwSiWljCQNCB2jsrXmG2LFK8p1VUoPUS8bi6_nYTsAX-VnSzN1bvSHcS66edWKHaRgLYTC1ATruJUcFEB8i8VJgfJQGS7RUboDUXh7w0zGz7fwudPQwuOkNS6oUcaR-lhVXLRzjFdeKHn6wXTX4rSsXLI6GacBfPxGECni-PXCQeUQAJrZxTe0f2zWaPyPFGb2hAm7ducGLT8lcM3P0sNXZfIbU3n9jidTv2kUOgnU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea9114205.mp4?token=ZHqZyzMuRKvkPCindcU7YIoiRNRmG5mjIUU-jZ89-U6WNSfnpTeyour9JCdatUNEIyXSqEP9yH22h3WGjyUMrKcK7mUWJPCc99aLGTYbuR1aF_WGwvIlbc_h0QT8rN2AdPZJL3pAyJKRTVfyIQht0nZJr0OMgBsHDzmaF_6wYcHri6KH9a7D4ZjQXYH5is4qW1PHz-4PK69WxfycfJ7tuRzCKNlaMfWUyNmEj7lb7YZFUrQ-wVJLYriQzKvtd4fhf6zZDYfa87wteR4LFL4RotIhZfDL4ger0-wSUpIJHq0zjwsT0Y0OR6ku9u43F8EnqjcSkGvZUKd8C1rrOp8pEAqscEXRhYT4lhaXtELNov1xdMBWRk9QRx9eYN_zmE0BkkknOxk4Tu0K10TPllvzvkBi-VQe_-amzRchZNhc_BevwVgdE8wYeKcF2NwT1rfbzGwSiWljCQNCB2jsrXmG2LFK8p1VUoPUS8bi6_nYTsAX-VnSzN1bvSHcS66edWKHaRgLYTC1ATruJUcFEB8i8VJgfJQGS7RUboDUXh7w0zGz7fwudPQwuOkNS6oUcaR-lhVXLRzjFdeKHn6wXTX4rSsXLI6GacBfPxGECni-PXCQeUQAJrZxTe0f2zWaPyPFGb2hAm7ducGLT8lcM3P0sNXZfIbU3n9jidTv2kUOgnU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 14-05-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في بلدة الطيبة جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/75994" target="_blank">📅 16:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75993">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe46a8c5f9.mp4?token=Q_y8OHyRR0U8LEuGPyAS5HtyuqD4CfnxvWBBV-OPwlXqBTpmFQ3qRZJH1gXRnZ2nd2_m3nQkjUYTWZQhqzcmfNCExPrZbRtZTIZLrQg-OttqakQGD5uaZ4e9jS8FG0ZuSYoxyvoZR8sMP43kVRxN2mf8l5DUBOJ8ZKwwAILW0l2ubg8THR2ZhI_U5ySmmCZUgFiZUgSGkxL4KZpKSr1U1xkLIaboeHN0MISDofG9WgUBV8UQ3XS3UM1DQ--Hjyp6EmhMQNHuvYF0iCu0_1WFAO9Cqt2UZFOhYQdtgTSWamRfPVkieGQzXmet4Z-K0nO4I8YCQjcjF1hT9tlwmH7a7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe46a8c5f9.mp4?token=Q_y8OHyRR0U8LEuGPyAS5HtyuqD4CfnxvWBBV-OPwlXqBTpmFQ3qRZJH1gXRnZ2nd2_m3nQkjUYTWZQhqzcmfNCExPrZbRtZTIZLrQg-OttqakQGD5uaZ4e9jS8FG0ZuSYoxyvoZR8sMP43kVRxN2mf8l5DUBOJ8ZKwwAILW0l2ubg8THR2ZhI_U5ySmmCZUgFiZUgSGkxL4KZpKSr1U1xkLIaboeHN0MISDofG9WgUBV8UQ3XS3UM1DQ--Hjyp6EmhMQNHuvYF0iCu0_1WFAO9Cqt2UZFOhYQdtgTSWamRfPVkieGQzXmet4Z-K0nO4I8YCQjcjF1hT9tlwmH7a7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
تنفيذاً لحكم قضائي يقضي بتنحية أوزغور أوزيل من رئاسة حزب الشعب الجمهوري، اندلعت اشتباكات بين قوات الشرطة وأنصار أوزيل أثناء دخول القوات إلى المقر الرئيسي للحزب في أنقرة.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/75993" target="_blank">📅 15:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75992">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYWNGUXJsIH2jwhByPfRTt2AzSt-AwprAOL1m4FHIskCMWBqBbB-37fGiFnijqhP4vB0ZJCyO6tS-4Zi4J3yfWIqYGYtxEl91KGv5YOoa34lGeiskWxSmG3ILs3XyfPXEIXT0kfWJbSSOckRT1mpr0ipxm7pa1OWnvU15Pj0--2Nmu3hAjuG6HQ4gIDIqtwBPilutg3U5T8GzKjpJhkWmaCmxD_kGztuWZHQTloKgtBC7GUTluYDZATKZh9OCK7Zb5mceKAt8wLklw7JZm6sl7JfbbBzFdA1ZyoGjY8LVEe3Mvv5XgS_614L1hPcjlyeaOY7PMW2arO3glqGuIhdjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب مستعينا بالذكاء الصناعي
كون الحقيقة مؤلمة جدا</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/75992" target="_blank">📅 15:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75991">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff86c83697.mp4?token=TyxD8b1UkRxToMl1DKuVAZZc31MNYja0-k9OGdINjKO1WkG-U7-gCXz5Nx8gJfyRg12IW-lTpxiVFRrii7DVIdjs4ZtazCHNPR3y0no41LsxI9Enxelpk69rKDxPKbtfHCsRjsDqz9e3PWZrq8ixGpdYyZowIrbsEoODyttGXJF91XBC4y5Z1qc_qPQA0gma8jBJX7WDZkKVLJu28TvkXr5K-xPf4CqEHG2hskoC3aBGdkm8mCTg3ZqjTbAtGIMaZGaFb6ZFDAy2Jp36npkl7xmT097Y46KADJYJgjgZKx6Ij0zunjPQEMjgFyS7pslwqIQhYwnl9QgM0jL1-DJIhz_O7T6sA9o0JhzRdHI5OdS4HmNe4yfikuDupvnLua5E22Fg4_ZKOWqIB6Mqnw8g43NYYhWiQzJhYhAsVP0DkH2JqXJga2escIf-jkx9RJO-i-zjRRMkkO28Kn8bDPUox_SaOuJv-aO0LaRe_6yDik2fQm7SY-CLdWu0eDIInHRJkUjWdKpZljfMrYuZOholAa8ONR2yT8_E175AX4uJwZEoGnbKO9MncPe6hoamnKXbt-MnFxy8fNcLfkQoUpYMUARXjAJgNrm9fGgPcIK-x7aHscn-nIyaGcQSWpuv60lsS1O1RQ2Mdu2_bUoRPM0cnRV2TeKr-4J9EISSa9H1TOs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff86c83697.mp4?token=TyxD8b1UkRxToMl1DKuVAZZc31MNYja0-k9OGdINjKO1WkG-U7-gCXz5Nx8gJfyRg12IW-lTpxiVFRrii7DVIdjs4ZtazCHNPR3y0no41LsxI9Enxelpk69rKDxPKbtfHCsRjsDqz9e3PWZrq8ixGpdYyZowIrbsEoODyttGXJF91XBC4y5Z1qc_qPQA0gma8jBJX7WDZkKVLJu28TvkXr5K-xPf4CqEHG2hskoC3aBGdkm8mCTg3ZqjTbAtGIMaZGaFb6ZFDAy2Jp36npkl7xmT097Y46KADJYJgjgZKx6Ij0zunjPQEMjgFyS7pslwqIQhYwnl9QgM0jL1-DJIhz_O7T6sA9o0JhzRdHI5OdS4HmNe4yfikuDupvnLua5E22Fg4_ZKOWqIB6Mqnw8g43NYYhWiQzJhYhAsVP0DkH2JqXJga2escIf-jkx9RJO-i-zjRRMkkO28Kn8bDPUox_SaOuJv-aO0LaRe_6yDik2fQm7SY-CLdWu0eDIInHRJkUjWdKpZljfMrYuZOholAa8ONR2yT8_E175AX4uJwZEoGnbKO9MncPe6hoamnKXbt-MnFxy8fNcLfkQoUpYMUARXjAJgNrm9fGgPcIK-x7aHscn-nIyaGcQSWpuv60lsS1O1RQ2Mdu2_bUoRPM0cnRV2TeKr-4J9EISSa9H1TOs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 19-05-2026 آلية اتصالات تابعة لجيش العدو الإسرائيلي في بلدة الطيبة جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/75991" target="_blank">📅 14:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75988">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GrCIu7ms_8qawOYneBvzTbI8Uhry19-6gto4vGrnuf_2E4cs5KKrqIo90XmBsm5f-4I9jZiLTuVT8yzelSsmbWp-7-nl46xiKnWwxNe6uZvsBtiXcSFF0EJt31nViHuph5C9QkNAWXWUYPAAsLDN2nWjwUO0lotxb1vahj5j8dPt4K1wcZ8tz6L2Su5E2lsyQ4sfEKWF8VZmonEgqJWQs2Cf10dqdvVCjlSBDN_zzpqxVG3RKIAacyEUKSUnPHnfSvKZgAlgEMMDYQ62aB4IjYMky9T21GySg-EK3LJmyaBDUyoZzifUwk410uda_aimx1mxhTIEBZNEwouspMtXAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ETk_7x1mY_MXscqADRSxgKc8MoSFY5twshkJ_K0gmQkPxXkwVwNW13sb6TBQv_vgVTGVJRzF0f5mItAgpficb7xuu8EVQFBNDTZwM0qfZyhLHawj0QSkj9WP-r152tJUAcqXYNwsMRzB4gwjVD7rUNC6fdaaKHL3hJF59wgclY7sgM5AtqMM_KdmmOqRhUhnL4MrotF5LEtxn_kwoRdrqILiGRN8H75HKiK0uEHizVXt_7f4RWGLm3Jq9EUYT0aZiqbwWgsAC7lN6TIc_iSlwu4x-8eHoNau2NXBvkNgERH3qMIv28VTxJwf0ciwtQoK8xQlmU6Wd5KK7EVrqQlZvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HVs0RYmIJwRXao0Y9LhkbW_ahO5VRGE0-VNW5jc9yjhj-B-iSasJB5sZhQWnqar8VlAn5Lk3QfMDeGafGHUd8bbjju1SUUYUtxxWk3l42DwMCU19t-MHZrKfchWdDIn6lP_HO8z38Wx4O0PXgeKWlO-8s0yEt6k38P3G0ZwO3MyzMP0HTZHWHRoVvVdqUifrqTk2Q6UIVDymVsSSJblHeTzmXnUCaNWgGksYBS9NZOrRZ1OIqIsrFKunYPapED7RHaBGbuNhdIUl2LJXSFhjPjpPcyNajVjnG_-IPr43EZv2otP31n73Xp7lVz6su6hP3hsl1FCZ_bgAQagHfGMsDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👍
ابطال الحشد الشعبي يسعفون اخوتهم في جهاز مكافحة الارهاب بعد ان انفجرت عبوة ناسفة عليهم.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75988" target="_blank">📅 14:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75987">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🎤
فوكس نيوز:
الاتفاق المتوقع ينص على بقاء القوات الأمريكية بالقرب من إيران لمدة 30 يومًا.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/75987" target="_blank">📅 14:24 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75986">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
حكومة البحرين الجائرة تصدر الحكم المؤبد لتسع افراد مدعية تخابرهم مع الحرس الثوري الايراني.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/75986" target="_blank">📅 14:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75985">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8621a769e.mp4?token=axe9SE69SiYBBUKuZ6YakPzYWNnh8rgMT1KorSd_SGEP3TNQ5VIWShDwPWWyRNskzVpvH-ZTIiWdjJ_am-ROq4T0NQ2mZcYafbBk66DD7CG7By53ya0xwWbaoJ6Lw_l9N_s4z6HFn8b_F6H443kEUiPE9dp7xOECKCdKY9t95sQ6w-r143hSsbFLhLrtDKolFwMvtUR4cA-0gooN0TidB5e-4P285kSY_w0Qas_Sj-eZqrtruXP2QvjY-LzGokoR9eaXua_-SfDGHKb75lwakF3c-_P1FU5B_qkJbJMiQlux2EAJCBgRM7DcJ768ViTPQf-2AlrWOZHDB6RMzV6W6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8621a769e.mp4?token=axe9SE69SiYBBUKuZ6YakPzYWNnh8rgMT1KorSd_SGEP3TNQ5VIWShDwPWWyRNskzVpvH-ZTIiWdjJ_am-ROq4T0NQ2mZcYafbBk66DD7CG7By53ya0xwWbaoJ6Lw_l9N_s4z6HFn8b_F6H443kEUiPE9dp7xOECKCdKY9t95sQ6w-r143hSsbFLhLrtDKolFwMvtUR4cA-0gooN0TidB5e-4P285kSY_w0Qas_Sj-eZqrtruXP2QvjY-LzGokoR9eaXua_-SfDGHKb75lwakF3c-_P1FU5B_qkJbJMiQlux2EAJCBgRM7DcJ768ViTPQf-2AlrWOZHDB6RMzV6W6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
أحذية شهداء الجيش اللبناني أمام مبنى مجلس النواب في العاصمة اللبنانية بيروت، احتجاجاً على مشروع قانون العفو العام.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/75985" target="_blank">📅 14:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75984">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🌟
🇮🇶
جهاز مكافحة الارهاب:
يعلن استشهاد 3 مقاتلين وإصابة 4 آخرين بانفجار عبوة من مخلفات داعش في صحراء الحضر جنوب غرب نينوى شمالي العراق.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75984" target="_blank">📅 13:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75983">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 18-05-2026 آلية نميرا تابعة لجيش العدو الإسرائيلي عند خلة الراج في بلدة دير سريان جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/75983" target="_blank">📅 13:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75982">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94daa968c2.mp4?token=TGp11dbD_hpBkpU9xkdsOB0HKNKOR7EbrjfV1Ep7_YmfLnBi-P6vhTI8Y0_xQIWTCZP7hB50c1pHAbAXmOghRDdbd3BjoNRckOtH6N5y28J3ez9FHKG-51YcYG6ROlKr9KvaqopdSFrSj3rlzL00Z5Y7FvvdLJi3c0bQdKLQsjttWPZsEiAq-HcyMcy1r_VixPXTdmlHUgq5mUvEvns_qhS_KSIhKdBhh-HkV7P0H6Y5ZxrXAMdZST-wFvfSkvRji42zVHXPycOpLIWuNLyPfrGQhoLNhjvENQvUqeVX2udxhbyqhEYkdblQtJwBNEkV_ZdNnhedvNiZ278A7mMYMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94daa968c2.mp4?token=TGp11dbD_hpBkpU9xkdsOB0HKNKOR7EbrjfV1Ep7_YmfLnBi-P6vhTI8Y0_xQIWTCZP7hB50c1pHAbAXmOghRDdbd3BjoNRckOtH6N5y28J3ez9FHKG-51YcYG6ROlKr9KvaqopdSFrSj3rlzL00Z5Y7FvvdLJi3c0bQdKLQsjttWPZsEiAq-HcyMcy1r_VixPXTdmlHUgq5mUvEvns_qhS_KSIhKdBhh-HkV7P0H6Y5ZxrXAMdZST-wFvfSkvRji42zVHXPycOpLIWuNLyPfrGQhoLNhjvENQvUqeVX2udxhbyqhEYkdblQtJwBNEkV_ZdNnhedvNiZ278A7mMYMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 20-05-2026 آلية نميرا تابعة لجيش العدو الإسرائيلي في بلدة حداثا جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/75982" target="_blank">📅 12:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75981">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🌟
إعلام خليجي عن ‏مصادر رفيعة: الاتفاق المبدئي المحتمل بين إيران وأميركا سيحمل اسم إعلان إسلام آباد</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/75981" target="_blank">📅 11:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75980">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇶
انفجار لغم أرضي في منطقة الطيب بمحافظة ميسان جنوب العراق ؛ مقتل شخص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/75980" target="_blank">📅 11:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75979">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">📰
رويترز عن مصدر إيراني: طهران لم توافق على تسليم مخزونها من اليورانيوم عالي التخصيب</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/75979" target="_blank">📅 11:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75978">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">📰
إعلام إيراني: في حال الاتفاق على المذكرة سيتم إعلان انتهاء الحرب بين الولايات المتحدة وحلفائها ضد إيران وحلفائها على جميع الجبهات</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/75978" target="_blank">📅 10:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75977">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇶
أنباء عن سماع دوي انفجار في محافظة السماوة جنوب العراق دون معرفة التفاصيل.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/75977" target="_blank">📅 10:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75976">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔹
في هذه الأثناء تزور صواريخ كنجال الفرط صوتية الروسية مدينة كييف   الهجوم الروسي يندرج ضمن رد موسكو على الهجوم على بناية سكنية للطلاب في جمهورية لوغانسك التابعة لروسيا.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/75976" target="_blank">📅 10:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75975">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc1dc9836.mp4?token=tmT8R-ejnryfOpkhZBwQe2G8Nrj9JSNZDIm8RiIUxBcO0sgxDnDVbLIvGTfQ3TJSHUwJ5Qk0npIjHTudHUoZSWYvrIoGc2HirmZBYqGltNy-Kurne3dzaO-3jpB3_hTIzb9G0PZqxWq9ppNhF0KNAi9NA18Rr_4_u8275UEouCuNe-7XZV88VxGkUA70f0mnhkyzygEjShoZG0DSB3xAHMe2CUBokgmLA2SUrYP-bVc7JptYq5YqTiyFxR7ugIswesoSR_q0ethoHfCjfLQhYaH8zM5V-PWptg_zSRCU7E662Rv5fUIotd_awhT56Uxvsay8HOqkxrd9SmdSxLrjSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc1dc9836.mp4?token=tmT8R-ejnryfOpkhZBwQe2G8Nrj9JSNZDIm8RiIUxBcO0sgxDnDVbLIvGTfQ3TJSHUwJ5Qk0npIjHTudHUoZSWYvrIoGc2HirmZBYqGltNy-Kurne3dzaO-3jpB3_hTIzb9G0PZqxWq9ppNhF0KNAi9NA18Rr_4_u8275UEouCuNe-7XZV88VxGkUA70f0mnhkyzygEjShoZG0DSB3xAHMe2CUBokgmLA2SUrYP-bVc7JptYq5YqTiyFxR7ugIswesoSR_q0ethoHfCjfLQhYaH8zM5V-PWptg_zSRCU7E662Rv5fUIotd_awhT56Uxvsay8HOqkxrd9SmdSxLrjSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
في هذه الأثناء تزور صواريخ كنجال الفرط صوتية الروسية مدينة كييف   الهجوم الروسي يندرج ضمن رد موسكو على الهجوم على بناية سكنية للطلاب في جمهورية لوغانسك التابعة لروسيا.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/75975" target="_blank">📅 09:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75974">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🏴‍☠️
إعلام العدو عن مصدر إسرائيلي: الاتفاق المحتمل مع إيران سيء</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/75974" target="_blank">📅 09:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75973">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bdaad755f.mp4?token=RZYXCkoPbqBZfzn5YqwpxHRH621Xju3RbifiSOaZXAaX-QEpPKYRbqXr-ExefbmcjDRmCmYS3hHRWnFM1k2YF4CgX-zJ9rkpiG0_ju3y4isickWtlynA5m8uegUYSFIiw16f0_uU9tZkPIkloiG-7kDXgtXau-FZPw1urFxxOY2m84IL5WE9E5AZVZMr_T7SQ8K6MP6NBTxf4a6uWDfXrrkezowJo524nXWsDDOqQuLFtbYuufPup28MWog6eY6Fud_02hajYdAYJQydHbGv8DF3N5XqKAb47jEmqKnMq8VvEBKii-gXeRL7paI4nXOA__VcZhYx70s1GcD6oxVCdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bdaad755f.mp4?token=RZYXCkoPbqBZfzn5YqwpxHRH621Xju3RbifiSOaZXAaX-QEpPKYRbqXr-ExefbmcjDRmCmYS3hHRWnFM1k2YF4CgX-zJ9rkpiG0_ju3y4isickWtlynA5m8uegUYSFIiw16f0_uU9tZkPIkloiG-7kDXgtXau-FZPw1urFxxOY2m84IL5WE9E5AZVZMr_T7SQ8K6MP6NBTxf4a6uWDfXrrkezowJo524nXWsDDOqQuLFtbYuufPup28MWog6eY6Fud_02hajYdAYJQydHbGv8DF3N5XqKAb47jEmqKnMq8VvEBKii-gXeRL7paI4nXOA__VcZhYx70s1GcD6oxVCdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇰
مقتل ما لا يقل عن 20 جنديًا باكستانيًا بعد أن استهدف قطارًا يحمل أفرادًا من الجيش الباكستاني وقوات حرس الحدود في كويتا، جمهورية بلوشستان الباكستانية.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/75973" target="_blank">📅 08:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75972">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🏴‍☠️
إعلام العدو :
تتضمن مسودة مذكرة التفاهم بين الولايات المتحدة وإيران إنهاء القتال بين "إسرائيل" وحزب الله في لبنان. ووفقًا لمسؤول أمريكي رفيع، أعرب نتنياهو عن قلقه خلال محادثة مع ترامب، لكنه تقبّل موقف الإدارة الأمريكية.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/75972" target="_blank">📅 08:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75971">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEkNdnNvLrBV0i9rUQ8-DmBvybJt_khigYGRwuez0sKTktNTUWulumy8Dmw7bnCusknEcGHSSNl1QXmNNEpbDAjjRgSOviXn5P4tAwoVaLndHbWrX1XBWGe5Xu826MWVX7A5dYKDaSxPfvvwoywn6BUwT4nkBcg-ODUbAKRFOsg3DKAUDNs_FrM8zwzGaMaoG1Jd_1wdImu0QMn7sK7bxH_qarbG4Q5PlAyLOK_TpxHaB5sOsicay8Cc5QxwSrYhzHbVuBMXCTwPoP6Gr7LQc2RYSVTeFLt8zquy13mQb2QYgMyDsOfh-NFrC1z4F-t20TRPYXjSIYmKTqTV1QhnZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب يشكر الخدمة السرية بعد إطلاق نار واشتباكات قرب البيت الأبيض</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/75971" target="_blank">📅 08:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75970">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇺🇸
🇷🇺
على غرار التحذير من العراق   السفارة الأمريكية في أوكرانيا تنشر معلوماتٍ بشأن هجوم جوي محتمل كبير وتوصي السفارة، كعادتها، المواطنين الأمريكيين بالاستعداد للاحتماء فورًا في حال صدور إنذار جوي.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/75970" target="_blank">📅 01:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75969">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8ZT5ApF_DisSMLPszS7cLxdJzLOznV1aRMJzsOodH4sLH8VUOosRmneUN8G9HQ7_qSKX5pitCDm0RjA5EJQ75oGJHIlgBpRtZsvHmVKov7ll-tTVTcegV5WjST-NTM5sjsIOvfuWRnwbf52OtGOBIpO3I9E8GIDYhZCnsA-f9LCJFthR4Xtn-7d1t24u6aisOAk1wKuBdB0atE7klnn2x2YJv_LPY5dRgpYysShHtFtZjMzhRVY98BwalZiYXiuSnUc2Zs2LPqw-9kpt4DqbVFx6DSNtvG7f6HBSl8QGcchNI0BjtLGpz6WJwcflgVC_KTtAihQBCxKhaDwqlYxIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إعلام العدو : ترامب يعلن الاستسلام أمام ايران .</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/75969" target="_blank">📅 00:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75968">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇺🇸
🇷🇺
على غرار التحذير من العراق
السفارة الأمريكية في أوكرانيا تنشر معلوماتٍ بشأن هجوم جوي محتمل كبير وتوصي السفارة، كعادتها، المواطنين الأمريكيين بالاستعداد للاحتماء فورًا في حال صدور إنذار جوي.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/75968" target="_blank">📅 00:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75967">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b8d79693.mp4?token=sOgu5N4nNRwiMC95gyTzz58GGkNdWI4BFpBppG9NiVC60xiEJej5mY5GjGs6s3Hj3PgEapq4-DtKRxgtF6pW3DSMmhz7BKCq5R8v9ZWOPDOarbURKxwu4msNrAHBTd1yZ3-ArwOHzKKw_lgHM-lyY3fqPdbTVTYLFPhCuf4ak2CptLpO-HA-lgCLQkeoeS73U7SSi1cK5n-eJloKPMS7N-Gsg6dcjGPMyjR9_gbbI_UX0m3OI-gHJfoPcImBsvWbu3gKSw0mVlyQ3Ekkqqcx985b46T4aW22L_jpnhuKzCzjWBEGYqrUYt71pjJJ1p6sf2zdh_nEBK36wr9QwkXKXEOA-408rbw34BnZN243TkScK8MlP97hQ3zqsEluG6GmQemCyOZTpvtXlNzQfgKvH8uQ63tWdeQkjrvDW1F8FQkWrjz9OyMbmiHCtYdFLAWfyyRKV7Q13MHNhCvDe3LG-w-5OyO_bafRN8CLJSPihGLQ6KNqzrq1AF6v8REXVCH93LXq5HczhjY_JHHJVC7EW0V-AIqRe0DgWO3zleMRR1E1oHynnSU822eUK4C04gnjaEvafNavh_hfBecCNWf7cQTxHCMStI7lp0PpEuYJER3-i1mnIqoverYLN6aLwttS7HmbzD46fDMA_klXnH_haHYxKGX2DwHjoIA-pzuCpFI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b8d79693.mp4?token=sOgu5N4nNRwiMC95gyTzz58GGkNdWI4BFpBppG9NiVC60xiEJej5mY5GjGs6s3Hj3PgEapq4-DtKRxgtF6pW3DSMmhz7BKCq5R8v9ZWOPDOarbURKxwu4msNrAHBTd1yZ3-ArwOHzKKw_lgHM-lyY3fqPdbTVTYLFPhCuf4ak2CptLpO-HA-lgCLQkeoeS73U7SSi1cK5n-eJloKPMS7N-Gsg6dcjGPMyjR9_gbbI_UX0m3OI-gHJfoPcImBsvWbu3gKSw0mVlyQ3Ekkqqcx985b46T4aW22L_jpnhuKzCzjWBEGYqrUYt71pjJJ1p6sf2zdh_nEBK36wr9QwkXKXEOA-408rbw34BnZN243TkScK8MlP97hQ3zqsEluG6GmQemCyOZTpvtXlNzQfgKvH8uQ63tWdeQkjrvDW1F8FQkWrjz9OyMbmiHCtYdFLAWfyyRKV7Q13MHNhCvDe3LG-w-5OyO_bafRN8CLJSPihGLQ6KNqzrq1AF6v8REXVCH93LXq5HczhjY_JHHJVC7EW0V-AIqRe0DgWO3zleMRR1E1oHynnSU822eUK4C04gnjaEvafNavh_hfBecCNWf7cQTxHCMStI7lp0PpEuYJER3-i1mnIqoverYLN6aLwttS7HmbzD46fDMA_klXnH_haHYxKGX2DwHjoIA-pzuCpFI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">على الرغم من تنفيذ حكومة البحرين حملة اعتقالات كبيرة للشيعة ومنعهم من مواكب العزاء.. شيعة البحرين يكسرون القرار الجائر في ليلة استشهاد الإمام محمد الباقر (عليه السّلام).</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/75967" target="_blank">📅 00:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75966">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامب:  «أنا في المكتب البيضاوي في البيت الأبيض حيث أجرينا للتو اتصالًا جيدًا جدًا مع الرئيس محمد بن سلمان آل سعود، رئيس المملكة العربية السعودية، ومحمد بن زايد آل نهيان، رئيس دولة الإمارات العربية المتحدة، والأمير تميم بن حمد بن خليفة آل ثاني، ورئيس الوزراء…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/75966" target="_blank">📅 00:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75965">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5W4YDXubMIlikLplouywHnbMVY_sRqtwclFkjhNM-2JrXmu--5S1jJJ48EGBgoXF4Zjy3Bme3tVLcW-NcBHkvcUSJeaocfDEP836BtfEFNebTGonYnSK7CmTZofI0tv2PpSnXYkekRvFLPBFuH-QUq61p68wnJpRxdt2-_XPlqUuwArKrORHiAswuwsweGUb50m_2_d1r94uiNdng-syj0cNDfIC4g876uMcsqyD3O0oOJT9f49mG-9BC5a-ZS6MbS2WItX4AWhPfow5MrvygpQzZVPzq_3fv7QTzJVL07RbSF2ZLrGli4_BrGh7cwOtOo8UyyfoWYT0yVnQmUJJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إسماعيل بقائي: ‏
في
الفكر الروماني، كانت روما مركز العالم بلا منازع. إلا أن الإيرانيين حطموا هذا الوهم؛ فعندما زحف ماركوس يوليوس فيليبوس (فيليب العربي) شرقًا ضد بلاد فارس، لم تسفر الحملة عن انتصار روماني، بل انتهت بسلام قائم على شروط ساسانية: كان على الإمبراطور أن يرضخ!
﻿</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/75965" target="_blank">📅 00:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75964">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">انفجارات تهز الجانب الشمالي من العاصمة بغداد</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/75964" target="_blank">📅 00:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75963">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dp3ivH1kwHktatvIUBQ7X4Fl28oH0xDdFm6Z3Qig5DFmDQ-NSDxpy90dgQvoqDxlCX9NUI2iXTz1ShpbIH2DUYgQqRWiLYMEr-i-IMdwBcj54A81kL4muFxg4ZrcA4mFTOhifi3IUdfvA_xlVlJszrCL1idfNW4AoBiyab0ZgSN8bCV88xs7NeF_ayKAmxvmtDERjky2EXbMwnRxPyahJcxBcfXHYE0-kE2ZKTd6xMITdtdKEKrxSPg5WseScb0hKbDtit3FyDMBlQKHQAh2mu1f_bxHCY9cDpuBsuzKs-SQzD4Wtp3hRnG9i30Qt8D1xUfcP_tJIiPm2BjLDGtnkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب
:
«أنا في المكتب البيضاوي في البيت الأبيض حيث أجرينا للتو اتصالًا جيدًا جدًا مع الرئيس محمد بن سلمان آل سعود، رئيس المملكة العربية السعودية، ومحمد بن زايد آل نهيان، رئيس دولة الإمارات العربية المتحدة، والأمير تميم بن حمد بن خليفة آل ثاني، ورئيس الوزراء محمد بن عبد الرحمن بن جاسم بن جبر آل ثاني، والوزير علي الثوادي من قطر، والمشير سيد عاصم منير أحمد شاه من باكستان، والرئيس رجب طيب أردوغان من تركيا، والرئيس عبد الفتاح السيسي من مصر، والملك عبد الله الثاني من الأردن، والملك حمد بن عيسى آل خليفة من البحرين، وذلك بشأن الجمهورية الإسلامية الإيرانية وكل ما يتعلق بمذكرة تفاهم تتعلق بالسلام.
تم التفاوض إلى حد كبير على اتفاق، وهو بانتظار الصياغة النهائية بين الولايات المتحدة الأمريكية والجمهورية الإسلامية الإيرانية والدول المختلفة المذكورة أعلاه.
وبشكل منفصل، أجريت اتصالًا مع رئيس الوزراء بيبي نتنياهو من إسرائيل، والذي سار أيضًا بشكل جيد جدًا.
تجري حاليًا مناقشة الجوانب والتفاصيل النهائية للاتفاق، وسيتم الإعلان عنها قريبًا.
وبالإضافة إلى العديد من العناصر الأخرى في الاتفاق، سيتم فتح مضيق هرمز</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/75963" target="_blank">📅 00:03 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75962">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifKzrJA2pu3jMozGL9Nb7BC4WhFXVzzLZXoJ-xi8_5ihtxnR8OfZuV5W22czPmZ9qTbv6zupqVe8el9NrRHlBharLIswBpGoyGOzA2FahK5f1BaKjPSmt--s09dW3BWtgUCbEGGkccGga8L1JNULVRlWdTsj6rH7g4mCjWautMmOkgEqEOe7fwlcjatPjV-AnGVCf1YDl39xHpTnNsFZxB6s10NhGn02jd0CNNAcjtz6zL72fih1TJ4ltq86A-tvj3WNgXqmK-ij9NXvpWxqHpVymBqbJ2nAU8asoXCC3U9QoqM4QW7VfHVZJ_QR9RF7WFDjvNBE3HAqGYxI9L25LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائرة تزود أمريكية تطلب نداء استغاثة في سماء الأردن بعد ان انطلقت من مطار الملك حسين ..</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/75962" target="_blank">📅 00:02 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75961">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">انفجارات تهز الجانب الشمالي من العاصمة بغداد</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/75961" target="_blank">📅 00:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75960">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">انفجارات تهز الجانب الشمالي من العاصمة بغداد</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/75960" target="_blank">📅 23:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75959">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انفجارات تهز الجانب الشمالي من العاصمة بغداد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/75959" target="_blank">📅 23:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75958">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇶
استهداف مقر حزب الحرية المعارض في قضاء خليفان بمحافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/75958" target="_blank">📅 23:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75957">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">على الرغم من تنفيذ حكومة البحرين حملة اعتقالات كبيرة للشيعة ومنعهم من مواكب العزاء.. شيعة البحرين يكسرون القرار الجائر في ليلة استشهاد الإمام محمد الباقر (عليه السّلام).</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/75957" target="_blank">📅 23:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75956">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmnNULOJWMXISahrBM1vA-g_R-ifTAcJGgq-7BXzBWgm6t4nyfBl3j_eK6L7HejSo1mtsjAHFzrJrKdtx_OpOiX_uGkD1yMv2iVofU-KF8xKFs5OdsFH_ui2k0Lmp3RUR9c254BFgcWdbFN9FLtonsE_ALHDt6UY3AkuPEHpQMlUnW1iQ6tmMVygTPxoYBL1_M8SpBMXTQso7PjHB_MHgHvJt-ZRO5uCilVhDPvW4lyCtqhkH3v0lCx97zI23_cckPlXMreATdimAdOCBKtmCHWvj8M4h-cRJK7fUs05SEzKEf626V_nOcwkHXaIKtIadcCz1w4iy2DlHhv8YMdUZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال: أليكس ميلر (23 عاماً) جندي اسرائيلي يقتل نفسه بعد إصابته بصدمة نفسية حادة، وسط تصاعد الحديث داخل إسرائيل عن التأثيرات النفسية المتزايدة للحرب والخوف من هجمات المسيّرات التابعة لحزب الله.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/75956" target="_blank">📅 23:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75955">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4228c26c11.mp4?token=iKPsqGyevoC6-3o750KXtSWzNdCmVCa_noBpuvFWRKrTB9irkCYv5yWxaLhcwhUMHo5EH3lVlrJOn3wLMQYEX3v7uEjG7hMkk3QedTUz9xO3EpHqchCbpcPZnK3g8TvWnttYHScv7kym7ASAzJUeSAR1lLWWTlIcOxIcH2z7DXeuzjqPD4EOsQMybg3-2c0R1eb9DOf0SOVi9EnnXxatqLF36iwKK5KV0X7XY2s8hpPr6T31ra6X0hloK6eoA0Ev3uMyA_1Itnz13PeK6gEhhfRa7Ta7xSxep9xGm7bJHW02I4zKjtNxi-M_C0j1NFZVR-XOW03DS24kjNteXr3Kfoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4228c26c11.mp4?token=iKPsqGyevoC6-3o750KXtSWzNdCmVCa_noBpuvFWRKrTB9irkCYv5yWxaLhcwhUMHo5EH3lVlrJOn3wLMQYEX3v7uEjG7hMkk3QedTUz9xO3EpHqchCbpcPZnK3g8TvWnttYHScv7kym7ASAzJUeSAR1lLWWTlIcOxIcH2z7DXeuzjqPD4EOsQMybg3-2c0R1eb9DOf0SOVi9EnnXxatqLF36iwKK5KV0X7XY2s8hpPr6T31ra6X0hloK6eoA0Ev3uMyA_1Itnz13PeK6gEhhfRa7Ta7xSxep9xGm7bJHW02I4zKjtNxi-M_C0j1NFZVR-XOW03DS24kjNteXr3Kfoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 16-05-2026 آلية "نميرا" تابعة لجيش العدو الإسرائيلي في بلدة الطيبة جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/75955" target="_blank">📅 23:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75954">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🌟
🏴‍☠️
حدث أمني صعب يتعرض له جنود الاحتلال جنوب لبنان وطيران الإنقاذ يجلون جنود مصابين.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/75954" target="_blank">📅 22:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75953">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">📰
‏FOX NEWS: محادثة ترمب مع قادة الدول العربية كانت "إيجابية جدا"</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/75953" target="_blank">📅 22:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75952">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70dd906bcd.mp4?token=cd6rT6SUJX7QyoQ0EdtE7g0MfA1L3whzUzzGVuJGKKzb7MxPkFa5zcwPwLfbdYWMKg2KSl9PN_61jhsioqt1dk9AzwJzIJ6beTspVPxhg2DubGYjoe-GslEzaoqy8xbXXfC7k-48grDKi2uoEZAN4H9L2aq8DSvgsKL7raakwOXnW2ekk8_2lLQcR94z9juwcPtu4X_c_-H2xifV0h-CRwkklCXUhX9IelMFlNwmNtI09gnFq6cIeS4rN6IHTVF4c1Args5PUyBx33b9elPlShHQTUHZrVQ93J0Jd1GrtBWaFYnMb25Nr0h0HoN9jkYIpgDUNjLuP2NK6V9QDioPiLtlm05LgXSe9RYzyE3lbd0oje5ejgnpS1HYnf31V9Ds3qf5kRhjuO5dn9DHQeXC83OdhOI67Hq_sDXzasCtFjxnVMM1wYQWE8wz0KB-dTV2EsCZgsSjfRuZG-b1BxqiuvMp0nVCMlPCI8jBYn3_G8cvd2fQLg4iHRHb6t6GQ7yKDkuP_oNo68AyKLsyT7EH3CVC88JVlrLpnuhTCOaulCiFCWVt0kG4plQH68MoaVT1j0uEPyJFHVKemyZhrs_Pu3yDR6o0-z1sMnTgUxZE-DLbZhEYBaX4ZggXROUKIL6r7Fk8KYdXXh-Usgu7ZZJYQ_UqsGbT5XH_t0oaribJD2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70dd906bcd.mp4?token=cd6rT6SUJX7QyoQ0EdtE7g0MfA1L3whzUzzGVuJGKKzb7MxPkFa5zcwPwLfbdYWMKg2KSl9PN_61jhsioqt1dk9AzwJzIJ6beTspVPxhg2DubGYjoe-GslEzaoqy8xbXXfC7k-48grDKi2uoEZAN4H9L2aq8DSvgsKL7raakwOXnW2ekk8_2lLQcR94z9juwcPtu4X_c_-H2xifV0h-CRwkklCXUhX9IelMFlNwmNtI09gnFq6cIeS4rN6IHTVF4c1Args5PUyBx33b9elPlShHQTUHZrVQ93J0Jd1GrtBWaFYnMb25Nr0h0HoN9jkYIpgDUNjLuP2NK6V9QDioPiLtlm05LgXSe9RYzyE3lbd0oje5ejgnpS1HYnf31V9Ds3qf5kRhjuO5dn9DHQeXC83OdhOI67Hq_sDXzasCtFjxnVMM1wYQWE8wz0KB-dTV2EsCZgsSjfRuZG-b1BxqiuvMp0nVCMlPCI8jBYn3_G8cvd2fQLg4iHRHb6t6GQ7yKDkuP_oNo68AyKLsyT7EH3CVC88JVlrLpnuhTCOaulCiFCWVt0kG4plQH68MoaVT1j0uEPyJFHVKemyZhrs_Pu3yDR6o0-z1sMnTgUxZE-DLbZhEYBaX4ZggXROUKIL6r7Fk8KYdXXh-Usgu7ZZJYQ_UqsGbT5XH_t0oaribJD2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 04-05-2026 آلية لوجستية "هيمت" تابعة لجيش العدو الإسرائيلي في موقع المنارة على الحدود اللبنانية الجنوبية بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/75952" target="_blank">📅 22:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75951">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d0057e37b.mp4?token=KPIiFk6Mx4C6XP8SschmfSLbtcOYp6fu2ksfJFJASaF1EFdf-rbdF3ll8QgHQ57kdjWYCSkjDTNaD5H7cyt7UHPPVcsO-wfmPwJflyDdKeTp0iyk4mnPxMQihgKVXQiI5-Zy9c19tudxYhde4cvNJq5OsUhYYGqUi5Sk9K6bEbUl4NadTvM8XgnJbCVx3cxMsvwgTn2LKs_-g_3w8Fq3eXVLnQMk3inZ1NY0SG13bF7o-_xlZXJr4rksq0KO-OfFdv3UADnzgdq4k6N-28FCndH1bA3_RwCaP78VQenQ9UlWwfBXOkmsqgt8Qg3x6-uIAIJnHIP4gRLQViMaAnAbMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d0057e37b.mp4?token=KPIiFk6Mx4C6XP8SschmfSLbtcOYp6fu2ksfJFJASaF1EFdf-rbdF3ll8QgHQ57kdjWYCSkjDTNaD5H7cyt7UHPPVcsO-wfmPwJflyDdKeTp0iyk4mnPxMQihgKVXQiI5-Zy9c19tudxYhde4cvNJq5OsUhYYGqUi5Sk9K6bEbUl4NadTvM8XgnJbCVx3cxMsvwgTn2LKs_-g_3w8Fq3eXVLnQMk3inZ1NY0SG13bF7o-_xlZXJr4rksq0KO-OfFdv3UADnzgdq4k6N-28FCndH1bA3_RwCaP78VQenQ9UlWwfBXOkmsqgt8Qg3x6-uIAIJnHIP4gRLQViMaAnAbMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
استهداف مقر حزب الحرية المعارض في قضاء خليفان بمحافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/75951" target="_blank">📅 22:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75950">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5151e44404.mp4?token=movSvik7any8IgXn1gTE-qDJFzC6eodXfx_7_IxyfKATlHBPB7qhN85PLmcfLDTsd66dSIO6sQb_5AIrg1u-25sATKnPe1NHrklCYVAZ81pTdediNBC4Q8P78SW1nSQNL_j58uh3_-mfjY0zpqU_TuXB231s6kFLtxt42ZbsxONfa86ZSC3swY499aQnMu5tkSUrBbHvv4HCfpx_emXGhAAxnI3MaEQCPq8MiHuvm1bqvTdIuCjxVCQCNP4T5IhsBpuEysrreouNw0u78-AmLe9fvwu2hrMTiZTeyzTLcI0VO2EDfq9zjr-vErOcW4u6Ori5PA6-ZBGWZRITegH6RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5151e44404.mp4?token=movSvik7any8IgXn1gTE-qDJFzC6eodXfx_7_IxyfKATlHBPB7qhN85PLmcfLDTsd66dSIO6sQb_5AIrg1u-25sATKnPe1NHrklCYVAZ81pTdediNBC4Q8P78SW1nSQNL_j58uh3_-mfjY0zpqU_TuXB231s6kFLtxt42ZbsxONfa86ZSC3swY499aQnMu5tkSUrBbHvv4HCfpx_emXGhAAxnI3MaEQCPq8MiHuvm1bqvTdIuCjxVCQCNP4T5IhsBpuEysrreouNw0u78-AmLe9fvwu2hrMTiZTeyzTLcI0VO2EDfq9zjr-vErOcW4u6Ori5PA6-ZBGWZRITegH6RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
استهداف مقر حزب الحرية المعارض في قضاء خليفان بمحافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/75950" target="_blank">📅 22:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75949">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74f4151d37.mp4?token=FGrplRAb2LHszre5-6fgl8rTDu2iGWRNrz8edaOIDvRJXl3Y-jmNSwvUYKOJIFpxafXZrl-1gIVCOhSYMnclIlKHzICihjWEPXlRqQ7mD_ewaaZWV2_jkwqsG_TKhHHXBe3pwOuOCMygLoYAwd1mN6uwEhBtb5ZiVR064xBWv3g_TzoZ5PK0Ur0ocP9-YSyD5uD73BXzttjWFoaF7rGRi4eQSYociiP-VwOaHwbnBz7m-unPaiQV8-ejWPBnh07_1xPa7kSALyb8RdCS4YkxA-QcjZDr2qu1C--q4fa3f1wXkNvi3M6xWK6KbLHela-M1nGOs2toNO8E4FORVizzPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74f4151d37.mp4?token=FGrplRAb2LHszre5-6fgl8rTDu2iGWRNrz8edaOIDvRJXl3Y-jmNSwvUYKOJIFpxafXZrl-1gIVCOhSYMnclIlKHzICihjWEPXlRqQ7mD_ewaaZWV2_jkwqsG_TKhHHXBe3pwOuOCMygLoYAwd1mN6uwEhBtb5ZiVR064xBWv3g_TzoZ5PK0Ur0ocP9-YSyD5uD73BXzttjWFoaF7rGRi4eQSYociiP-VwOaHwbnBz7m-unPaiQV8-ejWPBnh07_1xPa7kSALyb8RdCS4YkxA-QcjZDr2qu1C--q4fa3f1wXkNvi3M6xWK6KbLHela-M1nGOs2toNO8E4FORVizzPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تحليق طيران حربي أمريكي فوق سماء قضاء خليفان بمحافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/75949" target="_blank">📅 21:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75948">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">واشنطن تايمز": الولايات المتحدة وإيران ستعلنان عن اتفاق سلام خلال 24 ساعة</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/75948" target="_blank">📅 21:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75947">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuhwA102uZAIT6guikVSyIZw0lmRZ1eSB1zoifKjTBbnVS5ohcZFlXDaNj3BX0LZX9PQUgqzxTb8ZOwrVnM01PKGUjav5JrqSoLitSF63eQJvvs8xbOeqv3Ord_GZCjRntzPw-rZTp_VaeLbQQs-k-aHbNXtKqpl_gMThinvL3ZqQmnENkbKYYUUe5VUZtbPdwWd9yKglRp9b-LjxE1Hn5r5zXgw-iOwIKefD4c6A8ZcOZkO_ZaHQeXKKRYghAkb1Z0zedxrbeVprK9E8u49Wci3f4zsCxfQuJmwYD0A0glU_oIs3RIz5DAd9CKG8lW0ct4gnSjGn1p9DQy98trU4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال: نوام هامبورغر، 23 عامًا، من عتليت، مقاتل في تكنولوجيا وصيانة في الكتيبة 9، قُتل جراء انفجار طائرة بدون طيار في قاعدة شمال البلاد</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/75947" target="_blank">📅 21:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75946">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAgVWQvJ3deqTjsxFawNXYQkScHynsphCP3jleHvMaykW1C7dRS2tGsSg7wDUCztQ2JvOqcMSYLgQrZTkgYKyoP-_hDI6A1uSSR4261qSd_yWibrOfln_MhjfBOQKGb1noPVkSls_l3M130y65liHA1a17Pv_D0Qe3v-N8_qepLhhe7KH9WgyrPfS6Fa4u4ARuPLTfHPp5wTCWiK6uUQByAVAdejdyaX1TmZ_CpgI6DkQKyHonMtg_IofrcUtwNqRdUvh25MFySPbpNDbu-mXLM0W1KSb0T5S5OicrXSmvjuQepCjRwdPT9dsbXGbteOT7m-7SVGhHFLT5GdsDOLlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
شكرًا لك أيها الرئيس أردوغان!
«الرئيس ترامب هو الزعيم الذي انتظره العالم لقرون - إنه لا يتحدث عن القوة فحسب، بل يجسدها.»</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/75946" target="_blank">📅 20:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75945">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">📰
رويترز عن مسؤول أمني باكستاني: يجري وضع اللمسات الأخيرة على مذكرة تفاهم لإنهاء الحرب بين واشنطن وطهران</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75945" target="_blank">📅 20:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75944">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">📰
‏مسؤولون إسرائيليون لـ أكسيوس: نتنياهو حث ترمب على استئناف الهجمات ضد إيران</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/75944" target="_blank">📅 20:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75943">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-2Xuu_Wyb5-CsN9C8jVQx0pBKkM8lyERVFgX5t0Oqe_SWOhy4wV6ql9xsY_mxJK8hPyqTnWlRno8W4zEdubW-44wbOJzBNUg0Fmt_nTIAqwZH_OrMdxnVRN9R838F3u4UAFPrQXpAm_R7BFMsyfOYzWQTn6QiQ89XScyzGhVQnZLVdBk0tTEuUrjzuJyHHQ5715-hNj1YdOup_Kbaw5ASCTKgHrb4EEnIsYxTeWWe0PJbwWFE1S-hrtQ_VQ-2xqU8s6F9vLT7tlAv83WwP6DS7vTenQp_KbO32bJUci01FbOPBWidLhB1kKMQ0wjVa1_HuCQXsndH6oldmrDDTpsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
سماع دوي انفجارات وتصاعد أعمدة الدخان في محافظة السليمانية شمال العراق</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/75943" target="_blank">📅 20:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75942">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇷
وكالة فارس عن مصدر مقرب من فريق إيران المفاوض: 3 نقاط خلافية رئيسية قائمة وإذا لم تحل فلن تجرى المفاوضات
إيران تقول إنها ستحدد السفن المسموح لها بالعبور وفق آليتها</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/75942" target="_blank">📅 19:42 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75941">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fcd1734e4.mp4?token=fF2zgBXXLZmwrKml4Xk1oN_9Ev8dEuJWIjMBpJh4E7dRX024UxHrFW7dAm5iYDhWfylzaB6FtZIauTpGPs2WqykzIIAQguQYlQXhKzmttjE55Q7JUEMSLn9nY8TPnnHy8FET8l_acULnB376mo0udsx5WRcb2X_6MhHlePXmwJJdQVQOxrWma045SefLDXhviCYAPbTXF8kCO5f9S6kI2WX2Xg8QACwtLbYan9zaEBb62tKqTLezexsQlROgi3rkFkhRLnRNf5prPmcJWcchu-opbxvD1a6-6TsxyIWvoDSRHln8czMsgGKykLnEnpqvkwDbKggmuoidvc0KFQiOGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fcd1734e4.mp4?token=fF2zgBXXLZmwrKml4Xk1oN_9Ev8dEuJWIjMBpJh4E7dRX024UxHrFW7dAm5iYDhWfylzaB6FtZIauTpGPs2WqykzIIAQguQYlQXhKzmttjE55Q7JUEMSLn9nY8TPnnHy8FET8l_acULnB376mo0udsx5WRcb2X_6MhHlePXmwJJdQVQOxrWma045SefLDXhviCYAPbTXF8kCO5f9S6kI2WX2Xg8QACwtLbYan9zaEBb62tKqTLezexsQlROgi3rkFkhRLnRNf5prPmcJWcchu-opbxvD1a6-6TsxyIWvoDSRHln8czMsgGKykLnEnpqvkwDbKggmuoidvc0KFQiOGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
العمليات المشتركة العراقية: نفذ صقور الجو الأبطال بواسطة طائرات F-16 ضربتين جويتين ناجحتين استهدفتا مضافة بداخلها مفرزة تابعة لعصابات داعش الإرهابية في وادي الشاي ضمن قاطع عمليات كركوك وقتل 4 إرهابيين وتدمير مضافة.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75941" target="_blank">📅 19:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75940">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/625c4fea23.mp4?token=Fv2puMn-_lNNs03A5CdUjgWuXH9Y-PIi_xa2AFTLs7SVca-Z4h8S_pd3BFYobx4Alji1XTqRmrYtEZrL0VJJ_Eyhy-Fi2KHClq5X1H3qJCv9dL-rrExaHrPdEBvaAFLRRrPap5F-jSMv_rhnGExIyY7gV1eT4146Th_xqWD3r5IHEv9WDBVDG1xb5qbj_He5zy6o_uZgrE99sngkE89wdiAjTlLVvLj-747YBeRt2PHF-ARo3ItHXx-_AtN5P1Rh7J2JpI7s0a8IR8Fpw7GLun_loPbs7CkoFH_gZMvNKq9KwtRaDVkN0grsX0FMUKnp2lp44LaTiZpGDyufEygRmSHqJ6bj1CMPYXXPi5ZaFF46yZG7SmTc0sU_7eTTeSDve-5SGjZ4sYmmxFvqZZaIG3JFx2Zxh1JYlRYHjIicKSdkSrQAPl19igRdsuUfi08PgGl6fyT74nJuGLm_0xnSIixoLnZ98OgEUxbQBk5exSaNqda-1Z7zYFJUXKAK6XQNUFi8miCHNEtNI_zgt0F5-sc0pdDY725dnVf8JFiTCWXLnTJNU-Aw1HlGo8EvonmM_9QcBS922P3RNGAVUzycgYM_ZSVz6wJqYvjwyAvDJAxc2-xZbwxXv3Ell-esFFkubs8YtCMYLy2yPdHVjPDk3QoX9xPcfzZN4GecBaXNXos" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/625c4fea23.mp4?token=Fv2puMn-_lNNs03A5CdUjgWuXH9Y-PIi_xa2AFTLs7SVca-Z4h8S_pd3BFYobx4Alji1XTqRmrYtEZrL0VJJ_Eyhy-Fi2KHClq5X1H3qJCv9dL-rrExaHrPdEBvaAFLRRrPap5F-jSMv_rhnGExIyY7gV1eT4146Th_xqWD3r5IHEv9WDBVDG1xb5qbj_He5zy6o_uZgrE99sngkE89wdiAjTlLVvLj-747YBeRt2PHF-ARo3ItHXx-_AtN5P1Rh7J2JpI7s0a8IR8Fpw7GLun_loPbs7CkoFH_gZMvNKq9KwtRaDVkN0grsX0FMUKnp2lp44LaTiZpGDyufEygRmSHqJ6bj1CMPYXXPi5ZaFF46yZG7SmTc0sU_7eTTeSDve-5SGjZ4sYmmxFvqZZaIG3JFx2Zxh1JYlRYHjIicKSdkSrQAPl19igRdsuUfi08PgGl6fyT74nJuGLm_0xnSIixoLnZ98OgEUxbQBk5exSaNqda-1Z7zYFJUXKAK6XQNUFi8miCHNEtNI_zgt0F5-sc0pdDY725dnVf8JFiTCWXLnTJNU-Aw1HlGo8EvonmM_9QcBS922P3RNGAVUzycgYM_ZSVz6wJqYvjwyAvDJAxc2-xZbwxXv3Ell-esFFkubs8YtCMYLy2yPdHVjPDk3QoX9xPcfzZN4GecBaXNXos" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 18-05-2026 آلية قائد اللواء 300 التابع لجيش العدو الإسرائيلي داخل ثكنة شوميرا في مستوطنة شوميرا شمال فلسطين المحتلة بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/75940" target="_blank">📅 19:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75939">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">📰
أكسيوس: ترامب يقول إنه متردد بنسبة 50/50 بشأن الاتفاق النووي مع إيران أو القنابل، وسيلتقي بالمبعوثين لاتخاذ القرار ؛ وقد يتخذ يوم الأحد
ترمب لأكسيوس: إما أن نوقع اتفاقا أو أضربهم بقوة</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/75939" target="_blank">📅 19:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75938">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">📰
إعلام إيراني: الأخبار المتداولة حول مقترح إيراني لتجميد تخصيب اليورانيوم فوق نسبة 3.6% لمدة 10 سنوات عار عن الصحة</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75938" target="_blank">📅 18:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75937">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibrWvPkBj23SfkxVYiVq3iJgpwz9MyWPLMLcJEQYxIxdQLB2x1sPe1QTZYHZQ8HzQRZQMaqKHO7w95pffafa6PTs05WHIjGC3S8rWXMcPCaiX0SfbfpbRZLL3irXfNr2om1MrXMPrEY_X5P2op0rO2k2KFplciIjfGaenDwlQTrsnKFt8k8f54SogYsWXIRzt3OomZD74jvnMB2BHOSABgJsGkfEWh9aIS7dzJTcJb54YhyOFodAIns17ygPVxiu0ClpRkOx1gUEKMw4fkGNGdX4GxCEj2SrYSEmojEd33Rk1JY9JDxA85Ex0myzJTiGzaLZTVRKR-8tqyX3lJmRvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إصابة موقع عسكري في الجليل الغربي شمال الكيان بمسيرات حزب الله</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/75937" target="_blank">📅 18:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75936">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🌟
وزير الحرب الأمريكي:
طلبنا من قواتنا الانتشار في الشرق الأوسط لتحمي الأمريكيين وقواعدنا من وكلاء إيران.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/75936" target="_blank">📅 18:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75935">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🌟
حزب الله:
أبابيل المقاومة الإسلامية فوق مستوطنة شوميرا شمال فلسطين المحتلة.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/75935" target="_blank">📅 18:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75934">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQj1_D9dGB3BjaJCVHgk1JYLTmYEB71YBfuT8P8HqQU-UU-gfpVhPb8AbkiWVumCV7Huf6w3FJtinR3ZWjGXYRno-1AQGVYnR2doxTzzVWaGOkSgu-36Z5MOHG3mszEMb2IqpSu8XItwwlJicX-HhIETeSUf3sS_aRGM_Uu1XyeU_E5ZIKfvMzZTwj-U31vQ-Rzx3QnI5DH9vdHvLdHd9FuPGcPeFVaTJS4sItlZFuPwbwHkcS8kasqOAqSMbPORT7i0rPK6JONEmNY9DXzrJrF10OZbQmdIjYxuGxEfw3VM61UTF-fH-YdXBNHpVHbFWx8BwrofhOH5Qj3mWoGP4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب ينشر
: الولايات المتحدة في الشرق الأوسط.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/75934" target="_blank">📅 16:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75933">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🌟
‏
وزير خارجية فرنسا:
منع بن غفير من دخول أراضينا اعتبارا من اليوم.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/75933" target="_blank">📅 15:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75932">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljCP-8fpVMo0aCP2rEQRGElkqaz92ZXi2OAyhaajNIf3PgI_xUCPJoEOFDQ3zDQJf3TBwY_Ulc_mJMy9dKu8fc20Fy7KidX8waKVBmFLJaVIsKARRbIJL4OsfDIAAp6mriIo68aF-4r4aV1uDZ8ST_7SyNsJ3pm6by_86BLEEO9bnufir2648KjQabEZXJ6gc9EsIGezT7y0-AjE0YkbMEWj4rS3P5-s0nnGNos7pC30rkPpgT6ukI79j8aCRwNwlxhhXiNp9Ui9h4SVPCBby-sQCrZeW2vYrYZ3EcNHoBrGmlodZZ6-L6pNNAHRtO6BoICOLaM-pgaLOrlFBXQM1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">النتيجة الاولية  يونس محمود ٢٥ صوت عدنان درجال ١٠ صوت</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/75932" target="_blank">📅 15:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75931">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/315a28e845.mp4?token=ZGgVropUpUkuBsKB8sBxwtZ0jiDn4a4vMYixz_LB3UmqKBEBYr45VOdH-Ws4Nn_qqi-sOYeEdFYLBypoYh7RHV_eu1g5M7zsuItfcsBSak2_MdIvYvzctmbxFd08wriq_aPS-4jb9tNkeIb6v2vWRG2ciOAIexZvbbupryvrDmzqBLGOuqW-cRlfJE60e_L0RS1vyY0QD6fZzShNXvlr3bfae4Dcs1pet4GXoNCxFI2SSN_G6Al55cVftGno04TfenX4qcMcsRJVnNGf2Us2xvDW8yVYbXyIf2B74IOtDVNs9xFJwr-DFW0pwco35YmMbfp6I7TsKV5qnUywzFB55yiayzJwtcMb7lyBEL2RwAWM3vHA1eEdjA6R-QS7Fm9Xdy2HeBP_MIe-iKcxvZ_JnodPtWzsrzAg3_D-zuZyTEs0yJK3ixf71ZIY2APa5Ni9h1r0sswjkTXzxvbrVfZeJr4dtC4pq-2wUiYaQIgW8pI0AL2SEKqLSTgj1LhIcOZcmqYnHewj95ObU54lXMGjpGWR0v6u_nPDN_wEZibUQ_KSvqVvIvwWGGQm1MkQxyOAeWQMG6bwjLcOg9JAibh02ChTpzuH6gvC-BRG10yIucFylyA4jKUE95XuL0d0ItRCI2Va86_UgEo_qYu-5-hVag2Utj62pNCr2oLn3lwOtS4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/315a28e845.mp4?token=ZGgVropUpUkuBsKB8sBxwtZ0jiDn4a4vMYixz_LB3UmqKBEBYr45VOdH-Ws4Nn_qqi-sOYeEdFYLBypoYh7RHV_eu1g5M7zsuItfcsBSak2_MdIvYvzctmbxFd08wriq_aPS-4jb9tNkeIb6v2vWRG2ciOAIexZvbbupryvrDmzqBLGOuqW-cRlfJE60e_L0RS1vyY0QD6fZzShNXvlr3bfae4Dcs1pet4GXoNCxFI2SSN_G6Al55cVftGno04TfenX4qcMcsRJVnNGf2Us2xvDW8yVYbXyIf2B74IOtDVNs9xFJwr-DFW0pwco35YmMbfp6I7TsKV5qnUywzFB55yiayzJwtcMb7lyBEL2RwAWM3vHA1eEdjA6R-QS7Fm9Xdy2HeBP_MIe-iKcxvZ_JnodPtWzsrzAg3_D-zuZyTEs0yJK3ixf71ZIY2APa5Ni9h1r0sswjkTXzxvbrVfZeJr4dtC4pq-2wUiYaQIgW8pI0AL2SEKqLSTgj1LhIcOZcmqYnHewj95ObU54lXMGjpGWR0v6u_nPDN_wEZibUQ_KSvqVvIvwWGGQm1MkQxyOAeWQMG6bwjLcOg9JAibh02ChTpzuH6gvC-BRG10yIucFylyA4jKUE95XuL0d0ItRCI2Va86_UgEo_qYu-5-hVag2Utj62pNCr2oLn3lwOtS4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 21-05-2026 آلية هندسيّة تابعة لجيش العدو الإسرائيلي في خلّة الراج عند أطراف بلدة دير سريان جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/75931" target="_blank">📅 15:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75930">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d509ff84fd.mp4?token=Dnhnnkfv-LdS7G8-ZHLdkGpmDIozixP1IXXJqW90K8tAL_l_YGIpnz_l2j0NGUoFFm8KzMmTt2zaiAmP-UQ8i1tPoc5Y-iwEA6WfmHaKV68Azvss8f-6Ct7_6r4bO53qpOAwKMArWh_KYiERsbY-0FqMpAjDeuYc4eEmyiOFLehEF3fHp3xs3OSJRg1HfTCnJ81W-EThvqr9U47FdKBzSKBC4JuRQhqGeChbB2RIcuQucYYKZUI6DITiex28OAhuG-pVjMO-ktPEqTK_h4vq4P98YvIVoPTkfQrlW54xvYbdOmPMRRf3sSnhjEuZCBsRCbmXC-SySKUZID3zfUFYtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d509ff84fd.mp4?token=Dnhnnkfv-LdS7G8-ZHLdkGpmDIozixP1IXXJqW90K8tAL_l_YGIpnz_l2j0NGUoFFm8KzMmTt2zaiAmP-UQ8i1tPoc5Y-iwEA6WfmHaKV68Azvss8f-6Ct7_6r4bO53qpOAwKMArWh_KYiERsbY-0FqMpAjDeuYc4eEmyiOFLehEF3fHp3xs3OSJRg1HfTCnJ81W-EThvqr9U47FdKBzSKBC4JuRQhqGeChbB2RIcuQucYYKZUI6DITiex28OAhuG-pVjMO-ktPEqTK_h4vq4P98YvIVoPTkfQrlW54xvYbdOmPMRRf3sSnhjEuZCBsRCbmXC-SySKUZID3zfUFYtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
طيران مروحي كثيف فوق العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/75930" target="_blank">📅 15:23 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
