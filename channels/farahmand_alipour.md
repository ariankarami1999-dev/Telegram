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
<img src="https://cdn4.telesco.pe/file/aPYwn4rYQFQ-zH-OPyr6rzy7gFLfty2tzHCRwHT3slEhBR32s_6hVV6ICS3v6-Ijfm3c9td88HdFOncXFTdcMZo5U-JQNkOPDWEP4RWVI8G7dlI1WQk6jkK9tgf_ipORFNh9hfjRDvuIdlxn6csJCfXgygNKHr8MEF6IiHB_cPl_1n0PnpDEPijrgoIYcZZc2qrUb4H3v4ZDfFZA3oLusqXPZqBCVXhZncKytOT7-Stt1CPI22qyIuE499bd2fWKk4e_FbFrgyFOOYbFE_GtOvPudd0GzOtnHp8h7Z_7mIQ2Y6JpZMU5_X-Mdyds7Tl86ufopok9xXrNE_wi9Ni0wg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.8K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-16 13:56:28</div>
<hr>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=UUM9sSAco5EatrPm4ED9j5Unmx36DlLowxiAkQzHhTRz6OHTVKv7ZapEf89y9ur6_PQaKF8zNPQ7t58oBNhf_vv0so5l0OlPV8k7fCU3XBbQhH63tq7FT9LnfyBY2xj6r696wpWGRn2-cVJXKUuGk4yt-3GEiSAVXHHjhLE64X_fKSVJgDKwTsShz9p_znqoQ7CVMii2hYD0IUrsVaZ_ZofIzEzmS2w9P8U9Hua3J_nNCgtYIS42UI0es5zBViTyhC_AL9ZDkmqXGg153ObAHsAllxCXTr_MJAxSS8ef6tEYmj2pZlu99PjZyR106gGa6x5ujC5dwAWoVWYn_Vbl1Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=UUM9sSAco5EatrPm4ED9j5Unmx36DlLowxiAkQzHhTRz6OHTVKv7ZapEf89y9ur6_PQaKF8zNPQ7t58oBNhf_vv0so5l0OlPV8k7fCU3XBbQhH63tq7FT9LnfyBY2xj6r696wpWGRn2-cVJXKUuGk4yt-3GEiSAVXHHjhLE64X_fKSVJgDKwTsShz9p_znqoQ7CVMii2hYD0IUrsVaZ_ZofIzEzmS2w9P8U9Hua3J_nNCgtYIS42UI0es5zBViTyhC_AL9ZDkmqXGg153ObAHsAllxCXTr_MJAxSS8ef6tEYmj2pZlu99PjZyR106gGa6x5ujC5dwAWoVWYn_Vbl1Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رجب صفروف، عضو تیم روسیه در مذاکرات رژیم حقوقی دریای خزر، مرداد ۹۷:
‏همه ما انتظار داشتیم ایران درخواست ۵۰ درصد بکند. قانونی هم بود. اما جلسه اول یکباره جمهوری اسلامی گفت تقسیم برابر بین ۵ کشور، یعنی کمتر از ۲۰درصد
‏برای ما عجیب‌وغریب بود که چجور ایران دارد از حقوق خودش گذشت می‌کند
‏این برای بقیه کشورها مثل هدیه الهی بود. از خوشحالی نمی‌دانستند چکار کنند</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/farahmand_alipour/6521" target="_blank">📅 13:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6520">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkQ9qRQUS7w47T078UsCCr1OL4LCw1jfduu02WsozfK3iyE6yKh_gA1fegoauyy8Mh8ldlt8aLwok_o6cgnFrJtRJbHmeI_3gDh1Dgjfa-51xvqzxkfUa0k4TV8_SHRRsX7Tyhhbg0kCIb7KzgoNFPnGREPGqhUtySWdYffHaYrd8G0IySksQl4CfVtW9V9ACgRWwfGrkuqe6MKl-_bcQUMzRuHKKWvfyhV8X1BHsUvYOlTupLg2OOS8l8tL86_uaZ_Y9un6x94Ehl8bps9iIdrAyXoWQ1zv87R30cyvdp3qzERFf2r7wF15aTj8GWNHyfGUrnQvMos9UtUQbibkOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی به عنوان رئیس شورای عالی امنیت منصوب شد.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6520" target="_blank">📅 22:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6519">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQbNi7F0M-RfSSzb_Q4zV1n_-CcINqFKeYvMBrXbYYj7LPpL4dxwtZ2auSDHNijfoiLGUqSWMSb2hkKjeuFcnxdUc0ETCHkmHYX5Tp03Cnvv64Iz33ruPL-Rqax5ereVDV4yjGc2YyocKZNZOy5C1MDCzpQEzzN7zcZNSELlTmBYE0gJXKOnU7dNth7WPvUMPwJ60R2X_HTjoC6kOr-drq3NzMF3DfqDFAzsYumMct-Pc3_WQ_qVWpb5Db_eW2yfwUFQr5Bs5-_BPtq-G6Iw59yDGtO6E2FoMdrjzb8jE1MOgrB8GqsUY3iVOhpb7K-Cfuxi6bN2mVJXz6KGelYEFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«حمله‌ای گسترده در راه است…
نه، صبر کنید، می‌خواهند مذاکره کنند.»
این یعنی «دیپلماسی نمایشی»
که مدام در حال تکرار است.
استفاده از زورگویی، وعده‌های شکسته
و اخبار جعلی به‌عنوان ابزار فشار،
راهبردی شکست‌خورده است.
واقعیت‌ها را بپذیرید و به تعهدات خود عمل کنید.  ما به نمایش‌های بیشتری نیاز نداریم.
- فهمیدن حمله به کشتی‌ها و زدن زیر تفاهم‌نامه نمی‌تونه براشون دستاوردی داشته باشه ، از ترامپ میخوان که مذاکره کنند.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6519" target="_blank">📅 22:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UeEhMb5MMMtdBsReytDEPrXUtsaNYd3ZgLcAFoKm29D8sGrRU6UaLhCe7cTC8fLVNIPTQRsHdJ4L7gqzB515R9BXlwj4bTsyx5OZXDm05lAC1HoKOjCMxKSV3i_1GauLsMtJY39aRTyGYN3cOl81elBKfJi6U_DmD_dU12ypZTpIEKOZa4A0YfMAuOj9hlp4kCdq4MdT3BMLkOyetIIOOkaNdUkcwIs6-wK6SbUUR_G0Yx7FrA69p9BdTDbl8ljR8uSLU25yCfXg1mvDS36SRO7yRCuu9wiI_oeYsa62vyzQTTPJdYpbQ-s9b5KpjnVmzUV8ufX3gn6bkWGtSaNLUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به امید بالا رفتن قیمت نفت و فشار به ترامپ، زد زیر تفاهم نامه  و حمله به کشتی‌ها،  که با اقدام به موقع دوستان خودشون  در حزب کمونیست چین،  نقشه‌هاشون نقش بر آب شد!  خدایا عظمتت رو شکر!  اما در عوض برنامه آمریکا در پاسخ  به اقدام جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6518" target="_blank">📅 15:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6517">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwIaN6o6q6bn-9uCcTMpR8mSdg1iA534mGRYSEAMaBCECUlM56XZ-5-T7MIEcKMn0yLAKu_rDAifejaKLpSXmV7McjFxdugTAjTw4dPNNNvWBXO13e4biRch79ZuCtzuCiayZwLBKw7Dti9prwrY6TYmf1lyMv_0mFYxO4VLY6Mh7MOe2ckcm_WboY398ZfqBp1iznxOfYJS7ZT1lw5uoW1t01dcuFqaGBNhfbw0aI8Ogv3o2Q3I4OgTbAoKZHruJ8WbEveaRpQ2-NsNvRGr9ntTj8T072dMijFdLQ_jVyzGMWHb49Q-HEO7iOS4J2OPjb59ja2wSNYFtyG6WREocA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم : افزایش تولید نفت کشورهایی چون امریکا (که رکورد تا یخی زد)، کانادا،  برزیل، قزاقستان، ونزوئلا و….. است!  نکته سوم ترامپ!  و به نحوه مدیریت ترامپ برمیگرده!  بازار نفت به شدت حساسه به اخبار  و به انفجار و ناامنی و جنگ و…..!  خیلی وقت‌ها قیمتش «روانی»…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6517" target="_blank">📅 15:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRiInt98MsxwvNr7uVxgWJUBuPZOnpcnYgUUcRXoZNF2PURZG7dJUCvB6NWKz8RyOyrl3GgRPt-p-bHlRG8HGgxXTIzlOUCNCSHrA2qD8ohFZk4Xv3Hg6LV7SQIVAh0z4yOpvAZqayduz8ZBdmyiBU86jnumMZU89sNhnwzPlz5L9clF549E8gMl-GXfOPiPcNXWYo4g3UYZCfbcGFwYtZVT06RSa11IpRDKnwxG40RvonMyF51cQur4cxMRRgLsOzLzwIodg9n5GUMrAM1XHm06IB74vLAy9biH9Az5CdXVZGTANCDbsxBh6LfQ04XxcJa8tvFOZN59sj_b3zO93w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف نقشه‌ها و آرزوهای جمهوری اسلامی  قیمت نفت خیلی زیاد بالا نرفت!!  میانگین قیمت نفت در ماه اخیر با اینکه هر روز خبر حمله به کشتی‌ها رو منتشر میکنن، اما بین ۷۸-۸۰ دلار باقی موند!  یکی از مهم‌ترین دلایل اینکه قیمت نفت خیلی بابا نکشید دقیقا  «چین» بود! …</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6516" target="_blank">📅 15:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BZOd5cb83U6H5HSsLqWjepo3SgyQUS5toG0o1jtX09pyKd9imRC_6SS2T5SfzI8ULqj9ZT0oG5lC5KE-l2Oq0KBsU1pjaZg6y_ttBrTjJOsFF49b5vQFnoOD1CGQcPYrp3o-AAqlL-6yu59DhMQZUA8SZkCQMfFN5BrjKQ9bGAHNW1gClLRBJfij6sroVvf5_xM_sO8jbv7l-LGdNMqTWr62lP7nkYdaMPNiUH_VRmgaSWJGsA1w7fe4Yjsag_1k2L6i798ol_Qt7CmaLMcwEuRurrvE0xbNg8EFX7HzpMOPoOaRlziUuicilUG4QnOCPgj1uYpo4X__kXXadY8EpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A5_NsLJY10WqwGbIRODHAiqJAunuy-KNYma1idetQw0T7dRh9SokxSqIgCwT5bRaRA0xBCnZC0ac-HMw9dIoC7Gpdtapjx2w1aQclKEamZGMUz5koep6fDlEX2mWbYqooOROpeJyINA0EiayIqYZZVydFpoo3uUyFELkGt6AAkB5ITXTLtdVI6f-IGwqfbiqMTKK6iA6AD9H5vFmW7EGE4xvWPxxhfv0_jOn3XX5ZSAEIXL-41OhT8xOB-4iu36RWU4afOXwRG_XY0df-IF1b7AmcFplguzQkCK2cqd4nt10dDI1lFLipcs9iCmxpFV6k0CZMoOVEh_79aCYvOLU0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جمهوری اسلامی با امید به اینکه با حمله  به کشتی‌ها و کنار گذاشتن تفاهم نامه،  می‌تونه قیمت نفت رو ببره بالا و بر انتخابات داخلی آمریکا تاثیر بگذاره،  حمله به کشتی‌ها رو شروع کرد.  تا با ارسال پیام  «نا امن بودن» تنگه،  قیمت نفت رو به شدت ببره بالا،   حالا…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6514" target="_blank">📅 15:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.  اینها دنبال «اتفاق مبارک» افزایش قیمت  نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.  اساسا با همین منظور شروع به حمله  به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6513" target="_blank">📅 15:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=Irsa2RalaRUN50JqofwZZ4JF_KAoUlFjWBfOanwilZuDSAieHpxcOvNr8BHo2I_rDIAd_ZdbkDf4G6AA0UKFMKNA9XxmI54jDwRd2tz2vh9zbcspJayr_yb8I0puHYkHdg_GfwI1OKZmONkqV8CMHmUYYEd4VRIMPzdzREnzNcAfcSpywYboH_VmHRmfeSgG9d9JWqLbuIZwQJi5cHL4Jvc7Rlhk_x-m5ZU23If0a5Gztl70hX3RqIE22wd2iwkGuj5E6tdLsWs48PPx5_KgsxpagguK3VaB397rs43L5WB1_4s_Ek6_1V6r3Nafj7KK8qlCKfG0cmqjMdpGDjwczA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=Irsa2RalaRUN50JqofwZZ4JF_KAoUlFjWBfOanwilZuDSAieHpxcOvNr8BHo2I_rDIAd_ZdbkDf4G6AA0UKFMKNA9XxmI54jDwRd2tz2vh9zbcspJayr_yb8I0puHYkHdg_GfwI1OKZmONkqV8CMHmUYYEd4VRIMPzdzREnzNcAfcSpywYboH_VmHRmfeSgG9d9JWqLbuIZwQJi5cHL4Jvc7Rlhk_x-m5ZU23If0a5Gztl70hX3RqIE22wd2iwkGuj5E6tdLsWs48PPx5_KgsxpagguK3VaB397rs43L5WB1_4s_Ek6_1V6r3Nafj7KK8qlCKfG0cmqjMdpGDjwczA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.
اینها دنبال «اتفاق مبارک» افزایش قیمت
نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.
اساسا با همین منظور شروع به حمله
به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6512" target="_blank">📅 14:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.   خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.   او همچنین با اشاره به اعتراض‌ها…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6511" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=HswP15lXM2YUdv9QL1XZvuK8ZCRacmE2A5u3Dn-VmiwdOpFIergXXXMqNFX5clo_n2LjxSocKORUU9-bUhjsLrNhYWSZptc93hkF2fOE3Dy0pDU3_qtKbIw_Thu8FMdF95CKe4uYoBTGpwFEYYe8TdHHyse4YQSR0F-V8_4DUmWd8gJfOpSCTqzbWSGFaBNxdaodbv0Tj42trRT-Iwz-OZe0DCUeNWqiwd59ap7l-FAWidbIXMs5X8L1YMf0Jt1XjPp5fL9MjHEOZGiwiWc5awHZi-SXoH1hni5hSFEBhroW1Em7reISgJStR3ygCuzapVQQPhqHR-TQju16B770BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=HswP15lXM2YUdv9QL1XZvuK8ZCRacmE2A5u3Dn-VmiwdOpFIergXXXMqNFX5clo_n2LjxSocKORUU9-bUhjsLrNhYWSZptc93hkF2fOE3Dy0pDU3_qtKbIw_Thu8FMdF95CKe4uYoBTGpwFEYYe8TdHHyse4YQSR0F-V8_4DUmWd8gJfOpSCTqzbWSGFaBNxdaodbv0Tj42trRT-Iwz-OZe0DCUeNWqiwd59ap7l-FAWidbIXMs5X8L1YMf0Jt1XjPp5fL9MjHEOZGiwiWc5awHZi-SXoH1hni5hSFEBhroW1Em7reISgJStR3ygCuzapVQQPhqHR-TQju16B770BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.
خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.
او همچنین با اشاره به اعتراض‌ها و تجمع‌های خیابانی گفت دولت مسعود پزشکیان به پایان دوره خود نخواهد رسید.
@iranintltv</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/6510" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajxTNXJ5Q5EBWgtS_38_LOxqjjXQ7ri7GnI7Fa_p2J9kxzRfCmzaGPZzjoyTSrrQMH8wbTdwLZOjV3ox2sDxnig_X-ysZii0Hsjngg503tKbMfq_Kx2OrdsVOkXiuM_1PmMKlJ5T6sObnvzxsmI-goP9b8dbKJ_UwHl-xQDJGX8_En_W7LomB7Py-7JDzdYP8p0rO02wH43tj6ux0kPWDINXwoSu4AmuCO02OQs4It0gLm7mxS2OmYRifcm6sMdAyHqLxVZC3m9Uir680iFJmugJ0I8mbZKX6G3PZkITUbPpB04d0x7MHACWAn4FqfOkP8I4qaO6iwtA-xNq_QfQXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب PD که همون نسخه حزب دمکرات آمریکا در ایتالیاست،  هم چند هفته پیش، چند مسلمان بنگلادشی  را به عنوان نامزد خود برای پارلمان ایتالیا  در ونیز انتخاب کرد!!  که آشکارا شعارهای اسلامگرایانه هم میدن!!  مشکل ملیت و مذهب این افراد نیست!  مشکل اینه که اینها آشکار…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6509" target="_blank">📅 12:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5B4eB3hEFR5kGJirn8_qpUdY29Og06Vgks3eaNULtfm1BblQwD9-WjNOlN3ktUr938vhHscJCxJRMNl_3BBaYS8ZWOBUWiHWEd0rt8YGTd-A63mdQbo28RBvdM9PMkIm9yEo-M_6oekEjShnDWor60tMcBg7N3cXZuDgbqzt6bxgHWsvUyiqkPAxNZ7DTFtJ63VBIoWVFVOF4fCv5SEu_cu5L9OcUCvcnJWzIqJ3eN_65mCpFox8wNXkPi9enEDcj21ofS1T2lgqOINjHid_fJ1cNHV8-rjyatHHiWeAClTltdFQo9S25GW3ewnPPyaaovNC3FtDjMHhZPbBqsi0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!  که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6508" target="_blank">📅 12:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6507">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=j4wjnq8tst1kGATa88cgY7T-NB7bHtiKGiYcjljV_fePaLOWuWP_0lmbdamNJt66zIHm2uBH4B0HGlKUMmX1qdAApLRsn-6ByDpzMDt1XbrqRCC_0cgc2fDuEmq5-Y_1ksQhW_mRpR6gl37AcHW6qQtXTwauhkH44bXYQAfcnvyG73TzfmSTDnnIrRQcKv5SdVBEHktBiWiuHfp7nUTQkJehB3_AjRSJT3eG_mH1Ywwri0MiUZS39yGD76ysfgQvEgyedIHR-Oaj6lHb38ep7RxVUkOEcqO0pX_nLJZS3ift75IEH98TugB9Uijw4PfurBrX2l5qLf5eAfyUyW8svg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=j4wjnq8tst1kGATa88cgY7T-NB7bHtiKGiYcjljV_fePaLOWuWP_0lmbdamNJt66zIHm2uBH4B0HGlKUMmX1qdAApLRsn-6ByDpzMDt1XbrqRCC_0cgc2fDuEmq5-Y_1ksQhW_mRpR6gl37AcHW6qQtXTwauhkH44bXYQAfcnvyG73TzfmSTDnnIrRQcKv5SdVBEHktBiWiuHfp7nUTQkJehB3_AjRSJT3eG_mH1Ywwri0MiUZS39yGD76ysfgQvEgyedIHR-Oaj6lHb38ep7RxVUkOEcqO0pX_nLJZS3ift75IEH98TugB9Uijw4PfurBrX2l5qLf5eAfyUyW8svg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!
که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده
و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6507" target="_blank">📅 12:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای : پزشکیان ۲۸ بار استعفا داده و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6506" target="_blank">📅 08:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ilmdg2li5lAFG8jmsJa5jXjGR6mMfCwBqIZmEPTjKVFProEkFmtqzvAY8wZcnbkScMrtGYOHkhYZ6gsNuzg-21yf1yjnoafcVKMdVqAkoFvTnLwrRAurDpPnUD81bICLe_2BQQALVnrTAe2o-K-zvWXBWP07Yx2Nqyqn10XKZVkpC0mYQ2QwgPLltt0q57bEkflyy7h3maLA1WO695A-P2RXUosrtHMpL4-zyWWXVhUqO02uYbiPiOr5zqEBK_6g-Fdl7sbMLqh_UTHWM7MUkKQWxyg-n4p6V44B5fRq2YoRQp9l1Oxv1t5SeK7yAF0KaHb5kobr-DHbnI6hgonCjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توطئه است!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6505" target="_blank">📅 01:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">آسوشیتدپرس: مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6504" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBBCPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3nO9YflzmMUMdXN99oT98Yt4kG-utQ3O3sNudvjRNG3QlGkQ3l3PIeVxyc3qiV1P7Tp7scMpShuQIIIKtAKRafnAkQVth_ndyKV3voIbp3VWMipCrdKoare3iDGQYnCq9k97vCCJt04tb3zSq_NACm9rLKqg4DvZi1bkW7I7XL3i_vT79xvf6K9H3dCqzeUxS-I5jkW4StczVUHkn27ATlneg8SG6COTplupkfL1eLb9MEsiJen5Xkwv0pvijupl-WdtKVY4BLlVcKiOlPB_AFlMN5lb0OV3bFRnlHiveM-2rU5iPDs3X5DGlOe3tyK1SQ6ddvMkW647GR5umGyKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔻
سازمان عملیات تجارت دریایی بریتانیا می‌گوید یک گزارش باتاخیر از یک کشتی در فاصله ۹ مایل دریایی (تقریبا ۱۶ کیلومتر) از بندر «مخا» در یمن دریافت کرده است.
بنابر این گزارش، یک شهپاد به این کشتی در دریای سرخ برخورد کرد و باعث آتش‌سوزی شد اما خدمه و کارکنان همگی سالم هستند و نجات یافته‌اند.
به گفته این سازمان این کشتی اکنون غرق شده است.
جزئیات بیشتری منتشر نشده است. ساعاتی پیش حوثی‌های یمن که همسو با ایران هستند، اعلام کردند که با موشک بالستیک به یک نفتکش سعودی در دریای سرخ حمله کرده‌اند.
این هشتمین شناوری بود که از زمان آغاز محاصره دریایی علیه عربستان سعودی هدف قرار گرفته است.
سخنگوی نظامی حوثی‌ها به زمان حمله اشاره نکرد.
📷
Getty
@BBCPersian</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6503" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f29785e012.mp4?token=GIMT9fRHPLwOeEhz2uBVQBTRpvotyREIu99OK2ceRFTR02CuljRV1_l-ebLYlz_pJnFSU602cGExW87wBw7B_G609uSMGlAdQOALe69d7rGDy3R7HZU0j8GQAl7OCe2ae1-dBEPYHVTylaL9BvdDOzZRcAoKLT4c86pVMGRuzhgcoP127ws2OXlSYVEwVnNoV8_dlNRL2cUas6g1Cf6CVx5xwjIWbZ0wFlWlJrfHafRsN-Xew7H2rpnHoWOjd-kBT3yQ6Lfmodi3y9lzx91mbo-rsZycWmM3AU2IH2xnIikOHroilAMK2CYHxHaxxg_6tWNlgIq-z0GGhEf3tMbPuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29785e012.mp4?token=GIMT9fRHPLwOeEhz2uBVQBTRpvotyREIu99OK2ceRFTR02CuljRV1_l-ebLYlz_pJnFSU602cGExW87wBw7B_G609uSMGlAdQOALe69d7rGDy3R7HZU0j8GQAl7OCe2ae1-dBEPYHVTylaL9BvdDOzZRcAoKLT4c86pVMGRuzhgcoP127ws2OXlSYVEwVnNoV8_dlNRL2cUas6g1Cf6CVx5xwjIWbZ0wFlWlJrfHafRsN-Xew7H2rpnHoWOjd-kBT3yQ6Lfmodi3y9lzx91mbo-rsZycWmM3AU2IH2xnIikOHroilAMK2CYHxHaxxg_6tWNlgIq-z0GGhEf3tMbPuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اثر یک انفجار در جنوب لبنان ۲ سرباز ارتش اسرائیل کشته و ۷ تن زخمی شدند،
ارتش اسرائیل دست به حملات توپخانه‌ای زد
و سپس دستور تخلیه فوری روستای المنصورن را صادر کرد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6502" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6501">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=g61sK_y97EyY-pa0gIjmQ3kIZkj8yJDOq_EwLCsoduzAoW9-O4VGXAhiVIPDyQcjCQp2VSnPaqUtPPLG49K-zdBVCINguBjUsbi0NwMxqq2wVTAPB1KUXDHnc_OARbMQp-7lWnDcb_zB_O6UY2n4iUAbpyrKwyEzNJdZn68Ds9EzMWIj0ViwODUzuNNJVykNoc68XCdrh_DbcWubRsIzrJ8v0kwRZz5u3hx-C2KEuglA6HUYQYFpgFvf_vsaorhUIOn5Xm9-0eHL8Ae3h5QWfrlLWX9MmIVxulU7kmpif7Fbn-7nY02sN1lbOAI_2idsMdDhsU68OhcVrjSLfJ0Mbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=g61sK_y97EyY-pa0gIjmQ3kIZkj8yJDOq_EwLCsoduzAoW9-O4VGXAhiVIPDyQcjCQp2VSnPaqUtPPLG49K-zdBVCINguBjUsbi0NwMxqq2wVTAPB1KUXDHnc_OARbMQp-7lWnDcb_zB_O6UY2n4iUAbpyrKwyEzNJdZn68Ds9EzMWIj0ViwODUzuNNJVykNoc68XCdrh_DbcWubRsIzrJ8v0kwRZz5u3hx-C2KEuglA6HUYQYFpgFvf_vsaorhUIOn5Xm9-0eHL8Ae3h5QWfrlLWX9MmIVxulU7kmpif7Fbn-7nY02sN1lbOAI_2idsMdDhsU68OhcVrjSLfJ0Mbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی منطقی بود!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6501" target="_blank">📅 12:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6500">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=WaZZcSxrSMNXOQNgGglbj_JI0oQb6U88sL1-ikfKNJHqjfUdvL5k5unGIAFh4knLouKesx0tR89RekTKn4nKKaKhwI5DEVd8gl0o5cdIJUH3GwowLOKklFjJ_6C_aBFkhkKuf9B6XQ8jVywT_T6E6eSA_Ix2OksXay_B3fUcNNvjAuWT5Ta_vdrZnbRGrMS111tRvhgGBQKkAG6FhuMYq6t4ici216r4LsMtMzJGIDq3y72U3TnVphLWyyu44hbsAnC_fq9tyUC5QqY9Y8STE7hXnPo3ZUQcWZfgEg9OybgnBy3qpJzoajrSsgect6vtKr2gO0FuID5NsZNDL5-uSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=WaZZcSxrSMNXOQNgGglbj_JI0oQb6U88sL1-ikfKNJHqjfUdvL5k5unGIAFh4knLouKesx0tR89RekTKn4nKKaKhwI5DEVd8gl0o5cdIJUH3GwowLOKklFjJ_6C_aBFkhkKuf9B6XQ8jVywT_T6E6eSA_Ix2OksXay_B3fUcNNvjAuWT5Ta_vdrZnbRGrMS111tRvhgGBQKkAG6FhuMYq6t4ici216r4LsMtMzJGIDq3y72U3TnVphLWyyu44hbsAnC_fq9tyUC5QqY9Y8STE7hXnPo3ZUQcWZfgEg9OybgnBy3qpJzoajrSsgect6vtKr2gO0FuID5NsZNDL5-uSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمان مخالف اینه که از کشتی‌های  عبوری عوارضی گرفته بشه،  جمهوری اسلامی چند هفته است عمان رو گذاشته زیر فشار که باید بیایی با هم این کار رو انجام بدیم!  عمان گفت : تو توی بخش خودت اعمال کن!  در آب‌های سرزمینی من، رایگان خواهد بود!  که خب جمهوری اسلامی فهمید…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcEVoAL0U8v8RjMS_uSxkJEzWcIXukhcpR4Ct31aPdVXL9KFvF6kcurXZZyA3_7_DmnKPL2NBhDba_3yucYo4Tyc4Y3WmDHE7rA1AihIORVASDFGoMogdmg4V3BiyYC4yy6pi_apto7UOSfW3Fb9h6e3my9Ef2YeYxgPuwXh0_XgJ_YElKfOk1rhoNpcovZZUUG129smS9baH9sF3iTJFJCkGnejHetDRdd6xkxfLzsa7o7hY9j8U-Um0GrxcM8Fy5dNpkzxc83yigiVYP0f7b3hf5GfBWGiKkENLwaaaridIU6yybPQf7CcG9Yfn6-5iqzmYrl-rz0UvjHnOaurmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMzOB-QhR6I2CQB_QGnYa-zwaEXhTOEiTnehb6V3u-AJHlbyLtrGiZq2AfchWYDxwHHvoZhRhHN2GLIGZA7uipUt-os6DYrq-SiM0rqurnubgbw3IHmCGRuYB6Ga1NPhZRVo3YXDA0J5COGq6oIAgDpuLVYG6CB9-0ybehRyjAHEovB-Im6XIDQ8cWJSk8T1OR37leZJ8kSm5E1OFeOjjn8r3S_NJJagLsTFD_YUvDadzg7pkCVlKQhGN8hLDsVOZGVygrVZvVtCI9eSLWPKehcJy4PUZ2M9HPCY61pTfI0PAxfnwAhZXmu3mxy3VOpgneznIi4mZOdzVweMAJznww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5hN01yy2xjUWSXmwi0i3NHZNOESqHWiypsxtWK3wP5EgD4JH_etdv9IcmSw5oxOhp4IwmKB_5jiCEVKKEQSC6HkUxbtheGoWcAIoJgzLRIEPwf3t7-8t8lIF3Ecih1XhqNDnLW1K4cnrIYKS9nd6alCidX92R7HiA4PUJOwvsbx5Fs9ILn_ZB1ZbV66yzwSv6kGJCKJsbYOGt7yZ27aZVGyBNHQL65LO9876X22fsaDSvY2W3rS3SJFVVhLifH42SHvzPSFrz-hOnvchuPByJ8KBcpralBslXE9j6eLeuox8QZSu_XdRl6oNUTqCnJfdSGAWcEA2P21gI4CXEb9Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.
عراق : از طریق خط لوله انتقال نفت به ترکیه
کویت : خط لوله به عراق و ترکیه و همچنین به عربستان
بحرین : از طریق خاک عربستان و‌دریای سرخ
عربستان : صادرات از طریق سواحلش در دریای سرخ
(همین الان هم ۷۰٪ صادرات عربستان از دریای سرخه)
امارات : دور زدن تنگه و صادرات از  خلیج عمان)</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6497" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6496">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=KBEp8A06NkZwvEcWdlKX3XVrP-gyvi0r4l42utscsOdS5WmlBWe05ir-Ok93iN7OmxptbIEdRaZmVeuxDLHYBCZVlW9rk8f6J56LJojT45QMokVqrNciAeSCdks0g_BLiFOHuLnSAq07-Jt77Vz4RGTa6yW8uFarIf6IGkeGseQvdFQB6unMaYhuEyG0CvPz3lVMrdiROQoKpHPPAgruwBj1NgS2ZMT2mmInO0rbXJ7phzZaVmWmaWwRrO46xV_UyiQ1nDiMk-7iMlM0yZ9kBiApEOPxo51_hhkVfo2G5KM7CZPYL-l-l4YRuYAuVy7RWiV7L8VZF_Bfu5boII0y9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=KBEp8A06NkZwvEcWdlKX3XVrP-gyvi0r4l42utscsOdS5WmlBWe05ir-Ok93iN7OmxptbIEdRaZmVeuxDLHYBCZVlW9rk8f6J56LJojT45QMokVqrNciAeSCdks0g_BLiFOHuLnSAq07-Jt77Vz4RGTa6yW8uFarIf6IGkeGseQvdFQB6unMaYhuEyG0CvPz3lVMrdiROQoKpHPPAgruwBj1NgS2ZMT2mmInO0rbXJ7phzZaVmWmaWwRrO46xV_UyiQ1nDiMk-7iMlM0yZ9kBiApEOPxo51_hhkVfo2G5KM7CZPYL-l-l4YRuYAuVy7RWiV7L8VZF_Bfu5boII0y9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
اگر استعفا بدهم، رسماً اعلام می‌کنم؛ استعفا نخواهم داد و خواهم ایستاد
ما با نیروهای نظامی، کاملاً هماهنگ هستیم. می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و این‌ها یک چیز دیگر
همه مردم برای ایران سختی‌ها را تحمل می‌کنند!
[تحمل نکنند هم یا زندان یا کشته میشن]
یک عدد سه هزار نفری را سی چهل هزار نفر گفتن، نشان می‌دهد که این‌ها چقدر نامرد و وطن‌فروش هستند.»
اونهایی که به قول خودش بین ۳ هزار نفر رو کشتن، نامرد و وطن فروش نیستن، کسانی که به کشتار و ظلم معترض هستند، نامردن!!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6495" target="_blank">📅 12:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">جزئیات تازه از طرح تغییر رژیم ایران؛ قرار بود کردها «زیر پرچم شیروخورشید پیشروی کنند»
🔸
یک روزنامه‌نگار سرشناس اسرائیلی در گزارشی تازه نوشته که هدف حقیقی این کشور از جنگ ۴۰روزه با جمهوری اسلامی ایران، تغییر رژیم در تهران بود نه صرفاً نابودی برنامه هسته‌ای و موشکی‌اش.
🔸
نداو ایال مدعی است که ساقط کردن جمهوری اسلامی در حالی به‌عنوان هدف اصلی تعیین شده بود که نقشه راه حقیقی برای عملی کردن آن ترسیم نشده بود؛ تناسب این هدف با امکاناتی که اسرائیل در اختیار داشت به‌طور عمیق بررسی نشد، دولت بنیامین نتانیاهو هشدارهای ارتش این کشور در مورد مخاطرات این طرح را نادیده گرفت و به عواقب آن، مانند آسیب به جایگاه اسرائیل نزد آمریکا، فکر نکرده بود.
🔸
این روزنامه‌نگار در گزارشی که روز ۹ مرداد در مجلهٔ ضمیمه آخر هفتهٔ روزنامهٔ «یدیعوت آحرونوت» منتشر شد، جزئیاتی را از مباحثات کابینهٔ اسرائیل و اختلاف‌نظرها در میان مقامات ارشد سیاسی، اطلاعاتی و نظامی این کشور پیش و پس از جنگ‌های اخیر اسرائیل با ایران ارائه داده که خود آن را «اطلاعات تازه» خوانده است.
🔸
گزارش «رؤیاهای بزرگ؛ افشاگری‌های تازه دربارهٔ طرح تغییر رژیم ایران»، نتیجهٔ «یک تحقیق جامع» نداو ایال بر اساس گفت‌وگوهایش با ده منبع نظامی و سیاسی اسرائیل بوده است.
🔸
این روزنامه‌نگار مدعی است که تلاش او تصویری دقیق‌تر از پشت‌پرده‌ها در بالاترین سطوح امنیتی و سیاسی اسرائیل ترسیم می‌کند؛ فراتر از ادعاهای پیشین که دو روزنامهٔ «نیویورک‌تایمز» و «هاآرتص» در ماه‌های گذشته در خصوص تلاش دولت اسرائیل برای تغییر رژیم در ایران و جلب همکاری محمود احمدی‌نژاد، رئیس‌جمهور پیشین، به‌عنوان یک گزینهٔ رهبری منتشر کرده بودند و به‌شدت بحث‌برانگیز شد.
🔸
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از بین بردن برنامهٔ هسته‌ای و مهار توان موشکی ایران را هدف‌های اول و دوم جنگ ۴۰ روزه اعلام کرده بود.
🔸
نتانیاهو اما از آغاز کار پنهان نکرد که هدف سوم جنگ هم فراهم کردن شرایطی برای مردم ایران است که بتوانند کار حکومت جمهوری اسلامی را یکسره کرده و اسرائیل نیز از وجود چنین رژیمی که نابودی این کشور را عملاً دنبال کرده و با تشکیل گروه‌های نیابتی در محور موسوم به «مقاومت» در اطراف اسرائیل «حلقه آتش» به پا کرده، رهایی یابد.
🔸
نداو ایال گزارش خود را حول این ادعا نوشته که «تغییر رژیم ایران» هدف واقعی جنگ بود، نه یک خواسته فرعی یا شعاری تبلیغاتی.
🔸
به نوشتهٔ او، چنین هدفی قرار بود بر اختلاف‌نظرها دربارهٔ ماهیت نهایی جنگ با ایران در میان مقام‌های اسرائیلی نقطه پایان بگذارد، در حالی که برخی از مقامات و نهادها همچنان خواهان محدود کردن جنگ به اهداف مشخص و معین نظامی بودند.
🔸
نسخه کامل این گزارش را در
وب‌سایت رادیوفردا
بخوانید.
@RadioFarda</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=NTucoupX-odC4aLBJwjrYzjIJiqOwK-GghhAQbGJjZ2lmmoWsuLBLn201xpEi4p73nH2OY1fD5791n8SPwYk5rhQ5xvtmo2iJK3bOcCqt7X1MNDwHfEB4-T8WvfE_qV3f7YK5I_utayPqkGjAVvV6gqbmdyrB935vEV1tISBOm3-A1i-WokSu2twgFhQ-cxiooQBjoGqyS6gzeKmZYOhfsXameZeEi8FSpfmQSYYWDB3vpoxoVcI637OP-w51254kbt69bOI4mbAR6EhNkrNSgX4TPSA23dEMKijrQr0KYIU-ZxwVl_aBTSJrSefEbTJsVV5nC0Xi57b6hROmUdt9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=NTucoupX-odC4aLBJwjrYzjIJiqOwK-GghhAQbGJjZ2lmmoWsuLBLn201xpEi4p73nH2OY1fD5791n8SPwYk5rhQ5xvtmo2iJK3bOcCqt7X1MNDwHfEB4-T8WvfE_qV3f7YK5I_utayPqkGjAVvV6gqbmdyrB935vEV1tISBOm3-A1i-WokSu2twgFhQ-cxiooQBjoGqyS6gzeKmZYOhfsXameZeEi8FSpfmQSYYWDB3vpoxoVcI637OP-w51254kbt69bOI4mbAR6EhNkrNSgX4TPSA23dEMKijrQr0KYIU-ZxwVl_aBTSJrSefEbTJsVV5nC0Xi57b6hROmUdt9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای :
پزشکیان ۲۸ بار استعفا داده
و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a204c96911.mp4?token=sHgPiT-0lSv89xGH-sxWzDM47Yitq9Zz8k4sf_z-w9Ti1JVGOqZbKF9cdMkbMP24xxtbI20uwvbWJJh8JrUe7qXnI7HAUfJnKiEHZAKh-inQGzsZ2cyOJzIzT4l2un8bmHrDA3rQjTWQsjf2BhxQarNPAtIhmRO__Gi3Q7GZDtm6A5MBj3ekSNMuAGOtqgQxULAl9gGuMSjFyW7oYjaSV3pttpqysmN8AvIFajt5oKY0Atlvol1t1_ZBNKY4JHZikSFhBQJjWbDhyQ35PNM263kLqSCyEspTMcEh9aLEDieFMFh08T0S4JJIgBMgdAIuBWZZCl8zFXI5Sdt_sDWpwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a204c96911.mp4?token=sHgPiT-0lSv89xGH-sxWzDM47Yitq9Zz8k4sf_z-w9Ti1JVGOqZbKF9cdMkbMP24xxtbI20uwvbWJJh8JrUe7qXnI7HAUfJnKiEHZAKh-inQGzsZ2cyOJzIzT4l2un8bmHrDA3rQjTWQsjf2BhxQarNPAtIhmRO__Gi3Q7GZDtm6A5MBj3ekSNMuAGOtqgQxULAl9gGuMSjFyW7oYjaSV3pttpqysmN8AvIFajt5oKY0Atlvol1t1_ZBNKY4JHZikSFhBQJjWbDhyQ35PNM263kLqSCyEspTMcEh9aLEDieFMFh08T0S4JJIgBMgdAIuBWZZCl8zFXI5Sdt_sDWpwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تبعیت از ولی‌فقیه بر مسئولان واجب است»
می‌دو‌نید شمر تا آخر عمرش
از اینکه در کربلا شرکت کرده بود
هیچ گونه پشیمانی نداشت!
شمر خودش از فرماندهان ارشد امام علی بود!
توی روایات اسلامی هم هست که
هر بار بحثی پیش می‌اومد دفاع می‌کرد از کارش! میگفت  تبعیت از حاکم اسلامی بر من واجبه !</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6491">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=dxOQuICfeDvHTyQewjaZWEMX5BGPoEgDND3ewLeCzXkFmjpIt3XVIvnprU6-uxGjcWqsuPyNWxuqam0bznlj0lXC01E7GBHfdbUA7s-Umf2qOXRV45AF1-3H5r3TjDpca9attWtho2eWdglLdFEf-mfv_SikoH7vmbAe2yTFgerTNaQJ07I6Z_FMkEpY43xstySrsKzjvIA1BiXujbw5W3hQEeN4n-S9Sjov4drBUZeOENvRGDwaSXSEDbE2Ui6KyxwyngEOATWCeJMZ4vYyWOeb6oK3ShKF0ZqVeblhMIAyEQFsEff_lxqArwafClmgLpUap3rNMxzOq5iOTea4zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=dxOQuICfeDvHTyQewjaZWEMX5BGPoEgDND3ewLeCzXkFmjpIt3XVIvnprU6-uxGjcWqsuPyNWxuqam0bznlj0lXC01E7GBHfdbUA7s-Umf2qOXRV45AF1-3H5r3TjDpca9attWtho2eWdglLdFEf-mfv_SikoH7vmbAe2yTFgerTNaQJ07I6Z_FMkEpY43xstySrsKzjvIA1BiXujbw5W3hQEeN4n-S9Sjov4drBUZeOENvRGDwaSXSEDbE2Ui6KyxwyngEOATWCeJMZ4vYyWOeb6oK3ShKF0ZqVeblhMIAyEQFsEff_lxqArwafClmgLpUap3rNMxzOq5iOTea4zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ep1qoYzIZIfGGqUDVbYLvW6fxqRXy50KDnnnAe_ruk5Lo3ooKwuuasjtA4NDtyeBLFSwc7QpUrZfcpPz66lH_0Len-8ALBvb1ZxR-S9gZKSXjxwtYZKJZdnSjdA0ecLS2qduclBNsm6Ntmtj0lhSfJxmshaVMSJ1zUSsKhaMtSnhw2HTcTuNsBSuM-ENdRXeyvPlcbOD6X_Kk6sifqg2g-bshkVhtqoc_XEkZDaq_U5Bu-_6HEhPnn5RNp070DoXuLun6EciM5Xbo-AYtnxKcrovJ07LwKqsF6NtmenCzucLldYbNZfDddCfxlgFrSzUNtu9ybElqzKKvWELO9Ze0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCCvOIsIAAgyO6cNv5Vrju3dsRiWhgMCwzbeswVckbtDjMCu_RNVJpXdQQK-ERw02OwZFE_7mZn4aoJuwXgB3udYuGAtC2xNEvlNeNd4e_SQ15G3znIo7AdvN_t9WIj2iI5o46-nTXq_vrQqoM6TM1mUIMS9HuNG92Y4NdCieh6BKvY91Ey6BvTVRv1Yygf6Vrs_ktaO0zZZ19pX01TxPmxeAEadtkNlZln-WOF9Cc9PCvf1omJ5k4nZTQiHrx2-meDrKDh3cyF9s4wj8Gnsidj4nopzRIHXTulQg92gdis1Pa3sQJkfYo6HFUBFBdXP-_wsifKNLmP-uTob36yydQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U8vRE77X5aYM8kuNSANTuIv5S9zi5UlUj6FzmMVSEqdgSmmj66phK0xFW_-hue9fKchUmlKfFwUhulszixcaTpOIRV29zQK7brhNauUdLTnu9sPUr-Jxbv6u960NuoAKc5OlgNkhnRjH5JRXs-6fiu6vRtCv-tkdQCVrDnTbxNsqrzg30KWRuKaioAnWeNLECO5iWtTmDqHuyIWxGogyMKFJdHAsIV7Jt24HZpot-cS7C1lyjsFOZpvlvQe-frtK0C_mRjRy539DtHFtsxwvBwOucVkIYmKTS6cJVG8cbrqwabWOvCeyQY87HGwvfS4X8X_fqqfh26xX8iQ8Huzd0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPkJoYE8G2HHeVw2gNwrt1tmkf_n0z4Qm6gFBMhIky8zjFd774X2ZJgP983GKWONJR1ac64KkS7IHNK39YuoObnClOy-y2nwCG-_gskAXcVHoJFOoxzPOtEFFXt8UTxsqutB4vmJG57MgDRIy075DuG6TLRpJskjS9OJjxg0SBN-AayBwT4QzZEvaf-wXROPQKuT-_Cps5kKRRpYM8AcRH_FDoIdLIjjST-LOrGVWHoqL3QS3jvgfbVOf1LceDg8FYkxDU5PpTJUUrKufYiVoTKpVnTHjDH1Z2d6SFKiTZAbqOYFHjj5lxUX9MXgUvEjspkDBsUBfPdJkDCKZhIQ8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thmvIvykxsC6Aom4liUXDTl93JrECk5TU3sRlk0olxda9SA2ltOL_srWe8fdGzE_YZ7aSHfeJWAU77JmX46r-5BWTGQ4vqBa4usHsczWpaLCvGvnQx77x36w3lChUW6PX24Zi2i_gvgjIxbSNA0N0j9aCoWXvyAQh1ig8Rj8c3G3iELm1EUueRzeZYnJAcDE8G4E_2Ywmm66vE5LWQSvi8O4VIVi6JSfGXzaMLO7VhtF075gZ_FTzEre7lnUftw7DKh4Auic_VE_-f0zdJqsxMI78ZDmh0It1Qwf3R_3Ao9lwNcD7rmO9Ml6quQMKKbkMxMGcGGpOfDu4p0MAQToKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDdE9cR_ZewPWpcqb7_yefyTzQ_iFKy8InzQWezk0JXx4lywTUn00v58WgGvauuc-4Q7MHxchGp_AP0s_PR81J532aEqRxZxGXoFtOtmVtb0mKcNo2IdfnUUoRxe_HNHSjwjmgHyguVjBj33ljvN8HPCouzQ45S1NkRo4jK__4pr2YHESRqzEeLU6-kVP_7SBfdYbxFiIx3WAUhMilkoljtarDCtUyeVMkVDCUEKDGw5sq5Thld9JuIpNsTNzCu8UTEdrOrtyrsR8w3KGVw_FXPmll8AlBRdlhMgG5mdTQzHSfKHfGN9Z8gZrKTB7WDTWSTEufWFMBQ1l8xNw284KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBx4L1i0e1QsSBEnygyV5HCIRtY3FXqcFAlr4dxj4y6zt0ZwYPaQJMBdjgj6JjzgNIq-gPHjh10mngRh_ed8Va12m2Y0AkQa65CumOO2sn_3VXfBCss22vc9kgnEXCZHNWgwzxNZvikXp89fmutVVef6JfYojctPSj3OWeEAOMLy6n0YzUDOyNGSYXeffKvjKGLCMFa9o_BpyR4ueK39PsC52cYegSXWOxxTBgkYwQbPhuCNv1Wt-FGbsrui2yQn5KBohd9_opqNuCqvuoDNMcuVTvpmvewReA_6W1vRi2-zDNJvNUBO0Fov6K6-cYK_gj84n7uP-_3gA4BI2NYUOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FErUsOwsMFDp20IRQvUJP-8KxU1UyWta1RRCC935ryZ6Ot2ku6maoedyZ4RptM5EFg3YToxP0pdWjTn6kwGDSM1NU4mjE_0fyUZx3NIPgkezs7u9nd-gV_inWXrN36vXeMqQNOgOhkdd9Dya8xf6EtwW21Okfvahvd8Px64uPFkIjdXFdbiGPGfG_yG28Ky-jUPvCjvEtnNqAQiPgAIqCuXaaNmPDVYiV0SQ2lUtY0ezehSlX6kHgnHJhcZ2IW2WP6UaXjoZ_FdvlPECtiBhk7AYbl49MC-m39qmVwnYcQ-0NbOBm0UDETT6UX_loCLdqMJy3u94Kb1RamzKROYzCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Svhw-a5NBl8CpkdVZ62vBLl-J8hK3QT9V0BljtMdTIyPCbQBN505glF191edWPfbptDnUwih9CIuRG860yDFHMWFp3gKBHNpnuMNZCLKHFmh1dmxhc2GQD6zoLZdXAwB0bXXJ3RG373vJHHhu43Sex2N2FyWLa5OYBnSjSxbdkJC4EwGgV6qO3hEURO8FBF6qxktdXzzA7M3b4HIxaW_frzk_4sExLLCMRszlux0YTrLZvLFVk4NEhtkV2MgVQfYqw9WxRkINUxHXPNzUpKAWnKihJ7ioGHP1KkmJyJ7n7UnkjwLdf2vI6UnZDQholhe9Dz32Ns_mK-6OBB_wUz_hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرعون، جسد نخست زاده خود
را در دست دارد، زن فرعون گریه می‌کند
و موسی و هارون،
در گوشه‌ای از تصویر دیده می‌شوند.
برای مجازات فرعون، پسر او،
و نخست زادگان «همه مصری‌ها»،
«حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس
که در زندان بود.» همگی کشته شدند!
حتی! حتی نخست زادگان گاو و گوسفندهای مردم مصر!
و این تصمیم و اراده خدا بود!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_ebkinLQdDICl0FZ-_Gpl10Ou1mYzaJo7E2rWycfPg5Sq1xNiN8OjnJbky9Rpg4B_qJ-T1mpkjpUkeYfffurgTtgbQU7WK633hQka3rTPPsryvlh42lcS654dvSaA7QHQ_FZu7fQlhbqkQwR3IVq3L7qN_UAQLC838f75dUrzu-MXN_NIpgtPHmA8_BsBAoWWgjCEuN6N4JuZajtg8RNrr7U1qf2cAQb4O0iK7GrBnS3UFdSt_vIx92hqlNyofByVs5qMV2kqK9rg_s43c4JWuzwIZOK6_mukWHYLZY2JI8bpbWidciaLbRn3vVNazza04c9-QgspCKjWCp_ob4oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_f6ik5ZrPIXgNkNOQTUFG_hlR5TebwfGqXeyS4HLyBoOluq-hM2ectYq0Q8F9nTmSXNuduhD-1NVDrcOaw3Yf8xuHFlxMHpj9jcOLdb3L4Ine1tjlk9OJFMiAa6n8_pkQ7PqXQx0mxvIgXuhZOa-Ik7eE_DRPtTcqYpLhXHK4dXEUHBYelApKMibd5zcyyZ2pBnm0LTArmf_thcF1fhpcvTwYv-SmzUzyZuUWSoMw8KNPV6Kk-av4eC9tW8JQ2tF87MG8lFDb-MX9fgYA9RVBEa_Q9SUOkQjBQRgEQYL2dF01daOtzeL-ZfR4cSWWOyiriHUJUCLAgvXVOah1WA2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5MH_2xhVq-8FqbR8k-zvicke92mm6YFOXgAvvplvdFcx6xdxka9paRODiQMUX6ryXX3GJfCe8u3OhgZp_h2v4yAoG3zt0m9vrsjDR8YemhgFkxIB0oEtKUt90W-Eq7R9YYrxBYrYLkQLSLdrh6jkfCSAfWO7D3N-hWtjN5nVE0k7qZNKcdWcPD0pXSgdd7Y0XtvS7wtGeHSg3osEtETbq64DTnI7_w5LOtK0jypE_wCt6RAOtfR3EpIOmWkasTitFoWkI4dlaoUNfvbuaM4wnnNtG8sGGBS80VPgZWFvcG0iyu25G49A98-Y-Lre70uSd-SMymx7eQHodhaQ-zKAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-wqN0MrWx6JkackiTsSc9ImTXAipFlqTeoaPKNsnyK9bbCnc0FC9CZpjKnOGpReI1ceYSIHoT-82FJpTSdekFqvcAJxPWsIswvry9J-r2b8zMMCoPpAtXdlSlvoZUipfmBsRpxH3GcQMdmE2HjZu2fOIUXu7NH3YvV4mwyJGHm1W_0wnAi9Y83MqiZ3aJer53A_tAt70wjOeI8nBK1h8CE2qnAS3AfN9k5SQOKh1up5YLRWSFxM6gjO4i4bS-G8ghqLE8RVwC28pofxIYAvQAMPx0pdfGdZg95Rx4QzqhM275hAuJeoUKdWB-f82nX270dQXygSob_ZywMwBoCPXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -
سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!
تباه در تباه!
خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».
احمد شاملو - غلامحسین ساعدی - اسماعیل خوئی - منوچهر هزارخانی - هوشنگ گلشیری - باقر پرهام - محمد علی سپانلو
اینها روشنفکران ما بودن،
جامعه آرمانی اینها، ترکیب کمونیسم و اسلامگرایی بود!
از مسببان انقلاب تباه ۵۷.
از مسببان گمراهی یک نسل از ایرانیان،
از‌مسببان  تنبیه نسل‌هایی از ایرانیان که هنوز  به دنیا نیامده بودند!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILPI4s-1sqi1Gt5MvjeKTZ-hbGXDincfAjZrrKxM8Uvex_BjLghV9okzkoDGtpih7Dg9hN3_O43lLhQSlfh7ym8GeIm0Z7xnK0YfujrY6SpdtfgCVaAgWIcYS_hx9bSl_lNE2zpdcAnrXLoaPW71aSI5BbLUYTqgd1hv-YRgdcdlH9TnQ7ZUD4T7RHMQrnBKz6L_wLgDhR4XzwnNyqk2d9AbWdGMO-vD-BeoyJWhqk7yCcyaY5rjTRaT7JN3FuJPR9WYb2DIlrYcUQ5MnLs-roXw7CtT4ts3VApPY74zrxNqwjLxae9t7oOMqPAKysgIMkOILnsdRRJsBARERmRtnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=d0xLqnc-rZ0LnFPGreQ1Jd6JnJe3MX8DzEnzKILkVuDpKCM6SRbGuHNa_r4wZSLHN_A2oaCXMPIcHFqdlLu-7CksrJe9023fsfJxxXBVkNx37DF-RgWfs_p-aTR3_3AtXB2CrZVjr-sc_9-falxOVsBlUg96NzIiGIBccsTal6FJY4ydb1PTbd-60FYjJkgE6sI7_3IwavgQGc0a4VuVIMtvPuHESOX32xsb1LuihShuqVbetLtwrrKwSzeHpXsoj6D1_ztPNuYuPxU17sw2owa589cGdSr9YGxscH_ECG0gnETpVHC-8VdHwem0kkLeAb6Bs9dWEzDQZ_kAPIerog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=d0xLqnc-rZ0LnFPGreQ1Jd6JnJe3MX8DzEnzKILkVuDpKCM6SRbGuHNa_r4wZSLHN_A2oaCXMPIcHFqdlLu-7CksrJe9023fsfJxxXBVkNx37DF-RgWfs_p-aTR3_3AtXB2CrZVjr-sc_9-falxOVsBlUg96NzIiGIBccsTal6FJY4ydb1PTbd-60FYjJkgE6sI7_3IwavgQGc0a4VuVIMtvPuHESOX32xsb1LuihShuqVbetLtwrrKwSzeHpXsoj6D1_ztPNuYuPxU17sw2owa589cGdSr9YGxscH_ECG0gnETpVHC-8VdHwem0kkLeAb6Bs9dWEzDQZ_kAPIerog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SblThGaJXZ3Lr6FGfVddtE5K822dFtTfYaDMDJBLX-M-Spr-GOCISWEgNhG0F6Gbt01ZiwYLGLtf1rMssl5iWtCWjNkdUF5g-2PvPSLf_iDCqpkuit7mO3Bw_a3grpF3jUUVKqwc--njg-bsintVtKmdDcF5ifv7rT3w4PxI0eac8y-MK4jYUewK9hepYjS4HsKjRNXCf23F82LH24TwCWKTBtkH8eTYkv6V_73kcsIGJOh7K1s0YxHj9dd7DAiJvaSTQOwoMAGzr0IkbxaH4CG5T2ZUVlzeCQyiohPDoB2xGjxlheF4_zq_7YGFmZfzHoi1kpcGQyv_PqIodR7zcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxnzFo_nejZxYFdu1imYTgzp-9c00jWuSwemiwpmKouyYq-ecHjqnPFr6qPzLDeIakgsssEdarNlNfLueuGNh1EZZKCYj0SGGY7ktdgCdbHTPTNj5iE3eRnFvkD3bFP3VqC_YIe1SAkX98Fh3A_cAU70m81GycQnvpyKh4e8afTrppg7exKQS-ogEPRNsOAAcKnJDsRo3ckRCm1SVdPGrCAxhyjMkGPjb0zhO0-1quCVNLtyF0rxtd2YSxCmA2Zm4lB04CaP-4XVToTT_2IQEEvfVy_QQe_in5MwlQ9rhPGEWEsdUzoHB56QAoaz4LewCm_9Km0VUbqOHBL-IXx0kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlllgCaOxv9p7coPOpE97ujCSi516zRpOxl_-OT4omGZ9enlxhJu3GuegLNPFEJ5c0uAb9l4zGwPSpHSroUjs64Ue5dH3Uu5f3pTX8GMBOdRG0bsky2QJ4xbjaAdwmoXoYV-gXyUG32qaXH5GqsGns0weWMAW1mYWum_Tw-eh-00ypX8C1PZae28NTmBANZwFLAVnn4fe1DWjDw9LTrWbVlXAuirDL2Lpn3j3lsR8fyeRpPIFqMJGGNoXCMddTGgdYo4OJ7A8ahv2WPvtecerAhs954lAIBu2u0iicHb1HgXp5pvFtMIMdEc5DPyp2nrKNwT2OqZPLc8LDhJ-6Dz3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3onnyUbn_UBDn6oD_BSWC-Rw0st3Lx-RWHOj8M3rT6XsYIP7zABfwb-jvHfuWwiV3cyoaoHixD3BkT6getDHrt-KkQN4oSA8c3Hl1GHjOBMies1vHAuFRFqlni9CjP9C2w_VgJLGcdlqmiKTDZP2qXa4Dok_4wo429TrcBY8AS8O0Ztq_3GzlnDP727YwsXEZ3XCeeHNd0Z0BfzRK_75yLh5_M8kk_jNbuqlz3esMTqi041xy0677cwTZag6D_16crUDwDmVoso47kHj8smAX9xiw8GtslxruEEq3-xSWQAF5crJXmlTa2sG7fqM2GQERApakwsmn_zhDFKb7I9xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQk8PbVbAbFfryWnJWHr19CT4Z8b1pb97-GaxVty7GIdQ6CTwZZHQEcmtyrzGSvScF2tr_oeT9hfigxqaTnmjI1C2Au7vZ_y__xuS2a_fWIbtuaqO0nz95Rp3__Slx2rYTMZ5iBpUYtnPkGOUUpzry-CniMpsTe0GhW7Pt5CgA5vsACNCu2PGyodJMfC_EdzgX2AEvyWiekirWdeTruhubQnPP7LWSw0D0HQasfVn9DODo2WF6nbNecCJs-G0fR3H-jmXBd99jdI6ye0dqfkRBrPgWQb3QAn4Gdio3Jw7zhEBdLpSa0z-QnXzkHD4bEUwvVQtY2GsYnkpq-xEJJSLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2v3q7P0ZeTbv5n4r91V1M5MpISePaA9PhbNEXVF9b-uh4DB7fzxzJn8oBjceodP5vPFUP2cHdsS4xBEs3ys0j2KyQCJVVYDzADcxXDw4fKYctGqE1Ou1fWq-W1det5hggiJYejTkQDADQEB_SDV-f8TVg4SPJg79M3S513Dxe4MWk91ceumBP426zHy9-Mh5xStSWDYpNn74T49aFTQMkd42RvY_j_09nfLVnVS1bgO_pC_ngVWqcL-mxz5oEEWhojBLamSOEnSgF9mtAJg9UstyMCldSh5i4AYvizBhbQ7CuNVlX11xBIhu2qsiyRZg_vyJRA4T1aifbXt_6YfPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2PlXH4RI4BWdsUT6AaJ9vzFT7NjYpWi7y6PgbYZ7fSQdXU7m4y50spgtoj2f8fSUp96793y6-cgrCaUps9Gp0NBBg1WHZtH4Kd9rn5NTVUTBV_7J3_UB50cmN0JxGw0JgGSzolcaTWvns4Us2ar7h9NQo9jDvGYK-xii-qwbUA0aSg0EOYx4mPerswRefeu168C80WSYbILsTRnoNyLVVV9S8e2nvLbLUTMDDNO8lJeQO9qVzfLPmCdV22W4lPHnpUpAP35XOJuDfDXTPFNy0vx6MkybOaXXoNidBxaupxCldXfQvgSR2r-wr0i6yeAkXzPZE41_Ploh4E3gGauwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYCtWuQGouV1jT1Er0C8qV-r4KbeTY1AD1ujmhub23Q9YoI2TPs1YjUXCuYN4ppzIG0b_m5WW6-5bIUMjlAfc9-QZK2NB7DL2vpt__ERksb7X4jbx5kEFVfOl9GJ_CNWM2cjYvxmFcPvuIjDWjj2I1qPVso19tnhxBMPC9zzSPB03jdO4iRTEieqvgM91KeEUfnbYTUVJdmO9ptf_qqHksRtmQQbi0lOG0WcAQPUdFS31NRfI9XLe3vKpNlmZ2YrF16G7BXrbRZ7myutIm3L8uz-XRE-zCWIqCPzc6et51DmfoUY7B0_INSSIWLKeghDLUq_6thMC3-_RF5e3Xh07w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دولت ایتالیا آزادی رفت و آمد هوایی و دریایی
بین ایتالیا و اسپانیا رو به طور موقت لغو کرد!
این بدین معناست که تا اطلاع ثانوی،
پروازهایی که از اسپانیا به مقصد ایتالیا است،
دولت ایتالیا مسافران آن را کنترل خواهد کرد.
اقدام دولت راستگرای خانم ملونی،
فشار بر دولت چپگرای اسپانیا را افزایش می‌دهد.
دولت پدرو سانچز هم اکنون نیز دارای کمترین حمایت شده و پیش‌بینی‌ها حکایت از آن دارند که در انتخابات سال آینده از قدرت کنار خواهد رفت
گرچه برخی از راستگرایان امیدوارند با انجام انتخابات زودهنگام، انتقال قدرت سریعتر انجام شود.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=MTxU4tAFIcT1i7Q4q4bZkhXGmivEISZ2Ojok60XoFzpcAXWQQ0nFdphw2mkRDRsE_MWxre2PhKE934mCud7Pnw0puzRlusClsY6t7eafyS9hVG4q7xxhoK7UgHCpF4PfrH6J55ix6eDMMIb8x9eFLIrnd-7VgXiSFI9GmSqNXffftQ3lZpFa_U6fijwOZ9Lo7kNh8kLGrBlmy9gXhw1ffX2oKGJrl5DZMAEMxJFlHTB47dGwCzd6k9FhoHScRSEdeFdxqB4c9gAbLwp-7nftpt7W1ClRzJqh4m-8hAf6hHWNMIVmp-HskdSre1OYaghBgiRJCyjhu84fVmMmHar_cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=MTxU4tAFIcT1i7Q4q4bZkhXGmivEISZ2Ojok60XoFzpcAXWQQ0nFdphw2mkRDRsE_MWxre2PhKE934mCud7Pnw0puzRlusClsY6t7eafyS9hVG4q7xxhoK7UgHCpF4PfrH6J55ix6eDMMIb8x9eFLIrnd-7VgXiSFI9GmSqNXffftQ3lZpFa_U6fijwOZ9Lo7kNh8kLGrBlmy9gXhw1ffX2oKGJrl5DZMAEMxJFlHTB47dGwCzd6k9FhoHScRSEdeFdxqB4c9gAbLwp-7nftpt7W1ClRzJqh4m-8hAf6hHWNMIVmp-HskdSre1OYaghBgiRJCyjhu84fVmMmHar_cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OL97F4gOf035cWL4-xapVw1nXI08gqpksqtyNYwVMFFEIZpZfOg-IyKxn2h-sYwJ-YGPtVrYWGReIEmYFYBiXaRDTGqCp83YX3mKLYd-h0FkTuIi-ph4CLUuxshnPXvyUsL4auSWDGITSQUHkvPo-y_uU3IlZUfw6NI3V8oexHreQJOV5sl_cIibZTg7Z2aVzisCaiAsWm80n_UYNRoTjEQWl6WHtKd6jtrJdo_Qfnx0J9nDPSnnzCGKGBk-JciV69R13n4bmuDA3HBbTsRYNS511RjviHjZAOBCR7HtrnxyO2c60LE9bjtBOGMxLtQG64nW14xxsUVqphFFLyY_QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H90BeFmg32TfowdFBz6qhx2lY_EjCp9FpkAmcOaNSCOLAppcxspA5mjfBazTnMpoLLjtEGwoJE7M4D2SZvC8iXVLHhi-wrLYjE_uuLCwge_9HOUwET2tWyUAmVjO6SfGVLLRtdGM7R4zd8RETBUGz8EQCxsWd784UJZjeek87Fjx2NYG09QPtC-OXJkO1jBr4BfZe4nbMymrWGPFLBtCM40B5KjlR-eF4wt4Ai16Z_K4GAvgalCo5xl7R8a1ju7ojiLmLUvq30roGPphiacn17eXi1kH1lOhV9W2AgI5qrQIkMlyVOx-uySvJs3PqTH75VslG3U-_JcC1fl9158jwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftTXdW6wwGtzreU2vQ5aQPk5we-xvW-Roq79ek0973Ao-y_nYA52eDXcgYhP-iiLfepS9p838LFHwYDvqSU9UBGDgmmnNFIwdhpP0U1RHBzoO1tmgGYU3IKwYdIsSN7LrgnMP9i2sOgDCOiAQqAfoekW3q_DOjvxVyAAnaF1e9qNJAA85UQOimfRzcoEfjJ9Y14Olz_M6fKMktsJQSDYQ2qO9kbRRIWTxZolpsOmPRVH77PEo4vZXIxsJKmMaopQdILwZwU7BHulFecUa7b_KXs17uDE2DZUuclPyUlhUHgKtcXb4c1I17iarhgRmI6pJgCHv3Dxl-c4OZ-SeASUJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdY16XOLSCvnVoPXVMrW1lHEC9_p1s-4hAMg9rvdKwKqUwlXpzEY2xt3lG-KDFJAL_aqeGBEWRZ2bu8cd6oBuvMQ3HAXsg8zJ3Pygw40QUVW45n7huqnJ77LpqW-5JsRqKV7xcXkIKj6KN4EDJ0Jz3C1DToPA4npekgQcaGegLaqxtBsMsyem8orG7l8CXt9b53Oqj3uAviAfeGpagNrzFpPIaPPlLdntM6jJL9A_wrhbFA0OGR6F_Ki7oWw85GycbO8WtzBFZDicL0jgj1-EVOxsweo3GPms4jklWE-iA-yZlD8I1JKpL9gEu2PNMamulWr5ltCxbb5BnhsVuR4xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOxTxLkeYwqrgTFKJ15amYUh3K5Qpp28PDV4YnT9KEEvlShezGBJXeloxOTabe8I-CdCDFaA-dmhsF5kK9Tj2ofSWkf1poO639NcgYcfBAlp50mMv4IJn_x9_8bot-J7tupxVCuE0MWcVMYlaERzL2aYCtWEvncQux9tiWZw92LfDYgU8-51YtkwjUgbF8DrNuvCT_hmcK1tUhxF6BOmOww_ZZ_60bTgO_uXWSZlvQGSl-JQXlebc3HanMO0e9DnBI6y4V0wV-yndDwOR5zMpAPqZVXGY0oPIndjqFYxPCkXEwEUhlwu1nhPzHVI8BlwSndwk1WUlvbqelMGmwGs8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgf4GiAiDIrvnXb1lEsH7cyvQscNwZOEmEVJLRtpi07Oy-LyIFC9BMp_2xVN9Tz5Oh0smxfsY_tYvIePLGDS5BBrLmfhUuHxxwm-KVqBGN9C_HUiKtpOMOdfyHmo6rMSHbp4YycEgMYNsoq6A5A0ZgHzhqSnsXu-4NzvWqr2XFz-9jHtsNAXsfqttG9ttk5qMnhbbHCG0Jt9UmgDmZ4wMj0ZASv1DiFiWy1NtC2IZDhu6vvxCsntQ0plqfiF3q-8xINO7wDoJbfdRI_qQu8bkEPjyrOVyu7BzVilcC_xa2xireFh_v4nfT7YOId9_R7T3kZMubnsqjKDh-IEJ7QguQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUaYd-em7Sw84ds5jiq_g2PT--DwAmDh4hYmd-1UEAJ0-N6TfuNGzgTu8jbJDXufjStpv7iLvvTQ2rASXJCflgUVyqC0W4cmdjVTBWhJd6h2XZSFHftvQ9nrc8MbNaO-gmxjqQ4k3UuqG6gj25PrIBayUiVsfjzZYx3PfeG4_XhrHNuBIbVQkgmKiP1w9SBdDoLOgGWTIV-lpbX9LshjbXMiW65MWBSutDIVqdxM1aqBaCvyQJkFiQs7HfI_VZrSPK8yJWxv9_9HiS4QAMfyzcu8pI4sCcpCEF75LiDsE3DW_qu9AVncK7pfHdxAvCAvpqI9HVlgrP7Xn4G1NFNnyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=SXxT0iCR8SxgrTGqdwFidIDcGYOwpDUH1cufXE7muwEfq3aSvbJKTnQ3xsuvKtWdxFwgs8efAXIFiv48td4FLp7BhEb9hmT6xQfoSPAry7TMtwZ1g2b1jWmokhJNwbTVOz_2bMQOgq-ZSlUdMjy7KhcrQJ_s8kES1ThfzRyfpf2O2YHC2cZx5oRLSI8Oh_Pqja3OqxwfX5RqpnFqt2N2U0s3ujaoCSFtdCwf94qEettG81a49cGn0NIRGeefOLheTwMhSskDTKKP5NZdbB5HhHPbHAxtjVck3FxO-0oqd8m3hUaUGvhK1-r01j_ZuE4WRmUjcTF0TeOQK61-XEMWBzSNwGGHGvXh5-EcrtozVBGodHfmzlBf6d78ofeZw0h9khfsbk1tSbttLWsA-wxW52GECQggQuJcKzCDTXaPwlSZDMSBP9Fz7jSxEyJvQapnZav7xOrfqSoVM0HInO1seCbyVJxyLc9N6-MH-Hkj0Hzo5SFRfVdjmTy0OJsUbhBnM9dDIP_QZIcsYSTWoG480eMhGsvkfCRSJ8V-V-VGZxWuZlIkZokXS5fM_08LZDyP16rM2W98UNi0gwdZcbdm0zurBS65bBBXYzfehQ9am-IXs0aCKJJ-D7V3V9D2XXwuDqb40JbYjtchw1m5IsmJybh3DEi1FnmXE8FYpIqsNsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=SXxT0iCR8SxgrTGqdwFidIDcGYOwpDUH1cufXE7muwEfq3aSvbJKTnQ3xsuvKtWdxFwgs8efAXIFiv48td4FLp7BhEb9hmT6xQfoSPAry7TMtwZ1g2b1jWmokhJNwbTVOz_2bMQOgq-ZSlUdMjy7KhcrQJ_s8kES1ThfzRyfpf2O2YHC2cZx5oRLSI8Oh_Pqja3OqxwfX5RqpnFqt2N2U0s3ujaoCSFtdCwf94qEettG81a49cGn0NIRGeefOLheTwMhSskDTKKP5NZdbB5HhHPbHAxtjVck3FxO-0oqd8m3hUaUGvhK1-r01j_ZuE4WRmUjcTF0TeOQK61-XEMWBzSNwGGHGvXh5-EcrtozVBGodHfmzlBf6d78ofeZw0h9khfsbk1tSbttLWsA-wxW52GECQggQuJcKzCDTXaPwlSZDMSBP9Fz7jSxEyJvQapnZav7xOrfqSoVM0HInO1seCbyVJxyLc9N6-MH-Hkj0Hzo5SFRfVdjmTy0OJsUbhBnM9dDIP_QZIcsYSTWoG480eMhGsvkfCRSJ8V-V-VGZxWuZlIkZokXS5fM_08LZDyP16rM2W98UNi0gwdZcbdm0zurBS65bBBXYzfehQ9am-IXs0aCKJJ-D7V3V9D2XXwuDqb40JbYjtchw1m5IsmJybh3DEi1FnmXE8FYpIqsNsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=TzNpiMtG4k7496mBXhZQMio4XkACjvOoCsZZs8-fAydqNz7b_ybf3xaMhtYyRQeTvZtsSJoWcKqNR24PCu73q05-B0CUqBjo_nVViO0JC0YjoZIJtl4mnsC5NlNJuMofk1791jNAAuZtxR_1sO7M4ksAQuA-r78YftBiTijAh9jGUmb4uh40t5aX9JixYWEhpWzhX6_Vm1pkobLPZ3PkiHTSLBrsTTGB3AOemWeN93r606iyD71r10cOf9KfxtRy9bAN8cgkV5sDr2SFGXgpfaljR1IZygq1fD2zf_duHXjR7GusnUu9PWx4autN1-EGBmxvYEOX0Lp2lJ5DoJFP3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=TzNpiMtG4k7496mBXhZQMio4XkACjvOoCsZZs8-fAydqNz7b_ybf3xaMhtYyRQeTvZtsSJoWcKqNR24PCu73q05-B0CUqBjo_nVViO0JC0YjoZIJtl4mnsC5NlNJuMofk1791jNAAuZtxR_1sO7M4ksAQuA-r78YftBiTijAh9jGUmb4uh40t5aX9JixYWEhpWzhX6_Vm1pkobLPZ3PkiHTSLBrsTTGB3AOemWeN93r606iyD71r10cOf9KfxtRy9bAN8cgkV5sDr2SFGXgpfaljR1IZygq1fD2zf_duHXjR7GusnUu9PWx4autN1-EGBmxvYEOX0Lp2lJ5DoJFP3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvFUSNQ4qFGLzIy4E9bNqUbkwnu28vNEo0RB-sgRgrPeyBKJ4dzcGS6ysW1NpGdnmmVp3rM61kv3R4BNomZxp7NhOEMruAtySqzEpG97fQSpSo-JkRNuzNjWxKXl3B1GHRBlfOm7usqCYfVHeb9n3zZOdO6NIEZYS6wH597oS2WhSitroC8yoRMgVqDzPQv7LBlA6WCxXc0LrpaMdcp4uci2Yv6pz8CbWrWtCR4wBJIfiXo1tCyosYbQvWm8KIYkJUdRzHzZK5DHtE4u0170dbl6dVUEAVt0iON_vc4SW0Ts5DXNDWiMyX1XWOcVNevHN6P4i0pdfG-t-c1rVfrAMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taCgi4jq8JHI1bc_G-thGOSkVtlLoT7QUsqC2vy7SI4w_R9q9_28fXMOCP81BPG2EFNHigPYIleR4pCFWqgNHE0VVc4NB4oYIsQcjAtknXq3vxR2AKVdp1Eh6xinrEPv87fQ-M0ej9s00EblwEqsjp7rd6BtBGWuaYIwwFT4DmW-ZEmTGl0TMYFIGIJFRhG03kPKNylpTBs2Aw-9A9Q3pMMm7G58tJppsU-XBj-HdGZ5wB5tPuumOkYRkdvPGndeanoLVXfH-irbE5TDKcmPJYz9ZoZv2ruv7WUfAFRI9k7y1L9iLJ0QM2RdhvzTo2SpID7S2NrrlOYeZ7k31ldvLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=SZBICpWFFlDlsTmU50UajAtcyR0rZAn44e0wi7xV2y-HKRwUt6XlWghMJo43zD0jd1QAN-RSCcWFBlJVULPeJpuZxMX6PzWKqpfNVcmH2X9KeJum35y94mf2WF4F2V9S1h5c_aT60dr7K2m8s7DL3exI5XBE4wuI9sO0KBoeFzy455ZxxbfCs02ac96tYc5ZeWh2YvNHdRBoROKAC7ZHfJ7kRXpUY9y1V3-JibfxkqaJmCncZcPcwWipKvFRZPXNfoprAMhI74HPJw21TmUDCjdekfQkBXwk0QDLhehshWrtPXliQYHOZGjdhEANlIKWhwIHiP9cX6RBCTgwMpIC9oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=SZBICpWFFlDlsTmU50UajAtcyR0rZAn44e0wi7xV2y-HKRwUt6XlWghMJo43zD0jd1QAN-RSCcWFBlJVULPeJpuZxMX6PzWKqpfNVcmH2X9KeJum35y94mf2WF4F2V9S1h5c_aT60dr7K2m8s7DL3exI5XBE4wuI9sO0KBoeFzy455ZxxbfCs02ac96tYc5ZeWh2YvNHdRBoROKAC7ZHfJ7kRXpUY9y1V3-JibfxkqaJmCncZcPcwWipKvFRZPXNfoprAMhI74HPJw21TmUDCjdekfQkBXwk0QDLhehshWrtPXliQYHOZGjdhEANlIKWhwIHiP9cX6RBCTgwMpIC9oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDniJvqAqmI6hKDgW2v8zDFJFRhGOqSWgx44EIbimyu7P0z8gY7Xy798lexd-iFZzUoVrusm8xuVpIc-y_QcLm5889NZPWVX50u6a6nDGx4jBv1lLDChWT91at9KyGDC4uEDPLNix_lFG5KxSkmqISm2oGT3KAvoNXGIQuY2KNlTlYhpDZmlYaOnjU0D-L8pvg3ssifiarIlIGdvfGsGN_CM_WKKUxRgQ3uM_fvInpTAPcbgBuMf9mTzFkydbTq_Cs6Ljf1T4JITffHXq-EdJwbsNQq0J2rS2dsX7uERg9i63h1SFZ9FB689BcIRNvvjrmS5yBNntI1Nm2Qbo7DaOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی ۶-۷ جمله نوشته که خط به خطش دروغه!
نوشته که مصر یک شریک مهم منطقه‌ای برای ماست و نمی‌دونم امنیتش برای ما فوق‌العاده مهمه!
در حالی که مصر و جمهوری اسلامی ۴۷ ساله هیچ رابطه‌ای ندارن و مصر حتی ویزای توریستی هم به شهروندان ایرانی نمیده!
همون موقع که پروازهای جهانی در اوج بود، حتی یک پرواز بین دو کشور هم نبود!
نوشته که اسرائیل علیه اتحاد و همبستگی اسلامی است!!
مصر حتی برای کشته شدن خامنه‌ای، یک خط تسلیت هم نفرستاد! براش این اندازه هم اهمیتی نداشت! کدوم همبستگی؟؟!
🔺
دیروز به دو کشتی حامل گاز مایع در مصر حمله پهپادی شد، دو تن از مقامات ج‌ا به روباز گفتن این فقط یک هشدار بوده از سوی ما.
دمپایی پوشان یمنی هم گفتن کار ما نبوده!
حالا این اومده میگه ما روابط مهمی داریم و همبستگی اسلامی!!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fD4pSvWBBTpgK9NN-TxZ_3_Eq-SkdekhDOVeEdrAi_yGfBI-FXlxEb-AMN8TtGSeFUR6i7l0-51hVvRXSRGjV5natFZdyyac-zgxfqLNHCVUwOXEQ72Yv8AxvKuLHwGVFrysbO3h7JNQ1keYUuq3M6d-C3hC4-GNREdvZdMNsttQExWe3m82-OUZkhOJmpk7DbruDDQS6YJ30QtQXydGvLjBy3tp-5UOc25ZdJDBdiCRrv4kV9i_L1Gx2oyZrfyUvBGNubnTSW88kKQxCGLXLiDZYMuIi6IKqTC6WEv2MUI4tmMtXSK8fIzmQhenRECum-NFY38smRN2YToIeyVt2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeCRmo7GSTlP-nlZWBNe5Vsq_T_4HjpF43bfu9UTKXGIrHLeTB8CT0tIyl1m-lEf159uTKcdmtcNaiVD_xwSvBOXDV_rOtsPEeBtzvzDRWEN85lYJX10RVa4aga7XaEn96RffdKZdX1mAIVwZjFVeFuZP0N1Lw0Ztm5ur53NRnwYCCiNmD0rdC-jEwj13xz_mJ2vaw5mLHbm34-ZSq7CpRLLmGpPiuxxBPn2JN7MvTNpFifH1SHY4sWcu6i927nA47tcnN7KQDvPLHe468_KCLPp1EY6z3EbyhPsn8_NLDHh-RA0D1KKCJ4AXA05oxzLsirL0ixJs3ZA03dg2TXxSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/of6tUcqotL2we0t8ZVH_VEE8SRotVqYmKHAoY52Ksa5WG0hSjBgMmOzCLE88uhKp24JJ3fvGSdnQZ3WB4_Dwxivbf3d2KtaFSJL0w73NyB-l2A0Yj-8UyhhFiZ6jcOGzr-1KJzxDwp3r1XTe-_zzCJ67vBVHbQNmvmZWW6YJBxEyp8LEoYT8eUefiOIwU7TMck6Kw3Sp7z68Ns0YxOz-rUrei3Va-MGCZI22fONqhaJyYTfFXbz0TTwBdRo3OgOwq-dJLdoARl5RfQK5wvqVu9ae-aeQ-mPtBFAvo8njPuUyY-r-UaO-Zfivz4Mh1prXFq-bCDukXfJO3fJt5q8opw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه بار هم درباره حجاب نوشتم،
در حالی که اکثر زنان جهان اسلام
(نمیگم همه‌شون، ولی اکثریتشون)
دوست دارند مثل زن‌های غربی لباس بپوشن و…..
زنان غربی هیچ تمایل و انگیزه ای
به لباس‌های زنان کشورهای اسلامی و چادر و مقنعه
و عبا و نقاب و برقع و پوشیه و ……. ندارند!
نیاز نیست حاصل تمدنی که اسلام
و جامعه‌ای که ساخته رو در ده تا کتاب قطور جستجو کرد! همینکه جمهوری اسلامی با حکم
«۷۰ ضربه شلاق» و «گشت ارشاد» و بگیر و ببند و پلمب، ظاهر حکومت و فرهنگ اسلامی رو حفظ میکنه، نشون میده، این تمدنی که میگن،  یک آدم برفی و یک توهم بیش نیست!  که به سرعت آب میشه و میره!
فعلا پول نفت پشت سرشه و بگیر و ببند!
حاصل ۱۴۰۰ سال عمر و ریختن ثروت و اموال مردم ده‌ها
کشور برای صدها سال به پای این درخت، هیچی نبوده!
نه هنر، نه علوم انسانی، نه صنعت، هیچی!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXaFI-m1ohKofzf6jk9h_22Hflpg0Y5pQ1H9gBKs47Gk5GS6-ovA_UhLum7ZkP78y6hyAh83YQXUTAYuMypTrn7IwfUdQifjNvd05-wMdMlxRzW7Bv8T912oipQAGdy1TK-90LRLPsquxsSIn7VwxH3DQ0ylQ9mhCbp5pELnPoHRqfWlrmsCv_GV07H0LK0saeBa7YkUpaeY95rRtibk63vhjp1meknekPT-zs07XpiHW61q8_-QeUFcH0eHo2CIV9q0grAmVBXL-ZHJThFVCUIwlLrx77SM0CR-h5tOzefAhaMKV_77Td5EZ4OB9wEACRoGhSUSMRlxTpt-WZCcIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=S2W4devZ_YEHve5Xrm8ucBZ5dHEoQ1LdLA8CrOL5v5aSJfoTC-vcBUV0OG-76UkrvV0r7mwvMVgy1G22xAeupbC3_vArlCrzum21HZGMq6IWnTJ8Q0kgtjH_WmMwTYHlep8UCuaro1MdNCqHuU6tU92qXUWlXniPdV6pPYdRRGH-8vdW6cHPRj3bM2WIi0M9eL2BpY9k1SxADz41eH9Y80ObmmUH3et_Jn0kFGKDJvYRBBerAyUj_S01SNCxcUdugJ_67fE0kLfqmpBbloPgTj7ss8UjnUwBm-oYsAGqqUSPX4i_9qJUdSGhVaRjVKj0DFnK4P_aktY0nKBGKHDycjgYeD28Gn9dQPO-FxYz2JP_0qvnGeosVnv9tAp-6qhOlRiWLmXTZh1Cf2gkHmtl_rekzoiUsdYR3z1pSKgUZqv1vW57qW5bBZPBRH4L-wUAw3B_RzAK0_Qdbn_1dyIIyMXLMHLyIokibHORz_9Ldh32r9lzMm_908Y4Lyr9lH5DG8675NGn_y3DBWqFeYrUQlEhmIAjtoDgko2h9rXFWMekIVRGx2aj8A9gODryjPXTxswVpL4fXl4V381nAnR5dFOBNAsVCRP5PeeE3xVPE_vYGJ5VidKQKh6iJKmgk2t9ECvCGzCOdxouPOXnduTtS85gmalvyzNh88otombZ6CU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=S2W4devZ_YEHve5Xrm8ucBZ5dHEoQ1LdLA8CrOL5v5aSJfoTC-vcBUV0OG-76UkrvV0r7mwvMVgy1G22xAeupbC3_vArlCrzum21HZGMq6IWnTJ8Q0kgtjH_WmMwTYHlep8UCuaro1MdNCqHuU6tU92qXUWlXniPdV6pPYdRRGH-8vdW6cHPRj3bM2WIi0M9eL2BpY9k1SxADz41eH9Y80ObmmUH3et_Jn0kFGKDJvYRBBerAyUj_S01SNCxcUdugJ_67fE0kLfqmpBbloPgTj7ss8UjnUwBm-oYsAGqqUSPX4i_9qJUdSGhVaRjVKj0DFnK4P_aktY0nKBGKHDycjgYeD28Gn9dQPO-FxYz2JP_0qvnGeosVnv9tAp-6qhOlRiWLmXTZh1Cf2gkHmtl_rekzoiUsdYR3z1pSKgUZqv1vW57qW5bBZPBRH4L-wUAw3B_RzAK0_Qdbn_1dyIIyMXLMHLyIokibHORz_9Ldh32r9lzMm_908Y4Lyr9lH5DG8675NGn_y3DBWqFeYrUQlEhmIAjtoDgko2h9rXFWMekIVRGx2aj8A9gODryjPXTxswVpL4fXl4V381nAnR5dFOBNAsVCRP5PeeE3xVPE_vYGJ5VidKQKh6iJKmgk2t9ECvCGzCOdxouPOXnduTtS85gmalvyzNh88otombZ6CU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=Qn53bru_WPhhI5_Lz1D-1w2rMGd5-_bShqfqRFSJtcJRMYm7mbd7CmMJOp7DUBvhbFtIQvKeKSfGZSCtGfJxplKLecIA0lHRLy9cjcyCIApZavN95Wx33J4itW7rI50W0ufpjfdfW6mIMifR87as7M629CA-hGjJEZmmK51tqpTJMAbRIPmfhh5TprEVHcZsVDQF4R8TjYNg3JlVdzj1SQaCNsHwgGv7hg3yA2-ThMYc6GDnVTDXozmeUFiCqEQ2v2oHPzRfkzxtQZdy8hbYfIXvkXqV2nmsJlEovPHt_TvPM9Rd4IOKjateYfrZvjm3QJOjGap05ZUlC5B0k9pRfx2dbbl_32lzfw0iUkOoj362WugatLeMMXXI1-82lizn4ojkjBg-UDWFH8U2Mtl7IlDlISC8JyfugVIp4Mods8Zl_swNayB8aDeKXVxLK8--AxivtNl62b0-LQvU9IEgcwUYuvGkJMA3JNwzZ4qAjSBqEcJAQa7TRBkX0E8SvXbwMOw9_69A9ncK1XmuHZUpiom7MWQ3OejrdHmms5n1NuoPG8CcC_CMIPe5l5sKRGFH5lORpFVS6jkJhkVjNHexdY-RAhkNVM5rGyVsEmA-PVHO5eTFICni5k3ycY5dAwqw_474XSW--RaTevzX0qfcxp1jm750KjmCLDpzcjNwcRI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=Qn53bru_WPhhI5_Lz1D-1w2rMGd5-_bShqfqRFSJtcJRMYm7mbd7CmMJOp7DUBvhbFtIQvKeKSfGZSCtGfJxplKLecIA0lHRLy9cjcyCIApZavN95Wx33J4itW7rI50W0ufpjfdfW6mIMifR87as7M629CA-hGjJEZmmK51tqpTJMAbRIPmfhh5TprEVHcZsVDQF4R8TjYNg3JlVdzj1SQaCNsHwgGv7hg3yA2-ThMYc6GDnVTDXozmeUFiCqEQ2v2oHPzRfkzxtQZdy8hbYfIXvkXqV2nmsJlEovPHt_TvPM9Rd4IOKjateYfrZvjm3QJOjGap05ZUlC5B0k9pRfx2dbbl_32lzfw0iUkOoj362WugatLeMMXXI1-82lizn4ojkjBg-UDWFH8U2Mtl7IlDlISC8JyfugVIp4Mods8Zl_swNayB8aDeKXVxLK8--AxivtNl62b0-LQvU9IEgcwUYuvGkJMA3JNwzZ4qAjSBqEcJAQa7TRBkX0E8SvXbwMOw9_69A9ncK1XmuHZUpiom7MWQ3OejrdHmms5n1NuoPG8CcC_CMIPe5l5sKRGFH5lORpFVS6jkJhkVjNHexdY-RAhkNVM5rGyVsEmA-PVHO5eTFICni5k3ycY5dAwqw_474XSW--RaTevzX0qfcxp1jm750KjmCLDpzcjNwcRI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=DRbknAyizotFRpffV3M9VWY6q0lqW8hebo2OAkKViVgcKQi3EikW94T62cA02SkIHRXcuTQyym0gXok6EVIlqKS831T3qfQmHdZT7n36BESl8GbVX11ocmnZ6BqwmBytBfCGqRrZWUHyxmAYS2sZfG6ujFS-SgKY7BlRAH5pHNWseYkTIj_PN3Ul1KVJVhUZ7JMrBjj7qZYyMV3xRfOfvduV50hITnCIwCbeqZsutocx--HfJDAYAYZBffeiVxyxcwhPHVTdXRIEJNAQRk0-vi5rI1nnG7n-MkbndbSJ1ZgRRNesupxHMJkhGCzRWNVo3enyU3OmFFE0izYNzH0Chg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=DRbknAyizotFRpffV3M9VWY6q0lqW8hebo2OAkKViVgcKQi3EikW94T62cA02SkIHRXcuTQyym0gXok6EVIlqKS831T3qfQmHdZT7n36BESl8GbVX11ocmnZ6BqwmBytBfCGqRrZWUHyxmAYS2sZfG6ujFS-SgKY7BlRAH5pHNWseYkTIj_PN3Ul1KVJVhUZ7JMrBjj7qZYyMV3xRfOfvduV50hITnCIwCbeqZsutocx--HfJDAYAYZBffeiVxyxcwhPHVTdXRIEJNAQRk0-vi5rI1nnG7n-MkbndbSJ1ZgRRNesupxHMJkhGCzRWNVo3enyU3OmFFE0izYNzH0Chg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9JMu7xrwMBoqXKmLLOMIDkFu9hKenDVdnmj13Y1alqPGlWfrmPeQQm83Xq9mOiPxVSnEjGjvoGneK44vp8m6bFXHkBpgk2tJFdgYtnbQ3oDbF2vUd4zLd4mrfRZzcE5n7zGNre8-xuTEkTxn1a8ieGcElAPIs-eOnmegkVhWcpEWKtwu8qAJm-4vb4mvJtXmhc8bSAvA5mK_g6o8DJmUMUd7AOJQdAmC-zGTyS8XVrQqwfotTmZuXrtM0Fv557uY8Z95BO2y4HorKjtZPB3wtzN2MGEK9ahWu_OJG8dURhZDN7k714qYTi9AmhvfOm3FC_CDktTQqJ2OZggAAUDXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KV0Lpho7u9CsdCfyIZyVPAOmwNu1Iyynet65N2JAuwOEE4eUqD-gqiB6TkDDMWD-0Fy4O4mMnk8zr8-mhcxVTSagejVmx6XP8ZO9DningvUslc8OFlEQbyrfLNO7Zd05gCzwDfTwGQmSehrnZz30hG4UdT8aPVllz6_Kd4rN2jA1CnwRLIPGEEd7wJHoBG6OwMRI8s7FP7qkTcKk6JGDNCeHdXdnWOtfVVy_r5adUk0mCxWYx9xquLaeU0-6gOu7TBqCXVTmjFw0LlqTM5LZ-376n6FylMBdMu0vpM8WFrrXGd-gPxUlqai1MGVmP4RsXrvgPWsF8OcYW3Ai-GTp9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=qiwX6Ltut4SHp_YZbRofls2-yEGDp3TzkkMYMOvO2CCGPcn0LGEG5Gl_BF_IDsbl8bXYN6_LeHSWmiWGWg4EOYyxyGCKIX7zkavRhL7bEBrg0P04GSlEnS9zFi0aJ17lD07ybH81mLdAaNmoDf3c9cC3sJX5WQ6ewC-Oo6Gc4CXmVqHsBeRcCh7E3HbAHGYwec5VfP4A-D8Udd0bDm5P9Poql6Qpdujp6pLE-x8oQPmrg1_lYehfUpRIr6gY39s3Yf-X_yodom2jjN4Qh5qIBcTp2muzMnBfRTIUPlxQP38iELAL8Uzre5qHTtntkJhHIDTxFp-5jBOTLQyDHhPiS1Ws570UaVuC1D8rXXWHax3coFQPbihMLy1sNzKCUL40t3D12GaYLlS_W6K1vhPzTrfkZ8aWhuSNZjtpl5oXKh0J8YEmLUlhGJumQ8bhnAwPyT8xOCOu68MpmlT9IxOi4in2S9OTfhVM2eaHRSl-f0wmzpxIvyxbbvzUjDr67HpUvWfFSZ8qa3Bp5l5QKIFgapTz2XG5_FYBQU9k23RFG5Vi9Kikw_C66it-_x0NwNvPtzhuQnB2cR2tMuvc68K-wcCRwt4IPhjtm6wx_9oxbdLonnordlS4ylw9H2oQ8gPDRi5bLVXrspeFVf-QGvtItlCh7r7uLzfRKzLD3a-syuI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=qiwX6Ltut4SHp_YZbRofls2-yEGDp3TzkkMYMOvO2CCGPcn0LGEG5Gl_BF_IDsbl8bXYN6_LeHSWmiWGWg4EOYyxyGCKIX7zkavRhL7bEBrg0P04GSlEnS9zFi0aJ17lD07ybH81mLdAaNmoDf3c9cC3sJX5WQ6ewC-Oo6Gc4CXmVqHsBeRcCh7E3HbAHGYwec5VfP4A-D8Udd0bDm5P9Poql6Qpdujp6pLE-x8oQPmrg1_lYehfUpRIr6gY39s3Yf-X_yodom2jjN4Qh5qIBcTp2muzMnBfRTIUPlxQP38iELAL8Uzre5qHTtntkJhHIDTxFp-5jBOTLQyDHhPiS1Ws570UaVuC1D8rXXWHax3coFQPbihMLy1sNzKCUL40t3D12GaYLlS_W6K1vhPzTrfkZ8aWhuSNZjtpl5oXKh0J8YEmLUlhGJumQ8bhnAwPyT8xOCOu68MpmlT9IxOi4in2S9OTfhVM2eaHRSl-f0wmzpxIvyxbbvzUjDr67HpUvWfFSZ8qa3Bp5l5QKIFgapTz2XG5_FYBQU9k23RFG5Vi9Kikw_C66it-_x0NwNvPtzhuQnB2cR2tMuvc68K-wcCRwt4IPhjtm6wx_9oxbdLonnordlS4ylw9H2oQ8gPDRi5bLVXrspeFVf-QGvtItlCh7r7uLzfRKzLD3a-syuI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=Ia6jxQYlWBxAOX_0ioPqA4YSlsuWTzb6SlyZUSeWhMkhdYz9rMbPtIJrHIgrwTc-qI8MVhb2YEsLcO5wKOIofrtBXd5rXIYWfO9zQPE0_RtVZidwRpfMtujt7aVblI_mMc_5FADvd9_daGilLImG2FUQbbRvAz8a2DgSdWNSkF5tsIWlr7DpXqVg-oip9nIYjsiqtX6YbjBh9fVrQuc8QuYIluzD6mmxDy0sLdL69vkT9PH5ADSpiKhqcM1I1cxjQZoqp3bw06u0QCDuqQNgsp3qgDEMkGaZqxiQR4Lp6Q1q4h1WrA4R2xEMlT8gZvYWtQG2jlaFwwca2yfC9hNnvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=Ia6jxQYlWBxAOX_0ioPqA4YSlsuWTzb6SlyZUSeWhMkhdYz9rMbPtIJrHIgrwTc-qI8MVhb2YEsLcO5wKOIofrtBXd5rXIYWfO9zQPE0_RtVZidwRpfMtujt7aVblI_mMc_5FADvd9_daGilLImG2FUQbbRvAz8a2DgSdWNSkF5tsIWlr7DpXqVg-oip9nIYjsiqtX6YbjBh9fVrQuc8QuYIluzD6mmxDy0sLdL69vkT9PH5ADSpiKhqcM1I1cxjQZoqp3bw06u0QCDuqQNgsp3qgDEMkGaZqxiQR4Lp6Q1q4h1WrA4R2xEMlT8gZvYWtQG2jlaFwwca2yfC9hNnvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPvFWsmLGA7YolVMgC7tyGA69fEVJlY2fUU1Lzx7TsRUGC8XDbCl98ao90X0XLCq7YwP0JwK1n4zw_QUoEPfCqhV_sRPZ-7XLW0khcZk5dYEWOMs66ygCmuD0SdRQ4VqSrWSw9d-4msKxixJHQtTT1MXwIQQWm2w_X_ilq9EKaj51YY81KTyoT9JxulnMfTTvZuUnp_OfUqkgZ30KOs7yQe9V35exLEUuXYkFsozA4hgf32bUhEpz07tEZoixoUYlSCpxU9I3Z2u9JIIN969N_3njtJaIOWwbJDdysqYYb4GZg6C_DG-3YxygdaE7Uvkm3agR4Iucw_MWjct7ztjVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/od2uAsq2aSZRb9AYqLlCAKdnA5TGs7TM1zAbG60hobfOkVrM88cBhkbuhS_VW76UndOiR9eOlWgguObI4BsftGtpVXFYlLWZ8WG768VyDJJIMEmrNobkiiX29n2s9B-d2LBnRikEB7GLK1b3KoTdBr3VwduCmzko7B2-oqwPxct9sjWcJqxqtcVrN0C8oexCHRqPqnZHMLvBL8pxN0kY3ZVy_RwrRtPMQb8txmJzmrzYdGZwFuUlOABoLkImWxbxq3ZH5JuzqemVof_ft0Erv2ZDh9CYmqQjyBja7i9EcUzAiFZTSX1w-Hx2IwI0MS_dQUTeLrnL5JoJ1YtmOcIMPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hfxmvlvr2NBrq8dDMRUhTcCYc2FSn5htT1kk6mN-swAHwrygXoDBBiyrF4UXEiUjoJak849Q9G4you1T9UqPmOuYymrek8V5Im1s-26PtpQu5JqlJpU7blYJP7R24nTwQ-8JtIqSMXDqt6gMTNVoj9J29JpnukKh4OerZZpXA_U-pAoi2pNlH2etaB1_XOkAfJgtqVfKKTNjq8t9k5PGwP_IEBhhAlKLQcLsy-pdebpya1rHfH8j-8nuKZIZwJfaaeUwkx0HyqGXcYcF2Ic7bWj154HEWBbyTpocV4vgwXzSWE3bEWy3Ra2dTAZPGMchbk_a5HlMuRTPDm2BSUICyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=VLwErg0HcD5_l3aqNwZV1Vk1pP0842apuQu-M9z1POAHWQvpGcGvFYvpLeyUbvuUf-BXCGiomwdWG5pgmuERpZBPX9H-kBcTXhi8sR4LkG9NvBS6arDOICqPyq1Rv4mFlPW3IBOX0TF0pMtsilCTQyavhQikzgFK3L8wWzDLLnhp_P9zuKFcUQs4oD7JYVf7dm1GW7M1jR3bE6iy49aMaH5tX9WobvBbUuOP11qhHOV5SnU1_EBRM-NtLSZYGuj-WN6M6ZxIWmqLYEbPpNR_8a-N2HPg_0ztjWthqXqUPwQqY9_l3N-BjTPxaI0SQLPxmBlz3PN_dxB6P1EUYhyPXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=VLwErg0HcD5_l3aqNwZV1Vk1pP0842apuQu-M9z1POAHWQvpGcGvFYvpLeyUbvuUf-BXCGiomwdWG5pgmuERpZBPX9H-kBcTXhi8sR4LkG9NvBS6arDOICqPyq1Rv4mFlPW3IBOX0TF0pMtsilCTQyavhQikzgFK3L8wWzDLLnhp_P9zuKFcUQs4oD7JYVf7dm1GW7M1jR3bE6iy49aMaH5tX9WobvBbUuOP11qhHOV5SnU1_EBRM-NtLSZYGuj-WN6M6ZxIWmqLYEbPpNR_8a-N2HPg_0ztjWthqXqUPwQqY9_l3N-BjTPxaI0SQLPxmBlz3PN_dxB6P1EUYhyPXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=WiHXnjJ2FX_wizq6diLLhreMLf44c7Nv2-sJkFPSOC1a7ycDN7QZiAgKBcj4uHqXkTrR3n2tpE7E8K9Bm_2ewAp_a8mrsTaSa5ZwzLxivM5xwI-vMzXVSjGDIBIrZAKkW1kkL6sxqvZHBHJb945ER6qYXEXSThvqqbt4wlX0KVe93R_aBcqW21x3Nsz34D9QhBdtQb7IeOa6qw8qqlANv5mYQ7JBWHObqhIyU8BhuBUuYoIEAfWI7lsBN6g7QJ3HR8Wxdf-54gzeVWjxodrOnt5TIPclqt3hMtD3YCiBYep7EY28LP_I2ObdW0IcC-mRh6SUVIKgHfQhSMNnMWQn6IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=WiHXnjJ2FX_wizq6diLLhreMLf44c7Nv2-sJkFPSOC1a7ycDN7QZiAgKBcj4uHqXkTrR3n2tpE7E8K9Bm_2ewAp_a8mrsTaSa5ZwzLxivM5xwI-vMzXVSjGDIBIrZAKkW1kkL6sxqvZHBHJb945ER6qYXEXSThvqqbt4wlX0KVe93R_aBcqW21x3Nsz34D9QhBdtQb7IeOa6qw8qqlANv5mYQ7JBWHObqhIyU8BhuBUuYoIEAfWI7lsBN6g7QJ3HR8Wxdf-54gzeVWjxodrOnt5TIPclqt3hMtD3YCiBYep7EY28LP_I2ObdW0IcC-mRh6SUVIKgHfQhSMNnMWQn6IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzniDvqF97TfICMxToYcwHp9W0CLjY9rihJ0kzO09Ko418ip8jrpIP3X8U3R47OGF6x4jT12aDgtYPtAcgxW63F_rnG_rJEIGrSE2E7U9TFm3RBDcLyn-YvgBCJOVGEj2osm9sGISAdbfcmgCwxIicazhg8I1s2VkuHuXFVVAqAuuW5WurDekeGG11Xv4vOxgRUhM08yAYI0kZ1Xg5m3j127VRk2YEeo6F3fdTAF2_vRp62o2pUUzifm5BR4QQVDaARpd_TiYMUgln-4nuV6StIR3O5qpCnDBAEzWlPYA4nv1-gapFnLS4VNeYWKhcAl_ooxqNF5Q3YMPO7jZvruGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPQ_G2r6OG40Bc8F0gN4w09LVgvX1TrY8kMI1sT-YUo91TiffVy4uW49EYf42DTFOSB8IlSkvDzthdu8Pi2zcur3ADdBKSzvL_UpXeKXLpyrjQRMmeTj4XUcAvcL3j3M-sF6iQLftGAi_yJDmZJL-gQl4hVyPB_mY_CjvF0mf2El6DVPhocqzBesx8LNPpUMbeUJllAOEuJTkgWhgE3u5qPi1dbhGkD74v2eggrsmLvLTN7UqAjSYhnKjoETRSyRZKON8q-md50DV0LBh6xbzzASnPMwUDz0j9QM1DfdCo8ZeW4zWk_p6NHlAxyZ3cAmONaslEBTFfSDRGFr8Iy90g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=a83xv7GtkqLerVj4DnNS_Hu41XUiCS18cVXyUEVDqmPfJw_OW4qwW6fstWK9tExc8g76rSgz4Jhqlq4HnRd98cPWameSWDT1HGH1FeJ3xH8NqqyCPESHPaOMrOe2TTv72N2mYlSCKuPFKEYEAQFtkqwxOOA9QOAYjeBRv00e7og0atvk2X5pfNi8c-hkPWT1x8yZ9xMazG7R1ohiXluaavZMyYOpjKqDWGK8gTE2nDEDi2SEverrWlw7cuOZs2eVBT1YkvT4t7OAQUKzW9vi_-EI9_UX2xMkhvWPSUHzHXouKKrIBBOX9Tjc_QhXeuEvDBv-540A7m4-EozHP22utQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=a83xv7GtkqLerVj4DnNS_Hu41XUiCS18cVXyUEVDqmPfJw_OW4qwW6fstWK9tExc8g76rSgz4Jhqlq4HnRd98cPWameSWDT1HGH1FeJ3xH8NqqyCPESHPaOMrOe2TTv72N2mYlSCKuPFKEYEAQFtkqwxOOA9QOAYjeBRv00e7og0atvk2X5pfNi8c-hkPWT1x8yZ9xMazG7R1ohiXluaavZMyYOpjKqDWGK8gTE2nDEDi2SEverrWlw7cuOZs2eVBT1YkvT4t7OAQUKzW9vi_-EI9_UX2xMkhvWPSUHzHXouKKrIBBOX9Tjc_QhXeuEvDBv-540A7m4-EozHP22utQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDzz8PQYXFDtA-5nEgtB-t7BGN6H2ptYybLOU0rzKLi2GxW0OWO-S8Kd5SR1cG_WMkeoQm82ntJTgRQEnNxW8GFcnGZQSohG_KgzNNJfOURirCYjBzADIU-tIGEVq4kPh80TjkYWBypC19eMUVEIdqoDWbwVUdyX0Q10R-Ciufx9ZVaxEaN7h06bCo78fadO-yz7JqKTt3G3k5p0Aa41O6o-2q12EVOmQ_97QXz1TaCJWf3BxHSKKl7YMoYjtcVfPBeRCEGU9XR3sO-ZFq-qJ_hb1FUBUl1Vr5LtmR6zYmDhhW3gq1vJzphzerDzTQRQ-WfiheAMHCHMn5NbSv6CAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دیروز جمهوری اسلامی با پهپاد به دو کشتی حامل گاز مایع در مصر حمله کرد.
امروز دو تن از مقامات جمهوری اسلامی به روزنامه نیویورک تایمز گفتند که این فقط یک هشدار بود.
(که علاوه بر تنگه هرمز و باب‌المندب،
می‌تونیم در مصر و کانال سوئز هم تاثیرگذار باشیم)
🔺
صبح امروز هم سپاه بیانیه‌ای صادر کرد و از حمله به دو کشتی در تنگه هرمز خبر داد که قصد داشتند از طریق آب‌های ساحلی عمان از تنگه عبور کنند.
🔺
دیروز صبح هم به سه کشتی در تنگه هزمز حمله کردند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5PxsmF8fYPW54LbUg04rDIlYI8_Covl66QiXEiCr-MGj7Y0XormEiqkpU_EBndbgtX5PzVQ31JNgLuuueQ3f67_o6Qryj13NPc5P_d6dGF1U9u0CfsfMe9S8Wotu2WGDzljVTM4Nz0vAqSk-5EoCrVJsvebtpGYpzi71b2WsRSLemII9eIGjTdarelMja-jLAISRzot9kWM0CXlxoGow4bGLD8gM8fetT9_oLlupi_txIqyncd2lIlS3rhG9RRbFmyXHlazpoMWNXx7Q425GbCuKkzQGObcQ4SP5ojNWbhMMD0Ps2VxWcgCGJ34wXpfZYIC9zfKP_cenYPJgD8mDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی آمریکا
به چند نقطه در اطراف آبادان.
شنیده شدن صدای انفجارهایی
در قشم، بوشهر، کازرون.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FA2UvN35mLvJ8Uvm22Ih7pQIAlpgJg2kITkRd8b6hfye5LMZXNemWz7viLwOiKu9fNaXwPha_ya2t4IEeZShIZVZ2-wC0eh8_pdwLOpeReLQMj8gNPiFHkATtkXGHdVimcT3SWDyjgH1cGopjGsfOZNsEHP2y-1rJFFg_BR_06tIVa44Oosm_OrBNoPXH7BmW1CZJnP-2zAaZLgQwcrBeDGwCP0PLcHI44HrNrGze5Js92Hc4l_xmWsbn5ShMWQ0jSokwB8AF2OS3uZbavfH8NcqykqiTxoCRcNbcTFBO0CwihmIfRyUU0AWOqpcipXzPqjhGHtFz_Aeaqh4KBn1Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
