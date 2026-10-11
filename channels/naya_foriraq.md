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
<img src="https://cdn4.telesco.pe/file/nqdKgc2rCh0ws-279eWQ1AF94nGMA_w9UeBmMEw2ebjEGkJz8IztrMidtGIT1S9mXrVEfv77d4kd5NYhN3Cb8dopU6UxyCw6qV-0O2-0ix4uHN8p9YHNPRzpcqSmLj8yYLQHCo72P9MrOz1182MAlAZ1DTXpQRMnRVO_f4TWDkSlIzFgymcVRVSlebBCNPCtjBInS1mLA_2UjSqMGzuiYsTDgvDzaMrtiZELysDJrT9fOn7GfcMcSRu4HdKqvtygd95g45T57xZmuChUw9Mbj5a2fkTh6mZpWEZhxwXZ2244aqZx-yxs87bTm0xGlNUhnLQhRy7dM2_68ZV4h7Z_qQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 264K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 21:42:35</div>
<hr>

<div class="tg-post" id="msg-93301">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇸🇦
انفجارات قوية تسمع بشرقي السعودية.</div>
<div class="tg-footer">👁️ 17 · <a href="https://t.me/naya_foriraq/93301" target="_blank">📅 21:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93300">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owHb4sxaptXx-TBIyZUsnj3U3RcDCT2rEqzNR6xI_yAiQSwFlSsNtSztDj7zmOr6TylfPejwI9BmR76PDuPZdM8uG2BqwEF-aUKU2gE0Ae8pRLGoVrZbbrYFg-s6JUl-IuNwE0zi2kuUovXZd4IaOCmXvhtKz3JL_-Na5wnOAOqbqJnbWPCKjweGxB-foJ0_jLWDZV1XRS2KM2_xlXGieBTldfqUhf5H1tH4SNfYYSoZbYV8R7rrvuJFl1RerIkMaM7vGBeqFi4Ylhi8m-OYnn1ELNyYOtpGb2S9OL0IGP07q11pR4atyKh6BCkz0rNBwB2eqJueVPjvt8DQv4Z2Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الرصد اليومي لطلعات العدو الجوية التي يخرق بها السيادة العراقية.
يستمر العدو في انتهاكه الصارخ لسيادتنا الجوية، انطلاقا من قواعدهم في الأردن والاراضي المحتلة.
- طائرات (KC-135) عدد 5.
- طائرات (F16) عدد 2.
- طائرات (F35) عدد 2.
- طائرة مسيرة (MQ9) عدد 1.
طوال ساعات يوم السبت
10-10
-2026 .</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/naya_foriraq/93300" target="_blank">📅 21:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93299">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇵🇰
‏رئيس وزراء باكستان: 6 من مواطنينا أصيبوا في الاعتداء على مطار الرياض.</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/naya_foriraq/93299" target="_blank">📅 21:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93298">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇶
أنباء اولية غير موكدة تتحدث عن قصف في محيط محافظة ديالى العراقية قرب قرية قره تبه</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/naya_foriraq/93298" target="_blank">📅 21:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93297">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇶
أنباء اولية غير موكدة تتحدث عن قصف في محيط محافظة ديالى العراقية قرب قرية قره تبه</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/naya_foriraq/93297" target="_blank">📅 21:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93296">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‎أعربت السفارة الأمريكية في الرياض عن بالغ حزنها إزاء الخسائر البشرية جراء الهجوم الذي استهدف مطار الملك خالد الدولي في 10 أكتوبر، وأسفر عن مقتل مواطن أمريكي و12 شخصًا آخرين..</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/naya_foriraq/93296" target="_blank">📅 21:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93295">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03b452376b.mp4?token=V_EsqHA1cFGraXux3oIQamJGlbMxsiHC1poCoA-JxwIJ-E0ZGLpjRi8ngyOwFNs9xtGwZtcM4P65GN2YAlVSjWCBI-H0tUSu1XB8aHg_zVR07WBk8rSO6267Y_NG5rklg_2CW-tqEVGYpEbdbBiQT0ed-qbRwXh-5Qjqhssy0bPYwAJOcmGFRBvlbDyOyqBjMHC3FEg0xgVyQJys0mLalp562Yy7t471TpSeYAcEFzYCbnBz6lj5danbN_JUhlhg0lcHVQlnq9RFBo2ryU32h6CQKxF1x7IEUFvdi1wMAHvDvda9m_-yvs5GFCl2fd-B3H5ez6tFEqV7NnwgLoCBMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03b452376b.mp4?token=V_EsqHA1cFGraXux3oIQamJGlbMxsiHC1poCoA-JxwIJ-E0ZGLpjRi8ngyOwFNs9xtGwZtcM4P65GN2YAlVSjWCBI-H0tUSu1XB8aHg_zVR07WBk8rSO6267Y_NG5rklg_2CW-tqEVGYpEbdbBiQT0ed-qbRwXh-5Qjqhssy0bPYwAJOcmGFRBvlbDyOyqBjMHC3FEg0xgVyQJys0mLalp562Yy7t471TpSeYAcEFzYCbnBz6lj5danbN_JUhlhg0lcHVQlnq9RFBo2ryU32h6CQKxF1x7IEUFvdi1wMAHvDvda9m_-yvs5GFCl2fd-B3H5ez6tFEqV7NnwgLoCBMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
انفجار ناقلة نفط ثالثة بلغم بحري في مضيق هرمز.</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/naya_foriraq/93295" target="_blank">📅 20:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93294">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
أميركا ضغطت على أوكرانيا وعواصم أوروبية لوقف استهداف مصافي روسيا.</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/naya_foriraq/93294" target="_blank">📅 20:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93293">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇾🇪
🇸🇦
بيان سعودي تركي باكستاني مصري مشترك:
المطالبة بوقف الهجمات فورًا ودون شروط
🟢
.</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/naya_foriraq/93293" target="_blank">📅 20:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93291">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aAYNOznpmmh6OFQA0jj_owBdbZep0aE8RnxL326eans_RCwREnjTytU0UYadxcvS0Jv-hECmbojfFFYkwMca7GvMtPGSxdkrZFcCoXVpP5UrjMtwxr-83P251LpTLaeMN95B1WIuGRIX1lvkPKLJl4lHhVNBxxV6MiPP1AeKJkZopggdqFKhhTew_WxZQCLJCYpcOKwyBRqHm6BdwXUBzITBpxGrXAXyPjIA7oFN0kk7_TtVSGKAFVVv84kW1czlEU9qn5S81dcST4xHbMeWnWzXB6_y0RrZ6XWrFohlhZ87Ak0ICj4p9GfzdzeMwWizBVDHtrL1lF-Shew5tLSbhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sx5jNBpsxR3Ed23utpyMH_9LfL_XQ36oiCn6W1J4d7yGWxFs45tBsqLWxkyxpemh_2SnoOdd5HhP1PUS5_NgYdIy07ugCGJDNrP4IECa3Pok98iG5SB2gnnRTT8vQom6gAuPJ2aXcMCRVpcxghx6HbrUY4RPI40CkT_levn0zzr8Chpwy-Lv7JttGG88VuQUi6BcCkSBfdy4vJ3_WFMRLA7j3B-jEloU8mOElXdnHDJx2cd25VwEOkhG2OL77CZIWjMf8xyl21nTTlWRCKhmX4BoB7HSgrXP-HRlh61KcTBU8RzYmMseCCB9D4Q3EC53D8B_95PSD-fqILoLM2z3iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇸🇦
توقف حركة الطيران فوق المنطقة الشرقية و الدمام في السعودية.</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/naya_foriraq/93291" target="_blank">📅 20:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93290">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇵🇰
‏
رئيس وزراء باكستان:
6 من مواطنينا أصيبوا في الاعتداء على مطار الرياض.</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/naya_foriraq/93290" target="_blank">📅 20:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93289">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇾🇪
مشاهد طرد تحشيدات العدو السعودي التي تحاول التقدم من لحج نحو مرتفعات الوازعية وتطهير وادي شريرة والجبال المحيطة به باتجاه الشمايتين - 11 أكتوبر 2026م</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/naya_foriraq/93289" target="_blank">📅 20:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93288">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f3f134d6b.mp4?token=AqtnD2l7ySHN2WiHsmtLzArCUjb0opyMWFQimFxkkkUJ6nrxsCJqHpT-b5Ow1fcbAIi0vWlpa7f3wc2KMLUFOj8Dl10Xbmq1vtimk440CwbwadbHSPU4e1az3yzBTGDcYkV2yEXs7ZxKLiUxZwVU0tsnrDCNUfnOSmf0so1cW0XiGJPuE95McBuv-1sS7KW0uTcBk8lhtqWqTh41lr4R7-p5vhtinMCmjUgHizVWVc3bs1BLNMSKm0IfwEb1cBzel6o8PMg25Az0hm5udwh-0vyg1uiMSydhODVLXkZen9zlOPNzQrUMJkqbSbQzdhcn-I6kptxrNQPf9JWe8YCPnDylyGvJaw9WMHjpw0sPznjoRmZbraFWKu17ykxjNr7a8Zc5TSikx8oJ5h0LiZgR3ZRPI4LWfe4sUPPSo4TuY5q2T3raCMbOsTcxjxVF3ZszfMpScYwY_mC8SRcsxCHcuH5OZpePwbZI48wSqpYD4ZS3K1rxTcx0l5hZrCgPdBd7Zk4dNSkSNFuRFxG1fdhHh_B-AQh6jbry6RkeW-pKpXuGSL5HloowmfusyZzhNUXkknCA4xZShwcTfoYYR5TDgmxrMU64oM19iVZfcJ8atj4AW1PvbZgsbjvKOJyoFFV6FRa2TSKfsnZmQEO1iBTJalBeDi1hq0z6NygjIfuoQR8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f3f134d6b.mp4?token=AqtnD2l7ySHN2WiHsmtLzArCUjb0opyMWFQimFxkkkUJ6nrxsCJqHpT-b5Ow1fcbAIi0vWlpa7f3wc2KMLUFOj8Dl10Xbmq1vtimk440CwbwadbHSPU4e1az3yzBTGDcYkV2yEXs7ZxKLiUxZwVU0tsnrDCNUfnOSmf0so1cW0XiGJPuE95McBuv-1sS7KW0uTcBk8lhtqWqTh41lr4R7-p5vhtinMCmjUgHizVWVc3bs1BLNMSKm0IfwEb1cBzel6o8PMg25Az0hm5udwh-0vyg1uiMSydhODVLXkZen9zlOPNzQrUMJkqbSbQzdhcn-I6kptxrNQPf9JWe8YCPnDylyGvJaw9WMHjpw0sPznjoRmZbraFWKu17ykxjNr7a8Zc5TSikx8oJ5h0LiZgR3ZRPI4LWfe4sUPPSo4TuY5q2T3raCMbOsTcxjxVF3ZszfMpScYwY_mC8SRcsxCHcuH5OZpePwbZI48wSqpYD4ZS3K1rxTcx0l5hZrCgPdBd7Zk4dNSkSNFuRFxG1fdhHh_B-AQh6jbry6RkeW-pKpXuGSL5HloowmfusyZzhNUXkknCA4xZShwcTfoYYR5TDgmxrMU64oM19iVZfcJ8atj4AW1PvbZgsbjvKOJyoFFV6FRa2TSKfsnZmQEO1iBTJalBeDi1hq0z6NygjIfuoQR8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
بيانٌ صادرٌ عن القواتِ المسلحةِ اليمنيةِ بسمِ اللهِ الرحمنِ الرحيمِ قالَ تعالى: {فَمَنِ اعْتَدَى عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَى عَلَيْكُمْ} صدقَ اللهُ العظيم  ردًّا على العدوانِ السعوديِّ الغاشمِ الذي يستهدفُ بلدَنا وشعبَنا والذي شنَّ…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/93288" target="_blank">📅 20:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93287">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇷🇺
🔻
‏ فايننشال تايمز : مسؤولين من خمس وكالات استخبارات أوروبية يقولون إن روسيا توسع نطاق مخططات الاغتيال ضد المسؤولين التنفيذيين في قطاع الدفاع، وخاصة موردي الطائرات بدون طيار لأوكرانيا.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/93287" target="_blank">📅 19:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93286">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">الله اكبر
🇸🇦
تفعيل الدفاعات الجوية في مطار الرياض.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/93286" target="_blank">📅 19:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93285">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇾🇪
بيانٌ صادرٌ عن القواتِ المسلحةِ اليمنيةِ
بسمِ اللهِ الرحمنِ الرحيمِ
قالَ تعالى: {فَمَنِ اعْتَدَى عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَى عَلَيْكُمْ} صدقَ اللهُ العظيم
ردًّا على العدوانِ السعوديِّ الغاشمِ الذي يستهدفُ بلدَنا وشعبَنا والذي شنَّ خلالَ الـ24 ساعةً الماضيةَ 124 غارةً جويةً استهدفَ بها العاصمةَ صنعاءَ ومحافظاتِ تعزَ ومأربَ والجوفَ وحجةَ والحديدةَ وصعدةَ ليبلغَ إجمالي غاراتِه منذُ بدءِ التصعيدِ على بلدِنا 2058 غارةً جويةً ارتكبَ بها مجازرَ كبيرةً بحقِّ أبناءِ شعبِنا جلُّ ضحاياها من النساءِ والأطفالِ.
نفذتِ القواتُ المسلحةُ بعونِ اللهِ تعالى خلال 24 ساعة الماضية أربع عمليات نوعية بعددٍ من الصواريخِ الباليستيةِ والمجنحةِ والطائراتِ المسيرةِ الأولى استهدفت مطارَ الملكِ خالدٍ في الرياضِ على ثلاثِ مراحلَ منذ مساءِ أمسِ الأول وأدت إلى تعطلِ حركةِ الملاحةِ في المطارِ وإغلاقِه بشكلٍ كاملٍ.
والعمليةُ الثانية استهدفت محطة شقدم الغازية التابعة لشركة أرامكو في المنطقةِ الشرقيةِ وكانتِ الإصابةُ دقيقةً بفضلِ اللهِ وأدت إلى نشوبِ حرائقَ كبيرةٍ في الموقعِ المستهدفِ.
العمليةُ الثالثةُ استهدفت معملَ أرامكو تناجيب النفطيِّ في المنطقةِ الشرقيةِ وكانتِ الإصابةُ دقيقةً بفضلِ اللهِ وأدت إلى نشوبِ الحريقِ فيها
العمليةُ الرابعةُ استهدفت مطارَ الملك فهد بالدمام وكانت الإصابةُ مباشرةً وأدتْ إلى تعطلِ حركة الملاحة في المطار.
وفي سياقٍ آخر نفذت قواتُنا المسلحةُ عمليةَ استهداف نوعيةً استهدفت تحشيدات العدو السعودي في منطقةِ رأسِ العارة والسقيا بستةِ صواريخَ بالستيةٍ وطائرتينِ مسيرتينِ وكانتِ الإصابةُ دقيقةً بفضلِ الله وخلفت عشراتِ القتلى والجرحى في صفوفهم.
فيما تصدت قواتُنا المسلحةُ لعددٍ من التشكيلاتِ الحربيةِ السعوديةِ بعددٍ كبيرٍ من الصواريخِ أرض جو محليةِ الصنعِ وتم إجبارُها على التراجع بفضل الله.
نُجَدِّدُ تحذيرَنا لكافةِ الشركاتِ العالميةِ وجميعِ الخبراء والموظفين والعاملين والمسافرينَ من كلِّ دولِ العالمِ من مغبةِ تسييرِ الرحلاتِ باتجاهِ المطاراتِ السعوديةِ فإنها غيرُ آمنةٍ باستثناءِ مطاراتِ وأجواءِ المناطقِ المقدسةِ في مكةَ المكرمةِ والمدينةِ المنورةِ.
إنَّ القواتِ المسلحةَ اليمنية ستواصلُ عملياتِها بشكلٍ متصاعدٍ تجاهَ العمقِ السعوديِّ وأنها مستمرةٌ في تثبيتِ معادلةِ الحصارِ بالحصارِ والتصعيدِ بالتصعيدِ واستهدافِ التحشيداتِ التابعةِ للعدوِّ السعوديِّ حتى وقفِ العدوانِ وإنهاءِ الحصارِ عن شعبِنا العزيزِ.
واللهُ حسبُنا ونعمَ الوكيلُ، نعمَ المولى ونعمَ النصيرُ.
عاشَ اليمنُ حراً عزيزاً مستقلاً،
والنصرُ لليمنِ ولكلِّ أحرارِ الأمةِ.
صنعاءُ، 30 ربيع الثاني 1448هـ
الموافقُ 11 أكتوبر 2026م.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/93285" target="_blank">📅 19:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93284">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇸🇦
سماع دوي انفجارين جديدين في الرياض</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/93284" target="_blank">📅 19:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93283">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇸🇦
سماع دوي انفجارين جديدين في الرياض</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/93283" target="_blank">📅 19:27 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93282">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">السفارة السعودية بالكويت: توفير حافلات لنقل المواطنين الراغبين في العودة إلى الرياض ممن أُلغيت رحلاتهم، شريطة وجود حجز سفر ملغي.  سيكون التجمع في مبنى السفارة بمنطقة الدعية الساعة 11:30 صباحًا والمغادرة الساعة 1:00 ظهرًا يوم غد الاثنين 12 أكتوبر.  بدري على…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/93282" target="_blank">📅 19:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93281">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">الله اكبر
حرس الثورة يطلق رشقات صاروخية تجريبية الان داخل ايران …</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/93281" target="_blank">📅 18:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93280">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اعمدة الدخان تتصاعد من مطار الرياض الدولي</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/93280" target="_blank">📅 18:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93279">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اعمدة الدخان تتصاعد من مطار الرياض الدولي</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/93279" target="_blank">📅 18:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93278">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee20290170.mp4?token=XDBWF9QbvTAaydRMre0FpArWIZp2MP-BB5FMqaWJaPyO34naRzTty6VFPsgO76tXVgL80H2ZpQOtI1tQ_JOFcHMQwGvsh2Edu-Y9Q3njjJszC2ycsWT99frw0dxF87I0D6yltkop3OTUFX7OuUxdE8jT_2cvjtNQI3CxWb2kHEohRTOmOKS_pmPvPN3aG1tBhogdo0UpkFx7ywBQ1k81NVCxfvnZy-LK62cLI14apYSXJ0lcoj1on45jelptvWhHgx0XsgVdGNk7-fsxYmFjC5iW-7-8U11q0ELOjsPgm_C2JZp3El5JhjHS0FPFGSnTI2Dg_TodMM9RXwr8edj41w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee20290170.mp4?token=XDBWF9QbvTAaydRMre0FpArWIZp2MP-BB5FMqaWJaPyO34naRzTty6VFPsgO76tXVgL80H2ZpQOtI1tQ_JOFcHMQwGvsh2Edu-Y9Q3njjJszC2ycsWT99frw0dxF87I0D6yltkop3OTUFX7OuUxdE8jT_2cvjtNQI3CxWb2kHEohRTOmOKS_pmPvPN3aG1tBhogdo0UpkFx7ywBQ1k81NVCxfvnZy-LK62cLI14apYSXJ0lcoj1on45jelptvWhHgx0XsgVdGNk7-fsxYmFjC5iW-7-8U11q0ELOjsPgm_C2JZp3El5JhjHS0FPFGSnTI2Dg_TodMM9RXwr8edj41w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تتصاعد من مطار الرياض الدولي</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/93278" target="_blank">📅 18:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93277">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">قتلى واصابات في الموقع</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/93277" target="_blank">📅 18:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93276">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">استهداف المبنى رقم 4 في مطار الرياض</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/93276" target="_blank">📅 18:02 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93275">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انفجارات تهز مطار الرياض</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/93275" target="_blank">📅 18:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93274">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">انفجارات تهز مطار الرياض</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/93274" target="_blank">📅 18:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93273">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بيان مهم للقوات المسلحة اليمنية للإعلان عن عدد من العمليات العسكرية النوعية داخل العمق السعودي وعمليات أخرى، في تمام الساعة السابعة مساء اليوم</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/93273" target="_blank">📅 17:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93272">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامب: اعتبارًا من الآن، هناك وقف لإطلاق النار في قطاع الطاقة بين روسيا وأوكرانيا. وقد اتفق الطرفان على ذلك. لا تخرقوه! شكرًا لاهتمامكم بهذا الأمر.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/93272" target="_blank">📅 17:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93271">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spBQVIJDmrxqJGwWOotm8H4dSQmEArEUynxKXNtavW9-Alj44NGvdd16X-juUk8_T236fcmpWtGaxhRpzft8BoD-6eEHpijdmQSv7Bew4NPbs1An4BG2U80k-js45c3H9xMEBq3jkSdIPs_fjgVTQ0trUpaCXtqBvGnCqDCl3x05HZbPhRsI586e4ylPTHTFDtvBsjpo9kVo5Z7CzhFxJR0mXv4UNY3LIMRZOsiYsyFZA6tRocelEU4bIK9m-MhkAdIAjpm8a52mDF83U1KA-GoWCOf1AILcRWyiU5591xcav1GIAPvlFTs3BAvXcwNBpEE3yBw8fdLC-a345mEyrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب: اعتبارًا من الآن، هناك وقف لإطلاق النار في قطاع الطاقة بين روسيا وأوكرانيا. وقد اتفق الطرفان على ذلك. لا تخرقوه! شكرًا لاهتمامكم بهذا الأمر.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/93271" target="_blank">📅 17:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93270">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a384cde92b.mp4?token=MCFZMPG-f5hr61OycHMLQneIHOO1HWiCBbATZGMFbWY1-PKNsRuTgwURqT6cIhH7Ygfrw_vmWT2m-MtyHhuLp1LuW62cNLIZnBhytprMjdeulfzwOsTdubQsTPgYz5sfaAxQPvfjAOegmvtSzovfFzshD7Q1CuDbzldo7n26rz9L4JVxclbuw9WQpnc6rqL4vbjnMl_fX9lOu5qh07NVyLQfyG7pTnbIX43k_edMKVGi6tM4ySG0xhfHhSWF1ZSoIPuUhz4_8mn9kzd8EWugdGzscHt5k1shy4eOZ3xG4zTTVPM-so71o4VwbQ9QPjOHgdQSx6Yb0qt5EJpZPJTm6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a384cde92b.mp4?token=MCFZMPG-f5hr61OycHMLQneIHOO1HWiCBbATZGMFbWY1-PKNsRuTgwURqT6cIhH7Ygfrw_vmWT2m-MtyHhuLp1LuW62cNLIZnBhytprMjdeulfzwOsTdubQsTPgYz5sfaAxQPvfjAOegmvtSzovfFzshD7Q1CuDbzldo7n26rz9L4JVxclbuw9WQpnc6rqL4vbjnMl_fX9lOu5qh07NVyLQfyG7pTnbIX43k_edMKVGi6tM4ySG0xhfHhSWF1ZSoIPuUhz4_8mn9kzd8EWugdGzscHt5k1shy4eOZ3xG4zTTVPM-so71o4VwbQ9QPjOHgdQSx6Yb0qt5EJpZPJTm6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من مطار الرياض الدولي بعد ان احتضن الصاروخ اليمني بكل حب.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/93270" target="_blank">📅 17:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93269">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇱
نتن ياهو:
أدين بأشد العبارات الممكنة الهجوم الإرهابي المروع على مطار الرياض. ‏يستهدف الإرهاب الأبرياء ويسعى إلى نشر الخوف وعدم الاستقرار. يجب مواجهته بحزم.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/93269" target="_blank">📅 17:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93268">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وسائل اعلام فلبينية: ‏إصابة أربعة فلبينيين في الهجوم على مطار الرياض.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/93268" target="_blank">📅 17:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93267">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇵🇰
باكستان:
إصابة ستة من مواطنينا في الهجوم على مطار الرياض الدولي.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/93267" target="_blank">📅 17:27 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93266">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">انفجار يهز الرياض</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/93266" target="_blank">📅 17:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93265">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">انفجار يهز الرياض</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/93265" target="_blank">📅 17:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93264">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">السفارة الأسترالية في السعودية لمواطنيها في الرياض: ابقوا في منازلكم</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/93264" target="_blank">📅 16:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93263">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IK2wpqHD8VrgW-HLaimSaShpliFcg9pGbZ8zBWcvM5tJK29DqnhfXwAiAuTlFUkgbKJfRNW3CbIN-FqfmK1FjCqJhVi8SFBCddN1M-8E9-at116W_6_dFWTpU5dAfAQ8kXZ_vNFTz84VPRl8htWyhFKsZSXMcRNUvDWcz-t8mi_QX8dK-KoV5OU89SHJwiu6EnxTyK0FVY4vKInQq5iJHLh5nSJeodNxOQ6PoOmySByzE2NeTPNbXnab9xU2kxLZtRsMIPlJnOofwKXbwh4NBp3mTcgcF3lKjHcxkmkn4L05RJqv-HgpF9GkLkmfbWaEczUoK4wN-WWM17gMJTS0fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">القوات المسلحة اليمنية تبدأ بموجة جديدة من الهجمات على السعودية</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/93263" target="_blank">📅 16:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93262">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">القوات المسلحة اليمنية تبدأ بموجة جديدة من الهجمات على السعودية</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/93262" target="_blank">📅 16:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93261">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adee9d62dc.mp4?token=SHjD3150OGYu0hRMKU4uD3o1xQEJzPHhtNb7EEf_akgVdwgoFU5-qQR3FAXO9uoAAM6TKdmMAvw33hBOvHcNSKkL08rs067XU_GZhXWzgXk_Oh6nxp7vGb_Dh_uOsa040PekokYMK-x3_pZdZzzZKiUCtioldM-8KISmHUowqKaglECmzjZhKZhN0Aii6b99xPW1ezgU-zbPYlxMnIEWSEWpsWi6WT5IYP8XAJgMRa-dQs3-nOTgSS-baELQDK-ydGekaHQGSlBJnI3KXkMAwtDBU2kVqfvYuz2o-hVlz5X_4Pg-aqZdftkPd6db7Jw3Ku4paMj79UVZLNmeNNWP6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adee9d62dc.mp4?token=SHjD3150OGYu0hRMKU4uD3o1xQEJzPHhtNb7EEf_akgVdwgoFU5-qQR3FAXO9uoAAM6TKdmMAvw33hBOvHcNSKkL08rs067XU_GZhXWzgXk_Oh6nxp7vGb_Dh_uOsa040PekokYMK-x3_pZdZzzZKiUCtioldM-8KISmHUowqKaglECmzjZhKZhN0Aii6b99xPW1ezgU-zbPYlxMnIEWSEWpsWi6WT5IYP8XAJgMRa-dQs3-nOTgSS-baELQDK-ydGekaHQGSlBJnI3KXkMAwtDBU2kVqfvYuz2o-hVlz5X_4Pg-aqZdftkPd6db7Jw3Ku4paMj79UVZLNmeNNWP6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من الهجوم الذي استهدف مطار الرياض الدولي</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/93261" target="_blank">📅 15:36 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93260">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11c03a534.mp4?token=ayiwHBW21CQkWROc8E7LWMMVEsRtqy0Izvm8Uj3YMETbQN2E3Xnm7lSJ7NAeBvHF6Dqm3cJ1LpFTM1ic_j75m0_uMK75ufVHkJW63QCujo3x3pGp8NommZ0mTpvA7l7WZcjPJQI7Qct02MLwLGuoP5I31vSlueO1auoaQEEUQf8VcDMGI34U1m5PD316b3V77uQ3FJV_DfM6shIv0U4mijTGOzmByFtwIsTdaOTYZaZhzE5aqRZ6ZWAadSnweX3OiGtd8iCI5DApjuIco7h4Vi6byWDkJTFVUqPkwkdvTsea8DRwibXc056HcDLMPIRahCBirQVPVO9C-VE-wpYyzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11c03a534.mp4?token=ayiwHBW21CQkWROc8E7LWMMVEsRtqy0Izvm8Uj3YMETbQN2E3Xnm7lSJ7NAeBvHF6Dqm3cJ1LpFTM1ic_j75m0_uMK75ufVHkJW63QCujo3x3pGp8NommZ0mTpvA7l7WZcjPJQI7Qct02MLwLGuoP5I31vSlueO1auoaQEEUQf8VcDMGI34U1m5PD316b3V77uQ3FJV_DfM6shIv0U4mijTGOzmByFtwIsTdaOTYZaZhzE5aqRZ6ZWAadSnweX3OiGtd8iCI5DApjuIco7h4Vi6byWDkJTFVUqPkwkdvTsea8DRwibXc056HcDLMPIRahCBirQVPVO9C-VE-wpYyzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تواصل التصاعد من مطار الدمام الدولي في السعودية بعد ضربات القوات المسلحة اليمنية ووفق معادلة المطار بالمطار.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/93260" target="_blank">📅 14:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93258">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7bd81ef52.mp4?token=uGuCSKhglEHHgQo8Yz7F_6A65U36PufKRovrpQL-USiqyFRQjMDArpqP6DzP5Vp1bfdZmR8IvSHZF8-bC4-H00_iYMM8Kvg5EjmtJQujy4z2EhuIxc0-WPGPPm5WP1HVkC2jGjDFxryM2ilTOTawbgyvUzR9PtNeyOEYVcsv4ojs4Prc91wjk7icFO1gdVxO-y7ed0XmWze2pRxUOa3V7jauuxO2TuuCNRielnr71GfQqsuZnh_hSki2n479S--EUTqmwvyNKkLqZpsa7GloTXs49CG9r-9pOAPNrYj0s4h9sMcD-U84vYmnxNlCqT5K0T8JVIUKXGpVXB_MTSUt9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7bd81ef52.mp4?token=uGuCSKhglEHHgQo8Yz7F_6A65U36PufKRovrpQL-USiqyFRQjMDArpqP6DzP5Vp1bfdZmR8IvSHZF8-bC4-H00_iYMM8Kvg5EjmtJQujy4z2EhuIxc0-WPGPPm5WP1HVkC2jGjDFxryM2ilTOTawbgyvUzR9PtNeyOEYVcsv4ojs4Prc91wjk7icFO1gdVxO-y7ed0XmWze2pRxUOa3V7jauuxO2TuuCNRielnr71GfQqsuZnh_hSki2n479S--EUTqmwvyNKkLqZpsa7GloTXs49CG9r-9pOAPNrYj0s4h9sMcD-U84vYmnxNlCqT5K0T8JVIUKXGpVXB_MTSUt9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صور القمر الصناعي التي التقطت اليوم تُظهر وجود ثقب في مبنى الركاب رقم 3 في مطار الرياض الدولي وذلك في أعقاب الهجوم الصاروخي الذي شنته القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/93258" target="_blank">📅 14:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93256">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">السفارة السعودية بالكويت: توفير حافلات لنقل المواطنين الراغبين في العودة إلى الرياض ممن أُلغيت رحلاتهم، شريطة وجود حجز سفر ملغي.
سيكون التجمع في مبنى السفارة بمنطقة الدعية الساعة 11:30 صباحًا والمغادرة الساعة 1:00 ظهرًا يوم غد الاثنين 12 أكتوبر.
بدري على الحوثي يلمس أراضيك</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/93256" target="_blank">📅 14:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93254">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d1519bbc8.mp4?token=hiWIbmC__ne144M6UDJFPBtmrYJrZgpnHNykdroVU6XzlHDCphsOW0mN8kbzEq97qbKKchHRK5PD-WFeBmNnPWQ92ENRYxY-lfpM0F-4TrQomSIfWGv51hc3NW2AmkIU-9R2D5bTm1GyroOeULXdwb2bq6cDHVw5F69UBkqLhtBpWLYszWx1Qn3cTNSy1gQZLN1OTj0VIRqb-93YwKxFJg6pyJAu-GM3k6IIkBkUz2tWoqBqWe2LRPycjFBLwJLb3Vr1WOkTjaiLO4oERNOeFqCOgc5m8H8SNLrKHIPnwnzR6FH2Bo6MORkw2EBKm3LyIl7LvK-P6AXxefEhridnGxgAPfdNOxUMoStyi3sOl9VojVinhHAJrEqTulgM0bUZYX14DY_iDLBmcOKFAH4gsalJ9EPRT1ty4LYTHsa3pAPFYSeCY5YoUp_TEk9TTwB-WyfyvyXV_9JqLyfFUpXA3oxThZ0ZDrfsKwtU9kN22zMKJZALT0renzX7kDNz0IaVoV3u5_QlSw84GQleKde4GZPHor6zzR7mz0imQ5kaU37qQ3_n_RDoMmTcIo2BqHe52K0FN5Wobj2x1xZMwNEyns1PU9DeyOue6FVWgp4k47em1UIhw7uRjrKOmz3d5PCKual5DT1o27edS91m8ChP22A-HgDLATaFeiaH7UAE_Wk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d1519bbc8.mp4?token=hiWIbmC__ne144M6UDJFPBtmrYJrZgpnHNykdroVU6XzlHDCphsOW0mN8kbzEq97qbKKchHRK5PD-WFeBmNnPWQ92ENRYxY-lfpM0F-4TrQomSIfWGv51hc3NW2AmkIU-9R2D5bTm1GyroOeULXdwb2bq6cDHVw5F69UBkqLhtBpWLYszWx1Qn3cTNSy1gQZLN1OTj0VIRqb-93YwKxFJg6pyJAu-GM3k6IIkBkUz2tWoqBqWe2LRPycjFBLwJLb3Vr1WOkTjaiLO4oERNOeFqCOgc5m8H8SNLrKHIPnwnzR6FH2Bo6MORkw2EBKm3LyIl7LvK-P6AXxefEhridnGxgAPfdNOxUMoStyi3sOl9VojVinhHAJrEqTulgM0bUZYX14DY_iDLBmcOKFAH4gsalJ9EPRT1ty4LYTHsa3pAPFYSeCY5YoUp_TEk9TTwB-WyfyvyXV_9JqLyfFUpXA3oxThZ0ZDrfsKwtU9kN22zMKJZALT0renzX7kDNz0IaVoV3u5_QlSw84GQleKde4GZPHor6zzR7mz0imQ5kaU37qQ3_n_RDoMmTcIo2BqHe52K0FN5Wobj2x1xZMwNEyns1PU9DeyOue6FVWgp4k47em1UIhw7uRjrKOmz3d5PCKual5DT1o27edS91m8ChP22A-HgDLATaFeiaH7UAE_Wk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رحلات جوية هندية كانت متجهة الى الرياض تعود ادراجها الى الهند بسبب اغلاق مطار الرياض من قبل القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/93254" target="_blank">📅 14:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93253">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuCaYjbLsG2iiRDdqjYQuFpdk1WKYA4ldI4RuY8FGsRDTzVodK0k6YyKIwHWRfV4B4ZzpckC1m-WnsPfZmepJR_sFO4meEW1cYxGGx8g7OG9shByLE8Qj4AVb8rCDSybQjypFKzdoZlIT0Jx7CBiRHr4FMJJTRVby-YKXVhDtwmxabCg_sYDC3zT91L_Fns3O2I_A0pDoO3v4J5dqqLg3Hq7UYVHSYXZwPOxK3P0R0JvQDrzy88MTypbfyfeubVoRXrPsV8S_kuqoZPFbW6xP70MCRrrPAoEU2a4hi8BIPP0lUCVJ6wbNPcarTPVOYpSFqTfOWZnZdwqUU7jQFqtrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">القوات المسلحة اليمنية تسيطر على مناطق الصياحي وسوق المقاهي وأجزاء من وادي الضباب وتنشر قواتها على طريق الدخول إلى مدينة تعز. تم قطع طريق تعز-الميسرة أيضًا، ولم يعد لدى المرتزقة أي وسيلة لتوصيل الإمدادات والمساعدات إلى جبهتي الميسرة والنجد القاسم الا عن طريق جبل صابر وهذا مستحيل</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/93253" target="_blank">📅 14:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93252">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6251092052.mp4?token=PkSLAGfh7FUsPS6oXr6FwboyVpJvVcarBOFN7c2YdiWDzkdNQ3HBggyk5dCfLjjwJexJymXnlYKepWjEy3jK99T9JbzB4M8TLGINpbBsFjTQUe2V71ACvV8c21Q3J_7QlT6WdNxEC_QnKl4y7KTWyBnQsVIrtPexjvoMGnI6w5OY0EaiuCkT5ko3QLHfuh_oesdgUrea06s-b4ze-ABzki7PkEwsEkkd_RD_rTqqHwZibTPTeeaZwqnQjD4k30Wf3DdSRdBd5vvFELDxt38v_7k_AbrgjU9Dw0YEQBE4H5YRBzLFhlUz2AABhVkeWoQ7jFIiDtcOfRa3wiJ4FTD88g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6251092052.mp4?token=PkSLAGfh7FUsPS6oXr6FwboyVpJvVcarBOFN7c2YdiWDzkdNQ3HBggyk5dCfLjjwJexJymXnlYKepWjEy3jK99T9JbzB4M8TLGINpbBsFjTQUe2V71ACvV8c21Q3J_7QlT6WdNxEC_QnKl4y7KTWyBnQsVIrtPexjvoMGnI6w5OY0EaiuCkT5ko3QLHfuh_oesdgUrea06s-b4ze-ABzki7PkEwsEkkd_RD_rTqqHwZibTPTeeaZwqnQjD4k30Wf3DdSRdBd5vvFELDxt38v_7k_AbrgjU9Dw0YEQBE4H5YRBzLFhlUz2AABhVkeWoQ7jFIiDtcOfRa3wiJ4FTD88g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المناورات الصاروخية لحرس الثورة متواصلة في الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/93252" target="_blank">📅 14:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93251">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7d1b89e70.mp4?token=ClisKgVlHSzEeP8YohzXG1YoEttImITerI3PNbemCttlNcvbFp4W9Cg7_UKOADaL4j_6se6JGNZ0mhuDue282UR3hYbCRHVoC8pOsMHDNvHpzpOW0V-n5e1WqDqIi791ypQ2rQcIaiLzwsff2C5hsftuAECWdyOAtl9emax4KgLIUT2GqoN0G6HgdGn_0bXpfxU3wyLROu4wQBkU7e5J9dY2HCsUwouHWOjW-I4qh9ixZ4leoZK_lKnLt0TAui42lUvjzRcaANMsW1n60EWFwvum1HHzHNqJjC_EjJOHZr9fyuOCd5g7tNmUxleRWKCEh2hRksbuwr52pzt324a0bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7d1b89e70.mp4?token=ClisKgVlHSzEeP8YohzXG1YoEttImITerI3PNbemCttlNcvbFp4W9Cg7_UKOADaL4j_6se6JGNZ0mhuDue282UR3hYbCRHVoC8pOsMHDNvHpzpOW0V-n5e1WqDqIi791ypQ2rQcIaiLzwsff2C5hsftuAECWdyOAtl9emax4KgLIUT2GqoN0G6HgdGn_0bXpfxU3wyLROu4wQBkU7e5J9dY2HCsUwouHWOjW-I4qh9ixZ4leoZK_lKnLt0TAui42lUvjzRcaANMsW1n60EWFwvum1HHzHNqJjC_EjJOHZr9fyuOCd5g7tNmUxleRWKCEh2hRksbuwr52pzt324a0bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
إطلاق سرب مكوّن من خمس طائرات مسيّرة من طراز شاهد-136 خلال مناورات الحرس الثوري
🚀
شلیک یک اسکادران از پهپاد شاهد ۱۳۶ در رزمایش‌های سپاه پاسداران انقلاب اسلامی
@Naya_Press</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/93251" target="_blank">📅 14:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93250">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇾🇪
وزارة الخارجية اليمنية:
على أصحاب البيانات والإدانات مدفوعة الثمن دفع النظام السعودي للكف عن عدوانه</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/93250" target="_blank">📅 14:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93249">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇷🇺
🇸🇦
🇾🇪
🔻
مصدر امني لنايا
استشهد عدد وجرح عدد اخرون من المواطنين الروس نتيجة الهجوم على المراكز الحساسة ومطار الرياض في السعودية البارحة ؛ أنصار الله في اليمن أوصت الدول مرارا وتكرارا بضرورة مغادرة أبنائها وجاليتها الرياض و باقي المدن السعودية عدا مكة والمدينة المنورة كونها تتعامل مع العدو السعودي بالمثل باستهداف المدن والمطارات اليمنية .</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/93249" target="_blank">📅 14:06 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93248">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇸🇦
الاعلام السعودي:
تعذّر وصول بعثة النادي الفيصلي إلى أبها يوم السبت قبل مواجهة أبها المقررة الأحد بسبب هجمات القوات المسلحة اليمنية والامور تتجه الى تأجيل المباراة مدة 24 ساعة.
من المتوقع ان يتقدم النادي بطلب ترخيص للطيران والهبوط من مركز تنسيق العمليات الانسانية في العاصمة صنعاء والامر متروك للمختصين في صنعاء</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/93248" target="_blank">📅 14:02 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93247">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba4f94d651.mp4?token=RvVCoATx02EpHlNASY4O0IXHal0BIDUObeeyUNt34S5gNarYVzQBDrVzg7ygKdlUENUDnWmcA5r-QC0hkKgyEmDj3MzikTNQXj3dRhXRpf_s2oxpwKJ5m8-s2SGOW3-sjLT2MZLuxvkcRcddeaZIzrte0G-geh2YK2LGfb8b59770eT0TC873efS2Dq-MhIMaxmAUJiUcge4yD7L0V7SVUIY-lQ4mUVRAbGr0s7ewEzasIzJ-gNi0hesPsdtKH25VV-Q1V-fBinoY8pmZAlbxPo8gNEcq3tB-s1Kv-tSizg18PDEZWDZzYvjLxD8O3xOTl3oa7NI2Zp3WLT-rTh6mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba4f94d651.mp4?token=RvVCoATx02EpHlNASY4O0IXHal0BIDUObeeyUNt34S5gNarYVzQBDrVzg7ygKdlUENUDnWmcA5r-QC0hkKgyEmDj3MzikTNQXj3dRhXRpf_s2oxpwKJ5m8-s2SGOW3-sjLT2MZLuxvkcRcddeaZIzrte0G-geh2YK2LGfb8b59770eT0TC873efS2Dq-MhIMaxmAUJiUcge4yD7L0V7SVUIY-lQ4mUVRAbGr0s7ewEzasIzJ-gNi0hesPsdtKH25VV-Q1V-fBinoY8pmZAlbxPo8gNEcq3tB-s1Kv-tSizg18PDEZWDZzYvjLxD8O3xOTl3oa7NI2Zp3WLT-rTh6mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من المناورات الصاروخية لحرس الثورة في الجمهورية الاسلامية الايرانية  الاردن فعلت الدفاعات الجوية ظنا منها ان الصواريخ قد تتجه للكيان مؤكدة "لو يموتون جهالي اربعتهم ما اخليهن يعبرن لاسرائيل".</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/93247" target="_blank">📅 13:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93246">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇾🇪
🇾🇪
دبلوماسي بريطاني في الرياض:
‏خرجت للتو من الرياض. تلك الانفجارات السبعة التي ذكرتها في المطار أسفرت عن ثلاثة قتلى و12 جريحاً. لذا قررنا التوجه بالسيارة عبر الصحراء، فالمطار كان مكشوفاً للغاية. تعرض المطار للضرب مرة أخرى أمس. تمتلك السعودية دفاعات جوية أكثر بكثير من بريطانيا، ومع ذلك لم يكن ذلك كافياً.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/93246" target="_blank">📅 13:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93245">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d43172e017.mp4?token=VTo7Yl-ArOw_jMuBvKGgx-DbzCg9vDAdIEHlBCIZBlbv8pCeV8AlNSGJNnkuEVf1chW4UfhX1YKpYoMHRq92VBEC6eOJcavXBZT04AH3ARRYpiNdWzeJowCT9lxq6PsmX3BUyLs_ZxCrJfOoH6AzTM_QIXJhyvpfmCCRflJI7WnDoaYDFaoxztLwwM1TAQCZlWWLOw-rb9j5Z-HpKA42a23iuvR_P_hQvyQ4ScWrC7kG89LPOWiHztBOHEw51L_fHHNc8M8z5ee4zXi237M-G-_WCiuSBGHe4ZUxT4K16YUJwBQ1KRa7QZw6t0WYXf1dumv7duKWSj7lELb1jU2MTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d43172e017.mp4?token=VTo7Yl-ArOw_jMuBvKGgx-DbzCg9vDAdIEHlBCIZBlbv8pCeV8AlNSGJNnkuEVf1chW4UfhX1YKpYoMHRq92VBEC6eOJcavXBZT04AH3ARRYpiNdWzeJowCT9lxq6PsmX3BUyLs_ZxCrJfOoH6AzTM_QIXJhyvpfmCCRflJI7WnDoaYDFaoxztLwwM1TAQCZlWWLOw-rb9j5Z-HpKA42a23iuvR_P_hQvyQ4ScWrC7kG89LPOWiHztBOHEw51L_fHHNc8M8z5ee4zXi237M-G-_WCiuSBGHe4ZUxT4K16YUJwBQ1KRa7QZw6t0WYXf1dumv7duKWSj7lELb1jU2MTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
المناورات مستمرة و بقوة ...
رزمایش سپاه پاسداران با قدرت ادامه دارد ...
@Naya_Press</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/93245" target="_blank">📅 13:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93241">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r8noLoauGa0MwNQEvxPH1MJKQuOLMatnXFELL3Ed2yw2pEY2_jIJFS1xudNI3sXIim8BmpicHnRygBpgpONj3E7gmHXau0dZl-MGGjyRkw94rnVO55ZPlIM9mZMP27aRe8tKBDCqQitcFExs3dE8aQhl1F6mNbp42ckpEWWAuvoUKEwBxqY1aiCYWC-xGWe0TFRLmsVH_mcU0j4rFp8qkecsQVJjSR2tn-H-c0uTUu3R911sw4FBLoY463TF4wAT4ecApAJ1xFfeom6HtmexHtKldXof4FNgagc6EXm53dv-l9cFd1CmYoeQ8iEgTTy3uWW3VkKFMnHTenV5uf8eEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mFCr98VAu0ww3_n4nTtmajDPJquMd_rvWwDJIYIfMi0El36xccrXrMOFm6YiXGds_nLKZ7tWCLEv30Qs8W9oXnMubGmegn99Am00xMDxNDtatSDeQqvmg1o_FQAFhciFot1PYWK4Efxd4-o-w4qKxT3csFxFcNlZMF2tYhyAGpYE3aYNfj2ub-RS5Uqv-kSjJYxfT9JCsqR4TEGDoKb_16-zYoYg0vzIOYNtSS0Se1LdMQd3Lreue2txllXS01RidtIIDyqcJss2hrehIQ6zBHGG70SZuL8EWQ07Pr-8ayh23YcPEH4VajBTGn2uhNKNSIk9Gp4tHAjCbyhwGnq32A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eB4JfioNcpp8V4RxkZq8ri64C2yAUgm39NDmqKzWcw1nAugtLIrsWIR95qB5mTaOA9UbKgx-tKJNE2R6mUqhhc2BwPxDqK91ymaRNElMzZbgKH166Jw_rzMsz5QCMUQ4mjsMdoDhYvpu4x0oHRCkqJkpWqP8tEkVCd5mdCzcJ_LlQ74lKLDH5b4LcWwsx8tzGP_HsrSGGCkv7Px7txsEMSs34y7KaP0B0KHn2o61m_qEIz1TdNHBDAgAao4epa2davLy4O2yBMXLsqZDS-DUeRqfe2GZ9EG_ZkI410SrnK0zePBHZzdBCo-hW35Tvn7QP9HuOYiEKqOR-LHBoO7JIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WqI3X06qoUpeLheWxsZRVfBiI3AQuGXye88RpeiVVIH3d9e-ywFjTyaSTCjnRtgZT9t8W5fMrPn6DzcHeSQFrxkukfLJR7qCL9bS4ubj0uK49kJrv4wdmhqaAeZLhn6Jd1q4Tji4VW83Rs547L4O2eYVA_iCGieVvMCQjcy9XohB4ELbekvJ1UulJhF4iaskGjh1kN_T0q0SleSJlI8ElHgSMD90cAnNfvqT-aGClDlK2ovzTA-tOfthdbYaDFgLHqJGtnnv18fdd-UaH4vGJZ_UeGA2TsUaWDTDdVQmlGAc4uqgOl5fRnO5pg0OmoP52mzl_QY06CatBJoyYBL2EA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
من التجارب الصاروخية الذي ينفذها حرس الثورة في الجمهورية الاسلامية الايرانية.  الكويت تشعر بالقلق</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/93241" target="_blank">📅 13:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93240">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇾🇪
وزارة الصحة اليمنية:
إصابة 6 مواطنين بينهم امرأة وطفل جراء استهداف العدو السعودي منزلا في حي سكني بمنطقة باب شعوب بالعاصمة صنعاء.
لن يستنكر احد ويقول مدنيين
ولن تنشر الدول بيانات ادانة</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/93240" target="_blank">📅 13:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93239">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYvqGGR1dSsBDjz7NLRupwg7Xkki-upu01CwNgDqAArtYyXUSJypY3zl7IUigUzjfALKT7Tic173eTEa5krDkDGTGNnB7lgYuKVWoIxul3ssYSZxNOP-Y-0pbUxKGocsiC92jdF2IGN6PJF2fkYwsOVF0LysBuHXDBBpRvVNt_IB_Gy1MdzpDhNFzJL81e3BUcVLvbc-1I_Fgd1eBz84aG43oCylbka_36ZTa0Wy_PDB1hPJ6SHsvbqAdW7fvmL4GQjjpKZHQ5cTZi3rgEzXPn72Oz9fgFBuwtcBcQ44AfhyVrgzDSGYFRdp2k4mxVhs1MVzKCgv6VaSGFoThb7Awg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🔻
مصدر إيراني لنايا   الحرس الثوري أطلق قبل قليل ثلاثين إطلاقة تجريبية من الصواريخ البالستية خيبر شكن وعماد على سبيل التجربة .</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/93239" target="_blank">📅 13:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93238">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">وفاة 109 أشخاص منهم 15 طفلا  وفقدان أكثر من 116 بغرق سفينة قرب جيبوتي</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/93238" target="_blank">📅 13:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93237">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇾🇪
وزارة الخارجية اليمنية:
ما لم يكف العدو السعودي عدوانه وتدخله في اليمن فالقادم أعظم بإذن الله.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/93237" target="_blank">📅 13:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93236">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇷
🔻
مصدر إيراني لنايا   الحرس الثوري أطلق قبل قليل ثلاثين إطلاقة تجريبية من الصواريخ البالستية خيبر شكن وعماد على سبيل التجربة .</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/93236" target="_blank">📅 12:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93235">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">الله اكبر
🔻
حرس الثورة يجري مناورة واسعة بالصواريخ الفرط صوتية الان داخل ايران .</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/93235" target="_blank">📅 12:36 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93234">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Homayoun Shajarian - Iran e Man (همایون شجریان و سهراب پورناظری…</div>
  <div class="tg-doc-extra">Melodifa</div>
</div>
<a href="https://t.me/naya_foriraq/93234" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#شاركها</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/93234" target="_blank">📅 12:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93233">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الله اكبر
🔻
حرس الثورة يجري مناورة واسعة بالصواريخ الفرط صوتية الان داخل ايران .</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/93233" target="_blank">📅 12:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93232">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇾🇪
🇸🇦
القوات المسلحة اليمنية تتمكن من تحرير قرية الصياحي وسوق المقهاية واجزاء من وادي الضباب، وبذلك تم قطع خط الضباب ومحاصرة مرتزقة السعودية في نجد قسيم والمسراخ بمحافظة تعز.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/93232" target="_blank">📅 12:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93231">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔻
وزارة الداخلية البولندية:
الشرطة تلقت معلومات عن هجوم محتمل على رئيس الوزراء ووزير الدفاع.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/93231" target="_blank">📅 12:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93230">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇾🇪
دوي إنفجارات في العاصمة اليمنية صنعاء ،وسط أنباء متضاربة بين عمليات إطلاق صواريخ نحو الأهداف والمواقع المعادية من قبل القوات المسلحة اليمنية وعدوان سعودي.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/93230" target="_blank">📅 12:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93229">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇮🇶
🇸🇦
الحكومة العراقية:
نستنكر الاعتداء الذي طال مطار الملك خالد الدولي في الرياض والذي أدى إلى سقوط ضحايا أبرياء ووقوع خسائر مادية وبشرية، بما يسيء إلى الأمن والاستقرار الإقليميين.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/93229" target="_blank">📅 11:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93228">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇺🇸
البنتاغون : سيتم بث إعدام مطلق النار في فورت هود رمياً بالرصاص في الولايات المتحدة على الهواء مباشرة</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/93228" target="_blank">📅 11:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93227">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇾🇪
دوي إنفجارات في العاصمة اليمنية صنعاء ،وسط أنباء متضاربة بين عمليات إطلاق صواريخ نحو الأهداف والمواقع المعادية من قبل القوات المسلحة اليمنية وعدوان سعودي.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/93227" target="_blank">📅 11:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93225">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇾🇪
العميد يحيى سريع:
القوات المسلحة اليمنية تجدد تحذيرها لكل الشركات الملاحية الجوية والخبراء والموظفين والعاملين والمسافرين من استخدام المطارات والأجواء السعودية لأنها معرضة للاستهداف ومسرحا للعمليات من قبل قواتنا باستثناء مطاري مكة المكرمة والمدينة المنورة.
وتهيب بالجميع لأخذ تحذيراتنا على محمل الجد وتتحمل السعودية مسؤولية أي اعتراضات فاشلة. وتؤكد القوات المسلحة أنها ماضية في تثبيت المعادلات المعلنة معادلة المطار بالمطار والحصار بالحصار والتصعيد بالتصعيد حتى تحقيق أهدافها.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/93225" target="_blank">📅 10:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93224">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3s3UqnlmElU3lMDyRtJuaCVtF1vh7mN2VUEkFnjRUObJresWCbY_9gCKcBkGADpNuO8KghusOtlO7bgri3oJAX9Eb2_5uKO0sJw9J9OKOkQ8hCYzNnPkYgz4yybgldDbUK1cZcqq5bnhIB-2Csaxxi74XV484Rcu6gmIo45IfirBlanmfc89CfGqiCKl77ojOLyYtx1i7Pu1z7eram9JrP4qoO1Nmmr5gg5G7aCOZjfTelA-0zGYp0TX2i8BmYto4V0PDR2ndwsB9GZOtsLLR-H0-o09AGqXBx_TNuQFR4OD_3OW1nPvI7hNOED1ddJG_ynDxClEhkqLmme1PQASw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المعارض السعودي البارز حيدر القحطاني يتحدث عن الأوضاع المأساوية داخل السعودية في ظل أجواء الحرب وكيف ورط آل سعود البلاد وشعبها في صراع بات المواطن السعودي يدفع ثمنه من أمنه واستقراره وحياته اليومية وسط مخاوف متزايدة من القصف وتداعيات الحرب  رابط التغريدة</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/93224" target="_blank">📅 10:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93222">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OM6TtPIl19whJyCaIKKTXLMMR-kW8tm9JDDiQH0reKAYoRbta8DD3Wu36OrOMk4NeUa165T2tJUN1hXiYuNJs9Mh9IfK_jmYE4q_3aiw-K2pN41gk7LjoI1PiFQdTTuVWJi7Vxz-1OhTXlJlvhUSV8_Btbr_Z74YjZYK4pWhYDpBEECJNeYozNvsfeIbi8rKmLrYXo0ksu8ivZlOPCgtOkuTT6Prg9y5PDSQJnGZgLuQu0EKXTa4-ve2AvADfVmb0J6_5pj3HdxHwVdy7XmlcncCP6Z5j_JP5T8wfN2qFQWl-nC1LS0BCuTgB5S9XnoYwmY40xqpp67vSWnswGDZdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BsGzrjHSzPFvSIRJLWmJVJoPhQ1tbkf3eWeoZbU0un4n6BGk_R0S4FK52WnKJBvch0KXQdbAIryu__sR2TWzVMb55ZnAYSg8rCmPPdtSNaqo8x51kb1TWQCjuWfP_UGhQeXgNqhxzRJOkrE6im1dwZ-BrK9mEI1SkHOPsE9Splmp9piN9Y4XXxqEdBEHVqHFC7ZVVt6s89mFcPPlaGEZ-RRFIVSqxzcl9aeiISVueHqRYdcV9ihQ0qfMlST_yqMmFuFpva-8QDNUwg1LHxwXVA2SmgpgYjn1yiNam1lbwPXmZ6F7AZCTNCmZ_D6WIGmI6o_dtbBIYZWIFf6eyKB-FA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">المعارض السعودي البارز حيدر القحطاني يتحدث عن الأوضاع المأساوية داخل السعودية في ظل أجواء الحرب وكيف ورط آل سعود البلاد وشعبها في صراع بات المواطن السعودي يدفع ثمنه من أمنه واستقراره وحياته اليومية وسط مخاوف متزايدة من القصف وتداعيات الحرب
رابط التغريدة</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/93222" target="_blank">📅 10:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93221">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c0e97186.mp4?token=E4Y-TBWtrm3UxzodJKUUxgtW6m5zMdqvx7LBhLGQjMskbASb_jLDCekbvrrVn-tgKJGYcmHHnV-SaFOnSCzK879T3J3LRSwqLr52rAZK-mCZlNBXtvKDK9pEFcvOss3sR65qXgjnBaqV1xT5ShT26jQmLTLvGjpdPFuZg3xVmwK1LwB84CHSDDGowGWVOobVMJv7JbUTEZ4TAS6mt6MoambMcH1e1tpmKBaX1rVavNRBU7FuStthDw1GsULYpb7mt7dCuRYgxT26jUkEyyClCGhTuwZigQ7pCzIg02y_xNFwLSGUNFjPE8DCFmGdhRxJTFvg4Hd8tziHay0mQuig3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c0e97186.mp4?token=E4Y-TBWtrm3UxzodJKUUxgtW6m5zMdqvx7LBhLGQjMskbASb_jLDCekbvrrVn-tgKJGYcmHHnV-SaFOnSCzK879T3J3LRSwqLr52rAZK-mCZlNBXtvKDK9pEFcvOss3sR65qXgjnBaqV1xT5ShT26jQmLTLvGjpdPFuZg3xVmwK1LwB84CHSDDGowGWVOobVMJv7JbUTEZ4TAS6mt6MoambMcH1e1tpmKBaX1rVavNRBU7FuStthDw1GsULYpb7mt7dCuRYgxT26jUkEyyClCGhTuwZigQ7pCzIg02y_xNFwLSGUNFjPE8DCFmGdhRxJTFvg4Hd8tziHay0mQuig3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
تسلل طائرة مسيرة من جهة الحدود اللبنانية.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/93221" target="_blank">📅 09:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93220">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇺🇸
ترامب:
الهجمات ضد السعودية كانت فظيعة والسعوديون قادرون على الدفاع عن بلادهم.
لدينا اتصالات مع الحوثيين وسنرى ما سيحدث ولكن ما فعلوه كان سيئا للغاية.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/93220" target="_blank">📅 03:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93219">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/610dacafee.mp4?token=i90BeQ22TA1BDzWMTkTddk6GWgfUhtH4Ga1YTEVjOzDfZPxlOBJYUcVrWjFBZHi8P0ax4lsbfcSkbWDCJw53qX2wa8XRXSrbbMj0hPh9v2fcqx_Jr3uU4qYHOEVvgxjdguckCcn2yQraK4AGwHSbfaaf6JGqLPjc8S-bGn-WGBH6u-NLxa_34N5C4yb-CBpcUBrFNMONHAu1OtJwxeIC1mEimpitp3fLLVPE5bAPHnDAgQofR-NA56olFiJ5Q6vNwXDYkPieFAF3GIbwepHgH0cNnjx1evZ3Bn0uZUmu-Mgfh8pg80V8lGRuaWF22gpM4Yx8cug5RLyb_oIIUdbRrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/610dacafee.mp4?token=i90BeQ22TA1BDzWMTkTddk6GWgfUhtH4Ga1YTEVjOzDfZPxlOBJYUcVrWjFBZHi8P0ax4lsbfcSkbWDCJw53qX2wa8XRXSrbbMj0hPh9v2fcqx_Jr3uU4qYHOEVvgxjdguckCcn2yQraK4AGwHSbfaaf6JGqLPjc8S-bGn-WGBH6u-NLxa_34N5C4yb-CBpcUBrFNMONHAu1OtJwxeIC1mEimpitp3fLLVPE5bAPHnDAgQofR-NA56olFiJ5Q6vNwXDYkPieFAF3GIbwepHgH0cNnjx1evZ3Bn0uZUmu-Mgfh8pg80V8lGRuaWF22gpM4Yx8cug5RLyb_oIIUdbRrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الجيش الأمريكي:
قامت قوات القيادة المركزية الأمريكية بتعطيل سفينة شحن تجارية في خليج عمان، في 10 أكتوبر، بعد أن تجاهل طاقم السفينة التحذيرات المتكررة وحاول اختراق الحصار البحري المستمر ضد إيران.
‏أصابت طائرة مقاتلة عسكرية أمريكية مؤخرة سفينة الشحن "أوشن موليكا"التي ترفع علم بنما، بذخيرة دقيقة، مما أدى إلى تعطيل نظام الدفع بالكامل وكانت سفينة الشحن الكبيرة تحاول عبور المياه الإقليمية بعد أن غادرت ميناءً إيرانياً.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/93219" target="_blank">📅 03:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93218">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دوي انفجارات في المنطقة الشرقية  في السعودية إثر استهدافها بعدد من الطائرات المسيرة</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/93218" target="_blank">📅 03:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93217">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇺🇸
وزير الخارجية الأمريكية:
‏
تدين الولايات المتحدة بشدة الهجمات الأخيرة التي شنها الحوثيون الإرهابيون على المملكة العربية السعودية، بما في ذلك الهجوم الذي وقع اليوم على مطار الملك خالد الدولي في الرياض والذي أودى بحياة العديد من الأبرياء، بمن فيهم مواطن أمريكي.‏تُظهر هذه الهجمات الشنيعة استهتاراً صارخاً بأرواح المدنيين الأبرياء. يجب أن تتوقف فوراً.‏نقف إلى جانب المملكة العربية السعودية وشعبها، ونعرب عن خالص تعازينا للضحايا وعائلاتهم.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/93217" target="_blank">📅 03:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93216">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇾🇪
🇸🇦
هجوم صاروخي يمني يدك محافظة الخرج السعودية.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/93216" target="_blank">📅 01:49 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93215">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeINRjHi0mYrQuISdtxnCZpyEqW-d_-QAf8lo9G-3hTBEjICKriil8MIUde5NM8IlNnt9d5nhQvoNxFa_rNDcjbPWz_64wtWi9cZTQV_eUdzCO6B4Tholk12nZwqaWL7Wcaq4vmuz-1eKa07Y9q_WV9fQCHOycgJB14P6gG4vr84hhqL77-C8fGZpKpGsQglWARZKpgE0gYKdlg6EPlBIafiuMqYPULn1gXWpcjuoTn12nD1NOfaeTrHkuw_B5oJX4rpluAX132XO74fCLnWHPJ8BrqVRyKFPIhmDOEx6jAIPTXz2I6Hry9eq-1dRgW3-sjhh7ttI5XLVwnh-bSvEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
إستهداف ناقلة نفط بمقذوف حربي في مضيق هرمز قبالة سواحل عُمان أدى إلى إشتعال النيران فيها.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/93215" target="_blank">📅 01:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93214">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/705fd22f65.mp4?token=Zn2-cHK-Z6E1LouTW14T-Jx_5fzyKlikyqOfEcH3Q0253VCZofB1E7T9D4qAw07TM3il1hJVBp3OZLVIrLyRwF4yPxLZSCX20Xlc77D7ck_fIbYHyubJQJIFx5YNLZhE2fbJxH644U0etWulo6Ot0vPPWuz0fOUeLQyKm-qPB3ylTn0zuWo5cqMym8qIyjBzqZJ3jH4UeXFHqYkHroMtc_CtNKqaMLcLWpYOff1q9TfUPrvmjZsHvawa58Rgy33GSaLHwfdRdmkz_AsAwQKvp5N5yOoP_W7dkwJ003zVYTga6nRN8bllTqot9sQV1jpn8VGxdgaX6d3FVbKUON3iZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/705fd22f65.mp4?token=Zn2-cHK-Z6E1LouTW14T-Jx_5fzyKlikyqOfEcH3Q0253VCZofB1E7T9D4qAw07TM3il1hJVBp3OZLVIrLyRwF4yPxLZSCX20Xlc77D7ck_fIbYHyubJQJIFx5YNLZhE2fbJxH644U0etWulo6Ot0vPPWuz0fOUeLQyKm-qPB3ylTn0zuWo5cqMym8qIyjBzqZJ3jH4UeXFHqYkHroMtc_CtNKqaMLcLWpYOff1q9TfUPrvmjZsHvawa58Rgy33GSaLHwfdRdmkz_AsAwQKvp5N5yOoP_W7dkwJ003zVYTga6nRN8bllTqot9sQV1jpn8VGxdgaX6d3FVbKUON3iZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب عن إيران:
أولئك الشباب الذين فقدناهم في الحرب ضد إيران لم يموتوا سدى.
لا يمكن أن نسمح لشخص مجنون تمامًا بحيازة أسلحة نووية.
إيران دولة شريرة للغاية. إنها الدولة الأولى في مجال الإرهاب.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/93214" target="_blank">📅 01:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93213">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇸🇦
السعودية تعلن عن مقتل 12 شخص بينهم أمريكي ،وإصابة 309 أخرين نتيجة الإستهداف الصاروخي اليمني الذي طال مطار الملك خالد الدولي في العاصمة الرياض.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/93213" target="_blank">📅 01:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93212">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔻
بلومبيرغ:
تشير تقييمات الاستخبارات الغربية إلى أن إيران احتفظت بقدرة إنتاجية كبيرة للصواريخ والطائرات المسيّرة رغم الضربات الأمريكية الإسرائيلية. ويقول مسؤول إن روسيا تعيد تزويد إيران بأنواع إضافية من الصواريخ لم يُكشف عنها.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/93212" target="_blank">📅 00:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93211">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇸🇦
🇾🇪
مصدر لنايا:
هجوم صاروخي يمني يدك مواقع حساسة في مدينة جدة السعودية وأعمدة الدخان تتصاعد منها.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/93211" target="_blank">📅 00:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93210">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">توقف الرحلات الجوية في الدمام-بقيق شرق السعودية</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/93210" target="_blank">📅 00:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93209">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c921dc7e9d.mp4?token=CG_VQrnp-fWXrFa6zLTV6kZdtwJBNSyn6St6LXdsero420CyXo62bplUldIK6uYtOj8J0rwlnmBvcUbua3Y9SnBPNUc1CFFj_KmKVMxQfeHbkeUVbNYvW_G05xGOl3kIZO-lqYF8QVWR1QwdFdqypOgNzbe3Lxk7kn2UEh8YI2_n0OcCHNrJ-udqjaHSWkvO0_X0mkdNey7w-b5LmSR2eIQR1RcXGrR9vv3euuaSCS2bqJhhC-rjGLC_3vkSQYFguiKyTMDq_YdWmqVNIFIt4QCttP96NHlZ019pnQnVR6-fz-X-d-kdl4n2yhJGe-6BSuRY7uvLCEiTWQ_IGGvSNkCSBjvyJImKSOE9zG3Rp8rxJY7mczqnTYCAG4VOFqovPwsjmhVyqtTzQ2nHt9YeADZ5AgVxHdcXtr8Q9ioNDCkN2xFpEVWBir5LIshpsye8NY4A8vxyCnCPfkP-K09qakCZ8v0bpi7j2Vqnp6f8SNwckjcEsR1XCHAbpJ9Z0w14iQ6yYqaajmM09rd3la8bVhzA5ioPoi4Asbr4RlEV2fWocT62Co4unSQY55KwsuXjT3Fghd11jkgHuXZc402Hx1nn0k_KVfblz2XCSEqYFtMofMSxQreRmW-O0shQP2tBLksRN5myrrmP45anz6o0896plw42E9ncGOn9wtQtRLs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c921dc7e9d.mp4?token=CG_VQrnp-fWXrFa6zLTV6kZdtwJBNSyn6St6LXdsero420CyXo62bplUldIK6uYtOj8J0rwlnmBvcUbua3Y9SnBPNUc1CFFj_KmKVMxQfeHbkeUVbNYvW_G05xGOl3kIZO-lqYF8QVWR1QwdFdqypOgNzbe3Lxk7kn2UEh8YI2_n0OcCHNrJ-udqjaHSWkvO0_X0mkdNey7w-b5LmSR2eIQR1RcXGrR9vv3euuaSCS2bqJhhC-rjGLC_3vkSQYFguiKyTMDq_YdWmqVNIFIt4QCttP96NHlZ019pnQnVR6-fz-X-d-kdl4n2yhJGe-6BSuRY7uvLCEiTWQ_IGGvSNkCSBjvyJImKSOE9zG3Rp8rxJY7mczqnTYCAG4VOFqovPwsjmhVyqtTzQ2nHt9YeADZ5AgVxHdcXtr8Q9ioNDCkN2xFpEVWBir5LIshpsye8NY4A8vxyCnCPfkP-K09qakCZ8v0bpi7j2Vqnp6f8SNwckjcEsR1XCHAbpJ9Z0w14iQ6yYqaajmM09rd3la8bVhzA5ioPoi4Asbr4RlEV2fWocT62Co4unSQY55KwsuXjT3Fghd11jkgHuXZc402Hx1nn0k_KVfblz2XCSEqYFtMofMSxQreRmW-O0shQP2tBLksRN5myrrmP45anz6o0896plw42E9ncGOn9wtQtRLs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من استهداف سفينة مخالفة مقابل السواحل الاماراتية</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/93209" target="_blank">📅 00:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93208">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aefc2bfca.mp4?token=Gsgnd7p-VS4MKx_-Fsw2Cgy1ev0uQ8Ducj_WJ-mb_UIZdAFEEELqglZjBX9FRNuC9fx1a3MC3XXJbXmvj9WBUdw0J3g6fWW3iygOxmhufx-nWgS99C6cZJF8TgfaS09KMVsybuO9AvrCWnHW97kPFALBDklIualFqwyu9bBm3fbpHhgm3alZX-HZVoh_yjYWbgWeqJYa7ljLnzTD5f-g_ynx4CT8ZG_T5nyNWfkrq_U8cnt32gme-0R-8QRTDILkPmrZUj60yg1_DU_cY4c4Yq3lagBPswbXEV4wYMNDa6Juu-d1WrAT6YHzRJG72VZieowRBTfM3GOtgYAeIYSZZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aefc2bfca.mp4?token=Gsgnd7p-VS4MKx_-Fsw2Cgy1ev0uQ8Ducj_WJ-mb_UIZdAFEEELqglZjBX9FRNuC9fx1a3MC3XXJbXmvj9WBUdw0J3g6fWW3iygOxmhufx-nWgS99C6cZJF8TgfaS09KMVsybuO9AvrCWnHW97kPFALBDklIualFqwyu9bBm3fbpHhgm3alZX-HZVoh_yjYWbgWeqJYa7ljLnzTD5f-g_ynx4CT8ZG_T5nyNWfkrq_U8cnt32gme-0R-8QRTDILkPmrZUj60yg1_DU_cY4c4Yq3lagBPswbXEV4wYMNDa6Juu-d1WrAT6YHzRJG72VZieowRBTfM3GOtgYAeIYSZZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب يتحدث عن ايران:يمكننا إنهاء الأمر بسرعة كبيرة. إنهم لا يعلمون كم كنت لطيفاً معهم.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/93208" target="_blank">📅 00:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93207">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇺🇸
رويترز : ‏أذنت وزارة الطاقة الأمريكية بتبادل طارئ لما يصل إلى 4 ملايين برميل من النفط الخام من الاحتياطي البترولي الاستراتيجي في أعقاب إعصار إيساياس. ولا يزال نحو 69% من إنتاج النفط في خليج المكسيك و57% من إنتاج الغاز الطبيعي متوقفاً</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/93207" target="_blank">📅 23:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93206">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkuS-jd-o9MpkQIln8WxqDuGX5uT_8BzEMnZ8o6JhBv0Bwo-MkzX_rY3j44hO58jhahHnvKlkYJQ-BEEq-zjbep_x_2ghH-6hMrLR3xwzpcEEKcMImCms0DSu75ZAqsiUmMOQBk-wmNZ5DREyZ9wQF3nHIs2PyrgAuLvYrtFlx5oGSl8a8HelVW-tUSq8TSZyGyEpL9XZGzcRbQy_IbMO_lkA8RoNCgaOr95kjtuyopubwymrzjrHYNaUvB8Nxhl5PSSFad-tcTB612hx5EixzLI74OlXAe6vD0LN5cb6_WmXv5S2nq4fDHy806hc4TRdGwT5gRbgEEHPFpNbC-Ckw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقف الرحلات الجوية في الدمام-بقيق شرق السعودية</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/93206" target="_blank">📅 23:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93205">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇶
سوالف الگهوة
رجل من بني كعب يتدخل لمزج الألوان بين الأصفر والأبيض ويطفئ اللون الأحمر الذي قد ينتج من الهوسة التي بلا معنى  .. ابو الاء الولائي يخرج منتصرا سياسيا وميدانيا وعسكريا و النتيجة هذه المرة ٢ لكتائب سيد الشهداء صفر لاعدائه  …</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/93205" target="_blank">📅 23:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93204">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhAalg61wFYVyFf95dfQ4N4u8WW61nvy-u1SLN6q3XwJzHML0aQozfiLTUPc85jhPsK6qVgF4iwaLOcB46WR7S-Hc38YsijduPGhaRXmJfecNVhGyRPifcVwFfFNT1xq-Nlc4QNlSOiHP1uES9I6Vn4nm6Kb3fckP0GDkEW3lOquyfJnEeYQbw8xP7iY_oTrMsZGgtxPI_EQFzLkZx2nxz6hWruEUp2lAFmcKVFXOWx97qpIbP3j2fWMU5SN_IRk7wWd7qhxHbQoMNWvYSK2jF_FkhrXZQPYOtbYfJ6va_YcOtVoMyVy4IfSuShZF4kKYo2U_4SMf6swyq1gNlllGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بقائي:
لإخافة شعبهم، يستحضرون عدواً وهمياً في السماء للتغطية على التهديد الحقيقي على الأرض.
‏لا يكمن الخطر الحقيقي خارج حدودهم ولا في سماء لوس أنجلوس وسان دييغو، بل يكمن في نظام حاكم فرض حرباً غير شرعية على العالم، ذات عواقب عالمية.
‏بل إن الرئيس الأمريكي وصف تدمير لوس أنجلوس وسان دييغو بأنه "ثمن زهيد للغاية يجب دفعه".
‏هذا مثال نموذجي لسياسة الخوف: تخويف الناس بتهديد وهمي، وتصوير تدمير مدنهم على أنه ثمن مقبول يجب دفعه، وتحويل انتباههم عن الخطر الحقيقي.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/93204" target="_blank">📅 23:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93203">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8RwchJkyNCrGYWMlqoMP5W3EeboK0SCvjPTYBiFM0vwq0x0n7ZDemjomGldocVD3vwwAKV-kCFU1M8P7HmR3odtAlbrtuUR29fH1j25dEP654glS9EikB6znAZkgk_DJgFsyo-IvuNC7IKVW1G2IiofvLNcd3ZMqgsq-ES8cnQ195LYHrDEYM6L1OG8B5M3hN2OM4Ba50-TwUKJTKFPudSLzAMlEP9rx3vYZL9EtoA2yHgnrfsi89pcY7CDLEXozlAnCMPC_ZvLdCo6qX8a-y--2VTMoHWXzPZtHMAQvk-_qlKs9GRfSVNWEQvQsneORUxr2FL2Y9y5vRquIDIMcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
استهداف سفينة مخالفة قرب السواحل اماراتية.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/93203" target="_blank">📅 22:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93202">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇾🇪
مصدر يمني مسؤول للميادين:
تفاجأت السعودية من زخم الصواريخ اليمنية ودقتها، هناك خشية من طول أمد الحرب وبدأ بعض الشركات والمستثمرين بالتفكير في مغادرة السعودية.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/93202" target="_blank">📅 22:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93201">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇷
انباء عن تفعيل الدفاعات الجوية في مدينة ارومية شمال غرب الجمهورية الاسلامية.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/93201" target="_blank">📅 22:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93200">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇺🇸
البنتاغون رفع عدد قتلى الجيش منذ بدء حرب إيران إلى 21 بينهم اثنان خارج العمليات القتالية.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/93200" target="_blank">📅 22:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93199">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇺🇸
🇾🇪
‏تحذر القيادة الأمريكية في أفريقيا (أفريكوم) من أن التعاون المتزايد بين الحوثيين في اليمن وحركة الشباب الصومالية قد يهدد القوات الأمريكية والسفن في خليج عدن. ويشعر المسؤولون بالقلق إزاء عمليات نقل الأسلحة المحتملة، وانتشار الطائرات المسيرة، وتوسع العمليات المسلحة.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/93199" target="_blank">📅 22:04 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93198">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇸🇦
فايننشال تايمز :
أحد المستشفيات القريبة من مطار الملك خالد الدولي بالرياض استقبل نحو 50 مصاباً، بعضهم في حالة حرجة، عقب الهجوم. كما تستقبل مستشفيات أخرى مصابين، في حين فعّلت المستشفيات الرئيسية في الرياض بروتوكولات الطوارئ.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/93198" target="_blank">📅 22:04 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93197">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇺🇸
🇸🇦
‏الخارجية الاميركية للمرة العاشرة تصدر تنبيه امني بحذر السفر للسعودية وبالاخص المناطق المعرضة للاستهداف اليمني.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/93197" target="_blank">📅 22:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93196">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ygx4fBgoGQHP9GwVlTjHyw7sFuU6ZpOAJnNj61uZLcMMkyk5blpGNj0ETD0556nJuIc8CXmw-lC8IleWFMCiAOmkNbG3BBE8Ugxbb4Y_kAJMIjIbGmcItw1tH-oAhWSjbplS_Fg3t5HIGHMzpIpfYxWY2rlIU6hpEpC3ZGLN_4SYCdySxIoiAVgSOaulyJErYoTU3zAjRSdYIs5NvkTfb_ktFiF3iamGsXlwWFB_BGLFxula61pZau57sqDJTtNqj8bGuBOOb-1KmK1aQgl5VuOCAUufVKRffzYjIq7gDbeR8mNd-J9vms-rFu2VtEcf09txb3S80sk3mlKl65lfWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مشاهد للناقلة النفط التي تعرضت للاستهداف بلغم بحري.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/93196" target="_blank">📅 21:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93195">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">لحظات تسليم مجاميع من تحشيدات العدو السعودي للقوات المسلحة استجابة لقرار العفو العام
من مشاهد تأمين ما تبقى من مديريات سامع والصلو والمواسط - 10 أكتوبر 2026م</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/93195" target="_blank">📅 20:41 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93194">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇷
مشاهد للناقلة النفط التي تعرضت للاستهداف بلغم بحري.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/93194" target="_blank">📅 20:37 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93193">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇸🇦
‏وزارة الخارجية السعودية تدعو المواطنين الذين تأثرت رحلاتهم أو تعذّر وصولهم إلى وجهاتهم نتيجة إيقاف أو تأخر بعض الرحلات المتجهة إلى مطار الملك خالد الدولي إلى التواصل مع بعثات المملكة في الدول المتواجدين فيها، وذلك لطلب المساعدة وتقديم الإرشادات اللازمة.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/93193" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
