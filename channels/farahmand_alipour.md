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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 15:56:08</div>
<hr>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UeEhMb5MMMtdBsReytDEPrXUtsaNYd3ZgLcAFoKm29D8sGrRU6UaLhCe7cTC8fLVNIPTQRsHdJ4L7gqzB515R9BXlwj4bTsyx5OZXDm05lAC1HoKOjCMxKSV3i_1GauLsMtJY39aRTyGYN3cOl81elBKfJi6U_DmD_dU12ypZTpIEKOZa4A0YfMAuOj9hlp4kCdq4MdT3BMLkOyetIIOOkaNdUkcwIs6-wK6SbUUR_G0Yx7FrA69p9BdTDbl8ljR8uSLU25yCfXg1mvDS36SRO7yRCuu9wiI_oeYsa62vyzQTTPJdYpbQ-s9b5KpjnVmzUV8ufX3gn6bkWGtSaNLUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به امید بالا رفتن قیمت نفت و فشار به ترامپ، زد زیر تفاهم نامه  و حمله به کشتی‌ها،  که با اقدام به موقع دوستان خودشون  در حزب کمونیست چین،  نقشه‌هاشون نقش بر آب شد!  خدایا عظمتت رو شکر!  اما در عوض برنامه آمریکا در پاسخ  به اقدام جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/farahmand_alipour/6518" target="_blank">📅 15:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6517">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwIaN6o6q6bn-9uCcTMpR8mSdg1iA534mGRYSEAMaBCECUlM56XZ-5-T7MIEcKMn0yLAKu_rDAifejaKLpSXmV7McjFxdugTAjTw4dPNNNvWBXO13e4biRch79ZuCtzuCiayZwLBKw7Dti9prwrY6TYmf1lyMv_0mFYxO4VLY6Mh7MOe2ckcm_WboY398ZfqBp1iznxOfYJS7ZT1lw5uoW1t01dcuFqaGBNhfbw0aI8Ogv3o2Q3I4OgTbAoKZHruJ8WbEveaRpQ2-NsNvRGr9ntTj8T072dMijFdLQ_jVyzGMWHb49Q-HEO7iOS4J2OPjb59ja2wSNYFtyG6WREocA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم : افزایش تولید نفت کشورهایی چون امریکا (که رکورد تا یخی زد)، کانادا،  برزیل، قزاقستان، ونزوئلا و….. است!  نکته سوم ترامپ!  و به نحوه مدیریت ترامپ برمیگرده!  بازار نفت به شدت حساسه به اخبار  و به انفجار و ناامنی و جنگ و…..!  خیلی وقت‌ها قیمتش «روانی»…</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/farahmand_alipour/6517" target="_blank">📅 15:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRiInt98MsxwvNr7uVxgWJUBuPZOnpcnYgUUcRXoZNF2PURZG7dJUCvB6NWKz8RyOyrl3GgRPt-p-bHlRG8HGgxXTIzlOUCNCSHrA2qD8ohFZk4Xv3Hg6LV7SQIVAh0z4yOpvAZqayduz8ZBdmyiBU86jnumMZU89sNhnwzPlz5L9clF549E8gMl-GXfOPiPcNXWYo4g3UYZCfbcGFwYtZVT06RSa11IpRDKnwxG40RvonMyF51cQur4cxMRRgLsOzLzwIodg9n5GUMrAM1XHm06IB74vLAy9biH9Az5CdXVZGTANCDbsxBh6LfQ04XxcJa8tvFOZN59sj_b3zO93w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف نقشه‌ها و آرزوهای جمهوری اسلامی  قیمت نفت خیلی زیاد بالا نرفت!!  میانگین قیمت نفت در ماه اخیر با اینکه هر روز خبر حمله به کشتی‌ها رو منتشر میکنن، اما بین ۷۸-۸۰ دلار باقی موند!  یکی از مهم‌ترین دلایل اینکه قیمت نفت خیلی بابا نکشید دقیقا  «چین» بود! …</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/farahmand_alipour/6516" target="_blank">📅 15:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BZOd5cb83U6H5HSsLqWjepo3SgyQUS5toG0o1jtX09pyKd9imRC_6SS2T5SfzI8ULqj9ZT0oG5lC5KE-l2Oq0KBsU1pjaZg6y_ttBrTjJOsFF49b5vQFnoOD1CGQcPYrp3o-AAqlL-6yu59DhMQZUA8SZkCQMfFN5BrjKQ9bGAHNW1gClLRBJfij6sroVvf5_xM_sO8jbv7l-LGdNMqTWr62lP7nkYdaMPNiUH_VRmgaSWJGsA1w7fe4Yjsag_1k2L6i798ol_Qt7CmaLMcwEuRurrvE0xbNg8EFX7HzpMOPoOaRlziUuicilUG4QnOCPgj1uYpo4X__kXXadY8EpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A5_NsLJY10WqwGbIRODHAiqJAunuy-KNYma1idetQw0T7dRh9SokxSqIgCwT5bRaRA0xBCnZC0ac-HMw9dIoC7Gpdtapjx2w1aQclKEamZGMUz5koep6fDlEX2mWbYqooOROpeJyINA0EiayIqYZZVydFpoo3uUyFELkGt6AAkB5ITXTLtdVI6f-IGwqfbiqMTKK6iA6AD9H5vFmW7EGE4xvWPxxhfv0_jOn3XX5ZSAEIXL-41OhT8xOB-4iu36RWU4afOXwRG_XY0df-IF1b7AmcFplguzQkCK2cqd4nt10dDI1lFLipcs9iCmxpFV6k0CZMoOVEh_79aCYvOLU0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جمهوری اسلامی با امید به اینکه با حمله  به کشتی‌ها و کنار گذاشتن تفاهم نامه،  می‌تونه قیمت نفت رو ببره بالا و بر انتخابات داخلی آمریکا تاثیر بگذاره،  حمله به کشتی‌ها رو شروع کرد.  تا با ارسال پیام  «نا امن بودن» تنگه،  قیمت نفت رو به شدت ببره بالا،   حالا…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farahmand_alipour/6514" target="_blank">📅 15:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.  اینها دنبال «اتفاق مبارک» افزایش قیمت  نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.  اساسا با همین منظور شروع به حمله  به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/farahmand_alipour/6513" target="_blank">📅 15:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farahmand_alipour/6512" target="_blank">📅 14:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.   خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.   او همچنین با اشاره به اعتراض‌ها…</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farahmand_alipour/6511" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farahmand_alipour/6510" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2SgKn4EnNs6qzviU80TCo9WFcTQFjEu_EReNTw24Zdl13i3skjsQK5m2p2k40jOI5aCoLRn2XBSshIKOKjXla-ZDxl1KycLOHUAmoIzEljKdqR7IrkRiCeVwT_9Z9bEeNlectpAm4R3uIbu5iBi_SwHkouHi3x6OII4koxes07nbV_FneL3hTsvFyy_hAciLzqtVHhorZqHP_2afJRZchgveexLZBi8KAjUzyUUh8fkKwvnufhomjQjiW9l9jtKskFGMjA7v1LNSxGGsOv6ISYdnFVDJbDWkkj6lz6U9zZUKBVZvhCm5c7-UtBLRF9hyMPJWAaQHmxB8dnanyd11Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب PD که همون نسخه حزب دمکرات آمریکا در ایتالیاست،  هم چند هفته پیش، چند مسلمان بنگلادشی  را به عنوان نامزد خود برای پارلمان ایتالیا  در ونیز انتخاب کرد!!  که آشکارا شعارهای اسلامگرایانه هم میدن!!  مشکل ملیت و مذهب این افراد نیست!  مشکل اینه که اینها آشکار…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farahmand_alipour/6509" target="_blank">📅 12:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtvY7pvASyoNzE1MgzbmI19FAUjQSKLVX8nP1mr0oTry5Kco_dGNHIQ9lAHysx--cf0Z7hZQSy55Vg8Bgz-QvFTNoUyQeLDjQ8P02-Ezl5HLd1wFmqqIU_bAy3nN5pNfF1nfEzGD5pexnsHeZUlbHlwLvpsgFG3hZM5kUEESUUUQA_lNis7IPYPF1SS7BD3UvdFDmxDU3raBS55ep2ntzcFhEBxD8jdZX_f3mwq1QFKbRObBZF_RWkhZLuqLERybPOSpyBy3vUrU7C1FMffld7xaCTB2f3TL_qaJWlYieYDODkb84q25478JeTGCvAspVqpdIXQEvfk0NNyMU3-Glg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!  که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farahmand_alipour/6508" target="_blank">📅 12:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6507">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farahmand_alipour/6507" target="_blank">📅 12:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای : پزشکیان ۲۸ بار استعفا داده و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6506" target="_blank">📅 08:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_0-ptsJ4efHkAQo6huPuY_EM4QKUmw1vw7Fw2yb62dglPo2dDtFjm13hBcPVJAYPoD7IXEcdAK3YJ4IoHY1IcG1oY00nzsuQPf3WsFcks194zbKE9VNKMT3gxQzCG3qFkR4ya953IR8ekNef8XFXWsflG52MVqq-Pfwg24Pf-SokaCr6QI0O7kY0_gTyDIeIGrbkgbPVbeW3WALodJhZXGJYsSl2KaJhSLWbLPHWO9JUWQD2QdCAyPo-vAn-LsqVDG9AA_RN7iVdVmu_rtZxSH40UFFDAXQh9545lW37HDkYmQq1bSSN1JeHd8Lbg_pghpsu5eYS4FMh19R7wiWjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توطئه است!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6505" target="_blank">📅 01:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">آسوشیتدپرس: مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6504" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBBCPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOFfPu9UP_Rr5RkzqDCAgWftVhz5kbhOCzhtEQjT8Bq_pc2sbfY9FGuQu9faWbfc9oCu4C45qhoocy5uISJGosdQtMzII3tI9il-srGQ8ZOtQT5NeAkN7ACXuhMMf865cYEXECNr4GXfZNOU3ZY2gwSfifESoBNz68-qbAtJPq-5C8ToxDW7T4Ij2YxEgyMc9QmTOXK49QT4GDmCyVxR-SMnMifCECnP1zFtKTdwIo2Ojqbd5UC2QnMkd3Y730zbc1UZhDGH-oYcBsFMHUOAWfWSz9aSA0swKKs-nAuqknBWtaI8LP1Khg_xzXBv6xplyGuttt_Qx_emdeL1mqHaxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6503" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f29785e012.mp4?token=F9d7aGP3aNdl6aDp1bhYUTP8C7RShiHwzvdCxJsN42STQnfgQ7CA-clCl6_FLT_FsQzDEEJmK9085VMRzMl7NXTZXo9x2VwU0RWSe8XSuHf8QgLPla8OSGQCOsOOsMu1h3MYLkRoDEULjtpjKCdpOKYLE2qVdmNf-pPVw1Afx8CN6z49oXKgnJe0XEIHjh57D3MYucOf9fVCkSdnQTAK7q7jkjlvTHEDMlUxwbKMe5mQz226Zb0Y8olVFngtGGxPyvLBLoCz2kxLBBjg_53YV8vhvZ-9g0BSuBCBK-YtG8CaJWufMsE9XNc-YdgV6NKsQxPBq-tGbLg1nNiG-UnDXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29785e012.mp4?token=F9d7aGP3aNdl6aDp1bhYUTP8C7RShiHwzvdCxJsN42STQnfgQ7CA-clCl6_FLT_FsQzDEEJmK9085VMRzMl7NXTZXo9x2VwU0RWSe8XSuHf8QgLPla8OSGQCOsOOsMu1h3MYLkRoDEULjtpjKCdpOKYLE2qVdmNf-pPVw1Afx8CN6z49oXKgnJe0XEIHjh57D3MYucOf9fVCkSdnQTAK7q7jkjlvTHEDMlUxwbKMe5mQz226Zb0Y8olVFngtGGxPyvLBLoCz2kxLBBjg_53YV8vhvZ-9g0BSuBCBK-YtG8CaJWufMsE9XNc-YdgV6NKsQxPBq-tGbLg1nNiG-UnDXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اثر یک انفجار در جنوب لبنان ۲ سرباز ارتش اسرائیل کشته و ۷ تن زخمی شدند،
ارتش اسرائیل دست به حملات توپخانه‌ای زد
و سپس دستور تخلیه فوری روستای المنصورن را صادر کرد.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6502" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6501">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=IpRhCsMC4c3wKwKUnXR_ZhJjS276aUs5zeyt8wuY25CENPWkGNns_A6symthQLnmH0_MTEZZ3psGxiwWTqCHRjOPCgpP8iztlI9juVLHKQCBSTmWncqHXAuY0uq5X--kU23_B0OH5uCzvM_EsAObLORsGOIe1Lt_k53IEbKItrEmIKYjkgV621PYgcJMARLL4u8Fmqfux5MEme_27nQqcaFuXC5uVWLBRQ0grNlqke6J9hs4LTo8k6DTnyVej4vif10_k1k6Md4RxqMwoHQB_sMCUr_aK0DOnn7KBMi1teFJ608Mjsg5-ROFV8Uv2ZNGH-BpnwAUot9F67bvc0Uuiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=IpRhCsMC4c3wKwKUnXR_ZhJjS276aUs5zeyt8wuY25CENPWkGNns_A6symthQLnmH0_MTEZZ3psGxiwWTqCHRjOPCgpP8iztlI9juVLHKQCBSTmWncqHXAuY0uq5X--kU23_B0OH5uCzvM_EsAObLORsGOIe1Lt_k53IEbKItrEmIKYjkgV621PYgcJMARLL4u8Fmqfux5MEme_27nQqcaFuXC5uVWLBRQ0grNlqke6J9hs4LTo8k6DTnyVej4vif10_k1k6Md4RxqMwoHQB_sMCUr_aK0DOnn7KBMi1teFJ608Mjsg5-ROFV8Uv2ZNGH-BpnwAUot9F67bvc0Uuiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی منطقی بود!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6501" target="_blank">📅 12:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6500">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=kB4dfD8yCQkF2RCyzHJajeGGeaspPfsUf_llYjsY86XucisTnlfMuDsZMTV3moHnsbf2XzkPZFme-2e3UN9WZian8wJaHUnUIvr3AKK2kfqQeuynB2GtDEwgXiKk_tjk6yUWO1yI_ydc6hFuMeGuicIBRtVKvTuE8sbWfG-ttJjxhhSYdrvtO9Da5l0dUeRONirQdWgjNt6dD9xjjG1rKYer-P7Pr-ngqR2D9VlvpxZnIWVzf4mMtIrfsk7uYQKcQc7JO0jwmwUc-8KUXI4SIb-RrxRo81vYMgXgJX5beWNoCSGZughwNGlESe8ENXlRoT8rihkPvU8CEUETNXH3lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=kB4dfD8yCQkF2RCyzHJajeGGeaspPfsUf_llYjsY86XucisTnlfMuDsZMTV3moHnsbf2XzkPZFme-2e3UN9WZian8wJaHUnUIvr3AKK2kfqQeuynB2GtDEwgXiKk_tjk6yUWO1yI_ydc6hFuMeGuicIBRtVKvTuE8sbWfG-ttJjxhhSYdrvtO9Da5l0dUeRONirQdWgjNt6dD9xjjG1rKYer-P7Pr-ngqR2D9VlvpxZnIWVzf4mMtIrfsk7uYQKcQc7JO0jwmwUc-8KUXI4SIb-RrxRo81vYMgXgJX5beWNoCSGZughwNGlESe8ENXlRoT8rihkPvU8CEUETNXH3lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمان مخالف اینه که از کشتی‌های  عبوری عوارضی گرفته بشه،  جمهوری اسلامی چند هفته است عمان رو گذاشته زیر فشار که باید بیایی با هم این کار رو انجام بدیم!  عمان گفت : تو توی بخش خودت اعمال کن!  در آب‌های سرزمینی من، رایگان خواهد بود!  که خب جمهوری اسلامی فهمید…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pq28r_HDUU1tnm9TOJhXRfT45L-e0SZKLHhy-2nnSN8g3xv9KhOCBVwJEDrrVHGZgzkzUrSqs8Q-gOP6VPATGJ3SITWBXE7wYPIQxz8tGvVvUCcOWqF5g0iOJTvhyvLoEXMuYBJBC2RJSpY22_fJCk7UJoIg2OQGGG_Im63v308KEA7lD356BMlEc3Ydmen2PK_UcS3leUoTYPq7yKAVPFk3zCSPMNzD5MhUmPvXTzzlXH4jQylt2tTmnjzuFwqA2CHzOH9kewT0DHxegQozurckCeKaj4nChQzR4wnValAvt7jGwi0lyt1Jqf2fPw8V2vRdxvwY7EKh87WYqGmonA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlTaQd3YujCdMsAAdnOqUNnvnssX4hU42AsnMrjE4_DwyJRxnUyJxbfLkFCYaVebEa-89wweq3UcBMrotRbMGOx4w4ay8A4riqB38YIf5KuxbIZfreXxvO24ZongRCNK7rnmHkzqsUU8vubq_Q6Ilub5DMOZHfEUjClf0k62khXkNcV7R19s3s29pmDMedamUnOh2ngg6zmZBYOF-A_oDrI1LLeL05lk9Q6KCINFrNcmuMOMYX_1dFmKESkmMT8b1xAqSVN3ZAL5ypZeeIaaoeYVDcQTet-Vbwj6eFlwlu6Ai522R3g9GOmLrjFsmKBmyXAQn-g_xkv022RURZOlig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLNahGyWF7UcqcnDLCu9HNZYRFPxkLpGNItCZ1wry48AvlHqDYmOTyUydgP6068YgC-m5YGJtchqhJvF4SkuR5EQJxgHo-pauQ3b7WDOiN9rqUgrVDrxmtHwomLnfpVMFrG0M4BmGbmls1IAQfp4cRPvftqlbFi50MZ21xJwLycvQZaD0MWEoSTY_re88Jul4hLRFnsiKO9pHshlphcU0LRmt8RoFIdj43MIi6Tk-aWpx-u1b_WrAhkJPyp2mLBFIO2DGRh0053WEzqyRJWSioHu4CRhWjKM4ASkjEf_9Y5I883BeAzuOBGk6Xtly-3RuYvC3lAYeu-uxqrJWcrJVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.
عراق : از طریق خط لوله انتقال نفت به ترکیه
کویت : خط لوله به عراق و ترکیه و همچنین به عربستان
بحرین : از طریق خاک عربستان و‌دریای سرخ
عربستان : صادرات از طریق سواحلش در دریای سرخ
(همین الان هم ۷۰٪ صادرات عربستان از دریای سرخه)
امارات : دور زدن تنگه و صادرات از  خلیج عمان)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6497" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6496">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=V8KeysVryVPZCisIu-J-nUo-EXE_6C0vqHwZ3pavEhfklxtodFPyBI0ve8YtFHiQL2o8cTVWVywoJkUtnYUi71jlMmyl9sXpzDhQ-NsiCjoCh5qUIzjA6-V3yVRrIM4D7UQ1IcO4a0hJMDcuJQrrm_r-GFGM92jUrhiK_T9CAztiu18cP7413Z6Lt8a5qeIXrX4zTMnmD48MxlJUooz1UpJuYG2m61dkNfgcgOYgNXpWRlia231L1TMXj_v2FgCdxd7dGfHiD3CjDrVJI_9dg8mcoGXlH5K2aKIsvnQcI8P1c5zGxD6ubn-HD2JjX4HbLbTKpjSQZd9vyCsu44NxeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=V8KeysVryVPZCisIu-J-nUo-EXE_6C0vqHwZ3pavEhfklxtodFPyBI0ve8YtFHiQL2o8cTVWVywoJkUtnYUi71jlMmyl9sXpzDhQ-NsiCjoCh5qUIzjA6-V3yVRrIM4D7UQ1IcO4a0hJMDcuJQrrm_r-GFGM92jUrhiK_T9CAztiu18cP7413Z6Lt8a5qeIXrX4zTMnmD48MxlJUooz1UpJuYG2m61dkNfgcgOYgNXpWRlia231L1TMXj_v2FgCdxd7dGfHiD3CjDrVJI_9dg8mcoGXlH5K2aKIsvnQcI8P1c5zGxD6ubn-HD2JjX4HbLbTKpjSQZd9vyCsu44NxeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
اگر استعفا بدهم، رسماً اعلام می‌کنم؛ استعفا نخواهم داد و خواهم ایستاد
ما با نیروهای نظامی، کاملاً هماهنگ هستیم. می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و این‌ها یک چیز دیگر
همه مردم برای ایران سختی‌ها را تحمل می‌کنند!
[تحمل نکنند هم یا زندان یا کشته میشن]
یک عدد سه هزار نفری را سی چهل هزار نفر گفتن، نشان می‌دهد که این‌ها چقدر نامرد و وطن‌فروش هستند.»
اونهایی که به قول خودش بین ۳ هزار نفر رو کشتن، نامرد و وطن فروش نیستن، کسانی که به کشتار و ظلم معترض هستند، نامردن!!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6495" target="_blank">📅 12:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=i61zJYjSnGB9oYYwmzssSiV-3exBySCuo5P7VgZ_L-LhPagQY7FiOwwWLbaWiyNfGGKyanUAuP0ZoU9TscEMYJenXhORBTzUoy3HW_BcMC7L2s5qrGWPdzUqhL1p5askknWPfU44gsHBqSFoBsdparff5tcgAONUx-uLtpfwE2z6_zHFzIKiNw7likd1Xi_dPALFuBg8zUL0N0K0mR3c2Puycja2Qr6nLt7z-0ns2X1ZqLNCNIeAtyahgM2eVg8snsU-zEtR7BCm3Sj8WHnTeV_L9DoXOVxEThhSyqj8MlSY8e0ZBeeQUjLbPNbqiubt4F_wtn4y2JwVa_rFDYNOPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=i61zJYjSnGB9oYYwmzssSiV-3exBySCuo5P7VgZ_L-LhPagQY7FiOwwWLbaWiyNfGGKyanUAuP0ZoU9TscEMYJenXhORBTzUoy3HW_BcMC7L2s5qrGWPdzUqhL1p5askknWPfU44gsHBqSFoBsdparff5tcgAONUx-uLtpfwE2z6_zHFzIKiNw7likd1Xi_dPALFuBg8zUL0N0K0mR3c2Puycja2Qr6nLt7z-0ns2X1ZqLNCNIeAtyahgM2eVg8snsU-zEtR7BCm3Sj8WHnTeV_L9DoXOVxEThhSyqj8MlSY8e0ZBeeQUjLbPNbqiubt4F_wtn4y2JwVa_rFDYNOPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای :
پزشکیان ۲۸ بار استعفا داده
و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a204c96911.mp4?token=DYeKV69EBSi99hjxtT1vhiUr0DYHASUsWuC7iauf5BbRlP8Hygx3-8KcCdNgXEBIncAE9iac_lyG3AGmVC7G0YoNYGDaEurulSjhQN8uIt1HEFGwuBM0bkpT4hv9EcdLe2HSg8VbURY5JdigKcQV0wq6mrgdbtZjiHlY99djmBBlvcywEm3_nA_geMA68Av5BQdMUz5yVoDBu1r4iagHXJXgm14NZZp1imRzp7IGLAeHY-2VbaDwZtqnZcjcA3I13_MNnXbqQ72av84Y0gTy6r1fwlmS0A1AOCmZ9PZlg54zODUExUDFiQ2m2LZKDihs6sk08iFFLok62u9orSJ0Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a204c96911.mp4?token=DYeKV69EBSi99hjxtT1vhiUr0DYHASUsWuC7iauf5BbRlP8Hygx3-8KcCdNgXEBIncAE9iac_lyG3AGmVC7G0YoNYGDaEurulSjhQN8uIt1HEFGwuBM0bkpT4hv9EcdLe2HSg8VbURY5JdigKcQV0wq6mrgdbtZjiHlY99djmBBlvcywEm3_nA_geMA68Av5BQdMUz5yVoDBu1r4iagHXJXgm14NZZp1imRzp7IGLAeHY-2VbaDwZtqnZcjcA3I13_MNnXbqQ72av84Y0gTy6r1fwlmS0A1AOCmZ9PZlg54zODUExUDFiQ2m2LZKDihs6sk08iFFLok62u9orSJ0Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تبعیت از ولی‌فقیه بر مسئولان واجب است»
می‌دو‌نید شمر تا آخر عمرش
از اینکه در کربلا شرکت کرده بود
هیچ گونه پشیمانی نداشت!
شمر خودش از فرماندهان ارشد امام علی بود!
توی روایات اسلامی هم هست که
هر بار بحثی پیش می‌اومد دفاع می‌کرد از کارش! میگفت  تبعیت از حاکم اسلامی بر من واجبه !</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6491">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=dqeGy92s810jBbo5Y2MHQcoY8sUu5tKYOR_fvFpkrkcPdIjZnYhz-rR4Zk2JyKFkSTaXnDn8iuGwWLyXgPIWFdYzfpOVKYODU4pdXYygSgSg3sqSONbkIu2FltDJMatWOM_dL4_8q-1c7RIH2oZqspyyq4kH6Njb9sSjt2Mqg5L43FlAnv-OdHSsZobp1Gw7atBUlVSI7ZFjBbKL8Il9dNzcQkvRC6Ot1DXL68M4Znq4eR2P-BL98i0qIWE9sPjVDkZCx5xklTPQl991Tl39-FICv17jsiY67dCXkufRYzv7esTqPhiy1daYrpHFfKFhS5EIIGsd92QbF9aAOL0zbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=dqeGy92s810jBbo5Y2MHQcoY8sUu5tKYOR_fvFpkrkcPdIjZnYhz-rR4Zk2JyKFkSTaXnDn8iuGwWLyXgPIWFdYzfpOVKYODU4pdXYygSgSg3sqSONbkIu2FltDJMatWOM_dL4_8q-1c7RIH2oZqspyyq4kH6Njb9sSjt2Mqg5L43FlAnv-OdHSsZobp1Gw7atBUlVSI7ZFjBbKL8Il9dNzcQkvRC6Ot1DXL68M4Znq4eR2P-BL98i0qIWE9sPjVDkZCx5xklTPQl991Tl39-FICv17jsiY67dCXkufRYzv7esTqPhiy1daYrpHFfKFhS5EIIGsd92QbF9aAOL0zbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1YdFaqMoW9mWNQ8z5Av7-9TZY4aHV5J02GZGgTEk7-_QaZJAvSNI0KBpX4mjwcF1n3JKCehKBvr7ma7oQP6R9lg9gdFFIHkwwGw74N4KvaMKBQHspI_axYE6NvIJq707O1_43KExoczR5yGQnzBbWPSLwQaPVPkM5J58rUE4SHiumkRG3_N0NwqAEg8V7Iq-lOyLXvCYh0z2UoxwGsY2jQxEdFekzr882iixXZB1cd12ewIK44NYpGltBe7Ke7rumaaxLX_tKe0kgaVjptKqy7DMcLN1Xw90eIzbRr-7BKHVopkAjULIWx70QQ5jvnQcn1Tj39sDR4DbZWj43uTrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7XBybyHI78_JTFJsUEEP5Vr7L9-WBS52GSRxdzUKXLXe8BPZdPm1Ep9HvCrM66VrwOa-hOvJAyIGTNsvCiXd_IBbUyUUI0GBbxQOQfOPB2_nDSItH7c7-wRqcgf5lMPgBQfoR4NA93LL7OzZCVtqaQ04MCiLe7si7xfzzmuTih_dee5znr9U9OJWYtCXfpZq7lfSl0mUVpFQI3vy0npewMG07tYkSqrO79ShZzHyXRBmV73y6jPnHasSdh2a1UBXEjAtDACWvBh5xAdexGc7hFPu-XzyXXBPZLj4FbDeJlb9gALDZe0KEL69OKid3LyIlzcJlEmCpCtR_16VUCdeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZLu1I-VZv68B-fypor4p8nTd5mUb1O9pJoAX0twT9pv9yiqCsX3rwuc3NbLacaTg_WhL5ldKyualjphgAlMmDaDgWWJGF1OuyymkGk8kQcCn3AUs5HEgMpAqEweNS0k1vAQGTFiKwOWItMpNijg6StNz9VEp36o8BahzxAfoR-tmZUZFdOTBjMf_lZ3abWsGig73yNWKCeABvLLBaOYPahb59R2du24Wj3Te0HPhK1Gqt1vz6ECp5SaHlH6Gg6hcUuzRqNxX7XKynujXw0MKNpOjDJ5XdbAJuO_ifZVpz4-3j3cl7P06zhPYuYj07IfiILanEvsZpsXXWB3aLynqrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eqKere4X30O9YRUUGm_S2yR2AIV2t0bJfFgrL5EMTdLdgFfPZ17aCe3Kxc7NYUxWn7JGDDIRkE08ZOMK35vgJ2Y1MWhTmQl-adGMqVrvv1E3Abaic-A4qzZqlt661ydVi63YbxuWzMRn_wzUF2v4uFuvOUqokzFsVYrc-sJKnYh6YNYkGRHuI4nXEWBlpVPaXUwu3v5eAxgrwj_XoOjzictF_r9kN9mSJulCG3AkBMbcWneokwg3-ti_0SSrvO1qRlywNt3UJBgfgAfBHT3EyTeCEBxZ0p0pbSgXiAhnuXA7hI_TIaCvK5TTkUDHDpUtvgKHjXKzzuransULmI3BIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_2nK03BpL2gwgAxOVGNkCbIzY3OPAf2pvcoYznQda3pbxZmcxjIDfeK-StyFg4dCektMLgGgepX79uWQx3ZP4KD_4Q5eEBrkUX2Qnx4B45oxlpDkOiFQoau4nJLGXmpg0EW6W_4muLcxo2cprmXOBZ1Zr7mhD4cTunUjnRZx04UulbJqgjY0oPXS_6t6hEVKW6ZCPsVM0UsRFA-IDPlS-KAZeeo_iqk2TYHicAaF7Y1R3q0OPbWsbUoN57q-6VJTO25IVB6Ou543yNUM3sT6RiYfLNP3eL55gYJrfGYvtmAjn5_OYeClLvHgmbEaJaOxBM6vrrQjqr5zy0lMB-UQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpmdtCONYHWfOM4N_qQOktfMfAF1YH9me2TkR61RuZjIbdhvbyVECX2ikldEisoqut9F1Rb09Y3KQY-rmbiaqgbHuRQN2QQcJ2Ajr8WRjWzt-lk-bFMmQ6-Pna8ZiB-WW--sozem3R-hAwhoNskBWN0hbgcwdAMuKTAR9PkkrfoGvMEneoXe1WT8pyk0sQiqagYOviMi2jXp1tIEsUgehF1yZOgRJMfVlP3ZCY4Kq0y8beqNDT0GvrnCQK3DQs3oJcanhRctV9gV2OQeQLq4RFWvup6bEqOPDUxmXoUyLCgTVtbxilsvdHMmX3LAI8CyxSqucXgzCOMAzdtHJYxHyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bifabKZjsb8s1hIK87jf9R3Ei7g1p59cicbZgB_9DtfSVIONvZ6T5j2UN7JJq556nyKFAl4U5rZzdWIMDH-xFNpKeVlGEM5nVxZwO7_RNiFjlnSC9XrwDHIYnt6gNccE2QCGwm8qwnTZ68vURL6PEXAr3mkdl-t6CRnRBAuRTFqC6h8DrVIT4yJHWb0a-CoRjbGgeRrHaMYc8RJsNAQ4omK2P5Jkc8URhj_rtvPK8fGQI1q7nl2w24zF-UGkIyxz9AvXqY5-92saItvurMvgJ7024PqqDqRDjE3JjHrjikT22gmLXbyLwyAVJDuVejfHbbwgN2bbI0ux7LsR8AY1EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0I9CJE__zuXTq3cILd1kGEh9_5mBBBJ0ZxK9ipvbgQdFqnklO_3k0WgfkvmvOhT9rHp7BKiodYWc4Eq39l1WbDoOT-r_zyV3d4hEjhuFtMuz1WkVCsefz3libxxJBUKlfwiba4HcP9opzfWPOmh6YEBURQ7rtUSmQyGzfX4u4JkNd7XftdnzekdgnE_pgsAXC6vc3EA_rH0foaAfW49Mbl8SBUvaCI59-mk13GpmoC6RbKKXVuM2qXclZr2jzz_Z8SD7iXpGCIXbQ6Q2gGAx3XnGc1oaGPLUF6WfCZF_e_FDNttjV70GChMzpC2J3T5pRPxXg8fYhKX1n-19lBSDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6QBZFT8lFfLxS8dH6yuchS9ESnftF8Zm__NU4k9gb36KBnSLU_1G8-oeyVfvFNWlQMfzBeiQoFTmUQhmX5qljtKJdnaWUVEjTADU79oVLevIoOUctZJk8AbWJx-YwYsA_tdWIiKI7_ArSuNbMeqir4Y40P6Ou2siu4pVFNa0X3F0W1h0lLZyLfeOs-CGoHbg19k0QNRewju9wFs8DyvR1IXtruw805aklQHOuu5Qaa6Rg0KielK5Bzo9Dko1EEezZ1lNQTSy1c5w9gjm0yhMDYyq7B9Ub6yI49tkS4pX4Ve09SnU7oyn20qnRBdxOAvL-IB19Wd_5TYinhtRmH6Ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0jx4bB_2_PF8Rbial8ntd6DTyqwtJCGpgOsqypQyYSZ8BBIShTFWRHhycfToMsDn3aI4KpedH8fsjhMjnPGm0lhai6366rKaMumvD_KiAexsVlsLa0Afkv4Zcuy9PyUyYEsNTJ4Jq0hph6-dMBRH9QB-OGPBGTxctfvfP-PLcQEtrSbgb_tJCkGnkoTR_Jr8kulEvXJJftk2PuW-ohQ3_XBmq9YxrX69bu3cQAAx8HhvkGernxzp0i1dXCyfIHJi7uXjzeoci5r8v5Cg7Y7Mpva7ysBhPZ3TrWgvAffSGf3FUFXTh-gG2UZDC6vnzfOiejcJqSm36XlNu0A8XRk6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCuIASXryuGvcjs1W_SDViNDxU6kx3D_XxMiV4UzmrXoOTV1z8ycwfhmunWrFhuuXcXgln58Lqj3CqQxsceMgOVc9fFfjcTPmKrvTd2ik3v-fLZponzmiK-05r-MxCRZXuapCNtPEoBI7s9j8HA5QbTX6bYVBC_LVQz3e1e0qXEBVcnoX8Ahg3PEMDPkgsFX9uJeJ3E1uyrEtnry5nQCEaTtbWChW4dkLqD5Kovw2JLAY6HPedJyCwKxqpys-xvCQENZkw_ISsITl5qTuByzqPHGLTcAQ4dWr4ec72A5PlAe9szBVgzPOQBJLrjOvQBTWMdfB-THSl8lUwOhpYNW2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvVuqeNkqConauz0W-WvpB5sZDSfT94hz19t1Sombre67nA0aPKCXy3PaQdCeElrSxUHuruwJysMD7ZPiPBS4821yKNv0bevUOi8b7Xvud6ebpL4rirSfNc9qQxwRgCSh-WEL4ciIskCPXq8oNQcKVh9rEdbxzf_7jP4oDC0rDTQiYA5utm6QWSuBtL1DgcTGbkjveeyA3FVudPOyCEWJNsCAg0Z7v0fyoDCV4XDsPOFACtuX9t8jHWk6KJOGtEjTa-9hp4f4yM7dTsd47v7NrxbJEu3bt52uLIQrr5E3swCciNRqARdEkDCrzQY0Y5fEaoaX3Yee49lBH_lQbl4Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKOA2JLWtMIOvpaCCno8_tUvbeUhzW_OLGX81TmmiSBrVPDNzrBq8zLaL7QkLwZVIRn3u7o9l6lMyM7WpzLTHAC99UJ1nI9Cl6Kl3_0x8-jeKfD_FQfPrw9da--LxsRXP80QY5UMOVfkl4LgTYqqye4ldrjPzdGkoKbqvgPdW_IbALT5rEcCqcCJItdo7m5_1UtH3JmQHVxBINu3XM7r49n8nsqEfN2twoNDJcTGg1bo8NBWv-2eutWaQeOW35J-kDwcrMqhfe9_Hc7zliAKywza9P_cFxxnF25AG_wrTQtBNG7CfwSkhXWgmH_EGLEjLy_nJktueMBDB_Ap_KD-Cg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5UtsfrrRamk4Btn5Y7L9NZqsAoTi-N94ROB9N9tb5f-kAE8MdDyxFwSsNAcoHLHyboC9QBT2pesc9yUzUX1YiGKXqUpjv5nyIGw3Tv7dQKQihA5qObZlwL-Wg0QS25rGgRrQM5C419VigYZxlmmhF6ctBtmQzImRUmzVPcgLnAXupL3hwIXmOr28IGjyzAjguQ2yZIAFB6qkjUVUysYNCcTE_4GhLaYN-o4xc8myFrq8cVWYU81PyH4YSkOJytq4j0MR_eDjegPPUbNDTO0QoG3mF9HY6oHUhshHLeZ0190QmhSkrUgkGpiphCvNyB7sLdB-VqOQmriM7_NwWInWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=fEIxLKi1DonyAQjeCws4wVXUqnv6z3AiCmPylPMYA6b6lO9W81wTjNtTmK8rxRQRnlJaK_swNB7e5vA6Xhj4-uKSKNBC4UIgc09hcTgesQ7AQj7Aq6cJgQb8FfRhWcNUVOv8yiMjllE3qx4Y2mqYZXMREC1r3NEbToJh_fZSnJL-ymuPp3ih9p1DQWOFTCB1yLVqJ8fUbd5huPa18XM6UDhilSwF4yxKo-Fd6BqbgvAJn5X9ljdVs2SrehwhLHLOCC1JNCzUuz99PmrNUASwfzCvHUFtwG5XeCEOtx0FVhoQjW6h40QScZIo3u_Fli5BBZpYmRaWZ8DMpEA26d4Gew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=fEIxLKi1DonyAQjeCws4wVXUqnv6z3AiCmPylPMYA6b6lO9W81wTjNtTmK8rxRQRnlJaK_swNB7e5vA6Xhj4-uKSKNBC4UIgc09hcTgesQ7AQj7Aq6cJgQb8FfRhWcNUVOv8yiMjllE3qx4Y2mqYZXMREC1r3NEbToJh_fZSnJL-ymuPp3ih9p1DQWOFTCB1yLVqJ8fUbd5huPa18XM6UDhilSwF4yxKo-Fd6BqbgvAJn5X9ljdVs2SrehwhLHLOCC1JNCzUuz99PmrNUASwfzCvHUFtwG5XeCEOtx0FVhoQjW6h40QScZIo3u_Fli5BBZpYmRaWZ8DMpEA26d4Gew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAmjsz53KKjlbojRDXnNyoV0FGXYEG8ZtwGXi4f-nW7Bhvn6UoY0gDrXbzSDyTEXqiWA9cVc5LJt3k1iJ25qDeALHV1ahoOwJQhZdteZmrcJn66fzE4iXiPW-F3zY1XlCwJOKyDzvG5j_cFI72mS35bnJG_K4dzBA7Kex_hWelVG9uXepFXkLYcjGjSGu2KbbqyGvo5YE7jhKzRVtJrDISdTfppuW12W9lFLOR-szFiKdZvgaP5BB8iGTgFu1b9BuqsUBFKth_BGdTqtou1FyOZ7RNItonsowj3wjN6JZpqsK9Tz7ryzM0O6ejL16Vev_X-Ajl51qMVP8wYDQrgY6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q--v_K8Jznh-i3ZteSS1D8hZOYfyntFTI1Yn4k-0TXf453QyOYTHddG7tjWfDdeLmLW02pZBX1jAn6tZLGQOOQ5CjcPQGuGmB4DknESM-9Jb9wjJUlYktDEj3j6_VVteb9HMQRSWRsBeP0XNUX6o9hUd1ZMHBLkpw4KZIQaCdURHrd1kVcU0DUHj6jAy7dvgYUgOd_KpAGG7hUoxrd_8ncjifMeIWzh7-JKTh1IWTQsZ3qfsOgE1vx5f3FifzF8eW5DXbi0I0wslLJS-fONr6smU8iChZy566425_t983TWtkRQKdGBujf08z05xfX_Yh8claKIK4PTS9vYzyK6nVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCLtSwz_BKIuefaPmyr2527erpd1HPCogxv6v3wqJVn_xFLqz6UlrWeS2hqKadKUzKD-fgYWujS53FTHOJpL1cydfuO0E05A0CuOT3hvH9LGUeUq4bwQix9eRVcBUk2DfGIz7agqCdxSmV3pNG3mU_EVU-COxK2upQxsCmZJXkqLCsSl2NM_cBNoKDcGWaqTBjOmhgziyzhsb-QAH3V6hX0D1F4cVddOUpih2vn_T1S7Jmt3QgfgeB7x_luYkjgQ0-C23Fe0eE_xhf171McKfcTT2M8SrE8UgfAv6G3yihiyjH80BgVgyL4Vj8mT-Ie-QXd7kPsgAVPU9G5NuNUFDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjvuE4CM57bUXYmqu_pvso5ae75Nrgnk4U5hSGdOz94AP_9uMt4NV9jAYnZQlvBqK16ORO_eE7OZkZTtiaYCDCsqBFYzOgEbuzCqV1buEaA82yFZ7hSPiPqsvIPOApD6AugiU4sz9ZgzlhT4FpwPUFU4vU8FgNelWB0RUrQ4QJyhyGDsK2Be7FUhFGAbgiyPHEq8hO7T1F3LYItvDIujzg0E8vTKBBrVHGaaUfsEwAdtoS7mAGhGNmXnk3-Nl1LrDV7SoeGOBEpBFNzJ02VWgeDulXfvk31ol0HaSc72WUH4oSG8YfpqrMFFF_plrCDzfrsKfpy9wX20PBXZCG138Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyGfV5APKQLCuAdT-eiTi6d0fyabhIj9Rwr8jQiQOZX2Rrf8rRRRUPkizZ_M-VBbkA0fLr0RCm-qOBxEAUpgqKGa_5Xd5HWkgJWV5M_q9CIOexaxOdZ8r21vTNIa041gT3PB-vKzPd59-rsYZvMRymoRGgj4Jo4fOwwKHhN54U_rmW79ewytp8blWovGAGJkTwha7bo6-SXMRBbHOYYtKL4b9VRJVOxz5rPx4Nj9ecZ9ZLfzne3pKrIr2krNDAPbFUlzQMYkzsgv2_OlcTPe2e3qJHDnrXZB5Y6J_-A1B7I35OEbTPSL6cjkOdrwqB3H4kIElIlRwVx1W-rcb6Y96A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tp8hH1jxgxI46nwdcH2LaxF-qjTOxPniYpX-VyYb67xV0Kq8q7fNZ7qVQ474sglyt-WaQ8PbXqDSuAkcdrLQzG126ewF-F6Cdcs3617ceVJaSyWGcCFjBirFxGHTDfD1eB1GOK0LT1tzBTZYMcmFEgn-uC8Az6omHtqvOwN5j1DZtQZ0C4F2dU00-eDI9JynGdGV8vFWarICZFo8wJJwlyHVqD07lkaz4zhUPTa2-M9bs-QgRGPgiLStQtpIxm4yW04yRRkCkojVV4YDnvzzHP7AKMimYIbm0-e3OG9YRjlAJ6ucxaZG80XJKp5DNqIB8K-ao7Uxgsyjt4BcXaQ8hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9iE_JLpUYxKOX8gPXvZhH0Iw-e2Ug2m1pgggwfTVWwHXoTOLhzelwDAt1s6pS7vCTU88J4tXbLdE9Ts4a4kiajWIRp-185-LKQisl4s3IK_mU7QzfWX8ZZhdlvWMg56bVuFyIN0R_AwRxf7RiCsES6dXnnafDC7-1w267b3VAGNAt9j6mtYJYbQPryG7LxgOJMwYw48KCDCCHQURjSCxwCTlYSkk4Ejqwih42dvrkdXuZI4WOPulbY61kLsZrjC875G_GxTI_zpGhkGTPFUOkuUvm9T-ZPw8tvBdrG0DvE7WRDKyE875G_j7FYvdJgcdUeE_-inJlWD7IWaWaNpLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biwYIlOityJud3Mu_CqBZOxQKdSZN8FjcFgM2yXagdV5enUUFmyPvZOpKGwURZUNqMN11PVCb-2nKZG6MZ3RQIfs0Ad5LGoLYLzUC9JptFe32B0lL13v5EVgT78wOJ6kPYLjWEHAlylB6KYaJb1DqRWg4UubRP5VEwcpnOE_bma5TMSMsNCdkSTX3pbtEj7-_UTt9LwrE5l0gBt7g7HTVjU5SplRKEOpxvmygAyN-_50fhWOuxFYU4HevXhCAQV4ZKWxl1W3f1nC60R9nidT7zcisYOzYa8YEdl_2Zpjou6azPHQz7ufjpA7gHXsrRjA1XD9OzHzonlkbU6tlo4_Cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=KRKuyJsqjX49VK2wzArZE1WTZxaH5n37HeJXAW0pG2d7gY-t_10IkQbutp3qgCH37hK-b2r_dvy5uhadHv2okaPuju6Cj_pKk6thRZJlXGPirDts4hU0OLxwEvrdLZHX0UdGLIJM_Jy4lUH-kn6O9VsC4enYqrJ4vCx4TuQwec1wEhYbjL5KsN2qdvtjkzi4ZEo-vcY2CoYwtrVe7ii-2ZZDLincqPDxcDmSYal6lAXg7T7m0U8SNwmad5rOSiS3aTazzSAuGLbijo2AQ-9ixScmsnNTMjOVxtB453VZOmbovR3ncDRdI6qvXRBOnFy_j0_uOtcvy1_szdYG1A_jgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=KRKuyJsqjX49VK2wzArZE1WTZxaH5n37HeJXAW0pG2d7gY-t_10IkQbutp3qgCH37hK-b2r_dvy5uhadHv2okaPuju6Cj_pKk6thRZJlXGPirDts4hU0OLxwEvrdLZHX0UdGLIJM_Jy4lUH-kn6O9VsC4enYqrJ4vCx4TuQwec1wEhYbjL5KsN2qdvtjkzi4ZEo-vcY2CoYwtrVe7ii-2ZZDLincqPDxcDmSYal6lAXg7T7m0U8SNwmad5rOSiS3aTazzSAuGLbijo2AQ-9ixScmsnNTMjOVxtB453VZOmbovR3ncDRdI6qvXRBOnFy_j0_uOtcvy1_szdYG1A_jgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXS7zDtOxxSTMxzWXJSogzlKfMmt41X1siGjdSSe0WMCwpiAklG9cFZDd8DR4Av1pUa2zIw6gf_Gl1lzVbcN4Ph_bdSPettYPeGojxAonEppngJ05CmijwfPT8MvdhHbfbvBZoDBe8PSF16QxjO-D3TyoKwSzblWSUDW6Jgs5nMNAfHc6ybATVXPZnEHhqUkRNthJseTFbXSfk1QD4nwRuXCA6CIcMQkMfWAgJfDBA6LqIODuvXJRpfzYjq0vzsfyvLj18Qthbzgq8hrY_cqfW_7Nn9dhFgpRh-9r2Ey2lcLbYyU3BLhw3jp1_DfY9jMH2E1znlIRx1oshwxDoNzOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEHtDRAcqynkIa-irfucwH_fs0eQNQligf4uv_Ks3Y9K597CFs5de6Tx18vkEelr0zwRwPMqu2HnworJJVL1YDBmLqqKmCoeNxL6OQaxANDX_nEkpBt2e8W1Tex14WUCbMpHQVkowGpqZh8KUhmhGJYZHvvcf3eiQSoojdxvoLErBk4fCVflJMA3kEvKDO1eGjLFuajW-C-y00wjksZx1qMSDcTmXgGvm-VIp7ZEO2KJ9BLMgKZNmF7HgzTh3izdAfN8DTwaG6Qg2jXKs_BYz6yWu0P45N0wkFodCHoV_JJCNuvjvBxMab-Zfx-rcmNNbewG_fOQmJA7dsEWsXx5Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhoVMDgZYfNfTiYLSuqGUmSjF0bQtdCwV1bsIF05FqnwjFVY2KIeNY4MnVjbMPLZibPKRdZ_k7CXNuDsZCgd0pc0SRI2kvbH3RVGsANOkUnlwr8qi2rO1rfBtU16jeH5Wq3gCoWUfcrh7eR4gEHAGajgiBvEn4084V6dzDmdeWDfs0ocAmUgK4iECHxJEWOkxBFYIiPUdMCPXNJOLzuq7hAVR25GE_tcmbTisO_RelC3XTeCEoTmcVXdBZM_Z_BlVsrBI3GjknTZiCFf6iwa8U4zPGN46hbNIOGcl0qoe3XAjFbV43AQiAJJLF0-cOKRXfQA6qfBr-xNtCPfCuWrEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AP6THBWmuRxaf2OBqQdiK_eRfgoMFjw4OJJ90WetZBWthBmMpL0z3F6MTeN-jzp2CtNE6vHcdKAte8INKJ41IP3Hmv7wx8LVNfUMZVn-hWC_2Oaws0RiAaJ69Zbx_tzrd2NgZotZapJmxwKPkmTC1EtoXVE2wRtoLbaFjwbUR0mxYcsx-jxeRvl3N6NCde3zM9SqEdQ9A6xFdnXyJb7zR4KpHZfagPegM5mFPQxTx3uKuEWDOtyzpwxDTnAdF8ANo3-jvimEmXSMWtV8hfANejgjoODU4CLz29oUdnuZq2OeYhom8YDq7tdRofKcLfjrCseFpIEkUVouQTmoj7OY_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWfLC1OZUzir4kzkD5wpb0tjbWuZdpl8S4UJiebPWvIQii5Oo34p3FYGodQYJ0txyia5pVuMU9sM0CDDCWnxURoC2zr7zWm-ASaEr0WWFnUrbwBaomiIbNXEgDdQUIdXdscta24db3C0-dx0dD65lX4BdMDZPI3ZDKb2i9HX2r7cBETm0Z5j_YKP6dz4yTWOdqJpuStojYbF-l5CDYkq_G_s2kW1JkDOK5lGBi-DoTJ4_3JOtxQH1nBV1PjQEHQe9mGkMjJOFK4JPQPGTodySye0nxqqf24beVJzCTYf2twkJScVdthFxlfwXz5XwA4im4AsYWyMp0lKMtny2Gc-qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vI5xQcs1bVXd2avvXjFysaFC-PSXARugtIsrOIPleP8UrxxBhstATy6JbzUpGcDjahEfu9l-rvLIeRGnjMHwMzk4sk2Ioti9mtI8LfuS0U9Ug_FelITzPQioqx8L8Xp6bUwIs_2o0UQrY7sPu0097Cdpdw4_y_3I1M4iTKiCRACyXHnO8Piju-XPZO-yMBtOpTP4UJ1EOlHcd77M0ODbw_qtA-s1ChINnd-dfNMY_vIBzmZENIga7J65-rakv2osNm2O4zvfNXIC03DfGTX-IuN7LANgn1Vdep_VsRJ6MeUz5Rz7SMaw7Q_JLtxuyJbOGcRCWWsUkqShGQG91JoliQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ib-kbwm70ZiY_oJt-GrlcJhzTGFAASgV91s4dmiYNtK3_K9y1ZcE4UNqQaqiCi_Ms4eod04L7fynvvqnmEpKytUbrdEUDKko0gwPy5LtC7r_LfaOKWvpu928hsLtRDmvtYBeuh_8xDl3yBzDGq7UV7QV1yP4XBW_Va2p9VoUmma3Qqsdkz7OAtlTmY9ks7fm8SYRMyEPYElVaE2YpsagqIkAftJWt6kuTSvZ4ts-awb3K5EEldkom7s0jgRVggoMhyINpjAzQlvlrk9dl7WD1yTNdeJlh76bDao8pZX1k9BHxL5bPtsZLkKHTgITNjasQlXRf9GfGc6o-cB7RQdAfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=KEFVfL1Ql1b83VvFZMpOmOeHWQbNBSly9z6y59n6Usm0oIJi8h2YCIIOpyAC1bmpWtaTY7-1xTGwFUBcf7-x-Cz98JZwOIwMWwzt7RAYX3uU2Y-lZJpFWQK8SAx_cxwJjXvXYf4KY3SaNVGvezFn-2hF1iKhQgeBFTUBhNEy2Frajlh7NuViyPPOQf1343JYJJ8RAFDheZvtDJZrXSgQXHkRPcBb3_9doksJG_HAN42wyBOAoKiy3f4ZnxzST7Ah512FPWy-n5PK64pp9CUFLQz92iTykVaKpHm7fx5GsxwY1_WfEh_VK4ozBm0mRTaDIXXaaEAYpMIuZOF_nNgJ62_5b3l1-oPCY6mrvsxck3cHFhkHYOlttgm9o3CJ9tuCuO4OuaHS9bR7aCaAt3svqWBi5bDfsrVGHhTNXYHkoUDy0KKTfu1QA9nT3QgzVJnTAxZuv9FUaVB7sriysuJJgBoiejpwgQ26wY-apLDxS4IcGQk6Q8O_W2NNI9TQOPKgnzmfPMY2IZZvBc1WMVgme3ObKlPNjW1npn3O0HU2xl0b5qmTkyCA2HFAQg9E44clnxD_HvOYNNGDinXCjBWAmTSHMOcIrEdUSJUDzJnqNzdPfpZNQzrPfPxuQJoMNfPpTK6q9dET2A9g1Yfc33B4LqKZgxz1CQT29p8b8C0Id8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=KEFVfL1Ql1b83VvFZMpOmOeHWQbNBSly9z6y59n6Usm0oIJi8h2YCIIOpyAC1bmpWtaTY7-1xTGwFUBcf7-x-Cz98JZwOIwMWwzt7RAYX3uU2Y-lZJpFWQK8SAx_cxwJjXvXYf4KY3SaNVGvezFn-2hF1iKhQgeBFTUBhNEy2Frajlh7NuViyPPOQf1343JYJJ8RAFDheZvtDJZrXSgQXHkRPcBb3_9doksJG_HAN42wyBOAoKiy3f4ZnxzST7Ah512FPWy-n5PK64pp9CUFLQz92iTykVaKpHm7fx5GsxwY1_WfEh_VK4ozBm0mRTaDIXXaaEAYpMIuZOF_nNgJ62_5b3l1-oPCY6mrvsxck3cHFhkHYOlttgm9o3CJ9tuCuO4OuaHS9bR7aCaAt3svqWBi5bDfsrVGHhTNXYHkoUDy0KKTfu1QA9nT3QgzVJnTAxZuv9FUaVB7sriysuJJgBoiejpwgQ26wY-apLDxS4IcGQk6Q8O_W2NNI9TQOPKgnzmfPMY2IZZvBc1WMVgme3ObKlPNjW1npn3O0HU2xl0b5qmTkyCA2HFAQg9E44clnxD_HvOYNNGDinXCjBWAmTSHMOcIrEdUSJUDzJnqNzdPfpZNQzrPfPxuQJoMNfPpTK6q9dET2A9g1Yfc33B4LqKZgxz1CQT29p8b8C0Id8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=SEGSt631RfqNIyLqzDAcQgoD5J_16wTtzoM6DkvqCbdBBRbgfpLI0qUoTyRDkH8CcadwsgsOtCXBdnguGh1Bhg9YHJFA3D_f4OGaiNl1AWNGN_oLK6MqYifFIGrXLlYiowqNvWaEBAceYDBUlmdtoVh1C2_V98Um93pbKT1D_ZGMRbgtJtsxiJkcyo6ndKxKjDwZtOf1d69zqzC8N_Zy46mJU0ODJ9-aFA6nurPlvZRCKUrNjW9bFPRBRTv7OBCvRqwfYGxVrntqJAgWde1RkLXFpt9Zl_WVg4nWGHEzqLH51zlIrodb7MAp_5mppcjt1-XCtvjUnRc1F5BjiAnXmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=SEGSt631RfqNIyLqzDAcQgoD5J_16wTtzoM6DkvqCbdBBRbgfpLI0qUoTyRDkH8CcadwsgsOtCXBdnguGh1Bhg9YHJFA3D_f4OGaiNl1AWNGN_oLK6MqYifFIGrXLlYiowqNvWaEBAceYDBUlmdtoVh1C2_V98Um93pbKT1D_ZGMRbgtJtsxiJkcyo6ndKxKjDwZtOf1d69zqzC8N_Zy46mJU0ODJ9-aFA6nurPlvZRCKUrNjW9bFPRBRTv7OBCvRqwfYGxVrntqJAgWde1RkLXFpt9Zl_WVg4nWGHEzqLH51zlIrodb7MAp_5mppcjt1-XCtvjUnRc1F5BjiAnXmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTlyqEfGYaY4WIgr-6nNi8wTOnRcnMCuDzBoddx9B72P1tAPkLZOvSqooJpmnEe4OzQogmICZqMYr05aFjIRi_tHll14NFORKKCVXJBUgmh5IgqnvuTqUI5od8lfqfCy_HSXQghpL7Wvb1ylspEpySzxu3GF5jtjBk4SYrhFRV3KCr0VySI4J5JC8yNykHFlL537M8Kep5tWaSuzbt2QmyL6011zzdkxNOmTeEt_fbilxiuZBXF_VzR2lbVyN4X3mh9B_ZSWW-WmzFPMlkcwXtVdhzm5LRaZp4SsrkHTp7rJJQaR5HgmgbuFV3GgtTz5UPnO0pBACoOYm0dMf0_X6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwILRuiwyaeqlNCMHX82wGLNMW16bYJp8oDNcAuo19qTeszGgda3WpOxFtclH6PFwyBZY7zRzbuCg_kR5QIdYti6cC1gc7VGNoCkwqrvGE3x7rU_IMgJn8Ypmq-BUyMV5fGXVxxCUUFuxjuGyE5XlzwiISfcJSCnRZmatVbRmEkYkykcC01QCPifAeqN7SkRb-W_ckYP8rsosswV6ezICS1O46QSDn5OEbXlZOHjs9wNlHRTocDMIxuK23w-GDB51xt8DToyMY7JcMZ_Wb2CkoO58D6Mo6FpkwOLbrvg8PKjH4-W2T8ILalgECGhHDQOB4K3U2iga97MyE2fxJMgVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=PuYHTymsXd1cdJqoJDMcd9UL2-LU62h8MW1azb9zrDFks3odHG_xVnDUz0qBZ5TU2jyINwlcHn3b2XODc7_XaUNWCRoYQRqAeTO3jsEE7IJEEllWo5AZQ-haAb0ySttn3Q0RZMWWIwAHD6i1grYLogzrPEuUXv9ReX3RwW4jxblqUvrHMePBpmjnY-joSF8aKJMxUh2HNWp0tC_hXFILUg0dymXkHoDumph3kS0NVTT4cQcH4ytQhBje4VVKJ7OQRUjitS0qXWlbmj6or2nPAaie77xKj-vlY46J5dIMZ2gxvIQb7F5rEPTRZvZfA9HAvQxW4wVzRx7cliYZDl-s0DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=PuYHTymsXd1cdJqoJDMcd9UL2-LU62h8MW1azb9zrDFks3odHG_xVnDUz0qBZ5TU2jyINwlcHn3b2XODc7_XaUNWCRoYQRqAeTO3jsEE7IJEEllWo5AZQ-haAb0ySttn3Q0RZMWWIwAHD6i1grYLogzrPEuUXv9ReX3RwW4jxblqUvrHMePBpmjnY-joSF8aKJMxUh2HNWp0tC_hXFILUg0dymXkHoDumph3kS0NVTT4cQcH4ytQhBje4VVKJ7OQRUjitS0qXWlbmj6or2nPAaie77xKj-vlY46J5dIMZ2gxvIQb7F5rEPTRZvZfA9HAvQxW4wVzRx7cliYZDl-s0DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bdicg-LffKw7ehWPHppMs6q6XHaiuRZse8lV8j4YLJItnKf4eZ4q7LrqDSmjAXibsRYN_IV4w2cPSsdmgC9hq_dJ5ULCvhmnyneMLydpdJp_WLcL_fuxQrq_p8h02W-PJN0hc7AhWhL_5PDhbdGBkFqkrMIH55yo-0RKvoS3XtxyizgMH0ZaBRxFva0CbZ7lJ0BcFSHRWv-OjEOJZXvGvyL14IkqedeA-33cc0JU9Q2vUOiR7tMnoiLCqo1J4qEGW8deHLWz8BKFhBcSD0WYeWFduofNbb3Cbv3pMFBZJHbzzCrDTBcmhp2CrPd6QiU7kmi3KlttieVSIJ7nrPJSXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4hbYSTw5rCiB-rnzYwgrZRhdxsPcjZC6_jtzr5A3AwbfW4oU90aR9yNwuxNiB3eZ5DT5ieIvUCU2ztdRDa_37dqyVLjEgGDC2p1Scti0LQJNuD7SodsyIRyZxvDuB3oX6vPe71Xf0DjNYgOWlEJEU7IfGy4tnjFggXEQFvJBoDvmdZ3Q47G8JFnfpHSJD1X-s5pec29N_LT31anDoy_keOwlRQZZorq6LEpR7zdwzgIdeLwUELqzbMF-MBWFB4yyg5X8DObLIwpR-ckfAKarp_N4f2S3NeNyQ69n96cdgGR6h9_F6Cv3yURYcP6e4SfF9WfvRCD8J7FrVmKpvzIKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_VPtyRB8C8Bf2d_97m7xBE_9V2wo_sGbbrAYPs-YWKyH244OuFzp11k6nVdXq6EyUtUj_RP2aGrUZdAbuonNe3AruZI4LVLwCRBVWKoDcBjL_bHOO2Y1bXfvbf9zje5p9rl6cIwimIyDK8qwajsmO6tK1DwGc23KrNdfRCWIsLkoo3JNW8vKt8a19e4LDKc2sB0ZkGUOm_iYYaC4mBkQk-XnaEBDxUQM4xgaGwxcVStTgZgMu4_d-vB2HuFbn3hStfC1W_upgGO6V2SzDHsnlHs05haTvjpS8ce4vXq0q4lyg6gDY6cjx5U5EiDIP_Vocub7htfpEwdsP2efrzcjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2TB690h8mZmjRXztZn3GS08NvIgu3XAeOQ3m3ZQDD-i-Wgg4tk7gNAmPkpf59AKEGyTrmAtt6CrHnmohsWfss7EEJzRF9NwyIucWRD6QDLeEu6x2wFSOZYKWtsZllEIxWm61TyYpMeASw2kCOPylO0iQFyOwOFf-objQxgL9o46cduet-GQuhJ0d2oTsTW088bHFW6Ry_5aRBCAB55J3n2-PXphiYeycufIuMCVkl2PvOt0hVQ23oM4GdOA4djzF_5-hS1x8dxJxLyI0DBsXVii3ACfbYlgG42J4iBN-pmVG_rNQnd9DAFVo0QI9zTBNQEQ_W_BbCQdbHf5g-FkFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWJJ0Kpqn47LmD2kspx28eV1XgJaIW1mVrMSOs0n8vGz7WK7gvo1SN6LruF5at1F3arGHLyDO1T2wy9xZ2k7q0C94b_UP-Yfa-TRnIRvEUKDDiX0XT4PzImTL0G-ynsiEorCVZhCj6-h9-7NDDvYTGmtdEgWTRSUHiPiCE8Z4yDRDlP4bLC24vqpHZAp5eGruYuUJA5SEiHHW_UM45c09TaY0RXDc2qE4STwV-kI9gOdU8XgSIZKUKeGFnA-qe-WLC8WMH7XFFAL0Hu1tvvVPCZeldc5MQ8ka89qy3Ln6MD_0xcQFbHunsYDpip3Tdf7B8Zn3k_CBbMOQYRbl_qdog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5WmpF-W6MWbXs3DkwJFxYzH58JrST1TbE4BIGAaIBTiGHF7R1XU9FhVTgYUK99qc2mYguHO5YxHUrlW2fMDTHcqcVdXUV4IB3bqsYGSUmkNTJ4E3TOobiKXN8RZjo8IORLVTYaEQKZ7xMhFIBeMBdcAp6tg8hR6MXs-MxO-JvUngwkNGm8MYi0Izv7BIPpeV3IX004N71sHI0TMHzoyVN-sTqgQKr2JQhj9McllWcfbhoCOIT1GacbfWbSI2lOtZrV1MgdkMG6m-3v0ApHnm_9urQSH8iX6dJxyfKbbbpuOiYaN3J1PeBW4OqFdQtEXxIjEoJFNjFCpPEv0F4WAmuvs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5WmpF-W6MWbXs3DkwJFxYzH58JrST1TbE4BIGAaIBTiGHF7R1XU9FhVTgYUK99qc2mYguHO5YxHUrlW2fMDTHcqcVdXUV4IB3bqsYGSUmkNTJ4E3TOobiKXN8RZjo8IORLVTYaEQKZ7xMhFIBeMBdcAp6tg8hR6MXs-MxO-JvUngwkNGm8MYi0Izv7BIPpeV3IX004N71sHI0TMHzoyVN-sTqgQKr2JQhj9McllWcfbhoCOIT1GacbfWbSI2lOtZrV1MgdkMG6m-3v0ApHnm_9urQSH8iX6dJxyfKbbbpuOiYaN3J1PeBW4OqFdQtEXxIjEoJFNjFCpPEv0F4WAmuvs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnKooT3Wt7ddK8ctZpeNxIRSNGF1kCEDohNpJc7AdXv0ns7Q2zlML1oBHTns1sMy0v39lZCu27cyuxpBuV9-CRKRBmYfuyB_4Fd_iAtrxPfYORAZgx8Z6C5HYXQiyEaexN-6YLeD5KwYieXsGODtXDzbZmC8u6GBxwtn5IHuDK_SMJ0DCF2cZMai3p9SMrg6kPqNVOfCySNmS38fyxXev-3saUdLiQ6Hx_sAJrytovb15baxqTp-884iDx91c3dfUnAnfYjiGEa_3D9TxZEaJcTNWQrFrMgiINXS1xk81f4ghpRPZhZiIVy_6cFS2v3IkYp3aBLmMnnOj3AQUQNBICLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnKooT3Wt7ddK8ctZpeNxIRSNGF1kCEDohNpJc7AdXv0ns7Q2zlML1oBHTns1sMy0v39lZCu27cyuxpBuV9-CRKRBmYfuyB_4Fd_iAtrxPfYORAZgx8Z6C5HYXQiyEaexN-6YLeD5KwYieXsGODtXDzbZmC8u6GBxwtn5IHuDK_SMJ0DCF2cZMai3p9SMrg6kPqNVOfCySNmS38fyxXev-3saUdLiQ6Hx_sAJrytovb15baxqTp-884iDx91c3dfUnAnfYjiGEa_3D9TxZEaJcTNWQrFrMgiINXS1xk81f4ghpRPZhZiIVy_6cFS2v3IkYp3aBLmMnnOj3AQUQNBICLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=S5aPNnF99U1g1WBzwIxMEft4XodIS-zxQwlWcFdwMBfVg347Hv7eXuqWDSqxM_DSvdBDqf67eBblfcNwjw3EiGE2pUE40qWPmKyQTmB3Mba0XyJ34n3IYraCMbg3Boaw6-EWkpYVcRGdvQmsgSy7RVpJmFymFdakkKm3WONcB9BAW2LegENJ-NLCTM48ASErqGmA_34cdVi4-1_5YxWdcc25XcpZrUSkwsjw0HcqKvFhrW7Ox8LxUxtRh1QL307BVmB9OLOZnBg89RGPxUtj3m3bdlbpkctcZ3MClX9j6KtYbeZa4D6YlrGIAAldvKfCMw3WFWZmLDLYBuYDTL8W1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=S5aPNnF99U1g1WBzwIxMEft4XodIS-zxQwlWcFdwMBfVg347Hv7eXuqWDSqxM_DSvdBDqf67eBblfcNwjw3EiGE2pUE40qWPmKyQTmB3Mba0XyJ34n3IYraCMbg3Boaw6-EWkpYVcRGdvQmsgSy7RVpJmFymFdakkKm3WONcB9BAW2LegENJ-NLCTM48ASErqGmA_34cdVi4-1_5YxWdcc25XcpZrUSkwsjw0HcqKvFhrW7Ox8LxUxtRh1QL307BVmB9OLOZnBg89RGPxUtj3m3bdlbpkctcZ3MClX9j6KtYbeZa4D6YlrGIAAldvKfCMw3WFWZmLDLYBuYDTL8W1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvKNZnS4hsReuI0B2WHZmwMNMGXJ1O0IiaIFdLiVZ9nI5LtuoYCvq_giA23du6JavrNmLSXa9EnA81gRvAVRgYH_3CWAGqKRwP14QivkQccrkXvpsIq_vVvWkoyIWx9oYWNmfM_StDHgSVVuCVTEewKOzeBAREyBIlG4X2P5vBcNGVhIVsLOlngiJA9t0zhKEMgLS_QyjYCOb8DSjsu5cahdWZrEm9QochKFkdNekVAex4Yux6Dm399DDIpasLK9Elq2P9vQR6oUl2JRoNmnke9b2CkB50MicOW9j2eStnCtNaomn3QBTjsptDPcgoDSD0FDnsIV1g0lYHqWjgJCGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDcfBAarPWFL370pjUdaQ8WdNLHbAe3GxCYulicMcNxlfSR6tCcnv3tCB9UTCq5ERvv4T1yNuQlbsdsz538nRhYu_x-sApecP_Uh6xf2lJaabNo5SlxzATNIWZD4OSmoE6_eaPrXPbTr9Q0koHtPsgKn-A88_1YqMlUmFK71_hRS53ti_aOUkf3qiCJCAU9x4TZuhtVWPEPq3mh1rxUIOY87aU1Z0q7mE0zdirFBq0t_Ys9FkuIeObScMGwdcuX5p1_uRGRP7UMr-QZnUfHiAGTWwT3BJbjJJiNUufxWjeY8jaSbbaumAk8dx6uJTyYoxDzQvxUMkhvBpPvKTuwccw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=NFAK7r3q2y7iZoQpXKSURW4ZagwQva3lsmZLtf5d_u7pdngkz10A3nQ0K6A7BrvL2MiN0lW1pGn_pGe4Po1LbbOffFLjcFcYwNgtNLGkdwpFavNdkrE1Uml8JZSDydyze4WhfI_hTTXbAZzyGjU7E-IOCeZvOWwM6CxlClUCGBzd5G1lO-3Ww28v7g1zUaQDu0_FfKz5YRpgagf5ZFCi16uxmbwU2bN487zYK9Bf7MtBy3CvYrH0uc88LQlyFOkyfbdcvNufPDRDu5eKEuboXQCCKsyhkKulyTv7dRH2Fydfpkx3XAH2RqiPgHpl-GibGDarSKpPEIf1xRlE2JGpoFapBYr34QP541kxgi6ApyGKYbvqEtpiLisYQqsLDWkkSrZUs7AmiWVcv42xMyfxki9MBU265eomV9dTEUAG1V-iYF4Q6VmfMEkws95kazJO1OMvoNaeeyMC0YCVbWldX9yIBDxik8KipNGg7gOWnbc7cj7bUZ1ZxH3hptqV9XGDg9idbnlqVP3gTmzJx0Ych89DMZufF8QQPcP_RGoMhTju0k6hWX1rq2yKcaUwKFswwVcfc3EOM2D42wznuD5UlLu94FKO6yK4YbG5W53zSRt0sqX3KI9dRADeYdypoJ2Do7q2c1O8uTXXC3Bcg0tGI96WJc0-krk2uMEZZ6JGSmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=NFAK7r3q2y7iZoQpXKSURW4ZagwQva3lsmZLtf5d_u7pdngkz10A3nQ0K6A7BrvL2MiN0lW1pGn_pGe4Po1LbbOffFLjcFcYwNgtNLGkdwpFavNdkrE1Uml8JZSDydyze4WhfI_hTTXbAZzyGjU7E-IOCeZvOWwM6CxlClUCGBzd5G1lO-3Ww28v7g1zUaQDu0_FfKz5YRpgagf5ZFCi16uxmbwU2bN487zYK9Bf7MtBy3CvYrH0uc88LQlyFOkyfbdcvNufPDRDu5eKEuboXQCCKsyhkKulyTv7dRH2Fydfpkx3XAH2RqiPgHpl-GibGDarSKpPEIf1xRlE2JGpoFapBYr34QP541kxgi6ApyGKYbvqEtpiLisYQqsLDWkkSrZUs7AmiWVcv42xMyfxki9MBU265eomV9dTEUAG1V-iYF4Q6VmfMEkws95kazJO1OMvoNaeeyMC0YCVbWldX9yIBDxik8KipNGg7gOWnbc7cj7bUZ1ZxH3hptqV9XGDg9idbnlqVP3gTmzJx0Ych89DMZufF8QQPcP_RGoMhTju0k6hWX1rq2yKcaUwKFswwVcfc3EOM2D42wznuD5UlLu94FKO6yK4YbG5W53zSRt0sqX3KI9dRADeYdypoJ2Do7q2c1O8uTXXC3Bcg0tGI96WJc0-krk2uMEZZ6JGSmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=Ul8VAnW_HnBoO-864udCNHa_A8kgi7czlW_T6mqIgfiNILmNi4y6RQwQmH-ACivebjnvjmUw6VuhIwYM_YS_RLes_6zT_07DUUfNlyzX0T4Ov4vVev-z0N903bIhPIzsocExvekJjLRQ3Bc9zv0Aqv28OP7iztfi_yrqdHaV-LB7NdkaNo-VtNp5eFWftQm4RyUpUufnAftPgrPTF41Fg0W3hPkVtkEIz1MFjzwwvs4OJJzriI-qfw4fKVFqURoBhxchelJESgi7REnWgCQoFbBMjhfU-35YXYNmoe_xDAHXEzDEOc_VZZMQXP3zLLXSCAQCi0MhqH2Khyorsl-cXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=Ul8VAnW_HnBoO-864udCNHa_A8kgi7czlW_T6mqIgfiNILmNi4y6RQwQmH-ACivebjnvjmUw6VuhIwYM_YS_RLes_6zT_07DUUfNlyzX0T4Ov4vVev-z0N903bIhPIzsocExvekJjLRQ3Bc9zv0Aqv28OP7iztfi_yrqdHaV-LB7NdkaNo-VtNp5eFWftQm4RyUpUufnAftPgrPTF41Fg0W3hPkVtkEIz1MFjzwwvs4OJJzriI-qfw4fKVFqURoBhxchelJESgi7REnWgCQoFbBMjhfU-35YXYNmoe_xDAHXEzDEOc_VZZMQXP3zLLXSCAQCi0MhqH2Khyorsl-cXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kkq_GNp4NnSIyzDCoufv0ZGFpPjpzVztfT7cIAFVcB5dC_Bbly9hftbo0n6gzhMGwpA34XyRunLMkfs7Iz_3hDWmYUQlq7qYZQbNhV-HJwFmx-fxVIxFHfSY6G-fx78hkFItE4bmZucxlGbsz4dbSQ-_C-mF-wfMCTZuGXTNcCAvorm3iuofJK-HP1Llk2Pw5pjXU8Ltx4YAqVEVfG4CRviJB14Iy4rJwG2QN02KRiBQ-0aS-O5njaLIEOV0ixPhX6R4Cr4kVWhuEz0PxNcF6utH7H2U5nCODmpVvRDEz-I-cHdCwojeSQUjXVphyfjCLnNpOGLHGJf1Cxfpit9t3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z5rk2nemknGMB9Kllkp7DyNvHdN7IkcwpskLg0s_OeRfsNND-Qh7FXC3Dv6USxxJMTZqXn9dWv3TeI9fsihtQRelqbasggTzzU5hvyP0nG10q92iDtakDG4CpBI24raQnRL7GoqBOC1ENWD_HYLZbzeImfD1b1Qyxm9YGB9GmE7VN2mhG2ENCImgrqsOg78gJT5oz164lSYZ7CcWLMYltEqcdvv491ol9Qsk2oMi60btbzWdnhS5JMkWAlxy1JyDSMTrORe1wrNqbjh-7RUa-1z9Nnsu9EQ6fUwnv9E-6cxPD8SQWACikxBg9p5prp7kIK6M7D_MsdZDRIg_uRo7TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ClgTZFwPRgg02eM9s533tWu-yxTGJMepRqRORJ7-21EIKscLX-t-IiDfkFTtmz6lQjj7rcguriN1pYeUmXOca1cbM6x7WxYn4Wd1Spoyvu4u6Hh3foal0HeQmLO86ibQdbpUzXiE-yZgFuS3524qx8iLHI3nq0r7Hip4gjkiyCtuA37xqH05B065-DP1jzW_Km960zL1HRdRtolzP41hqSkn4iaAAWG5jwT9avbh7J2DskEgwL7CMXE7XCkkf5VNGKJHTPVTDqOymCTrvIlN2WKo23FcCHWcm27crjV-Lw_0eVMLqdCYe-6WZKdptFWS0YeHxRHcXd7iMzYiY_CoGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=LRVkyYyz3XFBMRH0953ey0H2xdPg3yRLv7LfYeUr9y9MQsJzvdiu_k8Mn92t3zxigWQlnwQLG5WRtjOqjx-Ipl2bDFe9CqRh99cvinn2JiZm3ya3ZxIXMnrkM_yIZsUXkk8l99-zAAN2xXSOIyLmXkNR7bx0NaPJ8qgwhNYEwQhOFcV0jh1-25A6D1X5AppK3_RaRxXLIy2g7vCgW4ikjYWaFu2CjsEKr2tn-OcWUsJjVH453euyrapofbdyPyz25JbfUFZea1AHmL1UNNh2JACgXILFDqEWXsDIrdxRp7XCwvRLAr54PaKr4JNu2Yg40-DqG_3BVu48NUCZHAa3BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=LRVkyYyz3XFBMRH0953ey0H2xdPg3yRLv7LfYeUr9y9MQsJzvdiu_k8Mn92t3zxigWQlnwQLG5WRtjOqjx-Ipl2bDFe9CqRh99cvinn2JiZm3ya3ZxIXMnrkM_yIZsUXkk8l99-zAAN2xXSOIyLmXkNR7bx0NaPJ8qgwhNYEwQhOFcV0jh1-25A6D1X5AppK3_RaRxXLIy2g7vCgW4ikjYWaFu2CjsEKr2tn-OcWUsJjVH453euyrapofbdyPyz25JbfUFZea1AHmL1UNNh2JACgXILFDqEWXsDIrdxRp7XCwvRLAr54PaKr4JNu2Yg40-DqG_3BVu48NUCZHAa3BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=jqjOPUlWiDT3XsnO8TauzG1Sc3mPsDSpOIdOUa_E_4kdarleFlWhWKm-_DLGCF6yvYNqsUwz_i2E3knTDLGlOzyiNaJsIAtUO_ok_Rts61cad4sVrEvYAzn2BiglcXDb5KT6R-1VFA72c0HkhYfK67uNhhzEWKAxU6uEIWz2a5bQcgNUmQ3O5c4c_ZQNCWW0-Vl5N8WazcTCNPPaBUGs4EheZW_USPhHthxy0i-0F9sosMCgcHiZUdkKupH4wscBsXzQn50tlGVmOF1nsrYADVS5kG_X2UtzQiEG3Db9JsVXB8MHA0ndjnG45amuyWi-EjU1cfFQzEkGFKjcEPBr0oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=jqjOPUlWiDT3XsnO8TauzG1Sc3mPsDSpOIdOUa_E_4kdarleFlWhWKm-_DLGCF6yvYNqsUwz_i2E3knTDLGlOzyiNaJsIAtUO_ok_Rts61cad4sVrEvYAzn2BiglcXDb5KT6R-1VFA72c0HkhYfK67uNhhzEWKAxU6uEIWz2a5bQcgNUmQ3O5c4c_ZQNCWW0-Vl5N8WazcTCNPPaBUGs4EheZW_USPhHthxy0i-0F9sosMCgcHiZUdkKupH4wscBsXzQn50tlGVmOF1nsrYADVS5kG_X2UtzQiEG3Db9JsVXB8MHA0ndjnG45amuyWi-EjU1cfFQzEkGFKjcEPBr0oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icongePsultf1Lyq-E7mQ4aOAAfjNYbkT0k2OcAaDd5Gwpgh6Auzh_C9DAVCUwk0qVH09hWqgBq72-XlbQUGiRGAYuamCi9SZbElvM553LtjSj0-uj-n0tVfp5wWSsN0JRj9nHzLtVrk1bGeyVISBkQZsieJ4foO7uvyEUHakPbkD6ffl7LEPDNzNUg9ThLth5u9ZzQOFiRKP-XS0SFmkkWH-qFT6hpjtiJaJxXZHE0a1XoyBXSDJollCe9dehJB3wTdU7av8LJRMdBfF2Iw6IRSeQsIknIuXbTJeMSUNSxOQWxB3jaQv-CO0qnx7wRMLnjVjZ4oFnmlNS_C2ac5qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZBGSp5uTZ_dPOM-OmRfXkxeE3f0u3ag-atWH5hI3X5SFEoSR0Y7GZ86VGQr4_sVMBIxA3lK65IbeXkVTxeMFXVOgROVqf30dVBgaskq20wOLEZUEO8QjOaPxMDG-iC0bh_417fgkim-nOF_fTfdwT4OPFtnFv7YfkmujRkEd_p_1SczSgnLIIe5qmpXEY--yE-KEvy2C29kK8Dru9P7yLWKbHBJXHF40c50jHc66Afriiaejn7SkiElboQHcd0PEhNR1KDi7Dh1jXTH-jViNDrBOwjQsYId4x1cEb-btijjiHy_nduBfIWap7Ci9Jvi-G4hhTRCOCevnXq5rs7jVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=YZF4X-c5b3U7AlFOhOJ64Iom0MyG9tohvgKUPDvhy1wQJAvJU4mN-OJ3HnxpxxmqzcRUSdTjIFFJJYjyfhVOcWQOyWqr0E1mH8HNsFKygTXQyzQbw2yIKLAQukB4IkTPjs6FOmVnkXUa9w4Ifa2Zl3yWL0XyUT3D7TLZJKQkh7IqWSWPBpOJzV_6ZLC8xa5eqBiCPJUgY3Pyoxk7-KchEvPSYtxe4uEqCGy_SHcS2M36qTYnZVpyP7uJm5YOI3wdji383WMkgE6HvhxDOi99eropZTR_spnD3ibF5EwqS8kOAvAeGY2dTq8raahqU-uasKBdOql1C2UCbt5skHGxYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=YZF4X-c5b3U7AlFOhOJ64Iom0MyG9tohvgKUPDvhy1wQJAvJU4mN-OJ3HnxpxxmqzcRUSdTjIFFJJYjyfhVOcWQOyWqr0E1mH8HNsFKygTXQyzQbw2yIKLAQukB4IkTPjs6FOmVnkXUa9w4Ifa2Zl3yWL0XyUT3D7TLZJKQkh7IqWSWPBpOJzV_6ZLC8xa5eqBiCPJUgY3Pyoxk7-KchEvPSYtxe4uEqCGy_SHcS2M36qTYnZVpyP7uJm5YOI3wdji383WMkgE6HvhxDOi99eropZTR_spnD3ibF5EwqS8kOAvAeGY2dTq8raahqU-uasKBdOql1C2UCbt5skHGxYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTKUku0U3CmK9OrNIYfrW8guyyOobzUXfF_iYh7SijM1HTQUDUHlVoz827qd1hEOdHh_GiPD1hrRL5s8_Xd-vZFuYAkcYfxif_OCA5MSG7eG5Nq9gAZGQ3JZHTQtoSB4cObtg-XEJ8avk7H9CgLdUL9TYhvmjg0ATDz0vVvTvL8JfKOgeL7r2NEdtD3QGoQ-uJxkjRgFSgNj_MCSVlZjmCtJHrVIx8yTSOw8HrCfaxrvXerxAN-W4YgCm4aol-3OxB9pwr4mIW6rY4ZugJRIaKGAPlMuJHkiJOCqNl8INI7HUWmR6e9Fa6QB9cInDbqogwXgsUe-K6V88AKcmRwU2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VY6hM83tak32VfiDUvzjYyyO-gTMNp_Kl9W4nGUE_3o1ptFbShb6LKnKkl-VzM2kilBn_IgYiRSORvKFEjG5x9pmAkLhpd3aZSO3B2e-kHOw_CH9oAX5Zq7QbTsxnK9IAouJ6C18VG8Z5d6b7AAvQ1EoG6PVtf2RxfBNJUmAaKguIPzgdMlqfWwzCYtgcJ5_W9EHDz64DG1APSqcyUzSbIHb1Z7AAg6i7jjoDB0RNiGjAs1fhCFkGfGCKw7udc7E29Qb35rn6qhiRySnHpUBYYG1KgUbuyjwypwCqpWv_JIMA1B5u5XJf97DsttbvLB4Ana3_JgTE7q05H0f74BuLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqFjzzViRVAZ0KQSTK0j1JarNxG9pw-HhDdZOctsk7VVNvuq1Xg0X8clirKoFOAdDd9OZfp5YSRgnqhCON_eEsL4xHBVeZo-kHxU3dSBz8TiNCnC7iZLHCMah91v8qr5bnSbe6X1L_g1o5tTpoM0mfSdYPOnIUtzqf36F00dr1zH5P6tRw-OwAYU5UnklF7yWgHOS0USFuD_K_2gtNe6tib6LPI5XwguREFr7n89Yqp7xOk4PCpis0gdqpCk2JVqjbM3yJwup5CLpPBddy8b-IVUU9eV7D7spaXYsRg613m77Mb0_rp-yhel1VVsPlflMpiRnOneklJgED9WWJMukQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLZIVlui3Xh7yXdlQGuwcvBshdyw-2rLJnNcuY7wnKyHi-t5p2nBLnyW6SiH-lrZh9lRK6XUlxOecEPIIVjJ_l_R9B1Vj3TBmje9LCn1J8yc8hNZLDZhcQ1mJH5QAbuW5cRVf61vr5VT3DwEbqWHHeimRfCWXdWrJaF76eVwltSpd0Zwi5mfjOf6ayMT15MQCnwWob07gf2WCcI90fIPho_5IJhXKMeHr7RBbwteWyJpnqWj5zvfsO7qoFxKq_EbIYL3Rb_HBafQzD0YUFeJyQeK2ix2sEBOJi8bczt0StB3OI0vp9tthylsuCaDCC_pmYw64p6xSKGWVEVxHwYHZrnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLZIVlui3Xh7yXdlQGuwcvBshdyw-2rLJnNcuY7wnKyHi-t5p2nBLnyW6SiH-lrZh9lRK6XUlxOecEPIIVjJ_l_R9B1Vj3TBmje9LCn1J8yc8hNZLDZhcQ1mJH5QAbuW5cRVf61vr5VT3DwEbqWHHeimRfCWXdWrJaF76eVwltSpd0Zwi5mfjOf6ayMT15MQCnwWob07gf2WCcI90fIPho_5IJhXKMeHr7RBbwteWyJpnqWj5zvfsO7qoFxKq_EbIYL3Rb_HBafQzD0YUFeJyQeK2ix2sEBOJi8bczt0StB3OI0vp9tthylsuCaDCC_pmYw64p6xSKGWVEVxHwYHZrnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G4f2JM4Hz1zDqpSg1NuHxz92i0s49m0AjsX8NeEfOy1cgi1gVRN6zPSUNO21OBAfQZVE39x2q6Q6iVjTm431JDCToXVDFHjoXTf04qbNYD5jAGOTB8D1Bc_w26PwAZfTgSU-1PPBI7u4J5dvAHbWY2YjHgS_w3H5-bL3q6Ih0OYZulM5yWJmxAYRCjyaT9O58W7tkLoQknHNu9iXN0Titt2gnFxjc1660YLXtzSP3fFG94FNYCzibDol4fvJo9qfOeu-UppvnjNk_jXnths9Dr0NyfBUEzP4fAljT9Xj_cja8_RRDibuU5c-OFBBjJRRQNbdFto7AK65Eg_auH5Xow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RTey6b5PeEKdEGwCQhQi_kUql9Q4cYh8WDMUx4O7-rBydRpFIN3fY4N-PN_PeYr6W6ZlMLuhy_8bFV7YAt-tn0FVqj8Ug4hg6fIAUNtYkqrt3IaJTKu2UlrGxcrFMtveUpBskLyRGKdxarJDTnY_68QC5DzJALUNZ80ibJLkJP3GfwW1AhZkRuAy3nSZWOiqndkldPsDXffmmeYesMV5SiMW1ZbTTAFBT3HgbIJUiRWitGzZu35H0O34bA8fMX4xq3avXNZFMw-exGjqlzPbu4Tye1Qc8E7wDyx3qjze078kPozrCXY2ANYfmHzvGdsgfQKT--tIDWxp3rKWv6iXyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
