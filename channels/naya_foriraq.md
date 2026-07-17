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
<img src="https://cdn4.telesco.pe/file/FKHlvjEDVU9q_fLGcjHvfUGNv90uwNr6RfMxM3Q46hT6ZoQq3ofAdA_kX23C_fGzPnIaxR57Ov-Kw-vaZnNQxtr5bd92n2QNUvx6E3kG6bkPhx1mMnlXLj1zUoXJiK9fPUjr_hdqVP4WYAGI7hUokHnDZzvQGzY2lai8gijiJlwIgsXIJBu7o0kMr3jaZh1XAj4TWrgBeOy8CBAGKnXpQKxRx0N850HO5YEcjktrpkwZ9yrZh4lWRDzj1L1nFE8xR3F2f9ZHQUjwplRMlS3PZV1hn-TfeHc2FzsKJBcDc4aVou2a26ct-y5iH0PE2fzyXlER9v5vnuEahbUdgPsvZA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 264K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 04:27:25</div>
<hr>

<div class="tg-post" id="msg-83506">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">انفجارات في قطر</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/naya_foriraq/83506" target="_blank">📅 04:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83505">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/948f6e6b08.mp4?token=mjKXLw0Fr5cDxuUrEvJtbXfQLdjClG9YZ3p0pEczQACmsXTudsAQ7if-thq0h1LRd4pfpawlU9IgTBoDa0I_OHsXnHxBWBQTDSlwH_iyGyeZapSJ0BNLtJD09CZraxHftlQVVb1DYdPFRGpPUnkWuuu7KdTX3IqridrbJgF8eDjw1l0-UaY46H1pcQzz56XgJAA12uNLsgSaJLpueTiIpTeEOc6VBGSByYHNbFAqAe9M-3Bvp_i1Y-uL0yuwxC_7VO4yxyGjMlXP0RJl3Ur8xF8s2RbGZHZPrCfCnRo4FA1z0ybuLsTYwSRoA64cbIXF_w73tMRUdr9_1_2nmpuOrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/948f6e6b08.mp4?token=mjKXLw0Fr5cDxuUrEvJtbXfQLdjClG9YZ3p0pEczQACmsXTudsAQ7if-thq0h1LRd4pfpawlU9IgTBoDa0I_OHsXnHxBWBQTDSlwH_iyGyeZapSJ0BNLtJD09CZraxHftlQVVb1DYdPFRGpPUnkWuuu7KdTX3IqridrbJgF8eDjw1l0-UaY46H1pcQzz56XgJAA12uNLsgSaJLpueTiIpTeEOc6VBGSByYHNbFAqAe9M-3Bvp_i1Y-uL0yuwxC_7VO4yxyGjMlXP0RJl3Ur8xF8s2RbGZHZPrCfCnRo4FA1z0ybuLsTYwSRoA64cbIXF_w73tMRUdr9_1_2nmpuOrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في قطر</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/naya_foriraq/83505" target="_blank">📅 04:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83504">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECu0FcFuqwreFyhjrO32oa-RYL_WRC2tQD__zDu3hUHS4YFQL9Fi_mTT8RydILo4rH9VJW6GnDkgTLedAdwWjZojz8vG3U7u5xDx64577cvY97ubLPZMMvXH36V9iH-agyIMzKccyf_1aWBjje45iI7eUjPdel85q8ZYuXPomEbmZsuKsIEF0Yjwo9cs6REEbIE9LI8GuQvsvMa193m9DtXGM_Ue-WGPsSYoVmOL7UiqAlm1ZZ0LVaESoFjTxgwfrkaA3agbmgnXpvk6JWwurJhaQrJTIH3XxqzN8sYk8F9Y9IR7LyrQwOuNsdr6Z4eYyRFJ5zLqX8Ycz3h8kOdIhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أبناء مدينة أم قصر يرصدون النيران المشتعلة في المعدات العسكرية ومنصات الصواريخ المتنقلة الأمريكية على الأراضي الكويتية بعد دكها بالصواريخ والمسيرات الإيرانية</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/naya_foriraq/83504" target="_blank">📅 04:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83503">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzZkGJmCQ3JljCAQpUTaYLziJ14UMY6NKUOQ0XdSJ1LY9inypkYgtPgZaSDClN4nU-Q-JVhqDpQ6HK20RQZwYdR52tojCL_9xRAU7b3iUyWxDu2vrdaVD-9JD9MDZ2hNFCPB8KcA84jULbE3WyHG1nRLn9PwVdNc7dltOoVXNktC21C8SS_bM8_6WLp7EAX8izOmUAilYn77j-zi8ecVK1IBAeBY2cdpSDY8gTyBua1qDS5Z_C5VvQsR1EBi08O0fQD_FKDzutBBKY3EStf79BFa-IMSYnJ6rodUClYlYN9hbVv36ewWXxVh1XsiaU9oHRQ7WXNuymzyJOwy-0-dng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات في قطر</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/naya_foriraq/83503" target="_blank">📅 04:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83502">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">إستشهاد 2 وإصابة 4 مدنيين جراء العدوان على أحد الجسور في بندرعباس كحصيلة أولية.</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/naya_foriraq/83502" target="_blank">📅 04:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83501">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انفجارات في قطر</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/naya_foriraq/83501" target="_blank">📅 04:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83500">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">انفجارات في قطر</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/naya_foriraq/83500" target="_blank">📅 04:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83499">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">انفجارات في قطر</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/naya_foriraq/83499" target="_blank">📅 04:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83498">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">انفجارات في قطر</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/naya_foriraq/83498" target="_blank">📅 03:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83497">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvrZUsp-FX_XANbd36lNjvmTU5YzY_OMzAYhoFj92fuZeTe7Q0aIHXAqb8IrUCm2Wrq8BBp7eus0V0rD3ezx_7wewHf-9DdAatpbXDeJkyr1Bk5faZLHoS_mIc4zGAoD_tDegnU6P99KXlO5t6coN4Ia1AcyMf6a-15tycq-un7lEVQdZR20oKWXcJuNNGOzMWND4vx9mkug6SHu0l8dfHAtTQkXqGXGOxxwjDCFaRM5hdj44aTtp0i2ll_PFuR9UhGqwYU6mGKQGOAGdDaX8DHEjjKIelkIXIgPDd-kqhAV20MTHq6V8KZb8qFeFo8xc8Yfhv72FPXla9VzAGDH5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد متداولة من المعارك الصاروخية بين الصورايخ الإيرانية ومنظومة الباتريوت الأمريكية في سماء البحرين.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/83497" target="_blank">📅 03:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83496">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8105b22245.mp4?token=tfJVW9AtPW8In2nQRS_FOj3OyDzOVzem7aSkdyDyo3W65AzEwF3krqitWJnZg2KF-39DNnUaN6kufVeu8K2hEw3DZjf24uVVOPBOxwtjmU6LbQUy2qN3_gE8KYGfUVWD3qH_fNFRYkwAIUm_pJQXtAHt0x1Sssv0oIim7yVdwCCnPw1PgFIjhvZCvEwF-6-zf50S76ioclsHSBp8shrwmk2-S60Ovs2qxgmZuy2-H2TJxXbKEzAaeMAyADHMx7a0k4S8dehJjLiqmbD25h7Z3QRktUiDjvkO8huU3YbtzIwet-9gl66eTStwAOTj4QQ6B2PY0H-0Zhssj1brhxor2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8105b22245.mp4?token=tfJVW9AtPW8In2nQRS_FOj3OyDzOVzem7aSkdyDyo3W65AzEwF3krqitWJnZg2KF-39DNnUaN6kufVeu8K2hEw3DZjf24uVVOPBOxwtjmU6LbQUy2qN3_gE8KYGfUVWD3qH_fNFRYkwAIUm_pJQXtAHt0x1Sssv0oIim7yVdwCCnPw1PgFIjhvZCvEwF-6-zf50S76ioclsHSBp8shrwmk2-S60Ovs2qxgmZuy2-H2TJxXbKEzAaeMAyADHMx7a0k4S8dehJjLiqmbD25h7Z3QRktUiDjvkO8huU3YbtzIwet-9gl66eTStwAOTj4QQ6B2PY0H-0Zhssj1brhxor2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجة جديدة تنطلق من إيران</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/naya_foriraq/83496" target="_blank">📅 03:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83495">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مشاهد متداولة من المعارك الصاروخية بين الصورايخ الإيرانية ومنظومة الباتريوت الأمريكية في سماء البحرين.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/83495" target="_blank">📅 03:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83494">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9786e5193e.mp4?token=V-azAZ250_zJf74iIcSdc3PXw7KrJ6uvT6-ekHdrBUhBh6JNxva7SbFSuchZkkxV3a0MHnCX1WHZ92K16RO51XhtUNS82TeroDspN4H9Jooe0LB5WWZ1ybZVjqEDrJ1hU50Zsp4160uQ9DLxGwOjJQUZOgY_HZE6VTu4hjPrR5i6Qjcngze4dUuNMItEn9JiX-Y9nMbJyxKqGB0dNjOfyHpcqEFymatEfgaxmqWRGE_6pXdO6bfQBCgpcskofHMLvLGjFPksm_fTRdmqxOPntXpJU2U2AGXiB9hdhxV4XUWJslQOJWUdBRdx-COTevyGaY5qfvF7Z0j85ecVZkSozg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9786e5193e.mp4?token=V-azAZ250_zJf74iIcSdc3PXw7KrJ6uvT6-ekHdrBUhBh6JNxva7SbFSuchZkkxV3a0MHnCX1WHZ92K16RO51XhtUNS82TeroDspN4H9Jooe0LB5WWZ1ybZVjqEDrJ1hU50Zsp4160uQ9DLxGwOjJQUZOgY_HZE6VTu4hjPrR5i6Qjcngze4dUuNMItEn9JiX-Y9nMbJyxKqGB0dNjOfyHpcqEFymatEfgaxmqWRGE_6pXdO6bfQBCgpcskofHMLvLGjFPksm_fTRdmqxOPntXpJU2U2AGXiB9hdhxV4XUWJslQOJWUdBRdx-COTevyGaY5qfvF7Z0j85ecVZkSozg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صواريخ أخرى تنطلق من إيران صوب القواعد الأمريكية في المنطقة</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/83494" target="_blank">📅 03:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83493">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d6c9dca2e.mp4?token=ozPTQGnCfgTbPgTIeZhbl1FpnV7tnfz6XIhoVLf3CTyPAaAGrmlMUHfl6b18oQYNf_HmIQxRqgGN0STf5b18YThyd1-Jgu3ViPoihtbPzkWYj7qmVPmx4M0ENsCUMrHv2slTldwPzFREnqBAWG-F5WC41eARaa9R0tRzHdJx_j3F2D5wTAih6PG2x9GRYE2ni28w8xZ4ayEn_ApE_ujPFe9yw7j9XNzOrKpdmLt9WOqBL2j2Og3D5COj21sMqxTT_oL0VSrlhXgjA1W7FhHGWKU9cmWP4s0XJlUmpmcR60XPdr-bYzMpZqAEAQ8jNUudqSvA0f8QPPi0mmUOsapPeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d6c9dca2e.mp4?token=ozPTQGnCfgTbPgTIeZhbl1FpnV7tnfz6XIhoVLf3CTyPAaAGrmlMUHfl6b18oQYNf_HmIQxRqgGN0STf5b18YThyd1-Jgu3ViPoihtbPzkWYj7qmVPmx4M0ENsCUMrHv2slTldwPzFREnqBAWG-F5WC41eARaa9R0tRzHdJx_j3F2D5wTAih6PG2x9GRYE2ni28w8xZ4ayEn_ApE_ujPFe9yw7j9XNzOrKpdmLt9WOqBL2j2Og3D5COj21sMqxTT_oL0VSrlhXgjA1W7FhHGWKU9cmWP4s0XJlUmpmcR60XPdr-bYzMpZqAEAQ8jNUudqSvA0f8QPPi0mmUOsapPeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجة جديدة تنطلق من إيران</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/83493" target="_blank">📅 03:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83492">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de24f0dac0.mp4?token=d6D6JCbbbBn0oUS9WPwjPTwDnE6Gd1Xr0OyDVfmuNl3mQ30uObNhytaFGRj4MrTqx7gW-e_qe7i6ItdWt9jJHX3GX6o5HMjpMAtfZnnkc3fvUGf0F7ncIbnL4bpRQB8YOKcjd3pCGt8odA-hb7cYLNdQ7JLg3BiV8uBsq_QGI3_2iWO5G3JJCEnSkcC8LX2CFET4P8F2daGrCjqmqhgVIG7GBy8d6DKpJMXbAzVFvWT0e_mJv9FqCKay3h_byAwo5qodNXhfZM_kAreu_9REu_Xy1Rvyz_EHrqbK503HcA7t5MzQKsVdxKzOW_8XOepQRVA27u_bjYd85hyH49XMqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de24f0dac0.mp4?token=d6D6JCbbbBn0oUS9WPwjPTwDnE6Gd1Xr0OyDVfmuNl3mQ30uObNhytaFGRj4MrTqx7gW-e_qe7i6ItdWt9jJHX3GX6o5HMjpMAtfZnnkc3fvUGf0F7ncIbnL4bpRQB8YOKcjd3pCGt8odA-hb7cYLNdQ7JLg3BiV8uBsq_QGI3_2iWO5G3JJCEnSkcC8LX2CFET4P8F2daGrCjqmqhgVIG7GBy8d6DKpJMXbAzVFvWT0e_mJv9FqCKay3h_byAwo5qodNXhfZM_kAreu_9REu_Xy1Rvyz_EHrqbK503HcA7t5MzQKsVdxKzOW_8XOepQRVA27u_bjYd85hyH49XMqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة بمنطقة الجهراء في الكويت</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/83492" target="_blank">📅 03:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83491">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15c20eb661.mp4?token=pR0H4pHdFl7t_AbcEFJ2yGOciyRJTp4-slenfMjl18KW5CjxfWhb3BLpNtae7NqC4tUa4OB4plrX1U_1SbRqQxCXOUaSmzS3kJYXpweZ-JcIJgRrveJKIgXIO_sxrN_S_Z1pHYXJ1dQePLaQvtuJKG1TD0wkNPhCcbZslhUM5CsNgkdlK2637WyaNtekkJVj9FoCYq3nwAvTmdLzdda-s6RMwOqTAsdyJlhpTrYB7r7AFibXyE6P7vQ8fK2VDK2sdv7Ml7yLULmILm8BI6Ky_AbcoEmcUcSYI0MxlNp4c8Iho1mjfL886K8sJl3nDYtqV9Pm2QzridqjqnX0rbs0Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15c20eb661.mp4?token=pR0H4pHdFl7t_AbcEFJ2yGOciyRJTp4-slenfMjl18KW5CjxfWhb3BLpNtae7NqC4tUa4OB4plrX1U_1SbRqQxCXOUaSmzS3kJYXpweZ-JcIJgRrveJKIgXIO_sxrN_S_Z1pHYXJ1dQePLaQvtuJKG1TD0wkNPhCcbZslhUM5CsNgkdlK2637WyaNtekkJVj9FoCYq3nwAvTmdLzdda-s6RMwOqTAsdyJlhpTrYB7r7AFibXyE6P7vQ8fK2VDK2sdv7Ml7yLULmILm8BI6Ky_AbcoEmcUcSYI0MxlNp4c8Iho1mjfL886K8sJl3nDYtqV9Pm2QzridqjqnX0rbs0Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏تحويل مسار الرحلات الجوية إلى البحرين</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/83491" target="_blank">📅 03:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83490">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5423809ebf.mp4?token=b0OIVO_6o0OVdr7VCz7ATVn6pRAZ11KNwpCnC3RzlTOwEvr8T3HShCWAvVXZr3Sz9Yt83aWqkT0wXwpWm_DDmZgm2Kf_bqK4jgxGqdxpieq_nN3Rw6SHnAAFzYoSKx6z3XUzPz0859pPCEpWEUQWzcUfxCpKKgj9JQHwnEhuXuVtF0AS4oUoCQb91pp1tyHDNstuU1I983sMhxcggP2tzdWo1TMimKpoewn8Eey187EXJEasnT1qbreoIhN4iniEA2kxZ02zuDZBmqqh_pFx_HzyjcfYXD7ZXqQaErMG8oBRIfHR6G_wYP3GzavgDbQ1s_VcC9W60tum913s9vthhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5423809ebf.mp4?token=b0OIVO_6o0OVdr7VCz7ATVn6pRAZ11KNwpCnC3RzlTOwEvr8T3HShCWAvVXZr3Sz9Yt83aWqkT0wXwpWm_DDmZgm2Kf_bqK4jgxGqdxpieq_nN3Rw6SHnAAFzYoSKx6z3XUzPz0859pPCEpWEUQWzcUfxCpKKgj9JQHwnEhuXuVtF0AS4oUoCQb91pp1tyHDNstuU1I983sMhxcggP2tzdWo1TMimKpoewn8Eey187EXJEasnT1qbreoIhN4iniEA2kxZ02zuDZBmqqh_pFx_HzyjcfYXD7ZXqQaErMG8oBRIfHR6G_wYP3GzavgDbQ1s_VcC9W60tum913s9vthhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏تحويل مسار الرحلات الجوية إلى البحرين</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/83490" target="_blank">📅 03:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83489">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">منظومة الباتريوت الأمريكية تحاول الاعتراض في سماء الكويت</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/83489" target="_blank">📅 03:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83488">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e21f06d5.mp4?token=bWLm9pN5LbscK8wdiFem-X-mxtiUCF7KNoJypV8GHlVczkU4D3Cv946o80Z2ySkaKVoCxoxS6KOecM5Qgj9U0y7cjhLHJcW3JGHMGj-d2h7n8sNgQZ16YaZisZI56a60WO4ItJ7OSskBNZAo-UwZQPC1goyROrb4qPNmVAIT-WC8iQWqmutWQtHverZKIV4b0ePZ7YMTuvwMFlmuiKsYbdOHgk25HUmZ2263Wm1V7SxyKIA5NwZfK3B1OpkXo-RI4aDFR47xRDdFlUZhVS5i2_sOTj43ACE6fl0429Iq44AJ9miHEhn8JwD1wFFp9rb7HukD9BbAatEFrRqLiziK7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e21f06d5.mp4?token=bWLm9pN5LbscK8wdiFem-X-mxtiUCF7KNoJypV8GHlVczkU4D3Cv946o80Z2ySkaKVoCxoxS6KOecM5Qgj9U0y7cjhLHJcW3JGHMGj-d2h7n8sNgQZ16YaZisZI56a60WO4ItJ7OSskBNZAo-UwZQPC1goyROrb4qPNmVAIT-WC8iQWqmutWQtHverZKIV4b0ePZ7YMTuvwMFlmuiKsYbdOHgk25HUmZ2263Wm1V7SxyKIA5NwZfK3B1OpkXo-RI4aDFR47xRDdFlUZhVS5i2_sOTj43ACE6fl0429Iq44AJ9miHEhn8JwD1wFFp9rb7HukD9BbAatEFrRqLiziK7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صافرات الانذار تدوي في الكويت</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/83488" target="_blank">📅 03:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83487">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏تحويل مسار الرحلات الجوية إلى البحرين</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/83487" target="_blank">📅 03:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83486">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/333b8f7dc7.mp4?token=Zi9JdAQUQP6rlMepKuZ9UernTPHia4vxnt31PIPB-5xX4Z7ff8XlP1JDNkXCZnI3-S4WVnqYo36lImYNLBIlijpHnT4-y4IJq6uvtsg1ernXOD-DN8P_V82_AMv9aT-wuAsRX_kveOSZLpz9dRtH-o8NBH2G8mSUobiRKiTu3FDZoZoLeYAl4-XSyrxyCspCIjchQpHRMhaL28A7Zth_cZfOJ97KATkWD5mdhiWpxS6U7FuCEED6--C6HAwEeGW9suHkL7sUwTYcjvwA_FFBZGlAOXFAoEaATfqNy2kcOyfQRyltA1SMiZARxkHZxU7CkGxC9pIoI5d8Wqe36vNz6YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/333b8f7dc7.mp4?token=Zi9JdAQUQP6rlMepKuZ9UernTPHia4vxnt31PIPB-5xX4Z7ff8XlP1JDNkXCZnI3-S4WVnqYo36lImYNLBIlijpHnT4-y4IJq6uvtsg1ernXOD-DN8P_V82_AMv9aT-wuAsRX_kveOSZLpz9dRtH-o8NBH2G8mSUobiRKiTu3FDZoZoLeYAl4-XSyrxyCspCIjchQpHRMhaL28A7Zth_cZfOJ97KATkWD5mdhiWpxS6U7FuCEED6--C6HAwEeGW9suHkL7sUwTYcjvwA_FFBZGlAOXFAoEaATfqNy2kcOyfQRyltA1SMiZARxkHZxU7CkGxC9pIoI5d8Wqe36vNz6YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة إطلاق الصواريخ من إيران نحو الكويت</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/83486" target="_blank">📅 03:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83485">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/83485" target="_blank">📅 02:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83484">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/83484" target="_blank">📅 02:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83483">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/931e975fb0.mp4?token=aLlOSIuXltshCTFVLXgxx8bXYlfCXcD-CSjg6vQZ4LRw4gdfX483nkHq551DSgXuJcchg75MuoPNsv5QVqv7YSdxZrl20glWEbAcRggANO2NZyh6SGTpP6WrTRakvlEKj5IhQNIXzb8or8e1G-eRzENA8DmRNQgJ_yBTUtMCrHMRv1KK0-vmyiwLxf1XISoVxkj9aW8YH8MmhweAoWL_rdWTL0H772C2XrBNQTb9-t_aT-TaIhbeem-Jb0EZ3pMmzjR6UH5v7Ie-WQKnyrqJHef56cQokdfJprcGRUlx2bRs9W0yjrgyRlb0cGSxHsPEj1xEPFMLd9ad0ppX4l1oyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/931e975fb0.mp4?token=aLlOSIuXltshCTFVLXgxx8bXYlfCXcD-CSjg6vQZ4LRw4gdfX483nkHq551DSgXuJcchg75MuoPNsv5QVqv7YSdxZrl20glWEbAcRggANO2NZyh6SGTpP6WrTRakvlEKj5IhQNIXzb8or8e1G-eRzENA8DmRNQgJ_yBTUtMCrHMRv1KK0-vmyiwLxf1XISoVxkj9aW8YH8MmhweAoWL_rdWTL0H772C2XrBNQTb9-t_aT-TaIhbeem-Jb0EZ3pMmzjR6UH5v7Ie-WQKnyrqJHef56cQokdfJprcGRUlx2bRs9W0yjrgyRlb0cGSxHsPEj1xEPFMLd9ad0ppX4l1oyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  رشقة صاروخية تنطلق من إيران</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/83483" target="_blank">📅 02:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83482">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">الصواريخ وصلت وانفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/83482" target="_blank">📅 02:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83481">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/83481" target="_blank">📅 02:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83480">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">الله أكبر  رشقة صاروخية تنطلق من إيران</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/83480" target="_blank">📅 02:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83479">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">الله أكبر
رشقة صاروخية تنطلق من إيران</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/83479" target="_blank">📅 02:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83478">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">إصابة مباشرة في قاعدة الجفير مقر الأسطول الخامس الأمريكي</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/83478" target="_blank">📅 02:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83477">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/83477" target="_blank">📅 02:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83476">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انفجارات في البحرين</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/83476" target="_blank">📅 02:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83475">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🌟
مسؤول أمريكي:
الضربات الأمريكية استهدفت عدة جسور في إيران يوم الخميس.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/83475" target="_blank">📅 02:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83474">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/795582ea80.mp4?token=c30H4p0IucsUzRVvsqWIxltIeNqpjAa3AQCLB1J2W-W61ZLVnN_FeWA5KI5BbfI6X_7gZKfMcTXsW7oPRqdfyA1ljB6MN8obKQqsAaCxsBOhF7e5_giT0R6DNUtdNvGBnVT_LigHWSVSfuB7bqxbZleVuhXxnSSoJdp1YGw094-PDPJPmIHrOOyafObs15fBfayPWtQlfKE1HOT4cIHMmF861RyxONa71dlhGBVneVoQd_5kLXLRlmRq4DJ-wahBSZpmY4nvp8Y9kvpOVnR-eeoImswoP8JCuUIrgUWCePpbU2oGXJM03gjcyCQNIh-8iLwPpU3Y8cCiPO0jtyhaAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/795582ea80.mp4?token=c30H4p0IucsUzRVvsqWIxltIeNqpjAa3AQCLB1J2W-W61ZLVnN_FeWA5KI5BbfI6X_7gZKfMcTXsW7oPRqdfyA1ljB6MN8obKQqsAaCxsBOhF7e5_giT0R6DNUtdNvGBnVT_LigHWSVSfuB7bqxbZleVuhXxnSSoJdp1YGw094-PDPJPmIHrOOyafObs15fBfayPWtQlfKE1HOT4cIHMmF861RyxONa71dlhGBVneVoQd_5kLXLRlmRq4DJ-wahBSZpmY4nvp8Y9kvpOVnR-eeoImswoP8JCuUIrgUWCePpbU2oGXJM03gjcyCQNIh-8iLwPpU3Y8cCiPO0jtyhaAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
في المرحلة الحادية عشرة من عملية "الصاعقة"، استهدف الطائرات المسيرة الهجومية التابعة للجيش الإيراني، قبل ساعات، مواقع تمركز طائرات الاستطلاع والمروحيات التابعة للجيش الأمريكي في البحرين، والتي تستخدمها الجماعات الإرهابية.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/83474" target="_blank">📅 02:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83473">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac4579531c.mp4?token=tAkyXqa9Xmr_uOT_GtcLBkfp7m3EGPXolXV-onu0LmF4H6MvD6ONYE6QSliVaOtotnm_G6q3cErtOj-gBU_-hx9EsAZCUQ6gURDEPSIyoGtKiTEtHXQHfepgHarySimxPMwxu4dHas4zGu1AIsOPsipIp3JK-ovv0cMZZy60pl1Kk_tcMWTT29PCGkQmH5Pzim-rjRm_VFpNKTX6AWQts1bJ2dCOsSgsYDFCGR2AbUQoCntZ-IJzcRpVOe5qrKt99phpKKjhQGQ6fZa1Jqz1qQkCS3YmESj3wR8vKnGs_i65A3dO-r1V6Gweodc5jY-cmakn-u9SPyhRBwkg2J66xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac4579531c.mp4?token=tAkyXqa9Xmr_uOT_GtcLBkfp7m3EGPXolXV-onu0LmF4H6MvD6ONYE6QSliVaOtotnm_G6q3cErtOj-gBU_-hx9EsAZCUQ6gURDEPSIyoGtKiTEtHXQHfepgHarySimxPMwxu4dHas4zGu1AIsOPsipIp3JK-ovv0cMZZy60pl1Kk_tcMWTT29PCGkQmH5Pzim-rjRm_VFpNKTX6AWQts1bJ2dCOsSgsYDFCGR2AbUQoCntZ-IJzcRpVOe5qrKt99phpKKjhQGQ6fZa1Jqz1qQkCS3YmESj3wR8vKnGs_i65A3dO-r1V6Gweodc5jY-cmakn-u9SPyhRBwkg2J66xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أبناء مدينة أم قصر يرصدون النيران المشتعلة في المعدات العسكرية ومنصات الصواريخ المتنقلة الأمريكية على الأراضي الكويتية بعد دكها بالصواريخ والمسيرات الإيرانية</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/83473" target="_blank">📅 02:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83472">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">عدوان أمريكي غاشم على مدينة دشتي في محافظة بوشهر جنوبي إيران.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/83472" target="_blank">📅 02:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83471">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترفيهي
🌟
وزير الحرب الأمريكي:
إيران لا تسيطر على مضيق هرمز.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/83471" target="_blank">📅 02:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83470">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⭐️
نتائج الحرب مع إيران.. ‏الطاقة الدولية:
قلق بشأن النفط والغاز إذا لم تتحسن تدفقاتهما عبر مضيق هرمز خلال أسابيع.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/83470" target="_blank">📅 02:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83468">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23edc9238d.mp4?token=nekSEzQHphO_hp8Zg4woUSj9sXJj26BbUgk_i7MnPbs0aY2i05GobVTgIcEP9jFJY4VmVZ90e8u6rSvmFavcIe_-g8nRVFHb2H0MB7DpKn7XGm41cMiW5m40UZJVju4QrkM9QasEd87n0eqQpHskUfd8LLxAHGqrC9PLfvGCJ7cuJ8EEqZojrqBpRTHLxXDX-FSn_Odl7IGQPIsknWOYX94b6YNOt4X_M0VWtOaxhEKypTwhwpe7KDqyRLIbu9junS9sTGyomoGkAxMCWnFSnsifUrGWGxZ7GgD4LimnTyjG5y4Kt5A9FTN1o_N38WBiTXbzKzJ3ZlQ79AaA6YJZvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23edc9238d.mp4?token=nekSEzQHphO_hp8Zg4woUSj9sXJj26BbUgk_i7MnPbs0aY2i05GobVTgIcEP9jFJY4VmVZ90e8u6rSvmFavcIe_-g8nRVFHb2H0MB7DpKn7XGm41cMiW5m40UZJVju4QrkM9QasEd87n0eqQpHskUfd8LLxAHGqrC9PLfvGCJ7cuJ8EEqZojrqBpRTHLxXDX-FSn_Odl7IGQPIsknWOYX94b6YNOt4X_M0VWtOaxhEKypTwhwpe7KDqyRLIbu9junS9sTGyomoGkAxMCWnFSnsifUrGWGxZ7GgD4LimnTyjG5y4Kt5A9FTN1o_N38WBiTXbzKzJ3ZlQ79AaA6YJZvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار الحرائق في منصات الصواريخ الجوالة الأمريكية على الأراضي الكويتية بالقرب من الحدود العراقية</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/83468" target="_blank">📅 01:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83467">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ارتفاع أعمدة الدخان في الكويت نتيجة الهجوم الإيراني الأخير على المنصات الأمريكية المتنقلة</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/83467" target="_blank">📅 01:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83466">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7606ba00a.mp4?token=MAijoTciSTvsfdgGcpjdoSAt6AuiqXNIklrxpengG9VRaRGQZXSIVAwi8eqm0SxGCuRVl47dFH6yRZwvm3-FTTPRmLf0RQ-ZpE1YXtccQfknP1aNvMbp1uMPNIEChtA8utw9qp-pABMEXSO7qH0WUr4osOaLJFf8TIA4RME1K7t1lP_fhfqyb3F0Td4UIXruqC5lk-_OLfTYjXIB3krMp3H4ImnTjmenF3AEI2k6LOfqQ9CUzKlLgV02bkVygIK11rjmAnRpSjtslPFqHLxnGkTve2PHE4L91oOgt51u4-h0b80y002PoURFfPSFVZqYohFHjihHSH1ABQjKun64xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7606ba00a.mp4?token=MAijoTciSTvsfdgGcpjdoSAt6AuiqXNIklrxpengG9VRaRGQZXSIVAwi8eqm0SxGCuRVl47dFH6yRZwvm3-FTTPRmLf0RQ-ZpE1YXtccQfknP1aNvMbp1uMPNIEChtA8utw9qp-pABMEXSO7qH0WUr4osOaLJFf8TIA4RME1K7t1lP_fhfqyb3F0Td4UIXruqC5lk-_OLfTYjXIB3krMp3H4ImnTjmenF3AEI2k6LOfqQ9CUzKlLgV02bkVygIK11rjmAnRpSjtslPFqHLxnGkTve2PHE4L91oOgt51u4-h0b80y002PoURFfPSFVZqYohFHjihHSH1ABQjKun64xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قصف ايراني عنيف يستهدف الطريق التي تسير منه منصات اطلاق الصواريخ الأمريكية المتحركة</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/83466" target="_blank">📅 01:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83465">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6b0622d10.mp4?token=MbiZia_0UNr39ryP_m0M6ICvc60dmKMm61mCQ34wyn8Sn1cmXpq2LKBtBlhN1y9AzaYFnvgKQ3MYlQQ8XIMwmyACJTqGjVIM1tFVfLdKKwtsCpyYb2vWFzxkpNpbiSrpCr93KvYrUEK9lKA8TlcFvB8lF06O-AJmgBYksxr62Pj8Zinhp_YUSAdUGYkYMMVQxz8ygiVsPi6HRhm1_97YE3XMOoEwXavzl6ETBgVNVLoePT5yq6EpZv4CFLaAo2pylDFhKaZtCazr1rrOQeRwqv_w7pwK8tx2UltHFx6qMy0Z6c28245vzFxHWc5w8jC3Z0-07R4I83CWLY-p1PQ-jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6b0622d10.mp4?token=MbiZia_0UNr39ryP_m0M6ICvc60dmKMm61mCQ34wyn8Sn1cmXpq2LKBtBlhN1y9AzaYFnvgKQ3MYlQQ8XIMwmyACJTqGjVIM1tFVfLdKKwtsCpyYb2vWFzxkpNpbiSrpCr93KvYrUEK9lKA8TlcFvB8lF06O-AJmgBYksxr62Pj8Zinhp_YUSAdUGYkYMMVQxz8ygiVsPi6HRhm1_97YE3XMOoEwXavzl6ETBgVNVLoePT5yq6EpZv4CFLaAo2pylDFhKaZtCazr1rrOQeRwqv_w7pwK8tx2UltHFx6qMy0Z6c28245vzFxHWc5w8jC3Z0-07R4I83CWLY-p1PQ-jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انقطاع الكهرباء في معظم مناطق محافظتي أربيل والسليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/83465" target="_blank">📅 01:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83464">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/83464" target="_blank">📅 01:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83463">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/83463" target="_blank">📅 01:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83462">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/83462" target="_blank">📅 01:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83461">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">انفجارات في ميناء لنگه جنوبي إيران</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/83461" target="_blank">📅 01:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83460">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇷
مدير العلاقات العامة والشؤون الدولية لمنطقة كيش الحرة:
حتى هذه اللحظة، لم يقع أي هجوم من جانب الولايات المتحدة على جزيرة كيش. وضع شبكة الكهرباء في كيش مستقر تمامًا، وجميع الخدمات الأساسية تُقدم دون أي انقطاع.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/83460" target="_blank">📅 01:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83459">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">عدوان على محافظة لرستان الإيرانية.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/83459" target="_blank">📅 01:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83458">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e6b275f2b.mp4?token=tcaicEyH2vrGsCMrqVsWroxx4yqjup8phrbAt34McNExxZ3ma8AxLPtLAACtyyzFgAjB0sa1hfJtMkBq2CCl_g8WwFYalnT5WrVFmEWnUA9e6STzoo2fBMMG2WmugzZW7p5NYjtrx2TUZ4ohkRLXjTLqy3En5k7xYi3iq-UIafmOgVrsN9khBbpO89PXKPgc5ytwYI72zgLMSWCqa1olnoa3KcBGmwdv6vHDTCo1Nze0SyLHSZFr0aGWUf3s20FXgdjV6H3Lv4IIUJYvOIMHZ_zzFR3XtgvydCWDU6W-1PsBjJae0cSwtKwbrTJSY8As6PwRq6qRSaPfgswA8bDc6Uef7FKtR-MqT8X1wO6R4DEwGK9wj6LEcWIq9gkYmcUT3nBUkGTSbAwq-jBXozY8EuKv44d400moBglPhLqwI9EJ4dx1DcoqfVgKemzxRRqMhxlkZS15U0BtnZg0JNdwmA5w35gz040-2Y6qNIBpVXAKT3EXn7fobo2nozlUMTqgepqhbut4WOP8oCE5k5wChigMfVaVP7vYyrR0xGVsHCcm32ENyNMej9n-a4TYKbjdSQDkg-IGTTZiW6-ukUJZo4JJ1u44buBT_Nt3Em2VRK7z3eQDf1vzgxXjsVwgYQZvVGnnr8qkEygfTKGQmlpmnO-Sf443PtwYCiqivNvsR_E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e6b275f2b.mp4?token=tcaicEyH2vrGsCMrqVsWroxx4yqjup8phrbAt34McNExxZ3ma8AxLPtLAACtyyzFgAjB0sa1hfJtMkBq2CCl_g8WwFYalnT5WrVFmEWnUA9e6STzoo2fBMMG2WmugzZW7p5NYjtrx2TUZ4ohkRLXjTLqy3En5k7xYi3iq-UIafmOgVrsN9khBbpO89PXKPgc5ytwYI72zgLMSWCqa1olnoa3KcBGmwdv6vHDTCo1Nze0SyLHSZFr0aGWUf3s20FXgdjV6H3Lv4IIUJYvOIMHZ_zzFR3XtgvydCWDU6W-1PsBjJae0cSwtKwbrTJSY8As6PwRq6qRSaPfgswA8bDc6Uef7FKtR-MqT8X1wO6R4DEwGK9wj6LEcWIq9gkYmcUT3nBUkGTSbAwq-jBXozY8EuKv44d400moBglPhLqwI9EJ4dx1DcoqfVgKemzxRRqMhxlkZS15U0BtnZg0JNdwmA5w35gz040-2Y6qNIBpVXAKT3EXn7fobo2nozlUMTqgepqhbut4WOP8oCE5k5wChigMfVaVP7vYyrR0xGVsHCcm32ENyNMej9n-a4TYKbjdSQDkg-IGTTZiW6-ukUJZo4JJ1u44buBT_Nt3Em2VRK7z3eQDf1vzgxXjsVwgYQZvVGnnr8qkEygfTKGQmlpmnO-Sf443PtwYCiqivNvsR_E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
نيران واسعة تلتهم إحدى القواعد الأمريكية على الأراضي الكويتية بالقرب من الحدود العراقية.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/83458" target="_blank">📅 01:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83457">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b22de48d50.mp4?token=oD4J7JOPiyERvWoDM_gkQorERUKg2FPu2-frimGIj_s-OuF73Dxx5oUeVhLPrWvgTkdpr1FMou8d9A9G86oWk1lOQzEGuJPsda28w6eRQpxcNmZp3k7YBOj7HPgVDH44uYQc2AVe0Jf8f_c1O8GLIgrtjN5l35qwLcWm-rXnSDmdcNFQ2z1LTZoDEBMbhNBeD4uscvW-spqCrdjME5cgKFGac4zEBicmV0jOGt0ujA61XShubeSNI9ZGGh5ELNwAbLvXiaRXgaj9-qF_bYl-QBPBSnHGUj-raNvZYnx4IXyvE6iSAwU8g2jbacRQ4KSuFPrqajyv3V1sin3mbKcnFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b22de48d50.mp4?token=oD4J7JOPiyERvWoDM_gkQorERUKg2FPu2-frimGIj_s-OuF73Dxx5oUeVhLPrWvgTkdpr1FMou8d9A9G86oWk1lOQzEGuJPsda28w6eRQpxcNmZp3k7YBOj7HPgVDH44uYQc2AVe0Jf8f_c1O8GLIgrtjN5l35qwLcWm-rXnSDmdcNFQ2z1LTZoDEBMbhNBeD4uscvW-spqCrdjME5cgKFGac4zEBicmV0jOGt0ujA61XShubeSNI9ZGGh5ELNwAbLvXiaRXgaj9-qF_bYl-QBPBSnHGUj-raNvZYnx4IXyvE6iSAwU8g2jbacRQ4KSuFPrqajyv3V1sin3mbKcnFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
عقب هجوم صاروخي وبالطيران المسير الإنتحاري.. إشتعال النيران في المعدات العسكرية الأمريكية على الأراضي الكويتية القريبة من الحدود العراقية.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/83457" target="_blank">📅 01:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83456">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a6f85a6f.mp4?token=LxAuWLVKali98A18EsClgGDgeFmNPxnVs8AVBIbSFtcaZmK-ogF_y5RDP3y0EEaUQ0XWmYxbE3WK_1T7LGsIcBpUMOMv25q4GsDRQMzMs9RRKsoi8Y9NQLTVn2QIrrbXIgCoUhjWYGjqnWMxNP7UmicNM_HrAouE1IS9n7VNvADB5AEBBgRWNVlhdo3KMdzXwd4spdl_aKg1kOf6KTeWCULVV3f4wsD4WqJUcl1xPRXfRk5Yv9DAEZ8dog47VaW2vosAqRocBoVQo5g1bJ1vUIiFAlLwA80qfvDOlFNb_2J8kwBD0bo2OSWK9M8zYn3k5OEdbk6dCa95loKJ4hekKgDaLhvm6CeebVVFXyo7PiQcwcCNtolXU8lkw3MW6ISjnVMqNg1L58jsPnM1OxUVBupE5cs74fhMr0tGZmizPHiY4go5rDNivxMBXzCv6eCczjdS0VIh6r5Zs1T04gEZcHUwxJfbx0dZeMcXeXyY2aMiHJwOIE1xXBgj_-7qFlruzC8sZTf52HOsvSXhciccKandX-frNA_ARmsJJbjWxk_Bo6mkn1G6CX5JSRsCEdhT_3R8ARHE2LJ2BWzS9BXeoJfS1nhVrMEPXVtvF-QoSF3dXl9emFtown8pwokNVBXvKJzxhGZEkosPmnqjeCA99LHUyjc53pAf2NSyYEZz9G8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a6f85a6f.mp4?token=LxAuWLVKali98A18EsClgGDgeFmNPxnVs8AVBIbSFtcaZmK-ogF_y5RDP3y0EEaUQ0XWmYxbE3WK_1T7LGsIcBpUMOMv25q4GsDRQMzMs9RRKsoi8Y9NQLTVn2QIrrbXIgCoUhjWYGjqnWMxNP7UmicNM_HrAouE1IS9n7VNvADB5AEBBgRWNVlhdo3KMdzXwd4spdl_aKg1kOf6KTeWCULVV3f4wsD4WqJUcl1xPRXfRk5Yv9DAEZ8dog47VaW2vosAqRocBoVQo5g1bJ1vUIiFAlLwA80qfvDOlFNb_2J8kwBD0bo2OSWK9M8zYn3k5OEdbk6dCa95loKJ4hekKgDaLhvm6CeebVVFXyo7PiQcwcCNtolXU8lkw3MW6ISjnVMqNg1L58jsPnM1OxUVBupE5cs74fhMr0tGZmizPHiY4go5rDNivxMBXzCv6eCczjdS0VIh6r5Zs1T04gEZcHUwxJfbx0dZeMcXeXyY2aMiHJwOIE1xXBgj_-7qFlruzC8sZTf52HOsvSXhciccKandX-frNA_ARmsJJbjWxk_Bo6mkn1G6CX5JSRsCEdhT_3R8ARHE2LJ2BWzS9BXeoJfS1nhVrMEPXVtvF-QoSF3dXl9emFtown8pwokNVBXvKJzxhGZEkosPmnqjeCA99LHUyjc53pAf2NSyYEZz9G8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
عقب هجوم صاروخي وبالطيران المسير الإنتحاري..
إشتعال النيران في المعدات العسكرية الأمريكية على الأراضي الكويتية القريبة من الحدود العراقية.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/83456" target="_blank">📅 01:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83455">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">انفجارات في مدينة بوشهر الإيرانية.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/83455" target="_blank">📅 00:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83454">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">الجيش الأمريكي:
‏
قام جنود مشاة البحرية الأمريكية من الوحدة الاستكشافية البحرية الحادية عشرة بعملية تفتيش وتحقق على متن ناقلة النفط "إم/تي وين ياو" في خليج عمان، في 16 يوليو.
‏حتى اليوم، قامت القوات الأمريكية بتغيير مسار 3 سفن تجارية حاولت اختراق الحصار، وتعطيل سفينة واحدة لم تمتثل، والصعود على متن سفينة واحدة لضمان الامتثال الكامل للحصار البحري الأمريكي المستمر ضد إيران.
‏يظل مضيق هرمز والمياه المحيطة به مفتوحة وحرة، باستثناء السفن التي تحاول انتهاك الحصار الأمريكي الذي يفرضه جدار فولاذي.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/83454" target="_blank">📅 00:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83453">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMXZWFk1G1Um6QX1fB6Bp07-WxAi70qAZ7ljgXlim6cVLhRhqMKkDAwikumjSx_OvwGipasetbj8ld3MFTm52WHdeSL2FkpFGKmotPklAiQZ6TctMGgaVEHgZ91zcHPRHmcHPHG3p77ntAVJD631VkGWHZKOP8kZNhHVhdkcDjR2StCFwfPMjUKjnhw-_RLVpiMplF-Biy7YlYDPIeVr-x_98r7Dsu1RSTWLdxvVxSA7P4ZemgNY1fwXtXkTk4Y-IQ3DxxskO3q_IGa_AGzdmRusD9opDb4crr6PM-OcZc7Og-wIpqeBp_KdadsAQ3MQUhpuVL7N-lesjtVaIyUZ-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقطاع الطريل الواصل بين مدينتي بندرعباس ولار جراء عدوان استهدف أحد الجسور الرئيسية.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/83453" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83452">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⭐️
عدوان أمريكي غاشم على محيط مدينة بستان في محافظة خوزستان الإيرانية.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/83452" target="_blank">📅 00:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83451">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">انفجارات في مدينة الحميدية بمحافظة خوزستان الإيرانية جراء صواريخ أطلقت من الأراضي الكويتية.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/83451" target="_blank">📅 00:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83450">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">إستشهاد 2 وإصابة 4 مدنيين جراء العدوان على أحد الجسور في بندرعباس كحصيلة أولية.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/83450" target="_blank">📅 00:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83449">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5MlzApgqNp0OSrzjKcZhqpiOe329jlFo9171mK61leRYqi8ewC6mRm00LjcJEeGAnitWx14XXJUDyO_ul9zcR-nZUVwp-AdExlaccMMODqUHRCBTKSH2IQ5L5FN3B-b1tJbb4IVLZKPGAjlEx0_vMndpOUvnuMSpEqyxgjVTOLVE_P32hiUO_1rm70DgwySomS8rMlAJuuQBeKaJHOmeyyNT58R0CMot5mWRZcMT6iNC6PbGSFr_pRYVk8z-HssxvgPU_ljPkNyk84cS9WvXdFPa2zf2drLLDQsaMAlB7pdeA2eG6fmhd8xhQFispAGhPiuSxq4o1p-M1eDMrXcCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
مقاتلة أمريكية من طراز F35 تطلق إنذار الطوارئ في سماء الإمارات.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/83449" target="_blank">📅 00:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83448">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">عدوان أمريكي غاشم على ميناء سيريك جنوبي إيران</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/83448" target="_blank">📅 00:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83447">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">استشهاد مواطن وإصابة 8 أخرين في مرتفعات "الله أكبر" بمحافظة هرمزغان جنوبي إيران</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/83447" target="_blank">📅 00:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83446">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دوي انفجارات جديدة في جزيرة قشم الإيرانية</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/83446" target="_blank">📅 00:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83445">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">عدوان أمريكي يطال جسر في منطقة كهورستان ضمن مدينة بندرعباس</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/83445" target="_blank">📅 00:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83444">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">انقطاع الطريل الواصل بين مدينتي بندرعباس ولار جراء عدوان استهدف أحد الجسور الرئيسية.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/83444" target="_blank">📅 00:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83443">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">⭐️
مصدر إيراني: لا صحة للأنباء التي تحدثت عن انفجار أو هجوم أمريكي على مدينة زاهدان بمحافظة بلوشستان الإيرانية.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/83443" target="_blank">📅 23:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83442">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/110e253ea3.mp4?token=nvvZt218fx1Pda5vYDq7QPdY4G7fmzOltbJmhUd0ujAcCUrCn33sDthd7rFcxtE_6p2f56Sj_8jdp2N89OYmoNR2BN6VAGfLy1kl3w1-CIHzoqJ8RkJv3LHJ4Eml-5aYJd_Zy3Tw4H0xDJ4xZVYj1dw_xPT9WsHryHFcUM6ba9pS4B-5EQSvT2L_ZbmyP8yYPV7cGPAhf3UkXDpewU_DiWdgQx-z549IVDEjDTPT9QQd5qhwETpBhrz9cakGRpyYe1bUJBHXDI_PwmGndoC9W1vIIkKLySEPfBu4UTadZj0ZwPT7Bbr1ZnFJYa8jeU96Z-zrt3dCw5TILqHyJ67Z3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/110e253ea3.mp4?token=nvvZt218fx1Pda5vYDq7QPdY4G7fmzOltbJmhUd0ujAcCUrCn33sDthd7rFcxtE_6p2f56Sj_8jdp2N89OYmoNR2BN6VAGfLy1kl3w1-CIHzoqJ8RkJv3LHJ4Eml-5aYJd_Zy3Tw4H0xDJ4xZVYj1dw_xPT9WsHryHFcUM6ba9pS4B-5EQSvT2L_ZbmyP8yYPV7cGPAhf3UkXDpewU_DiWdgQx-z549IVDEjDTPT9QQd5qhwETpBhrz9cakGRpyYe1bUJBHXDI_PwmGndoC9W1vIIkKLySEPfBu4UTadZj0ZwPT7Bbr1ZnFJYa8jeU96Z-zrt3dCw5TILqHyJ67Z3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان غاشم يطال أحد الجسور في منطقة كهورستان بمدينة بندرعباس جنوبي إيران</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/83442" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83441">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">AUDIO-2026-03-17-02-59-01</div>
  <div class="tg-doc-extra"><unknown></div>
