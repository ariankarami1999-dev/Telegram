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
<img src="https://cdn4.telesco.pe/file/OmnSSnxanoCXCxHJckNwsPtokqW-sErO63vLTsE7iUJHcjh_x8CWZ7lqy8f-gmdUANYH0KEJsmXrM9vS2H3eIHvUruRnhVpWsbiglnCnCdlnOvOKn14kJ902aRBg_Ht3dNXuBY4hzjRlI6UAzfKGbnAMUuRk7VlcoN2rXHZv1CUBwzluD2tU4tlbp7zQFNniYy_6YCINDjH-ZTOfr2DtCvyULJ4dJfxUPHqf0PeBHyqZry3o6tCqCpUPToR1DFp-e0R6qpiUNQTwngh2nfU_i0EZVADl36EHeFOC3b_tsrw2EU58js78A1qSKgznmf-LqsemhfzobkIsRfYhdoauzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.5M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 17:36:46</div>
<hr>

<div class="tg-post" id="msg-660425">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
گروه‌ تروریستی داعش در بیانیه‌ای سوء قصد به جان رئیس کاخ دادگستری در حومه دمشق را که به قطع شدن یکی از پاهای او منجر شد، بر عهده گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/660425" target="_blank">📅 17:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660424">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00d77ad613.mp4?token=GSqcwVE_10Jecf-lRtA8FgtwBHbvuqoTRPa8RZbnGhU1ms6MQDEE3DAPJP7k2C914ZGH1k-U_9c57r6D9W2rTaY4KlBlCY-BHRjFQTmT5ayR-OJa00PAfLM91hPTJ6vtjlHpE9bRwQqT5l9aEGJu5UUdn22FPnh7p4oG7AiitMAb-EpXlJpDWv2ONZIg9VX2ER4qH5UdAfRLRsvlo6zVVY2OpH59zUCgij4x4rNqFicTbWi1jphnsh3qJ6xSR3q4wttPW2mnwg9GlZgdFCUcv4l-II7exLd8SJbhVqnMxg6wBGH_T3rZSEFjG0jOJHjcYoOE_1CkOl1_h8fNjd96ezzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00d77ad613.mp4?token=GSqcwVE_10Jecf-lRtA8FgtwBHbvuqoTRPa8RZbnGhU1ms6MQDEE3DAPJP7k2C914ZGH1k-U_9c57r6D9W2rTaY4KlBlCY-BHRjFQTmT5ayR-OJa00PAfLM91hPTJ6vtjlHpE9bRwQqT5l9aEGJu5UUdn22FPnh7p4oG7AiitMAb-EpXlJpDWv2ONZIg9VX2ER4qH5UdAfRLRsvlo6zVVY2OpH59zUCgij4x4rNqFicTbWi1jphnsh3qJ6xSR3q4wttPW2mnwg9GlZgdFCUcv4l-II7exLd8SJbhVqnMxg6wBGH_T3rZSEFjG0jOJHjcYoOE_1CkOl1_h8fNjd96ezzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشویق وایکینگی هواداران نروژ در شبکه‌های اجتماعی بین‌الملل ترند شد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/akhbarefori/660424" target="_blank">📅 17:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660423">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgFnjeXet62I8FmnrscYzAfaMcXjTEgp_gQt61HRR3wbrhqXbUVh_NE4JEVlixXfq60OqkiudyMTiNYglNhf--oyydiFa4w9-S7c6lK51fPnzVjZShYmztcY9VWFtcg4emsfJXH-g9OQs7atwXzBjLaZLg_Bddgr7vtw_d4mqvfVcEaWp65X9wfwmS-bY7xq1s47_bqBAmegQ4ey89tC5vO8pTa4Lw76Yu3Qm_9c9JWdnE3A3_0Wi3Y61P0EPGyCbWGgQpEXRe2oLPOHjREvKYiPlqhhzhoLV71i6e8m2o2tDot6LDxKrw9Hz4AzAB6G0yBgkbtXPzCR4zWOL2Q3Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه وال‌استریت‌ژورنال از دارایی‌های مسدود شده ایران
🔹
بیش از ۱۰۰ میلیارد دلار از دارایی‌های ایران همچنان در کشورهای مختلف مسدود است.
🔹
طبق گزارش وال‌استریت ژورنال، بزرگ‌ترین بخش این منابع در چین و قطر (هر کدام ۲۰ تا ۵۰ میلیارد دلار) قرار دارد.
🔹
پس از آن عراق با ۱۵ میلیارد دلار، هند و کره جنوبی با ۷ میلیارد دلار، ژاپن با ۳ میلیارد دلار و آمریکا با ۲ میلیارد دلار قرار می‌گیرند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/akhbarefori/660423" target="_blank">📅 17:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660422">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
عراقچی: مسئولیت حسن اجرای مفاد تفاهم بر عهده آمریکاست
🔹
وزیر خارجه کشور در گفتگوی تلفنی با وزیر خارجه چین ضمن تشریح جزئیات این تفاهم‌نامه، بر گسترش همکاری‌های ایران و چین به‌ویژه در حوزه انرژی و اقتصاد تأکید کرد.
🔹
وانگ یی نیز با استقبال از این تفاهم‌نامه، بر اجرای دقیق آن تأکید و آمادگی پکن را برای تسهیل اجرای توافق و تقویت همکاری‌های منطقه‌ای اعلام کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/akhbarefori/660422" target="_blank">📅 17:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660421">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
پلمب کلینیک بیمارفروش در سعادت‌آباد تهران
🔹
کلینیک زیبایی «م» در سعادت‌آباد تهران به‌دلیل تخلفات گسترده با حکم قضایی پلمب شد.
🔹
بر اساس گزارش‌ها، برخی جراحی‌ها در این مرکز توسط افراد فاقد صلاحیت انجام می‌شد و «بیمارفروشی» به سایر کلینیک‌ها یکی از منابع درآمد آن بوده است.
🔹
همچنین ادعا شده تعدادی از مراجعان پس از جراحی در مراکز دیگر جان خود را از دست داده‌اند.
🔹
این کلینیک با پرداخت مبالغ کلان به برخی سلبریتی‌ها، تبلیغات گمراه‌کننده انجام می‌داد و مدیران آن متهم به تهدید شاکیان و خانواده قربانیان هستند.
🔹
صفحات داخلی و سامانه‌های پیامکی این مرکز نیز مسدود شده است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/akhbarefori/660421" target="_blank">📅 17:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660414">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vGCLZ4Cx2ubK_OMwWG9Bgr3eHqL54kOZm6b4q0VpbPZ_oUUrgsdWLbyljBO3QqtNsDUJY7WcUSNYSVkD9FoUjJ88NetRcoaPSUIe7YhcmK5TgUmP7elKftsYdAQrECTY2cNRCkeAMQg_dumrnT8MivUzV29ifjpD8HmJ2BiwA_YqPXI_ZTlFknEE208ojh-dJHne7HgDDLVYs6tTK90pwwCGbuACITJO4943OQRY0xH5YfGihZR2p8a36IAKXmk6eSQ-LcG2hmTmfT0w9IDKolHi_tI7Q9eGDHSFwSCX7RVLkHGt2O5RDhk_UTrB5W-X-Kar1MLmeHp93hh6Va4jBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iso-Z1hoUEfsrJ4ISvbfnATpeldJrkwwY8Nc4LaSXMXce6SgO4MXcAXilDAdaIq-LRRgdmP0zzIAxBJQZhDJ0L_Yduw_i66fy5azlyxwAyuKA4Qr1G5LN92RxDrztHYpr4P0Ad-0a1JAfSpaPBNyCMu-_tjI9H-JNPbrYR1fkiJISrkgqQf5dAggXynPimn0YWoIn69s67HIj7WVZNK33C9kMEnwKO6X-5S8Y_7tI2xIkZJdT4Srw6F9kWvtotwKsW16-Ei3ylDxiPCeU_XX6ijNeX7663moQPUEuWbc_c7I3jMyO5MuyW803ED3IbTt87L2cjJ_sUmiSjEQDPJEZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hjt8_NAhQBXxHzUQF1Yvq8hxVYw1mCjRvO-no0ar9toJTF8EWr3o8r4x70DNBMzGXqqy0fp7I3NV-rTbmURgvceU5m_DdovvlcECqvzkLRSKzvMNYAFa46YDBX44GhxYNoZwOdXGk12mbr5d7lymJthU3WigZn_YiCeh7fz8LlbH4hajjdpAMr9aAtf0ALF1s72YqDX9gMQmJKaQfgm88dueipO5KSZsNnQOnktAiys9DLlCDnskjGV87LmW7MLYerUeBd6Qg6_vZRqlumiEOIy_t-Jg-QGbmlwdEJ_dJupbOKIzNGkPSkB8AZIkpausH-Ll1_0HhgrGwBVV6mEndQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bv0bOIN4ZR7AwsIIssOtQ8oeOfmSBKbC3JbDssp4Y73A02JH3AKXjUYdkytW4AMDATSSZZvcnDMcxdcLwrGbqABwyN41JC1Skmd5lfFVFrW_13GFuawSoI8YlnB-j1tjQg9xF_z7KSCUuj-ssZP51PakZLf3eUv1s5HLvIApqY8FMQsKUHSLJO3WeHnVObwLp32T9ZKPjpeTpfzxiLinJ2ZOq3mDIkLT5kr0DXFmswwhoLlTTtdmCVvk_g2BuCaCO1WGRqa8QDTJ2sIwDswhVJ-z0_mtrqVGSxbHt-uaeWUzi7ltYIpQB5uat4m5NqAeaSAv1PpkzqzZoFTCnPv1rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MI3S7uzvTNmJgl7Tll8miXx8hB8gIs4AWgWPGcnA4xQ06cxm9drAOCop8343u8odo6-Qm36dkRS9EpDdwvkPXJXUMnck8CLFpPwcbEs1QPo6XhyNLiV6kEBYL0fQa3EnimoGeofX2odjPd0PEdo--ToJkF9Q-voRMgGbFdPCA8Y32OtuvgVdJnNU5rj8L0oTDAYtYuq0ATS1yZLwlpETAxiojgA7tKo5NR2kVbJG3uT51zARZNs-OGEpOyhaZ45R-xl_jaLB0ZPALt9HddsOZ5O1UB5y722gBGj89OZrXCoJWwnh3zoWIn7nIdRBqc5btkU9SDr3teTcYLV6-3DfwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ARzfyZEIPu8-W6NQkrbQUF7LS3j90eqVXkNbybnvakHmE3IZ5WNePf90yRdsriWCDanE_8Uq1yZ8hd5lPHDU-wQxMF4DaDGWyvpPF-bVNxqNK7menmFprsdjPBlZ9nk5niKvj93oMfXgPO07Bu6Vv2mOpIY_tNkU3uQTiMvwBEjb7Hqcm_8swSRccwqCnqGdgnBVtvWLHQ0OTQiRsW3yUJQkgXemHAmQ8sU3F5eJeHICplFNHWUOXUQTlI6U-lXCL0jVCEkJdCLFJDhUtxsO6qDXmJZBv4m9T31HuKyVUXmdz5NOkd0DJzkvUQJYJCjm3wP70y7cuNj05fyhzuQrVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WqGMW5gG41knU0bFJzTu1g4MUspDKdZJajVBXaVqEfqul7EU8jgjmv4Hc0CaBxuDjO6YxT3P0MU3-vhJGXHSkUo9Z-HqwPuv05MdEVDobxZR3M66x-JahWBWkHRa3RQPFjtzyS6spLgp5ymDnLS9JJ_YXpwf7Ua4NeB-G_oKqrXkZm590kmZVel_RX8-mPMaKpx_FrEVbC8V1oZuXXel0E9aJh3eYpNijoeBUkZLhVph5BeZppuDiShcvouTZhoJHu1btW7nXLF_idOOik1mf88to-WrM-D5bk6XaBcdJCws85cr71btQ1ozdJ2q9MJI7ZqhRPyD6jP0KzrvvX6JVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
۶ دستور قهوه سرد محبوب
🧋
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/akhbarefori/660414" target="_blank">📅 17:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660413">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gghmw8zWYaPWiM-RBSZpEwc0eln7AXFYaSUvmkxAD3Rc1IyjBvOH6fHkTBwnsCfZN1iyUNasTSleyRTS7kibve3f3djqillPEmxrPJ11BA4XjY9ROO3buVj2sWvL1ij_i-5B2L5zgkbqcSflk2RvBJBVRlg4TYZAHse5ZvEmNAAZ24v8fciZcAMLOptG0fUFI7dRcnYvNWBYceTbLb8YDPRXMUekttrydyL6A_wn0qZDkVErY-gxABhYQk_yMsVIkqrGB4uCm9TgfoFSkwt1ttNs29S_BG-pQz1FuxAhmc9H8L3id9a_I9v7T1ayKKVHm1D5HyIgKZpo0Js8QhMtGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/akhbarefori/660413" target="_blank">📅 17:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660411">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296d273d86.mp4?token=iBBzsPSqrR4dvDskayT0fsEiVajXQPhlaXw3wNJ5DBQt4RixMDhN7QH23Z1UYU9tfYzlJKoTVY_i6tGyRdaE7hKwN-4Hmy8EC6VS5IX3z-EOFg3vukA7S5GHvAnDb-O4V7BYKSeJLpcmxhTb_YKu1pP8xJIuM18RSXRXLzVF99tn-ORJWQ8Mf8S0aR8sM3mnjr75CBD3_o-VooGTQXmES9io_py4QcZU6HAosRw6TSxtb_raP5cXigjCL25QFoBnu5yDrKR8f5mK7dz5zs9PWoHD8nansddTTCkSkNXwyRHf3cvrnMoSJey_-DF5xs_TPjO4771N0USVqntmKAwy3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296d273d86.mp4?token=iBBzsPSqrR4dvDskayT0fsEiVajXQPhlaXw3wNJ5DBQt4RixMDhN7QH23Z1UYU9tfYzlJKoTVY_i6tGyRdaE7hKwN-4Hmy8EC6VS5IX3z-EOFg3vukA7S5GHvAnDb-O4V7BYKSeJLpcmxhTb_YKu1pP8xJIuM18RSXRXLzVF99tn-ORJWQ8Mf8S0aR8sM3mnjr75CBD3_o-VooGTQXmES9io_py4QcZU6HAosRw6TSxtb_raP5cXigjCL25QFoBnu5yDrKR8f5mK7dz5zs9PWoHD8nansddTTCkSkNXwyRHf3cvrnMoSJey_-DF5xs_TPjO4771N0USVqntmKAwy3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش رحمت الهی در دومین روز از ماه محرم در حرم مطهر امام رضا علیه السلام
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/akhbarefori/660411" target="_blank">📅 17:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660410">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHUZfy54yiH2s2NvyjP0jNXKfz3j4M679YfPnKqvX3X1dH0yHfhpabvsGcTs059TIQqkEuBLgyaHys3CwDVw7OhVohlNBn81Hhs-5Gm76UmEOCNe_5GeYCyyZTFFL5LnUykPyy5iPItjhJjsn9qKFKThxDfBmyLqrkvNvXDjdSq3VHGJmmt7GXn5gcuGZ-mw5efaU_kkryByfY625ZoS-Ey4Qw5U5jgc7DLtxgw60LzWRnEhJ2AIOJAQa1feOwPjNyXuKFTlMiUMM6rgykmiLTc3PcHfftU7KNGe0Pbga7rDGDsMjqatkWudC8yAlninckxdLEgAXGYvGxpvLZMi7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت سقط جنین یک مادر باردار در پی صدای جنگنده‌ها
یک پزشک متخصص زنان و زایمان:
🔹
در جریان موشک‌باران دشمن متجاوز، مادری باردار به دلیل صدای جنگنده‌ها ابتدا دچار خونریزی شد و سپس جنین شش‌ماهه خود را از دست داد؛ این زن پس از ۱۲ سال فرصت مادر شدن پیدا کرده بود و پس از سقط جنین در بخش بیمارستان فریاد می‌زد: «ترامپ قاتل بچه منه.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/660410" target="_blank">📅 16:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660409">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
جزئیات پیش‌نویس ۱۴ ماده‌ای تفاهم ایران و آمریکا منتشر شد  منبعی نزدیک به تیم مذاکره‌کننده ایرانی:
🔹
بر اساس این پیش‌نویس، توقف دائمی و فوری جنگ در همه جبهه‌ها از جمله لبنان، تعهد آمریکا به عدم مداخله در امور داخلی ایران و احترام به حاکمیت جمهوری اسلامی و…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/660409" target="_blank">📅 16:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660408">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rENVW30R_okobhox1PwM-IatLFOKakWASM6IXf6wXyqcnpflC81bNyx1ntrAAUPNnLOZyKj3cyU8AW5dePfUtFykitbhIE2j70Tvi1kC5akDWyrKWUgthvJ6Q3JqPnfFz306HJVk8aQWXn-FzkMLyrHgn5ltcoOMfK-NM_Dpyvih5e0VE_1Aj4Wg0JbXp64whccH9mohwLSHPZFiUfGNxscGVHp8xgBvDGmWgDeISvhd9QEEwXOK4Ak0j7_yerQOBtYn3yN0XOXlSuYKr-O3jL4_PCfdRtMCotfWNhn6aJK9teCTxy5SkA2MZhnKhR6a4eIXbnbPxAfl_tX0u1wjag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت جدید کارخانه ای محصولات ایران‌خودرو
🔹
لیست قیمت جدید کارخانه‌ای محصولات ایران خودرو ویژه نیمه دوم خرداد ماه ۱۴۰۵ از سوی این شرکت اطلاع رسانی شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/660408" target="_blank">📅 16:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660407">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
صندوق‌های تامین اجتماعی ادغام می‌شوند
اسماعیلی، عضو کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
یکی از دلایل اصلی طرح ادغام صندوق‌های بازنشستگی، تفاوت عملکرد صندوق‌های مختلف و سردرگمی و مشکلات ایجاد شده برای اعضای آن‌ها است. در مورد ادغام صندوق‌ها در فقط یک کلیتی بیان کرده‌اند و کمیسیون هنوز به جمع‌بندی نرسیده است.
🔹
کمیسیون اجتماعی با این طرح موافق است و یکنواختی در اقدامات و صرفه‌جویی در هزینه‌ها از مزایای طرح یکنواخت شدن صندوق‌ها است و شرایط جنگی عامل تاخیر در تصمیم کمیسیون است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/660407" target="_blank">📅 16:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660406">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
ادعای جی‌دی ونس: متن یادداشت تفاهم با ایران حداکثر تا جمعه آینده منتشر می‌شود‌‌
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/660406" target="_blank">📅 16:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660405">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a08cf29fe6.mp4?token=b56nhlyO75Aq-S1wMK7uLY5_Z5pTMiz6vJoAzKeLqSn3LwZ00e9MA6zuigLJ97m91_O0hhJ8y0BuQ2qeX8W8Cs9p1FhLkpH7vXkvOlmaO6yk-Kx9GMjvRMwPppgxh7dmptdh3XvO8YkNorq9l-q-640kylwmla4smqMHmJjwMi6VhPcRutx8gYGfWuspJd8UvC-50C-U7yFwwRz69MqcDwnB6DexHyMzphRIjY63Zu63vzM1fuq2GltP3_03ombt-ZBRFXwK8Dxhrv3DarzvCQf0Q537wiA8atTpqolmU5T_2Y4US-mAcIAxEZ8osnYIa5ONjLtHc8h-EK8LdoD2jZtg8BSYG4vy-1MfIHmkuEtw0g4BxJ1Puq9YGshLZJbhTe1qVitk1UCBkhfOmD5j28KIPJmg1ILl_EItPgcBP9WJXjyONQuIVMKGzPQ-o1WVUQY6a81PazISPM2u5iuE25Owc8GEIcnlnutURyS0Xjk7GiSBHdOp0vauhO456I5fd4R6xh78unhbuyWQ4GjfT5YfjXb5szdnSPTEzlaCMNPukD3vA2BYMeS_RA2RsBs8gbh1PU5GaZqzwWIeH8o7-vNvIUi72tibfBqFudSFU9WB_L7t0i8dPO1Noj-2MU622YPhXokTsa3TKUCav0iSzDvcazkBd3fBW6EEPlRa6yI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a08cf29fe6.mp4?token=b56nhlyO75Aq-S1wMK7uLY5_Z5pTMiz6vJoAzKeLqSn3LwZ00e9MA6zuigLJ97m91_O0hhJ8y0BuQ2qeX8W8Cs9p1FhLkpH7vXkvOlmaO6yk-Kx9GMjvRMwPppgxh7dmptdh3XvO8YkNorq9l-q-640kylwmla4smqMHmJjwMi6VhPcRutx8gYGfWuspJd8UvC-50C-U7yFwwRz69MqcDwnB6DexHyMzphRIjY63Zu63vzM1fuq2GltP3_03ombt-ZBRFXwK8Dxhrv3DarzvCQf0Q537wiA8atTpqolmU5T_2Y4US-mAcIAxEZ8osnYIa5ONjLtHc8h-EK8LdoD2jZtg8BSYG4vy-1MfIHmkuEtw0g4BxJ1Puq9YGshLZJbhTe1qVitk1UCBkhfOmD5j28KIPJmg1ILl_EItPgcBP9WJXjyONQuIVMKGzPQ-o1WVUQY6a81PazISPM2u5iuE25Owc8GEIcnlnutURyS0Xjk7GiSBHdOp0vauhO456I5fd4R6xh78unhbuyWQ4GjfT5YfjXb5szdnSPTEzlaCMNPukD3vA2BYMeS_RA2RsBs8gbh1PU5GaZqzwWIeH8o7-vNvIUi72tibfBqFudSFU9WB_L7t0i8dPO1Noj-2MU622YPhXokTsa3TKUCav0iSzDvcazkBd3fBW6EEPlRa6yI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیرترین حیوان خشکی‌زی جهان در رکوردهای گینس
🔹
لاک‌پشت غول‌پیکر سیشل به نام جاناتان با حدود ۲۰۰ سال سن که در جزیره سنت هلن در اقیانوس اطلس جنوبی زندگی می‌کند، به عنوان یکی از نمادهای رکوردهای جهانی گینس شناخته شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/660405" target="_blank">📅 16:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660404">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B02WmFtqwCiEINZ5mBUY5UlRffS-4LcRE_Z7cTQ-ZMMI1IiC4qPWVTqAE28ulLhgac7IYtWkp2ROGblJzGoBk3d9cD2g-NDIBj7rLHYlNu6MaIsjIERKLYC2IAAN8Qe9PPtfbk4Gtvz15vvquMoresqbUcgwP7hvM3Y-x2j9TJ63r11qZJjfWjOBfqhxcJjzyt5gj3LQFWCnyZA3RumUrb8oTfUAegd8h3Zv8LyYBQOQKrVNAD1OkAduxMB9vF7vG5hSFtfepTTyHEx0Nqx5-DauY-KCTvNDINQCt3uLpmkw71yoWhD-l_Uz0Sk6JyGSXT0IC9QBcQwfXAqJvwhaYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نسل حسینی
🔹
همراهان عزیز خبرفوری؛ عشق به امام حسین (ع) از کودکی در دل‌ها جوانه می‌زند. در این شب‌های پرفضیلت محرم، منتظر دریافت ویدئوهای کوتاه از مداحی و عرض ارادت کودکان شما به ساحت مقدس اهل‌بیت (ع) هستیم.
🔹
منتخب  ویدئوها در کانال خبرفوری بازنشر خواهد شد.
🔸
ویدئو های خود را با الوفوری به اشتراک بگذارید
👇
#ایران_حسینی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/660404" target="_blank">📅 16:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660403">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
عون: از آتش‌بس ایران حمایت می‌کنیم
رئیس‌جمهور لبنان:
🔹
ما مطمئنا طرفدار آتش بس با هر کشوری که به ما کمک کند، ازجمله ایران هستیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/660403" target="_blank">📅 16:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660402">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsK0xnHItGqyKFVnuI4AWGv_5klKw4SLztrjKXFp8iH9t67V2OY_Ym_bfdfw1m9Q9HNy_vssdtQwEq5fx02Fa9gi2p4ey0TBus6_35NcNANWxMOOJmALZMi-phZNPdmW5xxnowr3tLtexdxWMb-gY4OqGcRPkRVcMslGa8PaMpsJgxNaSt3Z1tA0FSvkjEed_TrbNi1wAhjml0a-t6q_bLR-9EP40HSrb-eYFz2G2EeO1bFu1tfoKR7v3OIaW7VEDJU01siYIqYJYyR1ogjocXDlNzSfQrFMDR90ygZkOHO5urZrRj8PIsloJTvCVBwJ71tp8LXPCKXzbPm5_9M38w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکونومیست: پایان جنگ ایران، اسرائیل را با چیزی شبیه به “شکست باشکوه” تهدید می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/660402" target="_blank">📅 16:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660401">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
تغییرات در دولت با وزارت نفت آغاز می‌شود؟
عصرخبر نوشت:
🔹
در آستانه تغییرات مهم در دولت و برخی پست‌های حاکمیتی، نام محسن پاک نژاد به عنوان یکی از اصلی‌ترین گزینه‌های لیست تغییرات دیده می‌شود.
🔹
از پاییز سال گذشته زمزمه‌های برکناری وزیر نفت بالا گرفت و سپس شنیده شد که با چند گزینه برای تصدی وزارت نفت مصاحبه شده است.
🔹
با رخ دادن جنگ رمضان، این تغییر متوقف شد.
🔹
با پایان جنگ و برخی حواشی حالا به نظر می‌رسد این تغییر اجتناب ناپذیر است.
🔹
اما مهم‌ترین سوال این است که وزیر نفت بعدی کیست؟ آیا از بین افرادی که در زمستان با آنها برای تصدی این پست مصاحبه شده وزیر جدید انتخاب می‌شود یا گزینه جدیدی عهده‌دار این سمت کلیدی در دولت خواهد شد؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/660401" target="_blank">📅 16:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660400">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
خطر سقوط آزاد خودرو؛ قیمت‌ها چقدر پایین می‌آید؟!
🔹
کارشناسان بازار هشدار می‌دهند که صنعت خودرو، بزرگترین بازنده احتمالی هرگونه توافق سیاسی با آمریکا خواهد بود.
🔹
تحلیلگران معتقدند حدود ۵۰ درصد از رشد نجومی قیمت خودرو در سالهای اخیر، ریشه در تقاضای سفته‌بازانه داشته، نه نیاز واقعی مصرفکنندگان؛ با حذف انتظارات تورمی، این حباب عظیم فرو خواهد پاشید.
🔹
نکته دیگری که کارشناسان از آن سخن می‌گویند این است که دولت به احتمال زیاد واردات خودروهای باکیفیت را آزاد خواهد کرد.
در خوشبینانه‌ترین سناریو، قیمت دلاری خودرو می‌تواند تا یک‌سوم سطح فعلی سقوط کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/660400" target="_blank">📅 16:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660399">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8780a438df.mp4?token=DeyxmzCm_ttikdmI212hHkjgXPf8_wwcSqSNjdJJLZ6uvljMuUNqaQoDKwwUE7Em_SumJ8SdlkOwiPBUZTCuAncT1Tv4FfGCrUngJGjMkStNpllpY0NY-O2Z8BW2AWNDs1ngOPipEjdduhwcn9nb8xBalwRhEqa25AXR6vYez4UpJ3qG2yqmi1X3OADXsFNoqmJY2Yea_dgcT9_yKE33kBr8mCj6oJ6g_fCov5R9EqDMRpyF5m5CbOQwvJTy8Q8ZuHrXKCJcTw5aqOwbj4_6eFcCu4CyQ_2azLhpuNzCUkYP8EcORFIi83xe9Z982t2kzmQvy9tZUT2Ywu_4ApCBOLQBbdSF1fA-1Dkn82elyxU3DOQOmnB2_SnqrLLQSfoGQjyKj6soRv17m6dTjB2tgRi8gVDyY3SO-JPNhZAZ65wDG8N_V8vQjMFltI-WJgJLAW0_319OqGKL_18jxNR4gVqU-KMLYr50HCwXj0fcZbHzDDcV51CBY4FzXZ8C9vb_W--HjTX26QP6wWF_xABdz8RpXZxCfhyHfQoxglXisHWjv3YRnqdeOboSSGLmR0zw_g0Whm253u2OaX-yArjWWUe59BQL62yre_h9ZuvJ8CMb3ubO9jl68rg2-N9MKWK39DmqN6GcH6AX431twhGFOmTxkMxi9VrP1Bd7-w4Q6rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8780a438df.mp4?token=DeyxmzCm_ttikdmI212hHkjgXPf8_wwcSqSNjdJJLZ6uvljMuUNqaQoDKwwUE7Em_SumJ8SdlkOwiPBUZTCuAncT1Tv4FfGCrUngJGjMkStNpllpY0NY-O2Z8BW2AWNDs1ngOPipEjdduhwcn9nb8xBalwRhEqa25AXR6vYez4UpJ3qG2yqmi1X3OADXsFNoqmJY2Yea_dgcT9_yKE33kBr8mCj6oJ6g_fCov5R9EqDMRpyF5m5CbOQwvJTy8Q8ZuHrXKCJcTw5aqOwbj4_6eFcCu4CyQ_2azLhpuNzCUkYP8EcORFIi83xe9Z982t2kzmQvy9tZUT2Ywu_4ApCBOLQBbdSF1fA-1Dkn82elyxU3DOQOmnB2_SnqrLLQSfoGQjyKj6soRv17m6dTjB2tgRi8gVDyY3SO-JPNhZAZ65wDG8N_V8vQjMFltI-WJgJLAW0_319OqGKL_18jxNR4gVqU-KMLYr50HCwXj0fcZbHzDDcV51CBY4FzXZ8C9vb_W--HjTX26QP6wWF_xABdz8RpXZxCfhyHfQoxglXisHWjv3YRnqdeOboSSGLmR0zw_g0Whm253u2OaX-yArjWWUe59BQL62yre_h9ZuvJ8CMb3ubO9jl68rg2-N9MKWK39DmqN6GcH6AX431twhGFOmTxkMxi9VrP1Bd7-w4Q6rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رقیب نامرئی در جام‌جهانی؛ تیم‌ها شوکه شده‌اند!
🔹
وقتی از جام جهانی ۲۰۲۶ حرف می‌زنیم، همه درباره ستاره‌ها صحبت می‌کنن... اما شاید خطرناک‌ترین بازیکن این جام، اصلاً انسان نباشه.
🔹
یه رقیب نامرئی وجود داره که می‌تونه بازی رو متوقف کنه، بازیکن‌ها رو از پا بندازه، و حتی سرنوشت قهرمان جهان رو تغییر بده. جزئیات رو در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/660399" target="_blank">📅 16:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660398">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
محدوده‌ مسیر تشییع رهبر شهید انقلاب در تهران مشخص شد  شهردار تهران:
🔹
مسیر تشییع رهبر شهید انقلاب در تهران شامل محورهای دماوند، انقلاب، آزادی و لشکری خواهد بود. تصمیم نهایی بر اساس ظرفیت جمعیتی و مدیریت ترافیک اتخاذ خواهد شد و از معابر فرعی نیز برای تسهیل…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/660398" target="_blank">📅 16:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660397">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
اطلاعیه شماره ۳ ستاد بزرگداشت عروج خونین امام مجاهد شهید حضرت آیت‌الله‌العظمی خامنه‌ای‌ قدّس‌الله‌نفسه‌الزکیه  بسم الله الرّحمن الرّحیم
🔸
«مِنَ الْمُؤْمِنِینَ رِجَالٌ صَدَقُوا مَا عَاهَدُوا اللَّهَ عَلَیْهِ فَمِنْهُم مَّن قَضَى نَحْبَهُ وَمِنْهُم مَّن یَنتَظِرُ…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/660397" target="_blank">📅 16:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660396">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca5f446d51.mp4?token=aI7JPyLwuFuoRcMfEzcP4Gz5-pAuaIIBTSW1BjV0b1skUbLmK73EOCYFGM1NXmnDdy1t7T9WqmJwOclF6IK6L4QjUQTbgyjRlB85Hk1jJcUS02_9GREIx3rjhMbxf1NrB15_mXhdvslZoHRe_SqbVJMVOtE-C9h02VsaB10PDKpp9xRirmLT3apc6ldP_27SOig-lmNZ9qf07mrR_woYQRkgrNPz-fi-oU5vL3XI08aDdRQCg4igKV3kkyT_RSdLtNz1KIZDYcRAQ3dOAriKzthj6XZpwFZSLJmLEYD07KgQxu5hSZCvTOR2xLogtbtDOD_1V1_NH1VTRT5935brtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca5f446d51.mp4?token=aI7JPyLwuFuoRcMfEzcP4Gz5-pAuaIIBTSW1BjV0b1skUbLmK73EOCYFGM1NXmnDdy1t7T9WqmJwOclF6IK6L4QjUQTbgyjRlB85Hk1jJcUS02_9GREIx3rjhMbxf1NrB15_mXhdvslZoHRe_SqbVJMVOtE-C9h02VsaB10PDKpp9xRirmLT3apc6ldP_27SOig-lmNZ9qf07mrR_woYQRkgrNPz-fi-oU5vL3XI08aDdRQCg4igKV3kkyT_RSdLtNz1KIZDYcRAQ3dOAriKzthj6XZpwFZSLJmLEYD07KgQxu5hSZCvTOR2xLogtbtDOD_1V1_NH1VTRT5935brtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر «دست دادن با اکراه» ترامپ، رئیس جمهوری آمریکا با مکرون، رئیس جمهوری فرانسه در جریان نشست سران گروه ۷ (جی ۷) خبرساز شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/660396" target="_blank">📅 16:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660395">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4M_GifdNHPPI1qc3CAh0PiVVYeV97O6GaVipQLlKmuJSGVg3dPVTXGZ_r0x-yrz2hct9q6TL7Sp4JzYk8KivXKKoFyxhIgOj8C4BCAV4aodoo6OiJEOEJTeB3wlutXwiEMNbTwxOVkNF-QVZGva6M5PY1u-TVEGudYtEt0fqilX2zXdaS37c5OA2LFOMuMCiLk5-CH3yyU5ZnwAFNLLd3tuuBWJAYldb5DzI28W8MOGZjnljaKe11omoKeaN5YZg0eVU_tb271YOUDrZyj5H_KPtFhmeN7IdPXEuFqrzdU-oGanWW7_Ml64w0BooX0A7L8eOXmRzrO5Y6aI-O6Qcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وام بانکی: طنابِ دار یا سکوی پرتاب؟
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/660395" target="_blank">📅 16:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660394">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
کانال ۱۲ عبری: بورس تل‌آویو خوابید
🔹
بورس تل‌آویو برای سومین روز متوالی پس از توافق واشنگتن و تهران به کاهش شدید خود ادامه می‌دهد.
🔹
شاخص‌های اصلی حدود ۱/۵ درصد کاهش داشتند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/660394" target="_blank">📅 15:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660393">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
واریز وجوه به حساب پذیرندگان در هر ۴ بانک ملی، صادرات، تجارت و توسعه صادرات امکان‌پذیر است   مدیر روابط عمومی شرکت خدمات انفورماتیک:
🔹
با انجام آخرین اصلاحات و به‌روزرسانی‌های نرم‌افزاری و فنی، بخش مهمی از خدمات بانکی این چهار بانک در دسترس مشتریان قرار گرفته…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/660393" target="_blank">📅 15:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660392">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2397199775.mp4?token=HuCZxSO5kqnJKj0RzkLPLOR4024IodINACSLYc8xQTbLCh6m1cKilbDcF6SH5T-mepc6rWycv_B4I1XbaagS0ycaGnoC3MI_l4f35O3T5fgzpvpwfIx9m7BmHhYEfSzCmoDz1U4Uk9R7iR1Kztg-xCCocoo2oEM9x-LsnATn1wMw7bkPU4ppr_0Gm8KZiBevrIHRwRTjQfLfa2jf7daLxwNC9vKmrVcrHNSZJ3kUhm-wA4YR7_V_CKU4RHxq1hrYbtk7iUmo1fOoR5bnP8FKjgy7OFZIO7EsHXFoPEW1aCUtfnftGvNcbOvI0-HnKTO07vrj5lQr7Z0vLeQt19gAgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2397199775.mp4?token=HuCZxSO5kqnJKj0RzkLPLOR4024IodINACSLYc8xQTbLCh6m1cKilbDcF6SH5T-mepc6rWycv_B4I1XbaagS0ycaGnoC3MI_l4f35O3T5fgzpvpwfIx9m7BmHhYEfSzCmoDz1U4Uk9R7iR1Kztg-xCCocoo2oEM9x-LsnATn1wMw7bkPU4ppr_0Gm8KZiBevrIHRwRTjQfLfa2jf7daLxwNC9vKmrVcrHNSZJ3kUhm-wA4YR7_V_CKU4RHxq1hrYbtk7iUmo1fOoR5bnP8FKjgy7OFZIO7EsHXFoPEW1aCUtfnftGvNcbOvI0-HnKTO07vrj5lQr7Z0vLeQt19gAgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: فراموش نکنید، هیچ‌کس تا به حال به اندازه من با ایران سخت‌گیر نبوده است
🔹
این کار باید توسط کلینتون و باراک حسین اوباما انجام می‌شد. باید توسط بایدن، بوش و خیلی‌های دیگر هم انجام می‌شد. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/660392" target="_blank">📅 15:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660391">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUKdQ5rLkWrfTwc5Xz6uAE2FGnsp1Q9W0Wn7sLo9FuEk_2Qlbh3nQL-GZdjvSKCAC3J791CKThGdDiwz6l4YCfeJnMqe-GIrjbYXqhEeIiLItHtEu-lHjsAQHZkZgzsIZQv0xqYPiRpmn3ufEsf2MY0lh0N-V6YWDW_GF5onS-eAuPOsZmzTFPSPw_DzmV4ph908m5bSNc8KhJyFMagaAr3s3M4VLtuTUeqQSeLf-ZJHc3y44x7rH4ZOJX07w1y-Z0X8T42dl7hba7RFQM8gRQL2YqnT1TaTeV_nrbH0JhWNBKYKTkREFXeNs6rydTDyzAhIxrd9j2JLoXAdaIRiMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شرایط فروش ۱۱ محصول ایران خودرو اعلام شد
🔹
شرکت ایران خودرو شرایط فروش فوری و فوق العاده یازده محصول خود را با قیمت قطعی و موعد تحویل ۳۰ روزه و ۹۰ روزه اعلام کرد.
🔹
برندگان نهایی از طریق قرعه کشی انتخاب می شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/660391" target="_blank">📅 15:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660390">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fK1o5qPMJ5MsJc6Z-te0tyyHTzqNXuDAuDQBQ_18GpIlQzbawpinriQGxf7GJmkJcWMHUJX5mx0dA4WpqXBvVPRh4KlFR3-40D5LVkmX8f9m56n3hO84Xaz8zN2VyTdSkJmTFFAfsWFzkfCQM-TIvb4EUdo-5nX_QPmDsw5e9P-Au5eMTzXq8lspu2gPRG6TDn2UqvZ3UQKC-sTXYLAWf9SsNn2OyP8mdYKLQIF4It96UKTinaDFxNgXbjPdw7UNxa4pm6JaurzczklUK2L3bQri8BAaHEUbv0_ccS8dRaE5SI_qM5yRL4-xMc4kUD8L-OzcIU9REOZ_gEYztNMBww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: توافق به ایران اجازه می‌دهد که فورا نفت بفروشد
وال‌استریت‌ژورنال:
🔹
منابع آگاه گفتند که امریکا به ایران اجازه می‌دهد تا بلافاصله فروش نفت و سوخت را تحت این توافق برای پایان دادن به جنگ آغاز کند و به تهران انگیزه مالی اولیه برای کاهش درگیری می‌دهد.
🔹
به گفته این افراد، معافیت از تحریم‌های فروش نفت بلافاصله پس از امضای توافق در این هفته اجرایی می‌شود. همچنین خدمات لازم از جمله بانکداری، حمل و نقل و بیمه مورد نیاز برای تسهیل فروش را پوشش می‌دهد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/660390" target="_blank">📅 15:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660388">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MNpLWusRSS6Bo43wwL0l-pJ2cT8UOqWboer-Sq9rFcPLItywNOGUpUpUY10mF7gmYw0DAew54Fp10hBxm__hY_d4pL5zCfbw6e6Fy8nvRYy250CBLpqArMYn9WVbSLU41Q58P3WomgekRgUZs7nlxQ5_TBb2xISkb6XzdlFlXsFrj388OAQ4MA8rK0jeln13PfeYpO0kAm62PA1-nPXCnkgYgMjs5cSDZ8BtbSDPX2sdsnyGfq3aWN7-U64q98P0RhPz5tJesuL0m44P_3nIfXc7Az1b5Eyt6v7OxRL9TXyYJkLFVXU08K7SjnUCCWtEZcHpnEjHx0g7qcg78Rm6bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f1HWXEMS37EQXQVqEyVMieM1KC-NuTHxY4k4SrRglz9Y_76h6nAbOwbiGjJ-gkI2vblIm7w9A8uR0u4qXIJXlYpsIe7Hd9CfqiZir8sIADdgggwuyd1WzPg7xESpmcHp3ZwGII_qAGc4g_-NWt_84-OWvalokp4K9V36o8GM8SQRXxkL3Wf0pLOLutuWiqHmzMMQZIdKU9-mwLN6YI3LpwekM4Q25aUSTzNa8TZnPF7XNwyy1TMR3miXy_3W8Mu4Um3zs8RDvurxC_BklryF3_tAS6X6qFyEZ-9HsYFEL5rSA2oTHz3zJ1DnBIkYPKKMWSn7SxHVPjw9VErTgYKDZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ساخت توالت رباتیک متحرک در چین
🔹
چین توالتی رباتیک طراحی کرده که با فشردن یک دکمه کنار تخت می‌آید؛ این دستگاه پس از استفاده، قابلیت شستشو و خشک کردن داشته و در نهایت به‌صورت خودکار تخلیه و تمیز می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/660388" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660387">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc54eb65d7.mp4?token=ZYKfjyOrlSj-xGzqDqomrrYBRaTSeu6neTCBFxN_fZ5N0pGSTzBUxNoi8BQPUYdyUkFpvJ7h7xLHf4FwJlBzBNKQV-LC-RdDY6lmHnZwIuYP1V42HU4H5Z79JQeMmSf5BxRmpIRWloEfPt_ElVxQ9dPAg4qYD8X_aYzHgm0qgz3Nwqb1EySYUwpquqBDNWgGqi12zEgDJ2UBB6U7T4We_KrSlcLUFBre7nmNzYVRq8ariWw_-SmsF_yXJhHZIilmUAERHR5S7Q_e1Fc9cRLBY5dO7Rsm8VdJKVxXn5cbLMZ_oZWHO4zH318Z0UoeoB0F5zz2DOI1eN45pOxI11aRUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc54eb65d7.mp4?token=ZYKfjyOrlSj-xGzqDqomrrYBRaTSeu6neTCBFxN_fZ5N0pGSTzBUxNoi8BQPUYdyUkFpvJ7h7xLHf4FwJlBzBNKQV-LC-RdDY6lmHnZwIuYP1V42HU4H5Z79JQeMmSf5BxRmpIRWloEfPt_ElVxQ9dPAg4qYD8X_aYzHgm0qgz3Nwqb1EySYUwpquqBDNWgGqi12zEgDJ2UBB6U7T4We_KrSlcLUFBre7nmNzYVRq8ariWw_-SmsF_yXJhHZIilmUAERHR5S7Q_e1Fc9cRLBY5dO7Rsm8VdJKVxXn5cbLMZ_oZWHO4zH318Z0UoeoB0F5zz2DOI1eN45pOxI11aRUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدر اعظم آلمان مرز: توافقی که بین ترامپ و رهبری ایران به دست آمده است، واقعاً یک موفقیت بزرگ است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/660387" target="_blank">📅 15:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660386">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
پرداخت معوقات حقوق بازنشستگان در ماه آینده
فضل‌الله رنجبر، سخنگوی کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
تامین اجتماعی برای بحث پرداخت‌ها مشکل منابع مالی دارند. درحال رایزنی با دولت هستیم که تامین منابع صورت بگیرد و تامین اجتماعی نیز پیگیری می‌کند.
🔹
برای پرداخت معوقات حقوق بازنشستگان در این ماه منابع مالی نداشتند و همراه با معوقات قرار است در ماه آینده پرداخت شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/660386" target="_blank">📅 15:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660385">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
امضای توافق آمریکا و ایران با حضور قطر و پاکستان برگزار می‌شود
دولت سوئیس:
🔹
مراسم امضای یادداشت تفاهم بین آمریکا و ایران در روز جمعه، با حضور نمایندگانی از پاکستان و قطر برگزار خواهد شد.
🔹
بیش از ۲۰۰۰ سرباز امنیت محل امضا را تأمین خواهند کرد و برای تضمین امنیت، منطقه پرواز ممنوع اعمال خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/660385" target="_blank">📅 15:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660383">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0283ab5cec.mp4?token=hOf2db9n7ysyvrXTEdbXdPXTeEDfpILpXbCrZiOCLyXxrsOuUUCR5gH6ho1QrZL_LpiAy_7yXAE2ClysE1eKZ1n56CsD39_bAC4T4T_UdB1SD8XNsxXshddXkac2-kn3G9VZy3bHI8lKvrRWY8Zo8wuIvSMRon5tQyD7Y6MNQoJFo_lYrWOc8J9MskOedM7_2gO81VnmKn3lg9DMPXqUzHmtg3GQ9T9jjMhzikL3jJfvRJ-JUkxMLtzLOp7QsGhSuIr1VsK4cxlAjHD1BMQxrUBwFXmvraU5IkRMEQzQD1WF_cyDPRpPpi1MsFDgCdNlBafeBIWxstMQPsZgp2uEuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0283ab5cec.mp4?token=hOf2db9n7ysyvrXTEdbXdPXTeEDfpILpXbCrZiOCLyXxrsOuUUCR5gH6ho1QrZL_LpiAy_7yXAE2ClysE1eKZ1n56CsD39_bAC4T4T_UdB1SD8XNsxXshddXkac2-kn3G9VZy3bHI8lKvrRWY8Zo8wuIvSMRon5tQyD7Y6MNQoJFo_lYrWOc8J9MskOedM7_2gO81VnmKn3lg9DMPXqUzHmtg3GQ9T9jjMhzikL3jJfvRJ-JUkxMLtzLOp7QsGhSuIr1VsK4cxlAjHD1BMQxrUBwFXmvraU5IkRMEQzQD1WF_cyDPRpPpi1MsFDgCdNlBafeBIWxstMQPsZgp2uEuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تداوم
حملات هوایی اسرائیل به جنوب لبنان با وجود توافق آتش‌بس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/660383" target="_blank">📅 15:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660382">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10f231732b.mp4?token=ezgvMOI7ZCX_DKFX8FIgDADH1GcdigiHniRGrJBGh4noGrba54sPT95E-uib3a7gAkK-S8VkPtpFBSe6z2taSFUw_p_hvvmQSAfTjzvL7TiD9d9S4MLInX9TyD_x8An6Mcs9dK9FzIgWGVQ6JiEOgbjx7Z5Gqotw1vfLEzcqVZDmAf2cM8e510vMhE5MKZ5aeoiAWR6cNbtN44bJTKRho0jkgyIpIowE_QEcousfM_UGnFUtAFHU7q7xUcDbH2flFqvE1ckuPjnkiJYwEZz65WUPXZ3IiNVxj1QiIpwTUDlPn6Q5h_gIH8Ou9GcOAhYb0gnvRJWGp0zGiDvRDmbyLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10f231732b.mp4?token=ezgvMOI7ZCX_DKFX8FIgDADH1GcdigiHniRGrJBGh4noGrba54sPT95E-uib3a7gAkK-S8VkPtpFBSe6z2taSFUw_p_hvvmQSAfTjzvL7TiD9d9S4MLInX9TyD_x8An6Mcs9dK9FzIgWGVQ6JiEOgbjx7Z5Gqotw1vfLEzcqVZDmAf2cM8e510vMhE5MKZ5aeoiAWR6cNbtN44bJTKRho0jkgyIpIowE_QEcousfM_UGnFUtAFHU7q7xUcDbH2flFqvE1ckuPjnkiJYwEZz65WUPXZ3IiNVxj1QiIpwTUDlPn6Q5h_gIH8Ou9GcOAhYb0gnvRJWGp0zGiDvRDmbyLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: توافق با ایران بسیار قوی خواهد بود
🔹
آنها هرگز سلاح هسته‌ای نخواهند داشت. بنابراین این یک توافق بسیار بسیار مستحکم است. یک معامله بسیار قوی است. هیچ‌کس نمی‌داند [محتوای] آن چیست. بسیار قوی است و به نظر می‌رسد اکثر مردم از آن بسیار راضی هستند.…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/660382" target="_blank">📅 15:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660381">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
گزافه‌گویی ترامپ: اگر رهبران ایران رفتارشان را بهتر نکنند، دوباره به ریختن بمب بر سرشان بازمی‌گردیم
🔹
با ایران به یادداشت تفاهم رسیده‌ایم، نه توافق نهایی. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/660381" target="_blank">📅 15:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660380">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
آغاز پرداخت حقوق خردادماه بازنشستگان تأمین اجتماعی
🔹
سازمان تأمین اجتماعی پرداخت حقوق خردادماه بیش از ۵ میلیون و ۲۰۰ هزار بازنشسته و مستمری‌بگیر را آغاز کرد؛ مبالغ پرداختی بر اساس احکام جدید سال ۱۴۰۵، شامل تمامی افزایش‌های مصوب و مرحله نهایی متناسب‌سازی محاسبه شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/660380" target="_blank">📅 14:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660379">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMNLMC6wTWzY16qsymEhzOzuGfhLA4dSzitjRlYX15zdmIOaT3V0w4oTOVtf0aMANWjPL4-OCug1Sjj1kayAqu_B9YeZVHPOBEodYvml-bLo65V5tsM7ZIQHbImdfV-qn5AGIH3MazhgK5Y3B9GypuwzRkSQc1SWOU0ZhIB3FyfK5pFuo5szNBEUY8feYCePpz6SmWMf4O4kaO8mXBn-96__pJgHW6msAaCtjI2ASEbQetp_lMauBps7P2FQFJBzWAFid6p4skUsrjwPE-c0czvmEjs4HwAgBH1DNxKYhxd8UkdkU6rQOAva_dLJmDEr9ZeE9mrX64SgDZr8AZ8amQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گستاخی پمپئو: نباید پای‌مان را از گلوی ایران برداریم!
پمپئو وزیر خارجه دولت اول ترامپ در گفتگو با فاکس‌نیوز:
🔹
در حالی که هنوز فرصت داریم تا به نتیجه‌ای خارق‌العاده برای آمریکا برسیم، پایمان را از روی گردن آن‌ها برنداریم.
🔹
پول به حکومت ایران برسد، برای اهدافی بد استفاده خواهد شد؛ احتمال اینکه ایران به یک کشور عادی تبدیل شود بسیار پایین است و نباید آنها پولی دریافت کنند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/660379" target="_blank">📅 14:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660378">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbX-p9pxqyA1F3h_NpwXtAJC1MSoFdm1K7zVKS7GvWD8fpPGrsjxNnEUXZmiE_PxSqgCFxgAq0C2K06dG3v4epEtAMfoypv-HrNNdg8e4j82fwtPpvNw6u-9Ii2IQt_RHH6vFOnJorPJSn1QBxrEVcnjA3yTzW1Ntn4gAg5cYgGn5T-boVQSIxTAcRWegQhchKUbMCunHfuQaGgGzKZt2GvF08RocUTUxHtbcOj2wLAOc_BlPN-wGcN7BborFYuv0oeYErYN7di-wAy08WTF4eq2lp-MZAlKgCf_tfn5sJEP5WOipjfRS-IK3yQv89ijNltw-M-lPQXsNkLbmbQvvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درصد تغییر بازارها از سال ۱۴۰۰ تاکنون
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/660378" target="_blank">📅 14:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660377">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5ba12193e.mp4?token=SaWl1_QA12udCySjC59e-8R9Fim5NtzQLNOaitZVS_RAl4lTJ3x0v6-qIUcYN3ZBhopjwRuxc5RpdYj42WLineRi54yDs1NfAz4OvbBkcvJimzr8TYZjqhThFRSEgPtRvoqQ8dEyTB5_vl3DXM1z2jTUB6ofQJB3mPjXj8wvLWqXaDRtlByqO0C32b76RqtgNy3-orLAymUEUexo5epqokkUAVNMxJ1Lzte9t8dYo9Vv6QwmqHs7Hjvezye4USpcuJj9ojdAfMD1-1-vTOPLRWx127fb5ZkYy3O0SIXp7pMCD-rpmR8eacHPGIQWdmFExNFmxRuRKhye_ltMZJ3ae5-HVkQS2gFFd0R_1mzotscAW4b-RRIy-d0H8X7R-O-70qHR1PRTQ_0DiKhAmJPx73FM-BCiSMPIjBmxwczbvtYRWjWD6e2UerZ5APTssSoPbSasxw911MBI85DVvcw37UON6jEzN-7GQ2cTwKzIlUJ4IE1yDgrYMaDZ017v1bWCGCI3YpRD1K72KNMTolTs4vEZ-YD3wh73cHIu-tZpszG58kDoX7kHPgyyKYniuIhscJfT6Z5ITeLS3wJWsrU1K3SitLlAFpupAJ0P5dCzf9oKFDkEpWql7Cvd2tBvrsXs0A2-5sjKLRt2DrPD4WtHLdulRf4YJ_649XMFcyVe6bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ba12193e.mp4?token=SaWl1_QA12udCySjC59e-8R9Fim5NtzQLNOaitZVS_RAl4lTJ3x0v6-qIUcYN3ZBhopjwRuxc5RpdYj42WLineRi54yDs1NfAz4OvbBkcvJimzr8TYZjqhThFRSEgPtRvoqQ8dEyTB5_vl3DXM1z2jTUB6ofQJB3mPjXj8wvLWqXaDRtlByqO0C32b76RqtgNy3-orLAymUEUexo5epqokkUAVNMxJ1Lzte9t8dYo9Vv6QwmqHs7Hjvezye4USpcuJj9ojdAfMD1-1-vTOPLRWx127fb5ZkYy3O0SIXp7pMCD-rpmR8eacHPGIQWdmFExNFmxRuRKhye_ltMZJ3ae5-HVkQS2gFFd0R_1mzotscAW4b-RRIy-d0H8X7R-O-70qHR1PRTQ_0DiKhAmJPx73FM-BCiSMPIjBmxwczbvtYRWjWD6e2UerZ5APTssSoPbSasxw911MBI85DVvcw37UON6jEzN-7GQ2cTwKzIlUJ4IE1yDgrYMaDZ017v1bWCGCI3YpRD1K72KNMTolTs4vEZ-YD3wh73cHIu-tZpszG58kDoX7kHPgyyKYniuIhscJfT6Z5ITeLS3wJWsrU1K3SitLlAFpupAJ0P5dCzf9oKFDkEpWql7Cvd2tBvrsXs0A2-5sjKLRt2DrPD4WtHLdulRf4YJ_649XMFcyVe6bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صداوسیما: با فروپاشی محاصره دریایی آمریکا ۳ نفتکش ایرانی با ظرفیت ۵ میلیون بشکه نفت خام از تنگه هرمز عبور کردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/660377" target="_blank">📅 14:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660375">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
ترامپ قمارباز: تحریم‌ها علیه ایران مؤثر بوده است و اگر ایرانی‌ها درست رفتار نکنند، دوباره بمباران سرشان را از سر می‌گیریم
🔹
ایرانی‌ها اوباما را فریب دادند و میلیاردها دلار به دست آوردند. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/660375" target="_blank">📅 14:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660374">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhKUbtaqenE0pRCtlTkmE3L2JnClaqRhbAZhOLA-9_4XhiChcmwSh7d5Omy5uXIb7BGbIXMxMdl_qegFvz8O3gyrL0Voo2vQQjWm7f0Imy4hWMzQFSrGYGqZDYhww9vV4LzOheU1IPqqp5-pmIllGXBH778Cw7din3SFf3m4aM8cGlWMGKr7hmtXL77SuQMRlW4WmBueG2u-I8zq7B-1gQepL5_5ov7iAbauAki563ZnooaFM2bhylRsEBqHmlonqpmMYrljDUFH5-BkZxYp5bcGZhS0psMzd_RlZcteGfyODPr2xB9_QhWf376gT0wXjaWqdYZFjuAynqXl6pOV3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رضاییان بالاتر از هالند و امباپه؛ بعنوان سومین بازیکن برتر جام‌جهانی تا اینجا
انتخاب شد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/660374" target="_blank">📅 14:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660373">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
ترامپ: قیمت نفت بلافاصله پس از اعلام توافق با ایران کاهش یافت
🔹
در این یادداشت تفاهم قید نشده که ما هیچ پولی به ایران پرداخت کنیم، اما نمی‌توانیم هیچ طرفی را از سرمایه‌گذاری در آنجا منع کنیم #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/660373" target="_blank">📅 14:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660372">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adea239337.mp4?token=NMCOtkij-8ZCGdf2gbqrVllXeHgx8vO6x7hWC4uY1zbEJfrRpPHTDoMythkJyn_KyC441tvNx73LdgZ7gyGZ2qAtLwMvByQdn65XuRgvcG45ytEC-rwI2lpo8etpNGJ4ao0WpAVN8P8mf-_4qXDlOLyD-pxPopTdBHz_LSi1bg9Jl0y3yXJR57eZ80V_eN2J9pO6Hq813MffgQ2jVlW07jf-VrnaOV5uxuoWU73tTSMI5RLMq3ubi2U49ds4k_2gI5X2VD668-dMVsjbeYKmVy1UVd5m1aZmzaCDR22oeG6As5LoWq1936TsO2X0d2GMysajmzGSBW9rmNy7fmkgNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adea239337.mp4?token=NMCOtkij-8ZCGdf2gbqrVllXeHgx8vO6x7hWC4uY1zbEJfrRpPHTDoMythkJyn_KyC441tvNx73LdgZ7gyGZ2qAtLwMvByQdn65XuRgvcG45ytEC-rwI2lpo8etpNGJ4ao0WpAVN8P8mf-_4qXDlOLyD-pxPopTdBHz_LSi1bg9Jl0y3yXJR57eZ80V_eN2J9pO6Hq813MffgQ2jVlW07jf-VrnaOV5uxuoWU73tTSMI5RLMq3ubi2U49ds4k_2gI5X2VD668-dMVsjbeYKmVy1UVd5m1aZmzaCDR22oeG6As5LoWq1936TsO2X0d2GMysajmzGSBW9rmNy7fmkgNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: تنگه هرمز طی دو روز آینده کاملا باز خواهد شد  رئیس دولت تروریستی آمریکا:
🔹
توافق با ایران به دلایل زیادی توافق خوبی است که یکی از آن‌ها جلوگیری از دستیابی ایران به سلاح هسته‌ای است.
🔹
تنگه هرمز به‌صورت جزئی بازگشایی شده و طی دو روز آینده به‌طور…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/660372" target="_blank">📅 14:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660371">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ادعای ترامپ: تنگه هرمز طی دو روز آینده کاملا باز خواهد شد
رئیس دولت تروریستی آمریکا:
🔹
توافق با ایران به دلایل زیادی توافق خوبی است که یکی از آن‌ها جلوگیری از دستیابی ایران به سلاح هسته‌ای است.
🔹
تنگه هرمز به‌صورت جزئی بازگشایی شده و طی دو روز آینده به‌طور کامل باز خواهد شد.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/660371" target="_blank">📅 14:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660370">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786c67eb77.mp4?token=VvbilDZqECi3gdHTlfNkUyW-B9MXHGxrmkxUdIoyV8sJPAnHzvRwFZBvdsEkPnvtDhim8Nt9_YJS0wglSTFrSE70FTJJwFZ2eCnrQquOGisdSNhJGCXFE7p25QkNbDZd7FXWcyB_yBodZZdDrX0zioP6W7fWCdHuWBrAPeFGzGn54ah6Vbh1Tu-J-z5dPEUi3s1CEwha0B9hVylb8xk0JuWJ_RTIgtAuSZsjLQHZaQhzwaB2A2bij7rnWfoVAsJoCReX8_k7lsEoaZSChWy6wmrfs9EnI1KFLGc9JK-Aa7XB5aK06-3XdrWACzyRWlsEM4PNIrhopxHdjTMmFz_Nqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786c67eb77.mp4?token=VvbilDZqECi3gdHTlfNkUyW-B9MXHGxrmkxUdIoyV8sJPAnHzvRwFZBvdsEkPnvtDhim8Nt9_YJS0wglSTFrSE70FTJJwFZ2eCnrQquOGisdSNhJGCXFE7p25QkNbDZd7FXWcyB_yBodZZdDrX0zioP6W7fWCdHuWBrAPeFGzGn54ah6Vbh1Tu-J-z5dPEUi3s1CEwha0B9hVylb8xk0JuWJ_RTIgtAuSZsjLQHZaQhzwaB2A2bij7rnWfoVAsJoCReX8_k7lsEoaZSChWy6wmrfs9EnI1KFLGc9JK-Aa7XB5aK06-3XdrWACzyRWlsEM4PNIrhopxHdjTMmFz_Nqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: ما باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/660370" target="_blank">📅 14:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660367">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e625a751f.mp4?token=HnvWuudV1N4OykkWZBsD89-eaH228owraZ2fb1siarIpqlcnwBH5KYTiLDmJFwGqOpr4iatDFFhkTT5A20-4-8U-F99bBOq2fP_oDb3TfDGaIoyzP1CaPXuyf4jEPe6iCn5T0GLFeG90CyCrK1I40kiBR3Vxk1ejjrC3JFqYMBitr0OOSiU882U9pYqgR6KOptpj3zOX88wXjW08rkGG8ZFDv433Xmd4A-cgr_ATfwPhWoIIak1UL45oQRrRx4-hmdoC0iACi9N65nUg-O6Kskal3P-2KU8GhjBPhssKaa2jfOD4mnJSh0RDBsfM1uYvLpwt9xFFr5gC0OChyIc9yQiG-b5NbZ_RMq86_SuC7SPg3K_3kGlcl4Z7lMaWObxRjAOalbDyGqxkXP5ksZUorxhFseY9nNhJD7Onvcwrk2Xy5x1LnnMIerfLrr4nVM3DpmHXuwk0HLBfB3NKEU-inRgSiHrYsoBGNWYAKplRM1p8O5_divSVVjdcZBUirSfUFksaHztR-Oczo23DiGqRwxdwHAb24hri9BrjHa_XHQ57huRAmsVIN3faO9-GX2RPFpG09FP39r9i63CC1eKEc6bYHWsqY0lO2qLhdWRu0JNKR_d6awb-vp0BlRYnGKn_6B3_mUF3DkC1zwXX9gv_N1PGmzdPObbHjNI_HujUIpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e625a751f.mp4?token=HnvWuudV1N4OykkWZBsD89-eaH228owraZ2fb1siarIpqlcnwBH5KYTiLDmJFwGqOpr4iatDFFhkTT5A20-4-8U-F99bBOq2fP_oDb3TfDGaIoyzP1CaPXuyf4jEPe6iCn5T0GLFeG90CyCrK1I40kiBR3Vxk1ejjrC3JFqYMBitr0OOSiU882U9pYqgR6KOptpj3zOX88wXjW08rkGG8ZFDv433Xmd4A-cgr_ATfwPhWoIIak1UL45oQRrRx4-hmdoC0iACi9N65nUg-O6Kskal3P-2KU8GhjBPhssKaa2jfOD4mnJSh0RDBsfM1uYvLpwt9xFFr5gC0OChyIc9yQiG-b5NbZ_RMq86_SuC7SPg3K_3kGlcl4Z7lMaWObxRjAOalbDyGqxkXP5ksZUorxhFseY9nNhJD7Onvcwrk2Xy5x1LnnMIerfLrr4nVM3DpmHXuwk0HLBfB3NKEU-inRgSiHrYsoBGNWYAKplRM1p8O5_divSVVjdcZBUirSfUFksaHztR-Oczo23DiGqRwxdwHAb24hri9BrjHa_XHQ57huRAmsVIN3faO9-GX2RPFpG09FP39r9i63CC1eKEc6bYHWsqY0lO2qLhdWRu0JNKR_d6awb-vp0BlRYnGKn_6B3_mUF3DkC1zwXX9gv_N1PGmzdPObbHjNI_HujUIpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیزر قسمت شانزدهم از فصل چهارم
🔹
در این قسمت ادامه روایت تجربه‌ نزدیک به مرگ آقای یاسر درخشان که به دلیل تصادف، روح ایشان به برزخ سفر کرده و بازخواست شدن برای آزار رسانی و زورگویی نسبت به همسر و فرزندان تا انسان‌های رهگذر را درک کرده، نظاره می کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: یاسر درخشان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/660367" target="_blank">📅 14:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660366">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDteMYxtDCA_VERGj9n6tmskrUoUeVmReA3O0xu8tPKKiq0Atyhia26eIOqxaIx_Zgeeapvl59LMs0sbAAc-7zHH2v8wPIysMSrCDSdWf2_phS7jwwdjWFjO4UgCpSl73FdVuFq5ohbyYKwUlpfe99zHItFN_XGl4tgpLIQFLBJLU3qm6Pk3YkmmuEQEn_KGvp6LVBYVaIlZsbni2lOniF8RzEUdBJNbOVIREac17pQS4me7fwdDC73jZQ-ER-4FgCjvCECqR1G6d2oT9BeADlqXb7ToeHN1N-k2wmsDCipSkr20wjizYCbqF74QGgVh7aGHks6xiNJsOFaPgpaKGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«تراز تجاری» رو زیاد شنیدیم… ولی دقیقاً یعنی چی؟ #واژه_کاوی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/660366" target="_blank">📅 14:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660365">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28c3cd264f.mp4?token=if3y2oVHl7AcnCDPOuiMwiWx3xc7r6T2IT6XytXYi23ec9Ck0wZ9lxHsZQsduM6gjbs-C46cPcC3hSgKntgcQ0zWVM9RaR_k0MUPGLM77W0WcUlU6AaNWEcsuory0Shft0KuxH-7huolBeKNdXGhzCUFFFoteULit1P66rKkB2aANx1hEpZv5PVPBY_Wx9k45Nr9scdu3cUcggFn1xEgfUteRVYPympRnjQ5hUjvQt76KMe2RlZj9R6n9ELGau1M-fsNWHCqMU0GG7pLT_n5TWs5LnjSDniXrRFEPcToQH0qVGsEQdUXk418hb_YyRiewcbHT7ApjaLvgnT3Ce76pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28c3cd264f.mp4?token=if3y2oVHl7AcnCDPOuiMwiWx3xc7r6T2IT6XytXYi23ec9Ck0wZ9lxHsZQsduM6gjbs-C46cPcC3hSgKntgcQ0zWVM9RaR_k0MUPGLM77W0WcUlU6AaNWEcsuory0Shft0KuxH-7huolBeKNdXGhzCUFFFoteULit1P66rKkB2aANx1hEpZv5PVPBY_Wx9k45Nr9scdu3cUcggFn1xEgfUteRVYPympRnjQ5hUjvQt76KMe2RlZj9R6n9ELGau1M-fsNWHCqMU0GG7pLT_n5TWs5LnjSDniXrRFEPcToQH0qVGsEQdUXk418hb_YyRiewcbHT7ApjaLvgnT3Ce76pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوران های آتشفشان لووتوبی در اندونزی
🔹
مرکز آتشفشان‌شناسی اندونزی گزارش داد که آتشفشان لووتوبی شش بار فوران کرده و خاکستر را تا ارتفاع ۳ کیلومتری پرتاب کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/660365" target="_blank">📅 14:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660364">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7465c6c61d.mp4?token=cqqwiRIxdrGMi1Z8qXUDrgIPm0SDAJ_nrGVCF-K5-xMUAvuI6lkFlhEMfhB-9WpsoKghSlTonAivRObKH7KrC8GdxdTR_wlRVW0xPoLVPcuaY9790yOrGwaMAOOWJpNIkXYlzV48Bm94IpPwb3Ft8_GN5ZVw_cURLBDihxVvXzemFhYvtoBt4XOSs4E4Ir5EsFnmXMfpmMzV6yyXrC0LHzbRX5fs9DrAFrbWVY3DHI_eYoI22S2d4Gtn7H1wwwIQ7H-Np5CgZQ2-hwFC9o-jvtXVFFTgk2X3Bq7xEpQGQlZeUjgAvPLPAkya2fiqL2twHmq4oP6Hb3pmXSHF4rJ0r72D_ZNuLPUmoJBADjTUU1L_oSinl7r-sa62UzNcWfahsP1GAyVQBIWLqaUs4pcQCnTiTSIxT8a4DlUF-U1FdkMrLf8rAVKVerolv6CCO-TYYWzahf6_asLNFwuPlIPSNNOUEXT92YA7PDkEBRBhf7y7AEhbs0z92rtnA9_knUyGPWqhMh0cVFLBYuszLKfMsVcHjh4zf3z_-0nf3ciOy8CVwwWTzFYGbE6kLd3d4LEU6cY1GGTKq9UEgbexR0B5TcPp1DNtRW5dfA_IuQORGze7bfy9KOYl4-Tz9gyYGtx8cW687nRP19he6YK4CQTOLQGNWBn1oXPV19O6er6oLSE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7465c6c61d.mp4?token=cqqwiRIxdrGMi1Z8qXUDrgIPm0SDAJ_nrGVCF-K5-xMUAvuI6lkFlhEMfhB-9WpsoKghSlTonAivRObKH7KrC8GdxdTR_wlRVW0xPoLVPcuaY9790yOrGwaMAOOWJpNIkXYlzV48Bm94IpPwb3Ft8_GN5ZVw_cURLBDihxVvXzemFhYvtoBt4XOSs4E4Ir5EsFnmXMfpmMzV6yyXrC0LHzbRX5fs9DrAFrbWVY3DHI_eYoI22S2d4Gtn7H1wwwIQ7H-Np5CgZQ2-hwFC9o-jvtXVFFTgk2X3Bq7xEpQGQlZeUjgAvPLPAkya2fiqL2twHmq4oP6Hb3pmXSHF4rJ0r72D_ZNuLPUmoJBADjTUU1L_oSinl7r-sa62UzNcWfahsP1GAyVQBIWLqaUs4pcQCnTiTSIxT8a4DlUF-U1FdkMrLf8rAVKVerolv6CCO-TYYWzahf6_asLNFwuPlIPSNNOUEXT92YA7PDkEBRBhf7y7AEhbs0z92rtnA9_knUyGPWqhMh0cVFLBYuszLKfMsVcHjh4zf3z_-0nf3ciOy8CVwwWTzFYGbE6kLd3d4LEU6cY1GGTKq9UEgbexR0B5TcPp1DNtRW5dfA_IuQORGze7bfy9KOYl4-Tz9gyYGtx8cW687nRP19he6YK4CQTOLQGNWBn1oXPV19O6er6oLSE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آیین عزاداری خاص و دیدنی نخل‌گردانی مردم آیسک خراسان جنوبی در حسینیه معلی شبکه سه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/660364" target="_blank">📅 13:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660361">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff0572683.mp4?token=QI1udps1yf7TLfAvqV1d6O-aUbXcr9cRZdnmsS_XK-Yy6V19qZqr5XR-VcrBpJFBKPKg7KsjfiNMgv9V9TUuRuzbv_2LGNO-rm9U_NW_nuHty3Q0QEAC9SaElh7j8AeougLHj6oJB_zwnvblYRQokpATYrVarCBMkdk5PrEzDawPNt-e5L4aaioCwyl79WrS9WB7qZ_yoDZVC4TMW7DdOcfR4cAq7gxPfoMkFuxgHKHWKT5EFFXjvkAYWFEJN9XGEAEbIQnh17AeiOcjpys-s5ne8KLbgD8y_ibwXzhudj_TlgizYcvBRaoOFJ5TsNsLABVvXl6NHXnexkN9Z8jBUQObMjVEG5A0F9nwCWmhjEI1v0O938jU2u0XA4P7mB50dnlEFlMooYTKM4zIO4Fa9F19NXqYoQ1vPFiMD9HfKGXvBBio03hkyBiRLc1D_sgvEhi9Jvi0v2br3j3Poz4Rp7hj0YMmzUy79_EKNXh7kZSaFZ-5wRFZ2mz8y9OmUfHQqWB0JL5UpbUPP7kqe1l-Ym9r4v8URIbGLDqRt9Eq52bO8yHuieCLxZXSGz1OlmZhwO4N-dH4roBt5wvji6TAcfIAzPhYs6yFz9oGD2QZNrCFGoq8QyccVZp4bhKk_2xWoqjJ4JBVbrjusVEevQ9vwmHYAjjh2ilJkheTrcq96G0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff0572683.mp4?token=QI1udps1yf7TLfAvqV1d6O-aUbXcr9cRZdnmsS_XK-Yy6V19qZqr5XR-VcrBpJFBKPKg7KsjfiNMgv9V9TUuRuzbv_2LGNO-rm9U_NW_nuHty3Q0QEAC9SaElh7j8AeougLHj6oJB_zwnvblYRQokpATYrVarCBMkdk5PrEzDawPNt-e5L4aaioCwyl79WrS9WB7qZ_yoDZVC4TMW7DdOcfR4cAq7gxPfoMkFuxgHKHWKT5EFFXjvkAYWFEJN9XGEAEbIQnh17AeiOcjpys-s5ne8KLbgD8y_ibwXzhudj_TlgizYcvBRaoOFJ5TsNsLABVvXl6NHXnexkN9Z8jBUQObMjVEG5A0F9nwCWmhjEI1v0O938jU2u0XA4P7mB50dnlEFlMooYTKM4zIO4Fa9F19NXqYoQ1vPFiMD9HfKGXvBBio03hkyBiRLc1D_sgvEhi9Jvi0v2br3j3Poz4Rp7hj0YMmzUy79_EKNXh7kZSaFZ-5wRFZ2mz8y9OmUfHQqWB0JL5UpbUPP7kqe1l-Ym9r4v8URIbGLDqRt9Eq52bO8yHuieCLxZXSGz1OlmZhwO4N-dH4roBt5wvji6TAcfIAzPhYs6yFz9oGD2QZNrCFGoq8QyccVZp4bhKk_2xWoqjJ4JBVbrjusVEevQ9vwmHYAjjh2ilJkheTrcq96G0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تالش زیبا، گیلان
🇮🇷
#ایران_زیبا
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/660361" target="_blank">📅 13:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660360">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0T-Cj8gbVOEq0BOXL_6ZjRHXEZO5bC6bTfSwwtNbYhUG9piAgEe0srTJpUW16R3W2aqiJrjR6m9d_wq4KWrWfj_mmFEmJRjqjxaOQAr6bbY-r2xMlf0Wyk7iNBSPz6Gd4bvvgJ2Dj7oKWkWqfr8B_-TFgby_s-xqPE1qGeIYSBwIOqJJ8XPoI14bFtwDHfyDbbdTtWM7ugowcQN5sNtKYyB-boqFS1R9LN1hXfK1ngxq6Qpfj5_thTU_negJrUk63l3d0MVGixh5T2uGRhn2HuIE3KZ-vIssYkfXvk-XB98W3v6St4Xm34yyzjc80Ran27DYKPAYVt6kHGZ46SRUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۷ خرداد ۱۴۰۵؛ ساعت ۱۲:۵۵
🔹
قیمت دلار امروز پس از چند روز ریزش پیاپی، کمی افزایش یافت و به ۱۵۷ هزار تومان رسید.
🔹
این رشد هزار تومانی در حالی ثبت شد که دلار طی روزهای گذشته بیش از ۲۲ هزار تومان کاهش قیمت را تجربه کرده بود. در مقابل، یورو همچنان در مسیر نزولی حرکت کرد و به ۱۸۰ هزار تومان رسید.
🔹
رشد امروز دلار بیشتر یک اصلاح مقطعی پس از افت‌های سنگین اخیر است و هنوز نشانه‌ای از تغییر روند بازار دیده نمی‌شود.
🔹
به نظر می‌رسد آینده بازار ارز همچنان به روشن‌تر شدن جزئیات توافق و اثر آن بر تجارت خارجی و تحریم‌ها وابسته است./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/660360" target="_blank">📅 13:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660359">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
از تسلیم ایران می‌گفتند اما حالا از قدرت ایران حرف می‌زنند!
پروفسور جفری ساکس، اقتصاددان و تحليلگر سیاسی آمریکایی:
🔹
آمریکا نتوانست ارادۀ خودش را به ایران تحمیل کند چون ایران دارای ظرفیت نظامی قوی و پیشرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/660359" target="_blank">📅 13:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660357">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3219a1fd4.mp4?token=kWYXydlRozJVSL-32h7FxSPNx-8TrNNLUrSKM7_g7hs0JYxg1BVnLjBTmJdDUUl23MXAOsJOutHabnLsxl4nPpXcDMYrL0blYayrQBRt02l1xcCBzDwXNGKIBZpeAQ-7YyAemjSAMH-INqHJITjDWKSTAynzvXNysYty1MCKZ8xzBkdq7Gh5YX39S_BOMRomCD1tPKkfirir-4oi9LHkFkdKxjpf2AYMSNH9zRqn6XXRxhADrJ_dGTzBv_LzgPw33lwZ0ZaOPe-vqXw2OXyX-BTViG72eQ7eSFgtmucEbuDASto8tkhatOaXuB_Boz5yg0-sO2dzS4V5DgSgjxtSQndh81b74ITLklcJlrM2Og0SECD7AwbtFSCi7YipYLxtZ2OjcH3z8J-7aarW7TDeO4Vtv8gd_8hFV8I9RX1T2pAXJOkho2-XNBto6QxzNVANDI6EzwbNyX4m5lGJ3mramguMSClV-FbmJH2qKDjRDLz_T7mhR9QDVhByzrkdcWnoH1Y2w_UI3jIrjC2BmGR5SPyjXNfXGz7GH6JtNntGHVgJLKOanbvnYjvErx47U-biHMLUpcaGWpcBNn8F3C429uWWpKQEtXpM_qx5tc0VDyuB177bj9SePws1t2iZn_YESGWyLiflZR-j_BGZljQ1VKpCIHkbkQedvHKQ4gVtgcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3219a1fd4.mp4?token=kWYXydlRozJVSL-32h7FxSPNx-8TrNNLUrSKM7_g7hs0JYxg1BVnLjBTmJdDUUl23MXAOsJOutHabnLsxl4nPpXcDMYrL0blYayrQBRt02l1xcCBzDwXNGKIBZpeAQ-7YyAemjSAMH-INqHJITjDWKSTAynzvXNysYty1MCKZ8xzBkdq7Gh5YX39S_BOMRomCD1tPKkfirir-4oi9LHkFkdKxjpf2AYMSNH9zRqn6XXRxhADrJ_dGTzBv_LzgPw33lwZ0ZaOPe-vqXw2OXyX-BTViG72eQ7eSFgtmucEbuDASto8tkhatOaXuB_Boz5yg0-sO2dzS4V5DgSgjxtSQndh81b74ITLklcJlrM2Og0SECD7AwbtFSCi7YipYLxtZ2OjcH3z8J-7aarW7TDeO4Vtv8gd_8hFV8I9RX1T2pAXJOkho2-XNBto6QxzNVANDI6EzwbNyX4m5lGJ3mramguMSClV-FbmJH2qKDjRDLz_T7mhR9QDVhByzrkdcWnoH1Y2w_UI3jIrjC2BmGR5SPyjXNfXGz7GH6JtNntGHVgJLKOanbvnYjvErx47U-biHMLUpcaGWpcBNn8F3C429uWWpKQEtXpM_qx5tc0VDyuB177bj9SePws1t2iZn_YESGWyLiflZR-j_BGZljQ1VKpCIHkbkQedvHKQ4gVtgcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شارژ به سرعت پر کردن باک بنزین
🔹
خودروساز چینی بی‌وای‌دی (BYD) از فناوری شارژ جدیدی برای ماشینهای برقی رونمایی کرد که سرعت آن به اندازه بنزین زدن است‌.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/660357" target="_blank">📅 13:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660354">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
اینترنشال: ترامپ مجبور شد امتیازات زیادی به جمهوری اسلامی بدهد؛ یعنی کمپین فشار حداکثری، تحریم و... کشک!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/660354" target="_blank">📅 12:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660352">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSExtEa_sjIbAeosB6NPRxib5kpBf7grRknZRJtIQLC397sMA5bnKKs1ozFMCOTbyjW16EUxsmXLCYDHNSPKdxztG4S9XQq8STuKyG34bNLGRuGH1gFiHtGjQlunkH0Nx_mZNkLVfXyiD6ezAnnHdVkSbX42yjs9kARjJ54ukP1fgx1NuZD2tWxwlXzZWLjSbNfCejXDtfNVqKwNpVPCx4YMe2NL1PKS5uzkTkSreMnOkldAzH3r-d2XMjZXvaWg1bBW-GGaGd2stS7E-r68UHAZ1GRwrC_RqW9dkyY4pTJAv22IFrDUoe_Oxq4-OOrk4mIg5mxLWu69QlaHTnXrcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رشد بیش از ۵۰ هزار واحدی شاخص کل بورس
🔹
در جریان معاملات امروز شاخص کل‌ بورس با رشد ۵۰ هزار و ۸۳۳ واحد در سطح ۵ میلیون و ۱۵۱ هزار واحدی ایستاد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/660352" target="_blank">📅 12:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660351">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hb9RkvnixgQj_xvSnFEqVpY7UI8AZV-pTrjw4Mn42Nr-nS0iu0wOSnXxwbDOFqP45cIGrdQxnIaV4fB278mKI5FTcDQKE9oMvl5EDcyXfPC7nzw86XwVyJjKNgTXsJ1xLBcp4Xd4MJLkUZGYFU0C9YcDHXqnbjSd7___wNu4VALIddOutSTc7V_BRKH-snLBCJpm24tr-dCedz2Uh8Y0WBhSBnyDhfzxzkB5zDS0lPvJr9Fyj90LLQ8d06nuIJ6YlLOKvV6JIVE7GCy00NcZ1ZMYG1pOGgxH6Bj8Qa02atLBlBi0dJ1d3jh5bEwu3otlC5NQJcEXLJQGqamn3FvStA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش قیمت محصولات ایران خودرو و توقف نماد این شرکت در بورس
🔹
مدیرعامل ایران خودرو در نامه‌ای به سازمان بورس، ضمن اعلام تصمیم هیئت‌مدیره برای افزایش قیمت محصولات، خواستار توقف نماد معاملاتی این شرکت تا زمان اعلام رسمی نرخ‌های جدید شد.
🔹
هدف از این اقدام، حفظ منافع سهامداران عنوان شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/660351" target="_blank">📅 12:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660350">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/90e6a34dfc.mp4?token=rSX9Ym1zJ5jQ5NVLXjP8PLn0Efqy2_KXYD7sN7wDKjHhwoz8nD5XDQdNh1x2yzqz0UWk8Mau5oBdgwSlkRMJvqcyX3Jr3RgE1Cr9PN5bDGxEgBG1Nm6r4B8gs8qVeNfw-o25at_8c-jHrGltCCddOqRv9ycYNfcHkeRg-gew-CZV_-ZVC3UrshkTwpdfvNujKNwCgxFRVV8RCect_GGxvVzwWVoAF9nb9VfDfbK3Aw0C6LJqUmW_aK_-zbsYxh0DtQXPOZXHv2mBmQO8Dtbn36Ur5IYPwpvzz_Y1HL9Ga7oJakMXxSdVIvbUg_E9rEaeQbq8baR0MEwYgFSaC9brfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/90e6a34dfc.mp4?token=rSX9Ym1zJ5jQ5NVLXjP8PLn0Efqy2_KXYD7sN7wDKjHhwoz8nD5XDQdNh1x2yzqz0UWk8Mau5oBdgwSlkRMJvqcyX3Jr3RgE1Cr9PN5bDGxEgBG1Nm6r4B8gs8qVeNfw-o25at_8c-jHrGltCCddOqRv9ycYNfcHkeRg-gew-CZV_-ZVC3UrshkTwpdfvNujKNwCgxFRVV8RCect_GGxvVzwWVoAF9nb9VfDfbK3Aw0C6LJqUmW_aK_-zbsYxh0DtQXPOZXHv2mBmQO8Dtbn36Ur5IYPwpvzz_Y1HL9Ga7oJakMXxSdVIvbUg_E9rEaeQbq8baR0MEwYgFSaC9brfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
مسی از سه گل آرژانتین چهار تا زد، فرانسه هم تخمه‌های کل جام رو تو یه بازی تموم کرد؛ فینالیست‌های دوره قبل اومدن که یادآوری کنن هنوز مدعی‌ان!
🔹
تماشای خلاصه بازی این دو تیم
🔹
قسمت چهارم برنامه جام تایم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/660350" target="_blank">📅 12:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660349">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
رد ادعای بلومبرگ درباره جزئیات تفاهم‌نامه اسلام‌آباد
🔹
یک منبع نزدیک به تیم مذاکره‌کننده ایران، متن منتشرشده در بلومبرگ از «تفاهم‌نامه اسلام‌آباد» را غیردقیق و ناقص خواند.
🔹
وی تصریح کرد جزئیات مربوط به بند اول و مسئله تنگه هرمز در گزارش بلومبرگ اشتباه است و برخی کلیدواژه‌های اصلی در آن نیامده است. طبق اعلام این منبع، متن کامل این تفاهم‌نامه ۱۴ بندی، پس از امضا در روز جمعه منتشر خواهد شد./ تسنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/660349" target="_blank">📅 12:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660347">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31b02ba16c.mp4?token=C-5ub7S58N_jBfZCDQxjjpK_ctqnmqydgkR5Qmn_S2S1bi_wVfEeUrt1lz6hJxggpZcktvo9WNnRnpc27Vb9T3MWhfpsyW6po8_TpLRLFRp97fmbTvD5y8fx1HReVRV5UerEQo_Y7HEbvkEfs0FLHb_7cybgrhcVxYx_ZWQthy44uNQ4ber8SANkhmfntJIZM2Q1uWZKl9vl7beAbteDvjSc_wO5q5UeQCivS4lvI4yDaLxnZGbdK9DGhfedf6DIEC-3_KZHEjHv0cv17Xw3Wc7M5aamIYsKdrtByfoC2fNGZ3JsfYQ4wRj4MNvLkSXOUaEmU9nzsFj-2p__Qd9gzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31b02ba16c.mp4?token=C-5ub7S58N_jBfZCDQxjjpK_ctqnmqydgkR5Qmn_S2S1bi_wVfEeUrt1lz6hJxggpZcktvo9WNnRnpc27Vb9T3MWhfpsyW6po8_TpLRLFRp97fmbTvD5y8fx1HReVRV5UerEQo_Y7HEbvkEfs0FLHb_7cybgrhcVxYx_ZWQthy44uNQ4ber8SANkhmfntJIZM2Q1uWZKl9vl7beAbteDvjSc_wO5q5UeQCivS4lvI4yDaLxnZGbdK9DGhfedf6DIEC-3_KZHEjHv0cv17Xw3Wc7M5aamIYsKdrtByfoC2fNGZ3JsfYQ4wRj4MNvLkSXOUaEmU9nzsFj-2p__Qd9gzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متن توافق با ایران را به نخست‌وزیر کانادا نشان داده است
مارک کارنی، نخست وزیر کانادا، به خبرنگار CNN:
🔹
او یکی از معدود افرادی است که یادداشت تفاهم بین ایالات متحده و ایران را دیده است.
🔹
این متن می‌تواند ساختار خوبی ایجاد کند و تغییر دهنده بازی باشد؛ توافق جدید ساختاری است که کشورهای منطقه از آن حمایت می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/660347" target="_blank">📅 12:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660346">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fba406a50a.mp4?token=LGOc-2G6juopdyAmfIxtYFyX0115MGn7LlXba9aKgyfguxRS6MBhLeOoyNRiyLglc4PQnzKxS_Q5xq6ZbhQ-JB7pMEhRKtrQ5qxKkWSkhH8JP45RWS-nQyLAXPoEE8f0I9Cd4ZnMEzxqkaD9MOdQCWiwoiogT99TnCmhBgIk95jSxBcpwdKZuqdtagu7hvolgBgKCnoOMkyO-D9Dk-PHGdolSx06A2CVFp3QGo4E-V81-tK3th5EUKQuxwy1hUKSVSnobL3tZs_wwk-C2MCRf_0nrGmLlZmF3y0nGm5TCfTybrpgVRXTGRHbsM4dtY_HOc7r8z85UXutKzSCsBYOMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fba406a50a.mp4?token=LGOc-2G6juopdyAmfIxtYFyX0115MGn7LlXba9aKgyfguxRS6MBhLeOoyNRiyLglc4PQnzKxS_Q5xq6ZbhQ-JB7pMEhRKtrQ5qxKkWSkhH8JP45RWS-nQyLAXPoEE8f0I9Cd4ZnMEzxqkaD9MOdQCWiwoiogT99TnCmhBgIk95jSxBcpwdKZuqdtagu7hvolgBgKCnoOMkyO-D9Dk-PHGdolSx06A2CVFp3QGo4E-V81-tK3th5EUKQuxwy1hUKSVSnobL3tZs_wwk-C2MCRf_0nrGmLlZmF3y0nGm5TCfTybrpgVRXTGRHbsM4dtY_HOc7r8z85UXutKzSCsBYOMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیدحسن خمینی: ۳۹ روز گذشته جهاد اصغر بود؛ از امروز جهاد اکبر شروع می‌شود؛ باید از نزاع‌های بی‌حاصل دست بکشیم
🔹
واقعا باید از نزاع‌های بی‌حاصل که نتیجۀ منیت‌هاست دست بکشیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/660346" target="_blank">📅 12:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660345">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUAxzlkrEITZ8zFxwFjFWwwl6bU0b4O9pdj0_bw4cp4oTBY8dp1GOkMFX-YYYatMrintd7xF16dsSfSt1T8uA3fc9Xw_OAzBbvPvxpo9LMI9ZD9_beCH6Iinn1PatQbeophGwmj0E3gBgn0ObnNXfBSJPdzI5Xo-iaipjWTGTR9dT4-LQDv6MXdWBCZJhKl2juMEfGMRU_ACgpjoFV6I1EMKRkcCRA86yVAf3RGr9LyWEHLstZwZYuKPd0roN-bkbLZEUbHW6fCXdsuiVmZFHc9E6CnUNzK9xaHpxpE9vBvCbPgCY1oQronLLMJdQwLovoQ1Tv8XU0E3kdigA4KMew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست اینستاگرامی مهدی قایدی پس از اولین بازی در جام جهانی
🔹
لحظه‌ای که سال‌ها رویای آن را داشتم، سرانجام به واقعیت پیوست.افتخار می‌کنم که نماینده کشورم هستم و در کنار هم‌تیمی‌هایم می‌جنگم. قدردان تمام کسانی هستم که در این مسیر من را حمایت کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/660345" target="_blank">📅 12:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660344">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6NRWFXw0oyraTohEnRXtFjG1uJ_x_wkNXn2VwADT05v0yLNwugxpUxs6sc44SpFVHifKuxInlLS6TbPpDyaz9vYf7n_RWqufbCayy3oFyL02kAKeiIJ7Nahdc8_Z7DL11ILUdRt3D5_AQM4C0y5RlnkFCeL-N07iZctWh5KJRLry7oSKUXSpX77uu-gs_He6OxTwbdG-rgwShlHbtUkUbNzJrwYnJlrYm9_Is-fRcZHIPgs_bAw1dcbVI5iGrRmvEgM1HpOuqXoS7nScyJziJzXgSlB2AW0vRVbcSqA11-9evD5HFmi3P5_IqnPvho77UNeqZ4jhQs08XW4iLjfRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فیشینگ چیست و چگونه اطلاعات بانکی شما را به سرقت می‌برد؟ #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/660344" target="_blank">📅 12:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660343">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
اتفاق قابل احترام و عزتمندانه در تلویزیون عراق: پخش سرود ملی ایران و ادای احترام نظامی‌به کشورمان توسط کارشناسان ورزشی عراق!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/660343" target="_blank">📅 12:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660342">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6655fd79.mp4?token=ah8jQHuupSNUTe5LdstzPv0VlH4SjqyAWQIkF0dHBWY-Q6hB8Zr1Pvw3TjFsUyEXF0NRQhk6UbdYe_zwpb07B5dHQwtEBRDm2-XJXq6tohGAlBkcxFTr2sVRuVo3Z0NeIPhDc37OyGmvnEuGx3mw7MQZskBpVZpP12mkB7y9FqpPUOP4VEAbo4NVLG4GJg793-ubMREOmUQfVBCYtnPJgz8XJGV2a3voOBCMufNLEkXQ9gvZcTOzN-CGzdjYxkq0fJ59aerUpmwxuzw0Jut6iwE5wmyruoOHzjkS81ZcAWrPg5-WE6UvmcEVsGf1I-ZhG8F2O0T8aGaFqTKsUA2J3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6655fd79.mp4?token=ah8jQHuupSNUTe5LdstzPv0VlH4SjqyAWQIkF0dHBWY-Q6hB8Zr1Pvw3TjFsUyEXF0NRQhk6UbdYe_zwpb07B5dHQwtEBRDm2-XJXq6tohGAlBkcxFTr2sVRuVo3Z0NeIPhDc37OyGmvnEuGx3mw7MQZskBpVZpP12mkB7y9FqpPUOP4VEAbo4NVLG4GJg793-ubMREOmUQfVBCYtnPJgz8XJGV2a3voOBCMufNLEkXQ9gvZcTOzN-CGzdjYxkq0fJ59aerUpmwxuzw0Jut6iwE5wmyruoOHzjkS81ZcAWrPg5-WE6UvmcEVsGf1I-ZhG8F2O0T8aGaFqTKsUA2J3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شروع طوفانی فینالیست های دوره قبلی جام جهانی/خلاصه بازی جذاب فرانسه سنگال و آرژانتین الجزایر
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/660342" target="_blank">📅 11:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660341">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcfQKVb2zfWUQigvxHhbfIJpREvvubPEWDx1fmTKUOxH1KJjEuCQGoZf0nY8w8xjSiPD5gIBJsXVrgfmGPhLS9TRRdLeW_svngfC--R3P-Hr97rtZKHhmD8iIyinaR8wUB1co1w-hwwWXDmMr6V1amf_3sP6RUqFFUyXnNYaOppSn7kvJQVq4jiEabJRy1EmKXb6JDS6sEQYzMqWnUUqM3e-RukQ_4t7b4n085WoKnBX3_IndqNO2rV_pnsgusfuxug7hLwmPRn1AQQft1CSNmUFGISK9NmfOxVNUfU3Hoz7odEyziDec3iC_Z-STqvK0E2rXMJJzQ8WV2hu5y6_Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در بریتانیا به‌زودی استفاده از ۱۰ شبکه اجتماعی معروف برای نوجوانان زیر ۱۶ سال ممنوع خواهد شد: تیک‌تاک، یوتیوب، اسنپ‌چت، اینستاگرام، ایکس، ردیت، فیسبوک، توئیچ، کیک و تردز.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/660341" target="_blank">📅 11:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660339">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006b6f0f1e.mp4?token=C2f_O-qrASsDQYlsSq1buPu-ZuXAp0xzHh91xdnsC63MO2aULT7F5Ot014Mnl9MWRiPhp4_HHdeI7dHBzTukqSYns18wYrwYdK_Nc5G3oyB0dzM6FdaJPxg-JPeyUCc5IyN8TwSnH4iO1PKUmu_Mp2twuycmrzq8wJanXIa1MFooPXMp9O7lBHKJ03olEA67ldGTdnpeN4n5kXE0gPiEH16scMPfuC2uGFj3vdvebXWTk-NaJtoHCYBvA5Oeozw44AqoR_KU_zsPyPJlAsWOr0KrHlxk1hyTk1AzVUSiZ0UDVy2jLwE9WIdY-ZpBJ87K_Kj7lvB4Ayrpiq9fTyIiBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006b6f0f1e.mp4?token=C2f_O-qrASsDQYlsSq1buPu-ZuXAp0xzHh91xdnsC63MO2aULT7F5Ot014Mnl9MWRiPhp4_HHdeI7dHBzTukqSYns18wYrwYdK_Nc5G3oyB0dzM6FdaJPxg-JPeyUCc5IyN8TwSnH4iO1PKUmu_Mp2twuycmrzq8wJanXIa1MFooPXMp9O7lBHKJ03olEA67ldGTdnpeN4n5kXE0gPiEH16scMPfuC2uGFj3vdvebXWTk-NaJtoHCYBvA5Oeozw44AqoR_KU_zsPyPJlAsWOr0KrHlxk1hyTk1AzVUSiZ0UDVy2jLwE9WIdY-ZpBJ87K_Kj7lvB4Ayrpiq9fTyIiBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرقت از یک بانک با بیل مکانیکی در انگلیس
🔹
سارقان با یک لیفتراک تلسکوپی شبانه به شعبه بانک در کمبریج‌ شایر رفتند و دستگاه خودپرداز را از دیوار کندند. پلیس اعلام کرد لیفتراک هم سرقتی بوده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/660339" target="_blank">📅 11:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660337">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 مسابقات جام‌جهانی ۲۰۲۶ را از چه طریقی تماشا می‌کنید؟</h4>
<ul>
<li>✓ شبکه سه صداوسیما</li>
<li>✓ پلتفرم‌های نمایش خانگی</li>
<li>✓ شبکه‌های ماهواره‌ای</li>
</ul>
</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/660337" target="_blank">📅 11:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660335">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/263955c247.mp4?token=JVbZD5Gdm1qB6PC9tgyPGmcOd_3JSPsXN_sLFjHRvq4-6VkNVou1jPN4qqIE5VUsb_Ji7tE4pWPAk4FcNcN9V4ps1JwT5x-zMVzmGg6mpWFvGNUQ19Ha7CEmsigRGcj_GPC4naGjD3ERLGZWzVuChJW4S0uqcrlKqYvVFlrzD2Pi1W1YU5HPTEqiYKKX9FoT1Tlj-xjVOObd_HNPnrjQH3m99aHmSqAy9YezYgn_hypz1mgDX19wSIDziJuIjd6Mg8yx6YO5ISa4JCmm0kiAhuDOYNEqYbE8NXqZUwnMa4gUUnkNZunvJqbNCkUIpWsTp0o3TmNEsfm4FHRTjBWH2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/263955c247.mp4?token=JVbZD5Gdm1qB6PC9tgyPGmcOd_3JSPsXN_sLFjHRvq4-6VkNVou1jPN4qqIE5VUsb_Ji7tE4pWPAk4FcNcN9V4ps1JwT5x-zMVzmGg6mpWFvGNUQ19Ha7CEmsigRGcj_GPC4naGjD3ERLGZWzVuChJW4S0uqcrlKqYvVFlrzD2Pi1W1YU5HPTEqiYKKX9FoT1Tlj-xjVOObd_HNPnrjQH3m99aHmSqAy9YezYgn_hypz1mgDX19wSIDziJuIjd6Mg8yx6YO5ISa4JCmm0kiAhuDOYNEqYbE8NXqZUwnMa4gUUnkNZunvJqbNCkUIpWsTp0o3TmNEsfm4FHRTjBWH2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هوادار متفاوت آرژانتین در کانزاس
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/660335" target="_blank">📅 11:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660334">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
افشای استفاده از هوش مصنوعی گراک در حملات متجاوزانه آمریکا علیه ایران
خبرگزاری فرانسه:
🔹
گزارش حقوقی دولت آمریکا نشان می‌دهد ارتش این کشور از ابزار هوش مصنوعی گراک متعلق به شرکت اسپیس ایکس تحت مالکیت ایلان ماسک در جنگ غیرقانونی علیه ایران استفاده کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/660334" target="_blank">📅 11:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660333">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
شرایط جدید بازنشستگی تأمین اجتماعی
🔹
سن بازنشستگی مردان به ۶۲ سال و سابقه لازم به ۳۵ سال افزایش یافت.
🔹
زنان با ۵۵ سال سن و حداقل ۲۰ سال سابقه می‌توانند بازنشسته شوند.
🔹
مشاغل سخت و زیان‌آور، رانندگان و زنان دارای ۳ فرزند یا بیشتر، امکان بازنشستگی زودتر دارند.
🔹
تغییرات به‌صورت پلکانی بر اساس میزان سابقه (کمتر از ۱۵، بین ۱۵ تا ۲۸ و بیش از ۲۸ سال) اعمال می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/660333" target="_blank">📅 11:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660331">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
۳٠
شهروند ایرانی از پاکستان به کشور بازگشتند
🔹
طبق اعلام وزیر خارجه پاکستان محمد اسحاق‌دار، با کمک این کشور ۳۰ تبعه ایرانی به شامل خدمه یک کشتی توقیف شده توسط آمریکا به ایران برگشتند./تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/660331" target="_blank">📅 11:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660330">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0632de855e.mp4?token=Lkqq_-MnRF8dqihTD2iXELcn356xFXLiUBq9eBg5oNF6CwqFw_-kZ70qiKk4Pd-trYDaXwcgilkStCgg-Pd2WSXapy-p9HDEI7ImQNijAVL0QAbbu2NM-G54y01IYKmIFieEi4VJTIbNGAsn1L7Inbpc3yZoJBEGt_ZCek-IEB_78kzMTf6fVhHVSG0PPrw7mi2xWsc5tyWQ32Jm1M-AqfBpz7WR_2Db9Sov6ZF4jFbMcgjgNtkvvapIRamVGeKCXslkeqvAdLwHbUfYoUrd39kYlX_343UI2BFliLVz6C7X1TTZN2dhCA50WMw-SekUVp-YbMyUAspWwrtMF9rlNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0632de855e.mp4?token=Lkqq_-MnRF8dqihTD2iXELcn356xFXLiUBq9eBg5oNF6CwqFw_-kZ70qiKk4Pd-trYDaXwcgilkStCgg-Pd2WSXapy-p9HDEI7ImQNijAVL0QAbbu2NM-G54y01IYKmIFieEi4VJTIbNGAsn1L7Inbpc3yZoJBEGt_ZCek-IEB_78kzMTf6fVhHVSG0PPrw7mi2xWsc5tyWQ32Jm1M-AqfBpz7WR_2Db9Sov6ZF4jFbMcgjgNtkvvapIRamVGeKCXslkeqvAdLwHbUfYoUrd39kYlX_343UI2BFliLVz6C7X1TTZN2dhCA50WMw-SekUVp-YbMyUAspWwrtMF9rlNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکت فرهنگی عراقی‌ها پس از بازی با نروژ؛ متشکریم بوستون!
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/660330" target="_blank">📅 10:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660328">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a63a7346fc.mp4?token=CQQVTc02iL1KO5VpPlg8vYAycHWbxyUpChkjPsAa-R3kVnSPKu41GdxoW7a0d8xAVAjjKivdJkjGTFLFwswQDtbT5n-rpQRv9MRlWpPKR5-7HZ2vbiU94uKFktqqrxwtqW-3lvclZnNvFHXQL5rItQPUuKe1jK4IqmbGrzsfSRrowpwyxqPXqcEZeO6SbG3spx8vlTCYvHhPUvd9dlLdSKaZnKcgL0ZvUKnk2T5NynvQ_WDqC4wdcpzIN6tGSeoUvhvQYLVfXmYn0gF9QOi6p0aZt1cU36spdfY8Cu9zUFRMOPdm_ayEoXEFjAWRZiobdUlzgX1_V4_eV8wtDA5cxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a63a7346fc.mp4?token=CQQVTc02iL1KO5VpPlg8vYAycHWbxyUpChkjPsAa-R3kVnSPKu41GdxoW7a0d8xAVAjjKivdJkjGTFLFwswQDtbT5n-rpQRv9MRlWpPKR5-7HZ2vbiU94uKFktqqrxwtqW-3lvclZnNvFHXQL5rItQPUuKe1jK4IqmbGrzsfSRrowpwyxqPXqcEZeO6SbG3spx8vlTCYvHhPUvd9dlLdSKaZnKcgL0ZvUKnk2T5NynvQ_WDqC4wdcpzIN6tGSeoUvhvQYLVfXmYn0gF9QOi6p0aZt1cU36spdfY8Cu9zUFRMOPdm_ayEoXEFjAWRZiobdUlzgX1_V4_eV8wtDA5cxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رونالدو رو هم توی آمریکا اینجوری گشتند
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/660328" target="_blank">📅 10:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660327">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mpf85ITJjYPuOCXSXb02kbU18BdA2bac6fV51UHpgHvbEYydw2fGHMh7yA4kwHA--CvNbVEa1tKLF-5Uh5fenm9mAUzDQaMoyDH2HICSDo6Tl5gJJPiXim7esbAfbhDR7RjjNG7GErsM40XRXbJjqtZsnnjw-QJBfdyPyfiYEIzh1g1s9xLvd9GNyCDwGMWywQOCL4EXGLTrkNJO-SInO7TUjgBJkDQ2A16wHohs9wJAzH_4PbRTtdVu8Spto9xw0jZFCK31eLPSREmgThoQFpgacf-nl2tdHGFFtM-v2rSJcBUsM0ZmfDzgx6pcTWxCzo2lWK-lwevWYxskC1FPRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قابی زیبا از معماری بی نظیر شهر هورمان تخت کردستان
#اخبار_کردستان
در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/660327" target="_blank">📅 10:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660326">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c298afccd2.mp4?token=GVQvEASbN5JyMLBPR00H9dH3eAhqCIAGF7Dhq7KPLSO58f1CHTAnO3gBnB2aez59bmaI3WGBsIPMeTFeBkvW1eVRSDeMUXT8aYz_jEdw8mwC3vFuZ_laR8VqO5LO22P954dcvelIgr2_jwOPvQNEnoIJTghoXtGbCXR1gQ47LK-GDYcd_rW9lalD6XXYJMK4HqPl2nZ69OIiX2kWAuEd_6rmRkuCMdQZXHaQVSoRJFutB2C1nUBPWl7Q6p7WPG0hM881gBZqPanskal603pVrj14YHQAJrI8-E7j1koDuwRUmR0PMZ4hOHeJFommy9c91kN3AIVE1P82DSk9kgDQpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c298afccd2.mp4?token=GVQvEASbN5JyMLBPR00H9dH3eAhqCIAGF7Dhq7KPLSO58f1CHTAnO3gBnB2aez59bmaI3WGBsIPMeTFeBkvW1eVRSDeMUXT8aYz_jEdw8mwC3vFuZ_laR8VqO5LO22P954dcvelIgr2_jwOPvQNEnoIJTghoXtGbCXR1gQ47LK-GDYcd_rW9lalD6XXYJMK4HqPl2nZ69OIiX2kWAuEd_6rmRkuCMdQZXHaQVSoRJFutB2C1nUBPWl7Q6p7WPG0hM881gBZqPanskal603pVrj14YHQAJrI8-E7j1koDuwRUmR0PMZ4hOHeJFommy9c91kN3AIVE1P82DSk9kgDQpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینم آسون‌ترین روش پخت لازانیا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/660326" target="_blank">📅 10:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660322">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1IsgHPkNDXYK9N_RK26E0vc-dCeWRbclmgJCkUjp6faOUfZyrj1usFjUDICfYvPxcpwyl7_vV01mbVjgPU6ewZ95wfVKaEtcCVpstin7eTCJkmTMWdjQiWk9Zrq4hjFpeFCl5RHIZEXi8YVUimvo2QkErx_KY9wddHgS84HolTcsrv_mirrjsXjvzRC3X88Cm0ZTI7pqfy_VHi33-GDVoKcB2ZJrFiEEXeXFKVzJt16hi2T7VIpnMWX3Y2VH-pH6jlBVwhTgkkUzrwkTgB5a5S9YWQQO1li45PT_IiFlZ3TIyHT_XqfFoc82V1CoCkyHN5qgg-8TJsNzGeKl-zXmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدول گروه J در پایان رقابت‌های دور اول
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/660322" target="_blank">📅 10:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660320">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6971a5404f.mp4?token=rRhu46H7yOKMnej-9ZPLttvK4xQGY8abOJ67Rjg3DZGuj6A2L4glNI1NmiXquewGUmz0NE6J_M1D2Aj1IcmW_v4jFJ9939XAnO17aXoix7PgLDeKXdOH1zIPJzwYv2ku5FatbZ2xavWeZy7UgX2vgO8TQB_wqTtAMbOlfWVdHVwlrvXrFYzxn7l2vuoakC_0ZMCnOTZaTgaROoNFuL5VO-RWLG_B7bISgOXtwH_eR2z5myl4mP1Bzkq5h_IVAoufg8BZzfpsQT9zxkNFEBuoOXS2Tx_xnJwFB43EqZ_EBeB8T_PxvVt-w6WfzBigpzCABY4iyIolHRgRe_mZTFhVXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6971a5404f.mp4?token=rRhu46H7yOKMnej-9ZPLttvK4xQGY8abOJ67Rjg3DZGuj6A2L4glNI1NmiXquewGUmz0NE6J_M1D2Aj1IcmW_v4jFJ9939XAnO17aXoix7PgLDeKXdOH1zIPJzwYv2ku5FatbZ2xavWeZy7UgX2vgO8TQB_wqTtAMbOlfWVdHVwlrvXrFYzxn7l2vuoakC_0ZMCnOTZaTgaROoNFuL5VO-RWLG_B7bISgOXtwH_eR2z5myl4mP1Bzkq5h_IVAoufg8BZzfpsQT9zxkNFEBuoOXS2Tx_xnJwFB43EqZ_EBeB8T_PxvVt-w6WfzBigpzCABY4iyIolHRgRe_mZTFhVXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تفاوت استرس و اضطراب به زبان ساده #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/660320" target="_blank">📅 10:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660319">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9797c47bc3.mp4?token=HMFXqVzwkn0WGoeAkE9K3Xk3TwRuR1tfWgEplzW2iJuOLYWPLavspjffrwUFjtEI8ZL3ietXgYWHxaaBIxU08rb_222AxAbCTClIoaME8l7Z9r7nm6YlWZcJXVAxNrA76xDVa5__8VuMejUerja4MEt4oNT-9JA8oK4a7HSQsRW-H1WNSvSRmKYwRBxsOXyQX8-E16KAG4ML3fq_eg1qiT-AB-hXLBLKlj_2h0ZDsD9TM9fNDpRpQRHo8ZJObMbSLCFppGEykn3O6zngnivbhPyrMq7JzQq7x0wt-ykgbACPm6H6fbFGO-KrPv-prrO54lCVS2CVZsq2ycdqoqz0cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9797c47bc3.mp4?token=HMFXqVzwkn0WGoeAkE9K3Xk3TwRuR1tfWgEplzW2iJuOLYWPLavspjffrwUFjtEI8ZL3ietXgYWHxaaBIxU08rb_222AxAbCTClIoaME8l7Z9r7nm6YlWZcJXVAxNrA76xDVa5__8VuMejUerja4MEt4oNT-9JA8oK4a7HSQsRW-H1WNSvSRmKYwRBxsOXyQX8-E16KAG4ML3fq_eg1qiT-AB-hXLBLKlj_2h0ZDsD9TM9fNDpRpQRHo8ZJObMbSLCFppGEykn3O6zngnivbhPyrMq7JzQq7x0wt-ykgbACPm6H6fbFGO-KrPv-prrO54lCVS2CVZsq2ycdqoqz0cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لیونل مسی با ۱۶ گل همراه با میرسلاو کلوزه برترین گلزن تاریخ جام جهانی شد
🔹
او برای اولین بار در جام جهانی هت‌تریک کرد.
🔹
بازی آرزانتین و الجزیره با نتیجه سه بر صفر به سود آرژانتین پایان یافت.  #جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/660319" target="_blank">📅 09:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660318">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
رئیس سازمان فضایی ایران: پرتاب‌های منظومه «شهید سلیمانی» تا پایان ۱۴۰۵ شروع می‌شود. صنعت فضایی ایران طبق گفته مسئولان فعال است، آسیب جدی ندیده و خدمات ماهواره‌ای بدون وقفه ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/660318" target="_blank">📅 09:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660317">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02a91c6e03.mp4?token=Q2sJZsZE5BSAL2TFZqhFTgBmeeoHopAiiq8Fbft01Doib045lE47WpnoPe6wHqwRyIMLUKuWveAp2h1uSx6cxHvloj33nVujk5wfkzmymqfO40nnGBve9cZsIJlqKMbBwhENE_uh1m6I4pxidxCOv2f73dyUB7BpiAuhii-HaqcC64dDcf2tu_xQe-B8qK-2BM2VZ_s06UYvN61-Hz6P1P1WUCuWAKCGZ43kOOZFwqm07AvkUsYivZpB_QTYy6bR4uKzsnHAqI_h5YJvRuUSZ2cSujxxKfxfKFtVqYzbeo_Df9Q0THKLSIClG9pg-Fzk2mRvkoMOSfJ-m8Ppg9igHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02a91c6e03.mp4?token=Q2sJZsZE5BSAL2TFZqhFTgBmeeoHopAiiq8Fbft01Doib045lE47WpnoPe6wHqwRyIMLUKuWveAp2h1uSx6cxHvloj33nVujk5wfkzmymqfO40nnGBve9cZsIJlqKMbBwhENE_uh1m6I4pxidxCOv2f73dyUB7BpiAuhii-HaqcC64dDcf2tu_xQe-B8qK-2BM2VZ_s06UYvN61-Hz6P1P1WUCuWAKCGZ43kOOZFwqm07AvkUsYivZpB_QTYy6bR4uKzsnHAqI_h5YJvRuUSZ2cSujxxKfxfKFtVqYzbeo_Df9Q0THKLSIClG9pg-Fzk2mRvkoMOSfJ-m8Ppg9igHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس: ایرانی‌ها در موقعیتی هستند که می‌گویند می‌خواهند تعهدات بلندمدتی به ایالات متحده و کشورهای عرب خلیج فارس بدهند تا رابطه‌شان را تغییر دهند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/660317" target="_blank">📅 09:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660316">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
جی‌دی ونس درباره ایران: دلیل اینکه متن تفاهم‌نامه را منتشر نکرده‌ایم این است که برخی از میانجی‌های ما؛ پاکستانی‌ها و قطری‌ها؛ از ما خواسته‌اند که این موضوع را به ترتیب درست انجام دهیم
🔹
حساسیت‌هایی در جهان عرب و مسلمان وجود دارد که ما در تلاشیم به آن‌ها…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/660316" target="_blank">📅 09:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660315">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3530ff42fa.mp4?token=FprsvCoHRqosZKTByrsQ4lQmEr1_JtE-PRe7fofrcFPdTLNtz9XODcHo5haJLeijmxxtzaMwh9UM0kezwANsHoW2J5oDksaUx5yrW2a1stVmPHhx0aryLPgPU9pz0GkSgjlPO6YwtgEfRyXqagU6CDLvypTLqHEOIMyJgEl8OZi3-YFzGdlIasUD8jdvjMZmfwuazXH_N29cCtdpA23MgY9Nls0rFzPKXscy6EHSOcoIKqaDR1rXV8XkJxtPwFZHc_ikEPqq8nCOaNoD4s995dtuE-KtziaAbWCU2QrGqtrqyszZl-c4HoBvglaXFOMfWzBNhxAlgQEtrQFisGQca4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3530ff42fa.mp4?token=FprsvCoHRqosZKTByrsQ4lQmEr1_JtE-PRe7fofrcFPdTLNtz9XODcHo5haJLeijmxxtzaMwh9UM0kezwANsHoW2J5oDksaUx5yrW2a1stVmPHhx0aryLPgPU9pz0GkSgjlPO6YwtgEfRyXqagU6CDLvypTLqHEOIMyJgEl8OZi3-YFzGdlIasUD8jdvjMZmfwuazXH_N29cCtdpA23MgY9Nls0rFzPKXscy6EHSOcoIKqaDR1rXV8XkJxtPwFZHc_ikEPqq8nCOaNoD4s995dtuE-KtziaAbWCU2QrGqtrqyszZl-c4HoBvglaXFOMfWzBNhxAlgQEtrQFisGQca4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس درباره ایران: دلیل اینکه متن تفاهم‌نامه را منتشر نکرده‌ایم این است که برخی از میانجی‌های ما؛ پاکستانی‌ها و قطری‌ها؛ از ما خواسته‌اند که این موضوع را به ترتیب درست انجام دهیم
🔹
حساسیت‌هایی در جهان عرب و مسلمان وجود دارد که ما در تلاشیم به آن‌ها پاسخ دهیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/660315" target="_blank">📅 09:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660314">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvqIWoyAdAatxwH-AzsXueHDI08ivkts1TSQLx5l2U-Hnxm7ZPMhzdqDc7KQof2lhke5J_T6gzdkwxYTfmDn8KKREtYZPjzM744l6vPB00wDii6u4AvOS5e8OB4aQcrjhnMHELS3LydqKpdP6FgluALo_ODcxxRiXfpORxf1sVv5XXmNmatJUeOrId1CUsRTJ4Xu5z8KHD3pueVlxOQF6c9EB7JXTeTh-osNKOUYvARREoPV6Pj3jU_DouUmhPZkB1gR_kzkbm3dTEd5nZelJF-XVK6sBfobjW2pErwGxG3uELSZ5kwz4xQSPjkcq5MQY0OziSLnLITyP3Gj3d1Sew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۳ گل و ۳ امتیاز شیرین برای اتریش
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/660314" target="_blank">📅 09:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660312">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/263458b237.mp4?token=PklHwPTWADiZNNRVw20gknItLrJqTAd0dGDG9IjowjRtfpx86o2vloCRc3PyUPucjkohNvzK4-JM6O8scQJbAqvI3NWaHk4rVqnCY3CqCBggdz9Zh4LmmcO3fOxKomPEEBValFVi5aPl91DE4QftBOKM7FXgk7RWFFnKULfsILtUy-S2XrUyM4MH63iQxFd5gjyEDjGAurpHGmxPiLFD1u_PKUEjgAMDUpEydivZyJcJqxSAbH8dvKrUfOzen64MN3fMT-uHIqPSs289pm6JznyL6-XmbMEh4XFkLHK2EsD4dlk69qUmEg4CLNAYes53oCj_sCYwQ-S2vvJgpKZKRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/263458b237.mp4?token=PklHwPTWADiZNNRVw20gknItLrJqTAd0dGDG9IjowjRtfpx86o2vloCRc3PyUPucjkohNvzK4-JM6O8scQJbAqvI3NWaHk4rVqnCY3CqCBggdz9Zh4LmmcO3fOxKomPEEBValFVi5aPl91DE4QftBOKM7FXgk7RWFFnKULfsILtUy-S2XrUyM4MH63iQxFd5gjyEDjGAurpHGmxPiLFD1u_PKUEjgAMDUpEydivZyJcJqxSAbH8dvKrUfOzen64MN3fMT-uHIqPSs289pm6JznyL6-XmbMEh4XFkLHK2EsD4dlk69qUmEg4CLNAYes53oCj_sCYwQ-S2vvJgpKZKRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تولد اولین گوزن قرمز هیرکانی امسال در پناهگاه حیات‌وحش لوندویل
آستارا
#اخبار_اردبیل
در فضای مجازی
👇
@akhbarardebill</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/660312" target="_blank">📅 09:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660310">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-h-KDI3EOehXLdu1QbXDNj1ypRvlyNH2xbcE_2FJ2L9f_JuosL_JyMkPXRpaRRvzJ47wM3e3I8Z1mrzY9QPVzRkcECO63g1IBweGuUW3NEp30HQOjhsTqfb-SSL6rw6xQsHOJs6bI6OsCsYCZKHfiCgYKd2gKqO_GvDhdNo9Kgg8kUoLi5xLMneATFU8Klx-RSl4rsRufEk6pP0jnXM9eS0Cuz_AvdGzRyrs74AecPEeJRyA5ECGTKALdnbJVnf_j1MSqMjkbHwgNxJourDOOwb5Tu4jIB71gQZp0dCSJVWJATP4M2bPUGCpKQzs4OPJqDgbePbnExjGwWtA1K2yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تمسخر ترامپ در روزنامه «مصری الیوم»
رویترز:
🔹
ایران شرط بازگشایی تنگه هرمز را قهرمانی در جام جهانی فوتبال اعلام کرده است!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/660310" target="_blank">📅 09:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660309">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfWPISjuL7jhUAxhUTrWBqLP_FWhQFfHyexuSEhBX6-9Uo7kknmm38Q126A4xDN1XWJO-i2ewGBArJU_r-bqO3VRG9VBgE7Mz0Oa9DSJtIj8myeiG_pvx4DuutF6S9WaO12hC2fUNiHbgc7BU18riNO_LVqGKK4JJuLKOp9P5RXafUey34zQX6z0zmTggz2DTkL8_nGsGJhl6jdsF6zMDMX7VVcXLZ2O0AqBXVSldKCivoxXE7T-SrvCPQ8dX4aZ6wV__AJ1GK81NS_wRNh2keRQp3ayaFNXBJYf6cAIaouxloKKxdCCwMdV1WsEq0_SPBL2XDQ5FTHM-0VWUXGGiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
داوران جام جهانی چقدر درآمد دارند؟
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/660309" target="_blank">📅 09:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660308">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2bf449e48.mp4?token=YpB868p2GVDzms2U6pjOnoz26Wp2X4yjDbaKAcmtaVQmS-nzQq70bNdIMPpCZEijxDhKh8bDPuWTovjVWlQpqxy8hJQwO4pb65AsOpwDuMzaWjqZRq5R6jW04I20CShq4OR_5dfggY1uKdGqYErg4l6G7MxRCt3DHJO8_SGgK9xFmTKvIf1z0G1_ZTVLKV7e59QS3wB4J2wXehmThp2hXeOzWndfzj3dW6Kj4D5rWU6OvRfS358h-laIw1VSL7y3wuMfmb3cu22qfS1h_YimhLUSDDckO2YCuWo42RUEF2xOBkGRm8Cx1GgIDczJXwMEsREfxk2Gc8V2_YYZm7tdbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2bf449e48.mp4?token=YpB868p2GVDzms2U6pjOnoz26Wp2X4yjDbaKAcmtaVQmS-nzQq70bNdIMPpCZEijxDhKh8bDPuWTovjVWlQpqxy8hJQwO4pb65AsOpwDuMzaWjqZRq5R6jW04I20CShq4OR_5dfggY1uKdGqYErg4l6G7MxRCt3DHJO8_SGgK9xFmTKvIf1z0G1_ZTVLKV7e59QS3wB4J2wXehmThp2hXeOzWndfzj3dW6Kj4D5rWU6OvRfS358h-laIw1VSL7y3wuMfmb3cu22qfS1h_YimhLUSDDckO2YCuWo42RUEF2xOBkGRm8Cx1GgIDczJXwMEsREfxk2Gc8V2_YYZm7tdbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جان بولتون: ایرانی‌ها ترامپ را مثل ویولن نواختند
مشاور امنیت ملی دولت پیشین ترامپ:
🔹
«این یک توافق بسیار بد برای آمریکا است. ما نمی‌دانیم در این توافق چه چیزی وجود دارد. اگر توافق خوبی بود، علنی می‌شد.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/660308" target="_blank">📅 09:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660307">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/047e511923.mp4?token=KgHQYR6y8FWpsan6knQqDPkX29LmZTSZnD8qIostz2O8yF6_9zmJ3IhMeUWHmKv0GrWCRBoAI4KqiKnBW32IAL7GZAbfml19kUa-u-cPJ6QxkmpTgj8I0qpIJElhlQThmo6uODvLeVv4YYMc9C6BrBXzEJKGDXJTML5ms2Yg80G2awKk1mZdw6oIWo-UfuRPWFuOe7pODJGUM_UFEWXk5qpjAz6u1ObVv66CBS8gV0TNiXy-aGGg1I6IAoeLCp12VrdlfU0T88tdBE-7n-FLyPShimRagHIQFhtsWQUclU6qfHVvZ0s1amXWvwgbDJ4x86-yGHSzrpvQrkM69BoymA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/047e511923.mp4?token=KgHQYR6y8FWpsan6knQqDPkX29LmZTSZnD8qIostz2O8yF6_9zmJ3IhMeUWHmKv0GrWCRBoAI4KqiKnBW32IAL7GZAbfml19kUa-u-cPJ6QxkmpTgj8I0qpIJElhlQThmo6uODvLeVv4YYMc9C6BrBXzEJKGDXJTML5ms2Yg80G2awKk1mZdw6oIWo-UfuRPWFuOe7pODJGUM_UFEWXk5qpjAz6u1ObVv66CBS8gV0TNiXy-aGGg1I6IAoeLCp12VrdlfU0T88tdBE-7n-FLyPShimRagHIQFhtsWQUclU6qfHVvZ0s1amXWvwgbDJ4x86-yGHSzrpvQrkM69BoymA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر صنعت لبنان درحال پخش شیرینی
🔹
خبرنگار:
«مناسبت چیست؟»
🔹
وزیر:
«آتش‌بس»
🔹
خبرنگار:
«گام‌های بعدی پس از آتش‌بس چیست؟»
🔹
وزیر:
«از سفارت ایران بپرسید»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/660307" target="_blank">📅 09:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660305">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a2e0f9b7.mp4?token=P-zx3cJA5cvUH7I2bG1YYOCIJdp0JC1rt-Ml1VHFA3eN3rcBa1AEUye_EDWhUYKcM6ApFBnpaft6BLB1bfWJV0i07laj-lOxDA4uKidEVW1ZybLWWClxs1Rih-BeHVPKlAb-lRo6TaIeKpC7mF0acUM8YgdJk1CCu6m9ncQa0LpGfBZHIEfNgBULOAuIMUdfjjwkCdSJ8YnQ0l_ozgQdtqsQBpVTv4diLk-ng61cGu1qP6YrKh6k108Q6eRG45H89AWlkFg6U9ap47EcbW6EwiT57xlVL5kPLJdMkOIKPwDCNCRGpbGRlzImcbTJaNLV25J3BWlEpSZgPTC-BneO4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a2e0f9b7.mp4?token=P-zx3cJA5cvUH7I2bG1YYOCIJdp0JC1rt-Ml1VHFA3eN3rcBa1AEUye_EDWhUYKcM6ApFBnpaft6BLB1bfWJV0i07laj-lOxDA4uKidEVW1ZybLWWClxs1Rih-BeHVPKlAb-lRo6TaIeKpC7mF0acUM8YgdJk1CCu6m9ncQa0LpGfBZHIEfNgBULOAuIMUdfjjwkCdSJ8YnQ0l_ozgQdtqsQBpVTv4diLk-ng61cGu1qP6YrKh6k108Q6eRG45H89AWlkFg6U9ap47EcbW6EwiT57xlVL5kPLJdMkOIKPwDCNCRGpbGRlzImcbTJaNLV25J3BWlEpSZgPTC-BneO4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هتریک مسی در بازی مقابل الجزایر
🤩
🤩
🤩
🤩
🤩
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/660305" target="_blank">📅 08:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660304">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/992d6374f7.mp4?token=S-dEuA7LpeAg7mTKe3ow5BU6_UjJCTwYyA0S26565YSkIkztqlbhXcvJKOufNRwvvmSkD-qwetYia2qE-kJ_dQjWHwfkkzdWvUFQXs-eaCYip_hgRCTZgaWL70dYXQ33PkNvN44JGVgcIBPuv6v_ETA7rn2zaYy6wroWEnofBODXs9Q06HelV3Iaq8HzBj0LBDB4dluHI2U-RwHbYuBNTKZoqp2vcoNuRkTL2FsoDGvMrvb4UwP2VJIH5xOpeA1lNk8L5gfF4qTrEMpBCcDEpeZ92-11IuJJjP70YDvjQV9ohsG9geRLuw1S4mVSZXj8vryxUc9AGfKwCZ6nDojctg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/992d6374f7.mp4?token=S-dEuA7LpeAg7mTKe3ow5BU6_UjJCTwYyA0S26565YSkIkztqlbhXcvJKOufNRwvvmSkD-qwetYia2qE-kJ_dQjWHwfkkzdWvUFQXs-eaCYip_hgRCTZgaWL70dYXQ33PkNvN44JGVgcIBPuv6v_ETA7rn2zaYy6wroWEnofBODXs9Q06HelV3Iaq8HzBj0LBDB4dluHI2U-RwHbYuBNTKZoqp2vcoNuRkTL2FsoDGvMrvb4UwP2VJIH5xOpeA1lNk8L5gfF4qTrEMpBCcDEpeZ92-11IuJJjP70YDvjQV9ohsG9geRLuw1S4mVSZXj8vryxUc9AGfKwCZ6nDojctg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم آرژانتین به الجزایر توسط مسی۶۰
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/660304" target="_blank">📅 08:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660302">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae7bd7f779.mp4?token=U3t7z9cFPmbBukH8QFWh6pAAzhZ--EC-5VuY7bBX66QDbndnY5k0j62VTVc72wJZ3EoHfZGhVbaW9_UCw8KOVcmPEBOX4I1bqi4UYU56LHWyccXwtZ9KuPhXyR-YMdvpFwo5yKs1ZLGZ55ShWm9MMaazTZYE6pvLMSzen8KCb95bo-Xgcnci3rME6wRLeX9SoeVKUl0fD7cbuqbhLHACHkvSnHxrO6m1au_A7zklF8E70ZgWbYvXN02-pv4Iojy0W561ESUu_VZIHGE60kPKniJMy25D2b7WSkrgYHzFT6hMgjOjPUHuKo3jNzxxb-P6GIITFDGMjhslVT3j6mt14g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae7bd7f779.mp4?token=U3t7z9cFPmbBukH8QFWh6pAAzhZ--EC-5VuY7bBX66QDbndnY5k0j62VTVc72wJZ3EoHfZGhVbaW9_UCw8KOVcmPEBOX4I1bqi4UYU56LHWyccXwtZ9KuPhXyR-YMdvpFwo5yKs1ZLGZ55ShWm9MMaazTZYE6pvLMSzen8KCb95bo-Xgcnci3rME6wRLeX9SoeVKUl0fD7cbuqbhLHACHkvSnHxrO6m1au_A7zklF8E70ZgWbYvXN02-pv4Iojy0W561ESUu_VZIHGE60kPKniJMy25D2b7WSkrgYHzFT6hMgjOjPUHuKo3jNzxxb-P6GIITFDGMjhslVT3j6mt14g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول آرژانتین به الجزایر توسط مسی ۱۷
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/660302" target="_blank">📅 08:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660301">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
زمان برگزاری آزمون ارشد ۱۴۰۵ تغییر کرد  سازمان سنجش:
🔹
به‌منظور فراهم کردن زمینۀ حضور متقاضیان در آیین وداع و تشییع رهبر شهید انقلاب، آزمون کارشناسی ارشد در روزهای پنجشنبه و جمعه ۲۵ و ۲۶ تیر برگزار خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/660301" target="_blank">📅 08:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660300">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097ef7de48.mp4?token=lwwABmfyB6G78ToG6bPQvr88xF469-PbZYAoHTE2RKFxfIUqcnPmLUvAcefQ9PTZE9Zozw9lspbKQQKn6QcE0dxPx-zlNKT--UcV8bNsFPyecUOOE9fcFeWK76l2vkLT1NsxDtCyRTjmb3pXutTCpfclB9mHoJblWeMZ8U_DTEaj3PXPdhY6yiUcr5ZrRHGbY_oGBhjCVTaCj4UO3Fc2bJIjDw3TYxsBpz33d3bsABsk-vOoyj29mBV7jK4HrXDUe4hU-sKhdvU5yVfEu9uGiZnABr8Ab9T1qsnU57XNlXk7itoLXPSob0u1Yoyz25RxZBZvvTJxpWt0eWY2jlMsuoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097ef7de48.mp4?token=lwwABmfyB6G78ToG6bPQvr88xF469-PbZYAoHTE2RKFxfIUqcnPmLUvAcefQ9PTZE9Zozw9lspbKQQKn6QcE0dxPx-zlNKT--UcV8bNsFPyecUOOE9fcFeWK76l2vkLT1NsxDtCyRTjmb3pXutTCpfclB9mHoJblWeMZ8U_DTEaj3PXPdhY6yiUcr5ZrRHGbY_oGBhjCVTaCj4UO3Fc2bJIjDw3TYxsBpz33d3bsABsk-vOoyj29mBV7jK4HrXDUe4hU-sKhdvU5yVfEu9uGiZnABr8Ab9T1qsnU57XNlXk7itoLXPSob0u1Yoyz25RxZBZvvTJxpWt0eWY2jlMsuoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات شنیدنی شقایق نورزوی درباره پروژه براندازی سیاسی؛ برچسب‌زنی برای نابودی هویت ملی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/660300" target="_blank">📅 08:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660299">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32074fbed2.mp4?token=gPGmGuWSRLFk885FAA9VgSwlETAgAeC_m6yMaBz6R9Nyg96Qt_muJQIq6XdnpDgwws_96hlOjRVZm9t9tDC6Q_LTlh20lS1cNpRbreK-dpl-OXpsQ2ChQmavaMLutXPElOWsAsLZjc-0u4mmdEfh-_lz-MkIyDuELC3ydkpMrRMaD_WqweVuq1GLblxGDmwxCTWGpKLzgCdeahZA89hvi6BkMUQWCSmKQ_fpG9dZw3XMZsF-L_9YO0qlty1T5WEjYrE60rWJtJcHINqMZT2gKn3-CrQGhDGBndrcq5tUUkePJ8Ig528fagCRsKnb8SnPedscv9CA45Q_m2dC_Jjcpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32074fbed2.mp4?token=gPGmGuWSRLFk885FAA9VgSwlETAgAeC_m6yMaBz6R9Nyg96Qt_muJQIq6XdnpDgwws_96hlOjRVZm9t9tDC6Q_LTlh20lS1cNpRbreK-dpl-OXpsQ2ChQmavaMLutXPElOWsAsLZjc-0u4mmdEfh-_lz-MkIyDuELC3ydkpMrRMaD_WqweVuq1GLblxGDmwxCTWGpKLzgCdeahZA89hvi6BkMUQWCSmKQ_fpG9dZw3XMZsF-L_9YO0qlty1T5WEjYrE60rWJtJcHINqMZT2gKn3-CrQGhDGBndrcq5tUUkePJ8Ig528fagCRsKnb8SnPedscv9CA45Q_m2dC_Jjcpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین از پهپادهای غول‌پیکر به صورت همزمان برای ساخت دکل‌های برق استفاده می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/660299" target="_blank">📅 08:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660297">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f529146bc.mp4?token=ThkR3StWncFGLm-H3NNxOASOrbmOdSsSVd-d7wCi6DnKUJLKCM9J0FbVMxBKFebDdAB6Sh7iJ-vrCsode_CTNfvPrEgMe8knC6dIPnJ_KTKt6Xr32PaLkOMAI61eLr2vxMGX-kmhs4OzYRZCb6jtlHeQQ6kB0FYshjGtdTZWaVETPBtFKTgOuZm5yX6DKpLj2gORau8mmBwg4Jny_aFNWuGf_COoXlmWpak-1jgvzUlqfhiwXMRF9AABpeWJgD6Qq4mgZ8PhhHmtqfDUkpACsRSZl23w1RqZpH-LaOkOSGsa_l4QhL2CraV5aDPlcbyaFfEGvEAjGI9ozqFPG4fzMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f529146bc.mp4?token=ThkR3StWncFGLm-H3NNxOASOrbmOdSsSVd-d7wCi6DnKUJLKCM9J0FbVMxBKFebDdAB6Sh7iJ-vrCsode_CTNfvPrEgMe8knC6dIPnJ_KTKt6Xr32PaLkOMAI61eLr2vxMGX-kmhs4OzYRZCb6jtlHeQQ6kB0FYshjGtdTZWaVETPBtFKTgOuZm5yX6DKpLj2gORau8mmBwg4Jny_aFNWuGf_COoXlmWpak-1jgvzUlqfhiwXMRF9AABpeWJgD6Qq4mgZ8PhhHmtqfDUkpACsRSZl23w1RqZpH-LaOkOSGsa_l4QhL2CraV5aDPlcbyaFfEGvEAjGI9ozqFPG4fzMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیراندازی مرگبار در بیمارستان ایالت دِلاوِر آمریکا
🔹
تیراندازی مرگبار در بیمارستان ویلیمینگتون ایالت دِلاوِر آمریکا، یک قربانی برجای گذاشت و عامل مسلح حادثه همچنان متواری است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/660297" target="_blank">📅 08:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660295">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">واردات پرشمار خودروهای خارجی از قشم/ نگاه بازار خودرو به قشم
🔹
با فعال شدن کریدور جدید دریایی بین قشم و عمان پس از جنگ، محموله‌های خودروهای خارجی به این جزیره سرازیر شده است.
🔹
با شروع این فصل جدید و اقدامات مثبت صورت گرفته در جهت تسهیل واردات بی‌سابقه خودرو از این مسیر استراتژیک، پیش‌بینی می‌شود شاهد افزایش واردات خودرو خارجی و تغییرات چشمگیر در این زمینه باشیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/660295" target="_blank">📅 08:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660294">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuFP25H9tQlfXSNWRKmOsm79FZhEz9_c29LuFQx3GhLm7z5w6nvLuWYNgjop8yM1RZ2uCT6DPx0cHOw2xKWzVGh_6mojUqiPjYc5ccpmySHfyj-KMSHOwtHIPZEIicHKoUZP2FXg3UkHn2XrjVca9lltCUclHd6cVCuFI8NnHS44eBptPAUmNb0mnuNKzy2YolGorvEKOQPThsiGj-RKNb1ood1pB7KhIRf2PIzEpHvvQfbuXG2Lnqnq17g8INslvMOkEJ0z6jxnXiQG86rPOv2idV_dmRy35PezSgv617PbUFOLDcgSXirXslLr_R-Ias-f3EqqYIP2yQjySPopqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دست‌کم دو ابرنفتکش شرکت ملی نفتکش ایران (NITC) به نام‌های دیونا و هیرو۲ با مجموعا ۳.۸ میلیون بشکه نفت از حیطه محاصره دریایی آمریکا خارج شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/660294" target="_blank">📅 08:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660292">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
ویزای مهدی ترابی منقضی شد!
🔹
مهدی ترابی به دلیل ویزای یک‌بار ورود، پس از سفر به آمریکا با مشکل انقضای روادید مواجه شد و فدراسیون برای تمدید آن اقدام کرده است. #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/660292" target="_blank">📅 08:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660291">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/993fab37b6.mp4?token=WNUaJGrpBlpUEcvB_jNZwfQaaSxeVZpbBgHfp7p3hoqZyaCKlMwbNyrCWs7SWFlveSbZfoPkRkF2C15IKe6M-1j5v3ZgysXRoMx5hAaa7_CTt124djDNYKut6sGr-FYki5InpUuc13VjXkOig2FH8dl_pRuoEp_KbQDTaC--lx32DIYb2sRWGzj3bK2AQNCVaSD5Stg6QKzNiw4SZep1aC7lMJFYygKu8Avwl7qFIYzS38bBHUQRO31qIPlYPnSs3ar4xUQnu46T3PDxUybfB-zLHiYxNYdb52XYWBkokv7UclT0z_cGWAZUqIJpyC8NVQmZdL8zlE_W9i2jbC45tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/993fab37b6.mp4?token=WNUaJGrpBlpUEcvB_jNZwfQaaSxeVZpbBgHfp7p3hoqZyaCKlMwbNyrCWs7SWFlveSbZfoPkRkF2C15IKe6M-1j5v3ZgysXRoMx5hAaa7_CTt124djDNYKut6sGr-FYki5InpUuc13VjXkOig2FH8dl_pRuoEp_KbQDTaC--lx32DIYb2sRWGzj3bK2AQNCVaSD5Stg6QKzNiw4SZep1aC7lMJFYygKu8Avwl7qFIYzS38bBHUQRO31qIPlYPnSs3ar4xUQnu46T3PDxUybfB-zLHiYxNYdb52XYWBkokv7UclT0z_cGWAZUqIJpyC8NVQmZdL8zlE_W9i2jbC45tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یورش نظامیان رژیم آل خلیفه به مراسم عزاداری در بحرین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/660291" target="_blank">📅 08:03 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
