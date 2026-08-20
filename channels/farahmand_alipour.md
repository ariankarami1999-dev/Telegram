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
<img src="https://cdn4.telesco.pe/file/FRnvbX7Y7jFBh5Q_manEaQFbNcJ2jqVqzNMxsqej9A5EH0zuDFUmfS2-7U26Ptq4A1LLFa3rfUA2Z6h8CINd45ZUoNcM3pQql30D9lBc1Qpxot5MlMMMwu_-t7r4Mawvm28wW0nytAinWM20-zr5Xn1hPxkuJsgTJiZd-OUsb4ZQAclGaqzA9MeIJoLR-nhbMPEoKfc0-PR7zfuqK8KnILeIoBIe5cTZY12-Jd3L0zydbb_pGNG0vL6Cr9dxXKuJROeAY4TuPG_Jz8DNWDxsVuLoRXbkpMKPkxPlQcH4FJKDm7hhbgfaGuCvjdnk5sUzbPeWCVpdpfIqwyYZmaSvJw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-29 09:23:42</div>
<hr>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OajWS756TJuSZ-_PIksd8ZET_qlHzEulf6ID5EiQvD76Fmc3QL3G_3dQY3l9nmB_YRt9uvF1piNwLUZGzsb35Wv1HEykKW_IakUp9FpUINsNtKbIIU10ukui_cT5h2a3VQRZVazS0L6DlZIv28_s7Ec_d3n2ChxUnwLyc0CfrcSwL5euD0wD5mXc6lWlXjXFqrMxWLKFO47PDe1OE6uthF0O7zd_QxuZagkeGs4bnoGVvkSoS71CXYPyPCJSpbL5PHzCqzJ0_SVo5ew33jDoyXRSDNACyaWIp6ByiD7C69PH1VQyeGMEAnHoJ6uplPXXQ7p4QLgQe2T3lI4Tv8YopQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scE-Gghzi4RMx1wizW5AonscmMNSCZGGtvf1RRqZoZU-Huf9G__JJ9GCcyuoS-xCWO1kRLELnVNpfer4GEeT6ALXbxjm1TRzw3vU1ffgO8b5GTMSt5EafzjAFBYAXM4VyKZ-QcuTf0Wi9VpE6LKm3Qp1v27H28Q8orRYIgjJ-3k3mCVQBwLmPuz0YqMxSKNq8Zr8jZo1wSJqBVxnqP1U8_bFc-tUT-kJpPmSdSzlvMqJkYJetNujIKnYd5drTmFdEFP5BdZi35KVl_MnRglKF_BcKkWW__hy_1ZhTvshd__A54xYLjH6sf8BIQL-Nbace0x0OJ1K_wTAYcsWXyKvNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCrKNgi8gBYR_ibWiJtJdWkV6aw4TY1T2SYyGFHNGDItArFijRtpyHcLyGCPuNBwzQFEYrmaxRvy74R7jkDjcpCu3s4Kspg7OjmV016VUEdwd8pBUG6rUWtL6dDFjPqmjGFm9dgkc-pnNYJAl8zT-GTZli29Le_PVBC-CXWaQ6KJamgObcC9CS1d7P3MNo_oBNsb7UVneW7PSkPhz2QXqOuKhifJzswlmcKN1COnrlQXpD2uWXoom9LCIIoJyf9yNZgOQ85djp51pd3PYJC8UKkxcrQhcI-Kane5IpFfMTCPxngzTU6AB22-q23h3PnRypurXg9OdRJcTRVdXcRzAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngVhZTfSJ5ybstWt-vG9gDZilEnsIGDX_CP3Y8a89X1S2IbC15A0zcgp9CjLx8bMlwqbV_3-SoKvNtFmNFMRTLFk35Z14JJuge55TuytYXb9fHm98OyJ0Gi7CHnoJGjrP36Q8ycP31Y92C_L1KmYY0gBzA4h1rYZNYNpsqScYY-yDg3SxfDM8xKnySYIMUx6rcLVYu-PveDTCEqY36PYgD8medlBmOVnqoCnboT8_V3nEbf_jB4nwMfP_b9z4OXCTyYQgmGzkifS86G1C1VmAKQOLTzcDVzZAQa655pfQw8ErcmGxc4TplVlRab4lCz0TUVjPn5f-jA3CYoaYCPPMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANUV6auyFrgH7gJ15yGSPnrqaoUWHx1Z2adYGwezWZNMjITGsBy_3leq-6iBgTVOziuR9kqz-EAjFRY8_28ejMw9agYMh_gWjcKpV-83zY_uXY0uRNA97MozeOh3sEg2yPeOEF03gG64lyXb-WhCgv0Ct7XG-ETp_byIqJ4R0nug-etnmhh1ovcpZxaKkSxTSPGImkBVU_2-J3rL96_cIO3jpeSmXxk_AMQGSBAZoKAX1v2JT3KnOlAnahRlFXzdlTIm_d9bocMS7Qe20dBrJNF388bQMZeBy96Nyk6YjmWmZRo_ha-8LteMsgIyEUIFPgq3CY28jj2Net2Vy7kwmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiNLVaE7y_DuWXHN1Wpt-9wctuZqCqdbsMeYgcBwSbkXCiV3F4o5WMOnc9y5Pm84_b6COoJBLHZMLeIxOTtmRZFbP7H5AL2tgwUCKA3eeM-j6PHrC-F5O22X1DrURC4tUxD2ufRhofARc9jEyclhdljKL0txQDL2KRWDXbZf9eE4oxYFg9uqKTGoxM8POZNFnUlrTu5mO1wZ_5gJ59kbYXfryh7ZCeKg3SuHzgeoECb394NFjCMzm25ZpfQWJ8Ra6rCnIt4ppCVMkSEBCkxyXkD7pfkX1BtNvpzLRSo6MZKw0PSSV7r62VXQIgsPHtRBr4U4qVVzAp0dkV2gRzFHYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvVArctzB1K6xkHzTtTAmgwRGG_XptcZ2Fe69Xz3hYZzdchQ6Sd8-2Sf-ubvayrW5siG7KErjEn7ioJ_3kltPjq9bug-Z5HzZmWC6QQQresxUyb8PK5dXzWRC3P_c5Lue3EpSHZzSF784RGcAlpIDp9hpPPFzhGCe_e6VHI3cu9kW8lLY7fRlIuu9zUsbxXJ6ZazIu80KE_NWgmhETeB0kzrpQvYRo9KD-V6gm2RFiYx0aB5eSALlOBxl-MOwGL8uwCfJEBW90dQC0chc5f04qm5vfPFEOKlU63dVmvYmlrxcy5XhbK-JQsX4QUL9KFdCM1ovydxkVrDSBIyF8kZEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBomc3Zyz9WbXOB_QLzkYHdago8z_vLdNuhVuBCX2lDT3fOubEpHC-O_d9ho86PxhCF-Bq-LhwGvXko31BVzXYSE4yMgKSl2AX-Q22X-nGyou03wM0T_zYEcijj-grYCadsbZu1QSIUpkh025RDvi8nLg4GffsL5_E4QN9pAH0k9Y4aXQY-ytImktw3wwmElvlkFGM4m0jO1a0YjlC_4vyfen_i4YK_iqSKcO7NUdttzaflyZlwFNRmhheNE5WLOet3F_JUfnc3Rp5oT9NKKT8__O1zWKQD0yZE-KgtOGhziLAsgC-2Pxa9WIHnbNQCe_Sdh3fZHzzQw9RcZpt10tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVfsOmvmIOwRHU10V5vSPM2lZOrIzrShNJpV2Y77FNW0i5dUyMF3XP3K0YgDokKd8xvIvd6L-q7wJUJ2peQxHlHyTA17TboF7Y8Z9W7qz2pWJdTe6AqlboeM4Bep4ovbwlS1K6iL4BG0g6YWNvTqGIHYJTZyQzDqTNFxY3C_6_klypHv6PFtCbW4NJuAV3FaaabKN2PmEwLgRBrf7IbShiYTOfk_oNAKGrUh3Sgv7Vcm0sFTjAq2XX6OdV68UtEPuhQq1f5cNfBg6rrEfymaXY6kVHgfkXJzfUqRBjlohSKSYh4VFSVgufhvnOqC12yBOkpdJ5Bi7G0Qu0FBwG0EGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeleeHglJHuehzqhfmzx_QU1mj6riUtYSarbZAMG1LXaRQh_ARFD9MWZio2VDiy9PREK2o7_Ufu8UK0QA_Ug6MNCyvYcMDWQlXi1NfYJhKAJNAHtlqF8taEU8zeUGt3NxgRZ_CDID9PMh_kNZE5tEUeRWIgiTzKvI3i4em3FMMo0CLLaTyLwjmZjEPymPOHIOAquEkTrNna7d_JjB5roKf3kFVA4S25uREzVLC_LwSZy66xfuuTcDDEbSjQqr6jXQdQt4BWzZYD3TMlM3xgevCjRLRAW3bKG0QXs3pCgDCZdh2_guz6E4HV4zmeCXjknq813hlSZnr2J8nG9eroF8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPc4Us0wQsN5OhxN_nWggkIM5M1Nvsf2lm6x7dz_1aRlET5fFBmUQ3ffTBH3Vk27JyJREzCeqTf-CFt2PuN0HbvVRMmNJRxpGQ3i1Cy3B7uzbnaSF0fpWOF_3jLWv2wk2IJd6ST33rf6cnCrKxPUYvT38qaKMQBG9UJQq0a9Js9qNBD3qSgjzY-gR1Udbq1OyMtAlSFGqhNfe1YEl7CltGduuWCPWEOsOk6wHTpNSe_tOob9GKt3T4dlT5HZ-ax08sLbppnfZ0pCzzYD7lX0RgfxbRyrHFw7zxzJQ2rZ2zJt2m2fy9PhncQG083ZErtG3Jp4IqfKykjAIneds6gdFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5-QeAbjVfqaw8o5LgIyjAXLC-FwyOJ70JE9L5rXnOWg5gflKZ8zekADG_jR4CK4LOP8YDu6by91ksjZXY4Xifjip_jBtveV9KJtmybXt6Q6G_SSNS4qIIhWdUPShVipKhaIm1PVBxyoxKFcFEl9X5AE3oAH2pZkwbxBSGf5tj5mzrsHVZ0n-Fa-w9xFkdEwS70wtInrVmGu1Oxut7CM3zLRRN1t1NYx17LGeaBemoTpEfmz5L8J2--NvM0CjM2pCRx8BHWE_OLSl8fhyR1xTTN1EOkZqECiNim__esf6jliFMGeXixwqzb_A8j8N3lsBhMX2aeDFGjrVwvT-MbHdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtGqgba6BruaRmSJepIvRJRBDNhozFiB1a11Btu4xaqdm6eWBv9GY5hKN_rJgc2XxwFWPogFFXB30uNuoFELzmx6R3qh45NU06-3MGNHvcbSw7a9l4roNgqR_5Ef8DAzg8ScW_KYlzq0H164aKwHP5AxHQLOsDo4IBfJLZhK0_YivhYlvfwAOrG0VsXyrRSNtywEwUjY-hI5VjBnXK0i9So6w_kMkabxRMsAyRR178fooYdYeq87cP1HsI2aoil3jFXZYrWpDWyOYo7DpFcsBbBsDgEYHW9QEvUMWBfG9g8CYZChaD3H2Rbz2Q0kKZkh3WU-uA5dMnvsIME5-GQ9WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند
«مصدق علیه دیکتاتوری شاه بود
و شاه علیه او کودتا کرد.»
ولی یه سوال! قبل از اینکه شاه حکم
عزل مصدق رو صادر کنه،
چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند
و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟
بله! یکی از آنها «حسین مکی» بود!
او نماینده ویژه مصدق در خلع ید انگلیس
در صنعت نفت ایران بود! به او «مرد پولادین» دولت مصدق می‌گفتند
به او «سردار ملی» می‌گفتند!
او دست راست مصدق بود! او مسئول اجرایی  ملی کردن صنعت نفت بود!
اما علیه مصدق شد! چرا؟؟ چه شد؟؟</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVt3nl44H_AtrjhEUZu1U7Gg0amqiqAwqlpfja2i-FpNtqXWFCfwUTiZU0QwdrWg_nQFrw3dFoO3VnWm72IHTXRvwlUX9Z-w_ErDvhQHTJ0KKAJnoZ___r0QNzfzsvcQ8HHPASBGPVtFH1LCOcd-iHEEsPGOKeGF-9FiIE_eaBKIa9rgyX13VlNoab94VtCy3Hjj6gyR-G88qzo3IoO2mbTEHnlGRD_nTY_PZ1ViH9DMaTArkMXFzeSU-v1vLcAQkyTs7ghjg-Tb5rf3Dpe3eBCXFYt-OIcFCFnjhUXS-APgcXmM_QMu27mbebCXNHnIayXV_vgQ1GShOgVQUvU1bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ei15hK44JU-khp0HZeyk6UonR8Amn6gNELrSXp2qMURe1OOSz6JGPdAR4O1oEJwm2dDIMEotvkHQ6Ry6v9qbBaFTkmf3yH05yab5-bSuiOhtrSSxdmOAgYkQcyysEoeW4RfrkYGaR6TXi8Lxfo7zEydvZGdnKmxaHN7yIxQTcJwPQTc4e1k3xbrzrSNOP9ZwixN8VEBiPeFrvBuxha7M6FRhOIl-yhsi3wCLQA0x0vtI7F9MDmOLhLiXTWD-qTuHy07IBQeTZ9_Db866Rw5-z-36nBFWzadEvD3ZNO-vWhNj1z9_aKHvjmo1fIMp3FyA8G0SNSVaEQofQSHizktu6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/moazXqmagn64PH9uxK6j-CZwdyj-S0kPdwpRaUKviV9v1RyXdwGuFZExbl2v4chKqWG-rMYDpmDuVUtwz_wCVSbbXumgas6qKej0W_LhfoYwlFKHmkEzpGhEWeJHcY8HLC9OtKsSPMi3ZwZKppRnmf_zSuABZldyX46kasesCrRNXbUQySc8dFDyEZ1-kTBXI_Y12M-ak2H4kHcziIpXeuBDZoqSCfe_wPlwbC0TdsRG1l0km9sqP4wpDPjwwCpQhQD3XawdERf7XWlav-LsZD3r5dDMNq_PQnSgn_Q-oJbs4w9CPxnMtmFOTiujN0lL0QcN-pnh6zBB3Vv27U7lUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Npa0IzIUgbPv9MQOSUpE3F16cB4Wb1oFeP9ZYUPxKcpwYGYJlPEANd8Cx_ygVp-pcp0inQBRB3y3mNRWiyyrPjFgcZOiA0vw-2mSt0HlVVWYZsSFUXZ5QM7QsKD33ODz45FSpjR2dg5rq1lUhb6SG6hNO4KsZeZrxfTil_kdJvfAWtqqmNQq6L_VL5QZCB5ivx6jkqYxeKIWtsjuTkzdHFhi706JkuKmhRjx_46-FJBLlsXSMrkSpHQ-EC57CmwmU9DEIpMoBiewGSjn_M2LyWmo2YhWQEQ8NnqHx4m3fiJHyBG-TqzI6HLlbNegpw3ZWrFWGJPVAhoUutvyvDewXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXSy2fUhqrs4IAuZYyxqGCMzs4J9nFAswcDnnULq-myGpvmjV2nOBzRUFQC-IeARLoDtZhz8fOD7ciTht8GcvoLhC9B-C1ny0ktH0lT6hfcGlD4NB0FByjx4ziAnd878BmYp3fVc_0RcWFoRdaVdqVu2CpKEvTiBcmb7Ie89aXzTomztsWLYi5RaPn2MwaoWT0kqsnRGGnmd6MuijVOu_2Qcc-bXPImYOPmd_yNh-ND9OTEQIKCMHU0Uk_LfK8h4k40y9tABoCDUIKj8BvTCxb8TZOsc2B_vtZm9vho-tqctQfI7cCy7O3NfwyXyyrqjYMCqrOS7-wT9OcZCq6aV5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFo92_eyRSMwSDVKFXiNmWveaBDG4g5v7TyCBFnzqjs6TeloZaOdtph3-AiuG5voi0SHbS_Tw3xBBohNKnIMJJGF3bQrqGGmowwpp-TJqeemsD1QcL0weZdf4mlubuAbUUCjUi0XiKu30AiyPRzph-96bsTWeAiq4aA2W_vuCxwE7MReFVFjRnC1dtnz995NTWGzn594fM4lMTuPwnx3qTgiiKLwPa1cU6rNyXmJnwJUBzrbFsiuFE9MufDiauoe9_t26OemIPeV_7wbyNFZeyCsjZr0bNexQv2ltz1zeQGq8ah5iY6O87WOnRIxpVIhq_yi0Bh1AqH_7XrJtCPf7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGzpZ8eDTe4rUu4Fe4GRiJbxHXpEaPZbYCFUmFjuaDbS0TUMGnb6Ngut0OLYyUZv1QAkpmUUx0K7aqcPcYZ3vIxCvSm65fUGqgT8yhsrnij0vP1j2flozQEB4Im1kf_BguVs9D4VualexfHmIczDs0vPN5acFcUs8bDks13UgPO1b2VHQcfU28utDwq_FHfPTP4Ru4VGte7T-E5mDX9VoHNYILfTPzCSTon4sMlkaZURJ8-wNz9Puk4aUNAnx1BfaBEchVu7Ze2GoMiRScZkdJhm1SX37xh07RGGlIexVp4Kzsd58zXOsL0o7XnyvXh_v27JjfS4G_qOvij4KWUarQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwOH89INHgkcB5jKhReoIargzTTLrP3v1PycNfGpuORUxoXmKHRv-ofpiWFo83E7Zyg87NrxE_cMhZeyBsPDbcfkzKtuSpkDGQxD0p7Gl8rmd5yclawjD17EGqoDKTHQwPjayXNbBkp_Z3IYfBWF8VEDjmYR-FbZ7Z8ovlfXZyA7R0hWz04W58wHKB0dc9-oHrbSw_RPNJhHUhTDjLh09RoY1pk5qPVaZ6hAp8qNHQ4-FzlKlHqW3uzm6WDkG4tfmVWLGcx5W7WK35759DpoI30LmmLzfPFfpFpOU1o02UBSnjRKUXhztL45lX0xz9Om3qF3yPeGDNC1D6wvzBrlWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpt48Ru8dcn3tiz0pLu_HXQ36mJJpwIvbhuwqLQQtxXWEarRHe37oEGqpypmcW9mhUZLD5m6kmoImYg0yhIk4K6oAnXl6gY_gXqfOT56XRRJsaem720Gqv3srB742W-eASp-izsTZ9rLQvthQ8IErnKgWG2FIeLcYffckib1JhbNYCmH_M9zc0fogZZ9u0FSYl-0VWw07IHndhNnhZsf-Hn_HNMBsfBqs3XdkL3mO8f8GnOc7L5Fphx_r-QR21DsxU-HfmylqcF9QZO0n7vOTAdR7J2aFIhjC9ekD_Q3lSe9jexD2X3BBiXgTeicXCJnpJGNAjRTzo-TSpGwgOp5Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwRNDTEqPb6WnNsELzGjhz_bakSkFKdf2SEdho2-v6c__a61EIYai_xj8RAe56TtfT8FhLgBp_JU69dOd1ObN2JvmmMz0Etb0Ga0Oq2w8ft16JuBtTbfSgzdB_-hmS38aq7htaZJJk1ed3Y1RtJVRx59OkPCGIFLrmOyqEY5OiQDkQp9yTBQnvnUzW9uf9psS8EehlS5DqZTiQ8Shh_1Ej6SWUn_bLT6137v-wWDxFVL4qIbHrQkIxK8GNvWVLzI-kcg5CZSFKFTICI0qOulkPN84y2We7F0ktVLpoch8Szj_j90fe1OcG5mdUeY3TpgVGiNeSadrg6PgFpFYNQEYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNZ-v4NEW16bBxot6AwjQjHuuBTnQfYJb1vAh30d_ySnmm3oZlTdJWMgv_XxoVUGUpoFZ4wwUE5Z-tgLDi-C-YcXhsIuIy_1nIxuuoEa84PaKZ3sViwStYGEPIU4RGPxw29tblUEy_sBHsI4z-rKYb7YlFkNwgB9ivum32zEHihPwc8TPBSVD9PiAGBcBn93-Jh9zSCAw-oSUduV05J9mMhsVzEF23JtukelAlgp2qsvcbmu1pRs946pfUY6cwDMYhPyOu1S893x8_2YWirmoFFWIPGDogJtEfKw_T4Mcp6v3rFFY2U_pIAzN7ov68F6PjlxGKrdNXpgxsEHVZyylQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtXKNH1fLmvkZcBItKU9zG-V588f-GWnlUvGC8yvxqEXhn0Ugd6NKrbKJvknSNeAwbnw3QBt6ZYY1C1bEHtlhzVmhot9IcsYRRmT_jk78U333wFPkS1y4kV99rYEFghDlZlDDhE-lksT51cwjkoFRnh9lQzHql69kbm0jtbyGlBdxpopXN6pHFliaaszLXAhskOYYrXsMRMEN3rQsCtnoVxt963hJb1a0vBLhAn-nMz2hbNvSi4bjSU_6NQVV8hUirRp0lySqUsoCa3f-UzBjiXIz-bT8dfRCgofzkBVbNpJnSNhGG1pbwE2Qo-yWz4qleK_JcOVXv_GGMMKoIWvqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIH3WQVePWAY-KtJX0_gpiHkMWgUyvtRP3NGPG8l4phD5VEuOlhv1EzBSjXx1lDaTWz4CNcPUEzXOFD9mNCJrTCV9XgrW4D8UwhQWbVQBcS9cZjXz0WxuZ-AHszKvwzAu_3rMO0ViKAK0fntUHpX1Gj90UU00G_W5WcmG__IMr13q5Y5xouBJc4EDepPnyjWic15XzVZpxuqvdGjgTo9ifD1yJEZNGx1JOgj6v9VK1BcOL_dZxxlXMmNWfk_ICoo_eI-2eXJ87fBzxN9T05Y9kib-vyAhieQEcdZUyMglZ9FxNhHWWL-fZxkXKvxZpZFueUKSqXkMQvrzatrnrfA4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1tCVKxpbnlK75vTL2q2sbXBQhyC8XpaXcUSJdWNOXsZEtpw-kT9dBqAePAjcJ-wnebabdJVY8GWZqao7vTBtfQDG_CPyTC9gKTX37byIi3VSeSPQyBDlQe9AsMyJgTACixT2RNHpeZH_nyUB0A9sI7OVLDqvQ73xuklMLGX7AWjL67OiKaLUPNbYT1e9ceSsyuAjyMsJzcbbYdayEHVoryjFLCpSqGsx7kPjT5_M7cDXh7MCi4D-m7xk5MLL3TGy7us9C8TpaEfgOSmighiIpLRys2Rvv-4EpLuSA62M7uCV9a5BC8qpS198P5SBi7W5AUlwf5x_D9J692TH1zhtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/We3EpHU4GAOe4ekHcgcljHky9aSHv18sK1CPngbaGdt_Wz9d4olec7nkrBERDHacQK5MpaLOF6sqArXFjpcAaHhSzmo4_1Ltq7vBl957COFwmBI0M_N_jecOIAYzmKrAE10hp2IPJh4KvXDAZKcXHL76tq6FpBa7ub9RsNBXq3haxVHsRiZNGbNix132YWZQrJcBSO2a8TesFOUqmFAEtywc7etyTKubF0xUb6vnK6yId6KsRuHA0a_EZ_b3XcbZJE4Aa7hQT7hZ6cqWttSRzC0SAVPqbtTgnfNoMfQzBswUUsI-TBnA_azJO_3PkPVOmajqrzK73gMU1cfI3e-Jmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhqm7Am1lGNT0qLeqpQTVkw2ScYVVDN6xQ9yuegIeTbjXgJVeHVbwGgtaODg0dzYJiOKW-yVCjSkUZjxMtRKD4VXIkM1DAC3mv_Af5su_81ga9TsuNQDjZYZZvBcXuw9PAA1pIfLwjDauwncjA464Gf-FNl20we-ch9tIWDy9gwCTpa1Lab0ExegBNS8xrUJ4zI-NvvheqwWnFkO-uOYEfyQ_HB_Jy7w06IXchAcqT-rS_H-4-uC5Ku98JyJxaxFIzftK6-eQG932Do3e1rk-lY0iFvRcaNvj1YDZEzsIIIFsEeXV4S9kFF0iKbfeZAb-OhOuwaE9cNAifv9nWwCjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkcvHNl1-iT3UOf23uTuiHTA11cL2J91BGRMdAC0a0B6ZfbigKjhzJvUVXhwbOQaiPivsQQLwv0gxH3vi0rWlEIbagXjxz3YGN5l2SykWpLZUYQKVSmLtzi2BWLmsWdwNzBxGsQs5glc6wAj7tw4foHD7zvqUdF8RcyCEwlmy5Nuf4NY8dwwnwXVCjGvPRyBk36wNBUSxwN0MXGUPkxLhzT3a9unhSDcQO8Q5Y1mlwBDrYdbrrGD9Ak9wOX-X2EdlBqgJ1tiyl4zVybHPvuLYjrKtvPChW_QoFSduXhJ295Qru0-uH9lU3hUXCqiDp23WZ5ug-2yqyGx2bT8iTkfpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPj9Nrn1hGcCQ2BN-ua5BFjEEqsJ3rP0dFclLm-kLjhwJidpOu7tkBHkuH2O9Gow5NDTIkcnLxd7enw4cpfslgKgfTF4dV7tv5YggdTdhbQVO41g6moHBUSGXjUEg4HFSLf8llQ2pR4hSZFxIxzrb0hT7sdYwhLxBY4MOQ8Gmm66VzqfAMzcmasqgDe3QOWOMuA6DTFPO76njwGKsPKihkCUloRa91__oYSD4rnNPYFLq2v0O-QTq1G8Ii_BOwdLj2gwLPW2SKnKn6levx2ePkmfq3SCd8MOPb-8bC0U1MLPAc41-_hwfFnCdif7fKyVdxCSrxleTa8TviF5G12QUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMF8lV4RggGwgiWHJjewHvfWI9-PE2r9XqHKgqNhyNf69GF9hI3s_mTHEbQL_FeFwGrlPCVHP5NrqJD6nSjd1d5p0CGJukthxS1g3__jOIQ3gBpyGwyHWPT8wBEahd-RmR9mlMyxcO0No3rheq5djvS3YjXeVC3I2YO0b3YBgEcgd8LHjkbHgZ4l8waUI7UCuozIO_LTjNiLFvp7dF0H24_J_bdV5RI4ej2LQETElucLK6787qoXflmY4PjMDoqqi38nd8XN2Tj19ST1uH8dL33jjmoJxkLH_nFuQ-uzGbfm4F1NjvxU1gyFMYDD1ApqDsmkvcki9yVyC9vqgF8J4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت.
ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى،
چه كسى میگفت؟
این حرف‌ها را مصدق میزد.
مصدق حتی اقدام رضاشاه در آسفالت
خیابان‌های تهران را به درخواست
انگلیسی‌ها می‌دانست!
او ۱۰ سال پیش از آنکه با محمدرضاشاه در بیفتد، یعنی در سال ۱۳۲۲ ، نطقی در مجلس داشت از آزادی حجاب در زمان رضاشاه و تغییر چهره شهرهای ایران و آبادی آنها انتقاد کرد  و از جمله گفت :« رفع حجاب از زنان پیر
و بی‌تدبیر چه نفعی برای ما داشت؟
اگر خیابان‌ها آسفالت نمی‌بود چه می‌شد؟  و اگر عمارت‌ها و مهمان‌خانه‌ها [هتل] ساخته نشده بود به کجا ضرر می‌رسید؟»</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6596" target="_blank">📅 11:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6595">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oshIujpgONBPV6O-ZQSpyMKa_p-64HOiz49h7iNjgiDjVKuF_mJEIN7UiJRKRAMJ60WQN-SI-80l25ZT2BG3zQF0KTeviPwDPxLsUvQcrfoENxdi_PFTAgzr18G-NaVg0hkKN5VnqRuDJuEKLmCJalKGuoop8bsBA40rKfQSvpQIHOaC1j12h5mwME0OyNCRtsflTW5-0yfqsyShVdG2X2VATl5i-dGTF-wgnFv6j0nrBSmGeNAp3yL5Qmz7qJTIr4c844KwMwiFMPXKlgVabcBbq1mIN7PXCR_YQAXS_Ap1sw_EYyd4dOeuW4cuAe9HR3BT5zMdwhdhHypxQscUrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز نچیروان بارزانی
رئیس اقلیم کردستان عراق رسما درخواست داده بود که بین ج‌ا و آمریکا میانجی‌گری کنه.
خوشبختانه جمهوری اسلامی
همون دیشب با پهپاد به دفتر نخست وزیر
اقلیم حمله کرد، تا یادآوری بشه چه موجوداتی
در ایران حاکم هستند!
کار خوبی کردید، قطر و پاکستان رو هم بزنید!
قطر رو ولی حتی بیشتر!
که اون شبکه الجزیره‌اش
کپی صدا و سیمای خودتونه!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6595" target="_blank">📅 17:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6594">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپایگاه خبری انتخاب</strong></div>
<div class="tg-text">🎥
تماشا کنید: «۹۰ میلیون ایرانی متهمند، مگر اینکه خلافش ثابت شود»
🔹
این هم نتیجه باز‌شدن مجلس پایداری!
🔹
عقلای مجلس از تصویب جزئیات خطرناک طرح جلوگیری می‌کنند؟
🆔
@Entekhab_ir</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6594" target="_blank">📅 00:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=rYPJ7xtu6SVB153dFkzNSpIsExPgNBF9YpgXy5Bkc3gObIn52h3Oo5sQKQCZnlWIcKXBSjaQiZ7zEgo9XDbiaW84vRsa2PGa-T9_YIGmUa6jcA1Zcr5nNVo5QnUsK3il8afO4QpVdI8COQSyWHJH3JQYqFAfOk9xdbVCd1QARU-r5I-Q7GA4IGUcqW1A6QKn6CVqqhlSgcrq7JzqBzD1ndGJf5JCfnaV4vWdp3VKbtcLdz9RBnDlCE4E2F0ud3UnPfnu4fr3Z6rk9GFj7gSXsAl_Rt9eeOJx_t1E2Mnr2H9TAm2eiBbngTX9bKDpbTt2PUFA8S6i60MuXfYiTQO-iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=rYPJ7xtu6SVB153dFkzNSpIsExPgNBF9YpgXy5Bkc3gObIn52h3Oo5sQKQCZnlWIcKXBSjaQiZ7zEgo9XDbiaW84vRsa2PGa-T9_YIGmUa6jcA1Zcr5nNVo5QnUsK3il8afO4QpVdI8COQSyWHJH3JQYqFAfOk9xdbVCd1QARU-r5I-Q7GA4IGUcqW1A6QKn6CVqqhlSgcrq7JzqBzD1ndGJf5JCfnaV4vWdp3VKbtcLdz9RBnDlCE4E2F0ud3UnPfnu4fr3Z6rk9GFj7gSXsAl_Rt9eeOJx_t1E2Mnr2H9TAm2eiBbngTX9bKDpbTt2PUFA8S6i60MuXfYiTQO-iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنبش شعوبیه یه چیزی توی این مایه‌ها بود
اعراب فاتح، ایرانیان رو تحقیر میکردن،
زنان و دخترهاشون رو توی بازارها می‌فروختن.
می‌زدن توی سرشون و ازشون جزیه می‌گرفتن.
ولی ایرانی‌ها گفتن اصلا ما خودمون از شما مسلمون‌تریم!  و در اسلامگرایی از عربها جلوتریم!
انقلاب اسلامی در هیچ کشوری عربی رخ نداد، در ایران رخ داد!
جمهوری اسلامی توی قانونش نوشته بی‌حجابی ۷۰ ضربه شلاق داره، نه فقط نوشته که اجرا هم میکنه.
هر روز پلمب کافه‌ها و... رو داریم.
هر صبح اعدام داریم، هنوز چند ماه از یک قتل عام نگذشته. اینها اما برای موشک‌های جمهوری اسلامی قر میدن و میرقصن.
البته که مردم ایران آگاه‌ترین مردم جهان نسبت به تاریخ و هویتشون هستن! خیلی!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6593" target="_blank">📅 18:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6592">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-4qVidjSW1RRL29efhKnphS0V1MlGeLxxQh1QBiwBRQ7KSKCimEbgUsYTeGX1UV-utQF1TK76fVDx9k-0_L81EN7qn0CJeZGzugxrUq3BfnUeORQqz9b_Uqqllbt_TbXokks-qHxEiKY-Qh8a33LEC1GAv9P_paDbozPaVhJ7Lj-SxxFkHomRjHaFse5SjYj0KFju12xpp8LV4qVUfqSD4vNcP8qGps02HrpiTDSLELxmGA1iHIKdKtIqt7JYiVoYxFXjoqXJOKOcyQyLt4Tdda4MOeq_yEvUo1dJ0qab6UFHfZS2ETc4y-aOLqlgH-NddjJmPGCcEG6hGnMLqQdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=nUC72VVXKJepXnBHEQZoXRNlKrfvjqj-E9tcgp4WyYP_1a9y2g3W2qIOY2gaRNEhHAL0iqOCpUS9qY9mBl2agTlMlw_0nWF0w81MXfVqHYK1lICF2_1if40uFs4YfqZ2iDUKxLl9MaAO7NHMZqDBv9YnTXrt6u9wvkTCafRmWwIRpIW8Rdv2WWUTTeSMORvMXpERu5IT4HgsrqWEdjLihiYl_R8ffLh-UltDSMVGtCRiULkSidyG4LRA9xyeG71r119w2qhaP-zdBoh0pRGsebGym7CCX7orOtvVLe2Q_KVbvqKTjJxSHby5fgZt9oadPoKU4qx9d0U_p-00oroeUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=nUC72VVXKJepXnBHEQZoXRNlKrfvjqj-E9tcgp4WyYP_1a9y2g3W2qIOY2gaRNEhHAL0iqOCpUS9qY9mBl2agTlMlw_0nWF0w81MXfVqHYK1lICF2_1if40uFs4YfqZ2iDUKxLl9MaAO7NHMZqDBv9YnTXrt6u9wvkTCafRmWwIRpIW8Rdv2WWUTTeSMORvMXpERu5IT4HgsrqWEdjLihiYl_R8ffLh-UltDSMVGtCRiULkSidyG4LRA9xyeG71r119w2qhaP-zdBoh0pRGsebGym7CCX7orOtvVLe2Q_KVbvqKTjJxSHby5fgZt9oadPoKU4qx9d0U_p-00oroeUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlhhjaU-u7PfsW7-v8Q6P_NB4njaa1GM7ys2WiBYnnQpk7vvMCtd8q_2nX3qqgT3f1LOJhYLKsm_wz7ejWW_Hi7NCMmd1Jz3I8IdacW80qzjAmYiXRKxNubETldMNw2yqRhiNsoIQf6XhVJS7T9QJ8GEz6nOBlI9fnFpI_ab452rGIaKH12_i5x3B_lQNHuiqGl0cJvUC91Xs5IvqWZbH-qmBDg0fdqGqydkcKQy4r2sGlMbXv-_jLkxeEpL1zph9g03Bd2Y6MlQE6tNBXhZaxCLD03yc1ww8XH9GGMv77ZgCqMNU0GTdmI-RFCSvNcBfvSJpheJ0q1_WbT-mVBr4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2f9DFsniY-tgnsVlrWnATPt6GNcAduRSl5Ed8UtOLs1tiIL6neAECYVu19cP0wR0oPmi6o9r4bB0DQSTRYMbz1qKn513AG4mINTnoMJpkgRSqh_rqHLUPhKk6UU6xXLsPRXTXkL6WSvM6ezSn7sxbH3361ogqHw7I1-MB5t1bN_S1aqMkAJodrnXbXROET9XXhv_CJJheistMK-5JtnN3sbnf4AvWyiSg7T0zWfOZoVK-zhBoFjWlnKfQHn3X3Qnt5EyD_em3pkSiYS_EcRjS1Q9FWEiT59X85kwSXS7RXU81b4nw2rgU-aHg5JFMd-6CKABGHezbHeMlhaHY9eEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=RFG74MZhz2CvGZDZ7I3_cgWKmnET7d_f9UGKhswJMoUTCSVnYKq9qJ70Oybxo4OP4Rl_t6fKek-Aa0vRPuuUwRORuWQeeOuDMAXAZSfkgCwArpD3Di1AqrxHeWzYpI487-cpQKZPObZ3lHEBzqfuO8VpHCA7mvEqMVA2OOka34t84LsZtgnNXX1IzmH-7HShjmrFq58KJVmBIY22o8rknvsw3FlBYmVvPUFC6Fj6Y2-6JVzZVRla6L8REhNSHuw0RSM546KgsDh2KDwoJKFA-1-0BXKTnQuMHg_BHg3tWqT4aOz13JxUwyzHRcyGFdj_bltzchKC-JKbyRe7eCbEiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=RFG74MZhz2CvGZDZ7I3_cgWKmnET7d_f9UGKhswJMoUTCSVnYKq9qJ70Oybxo4OP4Rl_t6fKek-Aa0vRPuuUwRORuWQeeOuDMAXAZSfkgCwArpD3Di1AqrxHeWzYpI487-cpQKZPObZ3lHEBzqfuO8VpHCA7mvEqMVA2OOka34t84LsZtgnNXX1IzmH-7HShjmrFq58KJVmBIY22o8rknvsw3FlBYmVvPUFC6Fj6Y2-6JVzZVRla6L8REhNSHuw0RSM546KgsDh2KDwoJKFA-1-0BXKTnQuMHg_BHg3tWqT4aOz13JxUwyzHRcyGFdj_bltzchKC-JKbyRe7eCbEiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8Qf1PsVYJJGoCiHpUHHSkuVsgYorM4Tb162msxF-CzzX2kABzhoRxLTby-BWrNehOtmkGpiZabpO992CJswecgxgPO1t-77ORVjQUla2p6ef6PrTJPcLNtfPTB-rRmRn1hQaKJpaBHnHqDm-H_AFAH6q6P9NeIUC7GkuaQ41ZkOp2j8IJEAF1hhvSUh7X2ZKqH0cmWpl_q3PocUIO9-vkZQJrmzzk1nT5bv7zStMJVPwqfxRXeKzJoz6FR-kGw7MqnXZsQ7LxSRPC5VdlCT0aqCdffd744UCEGeRojK4-SoZAc11QuvfcCoBZcANNKytG_Ii0a4tS-YaXLXm6EJfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه
اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد.
اما اين الگوی
به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى داعش اقدامى
ضد اسلامى انجام داده؟ پاسخ صريح : نه!
آيا مذهب شيعه، مخالف اين كارهاست؟
پاسخ صريح : نه! به هيج وجه!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6579" target="_blank">📅 13:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6578">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2svbG9ypbyahPkisudubOMlvS8wunhout8J0I88MhoROuSLgXjvn7rdNv-p2dumg42NRKaCbIY4VamWMoQcsXZmI1p5rPFgd8CggH70vqPO7313U51fRrqzRW0oA27AdTaPwzhz-CuYcDqIvs3MorQq55SuEZvGZqWCT0w8rRrXY2KGtHQCF4w6BWjcS7vHS3TVxwyCDBBpgJCsDHAeojDNPR49ceCZd8oy30b5U5jG8mz_iPnjOf-lM8sRn3v5pKyFt5Kw0cks8--lDPQiR0bf65Vniv0haEWL_yJ2MPCOBsqvCP8P7OGypu1ZRryv9s11mtLKpILL1mrb5lbquQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzT6g5LEKnI_Qm0Ysy0tpsQRMsX1gqoyakEjsWB6Xsfz6_X3JLgZ6ANGWkg-S2Nssy-q0IJDuScVAF-KPjHAHbVsZsZY42ln01jTRY-Lh3i2biIs47eL6x-xqtDnT3c4gjn7NrqzWvi4aAYHr33UEz-sZVeRCLLLDrMmLBYIihSG9ict5USX6td9q_hwnHH6JBqpaPPBYiKVpD9deqAboqPSjqhQN_vbRFfdRTfG0oXuKxlkkw0O7m2PtwUn3qxvqrhO1ibCS9Ol5DcjJpm06jGfXB015jSmlxAy0ju8jsMLAvbRm8aDpOxJgZmGbyKyk21IKLE44ThySEsA0zVbRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=HgSxShyoEZnm4kOLjEhQNdqIA4Mk1gZe1JaPgNYiOWAx01xnlG0myTBEhRjuXr2YDVHz6eJhc_auztpCbSUfk99BRUqvBxJ_wbh7JEuj61Uf598vl10q3X6WfCjfvKqDP_TUcW_mE8gZiIJhpn_EkuFeKbipNLI7TfNaVPZLL8eHfy7NoGkPoRbfUDEIbMk1Ass0_5wnHEBfQhm42EDDri9JquvqWfuz1-IMNZk3dGCdZe54nLNeq5kVYIeS1GgvyvtpR1NezlZam5y4LQG-vQmF26L_zKItrLHWgTqzSQL0xHi2O0C-LlOIuXR4T6BngAyYWMiHxSExE9vvC6asrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=HgSxShyoEZnm4kOLjEhQNdqIA4Mk1gZe1JaPgNYiOWAx01xnlG0myTBEhRjuXr2YDVHz6eJhc_auztpCbSUfk99BRUqvBxJ_wbh7JEuj61Uf598vl10q3X6WfCjfvKqDP_TUcW_mE8gZiIJhpn_EkuFeKbipNLI7TfNaVPZLL8eHfy7NoGkPoRbfUDEIbMk1Ass0_5wnHEBfQhm42EDDri9JquvqWfuz1-IMNZk3dGCdZe54nLNeq5kVYIeS1GgvyvtpR1NezlZam5y4LQG-vQmF26L_zKItrLHWgTqzSQL0xHi2O0C-LlOIuXR4T6BngAyYWMiHxSExE9vvC6asrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=Q7dxhstfaLFDHwpuz1ywlKSXcEkVruW1qV5zkRXU5NqqhkzzprbuBHU2e4vk-dSjO6cIRkclR06otwdf6YuPndByva_RoofRI-C2m6DfosyZhkbZVf8JR-Hj5f1yAU-gjsRVKuODklQaR7g0kjj4LbI2hFa3q8u3XsgljToHAdvnSaHmeFi2NeFj-e4BYghXwQY8xy5GJHT-omm0H2sx7AmNGK7ncvUNaA55dvQJ5zcmRelUn2Bry7C3hUiIvEBLHVJDfS6sXtFBQ5CtIQVzwLlDv-rbNQGLeACXXkQv3Qrde2gXM9fJ7sXMLhGZJdr22rzDp7c594W5cNIbfk3YIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=Q7dxhstfaLFDHwpuz1ywlKSXcEkVruW1qV5zkRXU5NqqhkzzprbuBHU2e4vk-dSjO6cIRkclR06otwdf6YuPndByva_RoofRI-C2m6DfosyZhkbZVf8JR-Hj5f1yAU-gjsRVKuODklQaR7g0kjj4LbI2hFa3q8u3XsgljToHAdvnSaHmeFi2NeFj-e4BYghXwQY8xy5GJHT-omm0H2sx7AmNGK7ncvUNaA55dvQJ5zcmRelUn2Bry7C3hUiIvEBLHVJDfS6sXtFBQ5CtIQVzwLlDv-rbNQGLeACXXkQv3Qrde2gXM9fJ7sXMLhGZJdr22rzDp7c594W5cNIbfk3YIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماينده ملاير با چفیه حمايت از غزه و فلسطين!
«مهسا امينى به درك واصل شد.»
مگه مهسا به شما چه ظلمى كرده بود كه اينقدر طلبكار هم هستيد؟
غير از اينه كه به خاطر يه روسرى و به خاطر افكار عقب افتاده‌تون، جونش رو گرفتید؟
حالا ناراحت و طلبكار هم هستيد؟؟
توى خودتون و دين‌تون و نظام تون
و چفیه‌تون و فلسطين تون!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6575" target="_blank">📅 21:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOZsCUSsvRFPoDuwV9u9cd8pIGxrtxyFeZnh2CNb_2snDVk8dCXmuSrmEuidRIZnZ13BI5tLZl9nNeMDtYqxZARGAiXpbxKb7AgLBC3ahFNdmpFzKe4da1jqrH6EGP2btTWWoOGp2udP2B9YtyPk1GTYyIwf-bY9_8Y9QA_bNq8qSDBMMFHgmF6h-75HBY9esoZsSoF0YwqceqcmjI1WbH6HoV1BBITw5uEReSOohXCyESlWrG9wXsKM48n41bMP2x9RLl2MGggmDc0NJDAL5LuK2ZgsDx_mgYuByWyZT9zOIviA9Goq48v_8rg-2q2ZGybKwweAhctjDa13B_Fn-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا اون روز رو نیاره!
همین ایران و غزه و جنوب لبنان
که حاکم شدید کافیه!
همین افغانستان بسه!
میخوام ۷۰۰ سال سیاه گروه تروریستی حماس نتونه حکومت اسلامی در غزه ایجاد کنه!
میخوام ۸۰۰ سال سیاه گروه تروریستی
حزب‌الله در «دکترین ضاحیه» بمونه!
و رهبر شما هم از زیر گودال و چاهِ حقارت،
«علی الاصول» بنویسه براتون!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6574" target="_blank">📅 11:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3xfMzpopt13cXuuH0VX5fHlOP6UPzWTMB63FguoR_z9G0fBsxGOFI1WwBOmx6HDXIQf-QRZiyob5nL95sCvPeW72HFhOI5SINW6fud8aAOcpKv0EQgSijfzNKSL6vcfIvcv4E8TL25gn_sNA8yLHIlO7zLXDBofL0uixd6VbUScGmacABPpGfLsWc1cpg8l23qeYPybt8mXJCrk8Vc47j_78MD06hqxK-3_g295FTGyW4nmRkWMHUz516Czb9C1rQ07d7FrlAhiurfGCDPUVSklgNeI5NcwDuaZBw2yTqAnVp-2OFhtmmGWtxbcV3mIyxP61qwkRaZKZJxq0YCiCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnSlC5HkG0mw6iy7FlAfcTM78xbta4wCW_ZFbzT0PT1_GT_ohwgT1m1VQsejaKNjIZCEOo_LBIRt2eE9VdIo3n2OmPzfm93yo2NxxhDunXFq26j9DAQQ_Wvfyq_i9K-fiWixTXcLhgsG6xVnlo6pwZG24qhHa1agLGMX-Ot-yRmdlNuE-SNhieSTTDGDcOGaOU6hA3eMNbOLy7nglovKss1XePDIan8qAqfm-P95_Sz9foT_hG9EzMKYRfRJDUR6SjiBK_hoPU9oBHHPmVvf2DnILdLCxOEq0lM-tU7ifN8hmNIsnEiE_4ZjZLVRXqGwIItzG01wilP3Z8kwjLZ37A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8BlUI2xbLKi9zxyoKUmhjB_nikGamjh84AF8Jg0YmF5Yyvf1oLznApi_Qi9CwJrnwb7yfI2VNqA7010LhAAXGoZKrkJdp5_GVZ8OUleLEERTH5c06045cUeqrgup0vwXkJysByIqfR2mW27IlPypP1k-MHe9NhUxFwvKdADv5Odmx0mkpOKUelNRhNxL4ZGLcXj9uq7AwmYa7d2hoxfvQINwqmDnrCWIpaM6puTGBeR1PMna6Ks-fBNf8qILaiArj_Wf0YYWMR5KLkuzb8iBIDhoildAfWtyAWtJapOCCkxb5M_JlAecjaujpIJmLsJXAAnGy4WjlaNhYAY6Rou3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hbl6UCfnNN7l8tosSWmZJsbaQckXLU89imzdw9R31HV1wRXdPzGI_TBxk9PdEPVInjeg2tIx7WxAh0kX_O0LE44zSBktVnkP-hT8el6glAO6Cw5Bp6NEpMbVoKyhG1WNy-YWMCkG-sHn9fnfMhSyL5ABxSkinVmHl24WlNRFR9gTd3sEWW8mXPz_fGD4K4VEfKuE_l9FMLbl9sqidZgVW6FrrqvbTh2zoXyfKOxGZRS1rfOSbnNNkNGKI7SWO1qhL6bKDzAkXWYGzcs1eUvepPwvpxMZof5Yj8lJtcAHsEA0W-4QLFeFAXDAMUsVomhJXPXGEBn3o-c6VkcEh8_SwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFThwjSueGpfXao9_oIRu4bBv09wDim5kACn_r91kYmreCTezgBKJe6mI6M9-nQT-iIZBWjP0iojGhNyCx_m4BnQjImllL7vfXFyUgwE2AKcUCrV_YttZCuPoyOYrMcvVzxrWBxiLC8lP9nzDh6qb3wRYz6l5p4978xzA57QxxaCX39pCmVUMKhzG822B8vJoUQV3SZox5V59ILMxfyKh-BWftb-lwF6ees6kWrgPNLIDesEdgcTj3IRlixm-I1z-9Mzs4x3dUk4lLJGmjV-C3mDaBspZNRJJLcvhhz-XmE7dHfRLo9xG7fuslMlFS04nswKs67qiBvj5Gm3YuUbqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر سیاست‌های این افراد،  از جمله این زن و شوهر،  کل کشور و جامعه ایران درگیر یک بحران  عظیم شد، آنها از رانت‌های بزرگ حکومتی  برخوردار شدند!  سید محمد هاشمی، وارد کار و کسب شد!  از واردات قطعات سلاح برای وزارت دفاع تا واردات چوب ! از جمله پول…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6569" target="_blank">📅 10:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">معصومه ابتکار و همسرش «سید محمد هاشمی»  که او هم در تیم گروگانگیرها بود،  در همین ایام گروگانگیری، با هم آشنا  میشن و باهم ازدواج میکنن.  سید محمد هاشمی خودش فرزند یک آیت‌الله است!  گروگانگیری ۴۴۴ روزه موجب آغاز خصومت شدید آمریکا علیه ایران و آغاز تحریم‌ها…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6568" target="_blank">📅 09:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exutxbYYGiLu9DeyAsVGFcT2GNUYEwn_nNgLhf4FtHa75EMyIQLElI3UKE844snJcdFpmT3cA4s0A0tjJo1L7YVuCij1K7sAIHnMbkdXz-_ybE9aLtS9_2r3_vLZ965mMZ5U-94ayfAuqnHQQDzrzmBIZDITY3MpU4c4OSWiupe8mrOkuB2a5mnRl3KIPvgOovePmZ6PkSBDXYqJxdzALm2zhKno5jcddU85yF9B8F6SkqW3oeL13vMYsLnB47JAvKY9RahWMZD4tHIDxHhSoPBiNy8yBVRPIB2oPUNCl9LYnhRfQEsRCkc8_wtLalwyBrFb4u05l2AciEWmn1GDeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم در این نامه به مقامات آمریکایی نوشته  کارهای «معصومه ابتکار» ربطی به ما نداره!  ۴۷ سال پیش بوده و…..!  توی این ویدئو که خود مریم گرفته ولی، خودش دست به یک مقایسه میزنه، میگه بقیه پرچم آمریکا رو زدن ولی ما پرچم امام‌حسین رو!  در واقع عروس خانم خواسته انتخاب…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6567" target="_blank">📅 09:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6566" target="_blank">📅 09:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=wCJ-zPeHa46LYD37t1rwmdFuw8b8TZBy3e27yePR4GPUxAQw13RiRdd7wOx8grqDOMiztsDk4bGN7THNxUsGAuHAuolTVxPloMIZ37haI9kbTN1h_Ys__PleTUItmZ_GU8uvmC-Y_Ov8W2yjftiivwhvHCXo9SZd8ADMGkg6ys0AALLnNhlYaDg3uuslLgMHWWnRjhFBJjsylNO5c9Rytjt6RBRl1sDzk07L2iWC5Chx8B6Z0VwJKEjUZMFmhdxWwnk-m7sBwb2k4h0ok9xZv07SXJKmP9G1CijKz_1RVC65UR7I0X7Sxk9EClQwqvwiyvqLv7KXF7It24UYZK0igQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=wCJ-zPeHa46LYD37t1rwmdFuw8b8TZBy3e27yePR4GPUxAQw13RiRdd7wOx8grqDOMiztsDk4bGN7THNxUsGAuHAuolTVxPloMIZ37haI9kbTN1h_Ys__PleTUItmZ_GU8uvmC-Y_Ov8W2yjftiivwhvHCXo9SZd8ADMGkg6ys0AALLnNhlYaDg3uuslLgMHWWnRjhFBJjsylNO5c9Rytjt6RBRl1sDzk07L2iWC5Chx8B6Z0VwJKEjUZMFmhdxWwnk-m7sBwb2k4h0ok9xZv07SXJKmP9G1CijKz_1RVC65UR7I0X7Sxk9EClQwqvwiyvqLv7KXF7It24UYZK0igQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مریم، عروس «معصومه ابتکار» در نامه‌اش
به مقامات آمریکایی نوشته که مادرشوهرم
[معصومه ابتکار] فقط مترجم بود!!
در حالی که چنین چیزی واقعیت نداره!
او «سخنگوی گروگانگیران» بود! که برای ۴۴۴ روز دیپلمات‌های آمریکایی رو به گروگان گرفتند
و واضحا تهدیدشون می‌کرد.
میگفت شخصا می‌تونه اسلحه رو بگذره
روی سر یکی از گروگان‌ها و اونو  بکشه.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6565" target="_blank">📅 09:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=Hs8yBwbRQzZbf46tx2d4DZyMaB_wxVDI7ByVt-OoH2dTOZ-C0vEb1p3tqPCLQ3ASXb-wLOX2JPVsJBkockUQX8ZbTBKlZZ5jQZco5WWFdjIk_hWNa7zgANfn7aQJdz6jZMdZcgXgDq0yuG5eL1FdUw7iIRsH6LlFtF9EznS_n4wiZa6sJ-W-OwJan1NQwmmlDk8UEq8S8ytDiDblMUAMRung2IzUtXJ-KcTj0OwVDsGRJJfsodjp59Ifdg4_1QEB6K8UBmNSMWfxtrCe685OXbOiqRZto4nwXtwjWIgUW8M5AfHoayuxLFCcjECJkeodZlMacXXhtGoF_RS_EsQo4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=Hs8yBwbRQzZbf46tx2d4DZyMaB_wxVDI7ByVt-OoH2dTOZ-C0vEb1p3tqPCLQ3ASXb-wLOX2JPVsJBkockUQX8ZbTBKlZZ5jQZco5WWFdjIk_hWNa7zgANfn7aQJdz6jZMdZcgXgDq0yuG5eL1FdUw7iIRsH6LlFtF9EznS_n4wiZa6sJ-W-OwJan1NQwmmlDk8UEq8S8ytDiDblMUAMRung2IzUtXJ-KcTj0OwVDsGRJJfsodjp59Ifdg4_1QEB6K8UBmNSMWfxtrCe685OXbOiqRZto4nwXtwjWIgUW8M5AfHoayuxLFCcjECJkeodZlMacXXhtGoF_RS_EsQo4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6564" target="_blank">📅 09:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است!
و این خونه عروس معصومه ابتکار است.
که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،
حالا نامه نوشته به مقامات آمریکایی که من
عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6563" target="_blank">📅 09:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=sphBxqo7mVPPkGnMXHUK9DalhgTIbomCOi4nlIykbXYlwk6TnAdwxrs1aA7E9Wg4thwQiVskb1SRWNR9Ew4rjX8Q5bih59i_8YeUBofvHgoH2kAjmlLCB1aYtdJP9fihPNJv3nKlEFbST_mX4fImYqNDhfcFoyXfWffylBdsdWwliEKF6I9cgFrllXxaVb0G4XmiXvRs21nA5gJVovfJ1ovupZdij1XORwWoveVHdU1JJB7tLIEfQbB_-0hxjHW2zJMpMx6pVoanGLgweeUDdBPmcQuR48a8d8H0RizxLwYnMLWZ1qDwi1E-Z1XthLVZU0ylCH57vuvU2D27tE3J4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=sphBxqo7mVPPkGnMXHUK9DalhgTIbomCOi4nlIykbXYlwk6TnAdwxrs1aA7E9Wg4thwQiVskb1SRWNR9Ew4rjX8Q5bih59i_8YeUBofvHgoH2kAjmlLCB1aYtdJP9fihPNJv3nKlEFbST_mX4fImYqNDhfcFoyXfWffylBdsdWwliEKF6I9cgFrllXxaVb0G4XmiXvRs21nA5gJVovfJ1ovupZdij1XORwWoveVHdU1JJB7tLIEfQbB_-0hxjHW2zJMpMx6pVoanGLgweeUDdBPmcQuR48a8d8H0RizxLwYnMLWZ1qDwi1E-Z1XthLVZU0ylCH57vuvU2D27tE3J4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت نمی‌تونیم بفروشیم،
راه دریا بسته شده.
چرا زدید زیر تفاهم‌نامه و حمله کردید به کشتی‌ها؟ که قیمت نفت بره بالا
و به ترامپ فشار بیاد؟</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6562" target="_blank">📅 08:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6561" target="_blank">📅 17:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=ENcCzGFqLqYtk6JX_efZCXsHMNNEr3B-z5T_xDM2JuUBi1SouiRv89SwXrFGHcadMvyKo-pEqAQ47WWpYs-gx2dZr5FWq9idyq1F49JiEtdN8S6QjUquwk-d89RPyl3Nor9b8RHXBAbZtgqkt5ZkVtZYj8hceHCY2SKbtweKga85jvQGKJ69QGZaQMNQ4p82Kc1am1Hj5X6Ri1Aqm5Jeo8GMEdf58W3wkzV2S-JEXfY_sBW0hXVOJ_PUHM1vjBOhTCVyu3xiw17TOzP49CF6Hpgd6Cp3vWcOJ_z2WihHtdZ6YgKjrv_4B8wsFJSQgtXHhqGT9ZHHPFKzh_SFRibsfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=ENcCzGFqLqYtk6JX_efZCXsHMNNEr3B-z5T_xDM2JuUBi1SouiRv89SwXrFGHcadMvyKo-pEqAQ47WWpYs-gx2dZr5FWq9idyq1F49JiEtdN8S6QjUquwk-d89RPyl3Nor9b8RHXBAbZtgqkt5ZkVtZYj8hceHCY2SKbtweKga85jvQGKJ69QGZaQMNQ4p82Kc1am1Hj5X6Ri1Aqm5Jeo8GMEdf58W3wkzV2S-JEXfY_sBW0hXVOJ_PUHM1vjBOhTCVyu3xiw17TOzP49CF6Hpgd6Cp3vWcOJ_z2WihHtdZ6YgKjrv_4B8wsFJSQgtXHhqGT9ZHHPFKzh_SFRibsfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6558">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=HScMcCqBNUHUQo-n2fxyhh6U6kwww8of8hOUlB_AxV-G99QtAM--MIfsIYyzUaAX1sEkE8ZjiKUvj_ohfeCIlGE7jBSq-VCzAzMh8S_9WLZparbXvpwpNH5_8K3iD6zCtDVQS0W9MQt6QR1jMq_1wlP62h3e_9cW_xcpTnukGY_TTyeZULkGxtAzfxR6IuyWGt6IKrtjF2D2_6np9EJWpPU6AJn_o87g0qd0v4P0Hu5nW-KIEc0xF5y2cN_3SMa-8hkHdIwQmhQoamOQ0gdxHGsJZ-Ao583uagpme99t_tpqewhk4NYIyvNVb0RcFz8FleGYgONku_bfdw9jtCkB-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=HScMcCqBNUHUQo-n2fxyhh6U6kwww8of8hOUlB_AxV-G99QtAM--MIfsIYyzUaAX1sEkE8ZjiKUvj_ohfeCIlGE7jBSq-VCzAzMh8S_9WLZparbXvpwpNH5_8K3iD6zCtDVQS0W9MQt6QR1jMq_1wlP62h3e_9cW_xcpTnukGY_TTyeZULkGxtAzfxR6IuyWGt6IKrtjF2D2_6np9EJWpPU6AJn_o87g0qd0v4P0Hu5nW-KIEc0xF5y2cN_3SMa-8hkHdIwQmhQoamOQ0gdxHGsJZ-Ao583uagpme99t_tpqewhk4NYIyvNVb0RcFz8FleGYgONku_bfdw9jtCkB-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08352cf997.mp4?token=exogaVkqL19SkJM_NWQDFgjYVobFfWuHIgooUbfPP_iDAkgpZ2jnP3lDuiWUNoRBD5KLnghUGNJ0ZlqIMelJLvlBOV-H_wrXz8VhpWpWYgOvI_64Tsk7tcZGfpecJpQsQR0aoI7uBRf0bA-y9jUR_YpzCaiy_I_xeezwLevflTXplzUdQGZqydeQ2_iX6TWLsaM3ibbxolNxiKXZLAMAq4Ci42NnkZUJ440WwHKrDNJGyhwJCXZnmxLrCLBv3olVx0ZKTucPA-IwI7WyJTCX5lL7Bgnny0xQbveDue6_x0ZIX_5MFYDoHcj3znw7LA9fX9gM2S_mk1rfwvWRi3EuQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08352cf997.mp4?token=exogaVkqL19SkJM_NWQDFgjYVobFfWuHIgooUbfPP_iDAkgpZ2jnP3lDuiWUNoRBD5KLnghUGNJ0ZlqIMelJLvlBOV-H_wrXz8VhpWpWYgOvI_64Tsk7tcZGfpecJpQsQR0aoI7uBRf0bA-y9jUR_YpzCaiy_I_xeezwLevflTXplzUdQGZqydeQ2_iX6TWLsaM3ibbxolNxiKXZLAMAq4Ci42NnkZUJ440WwHKrDNJGyhwJCXZnmxLrCLBv3olVx0ZKTucPA-IwI7WyJTCX5lL7Bgnny0xQbveDue6_x0ZIX_5MFYDoHcj3znw7LA9fX9gM2S_mk1rfwvWRi3EuQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نتایج حملات موشکی جمهوری اسلامی در تنگه هرمز،</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=JQO9A8eZYFk0TaV3tXCchDB1qASEgsFSBiXDzZ0SNMVnFk8giHCOsKOzJDg01p9vgQhyAqMkB5OB7hMxy5B4NKbSHxIDQHccF0jTzv9LsCwK94UpnJo6325DAXYfZIV0BJT4IURcoyxD33Nv16CGLBFVFkfLqJCQ2h4wkZYXHIwhpFC3kTffXlOvsL3Gcvdjwow4Ujo47q7Hmn3NPEb-LY5XHChqZM0x50OXca7wqWAnoqxdM--IYOYnEGeBuYlcPQl-Koo9LBq7yMxRvT2ekkmV40UZEsHWSZMDIUlBUkExa_K_W2xfAm8oHbqdttTy6a2DPv7E4ZTRGwxA0w0XDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=JQO9A8eZYFk0TaV3tXCchDB1qASEgsFSBiXDzZ0SNMVnFk8giHCOsKOzJDg01p9vgQhyAqMkB5OB7hMxy5B4NKbSHxIDQHccF0jTzv9LsCwK94UpnJo6325DAXYfZIV0BJT4IURcoyxD33Nv16CGLBFVFkfLqJCQ2h4wkZYXHIwhpFC3kTffXlOvsL3Gcvdjwow4Ujo47q7Hmn3NPEb-LY5XHChqZM0x50OXca7wqWAnoqxdM--IYOYnEGeBuYlcPQl-Koo9LBq7yMxRvT2ekkmV40UZEsHWSZMDIUlBUkExa_K_W2xfAm8oHbqdttTy6a2DPv7E4ZTRGwxA0w0XDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نسل دیگر ،  با بیماری و سوتغذیه در ایران بزرگ خواهد شد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6555" target="_blank">📅 23:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CduH5kJTYNNxRrX-tGCU28EFC4TmnkFtxdCc-2ioEtL7SWziO5LJKw4gbF3kB6Gu7Fis_RnYkPjmhpNugHsp_mCDgF9FKF9XxpYqa-TNQIFYg3HfixhYcxzsr1oOkV3LkJIGDqBB4jH2iSgcuO2sXc_AYrjZ5NxWLXXS1ioJyT4TwPOEp4TGQas-RrROmJ1opgLPIMG-Oc9jgdbnoDLLRv0jgxHytqxw52Dp11YCNVR0uRmd4owmpzLLRmelY4TAwbzf_G1CIuFhwmDuNWT6N2V54d9xrZDHdNZpRGI2ovGZ1RsC1FG5jlvUJPeFRdms1Gmxq_NemwTkiy_t8vlLIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6253088b91.mp4?token=eTIyJZecGnTGwE8QommBjqoa97Vw8ib7NIJQkjCyCIzMJi9SKVrcEO5qrNtZk_7fINLnAxfjjyezBMtHqFm5olvwT2RT51vRArLg3UOVWtae0GlAGfNiXBJeuSL8p4LzALVir3Q1xUDbmdMk209Hv1CHEP7P_4YII7gPk6ksFe3uajNU3Mr_Uo6ZTKnezknGfVuG6fTgcG2gwXlATkjWR-KMQVRLptrGKxN02vrN6SOP4n3z-zNEP0X3eXg7L9TGDNptgDESvxeFe0YM2ZmvXegddKUiYcVcpvcvuouM-hkAPpjuuAcixtpT4KkATYKIJTZo_0ARF-ixt1ICW0xRAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6253088b91.mp4?token=eTIyJZecGnTGwE8QommBjqoa97Vw8ib7NIJQkjCyCIzMJi9SKVrcEO5qrNtZk_7fINLnAxfjjyezBMtHqFm5olvwT2RT51vRArLg3UOVWtae0GlAGfNiXBJeuSL8p4LzALVir3Q1xUDbmdMk209Hv1CHEP7P_4YII7gPk6ksFe3uajNU3Mr_Uo6ZTKnezknGfVuG6fTgcG2gwXlATkjWR-KMQVRLptrGKxN02vrN6SOP4n3z-zNEP0X3eXg7L9TGDNptgDESvxeFe0YM2ZmvXegddKUiYcVcpvcvuouM-hkAPpjuuAcixtpT4KkATYKIJTZo_0ARF-ixt1ICW0xRAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل در حال خلع سلاح
(محو سلاح) گروه تروریستی حزب الله لبنان
اون چیزهایی که دود می‌شوند و به هوا میرنپولهای ملت ایرانه که صرف خرید سلاح و تسلیح این گروه تروریستی شده.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6553" target="_blank">📅 20:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOzFKnHVNYcdX3q7oJIHDWerxOJSGDg3HgENnlLuZD65tvpR2k4OiSuBZtKqPx3hTawB0BBZ6huf4n_Gigwx1CmCOmA0UnW4RaQt0CWkaYlh_V_kueaY5ql4S2OIx887oqNl3rcUVZS3uFxS50YcmhMDblonazRmTn9oyLPuULNAZ4yfj_-y6zddwu1VXII10kc0LdlCIvmzYZCw5XN7LeBtT2cezE9XNytj6gvoQtNceTFjw-GOdFgkmnLhSn_yncv8ZvLVdc1vCsXLVhd0V15ptW-gs1Zh6Y30e7DVhXydQ9U1UisKvh074t2OZ275STPn1CpAb8rmNhQmPoUaMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا اون موشکی که زاکانی گفته بود دقیقا به خونه‌ مجتبی خورده بود و خودش از اهداف حمله بود، باعث ناخوش‌احوالی مجتبی شده و گفتن پول واریز کنید  زخمش خوب شه.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6552" target="_blank">📅 10:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6551">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔺
آمریکا در آخرین هفته‌های سال ۲۰۲۵ (قبل از شروع جنگ ۴۰ روزه) حدود ۳.۹ میلیون بشکه نفت در روز صادر می‌کرد.
این میزان در ماه می، به رکورد ۵.۷ میلیون بشکه در روز رسید، یعنی افزایش ۴۳ درصدی صادرات نفت.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6551" target="_blank">📅 10:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.  جلوی دوربین‌ها وارد هواپیما شد،  اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!  نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6550" target="_blank">📅 10:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7kxRqsRnfC7vQBuZsmsGYsNF14RiCSAhM2oPZBQ4oKx6Gb-R-I57msr83UOTe-2Phu5ezZO6DE1fSq6ewKcmLOEkwHqUrlT2SUWsuT8QxPhBzASFOjciyjNveOMKltaHpwcL1nYgmm_tnH9DmBlFdj2X1wpYvBo87MuVvSNznmSdUqg0ASW4ya-3-qshlgw_0pBYPQrL1g08jg5T0QB-qfKMF8ku52XK_LC3xa70NIcNhJsMo0LWabGvBkzBWjR5P39Jy4Nhpc5f7VkTvwbsd3Bp2741YeiHHVAPlWZTVchjILuSvWi2-PAibDTqn_gTc_PfEcPH_4d5bl_yqrBgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لکه نفتی به جنگل حرا رسیده
و حیات درختان این جنگل به خطر افتاده.
اما این لکه نفتی که تهدیدی برای سواحل قشم شده از کجا اومده؟
جمهوری اسلامی ۱۲ مرداد (۳ آگوست)
به یک کشتی باربر (و نه نفتکش) حمله موشکی یا پهپادی انجام داد. کشتی داشت از آب‌های ساحلی عمان عبور می‌کرد.
پرتابه به موتورخانه کشتی «مینوان پایونیر» اصابت کرد و نشت نفت رخ داد. این لکه نفتی رو موج‌ها آوردند به ساحل ایران.
سخنگوی وزارت خارجه ج‌ا (بقایی) هم تایید کرد
که این لکه نفتی ناشی از یک کشتی‌فله‌بر است،
گرچه نگفت هنر دست خودشونه که برای بستن تنگه هرکز به کشتی‌هایی که در سواحل عمان حرکت میکنن، حمله می‌کنن.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6549" target="_blank">📅 10:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0dxvfp1pTPmYntFTUaPU27auNjcKlix9bwdPcKDQipG7tynZs1xZPmy_XcawOGH4mnndrrEaunDkp4Fw2HQbGmwHX72lnYQ4UGoHYSDYvX8Fzo8W2r1RoSiBEF6-sQaC-UhC6EdMiW3vyyj-i9bpQ2qOq73pW29uv3JWboGFrZd-bGt3PD_kPl6wS1BD1T42or2q_tuVvHDGt8X-bYo-hrXInG08CEJhbMmBk89QXnX76nnMMboGzdEUeqzg_imyAefep2kNfVLuvpMcPGBOczD7nT81HtzMdlhbztQ8iQCXA2LaSH-1vUOzgmIuxtEKID7yvIZ4FQboiPnnGp_jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بنزین در کرمان ۸۷ هزار و ۲۰۰ تومان!
میخوان آروم آروم و استان به استان
قیمت بنزین رو گرون کنن که بتونن
با تفرقه انداختن بین مردم جلوی اعتراضات رو بگیرن و قیمت بنزین
رو
۱۵۴۰٪
افزایش بدن!!!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6548" target="_blank">📅 21:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k06oR4RqWoEken-wasSM1Tm6dzTd8lxds7YaY6tgRKEfiqSEr8XNNE1wP2t7vBvzkD8p6qD3Y4vNfjS9JfE4ZrlhOp6jWGfQJJx6I9pgNYrVpPv7wlkt6NYUDX7JKhpuEyOK20_xXLddYjIGYM2IWE2PCYitQm3Dotax4vOGvKV6bLfH5MqRXOt7-tWn3dkMmeGfFJ3TgRJ3wB_8R9kg2EM_IiLAyG-IUg67meWclhXAdY6yZY02E9EmyzjSBZXV5kRXNTX9G5PSwrqtFyyBc0GIcoINMQhAPf5X21xxIXoh0xACUYt70C9pvvaJyqaZq5MSOi-ZyEyEERiCIU0s5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی میگه : ۱- موشک مستقیم خورد به خونه مجتبی ۲- مجتبی خودش هدف بوده  ۳- زنش کشته شده!   اگه مجتبی هدف بوده و موشک خورده به خونه، قطعا همون لحظه مجتبی کشته شده!  اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید  که…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6547" target="_blank">📅 15:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=i3bAgwsr5jH8yGsr5-AhmZmfd1eTPN_lf_3il8-khKXQniA76r27Vn2KsqnRKENyC_6-ocVYk4L6YW5hMds0sHlIlog5_wWudm1yuYvJrPThcJd08Aj3vz6TJJpRHKOWxvMvl0CxEzjp1_scQ9jlWSrbWwG1VosP8g6NLAZxnTq6yFZziMixiEN7yCaWm-707ivX9DgA20p7vA34iFJMZfIEumzdyMCWqHqckT5IbLIMDLKj5b0ivj2k0YxfDcZLSiaKvuPQaitSrNZUNYLzt7OWmOohCKidvj9AM1NYp1bc4kdVhjh3orfigp9htApa7CM16Ian4XqmyAFVx47qFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=i3bAgwsr5jH8yGsr5-AhmZmfd1eTPN_lf_3il8-khKXQniA76r27Vn2KsqnRKENyC_6-ocVYk4L6YW5hMds0sHlIlog5_wWudm1yuYvJrPThcJd08Aj3vz6TJJpRHKOWxvMvl0CxEzjp1_scQ9jlWSrbWwG1VosP8g6NLAZxnTq6yFZziMixiEN7yCaWm-707ivX9DgA20p7vA34iFJMZfIEumzdyMCWqHqckT5IbLIMDLKj5b0ivj2k0YxfDcZLSiaKvuPQaitSrNZUNYLzt7OWmOohCKidvj9AM1NYp1bc4kdVhjh3orfigp9htApa7CM16Ian4XqmyAFVx47qFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی میگه :
۱- موشک مستقیم خورد به خونه مجتبی
۲- مجتبی خودش هدف بوده
۳- زنش کشته شده!
اگه مجتبی هدف بوده و موشک خورده
به خونه، قطعا همون لحظه مجتبی کشته شده!
اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید
که دست اسرائیل (دست خدا) عیان شد
و خامنه‌ای جوان شد، ولی از قرار معلوم میخوان آروم آروم بگن که دست خدا، هر دو رو از زمین برداشت.
موشک خورده به خونه و زخمی شده  باشه :))</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6546" target="_blank">📅 15:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgbVc9Fc0Np0QQsXC9MD0xqmFoLMobGbYMJA0dAZ3xDy3ZdW3R_i-tJYkL0ChoobChC_kUSrX2YS1Vta4BmhpRJ8TNw-VDQahhKD0V5HlhfSBmFwjh2Tr9GHJ1ONZeRRvIzv32RvjtGCaxUlGe8wDaT3Xb18SoDKFVZ7TNj_e3J0BC7oJGh0wzTDUK5iaeTQAhsu1yoEWKy4ej5S53VCbgvN7GPpYsVjAq1H-rm2uK8Llh5-jsIkoqDflSEyDkGBYgvGVfN46kZBXqf7YY5W-6yZNTzokkS3a_AZxWHBbSwbDddegwRPTZz2dpeREGINCP2u3cDLtRw9piA38mB2lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شارلی ابدو
ایران - اینجا تمام سال
خورشید گرفتگی است.
(عمامه سیاه آخوند که مانع خورشیده
و کشت و کشتاری که پشت این عمامه سیاهه و روزگار خورشید گرفته ایران)</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6545" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6544">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏محسن رضایی دبیر شورای عالی امنیت ملی:
‏آمریکا باید جنگ را پایان دهد، پول‌های مسدود شده ایران را پرداخت کند و جنگ در سراسر منطقه، از جمله لبنان و غزه پایان یابد
‏-شروطی دیگر از طریق واسطه‌ها به آمریکایی‌ها منتقل شده
‏-تا زمانی که همه شرایط ایران برآورده نشود، تنگه هرمز بسته خواهد ماند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6544" target="_blank">📅 00:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=Rj_ZHNWTS_UCC_E0xCS-kBZTLn9gPgCbw_b8nFvGepRmZHvXimeEa18GpuXHW-er7JV7uq3GcecoLXnTB_KjLb0mfNVEhg9XAVRqGumvnlfXVpTjkiftmBE9VlWBXqlbutmsPkDveuAN7l9wk1sZrv51Fg46341eX5kUrbCUf2J8adu5GSlXVm2oKkFs4tTLnk4EI2Yv5DPx8RQnhNdI3mM2PcKblx7rtz4YWi8zM2suUsfvoOxM589nrE7serw_j7fV7NLJfi0ehyHiQbYE4c8japK15UgUd1h9uaO3pAx1-TuUKM86xwFFDnVAS2EsOlfS919l45JdTAWdDq6rXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=Rj_ZHNWTS_UCC_E0xCS-kBZTLn9gPgCbw_b8nFvGepRmZHvXimeEa18GpuXHW-er7JV7uq3GcecoLXnTB_KjLb0mfNVEhg9XAVRqGumvnlfXVpTjkiftmBE9VlWBXqlbutmsPkDveuAN7l9wk1sZrv51Fg46341eX5kUrbCUf2J8adu5GSlXVm2oKkFs4tTLnk4EI2Yv5DPx8RQnhNdI3mM2PcKblx7rtz4YWi8zM2suUsfvoOxM589nrE7serw_j7fV7NLJfi0ehyHiQbYE4c8japK15UgUd1h9uaO3pAx1-TuUKM86xwFFDnVAS2EsOlfS919l45JdTAWdDq6rXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.
جلوی دوربین‌ها وارد هواپیما شد،
اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!
نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6543" target="_blank">📅 10:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31726f423.mp4?token=r-9ZRve3lve1HaS5LPOMtlXlE-lZQqgyE1oAaxkWhZh47tSXhit7fICJ4o2yfompdsEWyICD2khWdLj0q2E5ag_6m7vHxyogty6P16lmXIlbTuRhv2xcziuaQaIeajtE9_queXmjlhw0P0HCRwLHlZAHsVsH1zzqlp8h1irNfcn58K20T-_rTkcrYQNHtXCF1bWLFd-JQqeUSTHh2E9BSBndtUxO5AajoDBhtfGVKurrGN5u3Db8-SVCM-2OkycVvBoEhVCs7-MmSL-DrMe_wQmi_4HU9x1EepsqHp2WQ5SSHnV2iPy4r7_kpfsy8gKKQ5Ab20n-nL8abiDgS6-QTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31726f423.mp4?token=r-9ZRve3lve1HaS5LPOMtlXlE-lZQqgyE1oAaxkWhZh47tSXhit7fICJ4o2yfompdsEWyICD2khWdLj0q2E5ag_6m7vHxyogty6P16lmXIlbTuRhv2xcziuaQaIeajtE9_queXmjlhw0P0HCRwLHlZAHsVsH1zzqlp8h1irNfcn58K20T-_rTkcrYQNHtXCF1bWLFd-JQqeUSTHh2E9BSBndtUxO5AajoDBhtfGVKurrGN5u3Db8-SVCM-2OkycVvBoEhVCs7-MmSL-DrMe_wQmi_4HU9x1EepsqHp2WQ5SSHnV2iPy4r7_kpfsy8gKKQ5Ab20n-nL8abiDgS6-QTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون (نیروی شبه نظامی تحت کنترل سپاه ) در تجمع افغانستانی‌ها در ایران ؛
هر کسی گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6542" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت: ‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.  ‏</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6541" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZwUFBqKug3n7YtOH26QEMUV7mZwyrPfvm7qZteSRuNLqk3CbDIfJmiW4uTIuX3LRByaIz-1W06_wKwYLG4yRcjle3RFzwOy9R7mIW0A-eAQJRqMmovIeR6pkD9LUQltlsRu9O0lzd-EPzNEOY5lF3a1EDGejxp4q3MLkvHPluchdvwt2tw_PUsHtLDYjU-0KIlRpU-mlWZAleTG8gD6MgWeLOWH1M4i8znV5ij0I23WK6Mq9tta1hQGy1kGGXow3gA9l30WGHt61aBTaELq1yRS_sDWgQhBYNAQ3vKBspU9Eak21O0CZPWMH0LwUYiHYpcE5Fj1JcvKTFZVmW9RFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت:
‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
‏</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6540" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6539">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tx0_B-LgjUePgdSmuZQE34bJauR_gHonjxdBLT2IsTrcW96F8niSFZDFFbg_j6mUJS7vcU27ifqufmltyxGQ-GNiMhBQu8e_lyyDyuhjuJjPEJkKtOexCgTWBc-L-aQWi8O_Jw6JVwKaM0MugNqUTsLrpQGUX4WT6yGeHBQd_sRa9MSrFTwQ6MSVW8eeKv2xIPE_35TSTWA6Knz8FJWhWLUIZUFZnYAujC8_pnwgAku-nBXM8AqI6aTnUWeqStCduNfn5he6Dt0uS3umSZhw7aBc-xRYNfA1tyBcSZBRRT9nT9zowhk8CDZgOxZWr5WGdc8isS2rcuJPhEOzk8WOjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجتبی خامنه‌ای با صدور احکامی جداگانه، شش تن از فرماندهان و مدیران عالی‌رتبه ستاد کل نیروهای مسلح، سپاه پاسداران و سازمان بسیج را منصوب کرد.
بر اساس این احکام، سرلشکر علی عبداللهی پس از کشته شدن سپهبد عبدالرحیم موسوی به ریاست ستاد کل نیروهای مسلح منصوب شد و سرتیپ کیومرث حیدری جانشینی او را بر عهده گرفت. در حکم انتصاب عبداللهی، بر ارتقای آمادگی‌های دفاعی و ادغام ستاد کل با قرارگاه مرکزی خاتم‌الانبیاء تاکید شده است.
همچنین احمد وحیدی با ارتقا به درجه سرلشکری به‌عنوان فرمانده کل سپاه پاسداران و سرلشکر مصطفی ایزدی به سمت جانشین فرمانده کل سپاه منصوب شدند. در بخش دیگری از این احکام، دریادار علی عظمایی به فرماندهی نیروی دریایی سپاه رسید.
در نهایت، حسین طائب نیز پس از کشته شدن غلامرضا سلیمانی، به ریاست سازمان بسیج مستضعفین منصوب شد. «گسترش فرهنگ بسیج، تقویت شبکه اطلاعات مردمی و مقابله با تهدیدات نوین» از مهم‌ترین ماموریت‌های محوله به طائب اعلام شده است.
@indypersian</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6539" target="_blank">📅 20:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6538">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJlm8v6McGjsnILLI6VK3OMk1HDac3h5Lx0U9qBAWlt2wd2y2CAcw5RXuQCP9H2mXTMM2yBwxFWayu0pt1C-xVwGVOCreZ5_e_hxZ7jkJzKXVbXwn_HDyZRiMB9ocrPkpCS0JaVZrZiX8qaGeE_co1X9bjkeEzxv05__PAbtDy-Zc28ShkCqXSfelhImR_GtpsQtAzT45W9XqVvvJd5mZlvggTfQVzCCoXyBA1UgrNkWG5hB-E41oPuPdBj4Oo1FNqZN7R7MGEu0ugIrqV__xNx3_c6z_qhLfFX6pRuvsa4aoHKgY0RTGkn_OE7flVWZ9P7tr51PdJ7eo1SBvtSS2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
اصلی‌ترین دروازه وارداتی کشور</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6538" target="_blank">📅 12:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
شرکت ملی نفت ابوظبی از حمله موشکی به یکی از شناورهایش در تنگه هرمز خبر داد.</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/farahmand_alipour/6535" target="_blank">📅 15:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=k7luD98LODrzz0aWzASMWJFAt9ihZb14quIWCsggcpf12Hp9yNbd7bdctJMxidO0RI8IkyxVDCltgmESZt1EjDQtKlR8n7UgoGgPNQ294Gnb1fjifJn9Ut8N-I8DVqZmqlkSQZLD0PHpUaQF4nF7p8crvGS4lFCax6rQnngaymNBMQnVVEU3Zevf9HB0tRYlFztVD9YEMieAsF4H4F6mwrUEuTZSE9p99bXMA32Y0Emo5UBTzps_wT9-h4RL7-dmDIB3GMR1xjSztv6VxWq_qBrTH2yKlohYrX0l8LswT3xAXBXr2xkxL_qwHjdpWHJ3FHcCfwWCH2zcqDfiMpMc4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=k7luD98LODrzz0aWzASMWJFAt9ihZb14quIWCsggcpf12Hp9yNbd7bdctJMxidO0RI8IkyxVDCltgmESZt1EjDQtKlR8n7UgoGgPNQ294Gnb1fjifJn9Ut8N-I8DVqZmqlkSQZLD0PHpUaQF4nF7p8crvGS4lFCax6rQnngaymNBMQnVVEU3Zevf9HB0tRYlFztVD9YEMieAsF4H4F6mwrUEuTZSE9p99bXMA32Y0Emo5UBTzps_wT9-h4RL7-dmDIB3GMR1xjSztv6VxWq_qBrTH2yKlohYrX0l8LswT3xAXBXr2xkxL_qwHjdpWHJ3FHcCfwWCH2zcqDfiMpMc4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل کوثری :
‏سردار کوثری: شمخانی برای جلسه فرماندهان در بیت بسیار اصرار کرد
‏سردار رادان جلسه را نیامد و سردار پاکپور هم نمی‌خواست جلسه را بیاید اما دستور شمخانی برای حضور بود؛
‏وزیر دفاع با معاونینش در جلسه حاضر شد؛</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/farahmand_alipour/6534" target="_blank">📅 10:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=LWadce1fIwQ2wDHjtnvmUN6OIZNfuk6Fc6-jkvv6JAgVGKZgkVmFiKewQl-PdW8AXfCEyzDB8AXNoNxRxrWKsXVmbFTpSC9lQN3yPrPI3s0Ftt5muTxzMCM9aUE-lGrZ0_4A7yEU_Hde_AFPsDXZN1hCWy9dRcrLBuJbGgeKCphWmUFeNyW2h39HN94BNSqxOwzezjvvReAMdFE9YVmrHujKEFx3RqDYo-pu29gKawzTnxzm0cecyJx8XwrcyWeK-xsHF0b64D-OLBKgbaiDDsVkhm5N0xdL7Qov0JQ2hAPjc0h-dq_yj7KifvezVOiqOH3HGEqGGT5S108G6gd-kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=LWadce1fIwQ2wDHjtnvmUN6OIZNfuk6Fc6-jkvv6JAgVGKZgkVmFiKewQl-PdW8AXfCEyzDB8AXNoNxRxrWKsXVmbFTpSC9lQN3yPrPI3s0Ftt5muTxzMCM9aUE-lGrZ0_4A7yEU_Hde_AFPsDXZN1hCWy9dRcrLBuJbGgeKCphWmUFeNyW2h39HN94BNSqxOwzezjvvReAMdFE9YVmrHujKEFx3RqDYo-pu29gKawzTnxzm0cecyJx8XwrcyWeK-xsHF0b64D-OLBKgbaiDDsVkhm5N0xdL7Qov0JQ2hAPjc0h-dq_yj7KifvezVOiqOH3HGEqGGT5S108G6gd-kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی‌دلیگانی؛ نماینده مجلس:
ما الان جز ۴ ابرقدرت جهانیم. نمیگم چهارمیم؛ شاید حتی دوم‌ باشیم ولی دیگه جز ۴ تاییم و باید توی شورای امنیت حق وتو داشته باشیم!</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/farahmand_alipour/6533" target="_blank">📅 18:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6532">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUWGikyGAapoyy6BZGvVgDOLS0DlfQp5Tjyy8iG0Fjflo8G6y7mvlFlvBWLXzxWoS9bqueEZClkkMB1tSjH-KnwOALeBBUQ4YuO9FSf5dJO4RWxZIn_2fgCA3S1DpGbGwYnHmaGyGxRCbcrYTBFvXPIDSbGbfhsNy4anUnesNpcEcf28GSKtQav73R6a1WuHQJgD-3ZkDnQR2-AdOrig1KjG1v_JpJqCGqZHAv5fiTfIqwC1kF1MPWkKJvgmnJpLunnx72aN7604hJycXyy74t6XFJADOFltzWlBTuLhE9ul7WiBKksbXU0wbs5rKyd2Jz-WhxOVPD8FD1I4MJWTIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از ریشه‌ها هم به این جریان برمیگرده  که پیامبر اسلام از نسل اسماعیله  و یهودیان جملگی از نسل اسحاق!  تمام پیامبران خدا،  یعقوب، یوسف، موسی، هارون، داوود،  سلیمان، عیسی، ایوب، یونس، دانیال،  ذکریا، یحیی و …… همه و همگی از نسل اسحاق هستند! پسر برگزیده…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6532" target="_blank">📅 15:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6531">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3WUMvJ8inyFD6QL94bhyx0ttaCbNZ9yLmlobLopAvNEEH2YahPrwaT624b4qzb0bDVslYdEevqAAQ1icdUxUX8KWOdwnff6kC9SsK0Rf0QksXO-fW6y47NBU9Jc2FaD0jTre10MGT0_tDaovZcUvAi-3OadEyTEs-lBnCMTQE-yNJmLHBGSDmLNOqYwrLZ7QAjoUOzNtQkt2L8n8TnBWPbS30Lg1PUD51X1vxR4WVsb-15ChmPrUEyRKJkKcbCMvhvLsGJ-H5p_XnuzELQ1xfygeiBx9SwIiEJhEZKm3C5wZsFTbm6WshTmhiQDAIKn9QSWL4D3czemb04uZDNFdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم در این آیه ۵ سوره قصص، هم در آیه ۱۳۷ سوره اعراف، هر دوبار  قرآن میگه که ما یهودیان و بنی‌اسرائیل رو تسلط دادیم و حاکم کردیم!  . «و آن قومی را که پیوسته به ضعف کشانده می‌شدند، [بنی‌اسرائیل] را وارث مشرق‌ها و مغرب‌های آن سرزمینی کردیم که در آن برکت نهاده…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6531" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6530">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">و شاید خیلی براتون جالب باشه که این آیه قرآن  (آیه ۵ سوره قصاص)  که خامنه‌ای برای  خودش  تفسیرش کرد،  در واقع قرآن داره درباره قوم یهود صحبت میکنه!  درباره بنی‌اسرائیل صحبت میکنه!  اینکه اونها رو از ضعف و بردگی در مصر به قدرت رسوند ! و اونها رو تبدیل  به حاکمان…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6530" target="_blank">📅 14:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6529">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4qy_34Bp2imS5JLBiIABleo-S7V7pUs8f3JZeDDbpHKwC7CXXILHZrQ7JGtUc-yDZ7rA2saJddYB2_Nml2t45uG5vtYqAnDogxhEqO3RJ-V4hJilVzU7kkIJq5uy34SGSvyuyIoKPuubtdhes_-58xiNSL8wVsC9cpASbR-Pg93kUd7ISBJiDazq6SGPNkx13azARrNXSe3-jpeh8o_AkxY4CxT_EgZIdaeDQQLeZUlMhTaq2KMquUnKJ_I2gw7S_AigzOnK9vAsalA3zz4bHMAXUmHZyj8fncApI2FgoRyD26Tuu1y_zNWwUsWGgVHbfgUhelcFcLJRe65gs372g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای در سال ۹۸  معنای «مستضعفین» رو هم تغییر داد و مفهومش رو از مردم مستضعف و مورد ظلم واقع شده رو تبدیل به معنای «پشوا و رهبر کشور» تبدیل کرد!  به نوعی گفت «مستضعف» من هستم و اگه میخواید خدمتی به مستضعفین کنید  به من و پسرهام خدمت کنید!  کفت قرآن اینطور…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6529" target="_blank">📅 14:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6528">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y75hywGxE38vOzvm8C4CYvovhMR7Wi7aV-rCo2pFVAe48u6-1RpJ0zMm7A7y1bAvl_J2ydBCIYWKMsxmfjCNrjucztRoDjzsCumpAbJP8jBlMHUqOBjwxOf1OhcdEjSvNf3dqlN6OXt6LeHdizk36qg63byE55qIeImE9HUocx1556ceww9DR82UYNeTPZGlL-bXsM0aFiEL-keAnQW57hL_jWn7YqXr0uJ3jwh8bba8U1M41anE24ennCDnDZysIHFbl_abSk-Fh8Fga1KqZDcYWqMJAd8gKuqepIdZ3tcxpz8lHsGC0-s-TnCOIR4ivblXTxLavSR3MbXvT9K18A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان وقیح جمهوری اسلامی هم به مردم عاصی ایران از فقر و فلاکت کشور  دائم میگن :  شماها بیایید زیر پر و بال فقرای کشور  رو بگیرید، مدرسه و درمانگاه و….. بسازید،  به کودکان یتیم و سالمندان و….. برسید،  تا ما هم بخشی از ثروت‌های ایران رو یا خرج لبنان و فلسطین…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6528" target="_blank">📅 14:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXS4gptu-8pLcGQBFwKppgyy2-Zsa9M5mXnryn4bOBA1QDH6ylNCWj7C9vv1nhwfKWqw7DG2EKe6zR74jnYHYL7VZ50V64L7P_BGAHt49VjRd8M5zW02ObRGn7uKFu_f15orywTHIcwQcQ5PeJD4N9KqdYlnCGTNkw5A2yRc0e-SKa4vD8EpkgAXkpuhJU6xVux-1n6ZXVtNWEkAJnpdba9l3sHFYJppMVV69akY-G2azEKJN45Hm8t5aQdKdizRLrs7y79g12vSPUvxg3ShToveOHtnfSp30Wz0gd-EGXPXYE-S5YCx1gEgrprKPv24hFLeTnKJ45HfjnSip0GoVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلاس‌های ۳-۴ میلیارد دلاری!  خودشون  که هر سال یکی از اونها افشا میشه  به کنار!  بیش از ۳۰ میلیارد دلار هم در سرزمین سوریه ریختند و شکستی مفتضحانه هم خوردند و اومدن بیرون!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6527" target="_blank">📅 14:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mrTbaej-1YR1X45XvWFJLzJMx6vk2JENeWqyf5LOYoueYo3aYu7xTKMKZznI78XmVV8wugn_2R6Q_Qgh1y7-bJbxhowPl8MpdyJYdN6RrpilC0jF3rt8FgDjzXfC84oWSq4MIg6QENjEx8-XbkibQYTevNrStdb9-GrAHgz5eg9FOgRN6JW2o7kEfbO7QGAuGrWolG6W5iWkucHk0oRgZLj47L7VQn_CmsXhw4--mKHhBgS-y2rzg2b1oNWWXzKGk3SRTghC5UAq8tmx2ELHpb-lndB1uZCKoLlFEAAfE2GIpFl20e8Z210STzZRhSBuCSamOxZeFuy3ggH8PrbkDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r0Q6WMJTKqHx9RVajQSM4-DSIUY_ciFK6zp5ZaB5jwd95_MRKK4kZFkrPoWCMx1UK5y_bkkcVwdMUJGgl7mLMInpk_33vXkTZcadzMydNHJIfr2FeN9Mny-5g_iHXA_ZIsUU6SVXs0GcNO330PCwSUYKJTFdSO6BdZEQDpjuYDJ5-SLLqRTfE0OCXVCTMJ5iZ-1RK2MrQb433i3MXr0QX_FbgYRhK231oHfFS8b0rsUq8ekhrpcM9ROZLRJZyg2ffCQADZYTT96deTUhCJYutOcEqcfvTS30y-4QbFAEMXCnJl9dOPhcgDCiw5k4xvuG2eJm0_StuRx26Evl7_8Ezg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tZ3G8eUOi_4F0ihNSUudRqv29OveODMmcQrrbE9ToDAB0vY3wgb6nH3JT6dkNM_yE78Gs4AfmmesVOoNTm3Udpr-E7ntKTMu5tlro_TEiyrj2dIODnJIPb2PJTlyM2PkbpITVIxvaLSgvvgPhMbWsdV2wdCUGeNWKRmrMM_-a2cbaGfNkMkigWhOEBUgGAiDXcxD5NLN8400di9CMnNyvOOfRURv9Ei3qhDUkjgnnfb9q-cS4OxoF2AYMNlYoF4x9yVJTjWyaBiShxaXePuBUUdJU18PL8pkykyw8x6kmKJHKaTifWz1kMHIt_vyGlfUCDLlfSb4QN1NhylbZEHRfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیرین مدرسه ساز در ایران،  ۶۲٪ از مسئولیت ساخت و ساز مدرسه  رو به عهده گرفتند. حدود هزار مدرسه.  فرض بگیریم همه اینها مدارس ۶ کلاسه هستند (برخی ها فقط ۲ کلاسه هستند)  اگه هر مدرسه ۶ کلاسه حدود ۱۲ میلیارد تومن هزینه داشته باشه، هزار تا از این مدرسه‌ها میشه…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6524" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
