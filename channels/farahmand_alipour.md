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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-16 03:51:05</div>
<hr>

<div class="tg-post" id="msg-6520">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkQ9qRQUS7w47T078UsCCr1OL4LCw1jfduu02WsozfK3iyE6yKh_gA1fegoauyy8Mh8ldlt8aLwok_o6cgnFrJtRJbHmeI_3gDh1Dgjfa-51xvqzxkfUa0k4TV8_SHRRsX7Tyhhbg0kCIb7KzgoNFPnGREPGqhUtySWdYffHaYrd8G0IySksQl4CfVtW9V9ACgRWwfGrkuqe6MKl-_bcQUMzRuHKKWvfyhV8X1BHsUvYOlTupLg2OOS8l8tL86_uaZ_Y9un6x94Ehl8bps9iIdrAyXoWQ1zv87R30cyvdp3qzERFf2r7wF15aTj8GWNHyfGUrnQvMos9UtUQbibkOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی به عنوان رئیس شورای عالی امنیت منصوب شد.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/6520" target="_blank">📅 22:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6519">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/6519" target="_blank">📅 22:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UeEhMb5MMMtdBsReytDEPrXUtsaNYd3ZgLcAFoKm29D8sGrRU6UaLhCe7cTC8fLVNIPTQRsHdJ4L7gqzB515R9BXlwj4bTsyx5OZXDm05lAC1HoKOjCMxKSV3i_1GauLsMtJY39aRTyGYN3cOl81elBKfJi6U_DmD_dU12ypZTpIEKOZa4A0YfMAuOj9hlp4kCdq4MdT3BMLkOyetIIOOkaNdUkcwIs6-wK6SbUUR_G0Yx7FrA69p9BdTDbl8ljR8uSLU25yCfXg1mvDS36SRO7yRCuu9wiI_oeYsa62vyzQTTPJdYpbQ-s9b5KpjnVmzUV8ufX3gn6bkWGtSaNLUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به امید بالا رفتن قیمت نفت و فشار به ترامپ، زد زیر تفاهم نامه  و حمله به کشتی‌ها،  که با اقدام به موقع دوستان خودشون  در حزب کمونیست چین،  نقشه‌هاشون نقش بر آب شد!  خدایا عظمتت رو شکر!  اما در عوض برنامه آمریکا در پاسخ  به اقدام جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6518" target="_blank">📅 15:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6517">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwIaN6o6q6bn-9uCcTMpR8mSdg1iA534mGRYSEAMaBCECUlM56XZ-5-T7MIEcKMn0yLAKu_rDAifejaKLpSXmV7McjFxdugTAjTw4dPNNNvWBXO13e4biRch79ZuCtzuCiayZwLBKw7Dti9prwrY6TYmf1lyMv_0mFYxO4VLY6Mh7MOe2ckcm_WboY398ZfqBp1iznxOfYJS7ZT1lw5uoW1t01dcuFqaGBNhfbw0aI8Ogv3o2Q3I4OgTbAoKZHruJ8WbEveaRpQ2-NsNvRGr9ntTj8T072dMijFdLQ_jVyzGMWHb49Q-HEO7iOS4J2OPjb59ja2wSNYFtyG6WREocA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم : افزایش تولید نفت کشورهایی چون امریکا (که رکورد تا یخی زد)، کانادا،  برزیل، قزاقستان، ونزوئلا و….. است!  نکته سوم ترامپ!  و به نحوه مدیریت ترامپ برمیگرده!  بازار نفت به شدت حساسه به اخبار  و به انفجار و ناامنی و جنگ و…..!  خیلی وقت‌ها قیمتش «روانی»…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6517" target="_blank">📅 15:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRiInt98MsxwvNr7uVxgWJUBuPZOnpcnYgUUcRXoZNF2PURZG7dJUCvB6NWKz8RyOyrl3GgRPt-p-bHlRG8HGgxXTIzlOUCNCSHrA2qD8ohFZk4Xv3Hg6LV7SQIVAh0z4yOpvAZqayduz8ZBdmyiBU86jnumMZU89sNhnwzPlz5L9clF549E8gMl-GXfOPiPcNXWYo4g3UYZCfbcGFwYtZVT06RSa11IpRDKnwxG40RvonMyF51cQur4cxMRRgLsOzLzwIodg9n5GUMrAM1XHm06IB74vLAy9biH9Az5CdXVZGTANCDbsxBh6LfQ04XxcJa8tvFOZN59sj_b3zO93w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف نقشه‌ها و آرزوهای جمهوری اسلامی  قیمت نفت خیلی زیاد بالا نرفت!!  میانگین قیمت نفت در ماه اخیر با اینکه هر روز خبر حمله به کشتی‌ها رو منتشر میکنن، اما بین ۷۸-۸۰ دلار باقی موند!  یکی از مهم‌ترین دلایل اینکه قیمت نفت خیلی بابا نکشید دقیقا  «چین» بود! …</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/6516" target="_blank">📅 15:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BZOd5cb83U6H5HSsLqWjepo3SgyQUS5toG0o1jtX09pyKd9imRC_6SS2T5SfzI8ULqj9ZT0oG5lC5KE-l2Oq0KBsU1pjaZg6y_ttBrTjJOsFF49b5vQFnoOD1CGQcPYrp3o-AAqlL-6yu59DhMQZUA8SZkCQMfFN5BrjKQ9bGAHNW1gClLRBJfij6sroVvf5_xM_sO8jbv7l-LGdNMqTWr62lP7nkYdaMPNiUH_VRmgaSWJGsA1w7fe4Yjsag_1k2L6i798ol_Qt7CmaLMcwEuRurrvE0xbNg8EFX7HzpMOPoOaRlziUuicilUG4QnOCPgj1uYpo4X__kXXadY8EpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A5_NsLJY10WqwGbIRODHAiqJAunuy-KNYma1idetQw0T7dRh9SokxSqIgCwT5bRaRA0xBCnZC0ac-HMw9dIoC7Gpdtapjx2w1aQclKEamZGMUz5koep6fDlEX2mWbYqooOROpeJyINA0EiayIqYZZVydFpoo3uUyFELkGt6AAkB5ITXTLtdVI6f-IGwqfbiqMTKK6iA6AD9H5vFmW7EGE4xvWPxxhfv0_jOn3XX5ZSAEIXL-41OhT8xOB-4iu36RWU4afOXwRG_XY0df-IF1b7AmcFplguzQkCK2cqd4nt10dDI1lFLipcs9iCmxpFV6k0CZMoOVEh_79aCYvOLU0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جمهوری اسلامی با امید به اینکه با حمله  به کشتی‌ها و کنار گذاشتن تفاهم نامه،  می‌تونه قیمت نفت رو ببره بالا و بر انتخابات داخلی آمریکا تاثیر بگذاره،  حمله به کشتی‌ها رو شروع کرد.  تا با ارسال پیام  «نا امن بودن» تنگه،  قیمت نفت رو به شدت ببره بالا،   حالا…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6514" target="_blank">📅 15:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.  اینها دنبال «اتفاق مبارک» افزایش قیمت  نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.  اساسا با همین منظور شروع به حمله  به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6513" target="_blank">📅 15:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6512" target="_blank">📅 14:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.   خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.   او همچنین با اشاره به اعتراض‌ها…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6511" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6510" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2SgKn4EnNs6qzviU80TCo9WFcTQFjEu_EReNTw24Zdl13i3skjsQK5m2p2k40jOI5aCoLRn2XBSshIKOKjXla-ZDxl1KycLOHUAmoIzEljKdqR7IrkRiCeVwT_9Z9bEeNlectpAm4R3uIbu5iBi_SwHkouHi3x6OII4koxes07nbV_FneL3hTsvFyy_hAciLzqtVHhorZqHP_2afJRZchgveexLZBi8KAjUzyUUh8fkKwvnufhomjQjiW9l9jtKskFGMjA7v1LNSxGGsOv6ISYdnFVDJbDWkkj6lz6U9zZUKBVZvhCm5c7-UtBLRF9hyMPJWAaQHmxB8dnanyd11Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب PD که همون نسخه حزب دمکرات آمریکا در ایتالیاست،  هم چند هفته پیش، چند مسلمان بنگلادشی  را به عنوان نامزد خود برای پارلمان ایتالیا  در ونیز انتخاب کرد!!  که آشکارا شعارهای اسلامگرایانه هم میدن!!  مشکل ملیت و مذهب این افراد نیست!  مشکل اینه که اینها آشکار…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6509" target="_blank">📅 12:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtvY7pvASyoNzE1MgzbmI19FAUjQSKLVX8nP1mr0oTry5Kco_dGNHIQ9lAHysx--cf0Z7hZQSy55Vg8Bgz-QvFTNoUyQeLDjQ8P02-Ezl5HLd1wFmqqIU_bAy3nN5pNfF1nfEzGD5pexnsHeZUlbHlwLvpsgFG3hZM5kUEESUUUQA_lNis7IPYPF1SS7BD3UvdFDmxDU3raBS55ep2ntzcFhEBxD8jdZX_f3mwq1QFKbRObBZF_RWkhZLuqLERybPOSpyBy3vUrU7C1FMffld7xaCTB2f3TL_qaJWlYieYDODkb84q25478JeTGCvAspVqpdIXQEvfk0NNyMU3-Glg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!  که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6508" target="_blank">📅 12:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6507">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=QMFT3BBrF9lkX1bC_SLgfuiVnq7zym8mxaBIskSTIIzpCA7YnWqi9DbPz8Z0Cwdipb-HSaIlAKkV0vTsbAghZGzSjvAyiMCzJZ8VdxCB211U2xkUIQrriGKlWlKv4IRHWHHvzEbBxelcTOIs3je-bL7A7_KLC2etMFRKgaEV66MQTMOAZl1rJWMW-guFOC62xz2CsC1PL7nD--ReQGEoYPGjYH-c4SHRy08PFHgX6e_82o4oZOl2jaMfYKShlxyZ9gmDh-Bt34qEm7JK3RVPIXtNw0A5jja1A3Y6YmbNSTs784kbDSkVRV43f7SB4hr9OA5qBaNG0TpvNSN2nZfpLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=QMFT3BBrF9lkX1bC_SLgfuiVnq7zym8mxaBIskSTIIzpCA7YnWqi9DbPz8Z0Cwdipb-HSaIlAKkV0vTsbAghZGzSjvAyiMCzJZ8VdxCB211U2xkUIQrriGKlWlKv4IRHWHHvzEbBxelcTOIs3je-bL7A7_KLC2etMFRKgaEV66MQTMOAZl1rJWMW-guFOC62xz2CsC1PL7nD--ReQGEoYPGjYH-c4SHRy08PFHgX6e_82o4oZOl2jaMfYKShlxyZ9gmDh-Bt34qEm7JK3RVPIXtNw0A5jja1A3Y6YmbNSTs784kbDSkVRV43f7SB4hr9OA5qBaNG0TpvNSN2nZfpLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!
که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده
و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6507" target="_blank">📅 12:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای : پزشکیان ۲۸ بار استعفا داده و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6506" target="_blank">📅 08:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ilmdg2li5lAFG8jmsJa5jXjGR6mMfCwBqIZmEPTjKVFProEkFmtqzvAY8wZcnbkScMrtGYOHkhYZ6gsNuzg-21yf1yjnoafcVKMdVqAkoFvTnLwrRAurDpPnUD81bICLe_2BQQALVnrTAe2o-K-zvWXBWP07Yx2Nqyqn10XKZVkpC0mYQ2QwgPLltt0q57bEkflyy7h3maLA1WO695A-P2RXUosrtHMpL4-zyWWXVhUqO02uYbiPiOr5zqEBK_6g-Fdl7sbMLqh_UTHWM7MUkKQWxyg-n4p6V44B5fRq2YoRQp9l1Oxv1t5SeK7yAF0KaHb5kobr-DHbnI6hgonCjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توطئه است!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6505" target="_blank">📅 01:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">آسوشیتدپرس: مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6504" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6503" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6502" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6501">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=IpRhCsMC4c3wKwKUnXR_ZhJjS276aUs5zeyt8wuY25CENPWkGNns_A6symthQLnmH0_MTEZZ3psGxiwWTqCHRjOPCgpP8iztlI9juVLHKQCBSTmWncqHXAuY0uq5X--kU23_B0OH5uCzvM_EsAObLORsGOIe1Lt_k53IEbKItrEmIKYjkgV621PYgcJMARLL4u8Fmqfux5MEme_27nQqcaFuXC5uVWLBRQ0grNlqke6J9hs4LTo8k6DTnyVej4vif10_k1k6Md4RxqMwoHQB_sMCUr_aK0DOnn7KBMi1teFJ608Mjsg5-ROFV8Uv2ZNGH-BpnwAUot9F67bvc0Uuiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=IpRhCsMC4c3wKwKUnXR_ZhJjS276aUs5zeyt8wuY25CENPWkGNns_A6symthQLnmH0_MTEZZ3psGxiwWTqCHRjOPCgpP8iztlI9juVLHKQCBSTmWncqHXAuY0uq5X--kU23_B0OH5uCzvM_EsAObLORsGOIe1Lt_k53IEbKItrEmIKYjkgV621PYgcJMARLL4u8Fmqfux5MEme_27nQqcaFuXC5uVWLBRQ0grNlqke6J9hs4LTo8k6DTnyVej4vif10_k1k6Md4RxqMwoHQB_sMCUr_aK0DOnn7KBMi1teFJ608Mjsg5-ROFV8Uv2ZNGH-BpnwAUot9F67bvc0Uuiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی منطقی بود!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6501" target="_blank">📅 12:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6500">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=WaZZcSxrSMNXOQNgGglbj_JI0oQb6U88sL1-ikfKNJHqjfUdvL5k5unGIAFh4knLouKesx0tR89RekTKn4nKKaKhwI5DEVd8gl0o5cdIJUH3GwowLOKklFjJ_6C_aBFkhkKuf9B6XQ8jVywT_T6E6eSA_Ix2OksXay_B3fUcNNvjAuWT5Ta_vdrZnbRGrMS111tRvhgGBQKkAG6FhuMYq6t4ici216r4LsMtMzJGIDq3y72U3TnVphLWyyu44hbsAnC_fq9tyUC5QqY9Y8STE7hXnPo3ZUQcWZfgEg9OybgnBy3qpJzoajrSsgect6vtKr2gO0FuID5NsZNDL5-uSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=WaZZcSxrSMNXOQNgGglbj_JI0oQb6U88sL1-ikfKNJHqjfUdvL5k5unGIAFh4knLouKesx0tR89RekTKn4nKKaKhwI5DEVd8gl0o5cdIJUH3GwowLOKklFjJ_6C_aBFkhkKuf9B6XQ8jVywT_T6E6eSA_Ix2OksXay_B3fUcNNvjAuWT5Ta_vdrZnbRGrMS111tRvhgGBQKkAG6FhuMYq6t4ici216r4LsMtMzJGIDq3y72U3TnVphLWyyu44hbsAnC_fq9tyUC5QqY9Y8STE7hXnPo3ZUQcWZfgEg9OybgnBy3qpJzoajrSsgect6vtKr2gO0FuID5NsZNDL5-uSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمان مخالف اینه که از کشتی‌های  عبوری عوارضی گرفته بشه،  جمهوری اسلامی چند هفته است عمان رو گذاشته زیر فشار که باید بیایی با هم این کار رو انجام بدیم!  عمان گفت : تو توی بخش خودت اعمال کن!  در آب‌های سرزمینی من، رایگان خواهد بود!  که خب جمهوری اسلامی فهمید…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcEVoAL0U8v8RjMS_uSxkJEzWcIXukhcpR4Ct31aPdVXL9KFvF6kcurXZZyA3_7_DmnKPL2NBhDba_3yucYo4Tyc4Y3WmDHE7rA1AihIORVASDFGoMogdmg4V3BiyYC4yy6pi_apto7UOSfW3Fb9h6e3my9Ef2YeYxgPuwXh0_XgJ_YElKfOk1rhoNpcovZZUUG129smS9baH9sF3iTJFJCkGnejHetDRdd6xkxfLzsa7o7hY9j8U-Um0GrxcM8Fy5dNpkzxc83yigiVYP0f7b3hf5GfBWGiKkENLwaaaridIU6yybPQf7CcG9Yfn6-5iqzmYrl-rz0UvjHnOaurmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGhksaBZRKHOc1GYLLmisLRGjUw95EzuTKz4mH1azGQ73d_UnFBu9rqra2UJNIvIc5WvQAnu_pHlgSx8xodMc86_RUuFNIG9e-0H3PianNLCg1xBYGL3CsexROHHOTheROpd1leavm3xjh0EkOsLvm8YVY6XP6LPMt2APYBIIQIVgbImLPbhvTQmzBIL51WN4Ct5i2k2uYEL3twMBRnZPiu8jha7NP_Vo7gcUZVz-CeKqYomDkAY52yHf2WPDqbtpWyrHaOmuffiELMBdQtBeWp4HoZRaOhJ74AuCDXQZQorqDlk_Dec5TQd_PxHuJVL12gd-KU5q5Ett1ta9cCofw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJX3QrGAonY7pmgZMAh0jiVFsTITIJF1cVlQja1vH6-ktif9yMOAnEETJ1N0kK9XJTDJ2LHNxIwPo9asq_iLSNFfP_KAEB0WVrc6fAaSfT2-knMa9bCNGJkXUxVzYel3rpN6rPihD2hRqiaWOoRODopgqtOWV3v4GO5dnKGiZTUx8J0295tbTx1Kpl746sz5Svm2ZbXuZ4t3D_CwZXf4Hmh--nH8ydt1a3Y8JRJhlJe7_2213UUIz_QAHZV2YUR9-NXXYN8Eb6D5tT8JnJBvN_UcPWexSOe_1so2Q-zPgFUvL9I7aLCeKTl-DOpL1gmgXj4UJcKKl5t6Zx5ne1vHOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.
عراق : از طریق خط لوله انتقال نفت به ترکیه
کویت : خط لوله به عراق و ترکیه و همچنین به عربستان
بحرین : از طریق خاک عربستان و‌دریای سرخ
عربستان : صادرات از طریق سواحلش در دریای سرخ
(همین الان هم ۷۰٪ صادرات عربستان از دریای سرخه)
امارات : دور زدن تنگه و صادرات از  خلیج عمان)</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6497" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6496">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6495" target="_blank">📅 12:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=QBd0fG7MT00h8ki-7zwU6UysBZLzTDY6YfytNRmqWAzqqTwqkhvDgWgZP7s4e3GXAoiVsIwB9HiBg5jDrdmk3qob5MnAjzjj1eZfwF8BWJKaTD52agEr79ZBXJLpxs-3-HP81KPjprXFPEQT4-fwte4vHCCxWsbqyiG8BBauZLoiWb6g9DXd6lEMsCi5W3ZwYKr6rtoEYE-g47XW7WEbVr3e2koNBD2hz0Acs4EintPe6UahRccugEf-eb2Xc2Hm0jDFzjwuKlTpmj-5ZNDTtcUVhKC_PvgtR-8-PevVXRjNVzxZYNWVDKiO1vVLre0XcUpvirodb2j-hHfXldrRYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=QBd0fG7MT00h8ki-7zwU6UysBZLzTDY6YfytNRmqWAzqqTwqkhvDgWgZP7s4e3GXAoiVsIwB9HiBg5jDrdmk3qob5MnAjzjj1eZfwF8BWJKaTD52agEr79ZBXJLpxs-3-HP81KPjprXFPEQT4-fwte4vHCCxWsbqyiG8BBauZLoiWb6g9DXd6lEMsCi5W3ZwYKr6rtoEYE-g47XW7WEbVr3e2koNBD2hz0Acs4EintPe6UahRccugEf-eb2Xc2Hm0jDFzjwuKlTpmj-5ZNDTtcUVhKC_PvgtR-8-PevVXRjNVzxZYNWVDKiO1vVLre0XcUpvirodb2j-hHfXldrRYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای :
پزشکیان ۲۸ بار استعفا داده
و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a204c96911.mp4?token=geC7s9CTvEQab7_oewv0kp1HVet14nT5hxYOy6MVV9C7ll5EPCE6L9hdOdz1girTgzRZ2iXDtBSWJsdDySazwMCxdgEUrxTCEfBgo8VOizfQPR9GcgVJ-gl54EkgUwq220meBh3YWPMh2TKVsnvn2b0MrQPh2JFBb7m7AZNLjIokP2tCNxH7FlGtdzf9CpRe0lC-UPYBtna11NtQtRnWZEgp7Z84yEb43dSyfPkxzd1BmQDZN_GQPixAOoU_Mk476iKwXpso2tf_zp12AH59Ym-Sk3m7KUMEHO0ic_9EMZ_uKdbg5FQI0dqP8E4q8JgC5YR5u3EnsUagmTeuyHBIGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a204c96911.mp4?token=geC7s9CTvEQab7_oewv0kp1HVet14nT5hxYOy6MVV9C7ll5EPCE6L9hdOdz1girTgzRZ2iXDtBSWJsdDySazwMCxdgEUrxTCEfBgo8VOizfQPR9GcgVJ-gl54EkgUwq220meBh3YWPMh2TKVsnvn2b0MrQPh2JFBb7m7AZNLjIokP2tCNxH7FlGtdzf9CpRe0lC-UPYBtna11NtQtRnWZEgp7Z84yEb43dSyfPkxzd1BmQDZN_GQPixAOoU_Mk476iKwXpso2tf_zp12AH59Ym-Sk3m7KUMEHO0ic_9EMZ_uKdbg5FQI0dqP8E4q8JgC5YR5u3EnsUagmTeuyHBIGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تبعیت از ولی‌فقیه بر مسئولان واجب است»
می‌دو‌نید شمر تا آخر عمرش
از اینکه در کربلا شرکت کرده بود
هیچ گونه پشیمانی نداشت!
شمر خودش از فرماندهان ارشد امام علی بود!
توی روایات اسلامی هم هست که
هر بار بحثی پیش می‌اومد دفاع می‌کرد از کارش! میگفت  تبعیت از حاکم اسلامی بر من واجبه !</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6491">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=dxOQuICfeDvHTyQewjaZWEMX5BGPoEgDND3ewLeCzXkFmjpIt3XVIvnprU6-uxGjcWqsuPyNWxuqam0bznlj0lXC01E7GBHfdbUA7s-Umf2qOXRV45AF1-3H5r3TjDpca9attWtho2eWdglLdFEf-mfv_SikoH7vmbAe2yTFgerTNaQJ07I6Z_FMkEpY43xstySrsKzjvIA1BiXujbw5W3hQEeN4n-S9Sjov4drBUZeOENvRGDwaSXSEDbE2Ui6KyxwyngEOATWCeJMZ4vYyWOeb6oK3ShKF0ZqVeblhMIAyEQFsEff_lxqArwafClmgLpUap3rNMxzOq5iOTea4zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=dxOQuICfeDvHTyQewjaZWEMX5BGPoEgDND3ewLeCzXkFmjpIt3XVIvnprU6-uxGjcWqsuPyNWxuqam0bznlj0lXC01E7GBHfdbUA7s-Umf2qOXRV45AF1-3H5r3TjDpca9attWtho2eWdglLdFEf-mfv_SikoH7vmbAe2yTFgerTNaQJ07I6Z_FMkEpY43xstySrsKzjvIA1BiXujbw5W3hQEeN4n-S9Sjov4drBUZeOENvRGDwaSXSEDbE2Ui6KyxwyngEOATWCeJMZ4vYyWOeb6oK3ShKF0ZqVeblhMIAyEQFsEff_lxqArwafClmgLpUap3rNMxzOq5iOTea4zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6UY9FAHpXzalmu5InbPcTIfnUSdJjpPRLz-UWJoU5LWNxIPvcUZKr_CpARMeaQo7fiX23LWufFwHkmt5FYfsiiFjN4PBhP9IsMYd2bK9kQMA1Q-ZKYXxp2eD7KD3fTL4KaSXhaWiMXUBxL0ybEPYE6ZVAywqaGZa3mo_1e-kcGsgF_fHTiicR3SAH43SHWlxzC4frUalNHzObvxYza6excL8aLWCay0pG_6SLLn8O6yVyEuhUeHiY762ITNRzngYdctESua12dyFYV5Gb_5231oM_NcaJ39-fs0YH5WOCXG2zaZy8DBtzVmCsJXeIevVnvSXKWq_FPhkEi4Gnt_2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCCvOIsIAAgyO6cNv5Vrju3dsRiWhgMCwzbeswVckbtDjMCu_RNVJpXdQQK-ERw02OwZFE_7mZn4aoJuwXgB3udYuGAtC2xNEvlNeNd4e_SQ15G3znIo7AdvN_t9WIj2iI5o46-nTXq_vrQqoM6TM1mUIMS9HuNG92Y4NdCieh6BKvY91Ey6BvTVRv1Yygf6Vrs_ktaO0zZZ19pX01TxPmxeAEadtkNlZln-WOF9Cc9PCvf1omJ5k4nZTQiHrx2-meDrKDh3cyF9s4wj8Gnsidj4nopzRIHXTulQg92gdis1Pa3sQJkfYo6HFUBFBdXP-_wsifKNLmP-uTob36yydQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jS_SDz3Z504tjotuWaI5oq1ZWQYsAkcxfANETbR96Wz7uCpwxbqXRK1pJT9FD1Usi8weQYOY8Qq-prOLZR83J8m8DyWh_dbWYPF9bSrZOFhqQr_3iM9HrOf_p6Qt9W5ScAtfKqcGUw0CpRQOuCGV0hraYzWW2K5KHHnILAyHIsL27kJWbKIiL07MZOz1gy53uTPWbZU8R8hGxGnOAC0T8vsLH5Ex93R1YWO0EWhznL8_VD8xEE-5jQ73dtnI5Gl7ICbcWZiPhJ0N7KaiQ5bT69tbSiiF8WkMbGgCACarW2YgsFfjCzt0GoKEJUGgG2hxSRenKytt25GXC9YOkx9A5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPkJoYE8G2HHeVw2gNwrt1tmkf_n0z4Qm6gFBMhIky8zjFd774X2ZJgP983GKWONJR1ac64KkS7IHNK39YuoObnClOy-y2nwCG-_gskAXcVHoJFOoxzPOtEFFXt8UTxsqutB4vmJG57MgDRIy075DuG6TLRpJskjS9OJjxg0SBN-AayBwT4QzZEvaf-wXROPQKuT-_Cps5kKRRpYM8AcRH_FDoIdLIjjST-LOrGVWHoqL3QS3jvgfbVOf1LceDg8FYkxDU5PpTJUUrKufYiVoTKpVnTHjDH1Z2d6SFKiTZAbqOYFHjj5lxUX9MXgUvEjspkDBsUBfPdJkDCKZhIQ8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thmvIvykxsC6Aom4liUXDTl93JrECk5TU3sRlk0olxda9SA2ltOL_srWe8fdGzE_YZ7aSHfeJWAU77JmX46r-5BWTGQ4vqBa4usHsczWpaLCvGvnQx77x36w3lChUW6PX24Zi2i_gvgjIxbSNA0N0j9aCoWXvyAQh1ig8Rj8c3G3iELm1EUueRzeZYnJAcDE8G4E_2Ywmm66vE5LWQSvi8O4VIVi6JSfGXzaMLO7VhtF075gZ_FTzEre7lnUftw7DKh4Auic_VE_-f0zdJqsxMI78ZDmh0It1Qwf3R_3Ao9lwNcD7rmO9Ml6quQMKKbkMxMGcGGpOfDu4p0MAQToKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcFgcP5CXtjcZDZfMmBGHDK7cYMXoNayyeDk36iJByD-tlPaqxTNtLFjqnXpeEXz9nk9wDuYJOAPbNTqmkP4q8p7u3DFx1l4UjUfT1jhZFUDPQ0oJw9ryQ2Aer0xDSJhVgVn0_v_Huay89yMVOqZ_q393PYq3uNjrYeajioa4iNWWHHImAqgIjnky7kb54ZYdd4ts_hSc_ZURyQ8QUeEjoX5Jk5hSMjS6HhVuxtM2dkoQtgxDNE5aCGhveL6reUgY5oUy0zS69fgBvrC7fXMDCqT2dakerxOyUdLs6tOIy7p919hkkvEAPGZXYpFR-XG6AWVPU4LOpTq2X7ms_O99Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9bgnmdwmqSG4X4_lvxSvoKw20D9cger3DxgVSPjanpY32wPK9AKMDfkgwi825MFvPglCARajMevQ15Sr7kloEDdLz_3dwx5hWs1tg1hNMekNXHbgnZVJaj6yiM_QP5nm1RFXYGjE7SLn5XYB6rvc5_Qdf-czhk6KYAJc2usW0Z1Rgdr_qVAaR6CSqfDxDTZfHNR-GGY_eSCKu7RWdv_lTk26HxpA1lNmC1RuJlaB5JKtSwe9E_6Bo10mXCdlFwUEH5ZNn0HKFQbOpBKNP7s9wq3rN7LI6SfDykF_-LExn1DWtCfrU-gt-LvDNSjrjJgk5w-HSQe5QQc-oISXXHIqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2H0jVOgVAkegBD7EpWL6AY8SDbkdizQ2jiuB2UEwmrqtEt7Wgzi9jpCzyspc5E0XAoyzlRbqlADnHRWO9GL2UcZOIXqm9276FKbaUVUZ6MsMDx8z4KcfMJGl5RmPetYhelDmwcV_qTk73qR0NnSnH9_xHI1Vum78K1McFkbk0D0GxNKEy96wbpVuXoAYRqY8Wbe9Gk4jJo8-n_LQ2vIcAl064ckZUBsH9TX1xpc27bBffqXqXAi_l3rb7e-m2HWTEMNe_hWTMokGhisLiqaXaAGCWZfp_XRPXuH_Fvffd0wZ9dNX-BfKyzjmS7lXP-WU5vzf352sdlnC_2kwm08KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CreTtTtrxRED1sQoGctoohOYU0qS_hwQojRYgPrnp0d5ksIKlAdSoxJCfJeOlG4HWKbKiJ4v6_1cwMp2stp-lYu7RDHoJtTIAffNYlLwM-FLM37Kb-iv8UndWmPiVCP3sc52p3dfQ2O4Ca11plhMCvO2GmXhh227CAoo4UukRmrb6FZjMeYJA9pGAZNG28ni-8NAMx_naf2qzSyX8Bebt3Q1926E-t1ijAziFKssEjZsB99D0zrzvOWhRiUO2OV1PidUl6udDCxPbhYgDCGYmSBe2iBjVmq6c8R_y_QDrqmtTpLy0H5km1wFVE20Mu5G7KF_en5FP8OsTJZQX4B_bg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_ebkinLQdDICl0FZ-_Gpl10Ou1mYzaJo7E2rWycfPg5Sq1xNiN8OjnJbky9Rpg4B_qJ-T1mpkjpUkeYfffurgTtgbQU7WK633hQka3rTPPsryvlh42lcS654dvSaA7QHQ_FZu7fQlhbqkQwR3IVq3L7qN_UAQLC838f75dUrzu-MXN_NIpgtPHmA8_BsBAoWWgjCEuN6N4JuZajtg8RNrr7U1qf2cAQb4O0iK7GrBnS3UFdSt_vIx92hqlNyofByVs5qMV2kqK9rg_s43c4JWuzwIZOK6_mukWHYLZY2JI8bpbWidciaLbRn3vVNazza04c9-QgspCKjWCp_ob4oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iS9CGVMSSNfgATyFyplIsb05KiEcxM3_uCi2WWi_2CN-M_LzmzyvhQtXM_dshID_HGGjCFvQn56S7axVf-Bgp1L7uMOcYGGtgJE9Zyn-MIuEkp3HDkDZU4OvQDRZ6SvZn2vp0Dz2N7nE1IDaV-ZBxW_eEFUQ4fS7m4JE2_sl1ZVQZmB96BHICKUA2KhXotlojUe9FvWkygsT8kAXUhi90JEMP45UDzsv3DmVZF4-YtztLKozaRURwsmGYpfUcnONAeF1j9cQfQJBSQT6gv5MFsdwQtzmgLJM_0b7n_ANRzchh04Vv90dpxiGU2h8_tXPr8-IkowGzbkobsY5fkUNIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZEiAg9F0-X40EDcZZ0TVtTNsCf_uMa3nHUBBzdWotwfL2rpA8yRNG5muTTY4_cpEyrlra4QF8IfVPaerp5cJXYwjZJnOKLZpyK73tS9zUbOLwTH4mu29RQsOwZ3q45NSPewvaD6IdLUmA3wOPmhr28GRAf1it4V4a4RFaNcyIx-YdEuHSLPd_p4deSR8oRxDtFPwEzvZ1UPOWmDh5uTqHNia8uyzwPV_ceeYmjxANpZhNgfE6VsbKTGL2K_x-_AlPKUVj1hcXy64pr9iNYxqza_BAmty2DL9a6Fo9X05NglMux-p11N3O50ZQVdDIi4KvGZ2LqTEWMYAm2TOTmoyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOumP07anACsV8sJc-TRf9cGSHw2npLf4_0yC1FahUIP0Um0B5fTzgtsoNPJZljsbOolZPrTocV47JOUHTNMktn331VS0oKJIxTaMw-AQV8x74TD4CtHPxiHsxWSKv-TSx6ZT0NwcfXIemeYnPg0z6zX_BTvT6IX6En8He3_NokYOzSMpCqgLOjYUBCoxl_Ymrai5G8UVhaDwiXUzDzoqNUr-PGMo7kmr67qIielvWquGZ8uFLxFFJDHBpoErUKunRtwcKOo0LNiVknc_KnV0fqW4KP6QQM2wqVUZEJfgAMGwPrrlcQyXvKgja-eyVL0dQYHIqx7GRAd1YfGjeleXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v14iiy3v5-UoH2hKQsSyffAVTXJKVZymb9VzWojSQQj2liqb_wVbuoB_pjLViNglVVcz4HB2FVw-ubExL6FdNd1ZWPO0wO937PoQR5MAP30cgeplqBBSD2VFlQ1JPZ8Es8GIbVq_cmWHBHUxrPGB7n2s6D4_N7rXBsNsD6t-oXYEiweuIvbgeZmenqDNjh9jbr-WO8KcFmqVjydVm1Vuq2ensLlGxdZIMgrKRnR_fkElsKlFuQKzXtXpie1BU7JvAViukUdsKIiGsQIId2u8Un5orfa1_Z0PjHI2UaxW0SsCX4nQecZSkqSJd6H9Dd1NYQid92VgNRtVi-PsQ5Cwxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=UJa5yAWrS--kpB4z8w0djoeBSa8xZxspVvv6LH87FXcei3M_6ATwcmoGkNrHVzLZ1YEqRnLHEE0w5MyQtarVbNLwHOpLKbwzd1mV9d0BSaHSAk0iqxxwUvBz3mp2lFSlJnHUAK5cuLihgFHKMwDumfoqbMEMpsIwXJ2EUUXko4UtEHYaXn7JKckOXUB2K7CbUGAd8eVzXzIoBq8LRIvIy3r_c2M4AUwyCJCUgk2sz110NorpVy9p12mrVcC8MfrGlJmxlk_R-7jq71PSddOKPwZmK86eWd0HFlJLjrYCAONrYS-uSzAXjZT7LpM93_tNTzEFgEnjZFIZMMsKjR5xsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=UJa5yAWrS--kpB4z8w0djoeBSa8xZxspVvv6LH87FXcei3M_6ATwcmoGkNrHVzLZ1YEqRnLHEE0w5MyQtarVbNLwHOpLKbwzd1mV9d0BSaHSAk0iqxxwUvBz3mp2lFSlJnHUAK5cuLihgFHKMwDumfoqbMEMpsIwXJ2EUUXko4UtEHYaXn7JKckOXUB2K7CbUGAd8eVzXzIoBq8LRIvIy3r_c2M4AUwyCJCUgk2sz110NorpVy9p12mrVcC8MfrGlJmxlk_R-7jq71PSddOKPwZmK86eWd0HFlJLjrYCAONrYS-uSzAXjZT7LpM93_tNTzEFgEnjZFIZMMsKjR5xsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SblThGaJXZ3Lr6FGfVddtE5K822dFtTfYaDMDJBLX-M-Spr-GOCISWEgNhG0F6Gbt01ZiwYLGLtf1rMssl5iWtCWjNkdUF5g-2PvPSLf_iDCqpkuit7mO3Bw_a3grpF3jUUVKqwc--njg-bsintVtKmdDcF5ifv7rT3w4PxI0eac8y-MK4jYUewK9hepYjS4HsKjRNXCf23F82LH24TwCWKTBtkH8eTYkv6V_73kcsIGJOh7K1s0YxHj9dd7DAiJvaSTQOwoMAGzr0IkbxaH4CG5T2ZUVlzeCQyiohPDoB2xGjxlheF4_zq_7YGFmZfzHoi1kpcGQyv_PqIodR7zcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxnzFo_nejZxYFdu1imYTgzp-9c00jWuSwemiwpmKouyYq-ecHjqnPFr6qPzLDeIakgsssEdarNlNfLueuGNh1EZZKCYj0SGGY7ktdgCdbHTPTNj5iE3eRnFvkD3bFP3VqC_YIe1SAkX98Fh3A_cAU70m81GycQnvpyKh4e8afTrppg7exKQS-ogEPRNsOAAcKnJDsRo3ckRCm1SVdPGrCAxhyjMkGPjb0zhO0-1quCVNLtyF0rxtd2YSxCmA2Zm4lB04CaP-4XVToTT_2IQEEvfVy_QQe_in5MwlQ9rhPGEWEsdUzoHB56QAoaz4LewCm_9Km0VUbqOHBL-IXx0kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlllgCaOxv9p7coPOpE97ujCSi516zRpOxl_-OT4omGZ9enlxhJu3GuegLNPFEJ5c0uAb9l4zGwPSpHSroUjs64Ue5dH3Uu5f3pTX8GMBOdRG0bsky2QJ4xbjaAdwmoXoYV-gXyUG32qaXH5GqsGns0weWMAW1mYWum_Tw-eh-00ypX8C1PZae28NTmBANZwFLAVnn4fe1DWjDw9LTrWbVlXAuirDL2Lpn3j3lsR8fyeRpPIFqMJGGNoXCMddTGgdYo4OJ7A8ahv2WPvtecerAhs954lAIBu2u0iicHb1HgXp5pvFtMIMdEc5DPyp2nrKNwT2OqZPLc8LDhJ-6Dz3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3onnyUbn_UBDn6oD_BSWC-Rw0st3Lx-RWHOj8M3rT6XsYIP7zABfwb-jvHfuWwiV3cyoaoHixD3BkT6getDHrt-KkQN4oSA8c3Hl1GHjOBMies1vHAuFRFqlni9CjP9C2w_VgJLGcdlqmiKTDZP2qXa4Dok_4wo429TrcBY8AS8O0Ztq_3GzlnDP727YwsXEZ3XCeeHNd0Z0BfzRK_75yLh5_M8kk_jNbuqlz3esMTqi041xy0677cwTZag6D_16crUDwDmVoso47kHj8smAX9xiw8GtslxruEEq3-xSWQAF5crJXmlTa2sG7fqM2GQERApakwsmn_zhDFKb7I9xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uG77dwsEkSixUJKGOkW-jlDfDskFAwiXjvyB6ZuafjpDcGO_qDLkY1Atz9fg9b30skUhcmfjgKwvpOOVgW0EPYyILM2XOo0eLmLsmpx4qWYWeOhC2bBU6wTj-GPPM5CMWQGxUcqSEnPjJ1jjINeMvbJvzXdwNog8YpP70AEMXLB55ylGhk8uCPCF2PnGROwR3QvqBGOg9aywbfn9ozw1bpg7WSXbSKtb5Oef94HjOCIjcg_YbOibtevdWhSwoHEG-i9BpRhqWr1SlKt5zzwcNn-8tCKIHq95Ez7s5k-b1gjYPxmPsX85zhN8K5EkD2VgOvWXxxTiIGyrMz3GhXeH9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2v3q7P0ZeTbv5n4r91V1M5MpISePaA9PhbNEXVF9b-uh4DB7fzxzJn8oBjceodP5vPFUP2cHdsS4xBEs3ys0j2KyQCJVVYDzADcxXDw4fKYctGqE1Ou1fWq-W1det5hggiJYejTkQDADQEB_SDV-f8TVg4SPJg79M3S513Dxe4MWk91ceumBP426zHy9-Mh5xStSWDYpNn74T49aFTQMkd42RvY_j_09nfLVnVS1bgO_pC_ngVWqcL-mxz5oEEWhojBLamSOEnSgF9mtAJg9UstyMCldSh5i4AYvizBhbQ7CuNVlX11xBIhu2qsiyRZg_vyJRA4T1aifbXt_6YfPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2PlXH4RI4BWdsUT6AaJ9vzFT7NjYpWi7y6PgbYZ7fSQdXU7m4y50spgtoj2f8fSUp96793y6-cgrCaUps9Gp0NBBg1WHZtH4Kd9rn5NTVUTBV_7J3_UB50cmN0JxGw0JgGSzolcaTWvns4Us2ar7h9NQo9jDvGYK-xii-qwbUA0aSg0EOYx4mPerswRefeu168C80WSYbILsTRnoNyLVVV9S8e2nvLbLUTMDDNO8lJeQO9qVzfLPmCdV22W4lPHnpUpAP35XOJuDfDXTPFNy0vx6MkybOaXXoNidBxaupxCldXfQvgSR2r-wr0i6yeAkXzPZE41_Ploh4E3gGauwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJjI1Q3RCvMfYHSr6_eWySsL6cWY3qsJrHSfyu4jWSxo3eg9d8KknfAS6s-3byAy0tWvBh25-92G6r8qayJtDrL9dhFGWfWZaF3o90nVmtO4lxdWGHwjprYCH3J6fILyL7BvCTjYngaUX2juj8OUxlir-xY9iOrPRK3B7oiJ0YbLGqdc4uARKnLJfnxYMBMGogSQ2jIn3RzzBWemH8GGAiUJxFPzGOSxFBl1ub39OzmxT35tHvk9HJl09TgqaNaSpJ21HCfiJXck-6T0fkjQNKOV7aywA6LxnXa-fnoRQMeJyqX2Crg6l2Tdsqe2BMlGqKMZVvJjlzK6r0r4MHKhTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=dH4lfSjRLwF1JmafG8ObL4VBcDtYU02nFlzuTd5yGexG-Ho1i3vFI-OnMdd1SNUCk2j8rX3ay6wlklpN8uEyBFxTpy0ltlVxop-V5xqDq3h-S5MTJByovLKbKNsjEr3sggDtcst7uepFJ6mxZzT69LILetzWDJAi7GKBEy6wbsYtWtoqcKhw6MGB2lOeZEKmV3C1w3VXgogXbOpBCW0yN-dcJyRW1Ir-J4VmS0zHhtHiY7AGdF4UARwRgdfKjAvP0PLDabhN_NIeszX0MFM0xTY0ruziLtL9si24LHYdelkjxg_j3RGSA3E3W0_kB_8zub_5kVSJIo76RydnBU0Ldg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=dH4lfSjRLwF1JmafG8ObL4VBcDtYU02nFlzuTd5yGexG-Ho1i3vFI-OnMdd1SNUCk2j8rX3ay6wlklpN8uEyBFxTpy0ltlVxop-V5xqDq3h-S5MTJByovLKbKNsjEr3sggDtcst7uepFJ6mxZzT69LILetzWDJAi7GKBEy6wbsYtWtoqcKhw6MGB2lOeZEKmV3C1w3VXgogXbOpBCW0yN-dcJyRW1Ir-J4VmS0zHhtHiY7AGdF4UARwRgdfKjAvP0PLDabhN_NIeszX0MFM0xTY0ruziLtL9si24LHYdelkjxg_j3RGSA3E3W0_kB_8zub_5kVSJIo76RydnBU0Ldg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlL__nflPXRCCMw9cc57_Rt8zwOK2a8ZA2WTGGCDAYGZ-Km2d1ftqeBxFzQs-yqbR79uZRCDGu1dglBTO7sVOKzYqF9ALBvpiU-7OExF3yrGFRnqJDeB7DGZpGbpmXFbbTn3_8rmdc6oH7p8GLmycFyLSrJVJhqH66s0CcUQLk7iocr9evEe3cZW2mCD73P2cQ44gnWSgOb6FHkXgSa9ajntZzrH45b74hd81nPxwzJcRyfcUdZeCSxRuYVtKc6PkpBnAc9vlvBQnn8ZvWo_cvaSUv49w74wnDSSuxfpv-GGeSUDXbdch-0epB6W0IsA318srDAj72QA5M2CC5thvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXCSYnCyoNw1YuKjkjqt9Aj73nJmZiZTSV0hVOU8kqdRCNv8cDRpK9DCCRlbw_theJlomfxLHhKtFgEO7_MRq0NoCfNwWp_O_m8qE8NsrTLNlm97F_bhOvzOzKiHO7CK5pIdnOumAHf_F5KVQVodo_vfp3foky5Nq28Ffj6Xr2JVHVKKxSpREN-SrLGhxeHoZs4U2W3u-jrmZfqv2LGAiB54u1_XyP7ntxPU4j2EF6uR1G3GU5EMfT4IZYB_ngDnd3dhizYs-Jbu18ctjEIaGezC3-nOQMR0957070NSRg7va5KRFGMGi3aD3BKfY-RlosvPQ-gJM093G_fMWaGwyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftTXdW6wwGtzreU2vQ5aQPk5we-xvW-Roq79ek0973Ao-y_nYA52eDXcgYhP-iiLfepS9p838LFHwYDvqSU9UBGDgmmnNFIwdhpP0U1RHBzoO1tmgGYU3IKwYdIsSN7LrgnMP9i2sOgDCOiAQqAfoekW3q_DOjvxVyAAnaF1e9qNJAA85UQOimfRzcoEfjJ9Y14Olz_M6fKMktsJQSDYQ2qO9kbRRIWTxZolpsOmPRVH77PEo4vZXIxsJKmMaopQdILwZwU7BHulFecUa7b_KXs17uDE2DZUuclPyUlhUHgKtcXb4c1I17iarhgRmI6pJgCHv3Dxl-c4OZ-SeASUJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SE6nL0FFRcVD4KKQbyQCY-h_khIGOPzT0iUSOtd2wsYVaSjZeHlRuxrzbtCHSGunZFBVErzUuFoQugky51x4Mqvt2El0zb2Q_Z0Pydjv4sN5j0dkijhYjLpzHeokgYICWBfYlhUOYStbCJAFzVjo1H8T3VFCwfK_AaJPXrjzgnd5ibMXt11VYNgx12JFvgyJlSrJQhHaeKt53I9-KPJvDRVkPZHJuruQzm_SIJcYc_6ZlqTs0VFY_9_oYPu19zVTbIxy7AmC4UwB5523xpbo49RGz8eWk4aLFn6opi0sLF2fKo6G22scO4wXK_iym_2M40IDAlyDv1Vx_NoSVf6pTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKPkT4P2xBw2xd3WE0EsTFCsGfGnWXEGxvny_FeqSCoC03_Zn_WsJF1MU6GT6zQwFwXKUNIY03mLphV3NKU2TF16ygVopMk07UJbjKJMkJ90L6F_Eqg4b3olU8bdWvUqr41wveexJdbuHQ5Sme7ORA2A_TQgPe-AFZUpo_aY0rh2_dGcwtVD_GA1_e2ZgKsPYGPyoxtTZUBbYOyG7ii6WPwvS8JN8bAnTojvK3EfUz3lzCEvM9jMSzlCiViQCAucaUMq56pTpFA9BMW6JEa0qt3dyOf1LXo_5YsV489yfu00XNCZxPSY1CedPuIyj0wHoNv-bQLdcmQLijr79vpX5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgf4GiAiDIrvnXb1lEsH7cyvQscNwZOEmEVJLRtpi07Oy-LyIFC9BMp_2xVN9Tz5Oh0smxfsY_tYvIePLGDS5BBrLmfhUuHxxwm-KVqBGN9C_HUiKtpOMOdfyHmo6rMSHbp4YycEgMYNsoq6A5A0ZgHzhqSnsXu-4NzvWqr2XFz-9jHtsNAXsfqttG9ttk5qMnhbbHCG0Jt9UmgDmZ4wMj0ZASv1DiFiWy1NtC2IZDhu6vvxCsntQ0plqfiF3q-8xINO7wDoJbfdRI_qQu8bkEPjyrOVyu7BzVilcC_xa2xireFh_v4nfT7YOId9_R7T3kZMubnsqjKDh-IEJ7QguQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CARQ0LHOPf-43CfaI6_s3cIr6eiUQq75aTLx_c5q2o-oiZw_F2ZswR3b-9_2Rr4fAxWan3dw9UxWJa8iag744CNT9cT5-TTP150m2Xx5Q38gBr9YOj_Tf54P3mfymExb7xluRfB0uN884dlJMQ0MXkb_L0830ChHQMkMKR_-oX59OUQjlvPce0RnbBSkGT092TELaK5JQcu1RPdN6OK596P78cIs9YypH04NnZXa1zkJUUCVxU54XbhWGTzOt7bxOZ597g0PTBd3YJfkBmJYomcYsZ3gic8naObGV3TZVCwHLd4q9i0phQO4Qq_-1WuuG1ndp6ikr2Oa70hWVxDchA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=Qgxwvr9l3FTBuaUfrWiU3E0CtD9uSD1Ph1AhCo6B1xq42N0NPEvlr2yPEUgj58Sg1kYrYo2C6OYWUjpjHrjznCwWqhzpJ0e_naKCiwTZ_qcR6yg6OmlwyxcpVAbDIhTyHZAaarPh00AcTBG9W-4fPW6WWGzfMp5uR76-X6bMaPP0p8maZ-7gln7Q33izHizuTUc1ReXmB3dX6L9ZZA3G8ekcg54MpzU9EMNl8QQKz_5a08X2Pht5CbNoKK2zAwFLpUCdiX_-NxuT1UGTiirZaKSNtGblFxGtAj_qAXs6-bwJQ4oPz6hh3aHLB8hBdUL-9A2Fmi3Iht6Jfotft_NqnCzTGICwcsuDsmxbIx_mqBBP1PtZ5DtL6xdY-yEdxo1SlhXjEtrqwSdtdu5RIMfnDLAPgttV7jjfHuFCJut1o5M1WwzJ-_oqYCsqlF88cnJd-bnUs6wJFM7oUkIoibMBijKDF3DSdBmfb71nmhZYIs3UV2_kqHd31dT9lxcnTDpjdZf1Pkmpxfq14i5ByzeaU_8zumBFhkJH19OuxoCIyyKPvhkq8P22OEdm7L3WeW-L9EUOrNvs8ibnWQX6gs7JYVR37hU9EK3TJ4BYbGD0xL1_ZhiJoWbcgVboQ3-mx32-VtJMBfN9JlGOOaq_VYY1p-G5G6CcFMALavEHdlJz_mo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=Qgxwvr9l3FTBuaUfrWiU3E0CtD9uSD1Ph1AhCo6B1xq42N0NPEvlr2yPEUgj58Sg1kYrYo2C6OYWUjpjHrjznCwWqhzpJ0e_naKCiwTZ_qcR6yg6OmlwyxcpVAbDIhTyHZAaarPh00AcTBG9W-4fPW6WWGzfMp5uR76-X6bMaPP0p8maZ-7gln7Q33izHizuTUc1ReXmB3dX6L9ZZA3G8ekcg54MpzU9EMNl8QQKz_5a08X2Pht5CbNoKK2zAwFLpUCdiX_-NxuT1UGTiirZaKSNtGblFxGtAj_qAXs6-bwJQ4oPz6hh3aHLB8hBdUL-9A2Fmi3Iht6Jfotft_NqnCzTGICwcsuDsmxbIx_mqBBP1PtZ5DtL6xdY-yEdxo1SlhXjEtrqwSdtdu5RIMfnDLAPgttV7jjfHuFCJut1o5M1WwzJ-_oqYCsqlF88cnJd-bnUs6wJFM7oUkIoibMBijKDF3DSdBmfb71nmhZYIs3UV2_kqHd31dT9lxcnTDpjdZf1Pkmpxfq14i5ByzeaU_8zumBFhkJH19OuxoCIyyKPvhkq8P22OEdm7L3WeW-L9EUOrNvs8ibnWQX6gs7JYVR37hU9EK3TJ4BYbGD0xL1_ZhiJoWbcgVboQ3-mx32-VtJMBfN9JlGOOaq_VYY1p-G5G6CcFMALavEHdlJz_mo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=QAYw6mahpBt_i4BPDd3xVfYrpmDqPOHGJT29thvNWNUHHzLECM74MFfwoHbyep3NKNDbsMMpF5CBB-aYp7U3EjV7illLnrw_6XCA2nGjXNxPT0Os_bz-VqZLWtyIWddxrpJi3I5VXyEuPDpNsw1Ia9v0CfOZGUMHQoZNGvO3u9Iv6ppvL3YDkMfWj9KgH_jsHpvV4BuVivRs5l_XkmS7QsjoFWLpXTKRDTt9iF4RWdItzPe1RKEHwjxO9AbD-JeUm5S4OdD4PH6PFMfWP6g3XIEWD-cz5HEy-xulcV7BdbRtdTWa3AHzsktzlt23dBBhOzMFZ03oGKHbYnvFI3hK0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=QAYw6mahpBt_i4BPDd3xVfYrpmDqPOHGJT29thvNWNUHHzLECM74MFfwoHbyep3NKNDbsMMpF5CBB-aYp7U3EjV7illLnrw_6XCA2nGjXNxPT0Os_bz-VqZLWtyIWddxrpJi3I5VXyEuPDpNsw1Ia9v0CfOZGUMHQoZNGvO3u9Iv6ppvL3YDkMfWj9KgH_jsHpvV4BuVivRs5l_XkmS7QsjoFWLpXTKRDTt9iF4RWdItzPe1RKEHwjxO9AbD-JeUm5S4OdD4PH6PFMfWP6g3XIEWD-cz5HEy-xulcV7BdbRtdTWa3AHzsktzlt23dBBhOzMFZ03oGKHbYnvFI3hK0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6eA6H79BDW5M4Vpx33mckl6Y-Kwgz7ceWZRzdevomcAeAOTrYEoIiv5yg7ExOunYPJLopWpQV0-DzMcZwwf0EsFsRYZGIk5vVPP-BWvxk6J05Jkv7tA6rhV4gz-PWW5rrlAQbPZ3jb8V93SrYfGMXZlXZTgyHosuXicEhEcg6ntF4_99kVXwKEjVYsb7SZoBi_X9AWB0oAzgOSsXEG_2vWwC3YCR3R_dDQDaQ89W-8TYLiIM8baMdkAOCOZ7FbkrdtW7tlu81mC0E6e8mRVzxa9bIcjBwUTQQHsDIexP2YebQGtk9Dh2POwwuL1BFBXLIl8zfG2EFRVdu-wnD6i9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyIjAAeahH2sXp7ibEdHApE_Nh9Cj2BDvWD7w3cQYIMBCeCiwIqMjyP4cyIQWyza-X_HWc8nrvnP6wk_mIMfbTOdd8SOSeZ7IHW6uMBfcpU8GY8dMl3NZTR_YQvhllkqX1kDzn7GC6vXIwzranhylRMLfzj2XSJKFRfKZPso949f0Lj8EpmT4-5XgQiveVk2nKC723Hs-Eu-oagU3hi4QpkgYrZEZ4ohsqmwpfM7EtO4o5Y1EEmVAmWtsGthfOiriSqxK45uWnrBzWfKADnUflGYciYqYF4ZUzzuXz5egvGtlkOsdfe_UD3ofljzBeUbuQ2ZWO5sm1iXppTmrFvxgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIMjO5izrOSu0fkOuXgVw4Ju4Y7i_erg3r9uokI0Ph7tt1xVMfJcXg7diCJ-kb-IJvybI8DhimYgKorqA7TWE6JhXbPW6NVIRoiq-MXZX4558rK15gLRIm7uDvl6yIS8HyhUooA_ReDVQyn-NsPPIMBz2Knqk6n4ygCxgrk6ywjc0IBKq4X8CVYSoSuAyboIa7DdRjf1vLC_94lc7Z6Ya_Bq89Ni4SPYmvAefkJQ406hHzjaA1IX1cKrprIJgGCHtUIwa7_hK3v-Z7xupu3RtOpvMxSp_sFrn92FDEVyss6egIaICtDmWINYbpfQK21wHv5Pvb7BaNY56OABFRjH9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_xZfux3mCNo1RD8rGvDSC36HggzyfnucFJPUbRfTH6yd5_fFQiMi4qb6DVu67jShzjgt09vp5vzNKsKaABUxlqnFolsBluiS-xAzJ6iU0dGSfWs__2Pn7XZhHVmlvEV7hVSF8TtAg6Rbui__Q9bopNtj-TPJHMGky_SAHIoiiSp5zDiN_yKLSm_JCf_b7lT79kmY6Jujfks2U0MDS_MIz-smEIffpc_VpD4sCx0aXGXKiJrqgOtkdQH4_t_mSPcDsAGJnP69Xc3BTeohftU49scno1hZbJuiBP-MUtESJUlSvfgANqwHh9bOo0FcVG6RRcJG6UsUmXst9Uw0t8uUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5bennULQD6eOT0vFVHYSudw3j7hKGPp6e4_D0YmXo-fQ8bev-LiDNRRYvNCRPZWluZHTVF57g0ajHf8-mDB5HZfCeCpyWEIrnXlcQu5r_tq28NLD41J9GyYQ1dwkbHSLYuBCZ2lMdShBldj9ncsjFR7jfTLA3V0_Wn6Nh1kGRvLtEW0Yh5cuDR0o43can0LVZyYI63R0Zr3Vc0vghiCpzuj4NW2xPa3ICqGTV4y_6q16wqQ52Ev3NkYQrrLrimq87KChQG15j0032APZKWvc9T63774lhVvyL712WF2PD2Uiikxq08ahryYtGveMzUX88MpKQicsYaHQJ5Rds-TIAGY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5bennULQD6eOT0vFVHYSudw3j7hKGPp6e4_D0YmXo-fQ8bev-LiDNRRYvNCRPZWluZHTVF57g0ajHf8-mDB5HZfCeCpyWEIrnXlcQu5r_tq28NLD41J9GyYQ1dwkbHSLYuBCZ2lMdShBldj9ncsjFR7jfTLA3V0_Wn6Nh1kGRvLtEW0Yh5cuDR0o43can0LVZyYI63R0Zr3Vc0vghiCpzuj4NW2xPa3ICqGTV4y_6q16wqQ52Ev3NkYQrrLrimq87KChQG15j0032APZKWvc9T63774lhVvyL712WF2PD2Uiikxq08ahryYtGveMzUX88MpKQicsYaHQJ5Rds-TIAGY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9JMu7xrwMBoqXKmLLOMIDkFu9hKenDVdnmj13Y1alqPGlWfrmPeQQm83Xq9mOiPxVSnEjGjvoGneK44vp8m6bFXHkBpgk2tJFdgYtnbQ3oDbF2vUd4zLd4mrfRZzcE5n7zGNre8-xuTEkTxn1a8ieGcElAPIs-eOnmegkVhWcpEWKtwu8qAJm-4vb4mvJtXmhc8bSAvA5mK_g6o8DJmUMUd7AOJQdAmC-zGTyS8XVrQqwfotTmZuXrtM0Fv557uY8Z95BO2y4HorKjtZPB3wtzN2MGEK9ahWu_OJG8dURhZDN7k714qYTi9AmhvfOm3FC_CDktTQqJ2OZggAAUDXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5aQt-97_eCuHCZX1bgB-0h2La9rRkx6WSoyD4FUic8oNXOAqC2W-ZTeldYWJM8lEvk8FNMqgEE_RaXJ2YP65jCUpQDC2p8h5WBeHA_wRUduLFxTyf8_HNt5YTCAKxSQ_z3gqWTVo7njwrTwa0bAjqykToBoLtAzqDfMJTt1Nx-1ihe1-8FM4RRpvWfrD8V-zLVMW-uwVG1eCEwxKhmWTx2u8ldPERk_9AVWS-IIesYU1-hxsD5B5atqf8uru88uO76y3I2dSvWfzNam1_7bOTcfLsbi-Bf5ifmXGmRjY9NphkY5JzBC7Qj1aDJIl5S0wZpoN5P5lm9sLYg3SYykZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=KuTv6JFFUrGHZ4cBR0Qmv9RG9LkDtzAj62-4HUSh9l5aQ-lm22Zji3vg_fMtlLVZwAQHclidhtvY5shc1q1GKbkT5_Iv0orIG6uXBZEiDW24-mBbNiUYD6KTlwubAcqlkUHzRxOgRY8ZHGWMwTWDn5_eDJwPc6i2Ef1PZuvAqDAwf5zfsUYlajNsF-yLm_rcyHScN8-150IQqNKxxPk1Che9DAptnxfx5oqLspUwATt2LgB_yTHfw6jbF5__enBIxKhBk36oiLxcquzZ95kP0NnDEA-O0_kl9rEuBJpywqib1Zn00oE3-mrax5CBtd4ZlnuGWfDf5xl-1c3ikOnNvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=KuTv6JFFUrGHZ4cBR0Qmv9RG9LkDtzAj62-4HUSh9l5aQ-lm22Zji3vg_fMtlLVZwAQHclidhtvY5shc1q1GKbkT5_Iv0orIG6uXBZEiDW24-mBbNiUYD6KTlwubAcqlkUHzRxOgRY8ZHGWMwTWDn5_eDJwPc6i2Ef1PZuvAqDAwf5zfsUYlajNsF-yLm_rcyHScN8-150IQqNKxxPk1Che9DAptnxfx5oqLspUwATt2LgB_yTHfw6jbF5__enBIxKhBk36oiLxcquzZ95kP0NnDEA-O0_kl9rEuBJpywqib1Zn00oE3-mrax5CBtd4ZlnuGWfDf5xl-1c3ikOnNvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYzr7M7Vr-8p1aYEaYVFyeX8jQxI9xJGQVqq4XLzV8x3IW9RLWpavArgIQ5tNGdrBXO6tCUWnPhWV0Oh6fKKBnlSyUetgTL5_v_XnUy-WZWARKPdCOMpi_tyFdnHnlhxVOvgyiJk99LeKCO-viUupajddbBEmefoO4fl9xkuZEEVpgTrWdB3w2AwqCaHEOTrC6kHGEfOQgcPyR0E2OIk9dMWjLJFouj0zC70tQz0GXCtktdjR9xCk3GIQg5PhtnqDxq008kR1B8CydPUgygB1sWkAlrg_lu0CjU3FOnwicf6VD4kRWtznT73JqoRDOrQn00CY2WlES8ADi_5B-Jvnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/od2uAsq2aSZRb9AYqLlCAKdnA5TGs7TM1zAbG60hobfOkVrM88cBhkbuhS_VW76UndOiR9eOlWgguObI4BsftGtpVXFYlLWZ8WG768VyDJJIMEmrNobkiiX29n2s9B-d2LBnRikEB7GLK1b3KoTdBr3VwduCmzko7B2-oqwPxct9sjWcJqxqtcVrN0C8oexCHRqPqnZHMLvBL8pxN0kY3ZVy_RwrRtPMQb8txmJzmrzYdGZwFuUlOABoLkImWxbxq3ZH5JuzqemVof_ft0Erv2ZDh9CYmqQjyBja7i9EcUzAiFZTSX1w-Hx2IwI0MS_dQUTeLrnL5JoJ1YtmOcIMPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/shi-AZWMMmOAVxT0ZdnLYLbihvtCNgDn0e1RDfcjFfYmei-w3UR2hiDfxStWWabBV345PZlwCKD-QyjQWxjBgabmV-LG6b0L9NtvI12MhFZKawizeX9SDRkSppGjwuZQc3tavNIGJu6Fv1aN8psLBPF4ZqMeHujvgrY4TPQ_R9Yb2fDNOt6swemzT0-FexhqR21e3Hor91BRFc1jb_4LBmwoMpA86vKnDOGD5RZoDaWOMbrC76vlUvV4tc-z2osN19uAOrCVWE_ZvLGBc5rnWgw9VubUJDiVMR_WscjKXU-8Dk4YKZebyXAVXAzpXqlHmWYrhrFtC6YryozF67Xk6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=WOupGGHMACwl-QcavHjQncU2plppbikT3DV5J1Ky1AYHXhlVU9YSbhMh7JGW-5ZRYnQnt4rE7bZ940wEnzwquVSQwy8T3j0WKzs9ipwrAkkXz9WAhrorcNxPhBcG-NKPRSHJILewbrXE4qH7SCfVzHB_aWUzkAG6ZA7PYYlGYXXF-OdD50MLvsdustqbjG9LY9fmrR9kWJpo3xmR5XKr85RpE88_ivH7OZnLWkoa3YZkCmWL-goh5C2LKqgzKhwT4LaAZkPUKO6U5Q8Q9N91hf9OrCrMbbQLg8E687k5yZl3TbSdkYg38SMc8Q_WvsZbyHNjbc-5mEBMIOlpBRsofw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=WOupGGHMACwl-QcavHjQncU2plppbikT3DV5J1Ky1AYHXhlVU9YSbhMh7JGW-5ZRYnQnt4rE7bZ940wEnzwquVSQwy8T3j0WKzs9ipwrAkkXz9WAhrorcNxPhBcG-NKPRSHJILewbrXE4qH7SCfVzHB_aWUzkAG6ZA7PYYlGYXXF-OdD50MLvsdustqbjG9LY9fmrR9kWJpo3xmR5XKr85RpE88_ivH7OZnLWkoa3YZkCmWL-goh5C2LKqgzKhwT4LaAZkPUKO6U5Q8Q9N91hf9OrCrMbbQLg8E687k5yZl3TbSdkYg38SMc8Q_WvsZbyHNjbc-5mEBMIOlpBRsofw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=WiHXnjJ2FX_wizq6diLLhreMLf44c7Nv2-sJkFPSOC1a7ycDN7QZiAgKBcj4uHqXkTrR3n2tpE7E8K9Bm_2ewAp_a8mrsTaSa5ZwzLxivM5xwI-vMzXVSjGDIBIrZAKkW1kkL6sxqvZHBHJb945ER6qYXEXSThvqqbt4wlX0KVe93R_aBcqW21x3Nsz34D9QhBdtQb7IeOa6qw8qqlANv5mYQ7JBWHObqhIyU8BhuBUuYoIEAfWI7lsBN6g7QJ3HR8Wxdf-54gzeVWjxodrOnt5TIPclqt3hMtD3YCiBYep7EY28LP_I2ObdW0IcC-mRh6SUVIKgHfQhSMNnMWQn6IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=WiHXnjJ2FX_wizq6diLLhreMLf44c7Nv2-sJkFPSOC1a7ycDN7QZiAgKBcj4uHqXkTrR3n2tpE7E8K9Bm_2ewAp_a8mrsTaSa5ZwzLxivM5xwI-vMzXVSjGDIBIrZAKkW1kkL6sxqvZHBHJb945ER6qYXEXSThvqqbt4wlX0KVe93R_aBcqW21x3Nsz34D9QhBdtQb7IeOa6qw8qqlANv5mYQ7JBWHObqhIyU8BhuBUuYoIEAfWI7lsBN6g7QJ3HR8Wxdf-54gzeVWjxodrOnt5TIPclqt3hMtD3YCiBYep7EY28LP_I2ObdW0IcC-mRh6SUVIKgHfQhSMNnMWQn6IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZhljYK7HS4aaQWcmgTp3vR0XTuSqWJQikSR4G8bVHKR81kVKjRjRA66KgPI9gd2ah_62JVGqgy8VTnkknj4SB216E4OQLQp8f2gPiln_4_kGM43VquYg0YgW-9-2XkOR7Q0PqNNmXhCWnUYt6krVhW-9NFq5M2ZbJhwsS-5EDWm1kBh15c1_xmKz4TNLkw0-Z0Be5CjOVH9HZBgly-cyvsF3rM41sSDe5vAOtZmfoaYEzr6AOkl5QGkLJqLfvLQaW8MlBrmlLqiIeN23I_cNvI_sBsCBQnx2u8YoLMdawffbg8ycxa6v5Q1qBJccSwvVWN5gcXRVhkhpjatlDRsZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPQ_G2r6OG40Bc8F0gN4w09LVgvX1TrY8kMI1sT-YUo91TiffVy4uW49EYf42DTFOSB8IlSkvDzthdu8Pi2zcur3ADdBKSzvL_UpXeKXLpyrjQRMmeTj4XUcAvcL3j3M-sF6iQLftGAi_yJDmZJL-gQl4hVyPB_mY_CjvF0mf2El6DVPhocqzBesx8LNPpUMbeUJllAOEuJTkgWhgE3u5qPi1dbhGkD74v2eggrsmLvLTN7UqAjSYhnKjoETRSyRZKON8q-md50DV0LBh6xbzzASnPMwUDz0j9QM1DfdCo8ZeW4zWk_p6NHlAxyZ3cAmONaslEBTFfSDRGFr8Iy90g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=evlPwwVO61Fj4F9eiKi0QgZdktHFbUB1j4hnupQex0wZAOMEknWBJOVTiedsTTq-yfAf76sUhom8eU1kfbGD-vvGYyPp7ssk-NedK14-NfzC9celoWhgiMsg0pLQsbOZ6TAqIQGiOrFU_19eNgK_exncuSqE2rlNnts0-ZwULS4Jjhm1iP3mbl4fuJ4JdkBsihaW7kAW97-gTvSNiTJRbSy9RJNGcqyn868qGhDI-Cmb9pm7X-_v0y1PPOPO9nOV51xNMlQfP-qn-HaZyv5QCY37O73ou_H1cQVGHqw9VLfn71NHNk2yLVZnpet7MTzg5j5Q-pAhv5BYJ6tHzkVvHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=evlPwwVO61Fj4F9eiKi0QgZdktHFbUB1j4hnupQex0wZAOMEknWBJOVTiedsTTq-yfAf76sUhom8eU1kfbGD-vvGYyPp7ssk-NedK14-NfzC9celoWhgiMsg0pLQsbOZ6TAqIQGiOrFU_19eNgK_exncuSqE2rlNnts0-ZwULS4Jjhm1iP3mbl4fuJ4JdkBsihaW7kAW97-gTvSNiTJRbSy9RJNGcqyn868qGhDI-Cmb9pm7X-_v0y1PPOPO9nOV51xNMlQfP-qn-HaZyv5QCY37O73ou_H1cQVGHqw9VLfn71NHNk2yLVZnpet7MTzg5j5Q-pAhv5BYJ6tHzkVvHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYlOCchrB3XX81FBv3BktikNKliMxYwEbvVKAHB3JiLh7RJe4KVuFmGr54f8_Hq5eVvtR2oWFeIX61DdIhbhq-TZZh2X7BMo3OCB2z2NopgkTKhz21SxPGGKYFatK4ViAdGaoKZSbYbNwGfaDUNGOhyLWr_RNKZFb95WtXnzIYWlcyv3x71HB7zYiqd6ycp_BIqc4PlGRPs_4RBx_PTYa5szMNQjXIqVVAwgoxHXtKDIKZLZNJ0cmCUrbaSn1SJUPOytZ_qNzW6O_CfpJFTRXU81jnNSQbPK1RUNAAcbUgQ8AKAZFD4is0XaZsuuzl_JiDOfK_fv80tuBlHKYvWZZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5PxsmF8fYPW54LbUg04rDIlYI8_Covl66QiXEiCr-MGj7Y0XormEiqkpU_EBndbgtX5PzVQ31JNgLuuueQ3f67_o6Qryj13NPc5P_d6dGF1U9u0CfsfMe9S8Wotu2WGDzljVTM4Nz0vAqSk-5EoCrVJsvebtpGYpzi71b2WsRSLemII9eIGjTdarelMja-jLAISRzot9kWM0CXlxoGow4bGLD8gM8fetT9_oLlupi_txIqyncd2lIlS3rhG9RRbFmyXHlazpoMWNXx7Q425GbCuKkzQGObcQ4SP5ojNWbhMMD0Ps2VxWcgCGJ34wXpfZYIC9zfKP_cenYPJgD8mDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ca8sMDigaR8AGHWCps16fXlZIp7yjpi9wVp8wE3bvzhH-y0L-dX7dKXGTZZCW5AXmRW6M87agPAP7Ttbxa3GgYWtp81VfEXa5wUQyqCRmjXSfR3O_Ud1wn7JwtZoiL56gwiI8V9jeGqB2tdCUUfNEgE53PLPg0lDxlmzCC65IcS3K_W_tmbxFM4j4bIS6Kkol9jF-PwU9ieq7dSyGvvz6FnUNNSP96DL6gMSe97HHJQHW8F-H5enAqcWk00JD-SF5o2gtLT475kknmB50UKrELwteezbkmmvgyiOYrKD0ZwY4H3du_8Q8ovoC0tF6a_iBG-1is6hvqHSe2Tnl12ohg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLZxpAsE91-HchOmyqIwavZ24HJHadq6Bp1ix-Av5knmDndNdp6NstSJ0KWepA7UzYrOm-j_sNIGO3jMPGr95L-9taZPl_tLCjm2gBt3pEAtCULtjqlG8ixNLoq-Cd8XAHVz74pOHhh75NrHA8TWTXj_NzySPAkUodHmilHKWsEfCCQcrSMI2piDtMg79trsvzoTsVhJVXvVTm0giFjsNQjOY4MCv2139Eb6XHrrdcngRik3rJIRzy2d9rZNjBMxKeTbkzonkTNJ-yF1H-nZ1lvUlt0_QPXmmHuou4FV408lAVb9s3buz-4845rH_1HQ_EAhNxQg-wc50NlDiHwnd1PE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLZxpAsE91-HchOmyqIwavZ24HJHadq6Bp1ix-Av5knmDndNdp6NstSJ0KWepA7UzYrOm-j_sNIGO3jMPGr95L-9taZPl_tLCjm2gBt3pEAtCULtjqlG8ixNLoq-Cd8XAHVz74pOHhh75NrHA8TWTXj_NzySPAkUodHmilHKWsEfCCQcrSMI2piDtMg79trsvzoTsVhJVXvVTm0giFjsNQjOY4MCv2139Eb6XHrrdcngRik3rJIRzy2d9rZNjBMxKeTbkzonkTNJ-yF1H-nZ1lvUlt0_QPXmmHuou4FV408lAVb9s3buz-4845rH_1HQ_EAhNxQg-wc50NlDiHwnd1PE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
