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
<img src="https://cdn4.telesco.pe/file/UVE4kDOR6uh7OvvoDUfGIXEaULS_ae5vGc8mSAzYrelbWk1gt4_Lc4dK_Rr_yDCzocEo25LoQyOLjVAyU1R35VACJl6sb49IaOqOPRmvPtjufM001mHfI4nK3wWTiflKjiaoGUNTZ-sVu5ACHdu2zJGmuB0w6Du8iZLx7Pr79RTH5lxF9y6BMNvDQIio6Fok9ztIyK4CygvczkAORQVu7jQ-vToGBQcbPCuJdLrFFkeXGu98o74J3R-RNXoTaAuEulT9JcrkIomqPTiVADI7p5KjSJstfgF9lzQNvi4Ain8vB2HrVO7Yd-hS5UOXTyr8aqVynL-fiCHC5jrWiE0Zsw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 435K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 19:01:30</div>
<hr>

<div class="tg-post" id="msg-25534">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHVBM1Osdcs32c4gYd1_TwttiU6nhkWtAYJQXR2Tam3TbXnVrQpT7ulbaSuhewIEBYKtYShD4cmUX7HTjM2Gl-fZ0pSePrr-Uy_StuPWecrilG2FDR9AMEyMJ3r2V0Ix0KLehRFYZYt7N0Bxg1NgweRN7d_dECKbHA-sGC2ZuTwly0lkYNXcPLFmRI7tuso0nJ0L_Aj2uBVry2c6ELY107sJtMpq--Bx0dVpIXHCeG5gjYtCEydIPc-mOWokGdiorjzjwi8V0HzZtpqELgJZWYDS91rwnvAe4mMikQ-lKodgjn0DJWXrXOX3EwgUZxLiV1biAyAmqI5xUFDXgPc62Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوسمار ویرا سرمربی‌سابق‌پرسپولیس در انتخابی عجیب با عقد قراردادی بعنوان سرمربی جدید به دوا یونایتدبنتن انتخاب‌شد. تیم‌یونایتد بنتن فصل گذشته درلیگ 18 تیمی اندونزی‌رتبه 7ام راکسب کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/persiana_Soccer/25534" target="_blank">📅 19:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25533">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iyi03NHvRJKZWB8-FK86aXpbipTzw2obiaQerUYCwKWF_PT4sw4072m0MDWEWT150XK31QLz2s7YeiOn4uys3_QllsWU2cGkFelUw0X3pz0QIxay0F9D5a3z5mPrSK4XGXyT5_Dv7scMrVRMiCKkXTyyQIdp50ks76EXkCYI9QwI4KF9R0O0mNXxpuOOb0R7Ws7bWlAc-2OeXcZq_NU6U6CBtBSC39zr6unzb5LhQ9hgUXGeYtKpR0hcLbMhfHtn_Xoz4O2t8zmqXlVNXnZ-s5_eIBxHaxNUnCYF-Tx-rzn_JRFPQNqma5u6vVvxR786VWPYzJrt3M1z77Gtxkf29A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
برترین گلر های فعلی فوتبال جهان که بیشترین فالور رو دراینستاگرام‌دارند؛وزینیا بادرخشش در تنها یک بازی‌مقابل‌اسپانیانزدیک 16 میلیون فالور گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/persiana_Soccer/25533" target="_blank">📅 18:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25531">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nm4dKF9netNceUd1VQonlbmfyjr-FE8titpYNJ3BPLMOQlHxh043OXgcEZNnso8szDnNS92X4NbQ3X-26w2JH69VQiLNIpgRfZSJxFAfjz07nyDMt9Q8kVe0lYZx99E2bs7zsW5k5D57F3iTX9r3WQb_EoozphQ3kO4Ar0kgjj3EdL4GuRyBxRzAz6wjKyuQWbYaMGt6zP8v-seUHRujnBJgSlgDfchR26QEB2MdAY84lu3YGEvLQZ0NP50jrAYKC2iBIqS2aV5DEFlYcRa1UjlJ0NkcoVw3q5cCVfiY2oYUkEkNl1lIbMmUKbQuBD8frCtpNXoTrkAY-aD_pmG19A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec951e804.mp4?token=sqrRDSudeuhmXjY9ZIvXPAGWlr_JAYczpXmhgMWgi0kehHwZVzQbUaQgCiORt8sBV_ll9cDjur0hPh4EGxxgbs7ium4msfBGwTZn29HUaL1eJyEIzcLeCSRtF92gB6EIOTh8uodaIpx60kjygbyNVYoS_KUqZ62auRn_WVUVlf-ywRoykoJeefxnosoQ7_nXLeoJRfSNtZPj3DIp0ImbaAB7rJySyScrzFxQ9XQ-f0INmcLxLmGbT-iaQ7MLS4WKoXT-FfKn6XTHoDoTxoBOOq1x8siwQ3Y4VtIMabob7fR6gh2EiOLaWrE8DS51Zi8yFwtcEtIeiJD6OCTCT1aPcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec951e804.mp4?token=sqrRDSudeuhmXjY9ZIvXPAGWlr_JAYczpXmhgMWgi0kehHwZVzQbUaQgCiORt8sBV_ll9cDjur0hPh4EGxxgbs7ium4msfBGwTZn29HUaL1eJyEIzcLeCSRtF92gB6EIOTh8uodaIpx60kjygbyNVYoS_KUqZ62auRn_WVUVlf-ywRoykoJeefxnosoQ7_nXLeoJRfSNtZPj3DIp0ImbaAB7rJySyScrzFxQ9XQ-f0INmcLxLmGbT-iaQ7MLS4WKoXT-FfKn6XTHoDoTxoBOOq1x8siwQ3Y4VtIMabob7fR6gh2EiOLaWrE8DS51Zi8yFwtcEtIeiJD6OCTCT1aPcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/persiana_Soccer/25531" target="_blank">📅 18:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25530">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2121b6e4e.mp4?token=hXTGJqEWJ4CmsAnXhFr30iXXUfqRXqVNzZTaiO747OOAVydX7PtpIvtJm8ft8o_nV7Fs4Jj3fQynLUsX3xDVMobqs3nbh0dM7gV-hFn4IWhI9hutV-b8AVA0Of2CD-CNGl7AGAYJavoCDLhrYctgpexwqmTqv7SGVto92ekdFzaAS2RTjBk0tC5yEz1NtmNv0dss5rQ1kW1Z30DrstzBJ2oEwprYPcnJEguZpgDMBkUAKuSkNZjozK2-7qigXhR_Tfg-Bb-NXQBA1GaR44t_346ZLcp8ZHegLTp-X6ayPFGN7pg-bs77RAlJzgkk0B3UDfY0tPgxZA9nHdZhGpXquQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2121b6e4e.mp4?token=hXTGJqEWJ4CmsAnXhFr30iXXUfqRXqVNzZTaiO747OOAVydX7PtpIvtJm8ft8o_nV7Fs4Jj3fQynLUsX3xDVMobqs3nbh0dM7gV-hFn4IWhI9hutV-b8AVA0Of2CD-CNGl7AGAYJavoCDLhrYctgpexwqmTqv7SGVto92ekdFzaAS2RTjBk0tC5yEz1NtmNv0dss5rQ1kW1Z30DrstzBJ2oEwprYPcnJEguZpgDMBkUAKuSkNZjozK2-7qigXhR_Tfg-Bb-NXQBA1GaR44t_346ZLcp8ZHegLTp-X6ayPFGN7pg-bs77RAlJzgkk0B3UDfY0tPgxZA9nHdZhGpXquQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسی تو نیمه اول با پینیرو داور پرتغالی بحثش شد دیشب: بامن‌درست‌صحبت‌کن، بی احترامی نکن. من باتومحترمانه‌صحبت‌میکنم تو هم باید همینکارو بکنی. انگار نمیدونی‌چجوری باید بابقیه حرف بزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/25530" target="_blank">📅 18:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25529">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0b0e1c0d.mp4?token=ZMoDFPWNraue4r34TJUFOlsuByTk_GU50R9p72Gc7s3nCaROU1fpuNrA2QYBSNGBi2QJLDI-KN7wYcwhRqHX_ooVSclZHXM7Vr2vsVZQD5OqcU3oK5KPl00KGOT9pjsJ4grt_AkUKE0a790b7Y9Gap-hThm75E3UOpvursLImaYtV3q4Yl4YTX6IM6CvX2FWoLqZx4egEaB3eSEur53WSUZql7Yms0m2fc9wXcF0-uGs-ri6R7U-11Lw8Bj0Xf7ok4HcpVn5rp0ScpsoMB6VQblWQKeMNI-cNax4xXxbvffYCZ0mUlYpMxSH3xu0Oze5PWDXq_rmwzgeMMmUUa43HTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0b0e1c0d.mp4?token=ZMoDFPWNraue4r34TJUFOlsuByTk_GU50R9p72Gc7s3nCaROU1fpuNrA2QYBSNGBi2QJLDI-KN7wYcwhRqHX_ooVSclZHXM7Vr2vsVZQD5OqcU3oK5KPl00KGOT9pjsJ4grt_AkUKE0a790b7Y9Gap-hThm75E3UOpvursLImaYtV3q4Yl4YTX6IM6CvX2FWoLqZx4egEaB3eSEur53WSUZql7Yms0m2fc9wXcF0-uGs-ri6R7U-11Lw8Bj0Xf7ok4HcpVn5rp0ScpsoMB6VQblWQKeMNI-cNax4xXxbvffYCZ0mUlYpMxSH3xu0Oze5PWDXq_rmwzgeMMmUUa43HTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیوزیبا از لحظاتی فان و با مزه لامین یامال و داداش کوچیکش که این روزها سوژه رسانه‌‌ها شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/persiana_Soccer/25529" target="_blank">📅 18:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25528">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8eD4u8ga_x2Syi5_AyL3wlv7Akdxrwa2eKDzjJj1G1mMAHzeM3nbXc3zb8WqUO1vwkl9dP6qorm0sfKg2nqRwZzKDRbJRW2yXfx-1LnEXwF9aG5wdCj_vFhowSa8IH25c6x96Y-ZUarABPpLDL4G0brOKYod7JElOZG8eSdCiQP8GXycHL52sjKMPj9bk45HKBwjA9Snv8dprl3VjAV8fRNIRt_sJJ1cHfRNR3BrreB0smQluVGCPZluH1Qq96U7nMvgpx4znrK53dIpSwNJyYRpHRW5hJ9YRHVC-RjAUu2ToQoC0SbTwu2YkVBvwL73h0vojpY2nBEjKtZ9tjXjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
👤
طبق‌‌اخباردریافتی‌ پرشیانا از اصفهان؛
مدیریت‌ تیم سپاهان‌ با‌ حسین ابرقویی مدافع میانی 29 ساله باشگاه پرسپولیس مذاکرات مثبتی داشته و درصورتیکه حسین‌ابرقویی بتونه رضایت‌نامه اش رو از سرخپوشان بگیره راهی اصفهان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/persiana_Soccer/25528" target="_blank">📅 18:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25527">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‼️
تو یکی‌از خانوادهای‌عشایری یه دختر بچه حالش بد میشه، بعدمیبرنش‌بیمارستان تست میگیرن میبینن باردار شده؛ میپرسن کار کیه!؟ میگه پسرعموم، دعوا میشه بین خانوادهاشون؛ برادر دختره که بازم زیر سن قانونی بوده میزنه پسر عموش‌رو میکشه، میبرنشون دادگاه خانواده عموش…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/persiana_Soccer/25527" target="_blank">📅 17:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25526">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZQumKjx26UpqqAOTYbfEpRrljlXPfesSi_6u0FN8efem4n7tiWGVTsyjb_64pb7tmzvxvSFbTEVgslZpd7OQ4nHes-Ji-_H2nilTVFLHrLsA8p-ZPXlWcnWTgoryQH9RJ2Z_KsKSGxng2RyJ2xm1MFdbHaP2UBBB_3Rp_XTqdBk1ev7rgIEru-a7gKXbp3ApAyxeIPCDF8KoSj2ciQGJUh6mILmEHCuxBvMDJ9ja-nvJpfckG4FJ3kyvja-K9zmBn-hsd1FeLBvo8sLruBiXinz3VNToOsQZ-dI-cKIvtNSwUjqhUARaON13ob0NLGhNG_0tNIJT928USBKTh1cCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تقویم
؛ پنج‌سال‌پیش درچنین‌روزایی؛
مدیریت باشگاه استقلال تهران هفته‌ای یک الی دو بار از سجاد شهباززاده مهاجم جدید خود رونمایی میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/25526" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25525">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C52JfnNMJoiqDi9hYNlFTyc-NvyWDmhKN7zusjb6FHnV2LhhfKbQ_lVGpJ48jzKn80VT2DI6PqXNogOeit81kck60UgoRYkxK2QJT4wYCYhExQUK56c3Q99htaSmzfqMijbPfZZXHybo5HVRF1PIIlW7luRll412J0rwHSwXomf5sKFbE-bSzhQxpMKlDyoehb2osfMnRh93-EUZNVjxta3N33v7ufVhAxiru15IxNK_lIAsaGuSM6AeE7Qc5ND2R1DxBfOW70ygSiN2YLpS5Ylg1ms5Ohj5017U2untuC8BuWzhsVhX1OzuE0Y0-6c2P7a5GZjiyyA9nl6nswMDVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/25525" target="_blank">📅 17:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25524">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhaR5RRxBQakZE8NvFYjHMFZN4RrVkySacKs4JVcPc3iWgJVyG7kD9ACSKvi5kfNpUUTuztbCh3VadptPIVQ1_LqmSoWvV3MvjdTj5iHBKIWzrzesxEFRtxn9ZfOxlxrYEu2ISNz8XOndhgZLDfJ3DGjb582wC4jyBSC2k0l3uZ3QXgNfeuGEDwGzpRMd_mvyKB89Al1N3l52-Xmbc5PoKc5DfZMisLsYz6vlC_a_20_yayxaMkg5WXzTzbYO5Du-qJQDXesPmCKHdUAuWyL1neXj4o-D3N3yVMhu0vekMJNASW8h6bgFwZrx1d1tzG4wZpi9hCgohBJbWXcWdpwlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
عارف حاجی‌عیدی هافبک‌جنگنده سپاهان که مدنطر مهدی‌تارتار و پرسپولیس بود بامخالفت شدید محرم نوید کیا در جمع طلایی پوشان ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/25524" target="_blank">📅 17:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25523">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9c9cac2a.mp4?token=dDP6Cj7FuGB04YixsAahLKYKoJs3OfSlCpOGHfdr9QX-LJlUEG4gGV6neDOryB5Acb47aZLO9FLHG0hRfOCi4MoyqMPLC5LeiUniY5i6kFD50x1KryVCguZEvaLAzhKLi6wk8gWHlhctXLI_w4JW0mhwiYDbnDD_kLjrSYU0U2BNW1mlX9tAEvFaLGDRYEKPJBAv9W7nI6r1XZeshtFP24pG72kf-2XYOVxwDAOW1ULhtEIhKXAI9An5PluacdQFiD6vSfwfDBGMLOKk3m9lr15NavnjT5BTfvUg9tipx3R_4ewJwHFjFfn9Nw9n9xp4wQajFbMfrceFftZXlT79oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9c9cac2a.mp4?token=dDP6Cj7FuGB04YixsAahLKYKoJs3OfSlCpOGHfdr9QX-LJlUEG4gGV6neDOryB5Acb47aZLO9FLHG0hRfOCi4MoyqMPLC5LeiUniY5i6kFD50x1KryVCguZEvaLAzhKLi6wk8gWHlhctXLI_w4JW0mhwiYDbnDD_kLjrSYU0U2BNW1mlX9tAEvFaLGDRYEKPJBAv9W7nI6r1XZeshtFP24pG72kf-2XYOVxwDAOW1ULhtEIhKXAI9An5PluacdQFiD6vSfwfDBGMLOKk3m9lr15NavnjT5BTfvUg9tipx3R_4ewJwHFjFfn9Nw9n9xp4wQajFbMfrceFftZXlT79oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هومن‌افاضلی‌از کادرفنی تیم قلعه‌نویی:
شجاع پاهاش پرانتز برعکسه اگه پرانتزی بود پاهاش اون گل‌هم افساید نمیشد ما میرفتیم مرحله بعد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/25523" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25522">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=ZjagCP72b48UANjEJB9xTHjlhjUnqNGN7lnlq0UWLc1I3ZOn_cAm4bcYEdA7hbM7GuYOwo30UU0KYVPeHxFLI2elv_mDgKDWFj8xoOI7Xk7zjTZjdLHJIpOXkCBokKUvfITMqW28CAxqoGlx3hzHHKm_Npr6lmLixJavaC3hrSxG2xMAkECsTuoCEQq9gOc1YhF-oQamWwql5WTnN9g-Vm4T7-dL8VtdvgKx6WQtaH0hB82NBllzQmsGFH-D8xmZySl5cq-FqNF4TjULCewJF5jnTfHNu6E5GZSpPZnwmyPVjLji_NPeIziu3sI-h2uqjJ42Gt09wznZywI-SDfMdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=ZjagCP72b48UANjEJB9xTHjlhjUnqNGN7lnlq0UWLc1I3ZOn_cAm4bcYEdA7hbM7GuYOwo30UU0KYVPeHxFLI2elv_mDgKDWFj8xoOI7Xk7zjTZjdLHJIpOXkCBokKUvfITMqW28CAxqoGlx3hzHHKm_Npr6lmLixJavaC3hrSxG2xMAkECsTuoCEQq9gOc1YhF-oQamWwql5WTnN9g-Vm4T7-dL8VtdvgKx6WQtaH0hB82NBllzQmsGFH-D8xmZySl5cq-FqNF4TjULCewJF5jnTfHNu6E5GZSpPZnwmyPVjLji_NPeIziu3sI-h2uqjJ42Gt09wznZywI-SDfMdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل فردوسی پور
: آقای اژدهایی، خبرنگار صداوسیما وقتی‌صدتا موشک‌خوردیم و صدنفر آدم کشته شده ‌میاد میگه که همه چیز عادی است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/25522" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25521">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4009214e91.mp4?token=JJ68B73lD_DPtnowezEOUCtn9ne9gUioj_Z4_8KkaBj7z3XMb02us45e6WC2Mp7cCSkcrFECs9nMsb_REkZWCOb59oiXFhBB5U60pp0pwAblxOYjF15v0bTIPce2YRqHLLwq03dZ9KPQ3xtBD2VObFwns2biblw3ovXySNEYPag87DZ-K-FMuzsCm7JIUvtgAkjC3p-Z9xCVYBXDOyzEsoG7M6vrC2FXsK7emuxI8ywtODE-ncXJwJnXlp2XaGNY2541YP2ZLMSIkx8dJ2jMcMA_6fbvi5GuYHiHOvekb78rI3dFbRUoeLTd-8lQGZrqO4FmmKaOUFYy2rb5NxrSvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4009214e91.mp4?token=JJ68B73lD_DPtnowezEOUCtn9ne9gUioj_Z4_8KkaBj7z3XMb02us45e6WC2Mp7cCSkcrFECs9nMsb_REkZWCOb59oiXFhBB5U60pp0pwAblxOYjF15v0bTIPce2YRqHLLwq03dZ9KPQ3xtBD2VObFwns2biblw3ovXySNEYPag87DZ-K-FMuzsCm7JIUvtgAkjC3p-Z9xCVYBXDOyzEsoG7M6vrC2FXsK7emuxI8ywtODE-ncXJwJnXlp2XaGNY2541YP2ZLMSIkx8dJ2jMcMA_6fbvi5GuYHiHOvekb78rI3dFbRUoeLTd-8lQGZrqO4FmmKaOUFYy2rb5NxrSvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بازی های جذاااب
جام جهانی فوتبال
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
⚽️
🔥
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
🌐
دانلود مستقیم اپلیکیشن اندروید
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه‌ای‌مطمئن و درکلاس‌جهانی پیشبینی کنید!
برای‌ورود بسایت‌فیلترشکن خود را خاموش کنید!
▶️
‌
Link
🔜
MelBet1.net
▶️
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/25521" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25520">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ef9dd527.mp4?token=m1diO67G7QJS1-405qVO0s7_ddwXFiH7vJyIVFzqc1FQNZNX405kFouKOv1NoQOoQ239tduKM0tE2WutXfLUiaUn9NE5Lhxb4LZWuLAHo8WRq4lLIGccVLB58Ati81Fi4mfOpb0LgJJ-dDIIP8-_mussXdTkTqj0NbTZhHcgiK982235UglmchNcPsVPmwTMl3Q2pQGEIHLge3u5UX5gAL0F-QAX9QADR753yNByjvFnlDpE5P5qH09UnSoehzYxthn9mcB-EcGM4Hy-R6XCNV7ZpKPK3herB64PeDDDFb9UbDYYHRH2lzK8l1-sFyBIjTrybpE9C7ZKcNHycQAz3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ef9dd527.mp4?token=m1diO67G7QJS1-405qVO0s7_ddwXFiH7vJyIVFzqc1FQNZNX405kFouKOv1NoQOoQ239tduKM0tE2WutXfLUiaUn9NE5Lhxb4LZWuLAHo8WRq4lLIGccVLB58Ati81Fi4mfOpb0LgJJ-dDIIP8-_mussXdTkTqj0NbTZhHcgiK982235UglmchNcPsVPmwTMl3Q2pQGEIHLge3u5UX5gAL0F-QAX9QADR753yNByjvFnlDpE5P5qH09UnSoehzYxthn9mcB-EcGM4Hy-R6XCNV7ZpKPK3herB64PeDDDFb9UbDYYHRH2lzK8l1-sFyBIjTrybpE9C7ZKcNHycQAz3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
شوخی‌جودبلینگهام‌ و ارلینگ‌هالند در حاشیه دیدار شب گذشته انگلیس
🆚
نروژ در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/25520" target="_blank">📅 16:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25519">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzYC-aGbpyXz-AoD-FMJnJujjYO6Ij4hSQxSpPXdtIl1NWN1PdRtOCu7weHrpmG3ADJyBYWxZAUpFw182_LLl30MQS_-H6v6P-JHCAQZ4wpphxNdAKfB51uwdz1JnAQdDIy-ZahZ8eAzrxtlBSAnFDFFYsYZr1N2SvYK3eKN9olVthy0fbnIHvLxQJNJd8OdEAHu52S59SMtQDaV_IXe3UdDp5g_Dagiixs-uGNfNx3IbgyRK1xOcq231PSg3wMGkecUEpGpu5tDX2B1rcBxb7XoBHd2JUGFHAY43MlBQ_u44JFu_qJ5C_veKcMHFXjF3-EEdPTV70BJoVYZs7MEgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد کلی کریس رونالدو، لیونل مسی، کیلیان امباپه و هری کین در تاریخ رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/25519" target="_blank">📅 16:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25518">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VME9K4RT3iCl34PnHAZeUb9EC6RW8t8pL26tIzU6vC2jLQDO3FfBGlJQMp7GA2LX8fzSMTRmEm6UI0jHqJTsi_HloYJ66eVf-BKSNUJLhAH9OELULDrvp1pGPzPLDt10ZdhbvAYDXnJYMR-BOY0fnHfwUF4--av9y6Ygi9VH0Bk2FxOKy2GVkDdd14-C-_bgJRfigmeggljNSJnnpyr6_Yg2VQJ-5cDYThF66j5KWwxkWH1fKlNMu5VcVD6ZC-nf7LBULqOXjx7ZpSDvRzBJ3D_cAueHLsSeMfvZFLVw9j_mS1zxS5qjwDxWslQLHmi-Yv8AlkXgbzcNPf-F4cBP3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلایتی از دو تقابل جذاب بامداد امروز مرحله یک‌چهارم‌نهایی رقابت های جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/25518" target="_blank">📅 15:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25517">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HR-Ya7jPtEVUDY_6o7KAptaCbjNhVifM2rkX__-HBGjI_sk2sAzjZxBapvG9_lKJdQYfaSaThkEh1_5RXInbifakPw10nx-yYCSCuEcBnQIX4phN5a61f-Yq2pCjQbJN6KsKGaoY8gvUW7k7aWteJkNhcgOr-LcpYRu8q8AecHr0ePN7w5Deu0W0lp8xNh0SBm3pzgCBnKDlx46E5DMhplmOnYuxaNWbwTZQ6VPyXPY8HFVHMDG2FmdSS_Z-zjSe58KYUuhx5cLdHDH39PauFpUZbDOH3dOPfanJOvEcTnkQ4SDSWBot8XDVwj9vhc-iayeD5HlwOJ1HrJgHFOXnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محسن خلیلی معاون ورزشی پرسپولیس؛ بعنوان سرپرست مدیر فنی سرخپوشان انتخاب شد. نهادهای ذیربط مجوز افشین پیروانی رو صادر نکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/25517" target="_blank">📅 15:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25515">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/25515" target="_blank">📅 15:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25514">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIyfhm4-xXY6hvSXYdouxvh0AaY3xNrF6NIKkYjfCuzh1FCDDqW7pOFgjMNdl6gGVskEldp8z4rIIzJ2D5tx0xNtMd_A1-wB-4GYC8qOgo-wWcZgL9Ana6Z-7meWmW0Obb4eY8yN2VjGxVLIVrbTKCipv3Ra1JTj-SJP9xcw5XZaYR-ZllCvsv33NtB8ceO4Je92YEHCA0jTJAxv_r3FfedmjSuwX1xuC7D0dXnqS54NVOzz1XnBEShTY9N-bOeUhcDb44Qbzy-f6tXRTS8qcIiXpRdzJu5U_6660J6EHiWFJF2enXhAqBT-q6ALPrxUEpDR2dwtSAGmXHVXb-lo9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_پرشیانا
#فوری
؛
یکی از بازیکنان فصل قبل پرسپولیس از دست مدیریت این باشگاه بشدت دلخور است و به دوستان نزدیک خود گفته اگر پنجره استقلال باز میبود تا حالا قراردادش رو با آبی‌پوشان امضا کرده بود و یاغی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/25514" target="_blank">📅 14:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25513">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reO2uPjupq_eo93p1GYsEVDFlQFxvS9JD6Cxh8Nnxc7-4XHa0NN1IAoT2ZLXXSPQ1cRyzFuoQ14DIJt5jpuVey9in0v0vEcKvzTNEt_bupskG3jp9aoe7cwJ8Fq9vw9yQao_wwpvCDWjU8C-37tgyyi3VbHj76HUk7GH-AeRB8m6WbZ4QiKzMYY9WhPqDmpdS6KAOd1LJww-50HnMboCVCFEX8jAcF91Ak331d0m5yzFqDHzziExauNUvyKi9rCPzsHJNa7Eb6gyoLZjPCBavWjqq3OtUFq65VTM2fHCn4CCpyWi8EfI1VzkRFVnI-I2SULs1JgOIIpo-ZT2BQX_wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد کلی کریس رونالدو، لیونل مسی، کیلیان امباپه و هری کین در تاریخ رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/25513" target="_blank">📅 14:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25512">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60fb9d0fb5.mp4?token=LZiq8C26xUqwWxclyEhVH04X-F22nB6ruYfYsVcuPlR-qL_KvyNknJeljeJeLL0bKGva1LT98IeSblxViIhkzqFT88Ucsg8_pyuiVU2tqqpiZzHJvXVG9QMjakJdo59DgJB8K7r47cKii6V-zfvOiNwBa9x9T_-_j1GhJ3vHxfb4aeEO9Yda0baYHD1cgh93F-G6XPiJ6mi4HGW034x8eL7HEHy7jePehmUqmRNtjojJAZS_U4OrdSOub-RjPM8uPDJgwrfgdpXShSIVX1CUZIfTqfVB_AAtUTO2rmu9z-0zOzHN7BWjlW2ud9rUG6k6d3zGHVC8FHqtPr8DTphgbVKXO8RG2cN3r-v2VBPo3FTiiQpmQkflqZ-0UjqVDCT_Fyw8Xbyyy_t357qAcB0T0WZerMEGAhPdJiGOYoQgUX0VI4_q8S4alLHXFMyLFtmoUPd-vHAkUn4AcqmQpfjxxEeoTRaq-scowcWiV5dhd5pIIf3vGMZtEWFcPspl2TWqMBqCwQc5KrHh4QZU5oPPit2BG2pQVERPj5TcJeMs3q6GVCgS1wKf-gwnE9gUtHzaGJ56QrrLELiDCinbX4EqV9957cuII7s2Q9hEI1qdJ8ppExin_xVWLCfQ7iSw1NBRyjwb8im9FjJXO5LF3YGkulfBgP7ARlzV7m6ufzvU2Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60fb9d0fb5.mp4?token=LZiq8C26xUqwWxclyEhVH04X-F22nB6ruYfYsVcuPlR-qL_KvyNknJeljeJeLL0bKGva1LT98IeSblxViIhkzqFT88Ucsg8_pyuiVU2tqqpiZzHJvXVG9QMjakJdo59DgJB8K7r47cKii6V-zfvOiNwBa9x9T_-_j1GhJ3vHxfb4aeEO9Yda0baYHD1cgh93F-G6XPiJ6mi4HGW034x8eL7HEHy7jePehmUqmRNtjojJAZS_U4OrdSOub-RjPM8uPDJgwrfgdpXShSIVX1CUZIfTqfVB_AAtUTO2rmu9z-0zOzHN7BWjlW2ud9rUG6k6d3zGHVC8FHqtPr8DTphgbVKXO8RG2cN3r-v2VBPo3FTiiQpmQkflqZ-0UjqVDCT_Fyw8Xbyyy_t357qAcB0T0WZerMEGAhPdJiGOYoQgUX0VI4_q8S4alLHXFMyLFtmoUPd-vHAkUn4AcqmQpfjxxEeoTRaq-scowcWiV5dhd5pIIf3vGMZtEWFcPspl2TWqMBqCwQc5KrHh4QZU5oPPit2BG2pQVERPj5TcJeMs3q6GVCgS1wKf-gwnE9gUtHzaGJ56QrrLELiDCinbX4EqV9957cuII7s2Q9hEI1qdJ8ppExin_xVWLCfQ7iSw1NBRyjwb8im9FjJXO5LF3YGkulfBgP7ARlzV7m6ufzvU2Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اگه ایران میزبان رقابت های جام جهانی 2026 بود؛ این مسابقات جذاب چطوری برگزار میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/25512" target="_blank">📅 14:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25511">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDObvdSp8zY6p6LC7ow0x1a_0bV83UC1Elnx088WXaLd_u0qWQGVKzGw4t-2b9GoY7ATLMyBJcRQpEIKhhsIcBWKPPDWnDvSSzoJyIyHCAHpNxyiFf3WlQpRYQb271smZPPo0AC6XG6hGvRI8uo6Dyl7lWGaxqNY3yvKWSehWbPdTNSc5kp38tZPoCasaFr_JYSa8NCZc4SlL7RZ8knsSE6rFybCschcULan_o3rIxaTOyJYxYzkdPlefgGU-hwcbznt3Trt6s4risoUIvWrMps2yj_MwHy3SWHupWUE1KMywMbAsUq8E06QecMR42A1E8uiVHNfS7Nw_NS-ddlzVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مدیربرنامه‌های علی نعمتی؛ این مدافع ملی‌پوش باباشگاه‌لوسیل‌قطر درحال انجام مذاکرات نهایی است تادرصورت‌توافق با این باشگاه قراردادی دو ساله به ارزش 850 هزار دلار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/25511" target="_blank">📅 13:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25510">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6wXzthsNyrA1uOoPxZ3XrZ6XWhtRvU7g2sVuHWzXk0z7m0JWg5hdMZKJrku1jm1kYHFYvSZdCwgljV_0AzsbNXrdth4LqwYFlAHf46Heepfrq5My1SIRceH541IHbvAKKfPvrwb02D3kiRDR3jv-tkmz5zxX4mbRS1Z2hoejZGdEuBcJPkTbw8gKN_joFoQe_4L7r_k7TJodee8Rr5t3P8XLcBZhnqCUcbqR9kx4SYhfTWuksJeuP72y_lUzmgzy-B7VoZea5yeiCclqIPL6Qa6AB2zqPOFnw-KmkAYbA0WNJnnw7YSOrzY4-E6MAEmuBZc-YkJ012q2_4JqFHhFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ آخرین پیغام منیر الحدادی به مدیران باشگاه استقلال: وضعیت منطقه آرام باشد این هفته به ایران باز خواهم گشت امادرغیر اینصورت باتوجه به شرایط خاص همسر و به‌دنیا اومدن فرزندم نمیتونم باهاتون کار کنم و ازای فسخ قراردادم مبلغی برای شما واریز…</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/25510" target="_blank">📅 13:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25509">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkZ1Ldb1GlfROK8STbZawO7U2kpYNA8Hr-weRwtjf3ib5dT3JpTvtrRWk4LwsOg3aqCgGyfgErdgrJC-iw9ghIlVHvNqRNTsKpiUHxPUNKDRtAQZH2Nae0GMO_aFSHBgPGDPLjTNvWudSCtnZ8cNT0j-WRq3OH370synbj5T1Y7a7NFTlIAUfTGA8OfKdmDwxv2PzC4LOhX6MRJBJa9jbzixBIWfzqhzPMbIJgELmsI35fPEWCtnVg_aN-4XRzbO9HTCJOt-Ao-HWfeUt0cX4bvZCWOgQar-DAmTcQ3e6_6edpSYVMFblxFKfoz0sP18eXOW0wzD2J4nIR1xL33S9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ مهدی تاررتار نام سه مهاجم خارجی رو به مدیریت پرسپولیس داده تا شرایط جذب یکی از آن‌ها رو فراهم کنند. بزودی اطلاعات دقیق‌تری درباره این سه مهاجم میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/25509" target="_blank">📅 13:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25508">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErXHRkzj1mAxWJQ_ujYPoMLm0TdgFWQ_W3ek6GjauM5JCEJWNz1_HcsKEX2oH4tREVkskr3RmORCtyIq3xpIn2SjsAevKvq-Bk1LGP8HLHPWBgFZbtXViLqN6cwYtpagNQ4XUOiQpBjn14Hs6CsvzPLuzo0_MxOJr1Gn2xIqYiL0G5_sUKJbdwzrfJTnAxrxi45EfMkLtv2WODo82cbPyt_gUoGs9X3Kl9TyXDMRsqMHchFZTK7DxZYOhnlNlg4vvmoRXqLPnPwyu_LTbVRrkzxpnMUj4FeiVgVqLGZmsc2CV5D-ftHXbhD95YngJp0NQmJD8acDms1ddjLfFRLEnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25508" target="_blank">📅 12:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25507">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3yn-09Esruwb5e6Gqybdc_8FsQJRfidqMVtdIGxHeD-wqTdqAKXl2GUzUlXGfDdmWwDs39dNFiHFzbz_UYb8ysFXo20zhs2IgW5D-XZLFM-K_THQ71dSGUWOT-vCnqRJlj7HobrHeQtQp5jyyCk7CFRFSw92ZMMjL3BvJIJYERDv1TbJgMlRHEtnoTDv81smrHziog2JfY8-5oxGV2ohoRE9RqEl95OBZKQxgjlFHDPNRBVvdHgXwJ6KmQKRimVFJlf2fPyjGVvsAAkXRTPFRU7cw4m5-HTP4fzNly3lGFZ0EGsQ896PJ1t1A52UzSYQsv80JSg5vtKyCYpVHzYbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
عادل خان فردوسی‌پور پیرو خبر دو روز پیش پرشیانا؛ مهدی ترابی برای عقد قراردادی دو ساله با مدیریت باشگاه پرسپولیس به توافق کامل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25507" target="_blank">📅 12:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25506">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6pirnEhanEAfdU1fFgMrlDSrHTWqVc9_8CX53tnuyVivvqxBNwVT59aRqjAxaQ3z1nNDHZv_q6gqS4DHE4E925jLKZv2EPdYWXGjaXa9z16Ekk2bviYc67MKKkEMaWlzEyCqPqR7yGjShx_Ca-t1Aeudy5vkljMhhjnGsAA2hw-6c9yExYQIIa91AJT9AJHwyvklPzk1N6K-0c6UmIGICYbC1QXlooidCx8602rrpoO7LAl5xwUzdZ82EHmh16xv-Dd2mHY3Ga778z-k7BacvvDz3ACqSdyFVFiuEkAdRxjPdfaz4JDU0Qbwe7tIdZQux4cqg7svitn8QYZ8vWS7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا
#فوری
؛
سهراب‌بختیاری زاده سرمربی‌تیم‌استقلال روی جلال‌الدین ماشاریپوف نظر مثبت‌داره و به مدیریت‌آبی‌ها اعلام کرده قرارداد این ستاره 30 ساله‌ازبکستانی رو دوساله تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25506" target="_blank">📅 11:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25505">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5482437b.mp4?token=I80nTItZNdTCKkfuSLXF8wcSU3FnQl5Feis8oFZZVxoKFCjgDmxdAtmJN-QB7Dg1ZV-3QsTRbX7KHLrFpn_7vGtN3Me2zCgmupIUrFRqJ1KBH4WdCjp7M6DV3cQZkZ44LWT2cznpUfnZaO1p3flpz0DvcAH7Zn9P_A2SU_OhFdgpjZ7c1zYIPGILWATPIJCK2hexTXt-zhvojkPq9DdFAEfh29sMCcpGlT9HSZCt89DolNZ-oWsXKjrBUk2Ay5d1yrKqQEt0_MXsXIRXy8csBWrr0llyz3UiX8v0aVAglAKth_CrcmnLL4SC8dvdQbFVqGlw0R1I8Crkv6vImf-B_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5482437b.mp4?token=I80nTItZNdTCKkfuSLXF8wcSU3FnQl5Feis8oFZZVxoKFCjgDmxdAtmJN-QB7Dg1ZV-3QsTRbX7KHLrFpn_7vGtN3Me2zCgmupIUrFRqJ1KBH4WdCjp7M6DV3cQZkZ44LWT2cznpUfnZaO1p3flpz0DvcAH7Zn9P_A2SU_OhFdgpjZ7c1zYIPGILWATPIJCK2hexTXt-zhvojkPq9DdFAEfh29sMCcpGlT9HSZCt89DolNZ-oWsXKjrBUk2Ay5d1yrKqQEt0_MXsXIRXy8csBWrr0llyz3UiX8v0aVAglAKth_CrcmnLL4SC8dvdQbFVqGlw0R1I8Crkv6vImf-B_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
تلفظ‌نام‌مدافع راست فرانسوی بارسا در بازی شب گذشته فرانسه مقابل مراکش توسط عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25505" target="_blank">📅 11:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25504">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIN5sYFGN7LxeDxtyjk4r0VxcfOGKcmWH9o7brbG2Obdw_ZzFq20G3yDVsM5evEuKz5xVXFZjnfVGeaYauFkXf4iiH9pkrRFf9HyVK7T9Zhf6ssCjsxaFe1FmWJoryD_xYjJHIeGfWUkGLgr4fiWjJeDiNvnzH5cuTvwW8KM8JP2DWugOrSj1PeAh_rXvTywr4vr05f6xksVR1-3is8i6GQIXlWc8dbiErfB0hm3t_sxedKo_DYGDMsl0mQ_zlhmRuUd9tJlAFh2fbwlI_f4KVSU8hS6_gCNKAWHgojqO6knzefD4UUnBLCIxs_hadnX0CpkPXG7N-51daOQ0m0dpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25504" target="_blank">📅 11:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25503">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjs5bxTjsfcFshbPqq9BCg5u6eOW6GOx-hsPflui3N39Zlh9UbNwsktDzrbecJmsJ9OBIT_ROIhdjkz7DDOSDu4jxaA2U8XiQVUNXBqU07bASFXexGfeOVvywAn2ArCEqd18YDN30IwQ2TIxQ1aw3Fr2JxQiuml0_IJetemYwBWnU6psXQLBpOssK_IxE79Nz1pPu4aWmwnC2q9__geMP1JmfXCvGmHQUfGbCnCRG8rG8VH1wW-F80j-EhkXG70nifxoN4edUFdpcteEz6WoW-esrc90iN68vlAJM9Q_Vh90hl5tH7Vc4HWw5ltb3_c_luSiVVzoCG4Bh7XZ_7WHYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25503" target="_blank">📅 11:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25502">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=JK3WHqBfwYN4gj_TR7N7vm2a_Kw9qpeWi62HkJlilACXSsn5p78PAB8RYrjlDsFZcNrnL2fsmHOsFe98sOBygHSylDU-moR7X38ZsBkqH283aXbGGmVinMAf0mB1qZEgf51Hyp1brcEh72MIqQJB04mZh_y4XwJ72I6sTS4u7BeX6YUqDaq7nXnrw91AhpMNARA2F4WOdQG5dkHZxPFGwH_w2sI8XjtEwixucCn4FQV7i-HWAzsDp_fuyfOCShKRKXpNBCrsngGSYcuDaOh-1QN-JppYEI29lSgZg2Te8ZrKldacnMhc0uhaqLYmSq36G8c3fi5sd22J-1bF7z-0pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=JK3WHqBfwYN4gj_TR7N7vm2a_Kw9qpeWi62HkJlilACXSsn5p78PAB8RYrjlDsFZcNrnL2fsmHOsFe98sOBygHSylDU-moR7X38ZsBkqH283aXbGGmVinMAf0mB1qZEgf51Hyp1brcEh72MIqQJB04mZh_y4XwJ72I6sTS4u7BeX6YUqDaq7nXnrw91AhpMNARA2F4WOdQG5dkHZxPFGwH_w2sI8XjtEwixucCn4FQV7i-HWAzsDp_fuyfOCShKRKXpNBCrsngGSYcuDaOh-1QN-JppYEI29lSgZg2Te8ZrKldacnMhc0uhaqLYmSq36G8c3fi5sd22J-1bF7z-0pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
نروژفراموش‌نشدنی‌ترین‌تیم‌جام‌جهانی۲۰۲۶ بود. جسارت‌وجنگندگی‌کم‌نظیری‌داشتن و شدیدا دل‌همه فوتبال‌ دوستان رو بردن. به قول یه بنده‌ خدایی اگه ایتالیا مدل گتوزو تو اون گروه اول میشد جای اینا میومد احتمالا این مراحل رو به چشم نمیدید. من خودم بشدت فن ایتالیام ولی خب مدل اسپالتی و گتوزو افتضاح بود ولی مانچینی درستش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25502" target="_blank">📅 10:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25500">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsc7_WqgsnCTNwdAUYGxmBWY55pE1AomIYjgbVSmBqOrhDNC8uk5h46_QChUy4PrYuyqt2kH3JwWXS2TVV47Qe3wDAGEB3m3Cg3m2Eo_4qxKQln6yzIFmh2wlaVQ2xkPvfDw9NfUtbbGiuLL5yCzkHmOni0AGEC34lmqhSLf2aqymrHOtpehmjIuH_eEQt57q9Q105p2CzoYJYo4wSdJvjZX6Qg8Q-SjJ28_4u6P_hGjAXJ9PddkFHTxXXMzIQ2E_SZMgrCGJqBUQWQiHDklkCn8haW_35EOzSksdTf0BSPwmDlW8fUWBOgEc98rTRjXnafxG2FcF6yzGdISelWPpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=Giiw11oOwBugb-O7_1HAixbwjxkxMRpLIcNhwlBYN6bgqIyt9hy30gJ3n46aGMQUtmE7Tumz4vxYqIFFRw-Eea_E72NHRZiv-vP3ZAqaoYC_nnu8c25ahhpekVbhD-g83Km-NMcZrMa6nUEfQuv0s170KRX_MUberzWXErFU5j9zYWp_bbyq_s5_aqzOUlIr0D2FkbYAG6O47kKzxWmzPelzumoq14gsYLpK3kEy4b4tROKRBoO5FvVHHxtZ1ccY34nbrSWivgcnK8IKuHJp-u6sVfO2ijFS0roYCy3BmLIBRTLBi6agBsQIIGfhtcddcFT9ZBaoRGszSf6oC9nrcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=Giiw11oOwBugb-O7_1HAixbwjxkxMRpLIcNhwlBYN6bgqIyt9hy30gJ3n46aGMQUtmE7Tumz4vxYqIFFRw-Eea_E72NHRZiv-vP3ZAqaoYC_nnu8c25ahhpekVbhD-g83Km-NMcZrMa6nUEfQuv0s170KRX_MUberzWXErFU5j9zYWp_bbyq_s5_aqzOUlIr0D2FkbYAG6O47kKzxWmzPelzumoq14gsYLpK3kEy4b4tROKRBoO5FvVHHxtZ1ccY34nbrSWivgcnK8IKuHJp-u6sVfO2ijFS0roYCy3BmLIBRTLBi6agBsQIIGfhtcddcFT9ZBaoRGszSf6oC9nrcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25500" target="_blank">📅 10:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25499">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/op8PhbyXCxzA2NRx2tJ8DPbwaQ2TX7J_-Buw51d38D2vmsTH3gmMfZQcf_Ua58-gOc0vhrAijeK2JnX33pUg4Ev2OPLdNb_s99Drx_O5OkJ3pGBQsKew5gFIwFJbx50cD50Y-X8y22W9nPb8RahAnPMMjD4GQorweBLzukinh3npWz0vBdFN6ShHLDUbvnr_zBR7cg_qlqQ6kvEMSbCvlr6mn0TaAxm-kJl-pC3m4W_gRqJ5EcqlAw7X8ted1CXRzLribHjIJlDCIiI1Ykfwrx2d5f7ozZWXOATZ0UJgfu20e0jE3JpyuCLzrkmdHOoLaSe-bCGMBpVFIjY5H9QUsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25499" target="_blank">📅 10:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25498">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5cz05sCyvQQDN33i_l7jOCcsq0AXHa0Xetpg8iY5xVWymUEsfTN3PVYJk8ZGHEgLSgw-2AaP9r83apWQlcUdbb-9qDHa2eQbpW2QUcwh54g7FQS5sua-EArfZ-hw7z3g6Jv6PMpGZNyiktWNSZR9uFuTHxmqvlEjATTQBbn6FhSsEOSO_7xpH1LfsrG75A-w44yp6tvFha1VF7pNbbWldnjYwugVuds0jNdP5CQ2-2pzeBZsnoctt_EKWxk0ZvxD2f-yD6_fk4Z5LRcnU09LR8yiXPmy1QFlcITtJWQwqYSTSpXVuzgUeRXihTSKvmFyPQzAlk7frDxswBgjZd4Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ جلسه مدیران دوتیم‌پرسپولیس‌ونساجی‌دقایقی‌قبل به اتمام رسید؛ نساجی‌رقم‌رضایت‌نامه رو550 هزار دلار اعلام کرده که حدادی‌امروز درجلسه‌به مدیرعامل‌باشگاه نساجی گفته تا400 هزار دلار حاضر است به باشگاه نساجی پرداخت کنه. قرار شده که ایری…</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25498" target="_blank">📅 10:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25497">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda5f52119.mp4?token=ZAPMsglfKLf0TGNVW23NEsUd_3ARFmOe_MqVKE0FJiyVknqgbK0bL-LFO-xpQalNoRy2YGRXmgmuS1cM0Ab_hcA2yvo4XlxyqcMuI-33Qng09EZL5qphnX0IYvpe7cllUZnTyo9fN0gGJRmTzT4e63D5MIB98COy8w4GXR-K7KTgEGVneU4qPX-C8zj4gZlFBkUoFZY3fHQv94_hCEil6EgeZO48XX03WFQxS468BRQzIHcufcf3IPn2VHyEWr4S3CnJ-CuleD299iPpekaVkr1XA5oxi9eCPdzQkr2MPp-NdPq_6zI0z83nO2Owhl5jkKxmMcvR_RQaczPMyJzR8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda5f52119.mp4?token=ZAPMsglfKLf0TGNVW23NEsUd_3ARFmOe_MqVKE0FJiyVknqgbK0bL-LFO-xpQalNoRy2YGRXmgmuS1cM0Ab_hcA2yvo4XlxyqcMuI-33Qng09EZL5qphnX0IYvpe7cllUZnTyo9fN0gGJRmTzT4e63D5MIB98COy8w4GXR-K7KTgEGVneU4qPX-C8zj4gZlFBkUoFZY3fHQv94_hCEil6EgeZO48XX03WFQxS468BRQzIHcufcf3IPn2VHyEWr4S3CnJ-CuleD299iPpekaVkr1XA5oxi9eCPdzQkr2MPp-NdPq_6zI0z83nO2Owhl5jkKxmMcvR_RQaczPMyJzR8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇧🇷
وینیسیوس‌جونیور ستاره‌برزیلی رئال مادرید امروز 26 ساله شد. او تا کنون موفق به زدن 128 گل برای کهکشانی‌ها شده و همچنین برای تمدید قرارداد بااین تیم با فلورنتینو پرز به توافق کامل رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/25497" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25496">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qi5rcjBx9GKaTsgPb0Lnfhrf1fPSELRhBGObPb59Ys8CnrbExPaMKN-9mMdKPWD-YEGgT5AZj7wpsCjgKGIpmbCnkC2XCW51-w5ja06e4gHveWzBCP_KGllLi0NrgM4Lxae1R6_0jmqNO__ScEKFYcx_PJXrYsniFSgyMsk-lzKr8fxI2cuVe9kPg6kbq2ydaeY2Y4IsScOwP52TF6Xwzuh3Hsgu2FayXigKcoD0S_d2Mr6-etEulpusfV4iXGbMSdOS3Y2q8JM6kNYIf1GagnltgQxcxn5fFZDzTnh4nf9NycRQN40FQXIjxplor1kKTZrtq1PgckB2SDZGSqx-qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
5️⃣
میلیون‌ریال‌فری بت ویژه ی فینال ویمبلدون
🎲
بدون ریسک در وینرو پیشبینی کنید و از تماشای تنیس لذت ببرید
🎁
🎾
فینال تنیس ویمبلدون
🎾
🎾
زوروف
🇩🇪
✖️
🇮🇹
سینر
⏰
امروز ساعت 18:40
🚨
ورزشگاه سنتر کورت
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
بابیش‌از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده!
📩
Winro.io
معتبرترین سایت ایران
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr21
📩
@winro_io</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/25496" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25495">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e63b6abc08.mp4?token=Ojbey0Z7oYrmF44Rnfd5dQN0UXmXbTAdTDbXoiYSSruLC9UCC7LvbEku-smAc00OFimLkhaU1FbvlSPh9o4unwbjKAHvXyH6r23ugyZ2GKioreN1CVq0NOxnLJpySWg1Ds_PYdUg_1lnd-4kUF5DCYBPIaic5gaFI-0SOTMjfRFkGwFvjn1t6KM0YxGvWAFF8bv968PADzJ7Sm7ceKZTd7KGtW9BoX-CF9k_s9veCVPzrCwiEFxjk0HLgFr6Vq99XtGk4wRieUGVUcxhONK7djQVFjZMcHh9t8hG0d5SzWsLACOg22P-uvvz1082boWqBz-gOGvw1Gvgrm33HEjZ7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e63b6abc08.mp4?token=Ojbey0Z7oYrmF44Rnfd5dQN0UXmXbTAdTDbXoiYSSruLC9UCC7LvbEku-smAc00OFimLkhaU1FbvlSPh9o4unwbjKAHvXyH6r23ugyZ2GKioreN1CVq0NOxnLJpySWg1Ds_PYdUg_1lnd-4kUF5DCYBPIaic5gaFI-0SOTMjfRFkGwFvjn1t6KM0YxGvWAFF8bv968PADzJ7Sm7ceKZTd7KGtW9BoX-CF9k_s9veCVPzrCwiEFxjk0HLgFr6Vq99XtGk4wRieUGVUcxhONK7djQVFjZMcHh9t8hG0d5SzWsLACOg22P-uvvz1082boWqBz-gOGvw1Gvgrm33HEjZ7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/25495" target="_blank">📅 09:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25494">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCam8NhIE61shhlp7IKrnt5ycOtv9UHDFMBRDReXAt9z96E7Cb7xqOOohCOSarHNMLeL1YeGOOvwowl5FN8Hsj-Z0iPA-7RWpRpiVy7dOsII2ZP2uTUlu7z37TKMeQUqyzSjtvqIQnl9xlkRReOl6rjaj-eJTgSnxMTiH0heV8gjAKmbE25AWKJ_p_I2mAt1EnObiJ9IUsTEW3kP7dH7YDXwH0ZVKQrdNGuwsIQGLvUYUzKumz_m5q-qz4a-wFkddnjhZND2i0qphtzF2kiAKJIXV-x7HwKmf04FWXBMtMOZy34n8OAEJBFKUtuLqWC0b_PFwbj-2coRXWxhduJh_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/25494" target="_blank">📅 09:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25493">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XC0RR3O-WsF244sfCDcXk-iYpQWz1ij67YCG4nQIE2LjSNIMc-E8uLZ7xVTqJe-FgaBsYFsU9CAXkB69ZsCVhAwUEfdLrpIUpHSlbmjAluCtes4EsKnpuyqqSy2UQBt1wReqApia_iQqugUdXQLdJlGYyhx5NYg2wBrV8SqMmGx1-z-sIf9yz5WhSZuA3Moos26kHf0EZmq7V88CadV0xn07msQxVB5mc4-eULqjuVEBS_A3K8Zpx97ozQrNtzvpwVRO9zo0HFqTFXR8pPDHgfCjs0u9n-9f-1eDSM0xnTZs9uOCwU0JmA1g2Mib2f8GrwYGQlXBnEt2Tjbi_A8U-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی‌رسانه‌پرشیانا
؛ فرزین معامله گری مدافع چپ پرسپولیس بعد از تمدید قراردادش باسرخپوشان راهی سربازی شد و در فصل آینده در یکی از دو تیم فجر یا ملوان بازی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25493" target="_blank">📅 09:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25492">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0c6aec402.mp4?token=OxS5pln_9WuVipuUEKlr8uI_lJaRgPz45eQkwylKSYvXRzvaOIzbhhYWQfXzAJCteq5T3k0mMuD0raItEi5AdBMB_fgoYy1RxCF4ftSTF7leK319AYh7na4r5CpIuJ1ThN_AOc0bpuoSHMpbRcuGSRG0ppgECP4nB0CUQJmRC_v9AWLG2jW0rqy-hkBxWMocjbxuDAbry_Wgqm_VayiRSLNeKIuMNxuOcg8MAxDUXDw6WJI-X1mGkFYdTgwUFxhVGTb9iHACdQtRk_htzK7tRTLVDxH-dUPOoxbpQgnoWsGc6mqQQxYaps3zZTB-uZMwVlaoVYfFghIWihk7g2FWaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0c6aec402.mp4?token=OxS5pln_9WuVipuUEKlr8uI_lJaRgPz45eQkwylKSYvXRzvaOIzbhhYWQfXzAJCteq5T3k0mMuD0raItEi5AdBMB_fgoYy1RxCF4ftSTF7leK319AYh7na4r5CpIuJ1ThN_AOc0bpuoSHMpbRcuGSRG0ppgECP4nB0CUQJmRC_v9AWLG2jW0rqy-hkBxWMocjbxuDAbry_Wgqm_VayiRSLNeKIuMNxuOcg8MAxDUXDw6WJI-X1mGkFYdTgwUFxhVGTb9iHACdQtRk_htzK7tRTLVDxH-dUPOoxbpQgnoWsGc6mqQQxYaps3zZTB-uZMwVlaoVYfFghIWihk7g2FWaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25492" target="_blank">📅 07:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25490">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mBpBjrR7VLTjRd6LntQtvTmXrLjJDBexlXt3XSVEQxNqCtU2WQby2_yRQ00CA9H4nI5pvX9_ESJqtLWUKMDT58ickBMx1MKZ41G32r3JgT2YJEVZVWjujOXWVd8gNfFKxtZPpOkAa91L1_FRzNTphUSD-YbnP7ie0ot9ZDfY1ttG1KJPJHDKqVtR8CHo15SkV-UNKRkKrj4g1V4nHPukETkc5jbAxo_WpO44TDabmDoZ9iqFv_2saqr2eBFi2W-YeYLE46E5AE8jCyiig3KURIkmYa5uHrrHW3SjDit9xWmdQrTzQWK3EBgkA27AS9Eff32Lfp-uVUuArtC4utxSmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J_qG7F7x1bBRo6PyjSM1Di8x5c7auLAwBK2d7RmqZmhXq9WWwdIGjPhgq4KLk-iGG0KRRjyLEcxFEvXS7ZGTlDBxrIa3Dy0TrO3wXsqBlBrkHTX1Nu8dr77Cy3sti3s5VvAxOxa5MnqyTJtdMntbOwMip3-MhtQaQFhuvmJ9UeRKXNGFigTWFjo_Oms91KC9jqCFUiMy1KhuX0PZQLywBCa8mMbX3qBuBs0cWc9dTFUzzrs8YUXa6Pfp_ykaNKNzp-DOfHn4BvNDD8SE_JQTF_CU156fj8u5kBH4C-bjFibOyn6CxBv-8T8eKBo3XVFG5WjO8_TD9PbtQ4-nAHnbBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25490" target="_blank">📅 07:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25489">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8bsEM7UP8ZuN8kaNgUYQN7pIlj2cyflHMissfuP8C18fEdOvRKragqA0qc4OMY5_R60jtRu9O5OHUaurvkZ9KZvocZ-_wMgCIvnRA_QwBFjncanfZkCJCr2AIekzOnkFXIb0ml92g2bG0wZ6j9N5gbD9zhlWxPKxIQh0RgQ_-Bt1X7hcXVVGRGEb9jYTs4xixKeX6XgEAamJlUN6aYE-DrcPeIuB51WWMZiKPIJnbX3632mFhT4EJg_hQPkERBWKW5Qx6wbMehaHCVJf7-gIb4SnKQkSCkItcUXXvZzCaFPLkh3GKIyfSmOw8yGUpFGzAJG_3jds2YyKySfVYyjHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25489" target="_blank">📅 07:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25488">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_BXA6loqpM_txWtA9Bbs0TBltACf0FJG7hnxcdM5Rvn_xVnq7LkWbICeRNx1K-HmYivX83c9stLEJxSPLn1QEwA-vS38jDUHx7BdnlfHu9_sUsVB732WhAZR3q600mxnwXOINcVxyuvBpiZDEgUHLv7yQzlirCY5rnK-hbYzGU9GSFVE4a0I6YAhowUXcAlDk7BJbNRvqEyJqMImeHLmyFsOjih9nuKO3_VnBJU87y5kgsWjewSHN12keJZMmk5RxDuJTTJxQM8VM45gUu8QbPPowCL-2Z2F-x4Utp6-kEJ0gEl1fA8olGVGPiSiOTiHpZ3Yw1RP3F--gXOv72Y3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25488" target="_blank">📅 06:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25487">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHuTOpdKSUxvNjUOWbozxpnnAFVT6zfgPCxxeiG0XIDRgS9Yye1QYyibIeKblobYJuQIjXcNoslc7tiiDvpGZgZgNtauiMJAS7s_RgX0cMJU8QNwVDTmRr619ONAHNONnW_n3eMfDLPhqyQS1267HKFIPcrO_edra7O9zvxOBFhfKdIf9Mm2rA1bM9LWXjEOSLuhBLMxVMw-l2B7DvGTCau_4JyMlqu3FITogWn_bI1PXk2bWx5nqtgdmGfPdrakt2Yo9I1yDpRAdTActYqYSNWPDcz9XRB34zbnazo78BFqWMW7ix0JGhqwlKPtLozZ1PaD15JlXWVXEIaYnLZBCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25487" target="_blank">📅 06:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25486">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcR6_mOgBqhmIbQicjw1J6gb8yD6_gpOstgH-R4PTvYY094kvb2PiMrh3Qi1zbLUxFF_E-Fssrk8PBC7fxZ3FkLy77teYRYIW8LIM_q60vhVTy49_2k29bnuwdd8ni7frxYV-iRCNrpPjT-nX9wu3192X21NnoNZdnvCcj6ikypz49azy7tTr-q7amkCDdnMrGgHL7O7k-nyz4aaLnlbq2tkmAQ-Hmjh5HJjBg0DMGckJEOu8i8BYCHFUAYso0zmt_pLmClII-bTOVePh19316-rzJciX35d8v4eyKAR_IG_mvfBgPBHUqejUqpsTLM_stajbh3VXbCxaXRa1HicCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داش‌چیشد که به این روز افتادی؟
چیبگم اون شب جای‌درس‌خوندن‌نشستم‌بازی آرژانتین-سوییس دیدم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25486" target="_blank">📅 01:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25485">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=sF34M2Bi4KlVmThMITVXZ7IrDaz8km6OuQTIfz5CVmhdP59cQ6wBotyi9M65z3mnZWwhON5M55tKg0Z_-gyvrq41C4jJNINZAS0rcHLEq-Be0O5z3wSMyDddNAjF-SzcoChVmq6_7AOFUHpx-Yd03GxoXlndYRgYCqfhN09xqUUw40dAhpctLIFHTuZ8q3xi-mZaIGFlTPOPnVUhNm5miAJ9xwe3FGv_WeGYuobExs9315Wm4vJizmbFCYhF1hp-YVgBHv-jUX7SCT6sFyd_4acx3IlgcfAqOdDBV2_QHf4D-3S0FGvRd2_PPe0uJMqV7-w-VQ_A8EMSxZEHuWiJJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=sF34M2Bi4KlVmThMITVXZ7IrDaz8km6OuQTIfz5CVmhdP59cQ6wBotyi9M65z3mnZWwhON5M55tKg0Z_-gyvrq41C4jJNINZAS0rcHLEq-Be0O5z3wSMyDddNAjF-SzcoChVmq6_7AOFUHpx-Yd03GxoXlndYRgYCqfhN09xqUUw40dAhpctLIFHTuZ8q3xi-mZaIGFlTPOPnVUhNm5miAJ9xwe3FGv_WeGYuobExs9315Wm4vJizmbFCYhF1hp-YVgBHv-jUX7SCT6sFyd_4acx3IlgcfAqOdDBV2_QHf4D-3S0FGvRd2_PPe0uJMqV7-w-VQ_A8EMSxZEHuWiJJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
واکنش‌جالب ابوطالب‌حسینی از رابطه سرد بازیکنان تیم ملی پرتغال با کریس رونالدو در پایان دیدار مقابل اسپانیا و حذف از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25485" target="_blank">📅 00:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25484">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtCR08oEMIJS6616fgMCBQm_h7uAMrnZ5DPk7IV52vikt8Z_9Vv66N3FZ9KmN0WjJHrABfZ2LW7CE-tFtdV29mtD98E0U97tnYrryVOYJc0lgOeic8Ri2iAnFihRH6DEkkBelTjG5H9DdCQNF35m2YqMLF0K5FB4O0KG7DawsUZHOkl1SUKjrm8vUeF8ooYT87j6sXSrRO7n1cTR3c6iLH3fgfzo8QAGQCmzehgkKl_EDZeyk_Sqkw9dVEqFlHv5TeE5IEiuOtGWZzbne6TzEY5Qbwlbn_1UxLzbnxyahC5aGJrtl1c3N-4JrPgY4WKvb-klVg0cOuMGNBUGV-o6rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25484" target="_blank">📅 00:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25483">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfqFP1D7wxCsmL92ONlaPIY_d0nyJ_b9bnJanFV1-RhR5CYX264hHB7-ZfhXcwblvjeL03IfF0IyQ-TxOWMbX7VJSYr7j-CYf20k6NgjXFrPAGGObK3YywXTo7QxtBTe2Ag1HqNm2yjMRVlE52JeVAgY_RoUh2BW_3HN2QnhvtvfegBQTQmqKbsnZ-_8DZwnQ4alJRK_I0B0iuCpjHjyoS6Med25xu8D4_aZHL16J03JYIv04c_VT3iKcDSOFNwnXIJaXtryX7yLwnyHN31sql3uS-6MswnJz784LaBOcoxWYyqEkfKwt95PT3cTeHZq1eCW90Ihb8LOBSa2FwY96A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
دوست دختر کریم آدیمی هستن که به شدت طرفدار باشگاه بارساست و روی انتخاب آدیمی تاثیر گذاشته‌. ستاره‌جوان‌دورتموندی‌ها ساعاتی‌قبل با عقد قرار دادی پنج ساله رسما راهی باشگاه بارسلونا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25483" target="_blank">📅 00:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25482">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F16n5B2g39OC-c-FXGjM0eZFwdJrasT8zCUfA8sJu2uj-k8Y8M_Nk05EaON1s0unS6dP88v_Oh8MEIM1BkHe4lyz05VofrHruqeMLaQlMuWRaRMupjbPR6hEwhJHHDWGzP27HxdqNKMSsVgqs9791Sd4j8xxb0d4kScd_6s5XWk5kwd73wCBB37l_NL6P0V18gACYL3mJbR4lNt3pmX7AId0rJHKrrFvIwJRMItcXPJO74DWqQh0FMOhFYHTj4fo_gtTm1t9YWUfFj5P0tJ3ibPx2zglqu2o0sF4bQFobzvFHdaFCI6qpRWsghFNAjFjkNWVXb_cnwy_v3piUorojA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25482" target="_blank">📅 00:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25481">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1FDKYgF0RtMCcqAFlPp3Ut_4bPyYpY3TKfgFg4cF5sE5nKP1cdvGrKWoUVSVHpLtWjJDoJhEFSlGlFJEHhF_07k91CwSk6eaR_3dwUuGtYUJv6XgV7DXRUdoqi2w7HlImBqkIJNfyvPWDmxaQtbLOaVMpYNg9598WaCMoMkQBpLph_OZUhIjxp9wD9Cs1OuUvaWBchsRpL_8BZS81IBAHmL3cqNcXN3iUc2GNILv4KrWaDMxeHI4myMpcXDzQWhj2-A3DOuOIgmgvt6QDvBtMo6fQt-vZRJtJwguVj3opiEDTXjQ3zdSLilLjw52IxZ9mL6lqwvtm-dfk_xjD-S1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25481" target="_blank">📅 23:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25479">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iRrRCWZOo4-P4GMOCJumY-ijn4zfPvb5iqTnx1XU4_43OZ1UAuHwtYgyVqxMGF9S8c-UUahuVuAZXdyPpznbWP7zvwspbapBgKfU-emJghjot2mQkxa5k8pb6Zxcbm2i7QRpYTooAsZ4orerOc1Vl3xu7wWu0vizYs5vh88srzUzzINnusGthDW_-w9wWDns1ExFSErYioN4UJcjOXOXqeD6aGQskyIAmSfsFBbo2tUwNsXYkVAZh4A5BKEJWCAoPDXa1kWDo23ZWUK7QIeBywcHuosXeg-KAHr7gRLp1QcsXLJ6w988WNRODq02QTIcEVg4tDWGcsCn3z96csbTUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q1shiUAvTCIyu-j0qMumWH5VQdApWm8HsPdTUHsVvL04GKzoiKdRK0LQC-BA-fLCglmPKqCG1V9rmjo2nvfep9PwgfzR4LPWyFVqAGSK3yi10vGPKik_PsnrLAmsghtPYZ7BaNpgzNt7vtWW8vmjtWdHtva49zI-oGstsYDByJY4OPyFpp3SLRsYOzgm8FdKvIMXx28253r6qgcla4iDwNWYnvjAsXGiq_tRpuONrO5DbFWCqYAX-XnZmWOdGxqkF7RWoBEFax1gtmE5RHsqQcyUNK13eSw4GSae1CK_1_6BiKJziurm_NBdSEcRlwkTczEj7JYu0QOnlpKbkOJFaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25479" target="_blank">📅 23:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25478">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1iYhfWvbG0_PxP71mQE9nZ1ftPjJxsIo5oGCjbmmsXi20UErrKALDI9S_fQtXyZwu6y3kTRR3HMr69iWOcOMUEcusrONIO5ERhjcoXNvuar8FcZVlgc6CQKogeneFzlHG1T2kGtmxsyCgtd5-DupfX7UeAIXh_IyLZDflAlnKHo7m_PS8sy5FLjgXqzjXEMXAmiatQp5Lzsd45AZFYx8kqBRLjzowZrnLgUx5UP4zALlyrKVAPtE2vUVtksjtnlbfGmCNpwOHz58qp0sLFkBAEBuEAxrOEg2fBfElzXs2ID-LWXuCEGIhpe6_4IJTGZP6Pn7ooecrqNNtaCOx1_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد سرلک در حال مذاکره با باشگاه فولاد خوزستان تا درصورت توافق مالی بین طرفین به این تیم اهوازی بپیوندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25478" target="_blank">📅 23:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25477">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itn0sSKcpc6IGN-KadAPsHz3-cz8ggC5E3ks2CdcPth-1wtZMJ783vyazbmkUvXh4SW5_R3oT5a6LgUmYt4-8cYuUHnvIHFFgU_nqLvFTghihJ8ukievYPec0iF0F-3sYzcCp7Hp2MgGJd-ez0PilhNDBKmbxdiv9zEYo74qLxogJqL-ts_knPRUXaphcccTKsg9RgXHbbHJMJ61WfXE2JRD5Yjwy9bZoa1i_aCouZZt2GQhzCHATrtnDDhVDEWvTiqsbwISat0dPC4-6ZRQHVHTsC4WJhk2EvdcIs1dXZx6pppW_8RTiJLhT7lKZGgsmCtJXzy44yx4tpD-9scQvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
وحید امیری کاپیتان‌سابق‌تیم پرسپولیس به‌مدیریت.این‌باشگاه اعلام کرده‌که درصورت تاییدیه کادر فنی سرخ پوشان علاقمند است که یک فصل در پرسپولیس بازی کند و در پایان فصل از دنیای فوتبال خداحافظی کند و به کادر فنی سرخ ها اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25477" target="_blank">📅 22:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25476">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NB3qKwe89i9A7rNENTGPfnkKSWVVUgJ11Wol_MRzuabvKvfywkbtLrFlLuNNQByOaZIPrsh5L1tomcNbrT06K_BcYSwpdA1jFdXKvcyqRD8DCDe-w3qUenBbvxxTmEWIklkmf3D6bvXOUV3LQVf-D2TdLjfOljDsTJjkDDyyfKiPFS4TY6gZugMIZqN5lb7UgBN14L3NpefFBT0WVXNRLw-3P9Nf9wWdaTebQmPp1meg_YsQAtVSZ15-L-rsbJTf-6lBBimUu1skIZBA5hNR95EqMzkWQweFzd10P_JbyAS2-h-leUpM0MfyC0Zq6y9gDT9uNMsK5LPqA5kmocDyQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ روبرتو مانچینی برای‌عقدقرارداد چهار ساله با تیم ملی ایتالیا با فدراسیون فوتبال این کشور به‌توافق نهایی رسید و انتظار میره به زودی پوستر رونمایی از او نیز منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25476" target="_blank">📅 22:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25475">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d020345f8.mp4?token=UD7Svr4DTUL2xcOxFzUAjj3H02Jy_zhI8vu1KVbGm4m50KEduhW7QloRcSTD32b808dmVQvmZGWdSAJDaErOdg9Uv5NfzcNz9-g1rPLELH-aBHd0UGkf6DoRp5og1dL1dYzWh6O1nNKxWR5u1j6gF02lIRAqpxCyVcX-fSbTonbFXIGlUGolZ1jdkFlwJDewsdAbdtC6sHI7JtUQ0A8OPTuB2F7WD7MdpwfjABh8jGgeu1EI1sqXi2uh19IiySb6-czq3fv9Yq5aak9dfQb8TW0FUJNSjimGt1bI5hDJ15YFFyW12_73MSiQoPK_HvLE6T52eCAlZ31Q7kf_4yEpkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d020345f8.mp4?token=UD7Svr4DTUL2xcOxFzUAjj3H02Jy_zhI8vu1KVbGm4m50KEduhW7QloRcSTD32b808dmVQvmZGWdSAJDaErOdg9Uv5NfzcNz9-g1rPLELH-aBHd0UGkf6DoRp5og1dL1dYzWh6O1nNKxWR5u1j6gF02lIRAqpxCyVcX-fSbTonbFXIGlUGolZ1jdkFlwJDewsdAbdtC6sHI7JtUQ0A8OPTuB2F7WD7MdpwfjABh8jGgeu1EI1sqXi2uh19IiySb6-czq3fv9Yq5aak9dfQb8TW0FUJNSjimGt1bI5hDJ15YFFyW12_73MSiQoPK_HvLE6T52eCAlZ31Q7kf_4yEpkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
روزی‌فهمیدم مسی هیچوقت‌تسلیم نمیشه که بعد دعوت به این برنامه‌ازمجریای حشریش جون سالم به در برد. لعنتی‌ها ببینید چه گیری بهش داده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25475" target="_blank">📅 22:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25474">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvv0mvaUA5smfWaW7f3VfM6ZACQ65BYdcw-S20URGdpV1a4pa_UXmGXjPUQWM2LWQvlRAqlxeyBbcn_gLUPJoC3x4YZqJw6G64RmsSduCPcTCgnE_juX0Da284E0MGQu4DNpEAuhngadCyYYzSXS-5mruFcPhEYY9OKkYvamcry2fJnOX0gUVL9-mdDZqHhnJ5YIjGxAOEGBIXu4X-l_3x78Mr9Cac5MqPhGIv2J_2RSAFaIIXQ9UjBLjgIF1sKVJ7HnuXD35W_QWw0ktrec6SVgRGGYAxC5tlQVew19gGuHgCnJirX2wC_dI2gr1xLolJq1etVd4_6EypTdzJiLtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی پرشیانا توسط پیمان حدادی مدیر عامل سرخ‌ها درباره وضعیت علیپور و محمدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25474" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25473">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=JsgiyrljWNL_xzFOk8GEZJKBiKlS-FC_O0y8czvQhCv9SmGFyNiiO571CRuujUryRrUxCMhWFiZ3sRVwnuzn8RYYkGtD3UiTzOpoIZmBkxMdd0d_ogYrkMtaqahU7DSudOKAPbpWI-Lw_2ommLQ_PGQvyyMHZjE6swL3GHB6hsxDu7RdYrvZlva906IQ37aIkO8T3k-xtiE9Bo3KY1chijJQyLDuwv94a-3oUMMAQSG5pW27hDMoeK_KDINe5zb4VqpZRg8IzLVTS4PCbNaG6-gIPB5i5bMlvQxbM7zVRW90fotgADiP9tJKJFa62_vxK8wMHXYN5vbjMTRpoo2glw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=JsgiyrljWNL_xzFOk8GEZJKBiKlS-FC_O0y8czvQhCv9SmGFyNiiO571CRuujUryRrUxCMhWFiZ3sRVwnuzn8RYYkGtD3UiTzOpoIZmBkxMdd0d_ogYrkMtaqahU7DSudOKAPbpWI-Lw_2ommLQ_PGQvyyMHZjE6swL3GHB6hsxDu7RdYrvZlva906IQ37aIkO8T3k-xtiE9Bo3KY1chijJQyLDuwv94a-3oUMMAQSG5pW27hDMoeK_KDINe5zb4VqpZRg8IzLVTS4PCbNaG6-gIPB5i5bMlvQxbM7zVRW90fotgADiP9tJKJFa62_vxK8wMHXYN5vbjMTRpoo2glw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
صحبت‌های‌ندیم‌امیری‌بازیکن‌افغانستانی تیم ملی آلمان در رقابت های جام جهانی 2026؛ این بازیکن از دو تیم آرسنال و چلسی آفر دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25473" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25472">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4EaciFv2Rws-Yd7X0bGpf6G9bvVp4Dra9dAyq9EPJtGagIWfAQl7ovRbVFHEGl5TpBpy2PCB86-82UofMqxXjHYaopP8Sa2G5fzQslOh8MqSu3ovcY_VVm12RGaW9cKqUHKEU8pU2jRnyLAaK9yeoUsPyWhwZYC9b3Gv_h_ADmbEWYJC9VIl6E-VAe-nOuXcsRXFvgbwrIP6LsJKCHzmaP2FEB8S0WQhJ-Giuaa3aWpHyyPHcvmMF11la5HbtJwemsvgfVwX_MlfDkvyzxf7jMrHqe3UyMupT7tlRK6X5KFN-tpBTmq47lEndmccg3w0ZKgCMB9yvwQaeh0QcRQKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
قدرت پیش‌بینی‌ات رو ثابت کن!
⚽
🔥
دو مسابقه جذاب:
🇦🇷
آرژانتین
🆚
سوئیس
🇨🇭
🇳🇴
نروژ
🆚
انگلستان
🏴
🎁
500 دلار فری‌بت
بین تمام کاربرانی که نتایج را به‌درستی پیش‌بینی کنند،
مطابق قوانین سایت
تقسیم می‌شود.
🤖
پیش‌بینی خودت رو از طریق ربات تلگرام ثبت کن:
👉
https://t.me/betegram_bot?start=p6_r4EF37DCE
⏳
فقط تا قبل از شروع مسابقات فرصت داری!
موفق باشی!
🍀
⚽</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/25472" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25471">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEfiUbYL5ukEtAtulk4hECveLgwm3k-NlfE0DLwz4Gi-mTphuwgsIOl_KEVDAevXeJcIXn8nQ6lzQoFKjNCuZuBBDMpPOqsAE2CsTqGqe8WBQRbNuXXtySohBOnER30HiZnT25ydFpdiOwFvYbkinDmdrsmBdpAnNIo_lF19l1IsjotjowyQ79yr7lIPol_5lLdpvFBm0rxQcNYro6t8Y0A21eUOFXUYYhXhJpxNVS5yaDGCn9VFRo8H_K-rLxD5gL5NAUVUOOOWFVm9IsvJ6fVn55cy2nWPE3YP4Zrjt-fFVRlkY_WF2I_ByVl9iS370pW3SSKb3fhFhCQX1joPcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ اگه جدول رده بندی رقابت های لیگ آزادگان همینجوری‌پیش بره؛ نساجی و مس شهر بابک مستقیم راهی لیگ‌برتر خواهند شد و تیم صنعت نفت در یک دیدار پلی‌آف به مصاف مس رفسنجانه میره و برنده اون مسابقه نیز به لیگ برتر راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25471" target="_blank">📅 22:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25470">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMTylZbR8CzPPuPk-l7pVnn0M_bagBRBcg6CQmJRbeZUoOd-nbQgjZwjScnIt82w5yV5t0q07hdhUqIw4xQhF0krW20BtYjahMuYDIAnkyVb_lEUGGAF231wMJM-ldjwpGLy9gK1cpa_X1NPTXb1tpBgKZA5SNhSPJNxzdgLLwfudKU21iXLZDYiQlTSLeUnBwIOUzI_FKLpwZGPgNB3DWw5dC63T5zDeouRpIWBFlh9TLK1Oqpd17qckCLF7CI1d88pwF1k4pdtpZwQiakKyq0UPZAaQ2B4MR9ZoE4KwTz5aJsWSFDvwS5HWUhM-LL0hb_KGfzH4j5ps5T39NK4RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جالبه بدونید بازی‌هایی که تو این جام به ضربات پنالتی کشیده شدن در نهایت تیمی که پنالتی دوم رو زده برده که این‌فکت هم درنوع خودش جالبه واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25470" target="_blank">📅 21:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25468">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=HNUnQa_5IlU6Ufn2g-3J3h2nOcerUQhxnaB9khLi9qvgV4UEM6-ezwaP1Y_vG8dispFCMB16PgVQNQNiYDouExY3FJdHO8HwAImhDt4XUWlbsnSoksR6I7_UqLT3oJkjMTO_sTx8Oh50AXpC6p87h1ZKvSKJKawW8JKaZzK0anc-1eS-4oJhs-XaPPcSaesKrnHOS-_t9m37E6QcdR8j_mifFCM7ZGcDJcTTs_m5KT7uCN4YWGOTZKcfJ1qGdqBw2JSGdCGrDmfRm6K-xM15yOVOD3KF6mzXJ1oNsOROuisPnH_PTTu9aX0QAXIvM4OXw1rjhzzBOdOa6juy4SWDUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=HNUnQa_5IlU6Ufn2g-3J3h2nOcerUQhxnaB9khLi9qvgV4UEM6-ezwaP1Y_vG8dispFCMB16PgVQNQNiYDouExY3FJdHO8HwAImhDt4XUWlbsnSoksR6I7_UqLT3oJkjMTO_sTx8Oh50AXpC6p87h1ZKvSKJKawW8JKaZzK0anc-1eS-4oJhs-XaPPcSaesKrnHOS-_t9m37E6QcdR8j_mifFCM7ZGcDJcTTs_m5KT7uCN4YWGOTZKcfJ1qGdqBw2JSGdCGrDmfRm6K-xM15yOVOD3KF6mzXJ1oNsOROuisPnH_PTTu9aX0QAXIvM4OXw1rjhzzBOdOa6juy4SWDUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه‌پرسپولیس که دوهفته پیش با ایجنت علی علیپور به توافق شفاهی رسیده بود حالا 72 ساعت به‌این‌مهاجم 30 ساله فرصت‌داده که برای تمدید قراردادش به ساختمان‌باشگاه برود در غیر این صورت قید او رو خواهند زد. درباره میلاد محمدی او تمام توافقات لازم رو…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25468" target="_blank">📅 21:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25467">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uK2U8c75hpeOXkf85rGwiA7UmypU2bmoInjXBPf8epOjpjuwbhtKiUxbAV3-quoSzCDk02MgnN_2bn7so7Iw1jUQ3aOb0zV6tRRI5nabBDk0J0aHxWtqUCAkNwx6ete3qD6aJmkDaSj4NdOQmfiOM-114sJG3s1zw9OfTtcU0LdI-eDfBPxfZP79T6Qi_SDa1F8sQAhvQaHxn5wK2KjwW-edJ7W3xZNCScaQv29E7ED9N80IWTdqNHEtWGMt7qYGPD71U0EZAHi87L7X0k0nUO4O7kNkJ58NqGoVnaocJZdsMXvmuGYkP1-45fTRBm_ZJVRIzPEE6vsZWDYtpGXn2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25467" target="_blank">📅 21:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25466">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSzibdHUJ6IYPI3VcOP4lGn9mt9yjxmxIZyzabqKA8cfxYzGW1jvtsn2TyeBTpqiksslJPFiTSUEeH6GfcyJklIS_YSFaEWxC_7Qw2V9b2qypkuVCr-Qy2x57rTx2DbheyfJebKsYW9SiGvQ0fyO08GiCaMAlCXzTRzXbSowIUXpembhdaZnqkuU1-rb1lxLUjg3RECRB-tb7wokdw8upSlsiDJoRrJFkPVJUhPVVZoQoL7NXsWyQUm9plfmDfsphmf6J3WpRszo9QP5IScdogE3umPGzRrWY1P9qMSZ14zt-GlK4O3RqrggMwYUM9eaiQIneWUxO5GJNw521tbTzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
طبق پیگیری‌های پرشیانا از ایجنت منیر الحدادی؛ خبری‌که رسانه‌های‌آفریقایی مبنی بر توافق اوبا یک‌تیم‌مراکشی منتشر کردند کذب محض است. این بازیکن اواسط هفته آینده به تهران برمیگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25466" target="_blank">📅 21:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25465">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMU_qSzSgYLEuKNZveJjrDC5OjXKglAUI4LX5YiTjKBZUFPm99gHqtrNjnvTowPOrSSscuLLg0vyY9ZHQQjNLN3OVztBhf6vioWyp4E4v186XaQfEsTcxmb3sDMjmE3V83YhfJqaxgWcstJT2ov2z4feCOFhvu_NyeD0J8Vf_OfrpXG0ksLZh62_tD0TQTQ_mDMfHXz6XoChoBWitHTb_Fk21c0j_Lc3oI3zVXb8Hg0Rw-kuOjq71xFdzmQId06tHw2hGjzFPca4XeNoalcTqkcdddqRG0LahH2J3NZXcqrJLuiaBfqM7hY4hFX0liEyGgfapgwfj-xMRFfSCS94pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل سرمربی تیم ملی انگلیس روش جالبی‌برای‌انگیزه‌دادن‌به‌بازیکنان تیمش در جام جهانی کشف‌کرده که چون یخورده 18+ عه تو کانال دوم‌راجبش‌گفتیم. حالا فهمیدم بلینگهام چرا یهو اوج گرفت. بعدجالبه بدونید 10 گل از 11 گل انگلیس در بازیای اخیر توسط هری…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/25465" target="_blank">📅 20:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25464">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMEy_sTjrx1QHS0aXve_tlY_cQglcFzRs2ZgAyEBcWV6UOSZDlkSUh36dGF4dKI4fUJ3G52xtjUvieYay-SjbZEK2Q7ZdWPWfDLCqiJHv35Ts4uaBbjKw1IQwbYFgRfUmyGaFn12iGaJA4rqguv06GX8fOpRX_cfNVETFkQWb4SunHlCdwPWHH9FPxfl-jxzn3ePyfpLMSACaHG_lF3nIY8qJ7QV5c42SKEPEGYeSM98e81j9m_ck5IjpPoB0u_EtJOSQq7JgCXPr2Vwp0XvteKxovv4cm7wuSbeSNJPKrBOX1POsOd2SgXLCsabO-wVVVRspgiBBxBdjKEpYn0D5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعداز موافقت مهدی‌تارتار سرمربی جدبد تیم پرسپولیس؛کریم‌باقری بزودی‌به کادرفنی سرخپوشان اضافه خواهد شد و قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25464" target="_blank">📅 20:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25463">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rO0uIL-okdHhHQ23BaVuRINY5YwQ8tAnGo_wNtoJPLgjlgGfP2psaUZpEAPkiyv8wxviIAFAe_I0f_xSd-tE7Do4IFec1Gt5zgDVdOs5GUpJ5eXAiRFIUycHVLamQRaLwwVnk8R0idJ-fRsMeA9hIjA7pf9SOIQ7VS8pO9Wslate8v0fBWz9X1x3ErWVH1POfuN1cFFF8Ryx658sHq50ewoYd44x973XMpf89wV8VAMm6xL6j7vtM-CFcxwPoWO8l79L6qMOzfmjdnj2P8y8t3T5itNiXaFnhyXSpXWMYDSM1vE02r00cJjg-pROz4rQOslPRtlZyD6IpFN19vLIWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌اخباردریافتی‌رسانه پرشیانا؛ امیر هوشنگ سعادتی ایجنت معروف فوتبال ایران با مالک باشگاه تراکتور آشتی کرد و در اولین اقدام قصد داره هادی حبیبی نژاد که روز گذشته در باشگاه سپاهان جلسه داشت و توافق نیز حاصل شد رو به تبریز ببره. اگه این اتفاق رسما بیفته یکی…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25463" target="_blank">📅 20:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25462">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcMJMbm0ZftbYZRSjdsV5J2v4EBL-INAinORAJU7dGT1-jCUh7ciqoD7n96J91OpXvJqFgxXkeEt__fMO5BCZ9pB1wJN6iSWJr3kgkIDTLmxzsW5bAP7e_dldIk6EVxLutmgx9p3yEE5l9ZXXIS3oc0iE4S0tSUTjycV8H1WEPoJHfGK7wXMl59CbPz5b9pEQCS7gQKBFWsd0vbNAk4e6pAey8eX8Xi6qHe6mNVK5C4rWuUkDVZf-UbGqlhnwr4cUWVZNGp4EzOTtjvuIGzeoapsVH5ckZdBEoxUL-xGLLZvL26o8ROg-astQzZsjPHUmJp-LIjMOZYHZmRWb0A7HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25462" target="_blank">📅 20:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25460">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6bi565XKEemN3yf17mH1Mpyx7UgetNvE56onr8RsA0oJeGgqLpWhWJ2xgAcCeHHdBLn3inT8n9agu_u0Jn-pF1B6Vss70EY5N8ttra01yLqpn6vJ1DHpb_w5PHdDgmJ1DaxjLMhl849ajRbOYPQIUqS8BOwwtwbeHcjZ6pvQXXUUWpqB9MsB3W6O9j1m7lgFLvCczoVHTU7L6Vx9ECb1jfDtz_tzVfcdkre8Aduo3YNlKIa_6LzWHcUUwIdmkwgf7QuwTgRCQALWIJsn916xY-7fvH5A44_IrMs3cWZgrFwLDp1-3_6JUfPGpNtjq-F-17n8S_2C6AbcI3iOFTlnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
محمد عمری وینگر 26 ساله پرسپولیس دو پیشنهاد از امارات و قطر دریافت کرده و به احتمال فراوان فصل آینده لژیونر خواهد شد. از این انتقال 600 هزار دلار به باشگاه پرسپولیس خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25460" target="_blank">📅 19:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25459">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDNq3ovhRqqKe7aKHrYmmlCLjJm8YYfzCKdMXomdf6WpJ3NabK9GU1ovFCIgcuIftsinaeUm0x7C5tefv2WR_bKIj6t23qRutznwHRUfy89us5j8-K_XeVK1aztaBJrQQIaXjDRG7bDKZC_DhPXUMbvbPa3T-nuHSY9-VMaxwD_oH31rJOpEFJV1xFAw67cDSZtMoeyCdNl_OZjsQjYf1bfdR_l31ybTj_R7JFjqWyGK9PvfTxqmfZHp_CsDCcg5bHpOfGXoEGXrh-mNxZ6AqwmxmUhn_q3uxjb3_lEs-e1ymeL6U_rSZ3KmVTBt0bL_A3CljeS5RaIeFVQPqpKfMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تقویم
؛ 12سال‌پیش‌درچنین‌روزی؛
بارسلونا با پرداخت تنها75میلیون‌یورو لوییز سوارز فوق ستاره خط حمله لیورپول رو بخدمت گرفت. آمار سوارز در بارسا: 283 بازی، 195 گل‌زده،113پاس‌گل، 13 جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25459" target="_blank">📅 19:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25457">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=DBe5DFltFJ66xp554SkWK2F0616vX6vEzxnJbTj3WiCt2rV_NpQBX3fUxiginfkLgUqAFEMaT0znpHIvCyfTZ1MaQPoWaZcQ3XU2dxuopx4IkIC7AHrwAFBBIuhqBqF9uUUenGQ1JMK1kOIlE2Wwfz70gkjnFr9hhVOYmLum8LPBHbr6gmDgrH7JHZKovUZLagphh5BDvmS5oGB6yappwmm3bWO9SYbrPT_rdq8OEpCPAlXcfS02DtJb2AXIpOx9bSM4rdY0lsP-kr4IeHoRrwvCR7jENcZcS1P8BVgawXloMf6YT-Q-4r0VHZxFXIqQooaU2uAsw89cWEKVettCRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=DBe5DFltFJ66xp554SkWK2F0616vX6vEzxnJbTj3WiCt2rV_NpQBX3fUxiginfkLgUqAFEMaT0znpHIvCyfTZ1MaQPoWaZcQ3XU2dxuopx4IkIC7AHrwAFBBIuhqBqF9uUUenGQ1JMK1kOIlE2Wwfz70gkjnFr9hhVOYmLum8LPBHbr6gmDgrH7JHZKovUZLagphh5BDvmS5oGB6yappwmm3bWO9SYbrPT_rdq8OEpCPAlXcfS02DtJb2AXIpOx9bSM4rdY0lsP-kr4IeHoRrwvCR7jENcZcS1P8BVgawXloMf6YT-Q-4r0VHZxFXIqQooaU2uAsw89cWEKVettCRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لقب جالب لوکاکو از زبان فیروز کریمی؛
جالبه بدونید که برای ایشان به‌خاطر شرکت تو برنامه جام جهانی شبکه جم‌ تی‌وی پرونده قضایی تشکیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25457" target="_blank">📅 19:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25456">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwjRSpPAZ6U5gyvtrZEXExWzPnyoEVUCGshVjCHaA0Blswy0Kpmeai8f97I6usd7D6_lC1zu5M9e12zDpBC2DZEw5HIdQOCjyAx7MbFWOQTPXJNllqjo2-4-6sDfvS8UaxcAhAHAGcvhy493aP5-LtWPI4hkR3hwXt7KINOT3biW2ZKvWd_Qjjj11haCDeLnC5u_fpmoLje59DLcJz_S-6UkoDBVdOI808hjM7fBBKW8x5_JPXRIzTYXlz3DU4FMWaLIofcQHrm5u2vIT_-0fxube9BFTcSLQsZqBZG4ipiUxsQopl2A8ZvjRBO89Gk6zsDBvom2fMtGTbcPG9Ayhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام AFC مراسم قرعه‌کشی لیگ نخبگان و سطح 2 آسیا سه‌شنبه27مرداد درکوالالامپور برگزار میشه: استقلال و تراکتور درلیگ‌نخبگان و چادرملو درسطح دو آسیا به عنوان نماینده های ایران حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25456" target="_blank">📅 19:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25455">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2gh11cjrzYjCTa-X-XJBpyzGK44oeWatocG3I5ke7mhjQC8qSgHJq-RrwOd5IsZWDcmCcWTKWwXZRNEZGcQHHMEk9c_JkBm5l3YWhMb3v8dQlbEPrzxN2p3jg5wmpDHJ-PlWMYxZHvd-_uJNilP27PZzkcdJJLsvIctbbJaFxIxO0qni6buhhH43PfjOfHPcRzJsvNGUzEJWC7p7wEuIIcj4RQbp0Ff6ePsptIK0_PhC0mAa2iukK8oucwJVk8QIYVMDnH9PC3iaolrXl-um_TxM4012Npv4-jriiaf-brXv_MuMB_JgHwdpywS2y2xq9VxUoBBpzYR2Yxmh26pZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
کریم بنزما اسطوره رئال مادرید: به کیلیان امباپه گفتم الان‌بهترین‌زمان‌ممکن برای انتقام گرفتن ازاسپانیاست. به‌هیچ‌عنوان نباید این فرصت طلایی رو از دست داد. اسپانیا برتر  از فرانسه نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25455" target="_blank">📅 18:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25454">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‼️
خاطره فیروز کریمی از حموم عمومی در برنامه دیشب ویژه برنامه جام جهانی شبکه جم اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/25454" target="_blank">📅 18:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25453">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMhMLYuMuH0dBxr9MGCNFINe9VntcdqLHZAy_UHgIkXzcW_L5XjjH5KK2lYWjH3qB4gbO1Eubhc7eedHkQS_A3oKvOuaQSiY1rSOaUsHFQKFAGBMpziH6DucTxds87JwXRiP163wy40k7tmc_KQ_oj2nmNnRzj_miTx2tJjevIJPy2TVgeLXKMON2DO7GlOjxXU9vrOy5rxFD3l-zuZ4Mavg0qUA0H6N3XO2764SB1nearqtqSyQF-7FE2el1YIykOhKMgogUwrCZN-yuACjwOorTyfOgGjSuw0wLNoeq5JMYviP_weErCMCjj1DelcsOSo_ta1AOjiWWbQ151d3QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/25453" target="_blank">📅 17:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25452">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCJTk5HSWPSbrstvX3qv5PSnjfR8TFaIrEPrTDlj6MQaKpE9Qy8CxevMaUM4eELTEYF2-0tf1cMmT7IAr8w5MNwKRNZ_e3j4phveiRUYdwLOWhp1lXhSstT9FDOlgSsiI0_2Fh_mSv7VmlzaC1_LvrMQb04PCzWZXoVUDdy7jtef-h6DvRFBcNHcaGF5E1MkAhR-PmUeKcPw7JHPpWpqQiri4oP6wuVX7k9HnlIDP7je01F-ER-jnQzLDUrmDcav78sqx5Knbv5NG5fLKcZBvBzAcx03OY6WrfE8PcYAQT94qzeJ-dvfmjallLN2weTU4jbrQUj3ATQ4nBY0jhl9Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/25452" target="_blank">📅 17:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25451">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRw0AkqvHlRHTPnrZ_kL4lYcWhsHKD2_hPznmz41RR0pj-Vptub9trhb8zU59V402Qm_crqRq4jPL_JO1WelW4UaPEB664m7pymQO06T3Wp2wP5tYeKxoKnRbh4QInO0gXY6rin6gFZnB-Ze6M7bFTLpzGTHFCHxNlHj_18dMgrxCPZHxC4pk3RxN02C-asz5bqUtun5nt3w-nkg5QUiqdyP1VtR0qPFO5B6LEDG8-OQjysAA0-OVW5ziOTrzX8inD6_13x2XpeTt-gvW6ujheykBe8teQrZjFin4v_pS77n_aXlWDawZY_5nmOJ0xaOKDwxgzgmcfP0P9mBM853Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
علیرضا بیرانوند دروازه‌بان ملی پوش تراکتور: اگر در تیم پرسپولیس میماندم شک نداشتم یه روزی مدیریت با من هم مثل وحید امیری رفتار می‌کردند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/25451" target="_blank">📅 17:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25450">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miOcyvL9znPNP-OewoHtCi-Z8SLbOMwCjLFxHbZ4_CRxQRCIYjSRDsBz83Vmyru6a0fSN79x6nf_b_-xQfBGOXH20ksXkquiGh4JrNGO3dD9pjBOTt16mE5CTYLZFB8YKeDFl9FObytJfgGP5FnOSx_lyAuczjYwHypZl5j0SogyZvVapvSzB7VuxoyNpfM4mWXoYu0-ud8zwc8Vs8XCR1KfeMqGjZTIZ5mSn0l4k2cI0HcRnFvDe3oBp3j7lv342ys0LXrfaBNCS2BFI0occewM0cXM6_nRnIuw1-Bbyxt7Nsmpq3U3IAVPznPiJI9O0qev2hUd-kNELdvpBnIZQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/25450" target="_blank">📅 17:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25449">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQPQU3a30YJKisIR_P09hlkU901WwZT1a6s6YaQ13jR2w1mxxfD_L87GzCweXWQKR9TKCUG38r0WP7KXYlN7b1WmZ4ErY03J7bzOi1FAnhYSosMz3aByBzTGCCQNO0IBZFIS4ggEQV84TI2JQLcq-8-Tr620O7KQWOP7rAkw-hhkMnyMVMYbcj8Az3Ukle7YubdkA90yxDC3274ID2M5ol3SYIEjJ7WXA-oard6oAwrQBhKKv64vXhVEBbimuY9DvfUuLZd3-nsCHEUnyXp3s4OmelA6rhEnKRliMSYGPkzVf_Ki2z2WB8k3rIdkEJq6Ofb_vhPa7K4DZ-VxGhGSrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
خبر شوکه‌کننده دنیای فوتبال
؛ جیدن آدامز بازیکن ۲۵ ساله تیم‌ملی‌آفریقای‌جنوبی که همین چند هفته پیش در رقابت‌ های جام جهانی ۲۰۲۶ هم به میدان رفت، به علت افسردگی خودکشی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/persiana_Soccer/25449" target="_blank">📅 16:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25448">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4ewdCbK5H-ICIAdRyUMVyE_S62rwaYQdD5qmaUVKCJjGMPDpuNaUSgtdwXpRv9WJ73B5BKs6L3mBT2eL2bALLHB1mEfDPSXCmMPu2Gv49y7SN4SbH_z1x1MwrQlgs94B-yuVkFtp7UeOagledMjGA2Y2cat9RsbzyMW4BvMxZtUuREB4arD6bc48gkJeYE7NPhoDYiGh0w6adCyUUleipNnw8upVi7R8uY1mp9ISgAA3nxSbQDdtrnTdR6w6ED9Sj-yFheELZBQNQqHIwuXCbkFdGK7pvt1i-slsTftDF5F8wqp_m4fPcn6STK89-IxA801egrvlLfabSztmO6kKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
#اختصاصی‌پرشیانا
#فوری
؛ باشگاه گل‌ گهر بدرخواست سیدمهدی‌رحمتی خواستار جذب ضرغام سعداوی مدافع‌میانی 20 ساله تیم استقلال شد که با مخالفت کادرفنی آبی پوشان این انتقال انجام نشد؛ بختیاری‌زاده به سعداوی گفته به.سبک بازیش اعتقاد داره و در فصل جدید بیشتر بهش بازی خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/25448" target="_blank">📅 16:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25447">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCaYT7G0RomJeyktf4VBbKpws2WSF3ZnlhXw8Al4i3a2GcKsjMr1mPwB1HeyQirxtt-H1qdTwRySe0dT45sj4gpye1Q_o_KDUDAlPtPaUWYyQAIDqECDmNG3Ox1s5TFTJlWkl99iZVelMU5-aG35xMoqpqcTWfuITuNKIJIqHeaWCt1hKaxTfxp2cg2tnMFiEAr3ZF6a62teCAkfRPre03Y42ZQs-r3H2gA03IYrhGKHJ9IfJogmbTOsbycZlVqMXjJoKAiT0xrkLZPqGnQd75vY8l6hPp_SugLhpJTyz4O-Z8e90vTMxXgY0UdA5AcLYbfLU--w0EiKo0Ms51V7sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/25447" target="_blank">📅 16:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25446">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khYfd4rmeMNDkNimqhmgiLyE0qeCWZ-NlLe6oeBRJgE1IGjPGeqDlgprPP2kX7B8_l3Oa9WPvP8NbLIM0ZZjwQZkZDYx9nE6MEUZZLkKO9Z_d15ZMLIKwDGoSOZmN506GppXoF9fw7x4soXTK6z7F0_oKH-DqsctkgIcqAsi259_TPDNgrYJ_Q4fhC55Jssv3UiJTHsd2qyaNhHYbGFm0iV6uxYwhkVTpqg28aNeXDioNl_FQO2UYD520LcRXBxHTd8UiolT718PP43PjNZ4Gkw8l0leyhmEEaRK13Yw2DGlVZMy69oQ_AkoDGbjWh14Cms2G9WK4T1d1Mvb8R97Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛ باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/persiana_Soccer/25446" target="_blank">📅 16:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25445">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOQBvLUGJClRC5zDdYMBuQa2Gp5v_MqIWAJrWocsx2v7-KvQ35riTEMEAMgmr7wbpS0MgGsRpCpImf9Xjf8_iKJGNZ-QF9ZXZyl5g2qTcPSezUtXLKMMCpzMvvpJRDiF10WWWGBm22DG5pZlDNU9GzCgpo4ueqPe7M2QnwT5NfdfjBmYMABSWmX-8t5aMb-z8rDVJrnSfrJqLDTL84Zv0r1SA3SSlbWsekJxCdZd1AWomi3FZABtTL4HvA7wf94bdl5-ZJi7bpmOXpQRktwTUI6v-LxBIZl1ORoJziVHF5frlmeyTrRutCDMM1rknlJUddsqyrjaVh24cFAH4IB8tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/persiana_Soccer/25445" target="_blank">📅 16:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25444">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihGPNAsoaUSyRgjwfqRot-n-yXUAon0tATtAv1CwVZe19vegOKdPy0yLub18z5u2cKj82YYh2EDhmxFhyYXQ1KCeq911kM-fN4Z9fvQsCWkgkZmGO6TEcS_oLyuNxltw8YqZKurUV-qEwuuaE6A6GhGo89ear88ocDyupbBnhR3syGQ5QkuehEw9aJAlo7IBGR24y06UGDh8Zi_xxvE2s7scugbgYVC0H2iW9bsKmLHf9E1fTAeHtc4aZCa17YRsex5mIdr9pkduOOyLiWmmSlccYP9bV0_hWdsI7MeJOiBOz-Wcjr_jvvcNvol-geTe47RXyY_bdZRH0xczD391wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/persiana_Soccer/25444" target="_blank">📅 16:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25443">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJufTjm9Gbh3iPbEW8GbRhnMpc0eDl5qyWun3S7XO7hOHtVHIoy5Z4HNXpEnnmYYu904syO2ysk7jkMexOI-rEl_r7xTzxBgS8lTcp9-n32_aW6X7D-WHWqrNTV9K4O4RaFNqk4d6b7NIEsCUGpU9pRFsYblqgI2a3tbjpgVp7bTFaJPnOwRlA_sr0nqthlt6U6QXUnclaH6d7RwHs4cYP82xDpSChkUREyGMUW-NI-1PzIkDxw1UMFwcVfkWC5jgNvYSTxdhGfjK852JIJMGkJWDPMU0udo7Z32rfaKm1Ig2f9tWrVQ_7az-sXTkNwgBOtG-mBSjrvvAqq6Kx86oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/persiana_Soccer/25443" target="_blank">📅 16:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25442">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAkdfaboFBDUhQ3TikjS8aZoCBD9jfxjyZujBRVg6fmi4ooEqKfd88KKoAGELCrgh6dd5IMO90ZR25DoGSMrzKW_yj3tB9IlHh_4P2GRl9mUksrWx-DDEev_MAoqFPvQfhWebWaYXaU-imyAKdvFuj_ivUZmuGJL7KsYKFcHoeUGQ4TWSr3EIJKRzSYfP3h9bXW5M4SyVviWfmQv4or_cbsVqj4gM2fFZIavdAV2z67mI03W3rko-ZPf7eDTznxlf6Ly-LCnGqYBvXO_CqMFpN-d5w_NCbIrVH6qepBy4KzFHBfPYNRtWKjIr_tzONh_nJpBqeiIwZpP-lmNvZH8oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛
رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/persiana_Soccer/25442" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25441">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8ad7a6bb4.mp4?token=OgRTOj_ErWVomvU_a2MRPRWM5zWOi-fsLTiHLvYHyjOiO73JP0oE31gQsSmu39rCr6Iu_hcbtoXT6IsM-qt-g-3RrcABwk5syue0o5_owperTSheCYCmlDNLu3FQ0XjpkRCGbo6YcchHKVSd4OIPdvwfrMmxquLpjd3Qp9NqhSgzLusKBruMAtp1ngOmCpmsXLB9206GfEkyW-SXzhS6AkVqbfh_JgpIY0USnndjB7uRjH-mWPilvdS2cJhwyN6grnn4vpNtrNJ-kq6n15MDvmIYolofqcKqB4jAUWsQyO6laQJfyAjl3G0O-hfp1bspmj3gH9udkOF3FF6RrTSrwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8ad7a6bb4.mp4?token=OgRTOj_ErWVomvU_a2MRPRWM5zWOi-fsLTiHLvYHyjOiO73JP0oE31gQsSmu39rCr6Iu_hcbtoXT6IsM-qt-g-3RrcABwk5syue0o5_owperTSheCYCmlDNLu3FQ0XjpkRCGbo6YcchHKVSd4OIPdvwfrMmxquLpjd3Qp9NqhSgzLusKBruMAtp1ngOmCpmsXLB9206GfEkyW-SXzhS6AkVqbfh_JgpIY0USnndjB7uRjH-mWPilvdS2cJhwyN6grnn4vpNtrNJ-kq6n15MDvmIYolofqcKqB4jAUWsQyO6laQJfyAjl3G0O-hfp1bspmj3gH9udkOF3FF6RrTSrwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
خواسته‌تموم‌پسرای‌فوتبالی؛ روزی‌بخوان ازدواج کنند و بچه‌داربشن، بچشون‌حتماباید اینجوری باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/25441" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25440">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآپارات اسپرت | AparatSport</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJfgHBtM2CULwK1UFLHGIettKCPUQrzM7wRJHaXSJMxukqGzYvdl_BwEdxl4LpWdcpAUvUfA0hcvRORw-y7mP12hIvgHNsISkZ0blUR1Qu9Wmb7gBK2R5Wj4Jn8GmlDxz9kxTjB8zw-elan00UVPKSqwLQtQ7Z83Osv1syQ_ZAqbazjqgBdy_R1tYknuKlorkySHE7cMZNVjZuGI6RoQoQ5qCzCIpJFIFjFHea5mI9jQxp_X-3JlGNW9aVXWOZVTtgzmbhpQ2_T3EoF0DVjb5mFjx0xNmh7Vi3qj19dHND6bMt-q0RUJcsQl0ffxwBtnl_uFWcmoAWVoxbKJSKbucA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پخش زنده و اختصاصی بازی نروژ و انگلیس با گزارش محمدرضا احمدی در آپارات اسپرت
📅
یکشنبه
👈
ساعت ۰۰:۳۰
🔗
لینک تماشای مسابقه
(بدون فیلترشکن وارد شو)
@aparatsport</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/25440" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25439">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1NKDrmIPnzS5mRshAJmp7kY3hnhp8E1DzMbgE9hKBU1Bc-qL86NVJKqnaO8ymlHsSo2t-b1VRB70XHPcKAILO-_74BW-OEJy0PhdUO7Hwyga_Ewslj8eHfnfeyqbb-x5T_bJsoiDH9J8X5z2v9XC_HgRdslEAMDVzy8fli471d09B6M93j7sghXCLx9Y_B-QpPhEnETQjzvTliGL98fvc7uo7bfdrLC3VSlYRb2OKa7ApsrPLWUqHiSd-8F6ah6r6rzz6B4Bl3K5kSU8CeFalLbAr2eKCI4fPtHoaffEJYekjITwzx-vq5anylvHTTIso2Lhi3zW8lTlvx595VXgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
گردنبند جالب‌ دوس‌دختر لامین‌یامال ستاره اسپانیایی بارسلونا که اسم او و شماره پیراهن‌ های این ستاره از ابتدا تاکنون هک شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25439" target="_blank">📅 15:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25438">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1Vx5oFQGa_bph6wQJt23P34uz7k4Syvnx7r7r8X55TyYBQySFecBiL1AQAk09UGuyVzrgmCYisG21hlEwtkTrJGHngfhfsklHY73JgMnIaBUgmtrilBninpyBuIeveWAg_5XXkABHO5amXTX2ZVSbfizrEmSfzyuoaNJqgtJiJu7Ck3_EoVp5-iY6Tq-raR6VA1rHSiN2oyxyod3NCrqyUu_IZrnO0ej9edrbIbaaT9N0lX8-hkCRgqjdIeEKgwv43L729FM3AkgyZ7YdfN2xLFPI1Smy0pIT93vRaNIbXqZx2qMQgWZ2DZx9Jh3OcA2EnY0gTxwalkto6oGC8rng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌هوادارمکزیکی درصفحه‌اش افشاکرد در شب بازی پرتغال
🆚
اسپانیا؛ یکی از ستاره‌های پرتغال که درلیگ جزیزه بازی میکنه بهش پیشنهاد رابطه داده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25438" target="_blank">📅 15:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25437">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXGec7yqPCe-veKxg8eJTiw43ksRiedgiu3O2KfDcwPZf-GPHOcPk0zn7JtR-IFHYTWnsCT2zBBVz21yqSedNp22X-9K-hZtUqFlCQWmtZs6FilRucK11rQT5verQRldA4rpZkdB2BnjLeBKHCuJmvxq62X0XTm9hRBzgrGgMPNwkA22DniuFOEmAKtQZnp0wOwRe2mCys7V6ct0aO1GrSZsv2lPh92zo2shikaHms058v3rOeiGJ1GylDOuIUk8qiUsRidqEP7doVUkQspkgg1ymjaTG49u-D38rhzF4Fr-zkt3xV5h9UrcalACb5iVa9Br6jmJo-2YZWpv3CEaxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
نشریه موندو
: باشگاه الهلال عربستان آماده ست که‌برای‌جذب رافینیا دیاز پیشنهادی 80 میلیون یورویی به بارسلونا بدهد و دستمزد فعلی رافینیا در بارسلونا رو در الهلال چهار برابر افزایش بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25437" target="_blank">📅 15:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25435">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JJIySPOSOci1naHMRhWljUKlQwWLx5d1bhB_SkOhs_bRT7KnC91DxhhGHYigGvkEN49TFNSfqu1o_ivcLgTiwNcugkhKs0M3lv86BvYx60whJAy-K64VdGw5eMv9lcgJQn6mzy2I6R8Q78xlg6EzU1AHC9_8Sah1hEhUdFu6aOCmnFSYaAUKsKbRGZcd_eADHiZw6ef9sPlPLnCaPN0NzuvOuGNICHLKRkFdPjQwXy-xES6tV9vIvWRjbox25wswBeNsNJ4TuhvP--Ax_F29NKKE5IZjsOL6cP2-L4dOmYEla5fjLBdFKEfJRg7cr-6KRRUsW45ZM6UynR1IBtI42w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o7SiRZ0Uji18ZhdTBu3xd5jfydzP3Ra4Mjlw2Gvtz32d9veAoZSVsqRqpn0nlPaLBk6d9Ivfn7GnHKzq4BmpIZhEGggMQEWpCqisvJQHxskte2dSHWZmHy9MU22IIkB5gHQ8ovaycutsmicCL4Hs57BgIZT5WAypk9WmlKRUjvOgI0O1V9GfWfDIQZ49h2jC4VSlmAgyovRZKAbucDwDEAONmyh7uCuzosnkdr18q6ASyuoXp8BVdNfrPFKn3PxyMGUcrNEbV7uhB2Oz_18NVk6f4vW7QPNRuscoTVyjEFBHioaMhM2jZWbysqQf_XfTdao488tDC8w0kZ4BR2PPkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
جالبه بدونید دوست دختر لامین یامال قبل شروع بازی امشب گفته‌بودکه اسپانیا دو بر یک تیم بلژیک رو میبره و راهی‌نیمه‌نهایی جام جهانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25435" target="_blank">📅 14:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25434">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56676ff59b.mp4?token=VQvra18ysgDwuRn9PlaDo37w2vKibDknO94NyRfdiFQC5rsugQsQ1AvUCt8KiBBjfk6tycQnXFCFGVBaS0baDodGSVOCf6UvueKZ8ORHQ1SPzgayF1ZeasnyxJxD4MZXRd1gMBmfS2Ryeb1F4c8fjH96qkGh9HFD4N6-R6Jw2rUs84bhfg1EAzeHZvMZwmjdIaFNoMY2U7rTTP_z_Uy-pTAaA6crramqv9nPQm3-MViu-lQdeZfRTuVQhCRRmLlRg-zh6LRVc-EActohVCmLUus0osfrQI3y58mk03SA-yDlBFM0nBQ17b8DqGSQxvd3kxJjOqPsYVxbhpLlnhYkfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56676ff59b.mp4?token=VQvra18ysgDwuRn9PlaDo37w2vKibDknO94NyRfdiFQC5rsugQsQ1AvUCt8KiBBjfk6tycQnXFCFGVBaS0baDodGSVOCf6UvueKZ8ORHQ1SPzgayF1ZeasnyxJxD4MZXRd1gMBmfS2Ryeb1F4c8fjH96qkGh9HFD4N6-R6Jw2rUs84bhfg1EAzeHZvMZwmjdIaFNoMY2U7rTTP_z_Uy-pTAaA6crramqv9nPQm3-MViu-lQdeZfRTuVQhCRRmLlRg-zh6LRVc-EActohVCmLUus0osfrQI3y58mk03SA-yDlBFM0nBQ17b8DqGSQxvd3kxJjOqPsYVxbhpLlnhYkfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
آندرس اسکوبار مدافع سابق‌تیم‌ملی کلمبیا بعد از این گل به‌خودی که درجام‌جهانی 1994 به خودشون زد توسط افراد ناشناس به ضرب 12 گلوله کشته شد و پس از 32 از این حادثه بسیار تلخ، قاتل وی در یک رستوران هدف‌گلوله قرارگرفت و براحتی کشته شد.
🔵
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25434" target="_blank">📅 14:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25433">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUzucvrDclaSSc2D3zx8r2wbL9_FWyNd9y8GGdH3DUA9DUX4_IyZ_7ZLYAz_ruOc4ygbgpcYyhoLbmWQJp5F7peoFHZlVanQa6vBbZhl8I6UinBVChu2HMNACJbJ9P8ioEkJhm43BBmhxb_jkK1GUX6S4CCtc8dXDGXl1Fw_PMPzpyPO-CuYVKTQCsBj-gJYqC-1W8CEWgYQjhj_K_yCLSHsmpqF4jI-Hmc1gjZZ8DefAWlV2WpCBYFgB_rlGguoecpigXhjxB5iNCP7XSsup5YIwi1KcPYBEBgyHTuWh3n3WvN0YFzWiX1Hy_opEmeYyt-KETbxkAMYbQYmcSEeOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25433" target="_blank">📅 14:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25431">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Co5cJieINFyBk_oPT7KpB7AezZDsuIqCBkgN3sDLEpybVzmhpHu-eKl6p8yGgOTigq9eHj7Xgj5-yVYoJ6edd7qK--uWw2YEPzov8_DpOLrKfuN7zcoVBPJZKIPptSBrXOQuqIz2hVaeOaGdKXqUprPQhvhAe0OEfFwfwydkMKO-ZQulEAJVxe_e34Oo1y_89-SK13H_nXFG--9GiG6mol9AUwd0HWvvMhB2KjIgLAQ113ek4QXYX9ryxLpkIyvtC_QW2_Y0OczPqGuMXIQ_F2cY2RwQxZXk6urDYIjC-mbTXRi7rxawaCXAcjIZHp4sKFCf8-vTakcxAZ2P_T_WGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
روز سه‌شنبه هفته‌پیش‌رو اسپانیا
🆚
فرانسه دردیداری‌فوق‌العاده‌حساس و مهم نیمه نهایی رقابت های جام جهانی 2026 رو برگزار خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25431" target="_blank">📅 14:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25430">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9zQQ388TuGpLPVvtTE8aiIQ1g-l74yCQt-i_ChEt85gFUCVtXUIOrBJ5p2a7a54WYqlJ0nWUWRY78-K497NMNsMoUI7hwyJX203oADtSmz5ayKJ0j7nDL3vAejDPpuq9SPChlISDFqz-j1licLpTtQ1DJH-H5pM6hZ3LrsOcodHAePuDSs2FgRrfKSGFy2681g2L5OLhI6HlvbfdjgGozwtGcW9kg56GQUMMb4ojUqgzsgNXIyXvefZULcoLQJFWjO6aH0hYyaJvfz87nCceNibT7lb9p6sgGiny19fxOA4OUSBl2IBCxciVJaAqpup3nsaie4vyi3WytB3MF3d8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛مدیرعامل باشگاه پرسپولیس قصد داره که ظرف روزهای آینده با امید عالیشاه کاپیتان 34 ساله سرخ پوشان جلسه برگزار کنه تا طرفین برای جدایی به توافق برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25430" target="_blank">📅 13:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25429">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZwef7T8GQ9GmquBGZeLEyj8kLkezxntnVog4107NKgxzWnbqeAjMMlLc3SmZ1OnJeMxRwMv1b12NbaBFYcrPPum81HvtOyaIrbjcx59OzA0ZtwnLst4F6OsGKw_HQDwGR5fUdu0PUHBAwe-ajxIdIEbf-7xsFpIoxszBpm1NkdiWNyoITSxGO09q42QVbleiX_hKDEcEYyoMSmd_-ExBi3nc1Xfzc3AFSt9x6G8ajNV2WDfX6fXhqCJ1qLP0tLVgO3xF6P_il7eRjrQYBi34S6iW9UBxd9IWkGvBklt2x5ORMZBmXEtRtbUMX-PT41hRebC4evNu-TIBwsiZnAs3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال بعد از محمد خلیفه؛با بهرام گودرزی مدافع‌ چپ 20 ساله باشگاه آلومینیوم‌اراک برای عقد قراردادی چهار ساله به توافق کامل رسیده و بعد از باز شدن پنجره نقل و انتقالات آبی‌ها بلافاصله از او رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/25429" target="_blank">📅 13:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25428">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o16ypaGDpExvD5vDD1VWuxUC4qvZEYJoXAjNSXJCWz99vusQfZDaTtd2WHVjys1fXbCH6_8gsEa33Z13yliiln9EPnhIyWEVaWj2xaTtLFu1PFTHDhyg3li6sK_ZxFc68AVRuO8dP6WdUeEUxOv0n1Ms6rADF1I0_eMTXTgJ3GQYb13LtsCh2UwigXjoCmixu08jzlcCMYNje2GAsSyTA2gRgh1kWxbDRLwja6_0Z0vXBnbfjLDa1ynpNX4Xwwx8m71baWbUJNePkrxkRNEn1oAOMOEoH72YkFa6WQ5g9mrJwt8cEq6AqRzPwpg0U15Qlb_JJ--irFiNj5aPwZtmmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 21 ساله نساجی به دوستان نزدیک خود گفته با باشگاه پرسپولیس برای‌عقد قراردادی چهار ساله به توافق شخصی رسیده و اگه فردا مدیران این باشگاه بتوانند رضایت نامه‌اش رو از نساجی دریافت کنند قراردادش رو با سرخپوشان امضا خواهد…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25428" target="_blank">📅 13:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25427">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4I0OtZcLOm3ENVTCnrYa6ira66NpdWYx2UI8ugMePnxKB_t10X6kMl9OW_xxKHumW5lLmxJvX0oW5llBpHfqdBUKTPt4ALYaxmUCcOB550EBC6gy0wtBGFFyAD_zqo99oGL7ZjToRd3--RC0AJhSniVgvIAuMa8s4QtP_VzHVS-TvVx0bhNRWCN0nLQ_c5B2WDrsFP7hPTLXUGFjTgogCcdzoczu4PHfLrbwvPcQEc5N8R9WTPbCvnSZk8oSFDRf1cQdb4kbGYp84DDos6RgvMnBaLwWZpwsLGtDVcOP8upg3ydbVPP-5UoZXmMdzQvxszIbaMxv6yugJx3XJsfCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛
باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25427" target="_blank">📅 12:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25426">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHsOWzDL5NOj1eaFl_58yiYmSsqigWnCHZHcZTUewNxbYRanBptebE-CZsqC9l94E_Z9f21VdF_oOT-B2CvvIiL81t0w1SyexJeJNZbEyO7wcievOaOM0wMtviwNfGgBxwlTo4kyJW9NpWVh_eh39vefZsu9PHISScujoOdMKXR1HIrlIwH1nXHl0-xkrktKShYPZxpULTrf6eyJSQ5CR_MkamqBtKDp_V5D0XZ444-pa5_N101qZ-5wlXIWAvEs3jNeUofZkUdbCePT1eLCZKWw30IGW7-b89HvuR17eUpBy1lOysWCSCNjkhkDUX_WXH2Sa0iLJJ4tV5Ukf5C_bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25426" target="_blank">📅 12:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25425">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06676f902.mp4?token=GuN-TaBsD18sNvzrlKdn1JdQgtxngSv6G34DvI9f8Jc6nQ5uWdESWSaq23gNM4c1KX7yjAw8ZfrBnd7IXFP6DumapKsciGlPMwzfz3oBcFtoqhb3F_aDsNUS2XkPphAEC6TGr_8Cz_LpDzupJTO7aCiXleSbBrymaW0Iv1g2Ni3G9ApkWAt4gvzYTaJPyN-V_v9QPB5YwzCFuM7QiF8OK3XLuQaIHINWjhht4QNkW0chSzq1kp_2A-KIaz6DfAJIumPK3D9jaGsqreawzjUG1ZKDdqVaauP53m_TvK2BbOziocBKvHKYFSe6scrZeZFKUx5uDeh4oUBcYfnaypDYSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06676f902.mp4?token=GuN-TaBsD18sNvzrlKdn1JdQgtxngSv6G34DvI9f8Jc6nQ5uWdESWSaq23gNM4c1KX7yjAw8ZfrBnd7IXFP6DumapKsciGlPMwzfz3oBcFtoqhb3F_aDsNUS2XkPphAEC6TGr_8Cz_LpDzupJTO7aCiXleSbBrymaW0Iv1g2Ni3G9ApkWAt4gvzYTaJPyN-V_v9QPB5YwzCFuM7QiF8OK3XLuQaIHINWjhht4QNkW0chSzq1kp_2A-KIaz6DfAJIumPK3D9jaGsqreawzjUG1ZKDdqVaauP53m_TvK2BbOziocBKvHKYFSe6scrZeZFKUx5uDeh4oUBcYfnaypDYSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
رسانه‌باشگاه‌رئال‌مادرید به این شکل از کیت اول این تیم در فصل جدید رقابت‌ها رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25425" target="_blank">📅 11:50 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
