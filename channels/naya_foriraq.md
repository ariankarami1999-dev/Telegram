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
<img src="https://cdn4.telesco.pe/file/t39hrraEYRoNkc6VkKUwTQXS4VxA544xA_qd241Odc-9cxonTwCjHsJG9775harmsOHjYPkt28HRI5MDgdd6vFlA9oYLKhre0Bjsof5FAl5YJod8JJo5__MBNXdoevXXvIlprIcUKkisqmE5fog7UadyO94Jz4bD3bNheqAYBNa0FSeUimR2xbGXfBfn1TSAVRSgnSW9pG0Zkcx6JtR1B9WTXgVrR8as0TkagJxBkd0i7dAC_WCm8eoDktBAjok7SZriJu7RIRPXr18ohDJZoiqymR3Jk6BbYEYiUZXtx7KMry3fvIvd99xU3Nf08ihbFBDhLllrszxf8JYgvGD3qw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 20:20:35</div>
<hr>

<div class="tg-post" id="msg-90394">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tzF1ft7EO_6a_Rfqm6_1aiWezPopdWTbIWp5NIwuRU7mcAjScYYAZv-LSLxF7LKcIbmbXDSjwMFIXpuuaps_XJo_YVSnRNfZVLxQbs5bw1U4UJ6zP0JOPh02XLFmQwZ-zw8TxPekCpMuj2WZr0EbQDJYnfkvdJ6SmLu2J3bec-U-CbJaMtE18jztKOiGxQlEOgpRmHGJAuYu4ytKvZQg0-eKf1ACLBNhsKIGTr-rTqSD7tXJWmwjFJRPCWyCdV9fpPND9O-kQcDSLXcnioJpiur5C9Cs1bT4kPTn72FbsUtqIaIfbw9K5yNNgMKXoaZX8t-IsU9Jnf-YyhU6L9N0yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MBkOre9xICeaBAw741D5PNkLiqGwZQ8uINvTSg8MtER-jz1KRf4cF5SaZGmrAZe18svBDhatC26e86T2DXUqVdXlNXDpAzemRcZRt5rEBTU2ha4Luzu45Rqqe2__w_FcxqfmQ_5XEsGWvcWj8z3PhfPmq0U2rhklBxI5URSSTSH73L1FBAjhVAkJBIdQK9SL0MuuEOSpuZLZbRanzfsSigC1erRYwHxg7Shn1CC4pX1csrUIxM9Bb7TJgv9uTFxQeHpVJoHad9A9t4AvgffpODtTpjLjoFlsOTiixEOYfe0UPc2B9_EzUYb8PfEf5UiEj-MUhw5t2GQRxQa740OV8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسالة أهل الثبات لقائد كتائب حزب الله، الحاج أبو حسين الحميداوي "ايده الله ونصره"</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/naya_foriraq/90394" target="_blank">📅 20:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90393">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca0be8bb0a.mp4?token=CJ1KrgM4BjLWh6cBfFs_I1lZELmpmz7obEWFKFa0ZVyIUNhXslkuBLLLGnKstEm3bvFzfT4oSoniwivZHOODjRWr80cqIFeOqTkB6DULLthQL7oHaAofYtfrCC7prc2FVg_yjYIYPosJ-RM5wMjnRQ5xgXqw1-o16Xabg1ARvcy2wwstbyCVKy4u8S6vMMrxewOLPbwdlxVfFxxv63f6qI5KxBVpiO0I_-Bm_tzPfruNl4DLhvj7HjNdPWkkIhAiDhtQ2_7hCYsetsPgXAIybtUGu9d5_xlqBD4ZuBZz1ldk87oeghTLhL4gwg0cxwsOw17HIGibNgoh_J-l3z4drA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca0be8bb0a.mp4?token=CJ1KrgM4BjLWh6cBfFs_I1lZELmpmz7obEWFKFa0ZVyIUNhXslkuBLLLGnKstEm3bvFzfT4oSoniwivZHOODjRWr80cqIFeOqTkB6DULLthQL7oHaAofYtfrCC7prc2FVg_yjYIYPosJ-RM5wMjnRQ5xgXqw1-o16Xabg1ARvcy2wwstbyCVKy4u8S6vMMrxewOLPbwdlxVfFxxv63f6qI5KxBVpiO0I_-Bm_tzPfruNl4DLhvj7HjNdPWkkIhAiDhtQ2_7hCYsetsPgXAIybtUGu9d5_xlqBD4ZuBZz1ldk87oeghTLhL4gwg0cxwsOw17HIGibNgoh_J-l3z4drA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تسجيل حالات اختناق بين عدد من موظفي معمل الأسمدة الجنوبية في خور الزبير جنوب البصرة نتيجة تسرب غاز الأمونيا داخل مصنع الشركة ونقل المصابين الى المستشفى لتلقي العلاج مع اخلاء الموظفين من موقع العمل.</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/naya_foriraq/90393" target="_blank">📅 20:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90392">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818a015df3.mp4?token=vK_IvgWPv09o0ltREfZZMtayAVc78xMu1gjhUIbuCU6TDMF1nBdrPRuVFljmleGybG0mFSn7zuSdKAgOsMkSXfD_Pq6y7bRhvlmtHhy-hNf3nQLqQX7-GAzOT2ObDysOHO3bL3g9H3Mqtb4KWFXNyGM7YE797SEI1bAYCeOti-x4eeDzvcHUd3JCreyTEfgzZbSZiLEuE11r1xmS0Xob2h-GyuzGMYZTHN88G4Ge8oS3sC1fpccfxt1bKKx_Ejqih0RtaRn7UxjWH68T8wKn0s6-Wjye0ihzXBYJyL4O2bYhHX5hxjjTu0ZvRRIEOTpCtJSGpKXgkJN9gt7y7lU7zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818a015df3.mp4?token=vK_IvgWPv09o0ltREfZZMtayAVc78xMu1gjhUIbuCU6TDMF1nBdrPRuVFljmleGybG0mFSn7zuSdKAgOsMkSXfD_Pq6y7bRhvlmtHhy-hNf3nQLqQX7-GAzOT2ObDysOHO3bL3g9H3Mqtb4KWFXNyGM7YE797SEI1bAYCeOti-x4eeDzvcHUd3JCreyTEfgzZbSZiLEuE11r1xmS0Xob2h-GyuzGMYZTHN88G4Ge8oS3sC1fpccfxt1bKKx_Ejqih0RtaRn7UxjWH68T8wKn0s6-Wjye0ihzXBYJyL4O2bYhHX5hxjjTu0ZvRRIEOTpCtJSGpKXgkJN9gt7y7lU7zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اخلاء معمل الأسمدة في محافظة البصرة جنوبي العراق بعد تسرب غاز الأمونيا.</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/naya_foriraq/90392" target="_blank">📅 19:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90390">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X9UcIPMxNcxLj4TNETOk1B5Bkvqe7KdOyLcI3g8zayaMApmA_6U-5_fzLeo1w4UXwed2Krfl9RsJC7CjG6SzVVPcCjebmdf9pEA5m7k8_Dd4jtzjcXGCcastoSXuJHap5OkjUOc2UreINeoirh8uC9CkTkcCtTed-LF2uIbVY62k6zPE0pG5Ry4mJAMnQrBaKnlO_Y11Ab-qFAShZB-6Yu3HuCvsRgPimBNe5hIRO-iv7IncmFiQDoFPrBPN3oopAYS-0fUuAiFRN0bJ--A4mPrge8ZlDTrh6cIMsU1CHCP0QI9KtC89W7VuHFCNDN4zIuxglKkaQnaa8em-n4NxWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BZrPooIIin0Y9yyE94-X-oDf8W7EulecljVEYdCgNF8DQQdBFUPD7rCSCpuMDLoorLU59LIKdODcWc1ltl7JI0RJh_oi-7QoZ0R0yW_G1SjM6BeeFPT9ifN5Jtz9Feek1fhK_nq07sVu808U1x_vC5c5C1ozAyoHudzHkQBU8BFaB8PyHKO0Kmnq3Z3TD_V1JkL1ez_-nfwsO9wn-zGKrK0RUzE-_c6i_T0ScKw1S14gUvtIxDPPqojL2SMQc6us3P8qUQTREU5CMPVEQdRXHsjkfvcvU0l73wHbKVPNYCglSNVqhmA9u9Nh3FJj25E3cP-PojJoyF0EzfZXViL04Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انفجارات تهز ينبع السعودية واعمدة الدخان تتصاعد</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/naya_foriraq/90390" target="_blank">📅 19:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90389">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇶
اخلاء معمل الأسمدة في محافظة البصرة جنوبي العراق بعد تسرب غاز الأمونيا.</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/naya_foriraq/90389" target="_blank">📅 19:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90388">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">صواريخ باتجاه خميس مشيط وابها</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/naya_foriraq/90388" target="_blank">📅 18:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90387">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/90387" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇾🇪
نقسم برب العرش
#شاركها</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/90387" target="_blank">📅 18:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90386">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/90386" target="_blank">📅 18:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90385">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رشقة يمنية زيدية نحو خميس مشيط</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/90385" target="_blank">📅 18:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90384">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/90384" target="_blank">📅 18:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90383">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/90383" target="_blank">📅 18:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90382">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇷
🇺🇸
هل ادخلت ايران أسلحة بحرية جديدة ؟</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/90382" target="_blank">📅 18:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90380">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نظام ال سعود يهرب من اليمن ويسحب معداته من مدينة حريب وبيحان باتجاه منفذ الوديعة السعودي</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/90380" target="_blank">📅 17:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90379">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇸🇦
إندلاع حرائق هائلة ومجهولة في العمق السعودي بالمدينة المنورة</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/90379" target="_blank">📅 17:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90378">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏ترامب في تصريح جديد: زيلينسكي يجب أن يفعل شيئًا واحدًا. يجب أن يوقف تعطيل إمدادات وقود الديزل في روسيا. إنه يتسبب في نقص في وقود الديزل.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/90378" target="_blank">📅 16:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90377">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a416e2d458.mp4?token=KYms1D1bhbnK0p5qprMaY9hrzHbOYNXT5l6W7gEpgL2sPoswVwxrrMISEtZ3kKt73sheFQUWD_xX_K6ODTGYZOtavbMKLt1c6afU9cC6R2yZwW3zXndPplBGtfy3sFzmQLBapG2AKAPBtXCTrTVy2wvag8wBH_q1NoeXISrMmlAZCWD-YQFpSbvCaFAzcYPrTUPPowJgWEWLUObC4FtBjOCmMIj3RFb3Pnd-YE9wKfUU2PGajMRxEdWHees5UjxNNk5yeB-PEJdcB3J-BzneDnaVzkSlw4DJ99ReT5JQoVrekTakkr-WzfMOTjSDQ_3H75EPn9r6FFA_m4vGOfAqU4IBFpLDJtlaH_RvVxdT-lgRtzDLnkPgdCHliVJDs0md0CU33DlYP5kZMoW9jl1utOMZqbRUT4fx9Fk6gQTjkE8BiZdNmKl7SRqHBDnc9mgbUg2oE5yOQpkPWuivKYuAypCxEDGjTG2rz03AQhYT0mGWPcxNdFJ3FULpqqaPPouMTGEkkt-CgMuxaO2-jihEPchkz1RiCdiYbBpZdQhtan-TP_4vA2IlkVF0OyOR5-n1oHarVAvHwGBj0Bvt_k97p1MlgftcN4yXR9MUguuQ44HwqlEPv0DEpieM0LqJHwUyw4UCcs7zWf_ClW1PJfE0gEnAWI_W2ZbRaVjJBGaOmvE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a416e2d458.mp4?token=KYms1D1bhbnK0p5qprMaY9hrzHbOYNXT5l6W7gEpgL2sPoswVwxrrMISEtZ3kKt73sheFQUWD_xX_K6ODTGYZOtavbMKLt1c6afU9cC6R2yZwW3zXndPplBGtfy3sFzmQLBapG2AKAPBtXCTrTVy2wvag8wBH_q1NoeXISrMmlAZCWD-YQFpSbvCaFAzcYPrTUPPowJgWEWLUObC4FtBjOCmMIj3RFb3Pnd-YE9wKfUU2PGajMRxEdWHees5UjxNNk5yeB-PEJdcB3J-BzneDnaVzkSlw4DJ99ReT5JQoVrekTakkr-WzfMOTjSDQ_3H75EPn9r6FFA_m4vGOfAqU4IBFpLDJtlaH_RvVxdT-lgRtzDLnkPgdCHliVJDs0md0CU33DlYP5kZMoW9jl1utOMZqbRUT4fx9Fk6gQTjkE8BiZdNmKl7SRqHBDnc9mgbUg2oE5yOQpkPWuivKYuAypCxEDGjTG2rz03AQhYT0mGWPcxNdFJ3FULpqqaPPouMTGEkkt-CgMuxaO2-jihEPchkz1RiCdiYbBpZdQhtan-TP_4vA2IlkVF0OyOR5-n1oHarVAvHwGBj0Bvt_k97p1MlgftcN4yXR9MUguuQ44HwqlEPv0DEpieM0LqJHwUyw4UCcs7zWf_ClW1PJfE0gEnAWI_W2ZbRaVjJBGaOmvE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
بدأ كلمة جديدة لترامب وتسرييات من البيت الابيض لنايا:  - اغرقنا القوات البحرية الايرانية - دمرنا القوات الجوية الايرانية - ايران لن تحصل على نووي - ايران ترغب بشدة بالاتفاق</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/90377" target="_blank">📅 16:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90376">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔻
بدأ كلمة جديدة لترامب وتسرييات من البيت الابيض لنايا:
- اغرقنا القوات البحرية الايرانية
- دمرنا القوات الجوية الايرانية
- ايران لن تحصل على نووي
- ايران ترغب بشدة بالاتفاق</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/90376" target="_blank">📅 16:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90375">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e66be65.mp4?token=Gl6h3lTorvHzthZkLmCKE5-d06WSwj1n8kwS-vXQo6wW-F0bGwMEKDIGT5zrvk5PGEzp8pBht8Mr7zoqWdFjObgnBMx0t1hXRJQsKDImjKdM2KrtWV_Fg6WjGTKX6PAA_wMAYb7nZUhwdr9rz92lOlm8UQzEN11VvzIzv6nP7E5eCgF6SS893GToBq0YAd11uUO43QKa-Nk37497E2vcWfliiQsBXsNuaMX2blqC8Ce8QFU20ATnzWa0OfhSaWLTzc-1HrAhMnFUx0xgm7LvIjUf65bHACQu6t-50rUI8yGmi3YMaZR6Us1xvSD1MDO5kFQFcyHh9AB_6mccVIG5sVS8wCHwyDSz5WO29A2L4mAh6w-VjaQxsQCFjexXzdWsGRyb9Dr3_dAYxRF2F_vMElxPZGZ5pclJtrfZjstlSPiivdPwbAcyYD0rfs-ufkkpS804qTo8T8-WOrRO3yP8Xf5rYxsROO7ALbiUv9PD98U0XoLrRbarT0bzf-MJvebx514clV9Ja6odOYbHhwCrqcHoVbsxus3b2b6C_jGcJd05nr3D9vifUkp9MtCul-LI7Q2kthLFbxRLJ48GJjBAv_KlVrRvun7-s_VTk7Ber7D2s1pkTCmw54n6oH1dd3ExM1VSt5tsmzP9YSsTVg8AvfEYkKFeHcNdkaOCYOtFJ4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e66be65.mp4?token=Gl6h3lTorvHzthZkLmCKE5-d06WSwj1n8kwS-vXQo6wW-F0bGwMEKDIGT5zrvk5PGEzp8pBht8Mr7zoqWdFjObgnBMx0t1hXRJQsKDImjKdM2KrtWV_Fg6WjGTKX6PAA_wMAYb7nZUhwdr9rz92lOlm8UQzEN11VvzIzv6nP7E5eCgF6SS893GToBq0YAd11uUO43QKa-Nk37497E2vcWfliiQsBXsNuaMX2blqC8Ce8QFU20ATnzWa0OfhSaWLTzc-1HrAhMnFUx0xgm7LvIjUf65bHACQu6t-50rUI8yGmi3YMaZR6Us1xvSD1MDO5kFQFcyHh9AB_6mccVIG5sVS8wCHwyDSz5WO29A2L4mAh6w-VjaQxsQCFjexXzdWsGRyb9Dr3_dAYxRF2F_vMElxPZGZ5pclJtrfZjstlSPiivdPwbAcyYD0rfs-ufkkpS804qTo8T8-WOrRO3yP8Xf5rYxsROO7ALbiUv9PD98U0XoLrRbarT0bzf-MJvebx514clV9Ja6odOYbHhwCrqcHoVbsxus3b2b6C_jGcJd05nr3D9vifUkp9MtCul-LI7Q2kthLFbxRLJ48GJjBAv_KlVrRvun7-s_VTk7Ber7D2s1pkTCmw54n6oH1dd3ExM1VSt5tsmzP9YSsTVg8AvfEYkKFeHcNdkaOCYOtFJ4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احتجاجات وقطع للطرق في سوريا بسبب ارتفاع اسعار المحروقات على المواطنين</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/90375" target="_blank">📅 16:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90374">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">احتجاجات وقطع للطرق في سوريا بسبب ارتفاع اسعار المحروقات على المواطنين</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/90374" target="_blank">📅 16:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90373">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjIxnL0IUHgUWp7k8-bGeqS9IJhVvKRFIEhMkRuEXiqKQhj_CjYhNmi3eH-yiDuuW--W2gm3NiJ72dCzOVHY4F_N0e4QjlVUINuDSyBmGfwOaDxkwiqD7tIBlpjMFNTdHojr6px169bUoNLenBGZxiC85_CQZ42kZzkNnaUHZoqR-BVUzoTu4z_WQqtJ2PAEB7o-wB7TEjNciXWG9Fp6EY3b2cap-yhQhj4Vz6F9Sdsg2wVA0ei-Rz9wb0fsLPd5yImvKkzu69rwaRT9CJkkfZH3hXpvx6ireqHjWb5qxF-BAAIa6aMRrwdgEmmwYKNeWKnC8SYRZTVc3UG9LzGpTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ترفيهي
🇮🇶
مديرية تربية محافظة واسط العراقية تصرف مبالغ عن طريق الخطأ وتطالب باعادة المبالغ.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/90373" target="_blank">📅 16:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90372">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDhmGVievPHYX-40iUMsGCk4vj7_cthgFA17A-aAc5-0ELUJimfogOCYlPXQLeNf_YdL-e2GdazcECzB8eBXBxDgoIX_cwlpPdP8jKGandjNakkyYlc6mW2pwQDN8E1h_DsJYJ3CZrVjGUx09gF-EyZP73xujfn85LlflhByqbzE1eRAzmynC3DgWW1fjS7z9g898-nW2vT97fO5JI88qZaUw-_gE-9vpCD3ZYbvGPnGvJvyMzSvJ05SIh5fOGQNuiTrX5DAeVL8ajGGDC1o3CDXxzZnwD-UbALI5CjYCMz0pNH3WUchtp2uhTAB6QJHFONXzPaelAbn4z3Z3G8oSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الكبسة ويانه غير
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/90372" target="_blank">📅 16:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90371">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇷
الرئيس الايراني مسعود بزشكيان:
أجرينا حوارًا جيدًا مع ولي عهد أبوظبي، واتفقنا على تجاوز الماضي وبناء مستقبل أفضل.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/90371" target="_blank">📅 16:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90370">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">الاعلام الامريكي:
وقف خط أنابيب في المملكة العربية السعودية يهدد خسارة بنسبة 4% من توريدات النفط العالمية ما لم تبدأ الاستخراج مرة أخرى في الأيام القادمة</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/90370" target="_blank">📅 15:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90369">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a08f0e1a58.mp4?token=qwN56tNdT3jFqLSNLycj0q5U-TBHMfzWRfErkAN1k7WAIRIPlsYIRsPdpZMI8PcgAWoVFEoZiq7gJ4Adg5eUdsRP22K_dYjo-w8ICmxOKO-tJeEY2VdZzUshEOUyq_4vzq44d51euQjlC56Q9IJ9bMWz-HmxZFKoWbtIzi97AE1zcLr3ZdMTOy46vrF_t9-NR8DaAddcIcF4kT_xztiM55ZoC6dtdbGBxyLzvAYyLGZwRodl5OJXv9XFwSHHZR9ptskzPWseM3TecOm9J9Og2h8gSWa3MWqH3jeB6_BwYlIMSkRISIDF3ZT7CQZw1061C9Dp-AvLMD9N6HGevBZl7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a08f0e1a58.mp4?token=qwN56tNdT3jFqLSNLycj0q5U-TBHMfzWRfErkAN1k7WAIRIPlsYIRsPdpZMI8PcgAWoVFEoZiq7gJ4Adg5eUdsRP22K_dYjo-w8ICmxOKO-tJeEY2VdZzUshEOUyq_4vzq44d51euQjlC56Q9IJ9bMWz-HmxZFKoWbtIzi97AE1zcLr3ZdMTOy46vrF_t9-NR8DaAddcIcF4kT_xztiM55ZoC6dtdbGBxyLzvAYyLGZwRodl5OJXv9XFwSHHZR9ptskzPWseM3TecOm9J9Og2h8gSWa3MWqH3jeB6_BwYlIMSkRISIDF3ZT7CQZw1061C9Dp-AvLMD9N6HGevBZl7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس الوزراء الباكستاني لمحمد بن سلمان: نؤكد دعم باكستان الكامل لأمن السعودية.
باكستان وتركيا:</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/90369" target="_blank">📅 15:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90368">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27850023e2.mp4?token=rOyc1vOjLv47gaPJ9KOen3q2pKe5qyPcFd9thK81rKeY-fFAQnLDyHWNEOjQB3Dm6UK9iLBc6X6MDr0hRZUcM9U7Z05p2LPu4fbBjAfeEIReMLk5zxt8GOJ5ntrxZAyOYwXCkbS6qMVNLpbaczvsbUVjjbaIdu5MEgvc7X5_6bSb9-W0uMWbytQSui36dVZo7NsHHqtn2_pBEVQT0Dq98mBFJF8FQ7bRmIRZXvTvHsG0LGDlR5N-sRwNua0W30HGl4nu1Dawg8m6OfmL1w-CbfdVUP7IrdATLOTj9t1JY9HYw0MfiWZXdj8T4-rkpcAVOOQ4THG95AW2XPGCdprK9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27850023e2.mp4?token=rOyc1vOjLv47gaPJ9KOen3q2pKe5qyPcFd9thK81rKeY-fFAQnLDyHWNEOjQB3Dm6UK9iLBc6X6MDr0hRZUcM9U7Z05p2LPu4fbBjAfeEIReMLk5zxt8GOJ5ntrxZAyOYwXCkbS6qMVNLpbaczvsbUVjjbaIdu5MEgvc7X5_6bSb9-W0uMWbytQSui36dVZo7NsHHqtn2_pBEVQT0Dq98mBFJF8FQ7bRmIRZXvTvHsG0LGDlR5N-sRwNua0W30HGl4nu1Dawg8m6OfmL1w-CbfdVUP7IrdATLOTj9t1JY9HYw0MfiWZXdj8T4-rkpcAVOOQ4THG95AW2XPGCdprK9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
عدوان أمريكي يطال سفينة تجارية إيرانية بالقرب من جزيرة  قشم جنوبي إيران؛ إستشهاد مواطن وإصابة 3 أخرين كحصيلة أولية.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/90368" target="_blank">📅 15:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90367">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIwtuaLnh4lZPDlF5QyhqcfHWhQvL7TVhH0Yyx7eo6iVAKES-_KveUhAGvx7sU0Ntjj1C4ujLrDSnN1szqBl4sKEOwVWH7TCVM3vwiO0Ifm4Q5Zzh3lm_WswXsmqdtQIQUmuSs7pEUu9FbbU81SJo5qglo7-dcmjecouzRhxR4qfb2RE3Ts0x0MHBdF6XjvFPNaQfHfijviHDKPDQCIAoSAB467oXWroW0xYkE16CKfpjpeckTm02p25XpJMQkMco5zDoSDo--I-UFUpHi1K6sry7GalKv7SrjHoP9659bN42Wq2KcCT4DX8byADic-E19XRH380ujASHfDDhEyrPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
قصف إسرائيلي يستهدف محيط بلدة بيت جن جنوب غربي ريف دمشق.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/90367" target="_blank">📅 14:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90366">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Me4mVI-dLNCcbR9rfkxV6PYSk1rBmbCh32857g2rnbKWc7gwY3lZgF87_6aoGCY6d7jm0W8OLI4_KNOobvE4IHLyIr7oM2puN7Iin6evUSPNNu8HX2jvS17z6M7l8jY-z2Gv_3Uz9_ojfkpql-Hbv29CdG0OIC08vhK4IKKKLM3BCqhzdaCptIcT-wEYB6p_Ke0GRHXuVOWgwVt_X17boTgcgIeYJmIngOJBV3UyVGjNm6xFs-gb9Y-A80s_uhwmfgcfpTEL65WbRS3sj8Wmvunbfbh6npTLw5kcebDd1ITeQZsEMwRlytsGcyhrh0xDnAWY7E7mGH2n9Ye2VLRK0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات تهز ينبع السعودية واعمدة الدخان تتصاعد</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/90366" target="_blank">📅 13:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90365">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇹🇷
🇮🇶
عدوان تركي يطال مقتربات قرية گلاله في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/90365" target="_blank">📅 12:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90363">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aH1RiuCy_cOFZOkATaufHhdidQcYP3_nqa5A8jUvf22-oWaYHQf_4VM9qnx1ssXEF14tXS3r9-0gthHGO2g-kJQ9t1JNs35GGY3-FTJrFGzJqMpqe27MSQhsX-eDEyJcM5oUnt_MVH0F-thq-Qce9jL8QmVVqTxabNUjQGLIfX4IXlUo_7zqSZty2y6fMdjAFoOnTycnL7jl5jMFz02ro3XLZk4TWtLSBjOKHNbA2b1T79pLO0CAZ1oBbvqMdTmFiwLeKbO-7UCGCG4RHpJ4A2SUxBnlmLaHRxrgoTrjQempU1wfgWMcOFEIooJSdXzCYUWss0ykMUnNwpdKUtqt2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الكبسة معنا غير
😆
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/90363" target="_blank">📅 09:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90362">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8041f170b.mp4?token=gHw03ZpOYoRFdszqhA2cBG8ssKhoBTBcGdGyCVQkyiz4yPKPU3-Gv7Ph5mpcK4YOUW50N6cBAbdlVUbs8snOTBAqB8jfkMfJokG70mOy7HO3nrpiJ3lze0H2rgSMbK1o_H-J60D_hTKhNVBGef9wEKLoe2U5H6FaNKCeifGj0iPNL3w3mSwVB7lP5PorAybxi8_gYfe83m0annzb114nvqAiI7YAMz8WEcYt-VkNMrT1ls9BrITuBNfAFtOnl3IqxjxP9Mbp0mfRX0LPZkZoPSerEs5No8OcmNj4xzsMLtIlFnrGlGNDP3fmcCEcwR22f7W_04Q_uK85OYxwaiiEcC5VRZxcrq0tmiKF-cGe_ktFTziAJZe17zQW-mRpEWCzaL19pqfMW1OWJ66TxqPix6109yZvpbCJkwNvvluGvpSJh1zesdbIxeklB8weohVas-zpOcEK4kBzJzVZzGVhWtkyAs9z7eZCpDuFd_dmCzhxQhZzLX604RVRbqKOK8NfWd037Ya4z-QxGCnCKHNjrPxw5g2kPFrggMf9e2x-SUwH4xv-IIuCyQXK_sEtcTalSdCA2aEBqnxUPzqSe5qiH5ls6PjzmkLr6VcLSa1v3HZpjI6TVlUfwpnGvVjunDsdVUn83qWY1M0Z0vohKOPqqKbvc0u_OJ-b30SHhNmdME4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8041f170b.mp4?token=gHw03ZpOYoRFdszqhA2cBG8ssKhoBTBcGdGyCVQkyiz4yPKPU3-Gv7Ph5mpcK4YOUW50N6cBAbdlVUbs8snOTBAqB8jfkMfJokG70mOy7HO3nrpiJ3lze0H2rgSMbK1o_H-J60D_hTKhNVBGef9wEKLoe2U5H6FaNKCeifGj0iPNL3w3mSwVB7lP5PorAybxi8_gYfe83m0annzb114nvqAiI7YAMz8WEcYt-VkNMrT1ls9BrITuBNfAFtOnl3IqxjxP9Mbp0mfRX0LPZkZoPSerEs5No8OcmNj4xzsMLtIlFnrGlGNDP3fmcCEcwR22f7W_04Q_uK85OYxwaiiEcC5VRZxcrq0tmiKF-cGe_ktFTziAJZe17zQW-mRpEWCzaL19pqfMW1OWJ66TxqPix6109yZvpbCJkwNvvluGvpSJh1zesdbIxeklB8weohVas-zpOcEK4kBzJzVZzGVhWtkyAs9z7eZCpDuFd_dmCzhxQhZzLX604RVRbqKOK8NfWd037Ya4z-QxGCnCKHNjrPxw5g2kPFrggMf9e2x-SUwH4xv-IIuCyQXK_sEtcTalSdCA2aEBqnxUPzqSe5qiH5ls6PjzmkLr6VcLSa1v3HZpjI6TVlUfwpnGvVjunDsdVUn83qWY1M0Z0vohKOPqqKbvc0u_OJ-b30SHhNmdME4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
بحرية الحرس الثوري:  ادعى ترامب، في حملته الإعلامية، أن مضيق هرمز تحت سيطرة أمريكا؛ إذا كان الأمر كذلك، تقدموا وأرسلوا إحدى سفنكم إلى مسافة 100 كيلومتر.  الأمريكيون يعلمون أنه إذا اقتربت سفنهم، فسوف يواجهون ردًا من القوات الإيرانية، وقد حدث ذلك في الأيام…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/90362" target="_blank">📅 09:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90361">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇶
الإعلام الأمني العراقي:
​1- استئناف دخول المسافرين من منافذي (الشيب والشلامجة) اعتباراً من فجر يوم الأحد 2026/9/13 الساعة السادسة صباحاً. ​2- استئناف التجارة في منفذ الشلامجة اعتباراً من يوم الاثنين المصادف 2026/9/14 الساعة السادسة صباحاً. ​3- استئناف التجارة في منفذ مندلي اعتباراً من يوم الثلاثاء المصادف 2026/9/15 الساعة السادسة صباحاً. ​4- استئناف التجارة في منفذ الشيب الحدودي يوم الخميس المصادف 2026/9/17 الساعة السادسة صباحاً. ​كما نؤكد أن حركة العبور والتجارة مع الجانب الإيراني لم تتوقف، ومستمرة بالعمل على مدار 24 ساعة في منفذي زرباطية والمنذرية.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/90361" target="_blank">📅 08:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90360">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇺🇸
🇮🇷
عدوان أمريكي يطال سفينة تجارية إيرانية بالقرب من جزيرة  قشم جنوبي إيران؛ إستشهاد مواطن وإصابة 3 أخرين كحصيلة أولية.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/90360" target="_blank">📅 08:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90359">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔻
بحرية الحرس الثوري:
ادعى ترامب، في حملته الإعلامية، أن مضيق هرمز تحت سيطرة أمريكا؛ إذا كان الأمر كذلك، تقدموا وأرسلوا إحدى سفنكم إلى مسافة 100 كيلومتر.
الأمريكيون يعلمون أنه إذا اقتربت سفنهم، فسوف يواجهون ردًا من القوات الإيرانية، وقد حدث ذلك في الأيام الأخيرة.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/90359" target="_blank">📅 07:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90358">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇾🇪
إسقاط مسيرة معادية في سماء محافظة الجوف اليمنية.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/90358" target="_blank">📅 04:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90357">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feda8091af.mp4?token=lIcM01BHDm5345rPj-tO26euv7RzaFetmSkoUJOCmrdVPfVqkl1MZ8fcVOdBT1HiSG_5ZVQhlCeo4F--zpFsvNjIFzpkFNsK7rcxRT8TvgKkPzGg9M-CiL4hbXyba87xL9NAavOrQIO7S_vtfR7owiVWZxnTlxf2noYRPcsVDn1nKfKJKALJWViu9lBPBithEGt-ZzpHERC0-MqMvPHAIQBEq2jdCt7giwLhNuCeQlIh_OEZN8t-4nJe6OF1E1AJF49mkWmV7Oz3YNl86L6IxnINeIvmBL36KHkQUJERcwrRaATiXRQT4RuTRCbJ3revsdEuRP3_B6AuDW4ePjlMTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feda8091af.mp4?token=lIcM01BHDm5345rPj-tO26euv7RzaFetmSkoUJOCmrdVPfVqkl1MZ8fcVOdBT1HiSG_5ZVQhlCeo4F--zpFsvNjIFzpkFNsK7rcxRT8TvgKkPzGg9M-CiL4hbXyba87xL9NAavOrQIO7S_vtfR7owiVWZxnTlxf2noYRPcsVDn1nKfKJKALJWViu9lBPBithEGt-ZzpHERC0-MqMvPHAIQBEq2jdCt7giwLhNuCeQlIh_OEZN8t-4nJe6OF1E1AJF49mkWmV7Oz3YNl86L6IxnINeIvmBL36KHkQUJERcwrRaATiXRQT4RuTRCbJ3revsdEuRP3_B6AuDW4ePjlMTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
الدفاعات الجوية اليمنية تتصدى للطيران الحربي السعودي.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/naya_foriraq/90357" target="_blank">📅 03:48 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90356">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WByN3FHdWeol4IlEo29RN3KhZ2lVwfCHr4F_DBAIOf2oLE1zrZncJa8xO9U_3OMReR5wwPfLih-InmhfEP0iKqIr8fUEQp1MFCCkFnXfesBvUh25yautr6WhPWG_iugc_s7tHoGum5KWsV0kmmBL6gZwRDJjcMhRY6KK3zKGA6C-dEJFUnQcP1CUp3pl2IxmvWAexnfiS8q--89XK8VgxHggidlzpf5toHvr22DAZG3aScxndNgkgIHXc8tBhyGdHPfmNXLsxGbTajqeMlhOaQe4vkuwwh3UZE8fuHpGwfQGXze9_ZoYNMdv-sbYFh01kfANgObeZDyKhTC4uMQFVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بعد مخالفتها للأوامر الإيرانية..
إستهداف صاروخي من قبل بحرية الحرس الثوري يطال سفينة في مضيق هرمز، أدى إلى تعطلها عن العمل.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/90356" target="_blank">📅 03:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90355">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce949aeb8c.mp4?token=hPzjEZGk_d8-89PM7m-CbsOSNLnWboRKfY52bziwVxlmuWVzMdLNo54wUVk5EfGeJwUn2MDT0d3iJaYu19a12geAGfo6CYtoqq_73ZGAwG_anaWrjBmcA8mi_XD02sKhlUG6jBNsgyzGXdD9xUCmqrv-yzUTBhBQ4aFg4PlkpmVuqxTm3i9T4JehTcbdDFPtFV4Ct7QfmR1alJqdYCNdmsL0WbnIse5iQRoKwjqFQjtT4rIOgC-s3BpHydS03IFpwCgF0KmpsSk0-uSOLB8Ybo1GLlBwV04kQLPjlQGF4oGtuIYEtwffzkrZiGf_JJ-WU8VosS6Xlcpj0GyuduRfeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce949aeb8c.mp4?token=hPzjEZGk_d8-89PM7m-CbsOSNLnWboRKfY52bziwVxlmuWVzMdLNo54wUVk5EfGeJwUn2MDT0d3iJaYu19a12geAGfo6CYtoqq_73ZGAwG_anaWrjBmcA8mi_XD02sKhlUG6jBNsgyzGXdD9xUCmqrv-yzUTBhBQ4aFg4PlkpmVuqxTm3i9T4JehTcbdDFPtFV4Ct7QfmR1alJqdYCNdmsL0WbnIse5iQRoKwjqFQjtT4rIOgC-s3BpHydS03IFpwCgF0KmpsSk0-uSOLB8Ybo1GLlBwV04kQLPjlQGF4oGtuIYEtwffzkrZiGf_JJ-WU8VosS6Xlcpj0GyuduRfeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
حكومة إقليم كردستان العراق:
بعد اشتباكات عنيفة ألقت القبض القوات الامنية على وحدتين مسلحتين و21 عنصراً سرياً من تنظيم داعش في محافظة حلبجة، وصادرت كمية كبيرة من الأسلحة الثقيلة والمتوسطة والخفيفة.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/naya_foriraq/90355" target="_blank">📅 01:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90354">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
رداً على استمرار العدو السعودي المجرم في عدوانه على بلدنا نفذت القوات المسلحة اليمنية عملية عسكرية نوعية استهدفت من خلالها مخازن الأسلحة  وغرف القيادة والسيطرة التى تدير العدوان على بلدنا وشعبنا في القاعدة العسكرية بمنطقة شرورة السعودية.
وقد نفذت العملية بدفعة كبيرة من الصواريخ الباليستية والطائرات المسيرة وكانت الإصابة دقيقة ومباشرة بفضل الله وعونه.
نؤكد للعدو السعودي المجرم أن استمرار عدوانه على شعبنا سيقابل بعمليات أشد وأكبر فى عمق أراضيه وستكون عواقبها عليه وخيمة بإذن الله وقوته.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/90354" target="_blank">📅 00:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90353">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇸🇦
الاعلام الاجنبي:
‏أفادت تقارير بأن القوات المدعومة من السعودية في اليمن تضم بعض الكتائب التي تتألف من نحو 80% من "الجنود الوهميين"، وهم جنود مزيفون موجودون على الورق فقط لتحصيل رواتبهم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/90353" target="_blank">📅 00:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90352">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇷🇺
🇺🇦
الكرملين
: اجتماع بين فلاديمير بوتين و زيلينسكي في قمة مجموعة العشرين التي ستعقد في الولايات المتحدة أمر مستحيل.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/90352" target="_blank">📅 00:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90351">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfe21f1049.mp4?token=v_cz2VPo1NEglovCxhd1cIDUSI3QDUwsHGV7eKp23_lb_ulw3IKr-J-l2csfnow-uyCrJcWaC_E4Jbgyxy5LAOcN3_n_dszk6lQ1yq-3RlZwLxpCLjLU-Ol69sO4vQo1mJaDD9dJgMnV9xqEOBeXEcxdtPA6Jly7zSYMO0FTUFVlVboEMhU6b65btKL7_EMxa9ABVZViW7IfMHuiOVrscCUdRsMdQKkfvf15vDU5W0U-Z_aQkEyCb2HKOBegsY3mAlfxOAoynIFJzxlHpIcuPKzkGlIxLr23aQ9FQuJEwOrcs2nMxnXHbY7aIySMUJ6egOTafBRJYoplsGvGTIerPllzprDZGc5dBCT9qQjk8oH_WnwRKFUz_mVgfjaE7ws9OunDgO6Z2ueUVn4coVWQEG53io6gnV7B_BWysvOwCvaLMAsT8sjj5SKISzYIY5bIUbY1znUzlx0FOs8-KAvSMRVD-BIpiy0qqo0b038nUdlNk0GiDAhKpcRIzP2-q3OpLU9Z4WyKUeSbIgoS09WuW7gg74gf0raY7DmG13tZaJYe6OpLLOnUz3UUd14_FPOX8wssTjliUianjtdcs4W6qG2b4Juw6iWk9zAOA0Tksil3z0d0FGcoaomWOz2wP721qNK6YdE2kyio7SZZJqRiNyYIGIJhTW1Uv0m1OjbY08k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfe21f1049.mp4?token=v_cz2VPo1NEglovCxhd1cIDUSI3QDUwsHGV7eKp23_lb_ulw3IKr-J-l2csfnow-uyCrJcWaC_E4Jbgyxy5LAOcN3_n_dszk6lQ1yq-3RlZwLxpCLjLU-Ol69sO4vQo1mJaDD9dJgMnV9xqEOBeXEcxdtPA6Jly7zSYMO0FTUFVlVboEMhU6b65btKL7_EMxa9ABVZViW7IfMHuiOVrscCUdRsMdQKkfvf15vDU5W0U-Z_aQkEyCb2HKOBegsY3mAlfxOAoynIFJzxlHpIcuPKzkGlIxLr23aQ9FQuJEwOrcs2nMxnXHbY7aIySMUJ6egOTafBRJYoplsGvGTIerPllzprDZGc5dBCT9qQjk8oH_WnwRKFUz_mVgfjaE7ws9OunDgO6Z2ueUVn4coVWQEG53io6gnV7B_BWysvOwCvaLMAsT8sjj5SKISzYIY5bIUbY1znUzlx0FOs8-KAvSMRVD-BIpiy0qqo0b038nUdlNk0GiDAhKpcRIzP2-q3OpLU9Z4WyKUeSbIgoS09WuW7gg74gf0raY7DmG13tZaJYe6OpLLOnUz3UUd14_FPOX8wssTjliUianjtdcs4W6qG2b4Juw6iWk9zAOA0Tksil3z0d0FGcoaomWOz2wP721qNK6YdE2kyio7SZZJqRiNyYIGIJhTW1Uv0m1OjbY08k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انباء اولية غير موكدة عن سماع دوي انفجار في محافظة ديالى</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/naya_foriraq/90351" target="_blank">📅 00:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90350">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/654afe11fd.mp4?token=qjJ5u7twXWTYHMxDJ91uqDyMmMHpvR8AA0pAn0PXjphhXUW5i_VlDX5j4upYbdofuf-xyk2xH0STuD7cHyrduO7SXHBpN9fNjAwKPOjm_9u0kaseXo3ifcWJEOzoJ-8bHC3YLxQvvJdc2Bs6oepKveP7JjGC-Rw4oerC0FY-qv7_SE2f_Kjimvs_wiB3DjJCCqMrhF1suPQZ-4q7jaWT7TaBWSRBoowYj1NqHo6CCmYxWJ4UM5DvQ9YzqLzf_4FgLr96rA9mv6e-SY-YO4ynTfz7sD0lZ37JAODOwkK9foU_9QTdGJ_nwuN_L-m7iyCpQfB1Wpu-i54a-2YFN0BrMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/654afe11fd.mp4?token=qjJ5u7twXWTYHMxDJ91uqDyMmMHpvR8AA0pAn0PXjphhXUW5i_VlDX5j4upYbdofuf-xyk2xH0STuD7cHyrduO7SXHBpN9fNjAwKPOjm_9u0kaseXo3ifcWJEOzoJ-8bHC3YLxQvvJdc2Bs6oepKveP7JjGC-Rw4oerC0FY-qv7_SE2f_Kjimvs_wiB3DjJCCqMrhF1suPQZ-4q7jaWT7TaBWSRBoowYj1NqHo6CCmYxWJ4UM5DvQ9YzqLzf_4FgLr96rA9mv6e-SY-YO4ynTfz7sD0lZ37JAODOwkK9foU_9QTdGJ_nwuN_L-m7iyCpQfB1Wpu-i54a-2YFN0BrMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
توثيق من الجانب العراقي للطريق المؤدي إلى منفذ الشلامجة، حيث يظهر خاليًا تمامًا من حركة الوافدين والمغادرين عقب إغلاق المنفذ.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/90350" target="_blank">📅 00:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90349">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">كمين محكم على قوة مكونة من عشر آليات أثناء محاولة فرارها
عملية "والله أشدُ بأساً وأشدُ تنكيلاً"</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/90349" target="_blank">📅 23:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90348">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa40032226.mp4?token=PjUESaeWfMffsqiS2JQSRRdLsCw0gRhV7y90OPanRFhUEn192-DetFSymf0TkqVHARopmnVzAEEON4L-H7-9lnP3TkFGe1XwVa12zInGKI3iXu6UM8XNZGMgF4poVwe2nmr-TiYob-9EllmZvIHzYB-3ZOCsDImeXw4vhuzi9FJdqyoXU2fsrCtCykFhP_9j7E2RRC-Ulr7yz1GadU4q1EVea1r7t82gh4n3WTvtEPqwJpVRSAcdU0fbkybwGX8okptW9FWIW41HoIH2y3NsplBujnbJXlke3Uab-lM1PUXuDfYVTJKOfMoIihPL518MjY7X4vzzeS-O6Y6bz4z1rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa40032226.mp4?token=PjUESaeWfMffsqiS2JQSRRdLsCw0gRhV7y90OPanRFhUEn192-DetFSymf0TkqVHARopmnVzAEEON4L-H7-9lnP3TkFGe1XwVa12zInGKI3iXu6UM8XNZGMgF4poVwe2nmr-TiYob-9EllmZvIHzYB-3ZOCsDImeXw4vhuzi9FJdqyoXU2fsrCtCykFhP_9j7E2RRC-Ulr7yz1GadU4q1EVea1r7t82gh4n3WTvtEPqwJpVRSAcdU0fbkybwGX8okptW9FWIW41HoIH2y3NsplBujnbJXlke3Uab-lM1PUXuDfYVTJKOfMoIihPL518MjY7X4vzzeS-O6Y6bz4z1rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انباء اولية غير موكدة عن سماع دوي انفجار في محافظة ديالى</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/90348" target="_blank">📅 23:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90347">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">انباء اولية غير موكدة عن سماع دوي انفجار في محافظة ديالى</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/90347" target="_blank">📅 23:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90346">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حدث امني في محافظة كركوك</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/90346" target="_blank">📅 23:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90345">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
ضغط مكتب وزير الدفاع بيت هيغسيث من أجل ظهور اثنين من الطيارين الأمريكيين الذين تم إنقاذهم بعد إسقاط طائرتهم من طراز إف-15 فوق إيران في مقابلة مع برنامج "60 دقيقة" للحديث عن عملية الإنقاذ.
كان لدى الطيارين في البداية مخاوف بشأن المشاركة وكشف تفاصيل عسكرية حساسة. بعد التحدث مع هيغسيث، وافق أحدهما على إجراء المقابلة بينما رفض الآخر.
كما أعرب بعض المسؤولين العسكريين عن مخاوفهم من أن المقابلة قد تكشف معلومات سرية أو تستخدم لأغراض سياسية.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/90345" target="_blank">📅 22:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90344">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">الله اكبر
سقوط مباشر في جيزان بالسعودية</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/90344" target="_blank">📅 22:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90343">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇶
تعرض ارهابي على نقطة تابعة للجيش العراقي في محافظة كركوك شمالي العراق</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/90343" target="_blank">📅 22:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90342">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حدث امني في محافظة كركوك</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/90342" target="_blank">📅 22:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90341">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">حدث امني في محافظة كركوك</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/90341" target="_blank">📅 22:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90340">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇶
الناطق باسم القائد العام للقوات المسلحة العراقية
: متأهبون لعدم تكرار مثل هذه الاعتداءات على السعودية.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/90340" target="_blank">📅 21:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90339">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مشاهد أولية من عملية "والله أشدُ بأساً وأشدُ تنكيلاً" العسكرية النوعية الواسعة من عدة مسارات متزامنة - 12 سبتمبر 2026م</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/90339" target="_blank">📅 21:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90338">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇾🇪
مشاهد الإعلام الحربي من عملية "والله أشد بأسا وأشد تنكيلا" العسكرية النوعية تعرض عند الـ 9:00م بعد قليل</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/90338" target="_blank">📅 21:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90336">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">انفجارات قوية في خميس مشيط</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/90336" target="_blank">📅 21:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90335">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/90335" target="_blank">📅 21:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90334">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">انفجارات في سعودية</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/90334" target="_blank">📅 21:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90333">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇾🇪
مشاهد الإعلام الحربي من عملية "والله أشد بأسا وأشد تنكيلا" العسكرية النوعية تعرض عند الـ 9:00م بعد قليل</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/90333" target="_blank">📅 21:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90332">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اطلاق صاروخي نحو مضيق هرمز</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/90332" target="_blank">📅 20:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90331">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e4cadf14a.mp4?token=hfAszbE0ex-8rc5bbuHMttloQPhyS4D89KOz9T_cMU2k9AgdU_eRS3YatRzUJv55A9O-40xyBYYLSAZZ7KC-5OXAPqrkZDqNS5I3HBrf4UkSc7endtu4KvZ2tXmBhu8rXmK4fe7orFJeJZtfe7K3IolJwxKcH8XEoNXvpoPEcaksR1iieFzcR0_gJksjx9gy_xTvJyD2llqr-9ee9oO9DYTqdL7kS5kCIvJwCyG4H13h1bYeTdLLZC2kPbe_xZTo-9HN7FzE7sHXoarwa71Z4De83NRSHLerocjjnHkquHhwumOeCABYs1rLqD9nkJ2m8qc6kh2X9_Om1RJrw6uk_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e4cadf14a.mp4?token=hfAszbE0ex-8rc5bbuHMttloQPhyS4D89KOz9T_cMU2k9AgdU_eRS3YatRzUJv55A9O-40xyBYYLSAZZ7KC-5OXAPqrkZDqNS5I3HBrf4UkSc7endtu4KvZ2tXmBhu8rXmK4fe7orFJeJZtfe7K3IolJwxKcH8XEoNXvpoPEcaksR1iieFzcR0_gJksjx9gy_xTvJyD2llqr-9ee9oO9DYTqdL7kS5kCIvJwCyG4H13h1bYeTdLLZC2kPbe_xZTo-9HN7FzE7sHXoarwa71Z4De83NRSHLerocjjnHkquHhwumOeCABYs1rLqD9nkJ2m8qc6kh2X9_Om1RJrw6uk_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
من الاضرار التي لحقت بمصفى جيزان التابع لشركة ارامكو السعودية اثر الضربات اليمنية.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/90331" target="_blank">📅 20:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90330">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وكالة تسنيم:
أشار المصدر المطلع إلى أن العراق سيحضر الاجتماع أيضاً، إلى جانب إيران وعمان والدول الأخرى المطلة على الخليج الفارسي. ومع ذلك، سيقتصر دور هذه الدول على الاطلاع على نتائج المفاوضات الإيرانية العمانية، حيث تم حسم القرارات المتعلقة بتفاصيل الاتفاق خلال جلسات فنية بين الجانبين الإيراني والعماني، مضيق هرمز لن يعاد فتحه بموجب التفاهم مع عمان.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/90330" target="_blank">📅 20:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90329">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
شن طيران العدو السعودي خلال الـ48 ساعة الماضية 129 غارة جوية توزعت على محافظات تعز ومأرب والحديدة والجوف وصعدة وعمران وحجة.
تم تنفيذ هذه الغارات بواسطة طائرات F15 وتايفون وأقلعت من القواعد العسكرية للعدو السعودي في خميس مشيط والطائف.
إن هذه الاعتداءات على شعبنا لن تمر دون رد وعقاب بإذن الله وقوته.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/90329" target="_blank">📅 20:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90327">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a60a908ab2.mp4?token=I3y3r_7idcUXIgCIsg24VyAlZxIvXkmgA9qTWly5CANwmA67duAlbwN-N76UlDOYTRXM_GPt28ADcJfBtyrXMFdUIl0SpUzPbyj6PuEeB5hoAn7nj-1QwPXvAkFBWoyMXXe7KlKZKVMqH7BfylbZ7rpJx6wAyzbhx7JQoqHkETrbng6afD_TMrqEjJSB9VOAZHEBP-XmjvMriTu0JvwgocqUkl5egiqEPwRBFNDQqub5Fg0Ug6eBkZDxQEQ78FhEod2P0q7rPAgiBprkiCap4n71q3U1RNPThHLDEWutZT-_5hDhxTL8ditXj_x3JsTPXy6-tHI7JSJuoJBcUKRwnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a60a908ab2.mp4?token=I3y3r_7idcUXIgCIsg24VyAlZxIvXkmgA9qTWly5CANwmA67duAlbwN-N76UlDOYTRXM_GPt28ADcJfBtyrXMFdUIl0SpUzPbyj6PuEeB5hoAn7nj-1QwPXvAkFBWoyMXXe7KlKZKVMqH7BfylbZ7rpJx6wAyzbhx7JQoqHkETrbng6afD_TMrqEjJSB9VOAZHEBP-XmjvMriTu0JvwgocqUkl5egiqEPwRBFNDQqub5Fg0Ug6eBkZDxQEQ78FhEod2P0q7rPAgiBprkiCap4n71q3U1RNPThHLDEWutZT-_5hDhxTL8ditXj_x3JsTPXy6-tHI7JSJuoJBcUKRwnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
غارات من طيران العدو السعودي يستهدف محافظة البيضاء.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/90327" target="_blank">📅 19:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90326">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQ5RXIf7vvwyV3EG97bkrHAYpm5xmbISVJqY7mNJleu2qyF7Z7JOo2HlJhWIWZXEqzYiroG1kfZlY58v-hzv1HFCaANtJlXbYG-IYJhHe_xu6gALntwtE-3RFiUnOaiiJFYgyBFBB-2PXVSkOQW9TWBMiTbZiDfS144RcwSz418263s7bwxSaHnZWkOkcNOpsfO0M6rGtpi3DgYOQjnwweYyqwelCpwsnP8JLOWX6e5oHd8f-LYIdlEF56-8sYIvnL0Iocpc6b74KgN0GFuM235IFAr5S6tqErsBWXuEtrWWft-1zKxnR9a8o7qFsWm9SAJ1t7nG-0zEEpkQwvjmow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
غارات من طيران العدو السعودي يستهدف محافظة البيضاء.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/90326" target="_blank">📅 19:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90325">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85a33591f6.mp4?token=ULxADojZWtEYEoNL6Kzf2l9EfAzmPIJHJ3rdth3Y9KALlq2Geutf_e3BLYjoisNnS_dRlkw0ZqliUJKnTzveWblei7ILS51tsEF2Xwm4gkXv7u7wCevCaujDYmxmKgHujYK0tPyCOK9jfsITSRbTJ77CL6DVujEE_j8Yv04qaVEH9-eieeucZfx6Zkw7GtmtPmqLcGJ1d_NFDLXNlwJW4tb9TFRg0iXfBI7INB_aqvRd5yqej3Q-cF36K10WLLjr5ASnf4-QfzMZfp3H1waC8D7bCWYQMSerradDRGNqi8YzS7psC5XskHN1HJWmsC2d7oYp-bgseNgy_W4177OKVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85a33591f6.mp4?token=ULxADojZWtEYEoNL6Kzf2l9EfAzmPIJHJ3rdth3Y9KALlq2Geutf_e3BLYjoisNnS_dRlkw0ZqliUJKnTzveWblei7ILS51tsEF2Xwm4gkXv7u7wCevCaujDYmxmKgHujYK0tPyCOK9jfsITSRbTJ77CL6DVujEE_j8Yv04qaVEH9-eieeucZfx6Zkw7GtmtPmqLcGJ1d_NFDLXNlwJW4tb9TFRg0iXfBI7INB_aqvRd5yqej3Q-cF36K10WLLjr5ASnf4-QfzMZfp3H1waC8D7bCWYQMSerradDRGNqi8YzS7psC5XskHN1HJWmsC2d7oYp-bgseNgy_W4177OKVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تدمير 6 خزانات نفط على الاقل في ابها</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/90325" target="_blank">📅 19:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90324">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6722e8cb2c.mp4?token=YXXcct5_IJ4pFH9Bd91UwQuzW5L7-Pn0lNstgYhDbIYNBx0roG4WQ4J9Ed2sNFiNjwTb8qYhcvLHH4NWcLa5PXUs6Mz0H9-UwisIYmd-2GEkMMUfz4eIu1lboFnA2U_nfRu89biw8p0tIJOYmQhdG6Ibn37_0VI-p41-Au2UcmWB5SrldfbVTtWjuXSokiWagMW6izKOfbr4T1dVv2APu1VELHMj91pXobNTYjDBrEG1URjJsfIJiXhzvxzpyvCShshKZYTHtv-vIjDG8xYiofC7GZewcvj05TlgjTRHrZM5W6Jra8selRdD0NZqpvrxk0L1k3b9A80eF9j4_X33nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6722e8cb2c.mp4?token=YXXcct5_IJ4pFH9Bd91UwQuzW5L7-Pn0lNstgYhDbIYNBx0roG4WQ4J9Ed2sNFiNjwTb8qYhcvLHH4NWcLa5PXUs6Mz0H9-UwisIYmd-2GEkMMUfz4eIu1lboFnA2U_nfRu89biw8p0tIJOYmQhdG6Ibn37_0VI-p41-Au2UcmWB5SrldfbVTtWjuXSokiWagMW6izKOfbr4T1dVv2APu1VELHMj91pXobNTYjDBrEG1URjJsfIJiXhzvxzpyvCShshKZYTHtv-vIjDG8xYiofC7GZewcvj05TlgjTRHrZM5W6Jra8selRdD0NZqpvrxk0L1k3b9A80eF9j4_X33nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صور الأقمار الصناعي تظهر حدوث أضرار جسيمة في محطة أبها التابعة لشركة أرامكو في أعقاب هجمات انصار الله، حيث تم تدمير ستة خزانات نفط على الأقل بالكامل وتعرض ثمانية خزانات أخرى لأضرار طفيفة.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/90324" target="_blank">📅 19:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90323">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMqMrr1LX7KCafS-oRqbjVdo2I-OrRLpAW1OmCHdUhEjAFGHyUWurB2ZoNyj94TsDsRwSDKU6hBl7ZAaWkvwfgrQvDrx-sHmaaEwIz2ribScwmSkhf7su474wLIz8j-lVIA5i4UW_vHN1lNDMu6nzBo3UigDYzpWTrOXbdpdTT4GyJZEAIg8hxuOQ_286q-2FpCJy-4u0Ay3-wqpdMONMGxbuaI073Dgw25n-SAsWMpuME2g0vRwdl6mhPH8j_m1GrTNaWWz1Atm79vf1XcMnWcWKp5K8deC5l3O1hpRW4N5KR3qxJBtWdVsP0zde3Qd1SIHa9ukjR_Rhmn_dS93oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صور الأقمار الصناعي تظهر حدوث أضرار جسيمة في محطة أبها التابعة لشركة أرامكو في أعقاب هجمات انصار الله، حيث تم تدمير ستة خزانات نفط على الأقل بالكامل وتعرض ثمانية خزانات أخرى لأضرار طفيفة.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/90323" target="_blank">📅 19:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90322">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">العراق يعيد اغلاق منفذ الشيب مع ايران</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/90322" target="_blank">📅 18:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90321">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇾🇪
🇾🇪
وزارة النقل اليمنية: باب المندب سجل عبور 36 سفينة في 10 سبتمبر و37 سفينة في 11 سبتمبر.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/90321" target="_blank">📅 18:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90320">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇮🇷
وزارة الخارجية الإيرانية:
تفاهمنا مع عمان بشأن ممرات العبور في مضيق هرمز لا يعني بالضرورة أن المضيق آمن للملاحة.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/90320" target="_blank">📅 17:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90319">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇾🇪
🇾🇪
وزارة النقل اليمنية:
باب المندب سجل عبور 36 سفينة في 10 سبتمبر و37 سفينة في 11 سبتمبر.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/90319" target="_blank">📅 17:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90318">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69e86b9dc9.mp4?token=JU6dPxXqDkwKzdpAy83qwF5992lyrkwSXrHyKLLThOSJwnXpStK1oo14zScj0E0fN0AC8qaJQ0yw5HRq_IGGB3sD9vu0EzppYWQ8uW8-NBSn4Evp94zaLp8b5jg2knmN_RZ39k3kCur_4uoXkW089HJUB7Bdo1TMjgLYWAf3zaucdnYdGMWAG45cpTcjlg02BOAXRAtWz_JezGgSv5yHWeNkqjFT0FtM1csyk5u7x7nG87J7S2sOI5eN-ybKnKPykux7pl488TkRlCK48lmyA1j8xwl_zi7Ts8bzJhqwaUVByaKpfgsTTyEjr0B71tixYnEjnzooK0PSW9t6NJaYrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69e86b9dc9.mp4?token=JU6dPxXqDkwKzdpAy83qwF5992lyrkwSXrHyKLLThOSJwnXpStK1oo14zScj0E0fN0AC8qaJQ0yw5HRq_IGGB3sD9vu0EzppYWQ8uW8-NBSn4Evp94zaLp8b5jg2knmN_RZ39k3kCur_4uoXkW089HJUB7Bdo1TMjgLYWAf3zaucdnYdGMWAG45cpTcjlg02BOAXRAtWz_JezGgSv5yHWeNkqjFT0FtM1csyk5u7x7nG87J7S2sOI5eN-ybKnKPykux7pl488TkRlCK48lmyA1j8xwl_zi7Ts8bzJhqwaUVByaKpfgsTTyEjr0B71tixYnEjnzooK0PSW9t6NJaYrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تتقدم في تعز وتسيطر على مواقع استراتيجية بعد اشتباكات مع مرتزقة السعودية</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/90318" target="_blank">📅 17:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90317">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">القوات المسلحة اليمنية تعثر في باب المندب على احدى سفن العدو الامريكي والاسرائيلي التي دمرتها القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/90317" target="_blank">📅 17:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90316">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">انفجارات سمعت بوضوح بالجانب الشرقي من السعودية</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/90316" target="_blank">📅 17:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90315">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/90315" target="_blank">📅 17:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90314">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/354f2e2cdd.mp4?token=UxLCD8fHvAdGV3ry9Prw9KD8_AXobuOkTFb5LAqWaUaJcm9SxQv6aW_R_YuNv9ZT4bU02KN4DqDU657bH4CkLeuEdZVOo67zqfK3mDrNLo9UEvkOgu31M0tA4aFX17bwZLqI9HIGGwDCHQNq5DnLOp8X3wZUbnrXte69fauQzwXmfdjSaVSyRJWRxamniraLvHEO2HOmSSR6kw8HJk5rK32ypVE_RWNP2eeUbXaMfICnewAjAJcrfyahCme_V2hacLX0hT9jb51rCz8Z55jEBm1-Y-Fj8spuaUqlry1lofPsr8H-ukEdJ_bQUWZU4TLOY7s2Q2NiOBalKHFMlrSza6ZuqQ6QKaVc3eNeikoDpcAd1f1I2I5f0Ol4h64BGQJFWP6ppw9M872upkwUDuVNxA7kPTAOv2JRQXHR0aZX1-liGhSmPIcgdSCZ22LrgXf6YCCphXZfrIP-nz02RxI_41KjZl1J9jVtIfzvEHTmWkKRWCEAZuKE9Fdp3ECbEr_vq2hxOXQTK7NwYL2vvUjUYUa4YqazlC2p813ci6V7ShIXzIM2LXdMXJeweWwzn0tbdEfLnNPOrLGSeP7TtXmNb_RSLzouJHiHkv1uyIGifwbzPsTinPTEb7RiO5aUL2qU5jqhCgUL0Ly0qWBmx0C72BOpLnRL5MfyLFdf6Zx9cH8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/354f2e2cdd.mp4?token=UxLCD8fHvAdGV3ry9Prw9KD8_AXobuOkTFb5LAqWaUaJcm9SxQv6aW_R_YuNv9ZT4bU02KN4DqDU657bH4CkLeuEdZVOo67zqfK3mDrNLo9UEvkOgu31M0tA4aFX17bwZLqI9HIGGwDCHQNq5DnLOp8X3wZUbnrXte69fauQzwXmfdjSaVSyRJWRxamniraLvHEO2HOmSSR6kw8HJk5rK32ypVE_RWNP2eeUbXaMfICnewAjAJcrfyahCme_V2hacLX0hT9jb51rCz8Z55jEBm1-Y-Fj8spuaUqlry1lofPsr8H-ukEdJ_bQUWZU4TLOY7s2Q2NiOBalKHFMlrSza6ZuqQ6QKaVc3eNeikoDpcAd1f1I2I5f0Ol4h64BGQJFWP6ppw9M872upkwUDuVNxA7kPTAOv2JRQXHR0aZX1-liGhSmPIcgdSCZ22LrgXf6YCCphXZfrIP-nz02RxI_41KjZl1J9jVtIfzvEHTmWkKRWCEAZuKE9Fdp3ECbEr_vq2hxOXQTK7NwYL2vvUjUYUa4YqazlC2p813ci6V7ShIXzIM2LXdMXJeweWwzn0tbdEfLnNPOrLGSeP7TtXmNb_RSLzouJHiHkv1uyIGifwbzPsTinPTEb7RiO5aUL2qU5jqhCgUL0Ly0qWBmx0C72BOpLnRL5MfyLFdf6Zx9cH8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">النقطة الاهم في العالم - مضيق باب المندب</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/90314" target="_blank">📅 16:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90310">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mwJZGu_OQazRlpoOOcrzQUzUcn6QrSXlH4HhaENWAqqFSCXnsnjr4hI56HHb4BxowFwRwlf_GlUH_-7jUnptGsaS9E1Kk0swFMbpj_NGZfDQ5iSM_3OLEIc5EAzZp0ckb_xnNFswy4liBhPZyfSx3tngBz9sB63HPboV6HETcI9bMl74kcxSvQ4JcHDpGHLLbHitThOBCo-xL696XRqsMR5twHVKJPIkFoOO7ZS55f4tdrbfQi0RWpcTDrW3shGsxBBMpVZPd_GLiOlZV1ikuJ9nyxy21OXCiliaOhLVg3LIX8sNHwoYQMVuIraLMqlVw2YmbvoAer-HtpqPQS2e6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hOtv0NLGcBmj13P5teMJpkJh_eTcuI5g1ONDkCXih_UFnk4ebeT5TyHfsd2LzWo9Nq3ItBlqLTsxEav2-LKzocvrf_c8G_qyEpFvqIsXZcGpxNBEtv3yDAosVfmHKvDdCguBVYXE3btFnFTu1xqg1XdlJ3kFWN6L3bBEf4_dphTxx161JenloMN43NLsmgttA42I8edVmMXiVesAOg2CqljNE_nrjfWP6lcQ2qKeNwv-8A4q6XKkiwGsyrl2H5IjW7h-jE0OLOGdB1jsxHE-dQDVTN0PY73ATyw5J_-63iiOvK7vnB3zpCHLI40RntcVFgEuN205XYQM43U-ShYtCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XStdPzm56F4MJeIhDEdKtz0ARI78Gr9oXHvZHeXJZp2oiNDgqTmLaFjnCWlSxKyK4xSXgH6_BAZoFUBkah16rchyF-AH5_ZGoCntt7i2UQBoEnzgDxCWBYyVTGd2q9jLLpQ3-SJsRXtqHBYPMXacxWHnuC4hHHsRShJSC1Q7Jozr81yptcxIir9vnsdnVO_7Xeuo1Z6NVw1E614JtuB1Yo6kQDjIsqdyidK2coTPnS-phqVH3CFj4vXd1YjY7YvXPF4Z75axGo9zBaJBzTWw8FXdEIHtLIxoG-C4D8zecGvoIwznya6FIA4sFNaR9t6vuXK_wGdU52o7YqXNmwh_JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J_61IVFpH2L9noSk0qW-1NyLoNbQhxdl1NtXI0pxPpJTMBqPy3BQMqN2jiJ5mDA896K4V8hoYooVV_3GiCH8tEWOWl-PI3mgUcq7gz3A8eXUeagjGx8O0BiRWzw0Ps2iOzuEaCSIV8rLxPrQG0B1Lpqz3pt968Up0A5hPrnM03zdaTvXNatk3RrbbvaXYOyDaCUDrSgwyp5av6bxRDOqzjv8CvD1msjho6kHUBfSGB35yjp7HUQAxesnb5nH8v_o_1fNFGXwVXuq0vl3MewVUp7r6Zzpi-Lj51VGDS6Vq5_zb1oT-KOKVKKP1d7NE2yGBNzSg5eTBef9h4iOk-lsAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بعد ادعاء المرتزقة يوم امس انها سقطت بيدهم.. محافظ البيضاء التابع لانصار الله يتفقد أحوال المرابطين في مديرية الزاهر.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/90310" target="_blank">📅 16:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90309">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇶
🇮🇷
مكتب رئيس الوزراء العراقي:
الموافقة على طلب الجانب الإيراني لإجراء تحقيق مشترك بشأن العثور على منصات إطلاق طائرات مسيّرة قرب الشريط الحدودي العراقي الإيراني.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/90309" target="_blank">📅 16:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90308">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">المدن اليمنية تواصل استقبال الاسرى المحررين من سجون مرتزقة السعودية</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/90308" target="_blank">📅 16:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90307">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇷
المتحدث باسم الخارجية الإيرانية: خطط لعقد اجتماع إقليمي يضم العراق ودول الخليج الفارسي.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/90307" target="_blank">📅 16:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90306">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">استقبال يمني رسمي وشعبي للاسرى المجاهدين المحررين من سجون مرتزقة السعودية</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/90306" target="_blank">📅 16:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90305">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇾🇪
🇾🇪
نائب وزير الخارجية اليمني:
النظام السعودي يسعى لتخويف المجتمع الدولي وتضليله، ونؤكد التزام صنعاء بالحفاظ على سلامة الملاحة الدولية.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/90305" target="_blank">📅 15:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90304">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇷🇺
السفير الروسي لدى اليمن:
نؤكد دعم بلادنا للجهود الرامية لخفض التصعيد وتحقيق السلام في اليمن والتخفيف من المعاناة الإنسانية.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/90304" target="_blank">📅 15:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90303">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">التلفزيون العراقي يقول ان لجنة أمنية رفيعة المستوى وصلت إلى منفذ الشلامجة للمباشرة بـ"التحقيقات في الخروقات".</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/90303" target="_blank">📅 15:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90302">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">استقبال يمني رسمي وشعبي للاسرى المجاهدين المحررين من سجون مرتزقة السعودية</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/90302" target="_blank">📅 15:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90301">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVnumS-6Whwh2bzfghDLxvpiIyf2ltrg_dNbCDkWdpsJBJBOjVvd0hiCu2YRx4fPgFWBG4H38zdFHRu5gxz9Em3MzdMk4F6jft6KZulW9_H2p4KnHRC8aSyODEzPLiX9GcCTMeCpbTaWjqs9F8Os9eCXJ29UBO6VKqCAmA_-ZnFiONyfr9JIoD-NQl8rGAcgEMXZnuZpO0SbPutJWV9PYwaExcJd0BKPYF5syUbPzfAh1ym6jAdKXu_M9YMSN0X-FXbCdN69BjK55u69YYMw1uvpGMWKSCUI-F8HovWUi5bXTKohOrL5KrINVBPWseUJfPgnhsiCbA2RpNSZ41_9oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب حول الهجوم على خط الأنابيب السعودي: الحوثيون يتجنبون الصدام مع الولايات المتحدة.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/90301" target="_blank">📅 14:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90300">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
ترقبوا مشاهد من عملية "والله أشد بأساً وأشد تنكيلا" العسكرية النوعية.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/90300" target="_blank">📅 14:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90299">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اعفاء قائد شرطة ميسان من منصبه</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/90299" target="_blank">📅 13:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90298">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اعفاء قائد شرطة ميسان من منصبه</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/90298" target="_blank">📅 13:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90297">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رئيس الوزراء العراقي يوجه بالسماح بدخول العالقين من المسافرين في الجانبين بمنفذي الشيب والشلامجة الحدوديين</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/90297" target="_blank">📅 13:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90296">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامب حول الهجوم على خط الأنابيب السعودي: الحوثيون يتجنبون الصدام مع الولايات المتحدة.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/90296" target="_blank">📅 13:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90295">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c12c317f4b.mp4?token=lyqZhtAlK_eQ5AMVi9sWFTxyEOfNBsdvDeH5oFkHuc-PNkXiiA7SNWXGY4pCp2MAqQ_zOKjJ_Ek1yepk-IBI8_1UDDOGpwQ9vsuYygw7CF8fuCzXmbwvooByU_tUiRwzCfBPnQImgeVG3Kz6TC2zQvdMP1SYzKA8OIP3smTvNo-6U5arauxI1u1ZyfN22z5Cm2Qpt2vJHKTf_w4PxzAK_tqpwmtScIkL2YHUJ_8ntJXGXl2nfC8ig_uvi7yLztx7NfVuTGCvMykmCfT8nUYdweQEMQZuhomX_VQh9h8X8q5dw_R5ItCJsBRiVkekosxBantaMqRCtEC20eFVNrh_YbV76Zv63_JB-RKhKVn0NlDN0v1K_wpkMAHJSJs2pLpGjy8sv2hvL1NwOeNTH8ycM03YteGFAvUXcLrKqwcfBBrwtckF8zIAd4oZ-rN5OOUBLgzE6_wvohpI0JfjXR61V16vISdbf1wiIZo91erETofBuVjbgYeYInDg1Qsogu-F-3nv9GiwXVyOaAHIs-YE7dySGuNSQPWvNiBJisxfCVJY-C76NzpeSrBstngHIOTDlez-17aS8duaJTeyFAQ08tqGHityjuwe8yAHGr7WyqTYTORGeFU9f13jIb7XD646Vw-15abbYhCJhKgjm-JiBF7WtgAyZkNeomITrVpl4Ns" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c12c317f4b.mp4?token=lyqZhtAlK_eQ5AMVi9sWFTxyEOfNBsdvDeH5oFkHuc-PNkXiiA7SNWXGY4pCp2MAqQ_zOKjJ_Ek1yepk-IBI8_1UDDOGpwQ9vsuYygw7CF8fuCzXmbwvooByU_tUiRwzCfBPnQImgeVG3Kz6TC2zQvdMP1SYzKA8OIP3smTvNo-6U5arauxI1u1ZyfN22z5Cm2Qpt2vJHKTf_w4PxzAK_tqpwmtScIkL2YHUJ_8ntJXGXl2nfC8ig_uvi7yLztx7NfVuTGCvMykmCfT8nUYdweQEMQZuhomX_VQh9h8X8q5dw_R5ItCJsBRiVkekosxBantaMqRCtEC20eFVNrh_YbV76Zv63_JB-RKhKVn0NlDN0v1K_wpkMAHJSJs2pLpGjy8sv2hvL1NwOeNTH8ycM03YteGFAvUXcLrKqwcfBBrwtckF8zIAd4oZ-rN5OOUBLgzE6_wvohpI0JfjXR61V16vISdbf1wiIZo91erETofBuVjbgYeYInDg1Qsogu-F-3nv9GiwXVyOaAHIs-YE7dySGuNSQPWvNiBJisxfCVJY-C76NzpeSrBstngHIOTDlez-17aS8duaJTeyFAQ08tqGHityjuwe8yAHGr7WyqTYTORGeFU9f13jIb7XD646Vw-15abbYhCJhKgjm-JiBF7WtgAyZkNeomITrVpl4Ns" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب حول الهجوم على خط الأنابيب السعودي: الحوثيون يتجنبون الصدام مع الولايات المتحدة.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/90295" target="_blank">📅 13:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90294">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ii91dk1dRu-IrqDFPGqfTwymLmlbRPky10AW3mqNSfh1TR6zDJSaPdITmHSlvyz7Oj1d1CKO4cFl9b_KAdAAnuXiKpR3wyTMvOBWI00ggwWw4t0I0HDVIN8ttiDtshgOt7zUj2ImlQpw_PzjY9tIV4ufiGQZInBKJGeQxRgxhQkrHXSSTbgKYUR8bxi9q-Etx-ZDOzAE_pM-uUqjekrf9_NOOOCOBKdUFNTkYsi91s7vcx1cMVr72gh7mB-n2df-O_cpWGqyHemAZ75oqKbGcx7TvHL3KW8jjDF0laTbmfxMD--xag7gD4LxVg8fekKgNo5acc-aeD7gXfrWDJnpKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔻
رئيس المجلس السياسي لحركة النجباء مغردا:
نشعر بالفخر والاعتزاز ونحن نرى هامات اليمنيين مرفوعة بانتصاراتهم المؤزرة.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/90294" target="_blank">📅 13:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90293">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38811a403c.mp4?token=BA98DxUb-LmhzzA-GWZmrGNh5UY9BPCzaOj081ydz2LDQf5X97ZgokP-3B0yci_VVsJJZHTYF50vWcdnkvisdOOWTTDYEZe_qW8TEiW1ackveiPZpZz8gAAg5oCGjLqrA4p9G1o2o1maMGqDugD8dZgqwsorFZOIGZPGXVg4jd5Ncugffgaa1t7gvNZMHsEz3EYndLv58UnK4peJhADjegTuXALtFGkSpUXX46p3zK-sldeONkRmpH5Gx7WzWX1ybvTjjuRqesrCzihRWoMT5-2qLwykWIWO9KxA45tlK-y8i3jZfQjJAs53rWAj6IXRi6uUWrSuvCfL6HpidRWb7q_AP3zME6dBxGFb9CbvBKBC40qIvvrTKdjd7WxUwhq7bmWB2T3F6n9yHahFHo3PEob3nsc-udVFn_A7jMdoRHxPSF935FXUoYu19DhT8hH6dE60sRG3UsJMxLwmw86RyRINwBAXcDoDGKCV3if_hjXexWMybNyApj5JpI357f9kg7tjgdFw3qiZfbcq6oxMrc0PMTeQ_OrQlummJNIhHW4-zrv_DScP6J5-Y7jFZYsSgR2h0F6YRvnZwPYPPD0Tvx3AzRgNX58qMHiPFpH4EBZBIbI1ghTMtJvBD6AHvJKKZ3VUot4QRqL5rjtgYsnQwXm_TRxNK96wcAicsw2UOdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38811a403c.mp4?token=BA98DxUb-LmhzzA-GWZmrGNh5UY9BPCzaOj081ydz2LDQf5X97ZgokP-3B0yci_VVsJJZHTYF50vWcdnkvisdOOWTTDYEZe_qW8TEiW1ackveiPZpZz8gAAg5oCGjLqrA4p9G1o2o1maMGqDugD8dZgqwsorFZOIGZPGXVg4jd5Ncugffgaa1t7gvNZMHsEz3EYndLv58UnK4peJhADjegTuXALtFGkSpUXX46p3zK-sldeONkRmpH5Gx7WzWX1ybvTjjuRqesrCzihRWoMT5-2qLwykWIWO9KxA45tlK-y8i3jZfQjJAs53rWAj6IXRi6uUWrSuvCfL6HpidRWb7q_AP3zME6dBxGFb9CbvBKBC40qIvvrTKdjd7WxUwhq7bmWB2T3F6n9yHahFHo3PEob3nsc-udVFn_A7jMdoRHxPSF935FXUoYu19DhT8hH6dE60sRG3UsJMxLwmw86RyRINwBAXcDoDGKCV3if_hjXexWMybNyApj5JpI357f9kg7tjgdFw3qiZfbcq6oxMrc0PMTeQ_OrQlummJNIhHW4-zrv_DScP6J5-Y7jFZYsSgR2h0F6YRvnZwPYPPD0Tvx3AzRgNX58qMHiPFpH4EBZBIbI1ghTMtJvBD6AHvJKKZ3VUot4QRqL5rjtgYsnQwXm_TRxNK96wcAicsw2UOdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد لغنائم القوات المسلحة اليمنية من مرتزقة السعودية بعد فرارهم</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/90293" target="_blank">📅 12:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90292">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالإعلام الحربي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtfh0rFGmeShBzon_ZbSYLIQR0RaITQsbL47FP2PIfCMPrfk2TooEDlMTOtkBL1pa8ifvDBuPSMNOX4NhkbmYbEv2oTZHuXqNmtAplyK19G0aUJwdA2VG6rITfHCS5-V-6d-fxEMAzUeW97tXT-uiHR9SJwmlO9mA9foxMG8ZVWcRClhBTORziddrgv-1UPgbHeOc-qWznywV-DCUgTLHf3CNbgrlU87s3_SkXz99dQ0XuqXAR0WrM84XqFZ_yRg0UOEKqRezMjSgbAxILJx7Cj2SjLItKXULjvTs6T2_2Bef3iUHHbywpuew6HH0fHbyaqwbIBYBZRg51O10mTr6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحيم
​في الوقت الذي نبارك فيه للشعب اليمني الأبي انتصاراته الميدانية المتواصلة ضد القوات السعودية ومرتزقتها، نؤكد: أن الاتهامات الموجهة للمقاومة العراقية بشأن استهداف المنشآت الحيوية السعودية يوم الجمعة الماضي هي (شرفٌ لا ندّعيه)؛ ونُعرب في الوقت ذاته عن استغرابنا من تسرّع الحكومة العراقية في تبنّي هذه المزاعم دون الاستناد إلى أدلة موثوقة أو تحقيقات ملموسة.
​إن تكرار سياسة إلقاء التهم وصرف الأنظار لا يعدو كونه محاولة فاشلة للتغطية على الهزائم المتلاحقة التي تتكبدها القوات السعودية وأدواتها على أيدي أبناء اليمن الأباة.
​وإذ نجدّد تأكيدنا على الموقف الثابت للمقاومة العراقية في مساندة الشعب اليمني المظلوم والمحاصر من قبل النظام السعودي منذ أكثر من عقد، فإننا نحذّر من الانجرار خلف المخططات الصهيو-أمريكية الخبيثة التي تسعى لزجّ العراق في أزمات لا تخدم إلا أعداءه.
​وختاما، نُعلن استعدادنا  للمشاركة في أي لجنة تحقيق حكومية بقصد  الوقوف على الحقيقة، بدلاً من الانسياق وراء الروايات المشبوهة.
المقاومة الإسلامية في العراق
12 أيلول2026</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/90292" target="_blank">📅 12:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90291">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97ae1f3afd.mp4?token=jDmQOKgno-koiuFugfuK8UiIJfOUReUp0WmU4KLZWHpXuC5wbOG2CecjsYNUp7Bx7617OdT3Xij3or9gK4V--SeAlVbzUxl3khsowYpn8FEIV4fhyE2zU4w6rETGg0wtTwbDlRcId8Lttw6T_pGK7L_EQf4L23HbMl9UhAgDxLNDpuScFDoTKUi6ZQaPcfD7U55whyF15jJqFUD46c93vc9c1SJM-6XutuzKwpJ023XBWz3RPGSCHL0U411hSCy7bYUEdwfFrRQ-YTvw9sj_jHdBvReC1kevo5H5BaaDBsoqk60ncYnfIJhE-Fhd8gkjSHV0nCwTrulORF2LfkZGdE1eyA6aqbHGv12ii6gvqksEKwR-XbOvvmXNDSnmNpN0vCDXzzlhZyA0_3bodt_-8J1-8ohG8h0oUF1zmPaAZTKiurj-AnWYUQbPbip27bre2BNVTBbKqlihvSZ-CzmwtC0z2TN2GHJCyok-5faVKhAHUTLy-DOIDkNjvRO3ktP6599SfmWD9wGVId6jMuvYnYLA4q8avTPkJ7B6Sk7CXe6UHg6DeJQnRZKGCBeoh-4JV9CAAdFurM3oSdaj7lwGO4co7bFh7jrpsbrDxnFZBIjAuDKoWkrOCrSls1MlbYsG-BfyHe03nBu9d1C7mPBItSck9Cx12ieUNe3KmkB39to" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97ae1f3afd.mp4?token=jDmQOKgno-koiuFugfuK8UiIJfOUReUp0WmU4KLZWHpXuC5wbOG2CecjsYNUp7Bx7617OdT3Xij3or9gK4V--SeAlVbzUxl3khsowYpn8FEIV4fhyE2zU4w6rETGg0wtTwbDlRcId8Lttw6T_pGK7L_EQf4L23HbMl9UhAgDxLNDpuScFDoTKUi6ZQaPcfD7U55whyF15jJqFUD46c93vc9c1SJM-6XutuzKwpJ023XBWz3RPGSCHL0U411hSCy7bYUEdwfFrRQ-YTvw9sj_jHdBvReC1kevo5H5BaaDBsoqk60ncYnfIJhE-Fhd8gkjSHV0nCwTrulORF2LfkZGdE1eyA6aqbHGv12ii6gvqksEKwR-XbOvvmXNDSnmNpN0vCDXzzlhZyA0_3bodt_-8J1-8ohG8h0oUF1zmPaAZTKiurj-AnWYUQbPbip27bre2BNVTBbKqlihvSZ-CzmwtC0z2TN2GHJCyok-5faVKhAHUTLy-DOIDkNjvRO3ktP6599SfmWD9wGVId6jMuvYnYLA4q8avTPkJ7B6Sk7CXe6UHg6DeJQnRZKGCBeoh-4JV9CAAdFurM3oSdaj7lwGO4co7bFh7jrpsbrDxnFZBIjAuDKoWkrOCrSls1MlbYsG-BfyHe03nBu9d1C7mPBItSck9Cx12ieUNe3KmkB39to" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد من محافظة الانبار..
ازمة الوقود مستمرة في مختلف المحافظات العراقية.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/90291" target="_blank">📅 12:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90290">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇨🇳
🇺🇸
ترامب بشأن الرئيس الصيني: «يقول البعض إنه يتجسس علينا، لكننا نتجسس عليه أيضًا، ونحن جيدون في ذلك كذلك. نحن على علاقة جيدة. حقيقة أننا ننسجم معًا أمر جيد. نحن نتعامل بشكل جيد مع الصين الآن.»</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/90290" target="_blank">📅 12:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90289">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9397297397.mp4?token=aWaB_lD8vquaEzrlAKTgfwOEuk7nlWqfquIz7PQdpj-cjtqh68ourbESesSBaQrJbwD245u6kDc277oPGVpreFUHvQWQecPzlgc9JwTJCC-H0Jykg8XTr_Sfk-uv7mYYM790fdklgwvE9ZDOHIAJN-pu1sa00PFnI4C1Tp5LMW5qdJK2LnVoqbFehnfvlsjElQQg7lY0TM0yg8-2ECopXJ_dLqgWj44NZD5jMVRyg78Pd3mjt-8GyZ2LVNe3KogrsXE4wmxc3HkHdu7uc1bAFG1eGTTJJRKezl9ryYNNXREj-Ke-yXSrvYOi5ETrbG7srxEyktJqTEC1Rt-IvLH6Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9397297397.mp4?token=aWaB_lD8vquaEzrlAKTgfwOEuk7nlWqfquIz7PQdpj-cjtqh68ourbESesSBaQrJbwD245u6kDc277oPGVpreFUHvQWQecPzlgc9JwTJCC-H0Jykg8XTr_Sfk-uv7mYYM790fdklgwvE9ZDOHIAJN-pu1sa00PFnI4C1Tp5LMW5qdJK2LnVoqbFehnfvlsjElQQg7lY0TM0yg8-2ECopXJ_dLqgWj44NZD5jMVRyg78Pd3mjt-8GyZ2LVNe3KogrsXE4wmxc3HkHdu7uc1bAFG1eGTTJJRKezl9ryYNNXREj-Ke-yXSrvYOi5ETrbG7srxEyktJqTEC1Rt-IvLH6Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
🇺🇸
ترامب بشأن الرئيس الصيني:
«يقول البعض إنه يتجسس علينا، لكننا نتجسس عليه أيضًا، ونحن جيدون في ذلك كذلك. نحن على علاقة جيدة.
حقيقة أننا ننسجم معًا أمر جيد. نحن نتعامل بشكل جيد مع الصين الآن.»</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/90289" target="_blank">📅 12:26 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90288">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇶
مديرية شؤون المخدرات العراقية تعلن ضبط 150 كغم من المواد المخدرة وضبط 3 متهمين بينهم أجنبي بعملية أمنية في مياه الخليج الفارسي.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/90288" target="_blank">📅 12:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90287">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇶
رئيس وزراء العراق يعفي قائد عمليات ميسان من منصبه، على خلفية ثبوت انطلاق الاعتداءات التي طالت المملكة العربية السعودية من أحد المواقع داخل المحافظة.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/90287" target="_blank">📅 12:06 · 21 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
