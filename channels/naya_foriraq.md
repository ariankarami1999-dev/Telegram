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
<img src="https://cdn4.telesco.pe/file/vaRanIZNDwf-QqZfTsARwZwpyuHFubtXuM08ej6fT4jwyu3azQKFU87FAb-_4b89rf2YYubXM3C6xkPWc3K6Qikr_VvKWe1U8Tq7fzFoDC2B8WS-eT9_7r06HCZG32Pb8hoIZmBwfVyZ-4VHcp0rEghtzDU59J4TEQJvLMgFZwA8L9Ss2u3TneCBcWBO2GgakCcHAfuuo7VUKsPHZ6yCQAQEdTfLsM7CCYJ-9HJd5iPPVieocTVisme8hhYXk8BF6bF-oJMI7pmT-KNsxkB8cgOQ1NdOV_iaO1AFIYrLkAvoijhmFKVXtL9-gfZNCMyumURwLEUavQ2JvnUAseef9w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 273K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 18:58:47</div>
<hr>

<div class="tg-post" id="msg-87476">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cfc415cb3.mp4?token=EEvMOMfLXbfTyidqF7yTnrFtng0C-sdDEt2b9jRv9cYzrCzpZ5vRgM2uX4eiWNvppd8W-qbOHG_wmFhTnKVRADgHRCAOq9dcyZwGbqGuJpHHfPZY2g7y0H7793KZ8wyYSnIqKXVvi-IwbK8tzS7BpLvr6TK5mZ9lZvyWh-DImuQqi2_mxA5sh2E6DEd6TTG00kv9dmnV893kYuyCNNmzRXNn1YGPNxu6cr6IgIfKuAw4HibGb24TScBt7v9lgnhxNYtvSBZG6I4NB6I1_0DvLUABbxLocOGblXLqPnVHIsJiE3jCDAPWpdrK_p_Q4hRf_WpIjyX17CK4aQMHVS0yjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cfc415cb3.mp4?token=EEvMOMfLXbfTyidqF7yTnrFtng0C-sdDEt2b9jRv9cYzrCzpZ5vRgM2uX4eiWNvppd8W-qbOHG_wmFhTnKVRADgHRCAOq9dcyZwGbqGuJpHHfPZY2g7y0H7793KZ8wyYSnIqKXVvi-IwbK8tzS7BpLvr6TK5mZ9lZvyWh-DImuQqi2_mxA5sh2E6DEd6TTG00kv9dmnV893kYuyCNNmzRXNn1YGPNxu6cr6IgIfKuAw4HibGb24TScBt7v9lgnhxNYtvSBZG6I4NB6I1_0DvLUABbxLocOGblXLqPnVHIsJiE3jCDAPWpdrK_p_Q4hRf_WpIjyX17CK4aQMHVS0yjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
اشتباكات عنيفة بين عصابات الجولاني و جماعات الكوردية في القامشلي بسوريا.</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/naya_foriraq/87476" target="_blank">📅 18:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87475">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇸🇾
اشتباكات عنيفة بين عصابات الجولاني و جماعات الكوردية في القامشلي بسوريا.</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/naya_foriraq/87475" target="_blank">📅 18:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87474">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇷
مكتب قائد الثورة:
أوامر بتعيين عدد من كبار القادة العسكريين في الجمهورية الإسلامية الإيرانية سيتم نشرها خلال ساعة.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/naya_foriraq/87474" target="_blank">📅 18:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87473">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇺🇸
🇮🇱
اعلام العدو:
أميركا تواصل تقليص عدد طائرات التزوّد بالوقود في مطار بن غوريون، عدد طائرات التزوّد بالوقود الأميركية في مطار بن غوريون تقترب من مستويات وقف إطلاق النار.</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/naya_foriraq/87473" target="_blank">📅 18:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87472">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/naya_foriraq/87472" target="_blank">📅 18:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87471">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/naya_foriraq/87471" target="_blank">📅 18:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87470">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇶
🔻
هيئة الحشد الشعبي:  توضح هيئة الحشد الشعبي أن المقرات الوهمية التي أعلنت عنها وزارة الداخلية، والتي ادّعى القائمون عليها انتسابها إلى هيئة الحشد الشعبي، لا تمت إلى الهيئة بأي صلة.  وتؤكد الهيئة أن إجراءات إغلاق هذه المقرات ومتابعتها نُفذت ضمن عملية نفذتها…</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/naya_foriraq/87470" target="_blank">📅 18:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87469">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇷🇺
🇸🇪
جهاز المخابرات السويدي يزعم إحباط عملية استخباراتية روسية في السويد.</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/naya_foriraq/87469" target="_blank">📅 17:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87468">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇾🇪
🇾🇪
انصار الله يشنون هجوم مسير على مرتزقة السعودية في المخا.</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/naya_foriraq/87468" target="_blank">📅 17:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87467">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇶
🇮🇷
رئيس البرلمان الايراني محمد باقر قاليباف يزور العاصمة بغداد الأسبوع المقبل.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/87467" target="_blank">📅 17:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87466">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZACHpJfW9_ZaIKOYToc0CTSmYDjV_qal4Nyy7qOkzRMSB4uPs7bdLbYFee4DXGasxLxwmZKVK4uV9McoYemNKjcA4cPaI86lSHYCayn82jXPLvb-Rh-JqAo5nSxjxhulqRiTrnRjEn1IrQd-a4nin1fLelSK0W8rc0GvaY1tP4pZKWlNR0cYWQ4I9Nd0HgLv9EGSiN5OpYDe11cOd4841lCaUr7M6QBANND3o_W4N9L-yLE3VCO4pxpdq4qe2P0EBYzyna3BnCh8ETaW2QCLWQOIemXsFt1bCKQnQFIgjyx36ziqxH7Jt0OqaXP1N3XuDQfKlOGWAfnk-N2LyDdPmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
اندلاع حريق قرب مرقد سيد محمد (عليه السلام) في قضاء بلد شمالي العراق</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/87466" target="_blank">📅 17:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87464">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d385f60930.mp4?token=aUyZYvrZsf5ifqMKBNY97WRWdrOL9-MB_0fufwFOx0uyzc2XPH6s_E4I5BrhaSYSxr9Yq3sZEFM8bSganD4XB41uAT8Izz4_vD75wXkwXXaBxPYGwH97eRwCxZq16TpNEJvq-8ndVy3vSZymlDQOtrEPtwLZS8-TOu2d-86yOO0tIBVNHfVhBUdn34qC4UpKXBdmlcKku_-886OrHBLyfEmOS2jvAtIFTBZBcfWP94HZCYzXtb8Zn2CT4oIRn7R9KcVKquvKEiAnjJcRRsyP1PkH5bbwsAXtD-O8chAo5ziagmfPgMYLRYBaQkD2qq5G8zmZLhx3j6MYvLS1ReInMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d385f60930.mp4?token=aUyZYvrZsf5ifqMKBNY97WRWdrOL9-MB_0fufwFOx0uyzc2XPH6s_E4I5BrhaSYSxr9Yq3sZEFM8bSganD4XB41uAT8Izz4_vD75wXkwXXaBxPYGwH97eRwCxZq16TpNEJvq-8ndVy3vSZymlDQOtrEPtwLZS8-TOu2d-86yOO0tIBVNHfVhBUdn34qC4UpKXBdmlcKku_-886OrHBLyfEmOS2jvAtIFTBZBcfWP94HZCYzXtb8Zn2CT4oIRn7R9KcVKquvKEiAnjJcRRsyP1PkH5bbwsAXtD-O8chAo5ziagmfPgMYLRYBaQkD2qq5G8zmZLhx3j6MYvLS1ReInMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زلزال بقوة 7.1 درجة يضرب كولومبيا</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/87464" target="_blank">📅 16:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87463">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">زلزال بقوة 7.1 درجة يضرب كولومبيا</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/87463" target="_blank">📅 16:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87462">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca01a4bc22.mp4?token=v2PZrYexP0NJotF5BCMeEQ3WHdT4cO2x5CEY83cJByErKb1wFutaY86cW--1BQjzR3iU8Z8hzhE0u09hlr3CaKSSSb3A3jtxHBLi8ls_M1tP6cmRmVTjoAwMQvzr5DkYmpoO1NBw6mDMDnYL8Gkk5XQEL3jyq6mcm2a0UsAMNLnm3qeScbYVxTpFfO0I0QR-8Fm5ZmAydnJbc6r9fDFh0TxWRoOa09Np84mecjL_7GwVDyjHJY6xpYvYWzLif4M59Mpb__enK4VCLeBZUD_m18IEEF21spFb1sLLDqOhWSfiLIuhapDbjN8NKV_UauWDJmiHNAAXcM-d67DwZaI02A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca01a4bc22.mp4?token=v2PZrYexP0NJotF5BCMeEQ3WHdT4cO2x5CEY83cJByErKb1wFutaY86cW--1BQjzR3iU8Z8hzhE0u09hlr3CaKSSSb3A3jtxHBLi8ls_M1tP6cmRmVTjoAwMQvzr5DkYmpoO1NBw6mDMDnYL8Gkk5XQEL3jyq6mcm2a0UsAMNLnm3qeScbYVxTpFfO0I0QR-8Fm5ZmAydnJbc6r9fDFh0TxWRoOa09Np84mecjL_7GwVDyjHJY6xpYvYWzLif4M59Mpb__enK4VCLeBZUD_m18IEEF21spFb1sLLDqOhWSfiLIuhapDbjN8NKV_UauWDJmiHNAAXcM-d67DwZaI02A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات الامنية تعتدي بالضرب على المتظاهرين المحتجين على تردي واقع الكهرباء في محافظة ذي قار جنوبي العراق</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/87462" target="_blank">📅 16:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87461">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">الرئيس الايراني مسعود بزشكيان يلتقي قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/87461" target="_blank">📅 15:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87460">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇷
المتحدث باسم حرس الثورة الإسلامية:
صواريخنا لديها القدرة على التوجيه، وحتى بعض الصواريخ يمكنها تغيير مسارها في مواجهة منظومات الدفاع الجوي للعدو. حتى إذا تم تحديد هدف لصاروخ ما، يمكننا تغيير ذلك الهدف في منتصف المسار وتحديد هدف ثانوي له.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/87460" target="_blank">📅 15:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87458">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdivRDiHp4rAPLkkobrjGLfljsTWwRV0XTNG7aUNfKO9VByUVPg3np57GLE_DOAp92YnMOJvHyuKBTfqVQjMfJSys2JmNsKYKiiV1gLQKcdkiSIMLfjZTbO97KBY6NF3RAIYIO2In44OfLXsb2fbQIS6ntz48rJPbUGphjr6txHTuQSOhW_OMgIiFEgnxUCdiWFV618sUxfVBr5-k5d-f4kxnHP1uIZfJynruocirMTsQGyQ3Dk7Z-6rrIbzGPIkSWRnrEq11Q1nHqYcNSIW3wShKLkUilGEfIXgMQ_v13sSUXIzrJGx8CjQT-zf7NUMHclN4UFjDlj4Y5QkfYcltQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انه زمن الديكة الشرسة اذ ولى زمن الدجاج الابيض … بحر الما يغرك ينعبر كل يوم
؛ والديج ضربته توجع</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/87458" target="_blank">📅 15:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87457">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇶
مواطن من بغداد يتعرض لصدمة بسبب الارتفاع الكبير في أسعار الوقود في إقليم كردستان شمالي العراق وسط اتهامات لعصابات مرتبطة بعائلة البرزاني بتهريب كميات النفط ومشتقاته المخصصة للإقليم إلى تركيا ما أدى إلى شح الوقود وارتفاع أسعاره بشكل كبير على المواطنين.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/87457" target="_blank">📅 14:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87456">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd242d2b06.mp4?token=VK5qMjOU83AqDKa2f9zAqdteVx7qzm4gm8nIPSC3vTRBfUFdQw8632gIMDpvmpHtwB8_Y1NlNQW47F0Dii47OQ71OK42w37gj6gF_S8iKnEX1L11TlzYPRLMs61amiVdiPxOdr9KreOSbiyCMJIdnLS_yUip0yiK-nDI2kozk33Zd3AjOa75vjPnhLDcsS3G44VaJQFb5dsHuN-JRYzBRE2g5oNQYrA333cUT5gz2v9ft3K7M5uQqLcKhJzfVpGiPZT679Q6dVPGPv1GAjmYo37shWEIZug_SYJBZjM09yXIBf7FPQSDKMG9FnHnei99JHUwqRbxX3HGozuIqQGVvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd242d2b06.mp4?token=VK5qMjOU83AqDKa2f9zAqdteVx7qzm4gm8nIPSC3vTRBfUFdQw8632gIMDpvmpHtwB8_Y1NlNQW47F0Dii47OQ71OK42w37gj6gF_S8iKnEX1L11TlzYPRLMs61amiVdiPxOdr9KreOSbiyCMJIdnLS_yUip0yiK-nDI2kozk33Zd3AjOa75vjPnhLDcsS3G44VaJQFb5dsHuN-JRYzBRE2g5oNQYrA333cUT5gz2v9ft3K7M5uQqLcKhJzfVpGiPZT679Q6dVPGPv1GAjmYo37shWEIZug_SYJBZjM09yXIBf7FPQSDKMG9FnHnei99JHUwqRbxX3HGozuIqQGVvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعض الديون لا تنسى .. الحرب السعودية المفروضة على العراق</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/87456" target="_blank">📅 14:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87455">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">صفارات الإنذار تدوي في العاصمة الأوكرانية كييف وتحذير من هجمات باليستية</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/87455" target="_blank">📅 14:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87454">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇶
الحكومة العراقية:
هناك تنسيق أمني وعسكري منتظم لتسلم المواقع التي تشغلها قوات التحالف الدولي في حلول 30 أيلول المقبل.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/87454" target="_blank">📅 14:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87453">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDT2ecO06cdJPmR0-rcfCjYyfkYbTOowGOIW6Y5zXONNHxLWmh7Ys9L0ROhNzrieIu_aJPwcce7QFjOjDxcH6Ia7OKye9o80AjHs4N9cd7jy0NrqS3c0xCR3lh1TWfUro_0x0MEVFw1Xa5TWqIkoKUJ2B_cWoBLG61_W_iQ9r7Q-aWGBYKWUbXwOhzpV21v9DHQzVlvQRvgGLmVk5RaERp6tX7dJlb4RnjnIhZzwBo-8JTzroiMrXIguYdlEkIXF4erE5bB6pgFGtXbbKpduvqyzhwdbym7wtnI5BJMKqoP-2Chsem7OuzKgHjG7PRSXaY8ywG_SOl2cVK0SSn1oUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
"نريد ماي يا انصار الحسين"
مناشدة عبر بوت نايا:
نداء لاهل الغانمة (الحشد الشعبي) نحن مواطنين يسكنون محافظة ميسان الجمعيات منطقة حجي حسن الثانية المكان المؤشر باللون الاحمر مقطوع عنه الماء صار اليوم سادس ناشدنه المحافظة ناشدنه المستثمر لكن ماكو اي حلول ما بقى الها غير الحشد ولد المهندس الشهيد ونگلكم (نريد ماي)  يا انصار الحسين عليه السلام</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/87453" target="_blank">📅 13:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87452">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇶
🔻
هيئة الحشد الشعبي
:
توضح هيئة الحشد الشعبي أن المقرات الوهمية التي أعلنت عنها وزارة الداخلية، والتي ادّعى القائمون عليها انتسابها إلى هيئة الحشد الشعبي، لا تمت إلى الهيئة بأي صلة.
وتؤكد الهيئة أن إجراءات إغلاق هذه المقرات ومتابعتها نُفذت ضمن عملية نفذتها المديرية العامة للأمن والانضباط في هيئة الحشد الشعبي، في إطار أعمال اللجنة الدائمة لحصر السلاح، المُشكَّلة من قبل القائد العام للقوات المسلحة.
كما تجدد الهيئة تأكيدها استمرارها في متابعة ومعالجة مثل هذه الحالات، واتخاذ الإجراءات القانونية والإدارية اللازمة بحق كل من يحاول انتحال صفة الهيئة أو استغلال اسمها بأي شكل من الأشكال.
هيئة الحشد الشعبي
10 آب 2026</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/87452" target="_blank">📅 13:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87451">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇶
الحكومة العراقية:
لم نكن نعلم بالعدوان ورئيس الوزراء العراقي كلف وزارة الخارجية لرفع مذكرة الى مجلس الأمن حول القصف على مقرات الحشد الشعبي.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/87451" target="_blank">📅 13:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87450">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇶
العراق يقوم بتخفيضات جديدة لنفطه المصدر الى دول قارة اسيا.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/87450" target="_blank">📅 13:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87449">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇶
العراق يقوم بتخفيضات جديدة لنفطه المصدر الى دول قارة اسيا.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/87449" target="_blank">📅 13:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87448">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اعلام سعودي: مسيرات انصار الله تستهدف مواقع المرتزقة في منطقة بيحان بشبوة</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/87448" target="_blank">📅 13:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87447">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اعلام سعودي: مسيرات انصار الله تستهدف مواقع المرتزقة في منطقة بيحان بشبوة</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/87447" target="_blank">📅 12:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87446">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e55da867fa.mp4?token=cTKM1UGfghcudwV_g-LiLpwx5IMqu0wSHV4ZUSwwSt53ZzOTXRWFABIZJeyssuVrsXexT437IPAiriT1u7yf2tj_DorXfURBgxSLUSw8nkVccUdo20RpRaS0Zh6HLmKlVSYK946BX9eYY1NwrftEO2OyeJBlyBApllETqyEm2bv_UbfkNR7mKtfHVqDqL3UW52iOi632UV-HjCZQQsdVRjO0L_ZG1nHwlhGpeML9rxWkjEORrD-Ub6yGBHdCBxXP8BpI-nX8X8zsLjJ1T53k6mJxkDr78syMfomOQpHqU4ByQzEPVLfwN9Xwx9MiXYigP4yxbzea9FY8foJqgSi8xb913A7f6MWuuCKq_TNzoRTchyuAV9au8gzdadVB4wCExTebH-Am5MnQyEZLavO755O1IjEEjzOwiH1A5elbhT2ZFCgctqb7X2rN1x9A2XxDkvf5XhTXXlN2uHY_TKvALL3Ozp_6dh6EZ-IsIcXwOsrI1WUoCVqRThgznGWUjJud8OGqWotkuiMXgB6TpvKXMaGmM7B8V2dhRyuY5uNBO0dLTuP2TSOSTZ6kMhGaxs5Td2GMc_6Q5A-PBg-DxbrEkZlbC4YhJ47SiazAJHmWqYLDe5xpqR9PqIcpppLapo8_OtXr24Wk0hNpZcaMkNCsJHWzJJ-P5FU8ZCyZwIBslEU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e55da867fa.mp4?token=cTKM1UGfghcudwV_g-LiLpwx5IMqu0wSHV4ZUSwwSt53ZzOTXRWFABIZJeyssuVrsXexT437IPAiriT1u7yf2tj_DorXfURBgxSLUSw8nkVccUdo20RpRaS0Zh6HLmKlVSYK946BX9eYY1NwrftEO2OyeJBlyBApllETqyEm2bv_UbfkNR7mKtfHVqDqL3UW52iOi632UV-HjCZQQsdVRjO0L_ZG1nHwlhGpeML9rxWkjEORrD-Ub6yGBHdCBxXP8BpI-nX8X8zsLjJ1T53k6mJxkDr78syMfomOQpHqU4ByQzEPVLfwN9Xwx9MiXYigP4yxbzea9FY8foJqgSi8xb913A7f6MWuuCKq_TNzoRTchyuAV9au8gzdadVB4wCExTebH-Am5MnQyEZLavO755O1IjEEjzOwiH1A5elbhT2ZFCgctqb7X2rN1x9A2XxDkvf5XhTXXlN2uHY_TKvALL3Ozp_6dh6EZ-IsIcXwOsrI1WUoCVqRThgznGWUjJud8OGqWotkuiMXgB6TpvKXMaGmM7B8V2dhRyuY5uNBO0dLTuP2TSOSTZ6kMhGaxs5Td2GMc_6Q5A-PBg-DxbrEkZlbC4YhJ47SiazAJHmWqYLDe5xpqR9PqIcpppLapo8_OtXr24Wk0hNpZcaMkNCsJHWzJJ-P5FU8ZCyZwIBslEU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
المتحدث باسم وزارة الخارجية الايرانية: لم يتم حتى الآن اتخاذ قرار بشأن مشاركة الرئيس في اجتماع الأمم المتحدة في نيويورك.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/87446" target="_blank">📅 12:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87445">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">هجمات سيبرانية تستهدف الامارات</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/87445" target="_blank">📅 12:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87444">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">هجمات سيبرانية تستهدف الامارات</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/87444" target="_blank">📅 12:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87443">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
المتحدث باسم وزارة الخارجية الايرانية:
لم يتم حتى الآن اتخاذ قرار بشأن مشاركة الرئيس في اجتماع الأمم المتحدة في نيويورك.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87443" target="_blank">📅 12:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87442">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇶
الجيش العراقي ينفذ قصف جوي لمواقع تواجد عصابات داعـSh بواسطة طائرات (سزنا كرفان). قد أسفرت الواجبات عن تدمير ( 8)  مضافات بالكامل ضمن قاطع مسؤولية الفرقة 11 في قيادة عمليات كركوك شمال العراق</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87442" target="_blank">📅 12:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87440">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇾🇪
🔻
هجوم بالمسيرات وانفجارات قرب قصر المعاشيق بعدن جنوبي اليمن.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/87440" target="_blank">📅 08:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87439">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇱
🇺🇸
إعلام العدو عن مصادر سياسية: خلافات بين الولايات المتحدة وإسرائيل على خلفية وثيقة الـ15 نقطة بشأن غزة</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/87439" target="_blank">📅 08:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87437">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇾🇪
🇸🇦
مرتزقة السعودية تعلن عن مقتل 7 وإصابة 30 مرتزق، جراء هجوم يمني بالصواريخ والطائرات المسيرة الإنتحارية طال مواقع عسكرية في مدينة المخا اليمنية.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/87437" target="_blank">📅 04:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87436">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇾🇪
🇸🇦
إنفجارات عنيفة تهز معسكرات مرتزقة السعودية في مدينة مأرب اليمنية.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/naya_foriraq/87436" target="_blank">📅 03:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87435">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVzxXobTMZPOSkFauxa1H4V978UJipXIw-C7kEhH85uGHgcwYTgXQE9NAVaHcdRWWqHqbiVghKzqOR4CFFikUL9L59W71NDk1_al2gaHcgvantJgEGU-1vl0yJm_W_81UmE-UT4FyBql15BBCZd3om9QXnXMNiLrENEmA1ZpwMxbgBTWbzTBwwhrQF_aiSeImw1IuXskv39hHOMZVRX9AWgA4l2elYu4v0ybp0BoP4mCvzpyVXyecmHCO4Lbx_zqb9rPNQb_RKGhoc8JX0-opzoxSvltr7CM64Q7xnMl6rUU5LpDFXJ5_O4fsLDIo6iWdIuhuAsZ6wuPGxe2PpoZvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
نتيجة الهجمات التي تشنها القوات اليمنية..
السعودية تستمر في إغلاق مطارات جيزان ونجران وأبها حتى إشعار أخر.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/naya_foriraq/87435" target="_blank">📅 02:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87434">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQOEmV80qhpPWDUwwR-w7P7LRVSJWP6SoIzg9JXJcg1qS2nkZqjgRoTiF2uKOZoe5JStAcFXWCh7lR01ZKb4icSAuT0qD6Z5PFtPofA57kyU1MRfj5-WI-YjlTnaZ-EX1Xxnzn_RQ6xBheM8Yple4xFyL54Xim3kZ-YPb9EI1vJE6goYBgJAKaknDKP5U3swsseSBOAIrVyTXTNZzYITx1S5pBFZWy_VMyf1CG79IU0M43-nFGdOXtKFvZSHcNRXV2mkyO9cfrAD4kvYwZcd2l2L0mzQID4wEPZZM-ken5xTTi2vjtyb1Vscvnnbe71ggSeGT6ro0rv9I8co7XYT7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد اخرى من السفينة المشتعلة قبالة سواحل عمان بعد دكها بالصواريخ من قبل بحرية الحرس الثوري.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/naya_foriraq/87434" target="_blank">📅 01:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87433">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9FCeWpZVWX_a47vWI-Kq0RNg424pXRgbiZWvJ9Hx0ZWd0ZLG7mXx7ZIaFHMDWxnJuE5zmetd6Y3eQde2pLthEBNjS2qkQI5RRxLkLiUEmqCLzI31dYY4r9wtzff34-4GK3S1i4kKS_Cem_m7zZBuIt3a_shxsBlx9KK2Nlpzxb0oBgcb9mvq5GGR0ss6LPTp5IW1vQ639kKktxd8mUq1x8z-DQjJc4iWoJvguACiZ16UcklSpaCDSXX26bGd9CIzdIEwW2tJGvNsfT_cNRtbmAGex3HU6dOp6Twu7hMf-uHVazSOjH-9nHKGc2TnZkQ5npax2C9QDh97IJenwawew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🔻
تعرف على محسن رضائي ؟!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/naya_foriraq/87433" target="_blank">📅 01:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87432">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">الحادثة بالمختصر ، ووقعت قبل أقل من ثلاثة أسابيع في محافظة واسط، حيث تم ضبط سيارتين محمّلتين بطائرات مسيّرة.   وهذا يعني ان الرواية التي أنتجتها قناة العربية السعودية هي رواية كاذبة بالمطلق واستخدمت صور قديمة من واسط وركبتها على بابل لأسباب سياسية كون بابل…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/87432" target="_blank">📅 01:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87431">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مسيرة معادية ثانية تم استهدافها وإسقاطها من قبل الدفاعات الجوية الإيرانية في أجواء جنوب البلاد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/87431" target="_blank">📅 01:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87430">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/87430" target="_blank">📅 01:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87429">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/87429" target="_blank">📅 01:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87428">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0db1cb8610.mp4?token=mR1xbo0KTYA3wdNfmZm3jdMlwDjo-Rfuf_CVFmZ30R497v_2_dJN_elKllh62RWySBJfft0kQgZFnXZ9tdyzJda5CXk_DiDh4u8mTLDXYO2PTWMqpG-E14_D9GUS-oyiex8dqQlnUgL7-E7eFNY9Cbby3iP5v7rsKL0KWheCxwY8SL0Z8OubX_gPfs6Z80lkk88H-zOK7xXJH6FjCALuMf-Gl4ZDGOP1PLJaZNdv9Y__kxG3FnRf3crIib-7QLXSkpqjjWWbVb_2NDv4UMvk4wK4KBgd_OuKgqjaOOREy-Pz73---hfXp02_ID58oOOFKD1UG0mqPrgXp5tBGOWlLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0db1cb8610.mp4?token=mR1xbo0KTYA3wdNfmZm3jdMlwDjo-Rfuf_CVFmZ30R497v_2_dJN_elKllh62RWySBJfft0kQgZFnXZ9tdyzJda5CXk_DiDh4u8mTLDXYO2PTWMqpG-E14_D9GUS-oyiex8dqQlnUgL7-E7eFNY9Cbby3iP5v7rsKL0KWheCxwY8SL0Z8OubX_gPfs6Z80lkk88H-zOK7xXJH6FjCALuMf-Gl4ZDGOP1PLJaZNdv9Y__kxG3FnRf3crIib-7QLXSkpqjjWWbVb_2NDv4UMvk4wK4KBgd_OuKgqjaOOREy-Pz73---hfXp02_ID58oOOFKD1UG0mqPrgXp5tBGOWlLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من استهداف سفينة واشتعال النيران فيها قبالة سواحل عمان بالقرب من مضيق هرمز.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/87428" target="_blank">📅 01:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87427">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzX4e4ooYOhNrkqvEfNe_wuaNy8ZHQdnMiWAVOlpnb8DPOfNbwF3ePYDONCN7D4RoDACcy6grHJ_EUnrUvbeH6mqWRDvllH8Zr4DrlHCVXL9X1E0Cy8HFjOVsXpjulygMqk9N6lw_juR5cJCCfPWcwzXxX3rP08b54LQpTE4fyjPBwSuKc_-6HUNpUnz5ioMrWEWPngCOI9huO1xWqjg86HLjJVJ9ZjbtXYrlmrGDTR95AwoAE9owTadIZUEcMuGPxe8R99IfzllepK4FG_s9806O83kogVWAz0GiaBS2tz-0uix6NQIb-kp8pwjypG9gnaQaHqatFyjezWT53xr-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب يستغني عن فريقه تدريجيا
تعيين ويل شارف مساعداً جديداً للرئيس ومستشاراً للبيت الأبيض، ليحل محل ديفيد وارينغتون الذي سينتقل إلى القطاع الخاص.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/87427" target="_blank">📅 01:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87426">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مصدر امني لنايا
عملية نوعية في منطقة الكرادة خارج بالعاصمة بغداد ؛ العثور على مبلغ مالي كبير يخص وزير العمل والشؤون الاجتماعية السابق .</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/87426" target="_blank">📅 00:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87425">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">أنباء عن أن المسيرة التي تم اسقاطها في أجواء جنوبي إيران تابعة للسعودية.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/87425" target="_blank">📅 00:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87423">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKLP4ugmHA09hLkQ6vrXxJOrkaTCPI2Yft1YgAMdaEUObhDsUiBAtF-THBkbJ3mcPBQRawMZGb-y7qV2iA5WMOHDoR_HWXOZVff4pB60wxLvvp0d8aJZq2Wl4dV30PekYqG_M-Ei7MuCxsfdhBQ5_JuJK5jTLnUk6bp2GxV8dP2PTXSwqDqUIO0kc5fZ6p_jJhdz-KtttSmjk45TDlqkqr71FB2amSl6PvL7H-HYvTiLb1pY9jSsFkhganezKjBchUNBHeRJEuBH-5rtmakUqBez7hWxRkr1vhpLN-gqNgQcREnBMkTgWyjPdL6Ii4eZcmcmgQJYYhgSAEWL2X9OSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94eb35c039.mp4?token=nqKammMKb-VA55AAbHvZKVrX7wAbl0q1SPpNS7ufrmVMy7W-wGcaei9QwcF-CRPpKvGQ8Ieb7o-LNAxhJM25mm5VA4_hFAF0IH2aBT2J6zWaSf17FdodRV4IJw9jm3qE0LhdsSM2Al0oaaUQTX-4AcNCS7kgyjIH66qg5TYGukvANgCtuS2ljs8-QL_LT0181TtSt-VGF24ySd7Ve9tYFJjShCXR965aBQ0FvyOhIKA5sgAVebIjn3LoC33FWVu2pYDX5pYYi5TQo8ctmfr9eYbI_9pSWHWib4Q9ahdkDp1Kzk6hHqbgi8EbAnz2OVMP0jzA9jocs-E19CauCJjJxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94eb35c039.mp4?token=nqKammMKb-VA55AAbHvZKVrX7wAbl0q1SPpNS7ufrmVMy7W-wGcaei9QwcF-CRPpKvGQ8Ieb7o-LNAxhJM25mm5VA4_hFAF0IH2aBT2J6zWaSf17FdodRV4IJw9jm3qE0LhdsSM2Al0oaaUQTX-4AcNCS7kgyjIH66qg5TYGukvANgCtuS2ljs8-QL_LT0181TtSt-VGF24ySd7Ve9tYFJjShCXR965aBQ0FvyOhIKA5sgAVebIjn3LoC33FWVu2pYDX5pYYi5TQo8ctmfr9eYbI_9pSWHWib4Q9ahdkDp1Kzk6hHqbgi8EbAnz2OVMP0jzA9jocs-E19CauCJjJxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف واسقاط مسيرة أمريكية في جنوب إيران</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/87423" target="_blank">📅 00:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87422">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/87422" target="_blank">📅 00:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87421">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dbf391292.mp4?token=cCZLzvw0cUsWGivrqzX51XRAPBQPWwDt3g9i78XXod_KlSuAnDsJpsOyRM2xqKpob-84BvbourA1QuBRKLjM9SfiZ0h1ZcgMgGt_5Jjrf8zi0PhQvfxRNiu2fNJgj5wpkC9vByog4SfKzw-X2Kwmq37HTll5lEEA6UUxWjP7ocqjhzOhbvx3ek03zBnunW8HUywMywxR-w8rbrhpG7ywiOrwtkWt3tQERJve4tO28SfZzXM37GCK0LPkDT0G6z0lsEOw93CTWZnOf4e-9dkP15dTKyXKF-mf9XuzdyJwaBQHbd13Lw57vGN3k4ntQER3rEZgAzK9hQEADf5LUkTjsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dbf391292.mp4?token=cCZLzvw0cUsWGivrqzX51XRAPBQPWwDt3g9i78XXod_KlSuAnDsJpsOyRM2xqKpob-84BvbourA1QuBRKLjM9SfiZ0h1ZcgMgGt_5Jjrf8zi0PhQvfxRNiu2fNJgj5wpkC9vByog4SfKzw-X2Kwmq37HTll5lEEA6UUxWjP7ocqjhzOhbvx3ek03zBnunW8HUywMywxR-w8rbrhpG7ywiOrwtkWt3tQERJve4tO28SfZzXM37GCK0LPkDT0G6z0lsEOw93CTWZnOf4e-9dkP15dTKyXKF-mf9XuzdyJwaBQHbd13Lw57vGN3k4ntQER3rEZgAzK9hQEADf5LUkTjsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضربة تطال سفينة مخالفة قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/87421" target="_blank">📅 00:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87420">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/87420" target="_blank">📅 00:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87419">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">انفجارات بالقرب من مضيق هرمز</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/87419" target="_blank">📅 00:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87418">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">انفجارات بالقرب من مضيق هرمز</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/87418" target="_blank">📅 00:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87417">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مصدر امني لنايا
اعادة انتشار وتموضع قطعات جهاز مكافحة الارهاب والشرطة الاتحادية في مداخل المنطقه الخضراء وسط العاصمة بغداد</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/87417" target="_blank">📅 00:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87416">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/87416" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/87416" target="_blank">📅 23:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87415">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇾🇪
انصار الله يعاودون استهداف ميناء المخا بالصواريخ والمسيّرات.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/87415" target="_blank">📅 23:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87414">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇾🇪
انصار الله يعاودون استهداف ميناء المخا بالصواريخ والمسيّرات.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/87414" target="_blank">📅 23:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87413">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مصدر امني لنايا
العثور على مبلغ يقارب مليار دينار عراقي في منزل مدير الشركة العامة لتجارة السيارات في العاصمة بغداد منطقة الوزيرية .</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/87413" target="_blank">📅 23:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87412">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مشاهد إطلاق عدد من الصواريخ الباليستية والطائرات المسيرة على تحشيدات العدو السعودي ومخازن أسلحته في المخا</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/87412" target="_blank">📅 22:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87405">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H5ERs6tA0y5jUklcFjglIHsAtjMVnjU4pe44sFbJIjeFQ0G-p0yjS_dKziu4uNrs6bn7hul23lYuCaobPkCQ_TpYTA5Gyz4o5rd9oQxpHH14-El23r90qFDgjv_5mtbwNkRRu0DbPfLyN3GpnBOXD6WOtGn3MyNvYkfQLxf5yic1Fqk_RC8QVlechqNpyUpNOSDyu-DA0nsv3eI6zkB618P4l9EG00oEFXNaIcSzgppCFBzcOdygRalUURfoF-29D-dX723YrAd3pJfcjg3WqDvZrvlRSjgUhEaoZgpPLdfEkMDt3vkrQOTreV8YRiLIq9Z4nEePi5NQfn01TqW7KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a_w6SDkp0O2YG3kTL_jdgwa8aXCFrSJYO7QbjMYrg6O1OrrBls8vAO6fiEWXcLslMZLRmn0aGCKftEUNCjH3bXWzxHpj24U4E5rIq9bii9ZyBKmcEng2YA-RWHpWTn9FppAUZmWg-XIN9setb19YPEl7F5L15Prtw_bOe2nkShPPSOKwGjumNDTVDU3sR5l8hRPEGFlgw2BS21mrv-iQLRKDZuFHSFT4dR_DFMiJYNn13KRXsgIzQsIoJraslWX63PaaZzJDHhZXxfQ5MvkAtohmiwNE1J9FyYdsel0bCW98DZy4L3I96yiH6U47fLZ0s3DOi2Cxxl7fGfHMUBnasA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PIunMt-jlz3nkIKGkS8MvVvo3NIqb5CyXYEJd-R2zb_0rbpV9pU2rwvw6vzp73c3sOk4twlZk9qyAE8AmiRwRrFrsiEzo31LW4_4I0ks8DpJVbai-8jL_Lz62HZUM0yaYffgoI4yTEMs98NcNc4InjCGPN6XFleYfG5fzqJxfgtPS0PnxYCNkASZ22lzhq5uJgJ3e_HPPmvmtPHniWVu6RKUAIxBPhzkq_tkbL8Xlcn5sz8EUCuFpenurUtJzqHCER6B71RNdP4OX1xeLNLRIk_aiRw-555dVK9J_ouecSHE2U-2toXDomoPx0gqgT9pBOgGRVG37WRBO5TlyhwAwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f4zXouxahclXqyBR9r0o-VDExzFElHCH9kQFUHF5wz8v61RgDk98jQOmI_6UcGpM2paR1E0-7GsZR0STCBD1QWrS2nrefd15fXS2fwiDB3ts4ewdOr_3UksJmReHHID_z_kO5f_J64yaMoDbZA1MS_Rolwq5lNylrDCv_ReOyVLxYJqBxcvKLIi1iGTo-vZLd7gIiU0koZvYVeJOMw_rPmsgMAkJJKWQEP6K3jz298dqCuagEgyxVHxrlmWMc1DLbzUhYWo_OQiyAq5xbxI44sTl5hd9mR9g1eL4TIqGkNF-tpMZBhlZc6p0mLWRJv6bdVb1zA4fVH_HJ0bQ3Mp0Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CLxkTQs0xPVMu-2rycegDV8pQf6CRucY3UoGDw0VjXDvXVb02yVJJnaVfEel8M5J73-abt9QpM9RADtDo3gufBzgPeSRU8l31xg1qcNqPSNJZa22rhL5B9byUhIFBcNej_5GbLh6iO5vEfcwnhWO-OA6kn6I8MF12mRuh8jAmJu82tS1vSH6OTKRFuVFvkWbz91QfR52oU2ZIRrdKzENTS9ViJYJp-yRu0qKWBshqOn4J3CBr5xEWhosg6YiA_zFaCPeSUb5rPqwRW1yzt0Fvq5plMlZi3CXt0vBty-hZ9d5RwwsdIT66aTXSBxktAlvpowOyf1_NOk8qi792LU4lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g1JV9LfIs7VUDFkFtmmXx_6SeQgoJBKUXnLWWnD_ubh-I6grGvBO9ATz42AT9MeopBJSDSZc0dzC1KB48ZAzxhVbDJV9OzInONEpyc1xSimWFf9-ssFIXbd32RldvYHjfmn5MPldCmhW0hlG2KU7-bXpB8ONLfdNtZTOF2Yavpz3CP_7RCGNdGlFSX7_oLT0j3oW-YbEHN_8ipBgnm8oWST6bc9OQmDqDd6FMJmdqRF7mPno4nOlVgop6ybUDlNyeuihicyiayrEOV5Hh1xGpK2UlNby-RQX1Y9VvCsMTdbrkqBy7XPStUF2JAhf7nnjoJFhXVz4uuPg3H7Om0fndw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C1puQVV-r70zGsl-w33mtNHVtcT08NebfD-lge6mLh6_coI4j85mkTZx3Hx8RftauqCONltT1zg76dLeHxflfb91gCbd0HUMgmnUhAMnmwv0Re2uQ_bregYc_OIwUtMaJSVTCkLQWT6uPd7t3ZyuoOzKgdRYuCfWQbjuYoRO2xyWrRu11HazuRTrE87Mjx1aQs_Y6FQybDvpZ9q98kEAAnLjYkSpQBiQnFu3xDTzk2puL5uTgbJCEQW0GJcZGx8wTBqDW9zuA-kSGwbqH2RHH-9vZ4eA5nbSL_Xi2oQJjf-76EqkMIb_oh-blnjle8MYTv1O0uS0SldTWD-87em3ew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صور | إطلاق عدد من الصواريخ والطائرات المسيرة على تحشيدات العدو السعودي ومخازن أسلحته في المخا</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/87405" target="_blank">📅 22:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87404">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uP-aUemVmpkEePkNHU126XBarxP1WKdU9S-RcLrYt0-LdcLbPRyP6SvgF2lskM6AvNJAPEFvznz-BYYqs7cbOBd0FrAIbCfCAumHbxB1lEle2M6hDCdx6oSdvz0FBiS3KMlsW7g1Io3KrhxEVmKxqfQCNDqgH0JBQbNT7TwFOlUVHic16WFsH9T1wDt56g9SBUmvcuchBQ0WXvvY7zhh3IM_BUR9nWjWqib4PBJsI2it7ouUfHX18D4e7NGHxm8I5d7-w246efIU6wH38eNToxyLM7ExKlXHtUvOU66atf8Yk_AhUpLC-tQy-9Y_ZbDvcsQha24Wq9Fj_6OoKAa_gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
عضو المجلس السياسي لانصار الله:
وجود كميات كبيرة من اسلحة السعودية في المخا تحضيرا لاستخدامها لقصف اليمن.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/87404" target="_blank">📅 22:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87403">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇾🇪
بعد قليل.. مشاهد لإطلاق عدد من الصواريخ والطائرات المسيرة على تحشيدات العدو السعودي ومخازن أسلحته في المخا
.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/87403" target="_blank">📅 22:38 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87402">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d683e056.mp4?token=nFYE9f0AxopxDwua53luXZWNZyrErghN5mkqR1DFFuqOAF6j6HcXU2qfmSgxgUDHzpQUq9r5x7xy3-mVwjhY3Rd9eZ1Iay6fct1sQaNUlwmSGVNS9g4jKQaGDl1TC9phxWuV_DgPOo_CItUR4XkIJlCZyGM4YvGnHg294_lRzUj_M6d8H4SOAF2JJryKSwaYAH37AZIHFS1ySmpYbVSnoT601n5QzPwdU25bxsqW22xHwbWlIxoOOWGlgntSf3og1EJeoEIZWfuYkOATUi9aLMNaiHzEwSg3vr3-kzpFCOx62ngkewZhNOWAo9Ex9xaBlv5TTIg6arU3CHbuUbY5eYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d683e056.mp4?token=nFYE9f0AxopxDwua53luXZWNZyrErghN5mkqR1DFFuqOAF6j6HcXU2qfmSgxgUDHzpQUq9r5x7xy3-mVwjhY3Rd9eZ1Iay6fct1sQaNUlwmSGVNS9g4jKQaGDl1TC9phxWuV_DgPOo_CItUR4XkIJlCZyGM4YvGnHg294_lRzUj_M6d8H4SOAF2JJryKSwaYAH37AZIHFS1ySmpYbVSnoT601n5QzPwdU25bxsqW22xHwbWlIxoOOWGlgntSf3og1EJeoEIZWfuYkOATUi9aLMNaiHzEwSg3vr3-kzpFCOx62ngkewZhNOWAo9Ex9xaBlv5TTIg6arU3CHbuUbY5eYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدث امني بالقرب من نادي بيدمينستر للجولف التابع للرئيس ترامب في ولاية نيو جيرسي.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87402" target="_blank">📅 22:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87401">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jud29CwTfugboOkwU5jJ-xSLj8I69nQLXZfcrUTlN1qv1UV_bwQOF8klBcBHDi8pQ24wXIY2Yd9CRxRyfQKDRtjdVkmetXQm_z0DZyZUE4kZ3Fkyjpqa0FmcH-taHTcaNnidz8u_LwSgjPC3frqiIfyarDCwfxcm5TUFVRJ47N9xUmYCvP71YMcGH-47Fo7xw9ReAvCBlNvqBrC5z09-tO9MoVaxYGRmE5riVN8Zj2S52JyMtXoTwPwQb6qb4oS79Jq3HXoT_c8KAsCwkbfsynjPCS5fly8JYx0hZrnZM8kuUagnhicWUwwQIbp-Fq-qxgRseHuS6IFCBAfEVvrcFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/87401" target="_blank">📅 21:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87400">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">حدث امني بالقرب من نادي بيدمينستر للجولف التابع للرئيس ترامب في ولاية نيو جيرسي.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/87400" target="_blank">📅 21:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87399">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حدث امني بالقرب من نادي بيدمينستر للجولف التابع للرئيس ترامب في ولاية نيو جيرسي.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/87399" target="_blank">📅 21:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87398">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/87398" target="_blank">📅 21:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87397">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/87397" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اخ الشهداء
#شاركها</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/87397" target="_blank">📅 21:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87396">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUp16iH4plDj9MeiOYzGMWzDpr0-6vnoZw_X36PKm0W9Q7RQxPq23lNpps7lrkn29srKCRzs125e3JE2fv-8sx3H6z3b2EP-Kaddo1BJ79eSiYdJkxXfvHZhkxjVzKT11Uq_5RXvc5vTlQClhJEAWGvbSDBCDfoOrhETvYE0cY1iWsitE9MiKpZey9Zxze4b6PSVW57UT6S6f4I2FL8DKHF7WlzARDWFIXn4VXO1XJg2T8AtAcpAUVd6ku6hMmO9ABKAmpZIaEmTwPmT-XlzGPVlysgShNop5Kf6XmyYlb990rzyNCZEgQCMAOZZrAIFtafAQiyHqxXEZIUXsydRxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#
توم_باراك_السارق</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/87396" target="_blank">📅 21:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87395">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">▫️
شقشقة هامة لذلك نسترعي الانتباه</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/87395" target="_blank">📅 21:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87394">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a679b54bf.mp4?token=TdG-W9-DIfmY-wLBzlw0ISZXB_6mSTAGz-cwsuhhM26M0GhW01upaHv_liutsTYG6uDQ_yhiIHNzhw3bhcqvpeGta2j7dLkudgC1SeXvwUX4HV9iKoEfJWmCGd-W7VOScISvksyZdTolujKgepg5-ppIp6MdwJICRpmrgEJB2ELOcBKsN3qaTcAimY94yZDJ5ydzUQYNgfvD3QjwDSdQ2lvnaGnpdGO7dY0vRK1eh7d7K7uCFRtseoxgXiFgWMlb9aVQ9_6lymvIHbH9GQbToOPEB85FDHb4DuNL3avnxYo_DpVZAJX9PzLjYilMX3LLZNCo9RWJbgOgaCrEKo6Xag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a679b54bf.mp4?token=TdG-W9-DIfmY-wLBzlw0ISZXB_6mSTAGz-cwsuhhM26M0GhW01upaHv_liutsTYG6uDQ_yhiIHNzhw3bhcqvpeGta2j7dLkudgC1SeXvwUX4HV9iKoEfJWmCGd-W7VOScISvksyZdTolujKgepg5-ppIp6MdwJICRpmrgEJB2ELOcBKsN3qaTcAimY94yZDJ5ydzUQYNgfvD3QjwDSdQ2lvnaGnpdGO7dY0vRK1eh7d7K7uCFRtseoxgXiFgWMlb9aVQ9_6lymvIHbH9GQbToOPEB85FDHb4DuNL3avnxYo_DpVZAJX9PzLjYilMX3LLZNCo9RWJbgOgaCrEKo6Xag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
قليلة التداول
الشهيد الحاج قاسم سليماني رضوان الله تعالى عليه يشكر الشيخ اكرم الكعبي ويصفه بالاخ المجاهد… السلام على نجباء أهل العراق</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/87394" target="_blank">📅 21:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87393">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‏
الناتو
: مستعدون للردع والدفاع في مواجهة أي تحرك روسي عند الضرورة.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/87393" target="_blank">📅 20:37 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87392">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rb1i7vVnAS_jmd8_vWyGdgZjn4-jscnbu2w0J2GhCGJVPVLB073W270GvIaNTSxvHa0Sv-3YdO54zTpGRbXDBI6K719fJG8Tev0r8yQZ1BWNnF0DL93X-omW6A2A25KD-pZRtKsf81cYABy1fk2vYhifcfAi5G9unv0Xwj5yKdmjcN1tjwis6sZFEdT8YyvMpU63FEGf-zVJ_p64xfmG_yPxfRgZltXKn6v4ort5PxEHB7_j8sCTdnO9YJwinN3CMag_nv70y4jMSWTTGjPkVPVyAvogoYR487chmBT8knUR_3GH3s6T8VjqFtnsd4C0PAyE6D2eD0gr4wW60iDywA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
تعيين الدكتور محسن رضائي ممثلاً لقائد الثورة الإسلامية في المجلس الأعلى للأمن القومي.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/87392" target="_blank">📅 20:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87391">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇾🇪
انصار الله في اليمن يطلقون موجة جديدة من صواريخ نحو المخا</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/87391" target="_blank">📅 19:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87390">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اعلام سعودي: انصار الله استهدفوا المرتزقة في المخا بـ30 صاروخا باليستيا</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/87390" target="_blank">📅 18:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87389">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4033ae6c.mp4?token=SeCR6QJ0-QYFDE8qbSwAHSd5GpNTvDLHo3GNKLwxkSOl6d_8pG5E7DgEXSaRVt0Y7ZkPg_x1lJp9-Ewnfufp2FHF9cul02j_eXZPi1wJRuiCGQ9qx4DpeRKVcNiOx9cFyjluCeU2Z53OSIpz4FhoRf2P-t7Bav3sCtti7uf1MNye8IMoUXP0rhcOFTY4z0seDBkyHRpEvQmfdZWBk_vF7rqrD69NPsjShNlu9AWyYozd6QUvO2IhfBWlaECjKeGxV7D55VtiKpxD0AIyVdf1pRPbT3NT8X_Onvb3oj_tERVtb5drsrAharFc-H7gPQsK2MUlyad6MqNV86_7z_Jt0qSCz5rW1QkUS1NPIGEpE23WHL5Y5TFgSBLM7j3W18SlzoEXY-TEZD--YJRUcDswZ19-QoyQgK8ErEhAmi0k2893X8lJylKbO8RZ-zAsMPgrkJVic9BJikiYMeqG-9LlzWlM6rxXZqqwJK413APm40wDYIv57KtqbxulnN7EvYYVSMN_t4rXbd_J3NKxZrnwuq7qkRFnByUatJzXHy1-2w0KqojLSKD-SO03EFcwws7Vqg8j2c6lZII-SVxo9_lIsFR0SeuB5HMibtVAVbMCAaM0skMhC3m7clt0GVtJi0dMRJp8WCC6klbUnOhZfXA7EFT5KfDzevtl6q2fNZ4OxP4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4033ae6c.mp4?token=SeCR6QJ0-QYFDE8qbSwAHSd5GpNTvDLHo3GNKLwxkSOl6d_8pG5E7DgEXSaRVt0Y7ZkPg_x1lJp9-Ewnfufp2FHF9cul02j_eXZPi1wJRuiCGQ9qx4DpeRKVcNiOx9cFyjluCeU2Z53OSIpz4FhoRf2P-t7Bav3sCtti7uf1MNye8IMoUXP0rhcOFTY4z0seDBkyHRpEvQmfdZWBk_vF7rqrD69NPsjShNlu9AWyYozd6QUvO2IhfBWlaECjKeGxV7D55VtiKpxD0AIyVdf1pRPbT3NT8X_Onvb3oj_tERVtb5drsrAharFc-H7gPQsK2MUlyad6MqNV86_7z_Jt0qSCz5rW1QkUS1NPIGEpE23WHL5Y5TFgSBLM7j3W18SlzoEXY-TEZD--YJRUcDswZ19-QoyQgK8ErEhAmi0k2893X8lJylKbO8RZ-zAsMPgrkJVic9BJikiYMeqG-9LlzWlM6rxXZqqwJK413APm40wDYIv57KtqbxulnN7EvYYVSMN_t4rXbd_J3NKxZrnwuq7qkRFnByUatJzXHy1-2w0KqojLSKD-SO03EFcwws7Vqg8j2c6lZII-SVxo9_lIsFR0SeuB5HMibtVAVbMCAaM0skMhC3m7clt0GVtJi0dMRJp8WCC6klbUnOhZfXA7EFT5KfDzevtl6q2fNZ4OxP4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
طيران حربي مجهول الهوية في سماء محافظة ذي قار جنوبي العراق.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/87389" target="_blank">📅 18:19 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87388">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/796dadaeaf.mp4?token=EMHv7YDy4lgSjRxpb9ClZLB51Fw49sXxZuf67eOZBw0qU_fcpn7RtiEPGsesm9HN1MOz6uwfF90KDgWs2RbaMV9PAQ3wWJ7Lk2eyURvpMfmPIFhXx0hyg5em8LehZo2i4QaG2MxMc_chDee1SbpBSZji3TgaubkxAbDhJLbUd2OKNgxgbTKD0Zcy_bxS2P0W9UV4BL-IMjzJjE8KZcQ12hXz-E9HCb3ogyYkLzEI2h_JIlDnWVPdMx8-QRq2N1b1GJHQFEeHT2iz4A55F4YeMNDcWnzfI8nfQKlt5NQkt8GERE2x_n8B-qFTEAjEz9e2p4zslmBJC1pCMbw8CWF-Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/796dadaeaf.mp4?token=EMHv7YDy4lgSjRxpb9ClZLB51Fw49sXxZuf67eOZBw0qU_fcpn7RtiEPGsesm9HN1MOz6uwfF90KDgWs2RbaMV9PAQ3wWJ7Lk2eyURvpMfmPIFhXx0hyg5em8LehZo2i4QaG2MxMc_chDee1SbpBSZji3TgaubkxAbDhJLbUd2OKNgxgbTKD0Zcy_bxS2P0W9UV4BL-IMjzJjE8KZcQ12hXz-E9HCb3ogyYkLzEI2h_JIlDnWVPdMx8-QRq2N1b1GJHQFEeHT2iz4A55F4YeMNDcWnzfI8nfQKlt5NQkt8GERE2x_n8B-qFTEAjEz9e2p4zslmBJC1pCMbw8CWF-Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
عضو مجلس النواب العراقي غالب محمد:
تستمر عمليات تهريب المشتقات النفطية من مصفى «لاناز» في أربيل إلى تركيا، عبر شاحنات تركية، رغم أن هذه الكميات مخصصة لتلبية احتياجات المواطنين في إقليم كردستان، وليس لتهريبها إلى خارج العراق.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/87388" target="_blank">📅 18:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87387">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اعلام سعودي: انصار الله استهدفوا المرتزقة في المخا بـ30 صاروخا باليستيا</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/87387" target="_blank">📅 17:46 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87386">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">انباء عن سقوط طائرة MQ-9 أمريكية في جيبوتي ولم يتم تحديد سبب سقوط طائرة الى الان</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/87386" target="_blank">📅 17:38 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87385">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86225a79fb.mp4?token=hyq6EElAiB6FhylB-No3BxanYbi0hzSBIQDVlPpHPwQutdZUF_Nm_aFh5AiQoVfpczjYI4TypjmDxSUAvebGMk1td1iuHwL3ZcxnB6T5Xd-wxmsDbw4maDIUAYQ9A4T05aCI0KFuKT4yvg_yArOZdJlfYvyAVZGS5GpBMusuHds9F9u5UTo6ovCjvMQ_2JCnUrTvqKSzok1LL94jQRbPkeGy15uosLAsKLYZlIegpc-NK-ZsA1avyVBhb_0SvuOGZdZhcBiA8hAI_5jHLrRKoh3kb_8XhUUdfv5qu4UDvhy0_1e4AryaMjtF-FKhCCsbKkRs7JN-BdJ8m7s7VNivNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86225a79fb.mp4?token=hyq6EElAiB6FhylB-No3BxanYbi0hzSBIQDVlPpHPwQutdZUF_Nm_aFh5AiQoVfpczjYI4TypjmDxSUAvebGMk1td1iuHwL3ZcxnB6T5Xd-wxmsDbw4maDIUAYQ9A4T05aCI0KFuKT4yvg_yArOZdJlfYvyAVZGS5GpBMusuHds9F9u5UTo6ovCjvMQ_2JCnUrTvqKSzok1LL94jQRbPkeGy15uosLAsKLYZlIegpc-NK-ZsA1avyVBhb_0SvuOGZdZhcBiA8hAI_5jHLrRKoh3kb_8XhUUdfv5qu4UDvhy0_1e4AryaMjtF-FKhCCsbKkRs7JN-BdJ8m7s7VNivNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلان حالة طوارئ امريكية في جيبوتي</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/87385" target="_blank">📅 17:37 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87384">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇾🇪
🇾🇪
مصدر يمني رفيع في صنعاء:
ضربات القوات المسلحة اليمنية على المخا ومأرب فتكت بالضباط السعوديين وتحشيداتهم، الجيش اليمني سيحول كل تجمع للضباط السعوديين إلى هدف وضربة اليوم وصلت رسالتها بقوة.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/87384" target="_blank">📅 17:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87383">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اعلام العدو الامريكي يقول ان ترامب يتجه ‏الى تمديد وقف إطلاق النار بشرط كبح البرنامج النووي واستئناف الملاحة في مضيق هرمز</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/87383" target="_blank">📅 16:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87382">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اعلام العدو الامريكي يقول ان ترامب يتجه ‏الى تمديد وقف إطلاق النار بشرط كبح البرنامج النووي واستئناف الملاحة في مضيق هرمز</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/87382" target="_blank">📅 16:37 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87381">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">طائرة امريكية كانت متجهة الى قاعدة إيلسون الجوية في الولايات المتحدة تعلن حالة الطوارئ لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/87381" target="_blank">📅 16:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87380">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuwowpM_CmlTW7X2DOdwWBztQv2OqNW0mouLqcYNJGGk8iQyoErlfmgyLURAHQka9o_Vx4kTNLbMxK0X1pz1078-HB8A7MAYlxVgrbRWh5wGJyERz9GipagnTwVYibFSFk3JxRcLsCbcQR6L0kHwtCOc_dtn_icoXCOwRltBD76V9GNExnRXN7FlwegryesIE00d8MXx7jA2SWXIfaEQEy3Ilk3RsfuehKqzEtBF_YmzGtgZdqUCxHYR1eDdnzfkq5RU7v2fQOXVE7Rp2pf40wNpP4QSldImmEL_LdNy0C_H0wiUlGybJa-22q2SKIrojKR0xqhSrp-PONK18LljcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد وصفها شهداء الحشد بـ"القتلى" وقتلى مرتزقة السعودية في اليمن بـ"الشهداء"
النائب احمد شهيد:
تقدمنا بكتاب رسمي إلى هيئة الإعلام والاتصالات بإيقاف قناة خنجر العْدر قناة الفلوجة الطائفية</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/87380" target="_blank">📅 16:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87379">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">القوات المسلحة اليمنية تطلق صاروخًا باليستيًا على منزل حاكم الحديدة المدعوم من السعودية وانباء اولية عن نجاته</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/87379" target="_blank">📅 15:47 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87378">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">عصابات الجولاني تقول انها توصلت الى مذكرة تفاهم مع روسيا بشأن القواعد في طرطوس وحميميم</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/87378" target="_blank">📅 15:46 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87377">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">عصابات الجولاني تقول انها توصلت الى مذكرة تفاهم مع روسيا بشأن القواعد في طرطوس وحميميم</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/87377" target="_blank">📅 15:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87376">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ecba7daa.mp4?token=mw4N1TGhjkcZVVn01YcFfZpLLWz16Wh9-J2I7w4MKYv-Sp7fYPmsPYffQg82cmZxgxypD-LTxAmIssotx1xoy5pgYfj0r3DATK25oMbhIQmcj_zBsV0qyWPEMLzHJap78LmDNArbHIEuIIMK536Rs1qJglSa_o14WHIDp-M71ujWha1EF5HoXU-h9wlUnaeTm4L13z4ARw0EG-Vu-j5GNvsVeJIQSfwLivllggeeVGZKe_zHCxKvWEPLwVzyExoaLg9lsowpebiGAe407zmUVj3dsbpmNi7wxpQ2QykOiWeXljvsC0LLXkJ7Iy2n8mwPad2CxgGMao20Vzuw92L7zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ecba7daa.mp4?token=mw4N1TGhjkcZVVn01YcFfZpLLWz16Wh9-J2I7w4MKYv-Sp7fYPmsPYffQg82cmZxgxypD-LTxAmIssotx1xoy5pgYfj0r3DATK25oMbhIQmcj_zBsV0qyWPEMLzHJap78LmDNArbHIEuIIMK536Rs1qJglSa_o14WHIDp-M71ujWha1EF5HoXU-h9wlUnaeTm4L13z4ARw0EG-Vu-j5GNvsVeJIQSfwLivllggeeVGZKe_zHCxKvWEPLwVzyExoaLg9lsowpebiGAe407zmUVj3dsbpmNi7wxpQ2QykOiWeXljvsC0LLXkJ7Iy2n8mwPad2CxgGMao20Vzuw92L7zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصرع 7 اشخاص و35 جريح من المرتزقة في ضربات أنصار الله على المخا كحصيلة اولية</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/87376" target="_blank">📅 15:19 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87375">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">رصد إطلاق صاروخين باليستيين من قبل بواسل انصار الله باتجاه المخا والانفجارات تهز الميناء</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/87375" target="_blank">📅 15:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87374">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5PHpdCih8KHdpJubxzHCpU5QIzJpGvM1fa3DnXwVR_RMnp-ZrDzaPyPjZE0aZPnv6LSkQBao771tcwJQ-tR_KGg-3BIevExIaizZZut1ke3f6biGHgeVhrQ_tnmglsRit__nwUL1ygnCVNRC4wmSICcY8FbQQyAxepqsXciTOhVdt0BvTG_u91kbpwhXHeii3l8f7TC-ypuhl8rW7TQ7bmqeVUvf2ptA9ZhmFI8pJK9osrK2gr2OdnKwuwWfeLRZFVdKaqEKA0xS_J2Ei_1iFQsuGKBwNOEoIagRPpBZac-rBq8Yhnw7EfPqi3Bo91zTa6YDedDWlLEDkMJ_LEK1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رصد إطلاق صاروخين باليستيين من قبل بواسل انصار الله باتجاه المخا والانفجارات تهز الميناء</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/87374" target="_blank">📅 14:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87373">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3801856749.mp4?token=vnD5Lnotc7mvyyopCt-W9eFB1D0PHLNYpgPiHcBurgmDEK_K5PI1EtjUiLkgZ2mMa-Jtf4-7sFvIOXGndLOpE2QHb_0gvGNpPoF89bs7-07UThJMFABDPlEz6gI-4PcVLreIfm4NdUBUR-lopoEcWId2gfv3P9dfKS9e6hclyZvckpkdh5hrTcfHod8s6kJxEwt9YK91bISVHoq-NzTVZSPcFQdXcMfTClzA9goBXIswuTJ4D29i13ZtGQtKPDrq3ULOhnsy-krbKQwBv7B7T7LNgMcq-ya7k-mjnEKQrT4u1_jhwZRTGYYYOWBxC7IiUNeg3SNdTXuvOQfPjw_AsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3801856749.mp4?token=vnD5Lnotc7mvyyopCt-W9eFB1D0PHLNYpgPiHcBurgmDEK_K5PI1EtjUiLkgZ2mMa-Jtf4-7sFvIOXGndLOpE2QHb_0gvGNpPoF89bs7-07UThJMFABDPlEz6gI-4PcVLreIfm4NdUBUR-lopoEcWId2gfv3P9dfKS9e6hclyZvckpkdh5hrTcfHod8s6kJxEwt9YK91bISVHoq-NzTVZSPcFQdXcMfTClzA9goBXIswuTJ4D29i13ZtGQtKPDrq3ULOhnsy-krbKQwBv7B7T7LNgMcq-ya7k-mjnEKQrT4u1_jhwZRTGYYYOWBxC7IiUNeg3SNdTXuvOQfPjw_AsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتن ياهو: أود أن أكون دقيقًا. إسرائيل ترفض الوثيقة المكونة من 15 نقطة. سمعت بعض الناس يقولون: "لم تقله." لقد قلناه، ولكنني هنا أكرر: إسرائيل ترفض الوثيقة المكونة من 15 نقطة!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87373" target="_blank">📅 14:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87372">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa310c312d.mp4?token=UbPEaAzXTH-X_xgFZCYtB95UswHrLXJOz8pDBgBENU2Dhk_rRTChwIixmDOj1N5SCE0DcuRCC62k5PKoQUBHvA85X20JBYV7heZjz_8PmUBr7ILM72Ve_Y4k5q1JDRwo3A-RSmFhSjJKcJJkYVFQzSSvmyUxo7Ik2hmBSvaY--Ho4ihu9E2X3kLnIzfxIIO92fGrb5GBTdVG-osz1bnrcbL1xX-ExJdeBQecv5BG16372ZuXY76auihmJN-gB5-ur8bIRPrEtSqjLwI2rjTFll2yyyBSufTrEQK_K_9japB7EZNc7rhPzTgBUwn9ILLEykDEYwOCrJ1iC1n_FdcSY3NrC6m5kZ-NDNvqgIoXEqZNSfVYJkVvtQ1vfpFWYS523RHvxCjbO1GY9E2ZwICyNLZRmAlpbgpOhDcww7Fab5chZ9K1ZSS8pxmqbezfTAXsHQOLnFmi_e5UOOZZl2pVpSfrhK48JFniMXh1xt9R1C4pCPXpPIoanBQ-r7CbDJgtHn3wFixXwIlzoPpMY2klh9EReo4E5TAyUWhXSKU0gUbYiJQ8TPKvZ3S7mC9h5_qeKz-jvV2sbyKCku5rEuiXzXNl9pRuSOIvpJJJcQfhJxXFyYKbGfshcj-aB9_YqTmjaPHeuks_zXMTiLmyCno80U2y5N_BdUE5UXtpThVYFEk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa310c312d.mp4?token=UbPEaAzXTH-X_xgFZCYtB95UswHrLXJOz8pDBgBENU2Dhk_rRTChwIixmDOj1N5SCE0DcuRCC62k5PKoQUBHvA85X20JBYV7heZjz_8PmUBr7ILM72Ve_Y4k5q1JDRwo3A-RSmFhSjJKcJJkYVFQzSSvmyUxo7Ik2hmBSvaY--Ho4ihu9E2X3kLnIzfxIIO92fGrb5GBTdVG-osz1bnrcbL1xX-ExJdeBQecv5BG16372ZuXY76auihmJN-gB5-ur8bIRPrEtSqjLwI2rjTFll2yyyBSufTrEQK_K_9japB7EZNc7rhPzTgBUwn9ILLEykDEYwOCrJ1iC1n_FdcSY3NrC6m5kZ-NDNvqgIoXEqZNSfVYJkVvtQ1vfpFWYS523RHvxCjbO1GY9E2ZwICyNLZRmAlpbgpOhDcww7Fab5chZ9K1ZSS8pxmqbezfTAXsHQOLnFmi_e5UOOZZl2pVpSfrhK48JFniMXh1xt9R1C4pCPXpPIoanBQ-r7CbDJgtHn3wFixXwIlzoPpMY2klh9EReo4E5TAyUWhXSKU0gUbYiJQ8TPKvZ3S7mC9h5_qeKz-jvV2sbyKCku5rEuiXzXNl9pRuSOIvpJJJcQfhJxXFyYKbGfshcj-aB9_YqTmjaPHeuks_zXMTiLmyCno80U2y5N_BdUE5UXtpThVYFEk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتن ياهو: أود أن أكون دقيقًا. إسرائيل ترفض الوثيقة المكونة من 15 نقطة. سمعت بعض الناس يقولون: "لم تقله." لقد قلناه، ولكنني هنا أكرر: إسرائيل ترفض الوثيقة المكونة من 15 نقطة!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87372" target="_blank">📅 14:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87371">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBRWcTJUsiXZ6wVpTkaKsG5xUoEqebhKNjNh9O8iZLxiZdPXvCcKJnftf_lnprO7WnoIKejgT-ax4I4WZ-2ZDUE2s0Oge0AsL0QEfctQVxxiEq7uhTRT7uUUKUHP9kwB9waQWPWe9eQKW6Gz7Iwb1D4hp6ObRzUSmx8kykSjBQrZWlFYxnkX5JhyL2bJ_Br08UzZlNI-eFJuHkLFS39_LevmkU3-HDad26Zex9REKSOtBypsvHslDg2xbwx8il05or-6KgC38iykZiV1QRn-PQyJl-iR5qAMCht7lRmjMCoAELRMIo1h_eWqyCkDNmHRwy7WWU04-HJo3RK79RYLMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">القضاء العراقي يطلب من البرلمان رفع الحصانة عن النائب ناظم الأسدي</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/87371" target="_blank">📅 14:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87370">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اعلام سعودي: القصف مستمر على ميناء المخا</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/87370" target="_blank">📅 14:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87369">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اعلام سعودي: القصف مستمر على ميناء المخا</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87369" target="_blank">📅 14:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87368">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">الرئيس الايراني مسعود بزشكيان يلتقي قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/87368" target="_blank">📅 14:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87367">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">الرئيس الايراني مسعود بزشكيان يلتقي قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87367" target="_blank">📅 14:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87366">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇷
وكالة تسنيم:
تكليف محسن رضائي ممثلاً للقيادة العليا للثورة في المجلس الأعلى للأمن القومي الايراني.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87366" target="_blank">📅 13:54 · 18 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
