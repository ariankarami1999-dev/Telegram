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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 18:14:03</div>
<hr>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UeEhMb5MMMtdBsReytDEPrXUtsaNYd3ZgLcAFoKm29D8sGrRU6UaLhCe7cTC8fLVNIPTQRsHdJ4L7gqzB515R9BXlwj4bTsyx5OZXDm05lAC1HoKOjCMxKSV3i_1GauLsMtJY39aRTyGYN3cOl81elBKfJi6U_DmD_dU12ypZTpIEKOZa4A0YfMAuOj9hlp4kCdq4MdT3BMLkOyetIIOOkaNdUkcwIs6-wK6SbUUR_G0Yx7FrA69p9BdTDbl8ljR8uSLU25yCfXg1mvDS36SRO7yRCuu9wiI_oeYsa62vyzQTTPJdYpbQ-s9b5KpjnVmzUV8ufX3gn6bkWGtSaNLUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به امید بالا رفتن قیمت نفت و فشار به ترامپ، زد زیر تفاهم نامه  و حمله به کشتی‌ها،  که با اقدام به موقع دوستان خودشون  در حزب کمونیست چین،  نقشه‌هاشون نقش بر آب شد!  خدایا عظمتت رو شکر!  اما در عوض برنامه آمریکا در پاسخ  به اقدام جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farahmand_alipour/6518" target="_blank">📅 15:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6517">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwIaN6o6q6bn-9uCcTMpR8mSdg1iA534mGRYSEAMaBCECUlM56XZ-5-T7MIEcKMn0yLAKu_rDAifejaKLpSXmV7McjFxdugTAjTw4dPNNNvWBXO13e4biRch79ZuCtzuCiayZwLBKw7Dti9prwrY6TYmf1lyMv_0mFYxO4VLY6Mh7MOe2ckcm_WboY398ZfqBp1iznxOfYJS7ZT1lw5uoW1t01dcuFqaGBNhfbw0aI8Ogv3o2Q3I4OgTbAoKZHruJ8WbEveaRpQ2-NsNvRGr9ntTj8T072dMijFdLQ_jVyzGMWHb49Q-HEO7iOS4J2OPjb59ja2wSNYFtyG6WREocA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم : افزایش تولید نفت کشورهایی چون امریکا (که رکورد تا یخی زد)، کانادا،  برزیل، قزاقستان، ونزوئلا و….. است!  نکته سوم ترامپ!  و به نحوه مدیریت ترامپ برمیگرده!  بازار نفت به شدت حساسه به اخبار  و به انفجار و ناامنی و جنگ و…..!  خیلی وقت‌ها قیمتش «روانی»…</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farahmand_alipour/6517" target="_blank">📅 15:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRiInt98MsxwvNr7uVxgWJUBuPZOnpcnYgUUcRXoZNF2PURZG7dJUCvB6NWKz8RyOyrl3GgRPt-p-bHlRG8HGgxXTIzlOUCNCSHrA2qD8ohFZk4Xv3Hg6LV7SQIVAh0z4yOpvAZqayduz8ZBdmyiBU86jnumMZU89sNhnwzPlz5L9clF549E8gMl-GXfOPiPcNXWYo4g3UYZCfbcGFwYtZVT06RSa11IpRDKnwxG40RvonMyF51cQur4cxMRRgLsOzLzwIodg9n5GUMrAM1XHm06IB74vLAy9biH9Az5CdXVZGTANCDbsxBh6LfQ04XxcJa8tvFOZN59sj_b3zO93w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف نقشه‌ها و آرزوهای جمهوری اسلامی  قیمت نفت خیلی زیاد بالا نرفت!!  میانگین قیمت نفت در ماه اخیر با اینکه هر روز خبر حمله به کشتی‌ها رو منتشر میکنن، اما بین ۷۸-۸۰ دلار باقی موند!  یکی از مهم‌ترین دلایل اینکه قیمت نفت خیلی بابا نکشید دقیقا  «چین» بود! …</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farahmand_alipour/6516" target="_blank">📅 15:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BZOd5cb83U6H5HSsLqWjepo3SgyQUS5toG0o1jtX09pyKd9imRC_6SS2T5SfzI8ULqj9ZT0oG5lC5KE-l2Oq0KBsU1pjaZg6y_ttBrTjJOsFF49b5vQFnoOD1CGQcPYrp3o-AAqlL-6yu59DhMQZUA8SZkCQMfFN5BrjKQ9bGAHNW1gClLRBJfij6sroVvf5_xM_sO8jbv7l-LGdNMqTWr62lP7nkYdaMPNiUH_VRmgaSWJGsA1w7fe4Yjsag_1k2L6i798ol_Qt7CmaLMcwEuRurrvE0xbNg8EFX7HzpMOPoOaRlziUuicilUG4QnOCPgj1uYpo4X__kXXadY8EpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A5_NsLJY10WqwGbIRODHAiqJAunuy-KNYma1idetQw0T7dRh9SokxSqIgCwT5bRaRA0xBCnZC0ac-HMw9dIoC7Gpdtapjx2w1aQclKEamZGMUz5koep6fDlEX2mWbYqooOROpeJyINA0EiayIqYZZVydFpoo3uUyFELkGt6AAkB5ITXTLtdVI6f-IGwqfbiqMTKK6iA6AD9H5vFmW7EGE4xvWPxxhfv0_jOn3XX5ZSAEIXL-41OhT8xOB-4iu36RWU4afOXwRG_XY0df-IF1b7AmcFplguzQkCK2cqd4nt10dDI1lFLipcs9iCmxpFV6k0CZMoOVEh_79aCYvOLU0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جمهوری اسلامی با امید به اینکه با حمله  به کشتی‌ها و کنار گذاشتن تفاهم نامه،  می‌تونه قیمت نفت رو ببره بالا و بر انتخابات داخلی آمریکا تاثیر بگذاره،  حمله به کشتی‌ها رو شروع کرد.  تا با ارسال پیام  «نا امن بودن» تنگه،  قیمت نفت رو به شدت ببره بالا،   حالا…</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farahmand_alipour/6514" target="_blank">📅 15:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.  اینها دنبال «اتفاق مبارک» افزایش قیمت  نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.  اساسا با همین منظور شروع به حمله  به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farahmand_alipour/6513" target="_blank">📅 15:02 · 15 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farahmand_alipour/6512" target="_blank">📅 14:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.   خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.   او همچنین با اشاره به اعتراض‌ها…</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farahmand_alipour/6511" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farahmand_alipour/6510" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2SgKn4EnNs6qzviU80TCo9WFcTQFjEu_EReNTw24Zdl13i3skjsQK5m2p2k40jOI5aCoLRn2XBSshIKOKjXla-ZDxl1KycLOHUAmoIzEljKdqR7IrkRiCeVwT_9Z9bEeNlectpAm4R3uIbu5iBi_SwHkouHi3x6OII4koxes07nbV_FneL3hTsvFyy_hAciLzqtVHhorZqHP_2afJRZchgveexLZBi8KAjUzyUUh8fkKwvnufhomjQjiW9l9jtKskFGMjA7v1LNSxGGsOv6ISYdnFVDJbDWkkj6lz6U9zZUKBVZvhCm5c7-UtBLRF9hyMPJWAaQHmxB8dnanyd11Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب PD که همون نسخه حزب دمکرات آمریکا در ایتالیاست،  هم چند هفته پیش، چند مسلمان بنگلادشی  را به عنوان نامزد خود برای پارلمان ایتالیا  در ونیز انتخاب کرد!!  که آشکارا شعارهای اسلامگرایانه هم میدن!!  مشکل ملیت و مذهب این افراد نیست!  مشکل اینه که اینها آشکار…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/6509" target="_blank">📅 12:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtvY7pvASyoNzE1MgzbmI19FAUjQSKLVX8nP1mr0oTry5Kco_dGNHIQ9lAHysx--cf0Z7hZQSy55Vg8Bgz-QvFTNoUyQeLDjQ8P02-Ezl5HLd1wFmqqIU_bAy3nN5pNfF1nfEzGD5pexnsHeZUlbHlwLvpsgFG3hZM5kUEESUUUQA_lNis7IPYPF1SS7BD3UvdFDmxDU3raBS55ep2ntzcFhEBxD8jdZX_f3mwq1QFKbRObBZF_RWkhZLuqLERybPOSpyBy3vUrU7C1FMffld7xaCTB2f3TL_qaJWlYieYDODkb84q25478JeTGCvAspVqpdIXQEvfk0NNyMU3-Glg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!  که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6508" target="_blank">📅 12:37 · 15 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6507" target="_blank">📅 12:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای : پزشکیان ۲۸ بار استعفا داده و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6506" target="_blank">📅 08:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_0-ptsJ4efHkAQo6huPuY_EM4QKUmw1vw7Fw2yb62dglPo2dDtFjm13hBcPVJAYPoD7IXEcdAK3YJ4IoHY1IcG1oY00nzsuQPf3WsFcks194zbKE9VNKMT3gxQzCG3qFkR4ya953IR8ekNef8XFXWsflG52MVqq-Pfwg24Pf-SokaCr6QI0O7kY0_gTyDIeIGrbkgbPVbeW3WALodJhZXGJYsSl2KaJhSLWbLPHWO9JUWQD2QdCAyPo-vAn-LsqVDG9AA_RN7iVdVmu_rtZxSH40UFFDAXQh9545lW37HDkYmQq1bSSN1JeHd8Lbg_pghpsu5eYS4FMh19R7wiWjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توطئه است!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6505" target="_blank">📅 01:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">آسوشیتدپرس: مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6504" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6503" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6502" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6501" target="_blank">📅 12:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6500">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=JsuNc3NsVllxKLfZ6vRmF4mqxjeD_CCwQTrwxXuyJlPABaHmDNy_aCvv7YFj0T3gZplLgD0wQRxisyS7zHHcQh7ti9H62synn4Icen_ePnR0-pzEyl2938oDpYLIG0Uuw1EQajLIvrt8mqMMoRiT5pU2MV8AUaYRjlfFu4IPs4tcEyeeQhdeThpFu64zDFXR2aKTl0_2MWUAcBjc3cK6_nRmVuQrvDG2Rb7xBbtESN20Z7Rq_rP3_7WdNeqsEgHMReynjJnNzyXoN3ZzDM94gzLREJY6ox4QkaY95sLXyEE4io7xeRGZZVfAEN_zsjhfjs9r-3X5rdYsSVHio0fP-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=JsuNc3NsVllxKLfZ6vRmF4mqxjeD_CCwQTrwxXuyJlPABaHmDNy_aCvv7YFj0T3gZplLgD0wQRxisyS7zHHcQh7ti9H62synn4Icen_ePnR0-pzEyl2938oDpYLIG0Uuw1EQajLIvrt8mqMMoRiT5pU2MV8AUaYRjlfFu4IPs4tcEyeeQhdeThpFu64zDFXR2aKTl0_2MWUAcBjc3cK6_nRmVuQrvDG2Rb7xBbtESN20Z7Rq_rP3_7WdNeqsEgHMReynjJnNzyXoN3ZzDM94gzLREJY6ox4QkaY95sLXyEE4io7xeRGZZVfAEN_zsjhfjs9r-3X5rdYsSVHio0fP-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمان مخالف اینه که از کشتی‌های  عبوری عوارضی گرفته بشه،  جمهوری اسلامی چند هفته است عمان رو گذاشته زیر فشار که باید بیایی با هم این کار رو انجام بدیم!  عمان گفت : تو توی بخش خودت اعمال کن!  در آب‌های سرزمینی من، رایگان خواهد بود!  که خب جمهوری اسلامی فهمید…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCpJ0LAK61XZoPbBTEsQFERsplLMpW6PaxAwuYoPA3prJq4RazKgjfvn18LF0puiVlFZsA8NwHoWVpWccXc8KT3J6QMra7hsMcqaARzAeo-iK6vYgc9kLeJHL7MrqHwpbxHyhCzHyil3dRlGPx0lPjihiZLUIBDtYHj7l3eGsMDrXXoZ2fLeTl7pZtWUeMiHAEpBYrrRRFz-s_HLdvDR3XgVQyIbB0-YmGwplrv50WNiXgL3_ADr9iLVF-RSs-V4Q4zqpF13IF7hJuPR7SqXSQEHz2PtID0kpkFJq5boSehSzBLGlaTaPKhBUL9z2GlVAdoPcFL_8EQXRMeO4ywcyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCREV5VnI9qV7nf7ueGS03ZyIU3SX8PAq1AhrGa2qGTLiG-norjMBKgmcMl1yPuc7D6tv867deFBo0y34-M9DVJtXs6ytgS7S7c1Ebg59V35JfmJVuYq51OKpcd94c4GjYV7gRQtWF54PZIm25NrMm9FkBM7ShDFyrzCuXWo7TrGFYsZHZTQGjWdbtyJhdANof8Frmu7YPgHOf88V26lH45tImK7OGotmoNVxArywZ3JPlElOceexUzk2aNlY5lpCsZr1nSstAY9-weX1mtSFI65TINzwXBNmv-uegPtBYi2di6qPZ40My2PMKT-DE5qofHcPMX7TtVs5aIb2KYMSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToATjIVERgkjqsfmfV3aJIW8MBI4bf6HBICLQCYlegSP1jOB2PM5JP1gJ3nuxRP1GlgmQytpejtXHofifSlh23ynPONjulE3r_KdHOt2cDglangmPrljY81pyMI04LZew6Ldom7eVIxh7WdjnHONnan-71YFPMOW7WV-jnkfyaWnFgrjxoVimOo1wfBITyMr6fbAZiIVChgjC7uYJnQ3VpfpfkIEgcyYUM6aSEj2Jn5GWN6J7NSt6b_LHZAc5xF7u6LH7Z80fNy27xqfy5O6XWIEidzushXK5mXr5YJw_y1oIsni3I6Pp6lyCh_vz5LzuDAJ-co8vo1uQkpSlcsxxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.
عراق : از طریق خط لوله انتقال نفت به ترکیه
کویت : خط لوله به عراق و ترکیه و همچنین به عربستان
بحرین : از طریق خاک عربستان و‌دریای سرخ
عربستان : صادرات از طریق سواحلش در دریای سرخ
(همین الان هم ۷۰٪ صادرات عربستان از دریای سرخه)
امارات : دور زدن تنگه و صادرات از  خلیج عمان)</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6497" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6496">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6495" target="_blank">📅 12:13 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=sllWH1MQMpeHcc0Bq4ze2ske6kZ2TOkELsZG-4geUiyhsvcOQPCPIfGC00DELZRV5V79VEb3d-cdZnqGCfHXQBM-t-Z9vMJvf27JYZZOMtBzM8HmU51g-l81WEmCQ2i-FpWx-aEZnqxTwa0xvemcwyLjcj8g8wIf9r3ir503A2rY3d0UAxTBdGWv2b2mkVt_Q_oHIanOAA9fOJl3uq3OzGXcBip1Q9aq9ZUNfzS0dS9DPiwfCkCQud6qIHSS1vfPtR1tHSAWtpLSNaa1Qh-ySApU97D0mOzZrsdX2dU1aXRnTC1K5VvOnzTxrgj8iu8bOuPbtrrCogiNuBnxwIMc-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=sllWH1MQMpeHcc0Bq4ze2ske6kZ2TOkELsZG-4geUiyhsvcOQPCPIfGC00DELZRV5V79VEb3d-cdZnqGCfHXQBM-t-Z9vMJvf27JYZZOMtBzM8HmU51g-l81WEmCQ2i-FpWx-aEZnqxTwa0xvemcwyLjcj8g8wIf9r3ir503A2rY3d0UAxTBdGWv2b2mkVt_Q_oHIanOAA9fOJl3uq3OzGXcBip1Q9aq9ZUNfzS0dS9DPiwfCkCQud6qIHSS1vfPtR1tHSAWtpLSNaa1Qh-ySApU97D0mOzZrsdX2dU1aXRnTC1K5VvOnzTxrgj8iu8bOuPbtrrCogiNuBnxwIMc-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای :
پزشکیان ۲۸ بار استعفا داده
و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a204c96911.mp4?token=pTGQexFZC7fRiaTJlgKvNbh7OSbR6z0P4oI0DmPpn1OdyY5ZEUG_naHTlLFhb8aOtl1an00JZ_W5EfDQCBsRf7BzgXh9ln7M9GX7OUTvUTBTVo-1mMstg2Ym_4mEZ9bGTXKORqw7OW-jpiS-nvuUPOwOKONcIsbYUt2qm9bAayU2MMwQvj_UIQuSpdERe0l9ACSABMVdZFq3dJVgGRwKsl9lFEw984znJkbu_Y_I5lMtam4CuovBW-jBzA4Xj-ZCvav2e54JsyC7xfMjmWilS3Vr3QpTbMYXIvpu8BPjvrbXXQcX6iyH6DjfyFj0oJZz_V9c5jHHpzAp1x24vjXzYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a204c96911.mp4?token=pTGQexFZC7fRiaTJlgKvNbh7OSbR6z0P4oI0DmPpn1OdyY5ZEUG_naHTlLFhb8aOtl1an00JZ_W5EfDQCBsRf7BzgXh9ln7M9GX7OUTvUTBTVo-1mMstg2Ym_4mEZ9bGTXKORqw7OW-jpiS-nvuUPOwOKONcIsbYUt2qm9bAayU2MMwQvj_UIQuSpdERe0l9ACSABMVdZFq3dJVgGRwKsl9lFEw984znJkbu_Y_I5lMtam4CuovBW-jBzA4Xj-ZCvav2e54JsyC7xfMjmWilS3Vr3QpTbMYXIvpu8BPjvrbXXQcX6iyH6DjfyFj0oJZz_V9c5jHHpzAp1x24vjXzYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تبعیت از ولی‌فقیه بر مسئولان واجب است»
می‌دو‌نید شمر تا آخر عمرش
از اینکه در کربلا شرکت کرده بود
هیچ گونه پشیمانی نداشت!
شمر خودش از فرماندهان ارشد امام علی بود!
توی روایات اسلامی هم هست که
هر بار بحثی پیش می‌اومد دفاع می‌کرد از کارش! میگفت  تبعیت از حاکم اسلامی بر من واجبه !</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5gtoXyZd7CJSad3wbsDE57B5orQmc9D7d1-u1S9y7q_m3N9J6JeVJN7Fvkg8miSsA3JcVnvBJLBDyY2DAlDH2-C6bo4eaELGxevVaReLsFcGeF2LOgo43tOYN0ev21zrTTxPX1LvzWHGRgdPac1sPbvSc4rS6ZuMxlATM9oLVc20skfQjJbBC9EPFoAiMq9eoACMEur_juDueaG998YZKIRK5oe8vhQqdHpqEpr8cVhe5Bqo5w3JE2UygJJIUi1liur1_KJ6b4a1IMbAC58Y320HSQ7X8jgKuTC4rmsLnkBPR5SbpRRjbPjIeBu_tL0fSLe2KYltM0h-koFQVwLPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7XBybyHI78_JTFJsUEEP5Vr7L9-WBS52GSRxdzUKXLXe8BPZdPm1Ep9HvCrM66VrwOa-hOvJAyIGTNsvCiXd_IBbUyUUI0GBbxQOQfOPB2_nDSItH7c7-wRqcgf5lMPgBQfoR4NA93LL7OzZCVtqaQ04MCiLe7si7xfzzmuTih_dee5znr9U9OJWYtCXfpZq7lfSl0mUVpFQI3vy0npewMG07tYkSqrO79ShZzHyXRBmV73y6jPnHasSdh2a1UBXEjAtDACWvBh5xAdexGc7hFPu-XzyXXBPZLj4FbDeJlb9gALDZe0KEL69OKid3LyIlzcJlEmCpCtR_16VUCdeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kWYeOErG3xWzVT5GtIyCPujfngQSO4-3XS9Y86RsxtHwy9L-89dcKCd-980KR2BWsgZfSS99c8xAwU0cvgIJQ9UjBjih73kRsMnoObmsrMptlFlMvxtw08A-EN2k3gmJ-KmqdgXMrdwI8eYWL2UFiDlQUKmdUr1IhVnv_qkmq9T6fKyWoKl7O65oaM7mnes_GohqKOy3Qe5rYT4GEJbjHC9lE0TuU9ceqLd-AJ0Rfjj4XBcBeZLk1WGxa1CJFIwKNqdcvNTODF-7ZEVJU542KNNLVgyAnElev_0-2m8Ru6LLK5s0tI_q7jF71PAnD5N6NVVz9L3nft7eCDtPfc1gyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QlbqV9jStqqeYUmyaptYqjqmF6tnACX3zQryb3n0_RUFljj5MxqS1BBfnW1Il_ClfJFbMUnkjnn-3i-PbwqOVqBzQY6c8Y5WXoDbJ5GsM753OmcrzZcJqIB46dwWqTyO2ZDkh5fSkGIoslNxDlva3YIENm0ZAJnmAhs7yMf089pGTe57OXIcAK8w0pUl_VASzJj_C4TDlr-Tdq4fW8jIED-PMx2fkvZ5BL8HZQxNIyVWo6LRIR-3dEQT_qbr6lzzFJn6ql86pI0OX2hmTVzf-M2fONsLiVMdKsRj6tF1L2TcMAeoRDGPLocVRmEkAJWW62lXkYVfUnliWeuDft7afA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daxWpJSmwFAFFzK15PLI5wrs3gTKvvh8D3eQWjd3_G-Kr5qUEc4k_zBPxqIvq2mDF17rD_Wo8C8RUgdpC0hnwDlWHHUQRZqNLL00JHqIvax94TbmhJrel5uLyMa0ddXhKKfYgqrY3jlcdELlTU7SmVTuQAhFYp9geFP8Ni3YWqCxxWGLMqZaE9YGcQiZ0RaabmGBEUF3cDUU8ILa-rJrUuTmUV0aKJc1rPSKJ-bhSOWDxfs6feHDRwSxdHcuMZZ443Olt_-q1TDSKIdiqWUteYhEf2MPtWwbAimf-0oTe38reOBuES-6EJLB1u9UtR3DdOgzxNPXCXYzOaakpc0P5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJ-e86NbN5Kjnn6Bfq-0zWh2yDM9oMeJWo2bZeALpMry9LnEHy7XOfMxu55Bypwp-wPOD7JkwGfhHUvCp5piSpS_bBzj1K6aS_QpLPuJwr5QQLnXHlUIxvrXNqxfA_XDuocvaVzvEI37jiwbLNuVjLVDYiaqzjkpglohrwnJBHPyJz7juIpXu_G6EmBnXJcc6HOQMHjPe_dGHl7He1_70azvZbCh8kkgEzQrI4zmCiEv42eFmvLjOj5nHAJ1I3hO4gS_gOa3m8liaQowAeV9cS4hU8UFjKzcBg3ba7LgB-sJGA5Z44dxYa9SlJGJvzQlDu_EkOkD54mTZNGI9TLMgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vtth-ixMKM-afeo6tKezHYYXoEviSwWSuz4HvHckyX1OT4tZNaXtuRyIVRP6mSd9BgRGuufEf38_K2VDBNGk6Cy7NNXgRYL0JqMGdZ5bhnloxxXkUtlqI2lKr9SnGeLB-FvqGS2FjY9Axh_up8_vyYlMu3OP3O73vfzopqBnTNCBHdpFw54If2w8g8QP8VNi2Tveonxt3pSqG8TFcOKqtX7BldgMIIX-SmwQmTjeQejcvyN8YLMKCkthjm2LGr3YefzrvOCnJU2ibmvqiC5y-NmnTzvmqebYHgaIMqwwgA_DEpr_fgI-tmtq71w4Q_WTCggvzKlx56mNKjnwxxi_iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2IpiGRNFHfBzQ7ht6eDlsVqteEmHR879jAEhzmmc9WnTZV2wJS63qiHoBkaau0CNWWlpWmL75Yk-sU-dIAXluDSD5dE5XaAQlXy67PciBDBuUIprjCU3wR1rvrNHzox4YaWcHo0ZPVJwMLNmbRyo4qGW5W3Fcte38wfGgZxxpaMv-p7GScLE_hfSA8cxZ3gmcthWKZIfwAMSrSXRotA0sbDDuEHYBqGsrcXrsQADdD5B9KmfoEEgQElXVwDkohXeAnwZEOILnrk873VqIZ5VSDU9uYDNKWIBFLaeCgCBegBfCKW8F7HxQhK3wum7vKcsD-ZiMMOoKluiUxnbcg6gQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTf3HQyZUmkOSOdHcoMrKkcTRMlEdPnPBpJ7YOfXCcH2XtO5UzX0s6xKY5T9v0rJuAyOhKrL2jSHp_gmhPGbHvFT_Z4dmxDaRr-jQnrVmwMiNFvt4kPB7D7eRETXvlVhRSZiDVslIproTwvkMgmLxGy_K8e1ZmO8X9qG6FloD26owAX8B91rSNrPiDK-r92faLqQzzAVj3gU6zWOqmL6xEJGkQEcU1HFgrbLRWdY5BuklJjlghUbowupqnxl6Fi6gjL8yRl9hPn7iyVrnKsJxBUltFCT-6MyzOrqDhjgtsBLfF6yusbURDGlyYApQG3-yLU0Xihf_JMKH6fyJirjWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Asgoaj30ajmhcMc_BljRdBAgx0jWjEkwy_JETrFDdS-u7kEC_xQKHS7vqySLQBiaKIFyJYGv0_tpFxq778lWTT5OxppszuZOv_BLp4AS9iQ8UVmgjFS2y-mENGomO_cB2GbBqf-g8lyGKd4xca8PdgCPaiqEFTO_zyPgSqsLtLx9jb6Zv3TwDjcGRWUHOnolsrxwUxSZGqSrbbngMRVoHb7u7c2iR-vxpmAvGqvrgWMgMSdFmGT2sl9Kbqzr2gEfKqkxMjmLUmTpwM7hY0z3BDqFp-WH9XM-ipVCZqfxInEPx70yoKBHjUUGPRBiSY-7M3YCPeYlnMXLfyvxADTtsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFr4GdCs251UQa-RcZz2ljpsf4ahcfktIagkGaO9TEuT27-Ip2BK_-3334B6LDfwrwYkEN_flMtIFBrM6Z-tuRsoYL-RVm7AOxglCgeOH8KySMifHbvkp3xnlgKIxQ3E35pa6lTfAbuurV0x_T3s1fc4swIzOSiHWwATclYihYkgxaAiT-GGv9tXx0wdI7cfx3Avpmg9MjgrdhPSqe5spoCbEKSY4BRM8Xzr4Tyq5-mNyYstXTk8I1nJ6eZiH-9zKn9-BM91iRmtGT0vNhPY0o_M6nfDM26ewlYVaaSYKF0Sxz107XQHtCqWj8uFHuOK8BwJxPEaKJgxGE604eAodA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ny4NZellmG-IpPcBp_XC9Gj_W_rJyrcM3KUqRbaaV5ZprgiKaMNmBOSHSe5lY7Ajep8tP_L0_s8sE5oERcKstDBcu0JUEBre5skaVRrfIyYWgHUPRobF-GW-G8T-QBCvec2xZbOmZcBM-vSeC9OhZo9sKgU9CqgDnAjvam2NX8dmoZ0ID9x_b5nBfFWiZ9gI4GWkDiCt6KxvbvYla04yXJ9w_tg2RUqwGfvcAciJdesLv1KLT0ah5kLStpz4fZSB4dRKKLsohKTic3bQZ4kAojn_wcO2gAm0PWtAvWLXDGBkKLzOjCjCLS87hntCFX_2WazsJGFW4XE-kAVjcSH5qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dq8FyWi5op2mXKZGe4J56gQ613DpIOrzpoAZPpEQzVvWeATE4UyVgYyP3nhyNGbvuj8oSsHt3H-RrQUn6sEmjp5oAMsn62m9gAiM8pUqwyqoEaxe5m6NdW9VTeX-H_pBWymKpxTGKpLJXOSqdQxZ7g-_GDr9aYQaCfXx3JR7XPk9vdcb-4HXqFTO1kuJ-KJ4eE0N9-Fh2OtiCdFsen1dNA2-LizXQL575Mpi_Iw08Ighas4mhAIpN9xNE44iscgC-fJqrh8L4aKqfNQkEJlpHIjFd5trguYngUgXjbX_xl5vlv9DUBSUFke1tESgeTfVjTm-QQ5FbrHQqqESkHdwxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SI0zxrirjgYuPJzo9TQXOslZCFIw1wjPUzjlnuRbSAkv5btF07cwKTc4Fw4XyARBG1-llS4b6xuXuo7-CLSZ0hLD3vwSHzFX-3_L0bAGiCJexrF-oAcvdzhnUruPj2YLRaFCYpgwff8V-vhHtG2c7tc0-wSntZBB5JJ9GSeKcFc84hrmyWERTVxT23F6tnX9o14baMZkKslKun9hGyTCkP07jn6jn8DrAMi9vvMN4Ipx-jTsR0VWFPXB8_TwBq2RjV6EzYQ-cKdySpQDxkeWjpGp-ya5ixVVlNTOBhGpTQPerAKDiHQPIRXLZJJIH9roDzsle2DV7MVt0f0fcGFMxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=eMXsKb2bK_gBlms-ZjQazbZx0KoiJ--ms7-4xAo59zdZ0_LFIGAJyAOJQKV9d-kCAZEQ6NEfWlLxfXkJ-BfrntiLvczjXiniohx9VL4v6ZREqBnthzlhDLZPviyHD4fgdn5TqKmuQ6DbeBjP0jl4rSlGVINIb6ayDSWZeDEC_uA16DXfe5sUQInR-ofdBChl4DKB-NDG0BeDjls-R157BYHPEZQ-k9E3zHBRDO3A0H6mcLVQjGfkplA05aCYKlr1NQW_o3aWE6FJVQUYB3ieZXUi-HVjm6Yj-KicdssKsQAOZNa-cidcmGyhL91fNUDjdkEsSg9phmSVzy6DyuvVsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=eMXsKb2bK_gBlms-ZjQazbZx0KoiJ--ms7-4xAo59zdZ0_LFIGAJyAOJQKV9d-kCAZEQ6NEfWlLxfXkJ-BfrntiLvczjXiniohx9VL4v6ZREqBnthzlhDLZPviyHD4fgdn5TqKmuQ6DbeBjP0jl4rSlGVINIb6ayDSWZeDEC_uA16DXfe5sUQInR-ofdBChl4DKB-NDG0BeDjls-R157BYHPEZQ-k9E3zHBRDO3A0H6mcLVQjGfkplA05aCYKlr1NQW_o3aWE6FJVQUYB3ieZXUi-HVjm6Yj-KicdssKsQAOZNa-cidcmGyhL91fNUDjdkEsSg9phmSVzy6DyuvVsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCLiglPfe2GndsE3Lz48kU6-lzjfgScGLEAf_A0mwzgQfk9VmxqiAFIZX5LHUsFWORmZCZ0bvci3aZStmCceewfElQJ6sSimJeIO5Fb0agHgAE3jY7gYziTMO1KnbHYuTNLApC9yUQHAFwlLAW5nT0N1mXjKSD-_WG9477M2AltmncNUORjMlkoqO-Uh2ttqorOc3B4zf1cyNlEMWgyvnk-EQveZztRql1K5FtxopamHjgn2egEdDpbStQtOswo3KcX5qEJPMWearqoO53LnoE1xWuZyJYi-8MAgCj-5RqwfJcbdWMHej3TuWpvMbQYjVBY2raP8mxkQ6vQ8VzGkzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q--v_K8Jznh-i3ZteSS1D8hZOYfyntFTI1Yn4k-0TXf453QyOYTHddG7tjWfDdeLmLW02pZBX1jAn6tZLGQOOQ5CjcPQGuGmB4DknESM-9Jb9wjJUlYktDEj3j6_VVteb9HMQRSWRsBeP0XNUX6o9hUd1ZMHBLkpw4KZIQaCdURHrd1kVcU0DUHj6jAy7dvgYUgOd_KpAGG7hUoxrd_8ncjifMeIWzh7-JKTh1IWTQsZ3qfsOgE1vx5f3FifzF8eW5DXbi0I0wslLJS-fONr6smU8iChZy566425_t983TWtkRQKdGBujf08z05xfX_Yh8claKIK4PTS9vYzyK6nVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZZBAVKYRfxnLQeMPNzuBKv3wGFQJVOb2mteBiisA9CmAwSuMiueZGzKibVsjE_u9uewh1jlTInHw00-Ud7FH0E343c6VxdTf5p2kmREgGd2DJzp5Roh2LVrN4FjeRkwXWOEkfN980-2KAFAbdBC7QqLAhFoBEd_fI_juO8hDjlAv8SFibaKUuC6b9lGtdnd7a4NyFm9sSu5_-DmiCv6V9sVBlpNN0LvRt22MEmw2iDi7hAGMOTN7OkYWTjUK9qCP6cExjDwPBK62-ktNxL5GXtOAUPBpWXmxZUXh8Xvhbr09iV7GNB3O2-Rk3snpbWXkMo-5JMyzOy2Hp4qy44gvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgam9WLYBVOZg9-YvSAUe-NAZxjRdw6p41mL1LS0CaiDXB81tZBEZEdqxyPZ3o5BIh1UtVFsX7sffNTWkQnZH4vQP7zzIXD8BTlghCuoNcO1pYA0PK6k8vQ_thUNlM2GR40Afeg6SE016NoOZ8X_VxReC4RoiMqz6bNRJ1abYxkuijAreVaUdVUOMh4MkpwOyEDrpgwWk6DTb24MnK8NWj3lsR8iJFNir-PmM54tIoJCWMNel9cpwSxAFrnMSaKvjDXjpcC0JTFI3p-MSDoj538NChn9yhBWVS7ELbRP1okpA22mDCxO8dUlpb8HlJzS1NmgsBPEbIF_40dk1eT_ow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcbMzOMEbDx54mua4qmfv8ic7avXN3-2nM8A91GagLbrJILDrFHONvQ9Zgu0ILzKHW5OxGRiOi7J6tMHb6wGFDPAEQdPOOg07iKKikMWDNoTO8HAuoVMi5sDott0iMFHPegmHcHrTyxhUnvDzjZNcLNoMelEbQyGktiX3jM9yuf5wbRWP_4gmlMIv1xhy00cQ8SzkFgl3VoVSuu4FL4Asy9LImypOyAQnT4_nxLyRbG9qgMS3nh8OvYWmOQVXKJSdjGIZrL45UCOwBZ3h1Me3q_g9ErPNmdi2L1dF7pAEWlTBL6ufA_cSZGtAk0kwH20JdltqiMxJoEHU9AGObAOPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBM4L0ZL2a7pcn8GRbOLnvuHYW7NLVR3q2_I0NogQHQzUAOQee6RLypi5GeSRZr2ybcmONtRJaTd4HgNnSiHhM8Tc6O0BrK2ZFVpZ-kt7S0lnG4EY_NwdbzfxkcRyZDhEG4R_X1sbyGDMBl3bCmKuq0a1zClSFamHxIJKkZk5CcNd-GJFTfRivRja2dMDS6P2aV2W5gOL0aRvfjaboh3XUIZgjH_7wuG4Xosp7RvafkUNHygmd0g-RzZQjEM6gf7kbVWXVIOUQk-5BMGYMQtA0G0-sSO0F-oso4P4qRfbLlFyV7se47fzJk0z8ecKifWn20DYIDnn2M3Ch_QNoSXgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k98grRaeJ2JVGCfjPiYpxK0stNMVWzhYT85sN3sQVz237nmLuxeha4eyXJZ-sLJr_NAp9l9WtRTHkEF3_njlAelRlzGazviYIw3Ku5_MQ3Cx1AkIrOedBF4qQqiL11PtmbdjyhKML-S8KKuCPoSh3bB1p56eAdFn3IUJo4OLUw5C8PSY_nsJ371sEoGVa4tTweRGcee0GorOVBAbR1PRT5NBoV_YTsybGVJZJFvUufxZFWLN13KSvH8D11VcFCpJg6NWPHWGIyq487CHY-mY9hFjXDJd-IboAcwSuVlvG48A2UAoq4ieazMtZYP_hs5FyCEr6TX0HVs3Q6kYDr8m3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEQBj8rpA7RfDSVcazDYsK9wiRA_b8VHq8EZfJI3ZMtCWWQ8vtX_oWgk43l5tqznOTJwW2KjkMk0qzBKO1a4DADu0QmCDcPVblORY9Cm8QGe-rhynHInYczRfRfInx2VKSgoTrQAeofMoheDvyT2tbT-UXky3MO6fqfFWUcpNW6sGCANB9GZRzjWDTWiQTR8b_XewOt6DR8XvHwvRj-wvWmfpEvPgrG-_UWA1BJOPHsKyj2APjfWOyQ7KGEYSCMohpelxttH6kLim6B_COpxTTx3nEu0pFfTPi_vdRACVEhoTudORsCrI6-V0HhNDRRSDfJ7gfgUbhmiSoryRKv6_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=ICYgpJFNgWoN-ngkUKqZsClaU5DKDp9CkN2aQhMo_ufHNGXh-DAvD8L6XLZvrXivEPlwMJSv7Qr5LNwRCSf_IsXkJ1mcQpnMu9vKacYmboOHBvLNMdfwGymVydyBJF07a8XVPCSyRS1MwRiRhTzMc_wHkCAKj4x_dvO0aZgoBzZABFJhtcribFVxN1xEKgKo-vgXS1tlXm0NsFqEi8mmpXwL2LAJd7tZud1DZX02hEA9E6r17VTYXaDXKuCs_oItMsLdNSNgVzneKknIXb7DgtVyWBs1tZY6hAcqlHqOxJ4yhtW1RZBXM0AyeBNG_EO2_nQHcxXrkDXrL176UFNcpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=ICYgpJFNgWoN-ngkUKqZsClaU5DKDp9CkN2aQhMo_ufHNGXh-DAvD8L6XLZvrXivEPlwMJSv7Qr5LNwRCSf_IsXkJ1mcQpnMu9vKacYmboOHBvLNMdfwGymVydyBJF07a8XVPCSyRS1MwRiRhTzMc_wHkCAKj4x_dvO0aZgoBzZABFJhtcribFVxN1xEKgKo-vgXS1tlXm0NsFqEi8mmpXwL2LAJd7tZud1DZX02hEA9E6r17VTYXaDXKuCs_oItMsLdNSNgVzneKknIXb7DgtVyWBs1tZY6hAcqlHqOxJ4yhtW1RZBXM0AyeBNG_EO2_nQHcxXrkDXrL176UFNcpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fmo0_W2SMon539er6GKl6gS8HOOJYNzBuqbx6xt_rbD4oIoesEaclM-hkEbWlj86fiROHqrxCNlgwVvgVdZN_IjAupkR-HdUAS3iBzTF_loLZDUz31b4zM4OxHFYCNvdYNMuM0g61eE_j8AO1lmN21O1dvtw-mDEZi1Clor4JYqxbdGrXSVNJK9pemPk0HxcOMhQ00qt4c45ci8FP9mPwU2-Digt5Md3q0ixwzPZgvhBC_YnBCoqSBEp9pZvq6rISYs4lF9jRSJFMSioJF9TNtj0t1vv0tnklSQI1cuW_vsfxm2lh2483d9KXt-Ns6tinVhrxLhYX5mhTqoJshKpwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJ6h-AIUKwxpp0WQFEFpHUVellGysVtXytXlmrnl_T-PBRKujRd6ITel6TRTNuJ8edAs0m3PQpMdV3INoBPOGn_mCGjJQrqYg7vKoLP0wFl5HQVBg6R5-Pvay-l7CMc_FSH-qaZT3D-284XBt6UmfOwLKyV8AET2DCCQGy0J-HjPRn7zF9LK4l84eNDflKIkkUILpDk8Zby-H4HHz-f_TcKGNwk1bw8y3xI2CbrgXU3TrRfsjuQoB8AbxxymQX6dx3rqUbNhpoKeE9eLjtE9krw3RNsglSbzihigtRREg7D04FsmHQ04KtZSrbK4sUNcGvWWmYdKH5KkIornkfObWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l34IPdLxUN7dT9f4gFDHdEw7WTUVvnq3TMX3rnk_cqKUXIc8HNoQsw6m-ECIiFKn6Oi6q8BO_Vdaz_hGmY4LMo_q71nuErtXw_QSZD1T6peCax2NLepBnJAPY3eMuixSPB0pIkLSpxGRaX700xMcfvU_RmoTNmU1xg4MvUufxAOpWHTBadfyRw6PScEHxikuwBIWOwdl54kkaUTSFtuWE3P6_gXNgY5equCBFliI58X2zk6t6tndk5c56VSRN6KT-MkETZ-SETmTAzKJbpDFGBNIXn_0JZs861_8iqCRFEchLmcmc_DyM-CWmTo6m0x6KlCDdJ9YZMcTzT7KnuJvWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaJPcUCiisncJ21bedMDoxUxSumi4kClAsDmF7CJ9BAx0ced7q1Uynq6vZkCmI8qg7MT720cXZlq7AL3TUJYQXyB6x5vtEPrw2LvCZI7VpUELWn07tMInog_uo9ZHHVOZX5BhoJQ5TYi-qaNJc_f-89mzo2VGhUd1A_SMRBHB3xOkqdk6JUGs-G92v4EyJHo-5hTeSX1I8-7kfqos7pIeXW1eQ44WmkiMuJWe1dr7QHBHBcrpVlKId6M23qbOh0ABXLkMD6SgxEQ1z0_9-jwy5psZdFaEGdarqwex7iYv_mIbmY5uBGSGk84XnYSLvKAx7bxwz_quZFKopGW05OwQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9kR6M44g3uDhdLD8bhq1UV0CnptJRX4_s-Zj4cmomCgcler60HroW84zBiDJVNqIxwr5drud8I4mMwZBTDvu2qKqSXrGcXHKDovmEuIkc0sgeBhIYNXUtD-30K1E2rgRNzLaAKKAjQayvoceSz_a4f1Ua2H8cti9DEoapq98nzzoQSys2gzF5M9tRr2c9Cq3QZ3wfff4WvbJGqs9zSPY15XWc-7GU-0fIdImjW1NQTIyWcocnc82CVCUZS41I3FZdtzHUqEMzH9dDcoNCIM5jyHRZ7xjQtg0f_IMoKxW8xr0gk4ESLvhe12AYgW697vrL1uLNGTh3QFPcNg36DcvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LS19HQKgmXzRdSvWdRaJN5t1tH2M5kEFS-Fg0Dvntb2dQtm5V4vgtG6SDoOcZSm1ltaALgRi7EKsUlZgEZbuJIAB5igmUx_LS2FniMv0UKDZHuGEHD1KU1UQCbFQZstejMMOclW4XKdt4kiDbUjhNYOATSwP_HmeV_4Fq1gtK-ZpSvij9Kg5uSDvyd1lrEdzy-3cqKxK2o-u6mSUkxk79AbqHMcM5d-Ilu_pCzsE_kzGmuvXVGwGuJrwl36MrPeuEbTHO5oS5p8FS29fDUXGXU8z6pqKXRB6EqgLsNFD-_-AGdfwcbjIlUfD0UFe8UdQNlnosO3qRHzfWO7ghXEvEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q81pf0SwsYGFcUiiAhH3AT1dI1kJwoYH7lg3yEkO1XOW9rHA2gV639hFY4al4QNvkLTNK1SSkbxDJtCVynjRDjdKG2r6P5ouHZ2kQ0s20-Lc8yzJ1-qIcbKEosxNNkCjFXOoisXqjQUMDQ6f5w1P9HlO-l-dJlcW6VB_OuJR65Tzs1Dgxwr36M1CnV9pdf5yM94xZ3YJgZZY92w3_TTHVy53maoNJclqBRVtQMt7xsLg9cgM0UD0w9jwa4yLfLU_NY4pEKC-hJ8zd3EZF36nOkEQXd8FeOvLJFAbDaK4TVNWT2D4XkZsdYJL_jCxxDDBL9D1FpJUtYLodmuzcCWCmg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=SsTjDjErbt1xm4bs51aUDszpBCjwWSs6ryUmOHZmdbYHZ4N_DZ_tRXs3nCd-LmE4sadUTD6HQQhKi6GhUIvLd4_Su4jMQmF6pxwBcpveOQhiUnb4CEJizTmfdlLwkplzFxhsuCUFTg-GtMDxwZg_TOP_n-soccRkkHrD-lWUaYhL6gXS70699MJ3GmYWsEv1xhWzDeEHQjK0zPrItkyr_r6JfhNgKE9HDgpgBFf36TCpJB05DD4-o6A50HgbDWf2Uc1IRy3RjDeQBN5BCNpaTDoBIsdfIOP_Ao38kkrNwpKsivxa0TKIaYcpEzqUUpeMr0oCj9QQteER9meUc_pi-rISLiKXut953PySFLVaWyJQbGRgKrQP7i_ZACIZ6GXuFxwegn-FM4WZMFtjbMeY1VnYwu-qIi0FAPINH7z-pRp_lm_3vjAg-Ntk14jHndZF--2nQWmvRQT-5enFBpt9zOUsR-mXWZMif0N0GKJ1mSpAnFZZ3lhD3oPNNA0kjuZn_mYDX6odm2dCvtt7LXMBh0xfEZsKyhaLcOYpLofF_Cg55yg-XBLkXzApeXsD7y02QlF6i6ki1QSGnXJVky5ke-gI5kgdoZx0Ym13cI22wo23E7z3-wKglU-XtH3t_EXtaEg7ZSCs_OeM0TAk8s0HFhWslQnFUAuzdC_SaAtyak8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=SsTjDjErbt1xm4bs51aUDszpBCjwWSs6ryUmOHZmdbYHZ4N_DZ_tRXs3nCd-LmE4sadUTD6HQQhKi6GhUIvLd4_Su4jMQmF6pxwBcpveOQhiUnb4CEJizTmfdlLwkplzFxhsuCUFTg-GtMDxwZg_TOP_n-soccRkkHrD-lWUaYhL6gXS70699MJ3GmYWsEv1xhWzDeEHQjK0zPrItkyr_r6JfhNgKE9HDgpgBFf36TCpJB05DD4-o6A50HgbDWf2Uc1IRy3RjDeQBN5BCNpaTDoBIsdfIOP_Ao38kkrNwpKsivxa0TKIaYcpEzqUUpeMr0oCj9QQteER9meUc_pi-rISLiKXut953PySFLVaWyJQbGRgKrQP7i_ZACIZ6GXuFxwegn-FM4WZMFtjbMeY1VnYwu-qIi0FAPINH7z-pRp_lm_3vjAg-Ntk14jHndZF--2nQWmvRQT-5enFBpt9zOUsR-mXWZMif0N0GKJ1mSpAnFZZ3lhD3oPNNA0kjuZn_mYDX6odm2dCvtt7LXMBh0xfEZsKyhaLcOYpLofF_Cg55yg-XBLkXzApeXsD7y02QlF6i6ki1QSGnXJVky5ke-gI5kgdoZx0Ym13cI22wo23E7z3-wKglU-XtH3t_EXtaEg7ZSCs_OeM0TAk8s0HFhWslQnFUAuzdC_SaAtyak8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=EGuBxeEPU2jaMlTjynxYsWCAE61jR1PpxnoyGqO1G5BKLxL_9bPbTzkNReX8X6RTqAZRmS36yK6cNNC2eNU0vxap45Elw0PHSR0Zqb0Zfb0j47L5U3zckrviGA3oxcv-_XhbtIkx4jMhALpGlMEbkWVmG2tBlON5BR-4z1leeGNw9iCUbwXCDcKfFDztJzdozN4ncy6QOeacKoGYvwy7lA98epVgkQLBT5chPvyjVI_epq2-oyOfenEzR8f34JsM22pC-0puGqvMHTZBl55-lKr2D_kmFh92gq7ycfMHJq8li8lXQnQYF_T2tCkHRfS2ZOlv8KBZOVnUPC7bYPYraA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=EGuBxeEPU2jaMlTjynxYsWCAE61jR1PpxnoyGqO1G5BKLxL_9bPbTzkNReX8X6RTqAZRmS36yK6cNNC2eNU0vxap45Elw0PHSR0Zqb0Zfb0j47L5U3zckrviGA3oxcv-_XhbtIkx4jMhALpGlMEbkWVmG2tBlON5BR-4z1leeGNw9iCUbwXCDcKfFDztJzdozN4ncy6QOeacKoGYvwy7lA98epVgkQLBT5chPvyjVI_epq2-oyOfenEzR8f34JsM22pC-0puGqvMHTZBl55-lKr2D_kmFh92gq7ycfMHJq8li8lXQnQYF_T2tCkHRfS2ZOlv8KBZOVnUPC7bYPYraA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v02lZhHqRB16Q5zlUKnvSSHBWbDJP3kIXzw-f1tXIzfpN1XmNOqmXgO7nOR7pUueqILjQQ42MonRwJs3-S_370KuFwzYcd22ViislfQmwXWCES_twht9ywaoT98RFL-oScYgLTISzUE4Mo3VZu6H4tYwgRamUfEWzZyKt8ED0065hVEvPlmLAbt7ONtxJF16fVgF3n8-jMNq7u21JFEnHvJj4GxMEjRZ3tWpb3F5ryoXif2_v9qKzD_eFoA0A0lIACO7cl1cchIlMeXStC5dz2WRu0S2pTTpZOfyOqJX_Akw9JnX2a9gdpurHZZDWQvZSFurcLZzhf13AmqZmwTTFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/So9XKp_oTk-YnNR95dOXpSZJlOEINuLyAARf7dl3a8nzBdhRp-v_eBUA4yoxTUUOwMguJLi0fUvOfKclx_ffksiYX73QcZpgE2RykTgOP44pZIu7dUf_OvcI4MgODiU5-COa4A0M3WnkwTOliyzZ-0fCnkXuZrjUcN5mFK4AmYKaulpyQkWXps6h7uKfrP3C51QUKuPScaOP-9ZvTEBlqcEewCzoAkk8CFvvHqSIGfzHBW8oDy1u2mg42bf6GZlC-XLxaqX46IICjGXAIjT1JlAPL5aRB9REufpITNKG9R549lvvoUaJcMdDxAMKGTENbOVna8zY-IA3NnEdK0FUBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=KOdg62XjeAyQqKo_gSfrGe5WbzO_08qyvrI8pWF81uCnPkwIjYGvjofpdLF5MK9AInTd7PNiZqY7ErtOLDraCAsM270Ey6qWkz7nuVLp-O-Zf45-qJVklJeN4v_ttzblqrfE2CqWaCD623BMUGYCJrdb-CAa5CmsQ2nbqWu60JVfBGr1e0IgETjTHaq3n_p8vpE0u2O8kHsrWvLWcT3PvUtWKbLf-VdBnSo8Lxvmkx8IcXGO89Kpr8WLIoSUOmHB6GbIra8ANz9bl6rXhzt8PtZpuHauO8yPcEy5No732mMfc5eixiZWR8xoUCDlkRxf_gZqFh0cPyEvbZWmNDKRdTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=KOdg62XjeAyQqKo_gSfrGe5WbzO_08qyvrI8pWF81uCnPkwIjYGvjofpdLF5MK9AInTd7PNiZqY7ErtOLDraCAsM270Ey6qWkz7nuVLp-O-Zf45-qJVklJeN4v_ttzblqrfE2CqWaCD623BMUGYCJrdb-CAa5CmsQ2nbqWu60JVfBGr1e0IgETjTHaq3n_p8vpE0u2O8kHsrWvLWcT3PvUtWKbLf-VdBnSo8Lxvmkx8IcXGO89Kpr8WLIoSUOmHB6GbIra8ANz9bl6rXhzt8PtZpuHauO8yPcEy5No732mMfc5eixiZWR8xoUCDlkRxf_gZqFh0cPyEvbZWmNDKRdTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0BXAwJKygOntYq6yq2hwJwAjSZQX1WTQV4zbgbrnobBTrKeR2drNZwqrDlMB7-PYNIhUbs-cjVzDzq6Kw6_EOVWoHQsHyuvkkWoD_LNq3sCzq7aVOBsV6-pRMb_BYQ9vl-lKP718lKc2BbwwOn48B0edc9NDF0nSAvhneLOJNaG_eH1lvqhLLQE03_hMqF5Q5qlGXXtCoIJc7NMACU8N8zSjrSSYssAIaQryi8hoDXddu5gvtiI0FShmLL7-mdXznTkDXk-tl_N9Q8T3QkkoE9umkExHk84y3zbuR587XzIAc-SzwwZkus8HqL8kjAMDAhVk85L4e435nDvnl-SKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5PCgF4hm575HgLbOUPah_wtwmoP9awOneuV2_jZ2_Djus3YQDVvy5U75WubCfrZIze-vJ0U2hcYeFQHOTtH7HZDjpa91CMPwJKNjfCpeiUpySd4y2aASHfijFLuBAZNNFYxkLSwaAVSFq8bHFyzsNkg9oFFRlAJ7IlmP7uyK0QjenmuMQ2w5DFRU6AiDdK4jzxdEy6agVdtx9AUzJvKlhJa788gAWKixgPywZA6jdImuMfj3wbn0eFq-60JpH9_r2n_nBH-nLvgGxMxgXMIMz1ybKvMziwLvEc0veFGy0LO2vbo0QG4XKRE6o6BdC87g5wWyv2ptqK0pXki4YcpBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUtS0KLiCRzUMSRJ1-eIlq6gJNB5EL6PLAxNO5IUTvYN34AGun-1a-vKIeu3iyp6oVUrvplCHcgxtDu7ubKQJyisVRzNAh0emTHTVfj3NfXrNkBMpUHFD28qvrJRAWF6g_vaL3aN1PywlZ2_bao7b4yaqIkEreMCbNI7An0uGnUdBJUOzGBug2LBsQ7uMLMxxRye0Fwa72OiIXJuEJVSbG2WTFM2lvWg5njQfgztDUpnQ50ZeSYCsSYNDbo-m65cA4RhLoGsHFdxIMOyiugclXwDxNh_giQyGyYYail4Jv7W9LdfXuVnDJGQCym7uhJWzAoRtAoiQiq2c0uUhh9z9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rScea5WoR1DXKsY5IokItMYvMi3SmdasKg_JylR4SDnjG0uMOxN7lbJ5PQUL76nc2sNkIFRW8QpRY7-afG1sMNFipiqbwS8RC-0HmueXlKg-AjseJxPWQExwRCz-lzWZmKkkS2wBiyv7LE8OSsM-1wJN8OToQ2Hx7GvdObOED2ZSzFiatgISJxNOpwAy1UzgnyNs5Owu6yTEQmLxsjAD4hqIXmn1qSc4bNcZRJOcFI2c-QK0FTfPHPHOoWA5EEIWI50Jt76nthh9jLnsr3Pr8TTxNQCLguMZIZnypEv3N3wu7t-hIBqpkIBlqE-C0qUCIO7H8sAVNlyNIDWmQ3mzdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qN7JNX5H1UmZPkX6ZJBJzKV1Klj0rMb7mI9uFbEx8fk-02jro5-xWNXgobFFIUbSNNClTiqcq4ubf9piEIG-C5fEvknt1aA4G9Qksj9G36YQbGD0Rb8uECp9L-h2NDZeWH0mVHJWHH39fKF0wLSJtE8VNO6QWVPTV31yfcMsnrd2tBTfqH4cQwOO_QCfj078fF80gXwNsQUhTBhF9BApXGIoBCUzsICSTK8bAc-TXPNetVQGehKra33JtZs7_hNc-oMoCiWYQzGdObV6b7mzA6imLXJLdhZ6EITdd3yhfdAku0fJY6u6VHFeFdBoOvmYSpiJqADrDguwcQZ-leoQWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5V96pqhUlnvxcR2JW9EEZ8V96NrKZ2mgYphTV1zbrF8T4G5gQzniPo2JBb6LkPO-BwiCgQDM3FQzTXcPfOgd60AnYExgSdEPJrVEYQYabypk-v5V59EW4Qegvn0Pcj9ijo1L8R_vjrqr1odhiZghOm0OXFmujNQl4bCenLYWZwXUSj2vjI1Vlk04YeNDVe9FS0lEU-5F2dRg5onLudg2OsaMa2MKZp7YUEM2uaUcG0dtIH64howhfR3vpkTtgDjEvAyNoZOmbo6sr88kH4RuBzuVME9EPhgEYyWGROWtj1o6PWNZpbWMGyb22TwTOxXAPMWU8FoMswQ1OKxe7qhGxGs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5V96pqhUlnvxcR2JW9EEZ8V96NrKZ2mgYphTV1zbrF8T4G5gQzniPo2JBb6LkPO-BwiCgQDM3FQzTXcPfOgd60AnYExgSdEPJrVEYQYabypk-v5V59EW4Qegvn0Pcj9ijo1L8R_vjrqr1odhiZghOm0OXFmujNQl4bCenLYWZwXUSj2vjI1Vlk04YeNDVe9FS0lEU-5F2dRg5onLudg2OsaMa2MKZp7YUEM2uaUcG0dtIH64howhfR3vpkTtgDjEvAyNoZOmbo6sr88kH4RuBzuVME9EPhgEYyWGROWtj1o6PWNZpbWMGyb22TwTOxXAPMWU8FoMswQ1OKxe7qhGxGs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=Qn53bru_WPhhI5_Lz1D-1w2rMGd5-_bShqfqRFSJtcJRMYm7mbd7CmMJOp7DUBvhbFtIQvKeKSfGZSCtGfJxplKLecIA0lHRLy9cjcyCIApZavN95Wx33J4itW7rI50W0ufpjfdfW6mIMifR87as7M629CA-hGjJEZmmK51tqpTJMAbRIPmfhh5TprEVHcZsVDQF4R8TjYNg3JlVdzj1SQaCNsHwgGv7hg3yA2-ThMYc6GDnVTDXozmeUFiCqEQ2v2oHPzRfkzxtQZdy8hbYfIXvkXqV2nmsJlEovPHt_TvPM9Rd4IOKjateYfrZvjm3QJOjGap05ZUlC5B0k9pRfxtRtqurAGIApEsIcmOQFXrczWuRdbT5WAHy9tWQ0JvH7rbZhHMOfNPavZsopABftIVtb1_H8lwuinwFzdiFXNHTHOMh9WAj01oxIbQSm4bYr2yWr6UPEI5Jb4MXn1XZPVPq2PkjDuO500jREY5Z65rme0Fp7oha57s3uzCTzP1ylY1w5wNK-8KOb1R5n8zLvylBDBqPnMObRiak90nZdx7TryU6lvxyjliXacC4lsWCsY_wmnFvHNtbszdhpu3ExuvS2Z9hDAPjrPmrve_6_kiRjpV_VMRSlSJzgkQGM1VikkZtaYvWTNiOyjDLIu11vXBY_dLlwg2hr0QlRSRPNjc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=Qn53bru_WPhhI5_Lz1D-1w2rMGd5-_bShqfqRFSJtcJRMYm7mbd7CmMJOp7DUBvhbFtIQvKeKSfGZSCtGfJxplKLecIA0lHRLy9cjcyCIApZavN95Wx33J4itW7rI50W0ufpjfdfW6mIMifR87as7M629CA-hGjJEZmmK51tqpTJMAbRIPmfhh5TprEVHcZsVDQF4R8TjYNg3JlVdzj1SQaCNsHwgGv7hg3yA2-ThMYc6GDnVTDXozmeUFiCqEQ2v2oHPzRfkzxtQZdy8hbYfIXvkXqV2nmsJlEovPHt_TvPM9Rd4IOKjateYfrZvjm3QJOjGap05ZUlC5B0k9pRfxtRtqurAGIApEsIcmOQFXrczWuRdbT5WAHy9tWQ0JvH7rbZhHMOfNPavZsopABftIVtb1_H8lwuinwFzdiFXNHTHOMh9WAj01oxIbQSm4bYr2yWr6UPEI5Jb4MXn1XZPVPq2PkjDuO500jREY5Z65rme0Fp7oha57s3uzCTzP1ylY1w5wNK-8KOb1R5n8zLvylBDBqPnMObRiak90nZdx7TryU6lvxyjliXacC4lsWCsY_wmnFvHNtbszdhpu3ExuvS2Z9hDAPjrPmrve_6_kiRjpV_VMRSlSJzgkQGM1VikkZtaYvWTNiOyjDLIu11vXBY_dLlwg2hr0QlRSRPNjc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=ksB9VE4B16Fz9LGdhbbsDhJtl7Vloc3br747f0S-A_KeZ2XwpI8Kn46pS_0iHA6KmWPqiQxHAR6gOzxUrkVA5_zToK1i6RHXZvkfnk8gIaKJUdN-Fl2JS5bekCsjJKdIGvI02eo7PoGwpEOgB1umpBaWpOssaSPhwhQmS0GmxP9oyvAjzjNiMLdHlOZ3WUu-_YXwbkKQIQFbUPsXhcy6ocJjgsgJmza8M5IyFka3y_zzFlcl-VrKLrFvWRG976e3xEnHNwtAEiuieSOZabAViNVfWYGXV80EF6FYhkaCIBIwyPbC1C8ym14l9WtTpmnrUgGr1wGQhmBk4Jwkp6qGxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=ksB9VE4B16Fz9LGdhbbsDhJtl7Vloc3br747f0S-A_KeZ2XwpI8Kn46pS_0iHA6KmWPqiQxHAR6gOzxUrkVA5_zToK1i6RHXZvkfnk8gIaKJUdN-Fl2JS5bekCsjJKdIGvI02eo7PoGwpEOgB1umpBaWpOssaSPhwhQmS0GmxP9oyvAjzjNiMLdHlOZ3WUu-_YXwbkKQIQFbUPsXhcy6ocJjgsgJmza8M5IyFka3y_zzFlcl-VrKLrFvWRG976e3xEnHNwtAEiuieSOZabAViNVfWYGXV80EF6FYhkaCIBIwyPbC1C8ym14l9WtTpmnrUgGr1wGQhmBk4Jwkp6qGxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpjgVIa0tV_mIsO5P3VWr7rdw5qqlXZIMyuCZXh4N40gW0F6DM5uG_AXsTJCMWaNl1TZFd6QVpBTvtQvTiKgPQjf5-hXpEf8XJD3tJbvtq4IBaufpBcLgcKJaUIvO0myV2d3mo7hXHRbckVRYxvH9MqBqjLIdvA6vWm63npCI6BYcbfc-gWz7MUAoe6-t3qeRsENiZdylPRuYNTAAcPSHYvGWjpid8QynBu9V_Jd16ClPMsMRRxcVYm0lAYVHl7uSWT6Y3awW6qEJfRzEdnXOXzk2Xyjf_ZAzbc63S7uUqT9NAyGU-w4LzLzCpPV5Acs8CX9vX5MYMtNVogCn6hUaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBBeWtBm6RYmRSCOIb7VENzOFzqMU8epue4xBPI5YGOxrBff_sgvob0Yd5_Ozz3uSGZDrXb3i7GWsgaJfIp6zBuyQUZYwwhclnUejcXq8EaUQuEdUGHs226QRDrz-lj-TULtl6J5vj88BqMF-ZCAv4CTpH6Xy5xscxe0HCUtNAD9520i79K4vIH7-bWNBfRlTb1UyHvxKNqSHP62Cz9q0ygSQ4ygmlA97gsJyw9vDcJBRdkq0EORlSIisxAerouBa85GxXtXT38Gpg8zC6UK30oOj5PtFCSuadO3414TbP90iUZZ8TmCwikyzqmPMfz_NypAeQ7SRDmx5TkkuBeU7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=qq_JNA4t8hXUW0owZQJu4icIs4hVU0ZkMlFbYUXsl5iO0lNTjzOGZyIiuhgq7UtoCxUImDD9_QBSYj7hZQrZE5SOOFq0fg-hwz5rBP-xzsrxw_NWXNy7RO-UWuOG3IxW_AdGCZoviVBHym9K4u5XVz8eyYCihrC1y_LAcX_XUCH1b7u0q1wtqF_w7sO4Hz0iPqU8CCLoiqxY1cfQFlESMH_QWG4mnPixdCYxwVuHR0_zg8pF--9o5i5laMkYgz3Ta-fVtaQ8QHUI2vYhCCFZiuEVWEEOVVyCyFG4iyDFNSOOYGv2tVoi76kks6Ahyq5a85rUWGDs7VDW-LguzSQyf5ZwX4XYThYdcUBc0ZqJJkyBP_p9G4LbXdlL15GTTqxUosjwAm38fdbxSCEe5VjPiN4uGTu1sbN1fOjbkfyKesm-Tzz_jMgjTS016cq_V0Hdiq6Ry9y_eZUXwvhmZaj1TbmuLpWXBKlDJtWw3P1ZoJBK89DY7cmNuxdlxGP9JFNbH_lo1TnpPtQrJZDS4eDVtI_w402qEe2G0oYemw2krINCRtFt3ZST20y9b185f6K5gApB6k7CPkcULY64AaqzWNeSSnEtRDj66H1rtAXkfX1LCznqQF2HoVDwqtWsVuN9zm3w02DRnmMBzkZmTQhdXTaDjLn9B6Te1JKfpL0Xft0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=qq_JNA4t8hXUW0owZQJu4icIs4hVU0ZkMlFbYUXsl5iO0lNTjzOGZyIiuhgq7UtoCxUImDD9_QBSYj7hZQrZE5SOOFq0fg-hwz5rBP-xzsrxw_NWXNy7RO-UWuOG3IxW_AdGCZoviVBHym9K4u5XVz8eyYCihrC1y_LAcX_XUCH1b7u0q1wtqF_w7sO4Hz0iPqU8CCLoiqxY1cfQFlESMH_QWG4mnPixdCYxwVuHR0_zg8pF--9o5i5laMkYgz3Ta-fVtaQ8QHUI2vYhCCFZiuEVWEEOVVyCyFG4iyDFNSOOYGv2tVoi76kks6Ahyq5a85rUWGDs7VDW-LguzSQyf5ZwX4XYThYdcUBc0ZqJJkyBP_p9G4LbXdlL15GTTqxUosjwAm38fdbxSCEe5VjPiN4uGTu1sbN1fOjbkfyKesm-Tzz_jMgjTS016cq_V0Hdiq6Ry9y_eZUXwvhmZaj1TbmuLpWXBKlDJtWw3P1ZoJBK89DY7cmNuxdlxGP9JFNbH_lo1TnpPtQrJZDS4eDVtI_w402qEe2G0oYemw2krINCRtFt3ZST20y9b185f6K5gApB6k7CPkcULY64AaqzWNeSSnEtRDj66H1rtAXkfX1LCznqQF2HoVDwqtWsVuN9zm3w02DRnmMBzkZmTQhdXTaDjLn9B6Te1JKfpL0Xft0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=Z2JCWS2z5H5FywVLXRZxlKHpx_mRCDfNQKQib9Av-m8JzibRA_fOZYN49cO8vtbPzP8ejBytapZ0vhUp1rDFf0IxU6TOT1j8Oe2Ni4DCRv2ViQNITe0m724OfCJfOoeQbxLhiH0tKycjwXGgsKN3QVBCHcPTmJRF5TTC90TX_MIybhY4Glfm57JlySq9FgEXViVOk6cJNL0PYFD_LcP8kptKj2g6Dih5e6VobSWMqN_Apn5Ufanyz3QbmeOXNb_0AXMrAdJKG81eQY5EE3dpPTws-1YNatmEcHTan426g-Gup5RJd0DvgpHVYz0QjQK-rY6dX21K84vNOqHZbi7DHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=Z2JCWS2z5H5FywVLXRZxlKHpx_mRCDfNQKQib9Av-m8JzibRA_fOZYN49cO8vtbPzP8ejBytapZ0vhUp1rDFf0IxU6TOT1j8Oe2Ni4DCRv2ViQNITe0m724OfCJfOoeQbxLhiH0tKycjwXGgsKN3QVBCHcPTmJRF5TTC90TX_MIybhY4Glfm57JlySq9FgEXViVOk6cJNL0PYFD_LcP8kptKj2g6Dih5e6VobSWMqN_Apn5Ufanyz3QbmeOXNb_0AXMrAdJKG81eQY5EE3dpPTws-1YNatmEcHTan426g-Gup5RJd0DvgpHVYz0QjQK-rY6dX21K84vNOqHZbi7DHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4QTdTULy9X7AjZUjUIYROv4C90Y3kdKjoya1cNTSEslUgSB58Pib_mOFuqLRvQtJGeMa3xedAb0C0RRCGANtteQ6ZtKcmjW8HaZhEshMKDxO0Ejz6kL9nUievF14fS7vwgnkSq5x3cFJE8JCVdE6khOEuDJBaoZ8YqZ184Qy-nTR1UytY4m1VlrD0XLgybLNcvIgQZ8EJitrta9Sg3OSlFmjuZ3jWILu2iU_C19nofvbXdBMy9fxHkY76qJEVMOP-V9R3l5QGTqoBRzYMweaMSuE7iBFDyZCdR4qVhzmkw9W6Xr5y5VjXEJMdUNKbsX3BHuPhNZaJCTZXCuFQvAlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TO_mV2ZbrWU7HzBlPtAQu5qind76jtzwyXX5bulQuk99aEZ9hE0tG1TXVFfMVWdh1P8chKGzcQae4OvqPFE3NFF7xkrkIkCHJbOwLEbKXUiTDftf3IkUx7h6KHFbChfCKAgL_fZmXb4LvNUiUKDxmcqWdy692pzqPtLlHeY_6IH5xre_TI4E0MHGRUXFxMGukFLae0LOwdhA2zzv_dJTKnRBAVpFa0oojTpjRoTqlWzKE0nGMZ6IKKomLx76sLYe2pXgFba2j3_NC9XaknA0IYi71zAV-YUiRJyN2niXRe5xoAIiNOSo0H_P1ljP0hWm4GzROd3VhJ36UjirLts14A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oUgljYHyViOX_ulWKr-ykztfFNZ-bACPmcKrBLbKmFwKeBAgKD9t4Vkl3U3GUOgERe3_zo8-AvXvVvac9kpzPzpU-70y6j-weJpYOZvQGgYD7jUS79QiKmK8dA7yyJlJun2h1QsROmEgwEr3IGMAxykz1_izqN1wwUTY2nbOsyakdoW8ohyV9g54UAKJH_Fyp67ttDOCQ29tjRA217ain8G8Mq0ckInfvcZtkdKnKymcGxFy-BFwPMgSk6SYnb05AX1NxIrutBrbvDCOa85fwfrxE9rR6nPeWWEjpVfX3FF2EWRw07eOe0ocKyMZvz0VH8ht2epbC64ofs92N9wQEw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=XPesqsE3-hxXMTzk2UyLy2q9lJCPSWjtPYTn2nY1189QBjKdqVSerrz47TfYwmlwZLEgw139r0rWfA8fl4_54JG6r1LfcaEGAavbCndAIxp0_c3h9t1v2hOT_pVW68KrrC4DybIJJ8PEw5MnhUSDAk_Af-HShQMHueH0qU39fpnvYUsEBchgf0ab9x0EdC54nLqeNp5bn2JILPmi9m21XV5UIE6cDksPgQwFAfohbcxCx6ohQPP2KI52cNJV6nSUSomkQomOJ20nEQfmh9E_iB6N4TjK-LJ87g_sjQxYBOfSQRulH7g7L-FDqpQYgDDUnuB_rdajpIon1ZqAPVWT8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=XPesqsE3-hxXMTzk2UyLy2q9lJCPSWjtPYTn2nY1189QBjKdqVSerrz47TfYwmlwZLEgw139r0rWfA8fl4_54JG6r1LfcaEGAavbCndAIxp0_c3h9t1v2hOT_pVW68KrrC4DybIJJ8PEw5MnhUSDAk_Af-HShQMHueH0qU39fpnvYUsEBchgf0ab9x0EdC54nLqeNp5bn2JILPmi9m21XV5UIE6cDksPgQwFAfohbcxCx6ohQPP2KI52cNJV6nSUSomkQomOJ20nEQfmh9E_iB6N4TjK-LJ87g_sjQxYBOfSQRulH7g7L-FDqpQYgDDUnuB_rdajpIon1ZqAPVWT8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=gopJg1cHD18pVQlyLrj_g_equoW0isLytoIB3HjbPlE5h-kPu4GSFQ89iq3_Jlhsb_7nm8gZ4GnxLDKhabbnhqyr9wRWfrRNtMDgq7PVlxamVGkmdMwMxX18xKZsg6bKiSYyLo92KroqoEj-ltR8w79eBRhCeAcFWbC9WyYzWhiBjCyM1Kb8WxPP8r2Obqo-8ceH-OyKjh-0yUBqgEfCa4rfCwCA5HoS4hj6ORWlWP9RJViltDxdMaWc_FB1a6RsUtRmtwMeFcZM7LoIBL3jlCRGjsrfejD59pWuBPMuAIomKqx9bMdifGmUD0ze4DKlkJ0KfltN_ahCNlpgoG7oAIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=gopJg1cHD18pVQlyLrj_g_equoW0isLytoIB3HjbPlE5h-kPu4GSFQ89iq3_Jlhsb_7nm8gZ4GnxLDKhabbnhqyr9wRWfrRNtMDgq7PVlxamVGkmdMwMxX18xKZsg6bKiSYyLo92KroqoEj-ltR8w79eBRhCeAcFWbC9WyYzWhiBjCyM1Kb8WxPP8r2Obqo-8ceH-OyKjh-0yUBqgEfCa4rfCwCA5HoS4hj6ORWlWP9RJViltDxdMaWc_FB1a6RsUtRmtwMeFcZM7LoIBL3jlCRGjsrfejD59pWuBPMuAIomKqx9bMdifGmUD0ze4DKlkJ0KfltN_ahCNlpgoG7oAIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6ijkSktZDOte2L8OwB3HXi0qIvRmBgT9mt8jUZUjphC24k23Ia67d16e81BR5hGK6j8qki6RalLc0SvyF4jgZkxBEgMeqQsaUXJY_pF5T6_Hq8M0wBOL5uQ5-ava6v3Npr1cpHEVe4Uh2LD2oYNpkg47JI-ue2C96c0nONkEwYNk8I_Gz-46cYd_Vv_OZOOSztwNUaSFfs4rVkIJ-lzH5bFQQaclgzi4LiKmGvP726y2lZcWmr199qOooaA0oeuwCPMvXnsRyNfzMyES3MFiCbzhY9SJX-9O0AX26ggkzUHpfTbA9QTP5O1JJ3HhjmP6Fb1tfWQbS1PA6KowG0ovA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKUv2-JnmhfBBmKBHpPQw8HVzmhVF5fpN6U1ag2OjqpvhFJN44dcZ4-lUanLYinnN9o4d4JZIz6J1xkBkWkXojR_svZ-3bFZhYLr8nv84_BvqDLgwWzy3j_ZWvaiIkXVfPeX183l6ow7KMQP12bLOS-IOrIb35GAz98Pd_YXRkOPXbGSEqcSFsUrm2o6MNJyAwQuyGSW2kCbGmNDyDCq9Wf-hK6hhpSMlHCY21cDIH83U7E2t5w4tm7F3Uv5p2pfwi0eMDy9-Ut-e4VdowT5uDvGxUZjdeuCQ6hi-0vx7K4-gMS4FMoulEr3OTDq2aMdTQlbhFsqdVyHlWAdnSTQCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=PyxiqBeDOxX9ObI3k8cntbwD8hJvGo4B_vlV1kRwXOQPF8pocQpHxuVsnnIz9x1lpiRdKNqakUgkViHvCEeFUKVHEl4ow0m-mDjHnr-EFfv_-IP5J_tvqyGfgknEn2ttwCK6pxaH9DLLiTuJjbtM3aP_2axqoiufJj_tjpMGTF8Sifr5EiyAgddBWD5kOEqDv7qWhw63dW-hzzjSw4eAQCxsv3Cy5zRz06qn-pQnh1zSPpwsWAy1m4ol-qckwRNUC7Xi-Lxb844jnQ61HT5SM0npJN-4AfgkjlNQ3PYWuWq54rhz8D6yA4RLyMlPNlCLj0riCC3n_usXDqSSYmmbMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=PyxiqBeDOxX9ObI3k8cntbwD8hJvGo4B_vlV1kRwXOQPF8pocQpHxuVsnnIz9x1lpiRdKNqakUgkViHvCEeFUKVHEl4ow0m-mDjHnr-EFfv_-IP5J_tvqyGfgknEn2ttwCK6pxaH9DLLiTuJjbtM3aP_2axqoiufJj_tjpMGTF8Sifr5EiyAgddBWD5kOEqDv7qWhw63dW-hzzjSw4eAQCxsv3Cy5zRz06qn-pQnh1zSPpwsWAy1m4ol-qckwRNUC7Xi-Lxb844jnQ61HT5SM0npJN-4AfgkjlNQ3PYWuWq54rhz8D6yA4RLyMlPNlCLj0riCC3n_usXDqSSYmmbMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9VlLfrNnUCybCSWuWgezyqPejh_Wveia7jS9lwFG4-22CEEpB9q77pZhJVT_91GJvY0BHnZ4MkG5sxF16BmmLsj5TzFW6roXIAzefHo5jnyeJYFRvegJ793NxGnfdUJY1F5YiLk32nxP0hUgsl6ijPweu2FhtMjzutDJO35hISkKbsm_fPPW8I0CG8M1v5CTT7mM1FSA84PLiOGdWyeSSMyHFPprX4jGkRWfKNcnkaiN8IwI0lECoV7UiVDLAcfzD8a33PKCiauG4LusHkXERaMUnNXfFOyvPiqkycwHkZsEBlqOcoEYNJFoVefQFeAvXMf957hRlwyS48jvq3bvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gseUUl55y8g_l5LTRlxz7HRWy1iQLMmWgtVbCNGBmrQsjRzF4wMISwbBAncUI5m7rb7Wsk6lEPc0kHG8iFyk10B6iVNqzlMfkgFkRBWPQBYBUBJQKAsC9LzElXLf6RhC-xHW4EfkakNHr2M86Xrs6PvnFsmuNF910cL3JfzK0EIJJdbV8cu59vMem5Rqw5RsaORkrg_-Sm4RNtWHqhLtUYa9I3spDZcvCOeBAnHWt4obT8SmscLi-br5iB7aMfW_IKtQRKm_HYLB_LhaCvSslEYgs63ouyNIVloslZjznkOc1T4wNfLw5cKW_AwOLMxbwOsypfov9RT72tq2R5AppQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P51v2blwS6gF3Dq5f0bPVbcmCr_pHmTEdd-4Pq60hf-6l86P2IbalVT2tJC3Ci_qNrlrsJ2WkaojirzYRXWobQ3NJIM0g-HrlYa6Nq67vSmZ5-sfr700ZpCZWzNo3ekBBdVKch8VlBJg2yTPbWD1JIr8JYuJES9zuXt0I9L5y-vYMIFa_rOeZ1aRoUEXkklRakCZAgFByA3CZDh-fJ5-epmafWfX-Q4NzHJqPyMbWxM6GW0fc65L2rD7H4wtBVWBGlx6fCZWxhDKd-BjHsfhQ3y4yz_ImcFI5J7v-MLrrJMkXPskfz1xxaPvgz8ixY617bQTVWzqIB5DnI0-bSyoLA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLSWBoMpeU9WEEtsyYXTmaD3QHFg3x2wsmpXNvaeAqM2dIdb5kJtFHfCPD2TfSsEmYhUhTv_Je16B9G2wnaJabMTgALWayFQjC27ysnrUbcRlhzkekpuLh4PxK0YtMIrZM2jvN1QxKPwtQWZidgpr827KBPyNa5OdJwLyqoapSOZz9cd-JBR3MH7kXZ2zvfFdsdgXjaQzexSPtVO8QTEMKn6oiYuWYmmco5LgFxQfsM3gDSPYhrYumQhmock4NxmoYM3vufKZtgKZcsaD5hEJr_U2SM5Kpu4nuleGcPi8-A4cr0kfUqGFBj9PD9k2on4G-JqveMXZKbJw5GR-YmTnTPE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLSWBoMpeU9WEEtsyYXTmaD3QHFg3x2wsmpXNvaeAqM2dIdb5kJtFHfCPD2TfSsEmYhUhTv_Je16B9G2wnaJabMTgALWayFQjC27ysnrUbcRlhzkekpuLh4PxK0YtMIrZM2jvN1QxKPwtQWZidgpr827KBPyNa5OdJwLyqoapSOZz9cd-JBR3MH7kXZ2zvfFdsdgXjaQzexSPtVO8QTEMKn6oiYuWYmmco5LgFxQfsM3gDSPYhrYumQhmock4NxmoYM3vufKZtgKZcsaD5hEJr_U2SM5Kpu4nuleGcPi8-A4cr0kfUqGFBj9PD9k2on4G-JqveMXZKbJw5GR-YmTnTPE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XfQTm21Kajm1wjB1AYSZqR36f680UOveVJC5nEaAkJQuh8oK8G40almWpbuwdIGbeky_BrweOeke5gUSaKyHpwAJDfqpxa02QvAELPuxGcmser9mU1w0JxHgI3QbX6nsB8U22uLpAUAbRk1NddvG5eZyFmbfeeI66bMZI_uOTPsPkgHjEivkFAl9_LZr3DkHCJsyMO8NeCAYK_CwOnjHrvQUD_lsTMU10nWz_p6fHYgK6UwSPzyP-_kpc8SzR0SXLrDT1zB8LDWrPFqfdWRReh9VN1Q5vzWIxCfPJLOfAJ7b3gB1wDVpPweUpuOrig_iKGgHQC5j4h9sG82ZiX7o_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ilZePW_PTrGXhvr-2AoTHVMtd4B9UWfybQsWJe40ROClJ0DQTDWhSqODk16SwCewgKPnLsvPvrrdbfG2GNK0LUVKCMayLsaSEtNMr-qFnNVEQwItUhc6ng9--RnL2B3yY9KtpScm1iJKpQuREmDbTeBSgQk6iLRYkF36-pMQVRcwVwwEE2wgykiB5y-K4BGjSFtCbtlLJ62J-MZ3hgnAEsGBSQmE81KW-NrojaLyga1prCrGQ2rIfk3_DPT3JwZy207SEc_bLzIg01htZtIIbhg9h4Hh5n78XFjtDIY9GkQyqenlO-sd0NXpoFiwaDNKLbGaAHyvJVPWekSySvQTdw.jpg" alt="photo" loading="lazy"/></div>
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