</div>
<a href="https://t.me/naya_foriraq/83441" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">وما اعرفه عن العراقيين وعن فصائل المقاومة العراقية</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/83441" target="_blank">📅 23:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83440">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">المقاومة الإسلامية في العراق: بسم الله الرحمن الرحيم  (وَلَكُمْ فِي الْقِصَاصِ حَيَاةٌ يَا أُولِي الْأَلْبَابِ لَعَلَّكُمْ تَتَّقُونَ)  إن أبلغ شواهد السقوط الأخلاقي للإدارة الأمريكية هو تبجح المجرم ترامب بغدره وعدوانيته في استهداف قادة النصر، الشهيدين القائدين…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/83440" target="_blank">📅 23:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83439">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eudkl4jX_io6-HP2CucgLx-NmMaEtwGqZcJ-r4BNCza4HlBjkKiuRHdSr53yKhl1RL32JFwvhWus7P6yR8lLPfKRRzD7yPlfU0XAOpo6Y5IBRgNCcrDMjMWyQMUBC16J8-qGZQ3Ce99la2yqFaio-xjrtqsJhLs1KygTZAj8rmiw8kqrGILhBxixHlB6gBZDUpH6GVjyqClgQXQrar_qFOEaLCFlBI5mmeznFpgruR6JclrqTa0ylYWj-a4uEyrI5yLcpqj9q-W3iFEGdhx5z0fysOdr7BXlcm9AXVJrjQeOtkKn_oa_rh_BtrahXhptMDh09Tai9FkxuhcjpH7KFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المقاومة الإسلامية في العراق:
بسم الله الرحمن الرحيم
(وَلَكُمْ فِي الْقِصَاصِ حَيَاةٌ يَا أُولِي الْأَلْبَابِ لَعَلَّكُمْ تَتَّقُونَ)
إن أبلغ شواهد السقوط الأخلاقي للإدارة الأمريكية هو تبجح المجرم ترامب بغدره وعدوانيته في استهداف قادة النصر، الشهيدين القائدين الحاج قاسم سليماني والحاج أبي مهدي المهندس (رضوان الله عليهما) هذا التبجح الوقح لم يزد دماءهما الزاكية إلا رفعة وخلودا، ولم يورث قاتلهما إلا خزيا أبديا وعارا يلاحقه وإدارته ما دامت الحياة.
إن المقاومة الإسلامية في العراق تعلن عن رصد مكافأة مالية قدرها (10) مليون دولار جُمعت من تبرعات أبنائها الأوفياء وأنصارها الأباة، مخصصة لمن يقتل المجرم ترامب، أو لمن يقضي بتخصيصها أو توجيهها لفرد، أو مجموعة، أو كيان، أو مؤسسة.
وسيبقى أحرار العالم يلاحقون قاتل الأطفال والعلماء، فلن يذوق الطغاة طعم السكينة، ولن يجد المجرم مأمناً يتقي به غضبة الشرفاء؛ فالقصاص عهد مبرم في أعناق المجاهدين، ودماء الشهداء ستبقى لعنة تزلزل عروش المستكبرين، حتى يندحر المعتدين، وتتهاوى حصون الطغيان.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/83439" target="_blank">📅 23:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83438">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c55ba97a9.mp4?token=op3XuB4imsYUNNrr4hw22QaANCweCip2eHdLXeFE_TH_5txviJk1KI5ubEI-KXxSyHedYhIXu_jgRzNIoLx5wN7Tjuoq8PXn_yR3r0IKrgb_hiSvAvKIWEezNOLf5g7ukOI9bQs4AOnAymrsCbhj1H3zbDcherTsLqgpbdaDUu2_gKw1dx4-Wv9LsxrVgR1Kbo_hnfxeGpBxGwZoSKPsosKp6A9Jhu7SufujZh0yOfQ76a4yKRLAs8uT08ve5NrhsUDalTob9mkh8S23Vi6KoOldxjtHSL6rPeRjHIERhVn79ehwER8yRS2Q-Twfps5_R8eUJRMsPw6dF5-fpyzWRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c55ba97a9.mp4?token=op3XuB4imsYUNNrr4hw22QaANCweCip2eHdLXeFE_TH_5txviJk1KI5ubEI-KXxSyHedYhIXu_jgRzNIoLx5wN7Tjuoq8PXn_yR3r0IKrgb_hiSvAvKIWEezNOLf5g7ukOI9bQs4AOnAymrsCbhj1H3zbDcherTsLqgpbdaDUu2_gKw1dx4-Wv9LsxrVgR1Kbo_hnfxeGpBxGwZoSKPsosKp6A9Jhu7SufujZh0yOfQ76a4yKRLAs8uT08ve5NrhsUDalTob9mkh8S23Vi6KoOldxjtHSL6rPeRjHIERhVn79ehwER8yRS2Q-Twfps5_R8eUJRMsPw6dF5-fpyzWRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان أمريكي يطال جسر في منطقة كهورستان ضمن مدينة بندرعباس</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/83438" target="_blank">📅 23:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83437">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">انفجارات في مدينة الحميدية بمحافظة خوزستان الإيرانية جراء صواريخ أطلقت من الأراضي الكويتية.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/83437" target="_blank">📅 23:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83436">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">انفجارات في مدينة ايرانشهر جنوب شرق إيران</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/83436" target="_blank">📅 23:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83435">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⭐️
إشتباكات بين القوات الامنية العراقية وعناصر تنظيم داعsh الإرهابي في محافظة كركوك شمالي العراق؛ مقتل إرهابي كحصيلة أولية.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/83435" target="_blank">📅 23:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83434">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1101d37db3.mp4?token=YJA4QthceMS4-t9-5NuUJn2zZrq0H_M4xtT2dDbgPSSIWZoIJd5pJf93VFAXiScX_04M1oBY6dC6BiptpSfl8J1pTutpgWbtI0nD-yXwNJCIgXTvbqT855fP3_FUU0G0eVFrwx5lQzdQ4IsqrW2FxZmTX-v9yAITeKwN-jR8yrBPG-P9mF_jo9SEegrnzxWlGmGwQ3H8SDFwUh9fKYAAOGPcDAId5kCVWEZtVNFmjDkTTCIQt9CtznSzrKPfaRJCIsYa3V8MXAn8RSnCTRtLmxy0-MXTtHakfQkukPOXnFlCYL5sRY4m3_IiIb6fmKI-0m4Y_AQaI-tSq8765pQGaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1101d37db3.mp4?token=YJA4QthceMS4-t9-5NuUJn2zZrq0H_M4xtT2dDbgPSSIWZoIJd5pJf93VFAXiScX_04M1oBY6dC6BiptpSfl8J1pTutpgWbtI0nD-yXwNJCIgXTvbqT855fP3_FUU0G0eVFrwx5lQzdQ4IsqrW2FxZmTX-v9yAITeKwN-jR8yrBPG-P9mF_jo9SEegrnzxWlGmGwQ3H8SDFwUh9fKYAAOGPcDAId5kCVWEZtVNFmjDkTTCIQt9CtznSzrKPfaRJCIsYa3V8MXAn8RSnCTRtLmxy0-MXTtHakfQkukPOXnFlCYL5sRY4m3_IiIb6fmKI-0m4Y_AQaI-tSq8765pQGaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان أمريكي يطال جسر في منطقة كهورستان ضمن مدينة بندرعباس</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/83434" target="_blank">📅 23:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83433">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bca01c43c.mp4?token=fS2j7SKUvAb9OzWYrPYY18HsAH76uONxrMGy4YqdJYYL0oaKae7nljf2jKg_EhNP9PDT8E-gS6fScpeCONXyVNk8QF4Lxx0L1FlGfyHO06u8IiKphjWoZn4365WVMc6K0OInEJNDyfOMKLKqtxAMAYSGaOa3yhcfHBBwTM7sgIl7WsE2dRWBJzD0zxgEBinWXuqWgecnUNUBCAfaej0DuU02STKG5JGfzgOhGNuI59vAVeUQDI7OxEAHS0YNDikmuGxndAzwWTBfNlW3BxRzm3qom9t8Rn-qYIOC1j7FhWqO8uwZCkpZXJx2rRBzIsHkzZa-wtpqJKLUKBf417lTUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bca01c43c.mp4?token=fS2j7SKUvAb9OzWYrPYY18HsAH76uONxrMGy4YqdJYYL0oaKae7nljf2jKg_EhNP9PDT8E-gS6fScpeCONXyVNk8QF4Lxx0L1FlGfyHO06u8IiKphjWoZn4365WVMc6K0OInEJNDyfOMKLKqtxAMAYSGaOa3yhcfHBBwTM7sgIl7WsE2dRWBJzD0zxgEBinWXuqWgecnUNUBCAfaej0DuU02STKG5JGfzgOhGNuI59vAVeUQDI7OxEAHS0YNDikmuGxndAzwWTBfNlW3BxRzm3qom9t8Rn-qYIOC1j7FhWqO8uwZCkpZXJx2rRBzIsHkzZa-wtpqJKLUKBf417lTUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في مدينة ايرانشهر جنوب شرق إيران</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/83433" target="_blank">📅 23:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83432">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c016d251a.mp4?token=ZTRK1MjSDs2p5niYxJrhuGpePSO3kWPi0lg49IWZFUoee4mfK8vADToOR0TmjB8zkcMts9ZRDMp6rYgrL-iI5Kw4BUkY_DP43tlacPnT97HX1PwWa0S9DJNiq9bDzvqiWAViqIhMJ0powFYsxNTOx6A8IXmB9EhOlu3bLEwpnbXMj8GQ3SgxIWNFiAOl_jNnvzo7O0pFPfHj9HjydM8qR9WuBfHQFCjGpJYzbgrNAEBM9OkCMw7WqX8gIs_Mx8NdOCogLoCG6RAjwNLK8_lOP2dS4V6IE5jxangTF5nCk_S6H8BBk00jW34TB8wV2gmhw_Jl5GXsRYQgWHgz2QB2Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c016d251a.mp4?token=ZTRK1MjSDs2p5niYxJrhuGpePSO3kWPi0lg49IWZFUoee4mfK8vADToOR0TmjB8zkcMts9ZRDMp6rYgrL-iI5Kw4BUkY_DP43tlacPnT97HX1PwWa0S9DJNiq9bDzvqiWAViqIhMJ0powFYsxNTOx6A8IXmB9EhOlu3bLEwpnbXMj8GQ3SgxIWNFiAOl_jNnvzo7O0pFPfHj9HjydM8qR9WuBfHQFCjGpJYzbgrNAEBM9OkCMw7WqX8gIs_Mx8NdOCogLoCG6RAjwNLK8_lOP2dS4V6IE5jxangTF5nCk_S6H8BBk00jW34TB8wV2gmhw_Jl5GXsRYQgWHgz2QB2Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار الكويت باطلاق الصواريخ نحو الاراضي الايرانية</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/83432" target="_blank">📅 23:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83431">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bab26e08a3.mp4?token=Wy14QgjbKX3sVzEeRqtQVWnhZrbkridHTPH5iiwFVNmJhd9lUV758YY0r1Wfa96QuSVJhIJNUjFxJYTC1AhTxCvBxY1B9jeAHvIM-5LwMz1S5jQiNge1ko2wjvTQsjjGcbKAqSgrbfYv917PPgfMSSnx5m2j8Dj4pp7nT0M6j3bdHGxKuYDAXxCvjRynzRfysE9kIPuyADiQAZBCP10usFb7eC4C1PpjGz1ILimx3HjMKWYYkwlQe2INxm8wyBWlRHIzoYy91g_GnsvuIUiEcoJ7WtDipz6TjljamFhGO1QkUctdyInLQrIhswSiJ0a4QK5X7x84MJxMCWynHYadFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bab26e08a3.mp4?token=Wy14QgjbKX3sVzEeRqtQVWnhZrbkridHTPH5iiwFVNmJhd9lUV758YY0r1Wfa96QuSVJhIJNUjFxJYTC1AhTxCvBxY1B9jeAHvIM-5LwMz1S5jQiNge1ko2wjvTQsjjGcbKAqSgrbfYv917PPgfMSSnx5m2j8Dj4pp7nT0M6j3bdHGxKuYDAXxCvjRynzRfysE9kIPuyADiQAZBCP10usFb7eC4C1PpjGz1ILimx3HjMKWYYkwlQe2INxm8wyBWlRHIzoYy91g_GnsvuIUiEcoJ7WtDipz6TjljamFhGO1QkUctdyInLQrIhswSiJ0a4QK5X7x84MJxMCWynHYadFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار إطلاق الصواريخ من الأراضي الكويتية باتجاه الجانب الإيراني.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/83431" target="_blank">📅 23:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83429">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bd969d3aa.mp4?token=JSdKLk6X4-Sfwr54ppXX4qpnmva9Qfm-PmadWmrdQItsp3FWAQ6tghlGE1Oe_wkhTp4V7MKCgXdnZDOoOHuIilBmQgnTEsnonsQRhQSKwOfBhr9anlMFxpFfcdZPuOn2RU8NQ6ZVZ7VV4OJYtpozMSKsiqCkLgbY95zY8ZgI1cMVD1m4cGw2ryXECqeH8Rujo4RDHaBXOVz4BZyL8FBmfetVIezcrRU3cpTV-T_AIzykopxpHp8ao3SNJHJe4nkYqwza3E7KfEFxDIzX0gC4kzRz8uMrszq8IE_TFAqjRfKViX4QNRf7wIJqIjoIYwEoUULbMaUFr7a5b5SR3suP1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bd969d3aa.mp4?token=JSdKLk6X4-Sfwr54ppXX4qpnmva9Qfm-PmadWmrdQItsp3FWAQ6tghlGE1Oe_wkhTp4V7MKCgXdnZDOoOHuIilBmQgnTEsnonsQRhQSKwOfBhr9anlMFxpFfcdZPuOn2RU8NQ6ZVZ7VV4OJYtpozMSKsiqCkLgbY95zY8ZgI1cMVD1m4cGw2ryXECqeH8Rujo4RDHaBXOVz4BZyL8FBmfetVIezcrRU3cpTV-T_AIzykopxpHp8ao3SNJHJe4nkYqwza3E7KfEFxDIzX0gC4kzRz8uMrszq8IE_TFAqjRfKViX4QNRf7wIJqIjoIYwEoUULbMaUFr7a5b5SR3suP1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من البصرة تُظهر إطلاق صواريخ بشكل متواصل من الجانب الكويتي باتجاه إيران.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/83429" target="_blank">📅 22:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83428">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14dca3521c.mp4?token=cxQ5E4yFcJzkjNDdEJlbMYxnxK3EQppZXr7chvOE36RVj6xWTqjS1bxJ6KGIXO9h9RMNWFBbzF4EssRb2e3rkzjSHEluQcl4ZA8JZOyWWTGV6k4pZOGJ4oULT9ztuZCINZnY1TeoBKRbHWQi3rI9OZ3TRKAMpjdD9QRDcedUOx8F_tUJbqG3-SsifUoX9Zn-2nNlQL-e-612fWVpyHpXA72VmC70NYp3za2nalQKZcEHFDtOpVKWkGmDNnuG1JoI33SIC2JzqxVzH1N_mE73lW6bfasjCZYTjkm7pU24YXmKL9S06TRcz8OcYkJ8ek5qbDBPQ0cc5jcGnP93vbGQ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14dca3521c.mp4?token=cxQ5E4yFcJzkjNDdEJlbMYxnxK3EQppZXr7chvOE36RVj6xWTqjS1bxJ6KGIXO9h9RMNWFBbzF4EssRb2e3rkzjSHEluQcl4ZA8JZOyWWTGV6k4pZOGJ4oULT9ztuZCINZnY1TeoBKRbHWQi3rI9OZ3TRKAMpjdD9QRDcedUOx8F_tUJbqG3-SsifUoX9Zn-2nNlQL-e-612fWVpyHpXA72VmC70NYp3za2nalQKZcEHFDtOpVKWkGmDNnuG1JoI33SIC2JzqxVzH1N_mE73lW6bfasjCZYTjkm7pU24YXmKL9S06TRcz8OcYkJ8ek5qbDBPQ0cc5jcGnP93vbGQ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من البصرة تُظهر إطلاق صواريخ بشكل متواصل من الجانب الكويتي باتجاه إيران.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/83428" target="_blank">📅 22:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83427">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da81453cfd.mp4?token=j9emDUL5WVrjjjgey14ALIRKwqzQTLXQfRcApPZ43tnzo0n2ypYAJRQAfCwL77s_B2SEARYEGA8ObGA6bqpOUKxbhLiKAzD99CJqKEHDnECZ4Xtptlxf9GxA4mRX_ntR5CxnQ6vXVWLnAtyhW28KDNDP9n_mkNr7P46Hu_1XxYw2KspWPQeFuG7240MPzKbZosvqH5vTucyPCSIBwCiUR2mvAqJUpKMQKU3008b0iswPy1sd89_70UYPvvIRCOPc179wiZMchSkBOvdk51GnZ971bTQNao-OO4gR5PC1U4xvHExMhfa9-Y9gSOqoqoM4epQSmFjkToP81cDXTtOQAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da81453cfd.mp4?token=j9emDUL5WVrjjjgey14ALIRKwqzQTLXQfRcApPZ43tnzo0n2ypYAJRQAfCwL77s_B2SEARYEGA8ObGA6bqpOUKxbhLiKAzD99CJqKEHDnECZ4Xtptlxf9GxA4mRX_ntR5CxnQ6vXVWLnAtyhW28KDNDP9n_mkNr7P46Hu_1XxYw2KspWPQeFuG7240MPzKbZosvqH5vTucyPCSIBwCiUR2mvAqJUpKMQKU3008b0iswPy1sd89_70UYPvvIRCOPc179wiZMchSkBOvdk51GnZ971bTQNao-OO4gR5PC1U4xvHExMhfa9-Y9gSOqoqoM4epQSmFjkToP81cDXTtOQAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من بندر عباس تضهر ارتفاع اعمدة الدخان بعد قصف الاحتلال الاميركي الاخير</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/83427" target="_blank">📅 22:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83426">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">الكويت تعرضت مؤسسات حيوية لهجمات إيرانية بالمسيرات</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/83426" target="_blank">📅 22:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83425">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">الكويت تعرضت مؤسسات حيوية لهجمات إيرانية بالمسيرات</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/83425" target="_blank">📅 22:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83424">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/83424" target="_blank">📅 22:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83423">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🌟
ترامب: سمحت إيران لمواطنة أمريكية، احتُجزت ظلماً في ديسمبر/كانون الأول 2024 خلال فترة رئاسة جو بايدن، بمغادرة البلاد. وهي الآن بأمان خارج إيران، وبصحة جيدة. تُقدّر الولايات المتحدة الأمريكية هذه البادرة الحسنة من إيران!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/83423" target="_blank">📅 22:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83422">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c56cad1a2.mp4?token=Ae_xxFHMfk0QvHH9DCcwDHgFWO1R8RDuwO4BYknQ4stJXm5RIu3-OXD7VoMd8V97yyED3cIZmZAs1jvJJWdRwbr0NNtKhzx1JtxsHx0YUt-4QoyNPL6mbjGjTanQQcVYdOoRR3XmfYKGn9WQXHjyRV4gBM3EZOMwGAK1Jp2kKf0k0B6BM6f2O36KSf-UcsC4PugY6-y_1XCilGak3L-XjwPLchiU_mSB9YpJQ6fE6diokz9Ra3UCM_d06Wvg5F7sU5M4nAP9zb4MhRfc_u0N_On1rv4ELxqqVQ5LRA96lDkCKCHO1GzjPC8vP5nOoaVlL82WY0n7mQ1SoGKxQ6kpEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c56cad1a2.mp4?token=Ae_xxFHMfk0QvHH9DCcwDHgFWO1R8RDuwO4BYknQ4stJXm5RIu3-OXD7VoMd8V97yyED3cIZmZAs1jvJJWdRwbr0NNtKhzx1JtxsHx0YUt-4QoyNPL6mbjGjTanQQcVYdOoRR3XmfYKGn9WQXHjyRV4gBM3EZOMwGAK1Jp2kKf0k0B6BM6f2O36KSf-UcsC4PugY6-y_1XCilGak3L-XjwPLchiU_mSB9YpJQ6fE6diokz9Ra3UCM_d06Wvg5F7sU5M4nAP9zb4MhRfc_u0N_On1rv4ELxqqVQ5LRA96lDkCKCHO1GzjPC8vP5nOoaVlL82WY0n7mQ1SoGKxQ6kpEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
انفجارات متتالية في بندر عباس</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/83422" target="_blank">📅 22:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83421">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سنتكوم: ‏في تمام الساعة الثانية مساءً بتوقيت شرق الولايات المتحدة اليوم، بدأت القوات الأمريكية شن موجة جديدة من الضربات ضد إيران.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/83421" target="_blank">📅 22:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83420">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇶
🇮🇷
انتقاد شديد للدكتور علي أكبر ولايتي من رئيس الوزراء العراقي
مستشار قائد الثورة، في مذكرة، وجّه انتقادًا شديدًا لزيارة رئيس الوزراء العراقي إلى الولايات المتحدة، وكتب:
بسم الله الرحمن الرحيم
﴿إِنَّا لِلَّهِ وَإِنَّا إِلَيْهِ رَاجِعُونَ﴾
«زيارة مؤسفة، جاءت في غير وقتها، وألحقت ضررًا بتضحيات الشعب العراقي الأبي والمجاهد عبر آلاف السنين من تاريخ هذا البلد الكبير، قام بها رئيس الوزراء الشاب قليل الخبرة، السيد علي الزيدي».
وأضاف أن استخدام آية الاسترجاع في وصف هذه الزيارة معبّر تمامًا، معتبرًا أن ما جرى خلالها يُعد من الأحداث النادرة في تاريخ العراق الطويل، وأنها وجهت ضربة لا يمكن وصفها أو استيعابها لكرامة الشعب العراقي المؤمن والشجاع.
وأكد أن هذه الخطوة تمثل عارًا كبيرًا لكل مسلم وكل إنسان حر، سواء كان عراقيًا أو غير عراقي، ولا سيما أنها جاءت بعد استشهاد أحد أعظم العلماء وأكثرهم تأثيرًا في عصر الغيبة، في وقت لم تكن فيه مراسم الحداد قد انتهت بعد.
ووصف الرئيس الأميركي بعبارات شديدة، معتبرًا أن جرائمه لا نظير لها في التاريخ، وأنه يفوق أكثر الطغاة والقتلة شهرة في الإجرام، داعيًا الله أن يكون في أسفل دركات جهنم.
وأضاف أنه لا يعلم ما الذي كان يتوقعه رئيس الوزراء العراقي من هذه الزيارة، متسائلًا إن كان قد اتخذ قراره دون استشارة، ومؤكدًا أنه لو استشار أهل الخبرة والالتزام في العراق لأدرك المكانة التاريخية والدينية لهذا البلد.
وأشار إلى أن العراق، منذ الحضارات السومرية وحتى الإسلام، ثم في عهد أمير المؤمنين الإمام علي عليه السلام، والإمام الحسن، والإمام الحسين، والمختار الثقفي، ومالك الأشتر، وميثم التمار، وحجر بن عدي، ثم ثورات الأئمة عليهم السلام، كان له دور محوري في تاريخ الإسلام، وأن الشعب العراقي قدم أعظم صور الجهاد حتى أسقط نظام صدام.
كما ذكّر بموقف نوري المالكي حين رد على ترامب بالآية الكريمة: ﴿وَلَن تَرْضَىٰ عَنكَ الْيَهُودُ وَلَا النَّصَارَىٰ حَتَّىٰ تَتَّبِعَ مِلَّتَهُمْ﴾، مشيرًا إلى أن ترامب كان يعتبر المالكي عقبة أمام سياساته.
وختم بالقول إن من المؤسف أن يزور رئيس الوزراء الحالي البيت الأبيض قبل انتهاء مراسم عزاء القائد الشهيد، من دون أن يظهر أي أثر للحزن، مضيفًا أن السياسة تعني الإدارة، وأن من يفتخر بقتل القادة الشهداء كان ينبغي أن يواجه برد حازم، لا أن يُقال أمامه: «أنا لا أتدخل في السياسة». واعتبر أن هذه الزيارة وهذه الإهانة تسببتا بحزن الشعب الإيراني والشعب العراقي المؤمن والمجاهد، معربًا عن أمله في أن تكون كلماته دافعًا للتأمل وتحمل المسؤولية.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/83420" target="_blank">📅 21:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83419">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سنتكوم:
‏في تمام الساعة الثانية مساءً بتوقيت شرق الولايات المتحدة اليوم، بدأت القوات الأمريكية شن موجة جديدة من الضربات ضد إيران.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/83419" target="_blank">📅 21:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83418">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RY_4IJJot_23e7G11LHOgunMys1A4naOX2Zht6MyhZ9anWibkac1lJA1krCi3aimvE3s_2rcySOHBz5YFnINl33gSwR6Qm23trq_mKtYagRT9uuHkjbclZrgqoVJk9V38Lmh4Nu8OQSDWz93IbdxSOtGq6RcLqQM210rEbZpheP2Pqijg7jyyvkf-Uegy-WOiUDHxj1HY44g62M1qfBbi6jYxxDgEYjJ5uz9g-3nWHkS38vo7SRycmZ5UVDpuj3I09dtOf2CN__jFstJVhpfHPx4D2JTCw_RB7i7ItE-bLcvvP9xHGUk4QvoiTKPwMbXfqj6xaUbmyc0ITHrtZvFwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ناقلة الغاز الطبيعي المسال "مبارز" المملوكة لشركة أدنوك عالقة في نفس المكان بمضيق هرمز باتجاه الطريق العماني منذ الأول من يوليو بسبب تحذيرات الحرس الثوري الإيراني.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/83418" target="_blank">📅 21:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83417">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇸
‏
البيت الأبيض:
إيران تواصل الانخراط معنا في محادثات وترغب في إبرام صفقة.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/83417" target="_blank">📅 21:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83416">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇶
السفارة الأميركية في أربيل شمالي العراق
تنشر تحذيراً أمنياً شديداً بعد قصفها ليلة امس بطائرات مسيرة تدعو المواطنين الأميركيين إلى عدم السفر نهائياً إلى العراق، محذرة من وجود تهديدات وحالات عدائية تستهدف الأميركيين.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/83416" target="_blank">📅 20:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83415">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇶🇦
‏
قطر
: نرفض تقارير إعلامية إسرائيلية باطلة زعمت موافقتنا على المشاركة بعمل عسكري ضد إيران.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/83415" target="_blank">📅 20:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83414">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انفجارات شديدة في سماء دبي</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/83414" target="_blank">📅 20:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83413">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkZ6lnXE1nxI6M0oiwzhxddrFvW68vAfam68W_N3jjZrHgvUoduy7yi3exnXHGZoavTBjXbt22O_NHMPNxOTu5UFSM2TFIn8KiZ_oAPhsLSwNMxrAm6h_Ozj93XtBZtzLJ7p3EUIGyMXStMfw7h5lunAR1UyRtp1v9LOOQDYZKm9gli07aVAYT3hWmNFlLQp7z5Y74FDSTo9hdcCMkp0fH6Ok_tBDHNEH-2PPy7GCNL4Qh26U3iZkzBnTjnuaTxkUTVu155s2nfB60yN4Dj-xX1jD9hw9ggWlCQYR9JyPVLQlCf8y53gSUREJk9sGjhL7XwztOzVa9iaOFneBH9SHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اكبر.. انفجارات قوية تسمع بقاعدة الظفرة الجوية في ابو ظبي</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/83413" target="_blank">📅 20:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83412">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رويترز: دوي انفجارات في وسط دبي</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/83412" target="_blank">📅 20:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83411">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">انفجارات على مقربة من الحدود العراقية الكويتية</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/83411" target="_blank">📅 20:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83410">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رويترز
: دوي انفجارات في وسط دبي</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/83410" target="_blank">📅 19:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83409">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي: ‏
"اذهبوا إلى الجحيم، أنا أمثل الأمريكيين أولاً." هذا ما قاله نائب الرئيس الأمريكي جيه دي فانس رداً على الحملة التي تمولها إسرائيل بهدف عرقلة المفاوضات بين إيران والولايات المتحدة.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/83409" target="_blank">📅 19:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83408">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇷
انفجار في بندر عباس</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/83408" target="_blank">📅 19:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83407">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇧🇭
‏
خفر السواحل البحريني:
تعديل موعد الحظر البحري ليبدأ عند الساعة 6:30 مساءً ويستمر حتى 4:00 صباحاً.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/83407" target="_blank">📅 19:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83406">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B648NWVMiUi8QIzJlzRd4Yo8MUJq0y9ja1I83JmSsxSSmkoUWqWV5h9UbQc0Ubpbbe7agvA0BZ8VR1gaFExDJAGw7N4KtoWj1OlsN72_VRViuj16ZqGmHKfWv3AkqSoxcrPQpMf2mYzsN0uxMFZUFBY0pLlltmNs4d7ff4I7FWX_2N1hlk3ix9jWfi2GSeqLTU93aM2Q6-hfleTqskApo4sL8kmz8GowdWx5xJaJCx6uADxx478s_m6WsuisQcEWY8WdnaWvp_4Zd4j4qb0dwuCWGz8KzWTd0qXlz1ozCRit9CCZek4FMnt0yOcnBGMASXTyo0tJUUZk_VWHc8y8sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
شوهد مضيق هرمز اليوم شبه خالٍ  ناقلتان فقط ظاهرتان تعبران المضيق ناقلة باناماكس متجهة للخارج عبر إيران، وناقلة عملاقة متجهة للداخل، وهي في وضع الخمول.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/83406" target="_blank">📅 19:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83405">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JscGVBChV4Y6qogtWCWzguLYPK_6sxlkxr1OZQFRy-AvLqJ5dXp66DlQkEJaPlB4TPTyuiz0hNk7USLbX9soxCh1zpFoaugcwIpzr2CP_viSjhGtZlUFfXAELwnvLCQ7ZA8-9JCLvLNxpbk2jf4hYPd9QBw4Q_HPk3OxdvBgeIB51XHkLvl_gz85gOqMnAgJDZkKRC_t4dsMTmvNek-oamvqnq-v-cv-2Mz99kDEP3_hW7QIov9iNTowhE8J9pvNvJWEemaXJ9ooMU3qAeEarZafUVualTKaEIKtFu9fMII3pnit5MbPN9sAkzXkNlP42UxpfwcZvfM6tnsN8EXsGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
شوهد مضيق هرمز اليوم شبه خالٍ
ناقلتان فقط ظاهرتان تعبران المضيق ناقلة باناماكس متجهة للخارج عبر إيران، وناقلة عملاقة متجهة للداخل، وهي في وضع الخمول.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/83405" target="_blank">📅 18:56 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
