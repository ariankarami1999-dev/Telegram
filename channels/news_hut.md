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
<img src="https://cdn4.telesco.pe/file/I7prIQhZP5BTnu9NtgpCwpYH1GDZ4g8EfQJIH5pYyc2oW0O6oT748SCbD4kdRIaEjGI4rtZJi0tTIqDS_Kce074OXnNSaNLTC8yVu6jyNlk0nsYT2VZonRmsiPEe99rJXGfNQvfpGXGM5B-oqUh-tbjtDsQe_kZ20Z-FVle6UiueyE6kWcNq1Yb_wVLxcRLhejESMxWjnU4JRkaVytn3wreRtxTr5m1KZCi47WnVjrLVAHp5n5t9Ks86KkcvOD0Ja6b8yOTOmvMI4KyianF59Dn2LNEoqkMc6JriFUz9l9WAJixufDoqiZoVVBTFzod9bWy99zosvzWjbpBhgsUO5Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 111K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 00:48:50</div>
<hr>

<div class="tg-post" id="msg-71441">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkEyefNagd0kJ0n7k02Sp6BFLnowPMduf_pCoUulqhY0YnDsb8xorot4s-Rm1vhw70ARTgWWdAP5gy9isbu7rQsLxJRfskXm9tJTTY08Cx_JODacSldPuRsEQvOjJTsGzTh_DmooGWvgJ9Cut7r3-74CtaaIQfB4VWsf8rFzdHTMYq3y5nB4hnMo9Wm7qHE-8KZti7Ug9JLb3PU9hErYfu2fbEspheZPKiqMRy-Z_RS3dGf5IJMyCrMUpzDMEjV4H_LrmO8EQUxLWdl5poEMx2LSMcOLuRr7YL2VIt51KAPsqQTtjKBuQlZmb2QTeBZx5uzOEqtgHSVnGjVAQfNEAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
دو شناور در تنگه هرمز، در فاصله ۴ مایل دریایی غرب عمان، هدف قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/news_hut/71441" target="_blank">📅 00:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71440">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⏺
🇮🇱
❌
🇱🇧
ارتش اسرائیل اعلام کرد که برای تخریب زیرساخت‌های تونلی در زیر ارتفاعات «علی طاهر» در جنوب لبنان، بیش از ۱۱۰۰ تن مواد منفجره به کار گرفته شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/news_hut/71440" target="_blank">📅 00:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71439">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae4183a669.mp4?token=FTrc_v0tooxTKGeMJU_87uZfdMI2lB_VNdtjbYKB3sgbg3-LInyR6YVLQ_IczlWwUmRYxem-Ku83_GRp5-ZAwq8A-ZyE5ZUhc2zr0A6qiwhmJnM_d_kDTlvTaFEVdNwwULTHFKRSxiU7LK8kcyUXkDDqUPwaZ7NOcKm8f0VyZQC2OgF2pclawcJe0nWqNIxvgjjmTtnjqPYIJ-qpMOecclzLTDxOFy6lSJ-YQH-V9DgpJubM-71fGeV3LA56I7oy3rxJ-FJlMXEGpGf4WHtXsP-1TGz7jkRtfkqMz6-B7YZybrFZCZPuAqU3Vq4chseP5_sF_WRzdYrr_S9-XpbzoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae4183a669.mp4?token=FTrc_v0tooxTKGeMJU_87uZfdMI2lB_VNdtjbYKB3sgbg3-LInyR6YVLQ_IczlWwUmRYxem-Ku83_GRp5-ZAwq8A-ZyE5ZUhc2zr0A6qiwhmJnM_d_kDTlvTaFEVdNwwULTHFKRSxiU7LK8kcyUXkDDqUPwaZ7NOcKm8f0VyZQC2OgF2pclawcJe0nWqNIxvgjjmTtnjqPYIJ-qpMOecclzLTDxOFy6lSJ-YQH-V9DgpJubM-71fGeV3LA56I7oy3rxJ-FJlMXEGpGf4WHtXsP-1TGz7jkRtfkqMz6-B7YZybrFZCZPuAqU3Vq4chseP5_sF_WRzdYrr_S9-XpbzoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئو دیگر از تخریب کامل پایگاه عماد ۴ حزب‌الله
@News_Hut</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/news_hut/71439" target="_blank">📅 00:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71437">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4770f428.mp4?token=ERVSWZnS0iCTdi73-UscSWDMPdTL0gcn0-ef1srfJSV7_F8xvVMFnbx1FZzQC1JnUSeUYPQFU12gXw1F1G-QuMgJ8DxN5p4YDiIwOEPdg_AyxW-2ugRkZz-I6k8XLnvgQfBWcLOwDeVSrC3tQlDDJ49sxm-2YUA7BwFf75eK74Q6fdVWoQivPozTTzI5rK8LPXFsrYRZ1G50CW22QgKMpnE_mluDktx_J-IULKZDvVPIzWApoM52xvovSZotFPKLlG7PRyk3od8yKrVLmJcOyBuP3AbsRwOM281Pn3MFxekpNZphW-AFF5RFlxzP9UfbcNgLElySfGkPS6oxNcQrhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4770f428.mp4?token=ERVSWZnS0iCTdi73-UscSWDMPdTL0gcn0-ef1srfJSV7_F8xvVMFnbx1FZzQC1JnUSeUYPQFU12gXw1F1G-QuMgJ8DxN5p4YDiIwOEPdg_AyxW-2ugRkZz-I6k8XLnvgQfBWcLOwDeVSrC3tQlDDJ49sxm-2YUA7BwFf75eK74Q6fdVWoQivPozTTzI5rK8LPXFsrYRZ1G50CW22QgKMpnE_mluDktx_J-IULKZDvVPIzWApoM52xvovSZotFPKLlG7PRyk3od8yKrVLmJcOyBuP3AbsRwOM281Pn3MFxekpNZphW-AFF5RFlxzP9UfbcNgLElySfGkPS6oxNcQrhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
#فوری
؛ارتش اسرائیل عملیات تخریب تونل های زیر ارتفاعات علی الطاهر را شروع کرد.
تصاویری که لحظه انفجار تونل‌های زیر «ارتفاعات علی‌الطاهر» در جنوب لبنان توسط نیروهای اسرائیلی را در همین لحظات پیش نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/71437" target="_blank">📅 22:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71436">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/249279a367.mp4?token=dD_JB2TcDp_xKK_Vq2kVhWtKTCM3hl2JT0o41mFseNpyA-AAbqb67aSur2X2nG58A4mlISFVtsswO2TMUUvdi0o4UcCFzsntCz62IBs1V3rrdEMkIuvNGCm_1HIuT7OuzBv0MmTZeJ6XdYUkAKudYrkwPGex_M5_OiTXzBulSTzwru7BR8jgqLZg0Bo0FllEaIVAj6KIftxCIFP2PJgmKbSZhU-7P4zA4YMQrLsGU6eYa1xJWnk-pwVDeZGs672spHvv8KcDQLDSZTEnzVe-d3jbG5wMcChOtcB49dQcCQuIlMW3fgjz22BWsYxyiej6CcpHW6jtB1QJA32R9eWfQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/249279a367.mp4?token=dD_JB2TcDp_xKK_Vq2kVhWtKTCM3hl2JT0o41mFseNpyA-AAbqb67aSur2X2nG58A4mlISFVtsswO2TMUUvdi0o4UcCFzsntCz62IBs1V3rrdEMkIuvNGCm_1HIuT7OuzBv0MmTZeJ6XdYUkAKudYrkwPGex_M5_OiTXzBulSTzwru7BR8jgqLZg0Bo0FllEaIVAj6KIftxCIFP2PJgmKbSZhU-7P4zA4YMQrLsGU6eYa1xJWnk-pwVDeZGs672spHvv8KcDQLDSZTEnzVe-d3jbG5wMcChOtcB49dQcCQuIlMW3fgjz22BWsYxyiej6CcpHW6jtB1QJA32R9eWfQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
#فوری
؛نخست‌وزیر نتانیاهو درباره ایران:
رئیس‌جمهور ترامپ امشب اعلام کرد که ایران بار دیگر در تلاش است تا به سلاح‌های هسته‌ای مجهز شود. این سخن درست است.
پس از آنکه ما توانایی فوری آن‌ها برای تولید بمب‌های هسته‌ای را از بین بردیم، آن‌ها دوباره دست به کار شده‌اند.
من اینجا، در کنار «دیوار ندبه» و در آستانه «روش هشانا» (سال نو یهودی) به شما قول می‌دهم: تا زمانی که من نخست‌وزیر هستم، ایران به سلاح هسته‌ای دست نخواهد یافت.
هم‌زمان، ما در حال ضربه زدن به محور ایران هستیم؛ نه تنها ضربات سنگین در نوار غزه، بلکه در لبنان نیز. ما ارتفاعات «بوفورت» را درهم کوبیدیم و اکنون در حال نبرد بر سر ارتفاعات «علی طاهر» هستیم.
اقدامات بیشتری در راه است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/71436" target="_blank">📅 22:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71435">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یه بوهایی میاد، مثل اینکه آماده دارن آماده می‌شن تا دوباره مراکز هسته‌ای ج.ا رو بزنن
#hjAly‌</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/71435" target="_blank">📅 21:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71433">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Se0Jp_BZ9FmpzRP2-D4YiES-Xm4zizUQtZpIMVfByk8J3pj1Cd6RtE8acfl0UKE0C_9uA3XzARGEWmYBWpqESsdE5j_u-z3o_XcorfNoXSj-DZKFBpOK2pAVguVcy9Ayeye1L6Q1xzq5v9uNudyxsy8dR7dtjATj0ohadSyuJVnLhyQTnPmbJIUmDIHo6BpgFmaU-cBVvy9awmTgBLlx7bQPvbkOaMm3M84577d00MpZgnG4NJexJWaiJiHpxA3C996etVEiSL9RkGZJBZMxKAFYUmWHwKavArRkXdkyFu8HE3KF6zJAJgFR1vdBI59AkFKorA45cy1wzQP9i_c40A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d882666df.mp4?token=QOB8XMC8osxsly4omY9ekJExlWj-wynlBUbKwTfaE7_PRRP8HuhMlzREWdnZB-YwTAAoH5g6TKpLI_lWNkeR3YpVV1Pgcq1_EiiivsnRpwPVcJ-e4jjJQ4T3d_IkCBuQr73NMVTS6UpDs088PXStpKMeidZxv12hlu0gVUsefjo-86r4iX-fid2t_JeweoDEO_rbVo1H3bx6YMMC-x9HNlznduf_xcQ9SNGCgWH5o-uqdZY4TU4x8NnAyvgRaHC9nGDg1Ne7yvKK05M3WKHUEHiwECJaQr6ddrunLer2eZFdcrn1ZWyTedp8zf4AH5Xq5tfz5Li-BihE0OV-qK51Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d882666df.mp4?token=QOB8XMC8osxsly4omY9ekJExlWj-wynlBUbKwTfaE7_PRRP8HuhMlzREWdnZB-YwTAAoH5g6TKpLI_lWNkeR3YpVV1Pgcq1_EiiivsnRpwPVcJ-e4jjJQ4T3d_IkCBuQr73NMVTS6UpDs088PXStpKMeidZxv12hlu0gVUsefjo-86r4iX-fid2t_JeweoDEO_rbVo1H3bx6YMMC-x9HNlznduf_xcQ9SNGCgWH5o-uqdZY4TU4x8NnAyvgRaHC9nGDg1Ne7yvKK05M3WKHUEHiwECJaQr6ddrunLer2eZFdcrn1ZWyTedp8zf4AH5Xq5tfz5Li-BihE0OV-qK51Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه پاسداران انقلاب اسلامی  اعلام کرد که یک فروند «سیل‌درون» (Saildrone) — یک شناور سطحی بدون سرنشین (USV) که برای نظارت و شناسایی دریایی به کار می‌رود — را در ورودی تنگه هرمز هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71433" target="_blank">📅 20:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71432">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
بلومبرگ:
آژانس بین‌المللی انرژی اتمی می‌گوید فعالیت‌های جدیدی را در سایت بسیار مستحکم کوه پیکاکس ایران شناسایی کرده است، اما هنوز هیچ مدرکی مبنی بر آنچه در داخل این مجتمع زیرزمینی اتفاق می‌افتد، ندارد.
رافائل گروسی، رئیس آژانس بین‌المللی انرژی اتمی، گفت بازرسان به این سایت دسترسی پیدا نکرده‌اند و به تصاویر از راه دور متکی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71432" target="_blank">📅 19:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71431">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3ebe5e9d2.mp4?token=LkHnYoyn5QgZcw_-3ovn6GCnq8Ut8Qp8MD83y92biRF4hAZrO8i4DPLsHQ_nzud2ckwrLUgLMfViW8W5w4ynyVhcYQKHXruw7iKcuLp3NXxWyUpLZiWqPpk5BWEDiwT5uIKk0WoqQNEewLRDdNssstdz1l0FmiePWJAJQNVQMhKSlp3OZ3V5LhbYDBZjW1hjVeeZ8kDB69zCqJa_43BLa-vq4jEjvZLx0UF3HVF-fYvF4OKh5v8C8vE9MgfmtGUqu2iTqihQfXpGLKI4Tco-wVRpQ2SltzIntrJ6O0C6Hj_R0THTeavas4F7RcxOh8-aOze4yA1cmTzf2D_3r-6ZXW3YOuz_NfbIPOkoQiLikWmlurUTl9W-Fv302HatI93Yj4L4kGDh-Q22Btg40KMgHCOUaaxd0qOBBXOT9dkGdOXWvGNO4tY2-JNzVW_EE-SE0cimq_JfWy-GBl60nEAX5MziYyogapnY1G5b1i29BFu7RlUqBA58VcchRZq90CJwqjwy60qC66dRO8RuhNBMvxhm5BY8-CSXisrRsL-3vcy_z1T19YZy2Gk7wuy4N2MXQt-nR7KVDhKVd-1ID7m5jhm8ekuAlTZpz3Nw7Gxlsfml0JXKSQa59776bI1itufyS9n30X-dClpCNV2tsbnGp8FEVDwjcBgbhvGMhC2cwpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3ebe5e9d2.mp4?token=LkHnYoyn5QgZcw_-3ovn6GCnq8Ut8Qp8MD83y92biRF4hAZrO8i4DPLsHQ_nzud2ckwrLUgLMfViW8W5w4ynyVhcYQKHXruw7iKcuLp3NXxWyUpLZiWqPpk5BWEDiwT5uIKk0WoqQNEewLRDdNssstdz1l0FmiePWJAJQNVQMhKSlp3OZ3V5LhbYDBZjW1hjVeeZ8kDB69zCqJa_43BLa-vq4jEjvZLx0UF3HVF-fYvF4OKh5v8C8vE9MgfmtGUqu2iTqihQfXpGLKI4Tco-wVRpQ2SltzIntrJ6O0C6Hj_R0THTeavas4F7RcxOh8-aOze4yA1cmTzf2D_3r-6ZXW3YOuz_NfbIPOkoQiLikWmlurUTl9W-Fv302HatI93Yj4L4kGDh-Q22Btg40KMgHCOUaaxd0qOBBXOT9dkGdOXWvGNO4tY2-JNzVW_EE-SE0cimq_JfWy-GBl60nEAX5MziYyogapnY1G5b1i29BFu7RlUqBA58VcchRZq90CJwqjwy60qC66dRO8RuhNBMvxhm5BY8-CSXisrRsL-3vcy_z1T19YZy2Gk7wuy4N2MXQt-nR7KVDhKVd-1ID7m5jhm8ekuAlTZpz3Nw7Gxlsfml0JXKSQa59776bI1itufyS9n30X-dClpCNV2tsbnGp8FEVDwjcBgbhvGMhC2cwpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جورج دبلیو بوش درباره افغانستان:
این باور وجود دارد که همه خواهان آزادی هستند؛ و ما این را در افغانستان دیدیم.
برخی می‌گفتند: «خب، آن‌ها نمی‌خواهند آزاد باشند؛ آن‌ها... می‌دانید، اصلاً تفاوت را نمی‌دانند.»
البته که آن‌ها تفاوت را می‌دانند.
دختران جوانی که برای نخستین بار در زندگی‌شان به مدرسه می‌رفتند، تفاوت را درک می‌کردند. زنانی که پزشک و استاد دانشگاه می‌شدند، تفاوت میان یک جامعه آزاد و یک جامعه استبدادی را می‌دانند.
و متأسفانه، آن زنانی که در مسیر شکوفایی کامل استعدادهایشان گام برداشته بودند، دیگر فرصتی برای تحقق آن پتانسیل کامل ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71431" target="_blank">📅 19:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71430">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71430" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/71430" target="_blank">📅 19:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71429">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFz2Dw8LYdzSaDugUlzrDj4aECjNmH4c-781vh3kkMvlqMeS__75oxAVDPcPYWh0N4rBeHywxnL0ofwzESWq6FfckUOXs5w7v1Fv7HuSghz683dMcVEdkZOAdhJCug4plqNqrks-Mnp5yFAC0rs3Tgemwi85QX_4elDOZ0UMx33fmkS93dBT2K23eUvaEmZnX846bPeGDtwRFgejoSMDupFaPasSXzOwasb2Br_55d3UP8yn6EnIW-kXANqPkP0z50D7-e3keq3qJDIb7nZJjUhXXw8ZXuurhvk0NLnsOtiq1VoZymqGZrK1M0ey0NsXfZ91JVJqYDnKPt_8j8NsrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فوتبال اروپا امشب دیدنی‌تر از همیشه!
🦖
بازی جذاب صباح
🆚
منچستریونایتد را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار ۲ تیم در تقابل‌‌های اخیر:
صباح: ۵ بازی, ۴ برد, ۱ شکست و ۱۳ گل زده
منچستریونایتد: ۵ بازی, ۱ برد, ۲ تساوی, ۲ شکست و ۱۰ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/71429" target="_blank">📅 19:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71427">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd5897a7d3.mp4?token=niuQJ7MWmscDFYxohfJnLFpWUkcIiMu16rmHsRnCL10_YnmuFTGSVylWH-vk3XHIMWfMl6tNhDw4NVnFiLebDzgsEI-15uRjEZfVhnEJeECJHzmiUYukvvZ7SZ-bsvNcU-5ueKj0oy9_4ttLAuxQF2cjXjqTdZ3bHrNM2qC1dUTLnyaVnePHC5UyM3Z844ILApa221cn4OvezyvaemL7XzGzw2J_2ARjTX9341gHK8Se7lSr6PHGstsBy5JpYKExnukydKzGDPBb_70T93JiQNJnBcgjFh7GBDfAoOhOldtzfbzqgOUAW43mtl2PNdnI-RLZ1ZA-iYJJ50awHj9Eug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd5897a7d3.mp4?token=niuQJ7MWmscDFYxohfJnLFpWUkcIiMu16rmHsRnCL10_YnmuFTGSVylWH-vk3XHIMWfMl6tNhDw4NVnFiLebDzgsEI-15uRjEZfVhnEJeECJHzmiUYukvvZ7SZ-bsvNcU-5ueKj0oy9_4ttLAuxQF2cjXjqTdZ3bHrNM2qC1dUTLnyaVnePHC5UyM3Z844ILApa221cn4OvezyvaemL7XzGzw2J_2ARjTX9341gHK8Se7lSr6PHGstsBy5JpYKExnukydKzGDPBb_70T93JiQNJnBcgjFh7GBDfAoOhOldtzfbzqgOUAW43mtl2PNdnI-RLZ1ZA-iYJJ50awHj9Eug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇾🇪
تنش‌ها میان نیروهای تحت حمایت عربستان سعودی — یعنی «نیروهای ملی» (NRF) و «نیروهای امنیتی ملی» (NSF) — و نیروهای جنوب یمن که پیش‌تر وابسته به تشکیلات جدایی‌طلبِ منحل‌شده‌ی «شورای انتقالی جنوب» (STC) بودند، رو به افزایش است.
فرماندهان جنوب یمن مسیر عقب‌نشینی نیروهای NRF و NSF را در کریدور جنوب‌غربی «عدن-لحج-تعز» مسدود کرده و از ورود این «نیروهای شمال یمن» — که کاملاً مسلح هستند — به قلمرو جنوب جلوگیری می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/71427" target="_blank">📅 19:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71426">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBBVBr7pehkuHfBntN6Cf3uOa9XmiEBH9gCA7McNOEPU0flqxBR88erj0B0WSuSsiH-MjMCuga8KUxjtN-pD8KO3C8vbxHn4y4a4LI2pVpOounlo-2MzoDbjO_4WttK4gCQw3kL7i4nEo1xDGQKdpHYMmHPHK5eY4I9vSIFKL355gTgFvxCTwi-RvisZUCVlB7D__LwJb9NWWHQx8ZBvxlcUwzE5ZKML-PFJrHzMNFCZeqyVrI3bJ5m4W4wPIqbLfehAxI-l2a0cfngCgyCkYKTJtsABv_FMYTBOvD-nwIWLMaT2cjGqsgRLOgVx7lBGrNLKATBJZjLGuy15RnFCbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇨🇳
🗞
به گزارش رویترز، ایران از یک سازوکار محرمانه و شبیه به تهاتر برای تبدیل درآمدهای نفتی به اعتبار جهت خرید کالاهای چینی استفاده کرده است؛ اقدامی که به تهران در دور زدن تحریم‌ها کمک می‌کند.
طی سال گذشته، مبلغی بین ۲ تا ۲.۵ میلیارد دلار از طریق یک «سازوکار ویژه» (SPV) جابه‌جا شده و صرف خرید اقلامی همچون دارو، وسایل نقلیه، تجهیزات مخابراتی و — دست‌کم در یک مورد — تجهیزات پدافند هوایی به ارزش میلیون‌ها دلار شده است.
این سیستم شامل نهادهای مرتبط با چین و ایران است که مدیریت درآمدهای نفتی را بر عهده دارند؛ بدین ترتیب که حدود ۷۰ درصد از وجوهِ تحت مدیریت شرکت چینی «چو‌شین» (ChuXin) به پروژه‌های زیرساختی اختصاص می‌یابد و مابقی آن برای پرداخت به تأمین‌کنندگان چینی، به آن سازوکار ویژه (SPV) منتقل می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/71426" target="_blank">📅 19:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71425">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🍏
اپل از نخستین گوشی هوشمند تاشوی خود با نام «آیفون دو» (iPhone Duo) رونمایی کرد.
این گوشی در حالت بازشده، باریک‌ترین آیفون ساخته‌شده تا به امروز است و نمایشگری ۵۰ درصد بزرگ‌تر از آیفون ۱۸ پرو مکس (که به‌تازگی معرفی شده) دارد.
قیمت مدل ۲۵۶ گیگابایتی آن ۱۹۹۹ دلار تعیین شده و عرضه آن از ۲۳ اکتبر آغاز خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/71425" target="_blank">📅 18:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71424">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uIcqPGj-aCSTfq7pLBgh5dntKN8sm0jHKlAMjoyGKsAjQhQDoze7QnSUO6TQbaq_Ynunz9EGIhyna0sKpvN9eqRG8bg6ozCzYxDnacn2Z3_WOM654o9NcIoKtkXXlwJq3JrG3lENQajQxNAZrS2s4krzvsoqVmhfjT4zXnUkrhxq6ZMFlPqWh5PwOcqWQwfK3-FN870D-tD660iLmEpa_slvkWhbnI6BA_FUaBjHFiJtZiyDbeqiy3KCLezpmoyYUogiptZIdTSd6D9933Ux_9nvVRt-0dTzi-lcrWU4mPhiTbJZnpOnB5PR3NPb8BnB5fi7T9LpYwzXA8WH6lxAdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروط عجیب پدر عروس برای ازدواج
😳
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71424" target="_blank">📅 17:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71422">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ridyQfrhsInQTZafCeiOHrLG3H2Oadj7Ql01cK84o1s8fv5ANRyFBAlQYsEaXqMk4dWbV_q--W8BSVjDyDjU3AIdutstHREW1y1pCDMK1bFuz3SrwoTVV_h8VT_D6ufDUSyznLPcj341zgVzbT3SeHfYxaSf0kqw2zZ-gH9S-8RRoobcv2u_6xdQ5POPNZOO7g72kM2m-6TKv53V1GE1o-xwO7POENdrOS8tPLZ5c5c57zjJ7v-BKMMhaWHAmnobhU7nM32FEmgNic3KgHK-9T6Lnwgd5tznGqjD42sg5zPRz1G_a50IZl1aSvF8DENU6XKdFpwtyjr7TyMN14LdPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dfa56bc26.mp4?token=upE0oUHVJ1IJyYCgB1OkgeolAxf-QD1g-S6hBWWRV6OBlBq6oZKqHQgALCrRPvbeck_idA-wJN5UXJM4raRUEVn7oo-plCGJTqlIe3RXd0p376Al8XHwd_QV0hB7ovnPZuBSAXv7zUCfI9eyq5WxE2MxJ1MmDqTvVgU-gN7RBJsLMtKrVIUPk-r31oiIme3UZBIOa_HumGgE2gO0OIyqgyo5pJn-crBZ6aAdTuUnHnQ1AyPaTL1DkZ3kFSacnp97IlXpCWuvI4_I_ugVFStGIVXbmHdlXiRJp7i5CjOO0KFWUchIXnglxD4FSA9Bp79tvYzpPTjeKq0m0WFKg42QQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dfa56bc26.mp4?token=upE0oUHVJ1IJyYCgB1OkgeolAxf-QD1g-S6hBWWRV6OBlBq6oZKqHQgALCrRPvbeck_idA-wJN5UXJM4raRUEVn7oo-plCGJTqlIe3RXd0p376Al8XHwd_QV0hB7ovnPZuBSAXv7zUCfI9eyq5WxE2MxJ1MmDqTvVgU-gN7RBJsLMtKrVIUPk-r31oiIme3UZBIOa_HumGgE2gO0OIyqgyo5pJn-crBZ6aAdTuUnHnQ1AyPaTL1DkZ3kFSacnp97IlXpCWuvI4_I_ugVFStGIVXbmHdlXiRJp7i5CjOO0KFWUchIXnglxD4FSA9Bp79tvYzpPTjeKq0m0WFKg42QQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
⁉️
به گفته تحلیلگران CSIS، تصاویر ماهواره‌ای امسال «افزایش آشکار فعالیت‌های ساختمانی» را در کوه عمیقاً مدفون پیکساکس (Pickaxe Mountain)ایران نشان می‌دهد.
آنها ارزیابی می‌کنند که این سایت پوشیده از گرانیت «احتمالاً» به عنوان مکانی محافظت‌شده برای کارهای مرتبط با هسته‌ای، احتمالاً محل مونتاژ سانتریفیوژ، غنی‌سازی اورانیوم یا سایر فعالیت‌های «مرتبط با سلاح‌های هسته‌ای» در نظر گرفته شده است.
این تحلیل افزایش فعالیت جاده‌ای، ورودی‌های تونل تقویت‌شده و مرتفع، جاده‌های داخلی آسفالت‌شده و سایر کارها را نشان می‌دهد که نشان می‌دهد ساخت‌وساز از حفاری به سمت توسعه داخلی تغییر کرده است.
اطلاعات اسرائیل حاکی از آن است که ایران می‌تواند سانتریفیوژها را به آنجا منتقل کند، در حالی که ترامپ اخیراً هشدار داده است: «ما ممکن است خیلی زود پیکساکس را بزنیم» و افزود: «ما همه کسانی را که در حال حرکت هستند می‌شناسیم.»
پیکساکس حتی برای سنگین‌ترین بمب‌های متعارف سنگرشکن پنتاگون نیز بسیار عمیق دفن شده است. سی‌ان‌ان گزارش می‌دهد که ایالات متحده برنامه‌های حمله عملیاتی برای این تأسیسات دارد و به مطالعه راه‌هایی برای حمله به سایت‌های عمیقاً مدفون ایران ادامه داده است.
چند روز قبل از شروع جنگ ایران، پنتاگون همچنین یک قرارداد اضطراری ۱.۲ میلیون دلاری برای آماده‌سازی در یک مرکز آزمایش زیرزمینی گرانیتی در محدوده موشکی وایت سندز (White Sands Missile Range) صادر کرد. منابع به سی‌ان‌ان گفتند که این کار با توسعه و آزمایش قابلیت‌ها علیه عمیق‌ترین تأسیسات زیرزمینی ایران مرتبط بوده است.
ارتش به‌طور جداگانه در حال توسعه یک «نسل بعدی نفوذگر» است تا جایگزین نفوذگر مهمات عظیم مورد استفاده علیه سایت‌های هسته‌ای ایران در طول عملیات میدنایت هامر (Midnight Hammer) در سال ۲۰۲۵ شود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/71422" target="_blank">📅 17:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71421">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8709946e.mp4?token=NKypW9aFiG_YfRgv_z_rkKSlsNd3OqcZX5I8SUBZMJZMZ7vglrnnkZMiGd1nAU0VOYdZs2AXWTbRpRmf1V3qiLNBmiJXfNvbXh0JK4I3XqA-nCbSEp0CXysrv1QR_XRGPLLe1p1-J_8y8tzSE0dIpwwRJO8vFhKJ1wS2dEQ_XBpYw43klL_eWe8hiozfjPrpuHeegYPjk2ulU1VOHQVfUZzzDWRaAlCrAg6JgzWC0VbfC-kgHf5Vyn8gz0IdRvOrJBwocxIfyajETGjwb6Nwx5n3uDz5mZC-cpcFHHXZ-xCtWvKlkIYNIfW4BelG1mg2IeGCLj6NJxOqzavDEzGC-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8709946e.mp4?token=NKypW9aFiG_YfRgv_z_rkKSlsNd3OqcZX5I8SUBZMJZMZ7vglrnnkZMiGd1nAU0VOYdZs2AXWTbRpRmf1V3qiLNBmiJXfNvbXh0JK4I3XqA-nCbSEp0CXysrv1QR_XRGPLLe1p1-J_8y8tzSE0dIpwwRJO8vFhKJ1wS2dEQ_XBpYw43klL_eWe8hiozfjPrpuHeegYPjk2ulU1VOHQVfUZzzDWRaAlCrAg6JgzWC0VbfC-kgHf5Vyn8gz0IdRvOrJBwocxIfyajETGjwb6Nwx5n3uDz5mZC-cpcFHHXZ-xCtWvKlkIYNIfW4BelG1mg2IeGCLj6NJxOqzavDEzGC-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
عباسی معاون وزیر راه و شهرسازی دولت سیزدهم:
آقای رئیس‌جمهور!
مگه نمی‌گید هرکی می‌تونه کار کنه بیاد؟
من می‌تونم
کجا بیام؟
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71421" target="_blank">📅 16:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71420">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aea684770.mp4?token=KfveprG7_sjfh9BSL1OCvH2Z6yYyqN8jMUjh4SweBmXz4K-D9TXZSZ4hVrxc9OhlqhilvWlgsvdQK8ErdKO68oxUOeT8UPLNVGKENRGECUGVY4U73QP6YDXmsdUYky8MMWGRXd_2_goJX9IfLj1SDeATzifZBOE5goCxiOSLoTLdLUTmU54j1ajf1r828bgW6Eao1LyqYwYYEIz_odlANQLA2PAB43tUlJYxbENQ7Sy1cuqNN-skY546FgNyvdouIjrekEIHB4ACDOcDPMkKpZxZAy3LEKM5cAt73xC-WhxGkzWD8cgbhnnut5WE1IXaCUUAdIRRFUmFwQDCN01AzTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aea684770.mp4?token=KfveprG7_sjfh9BSL1OCvH2Z6yYyqN8jMUjh4SweBmXz4K-D9TXZSZ4hVrxc9OhlqhilvWlgsvdQK8ErdKO68oxUOeT8UPLNVGKENRGECUGVY4U73QP6YDXmsdUYky8MMWGRXd_2_goJX9IfLj1SDeATzifZBOE5goCxiOSLoTLdLUTmU54j1ajf1r828bgW6Eao1LyqYwYYEIz_odlANQLA2PAB43tUlJYxbENQ7Sy1cuqNN-skY546FgNyvdouIjrekEIHB4ACDOcDPMkKpZxZAy3LEKM5cAt73xC-WhxGkzWD8cgbhnnut5WE1IXaCUUAdIRRFUmFwQDCN01AzTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
حامیان حکومت این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین، دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، ذلت نمی‌پذیریم.
بنزین رو کم میگیریم، ذلت نمی‌پذیریم.
دلاری گوشت میگیریم، ذلت نمی‌پذیریم.
مهریه کم میگیریم، ذلت نمی پذیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71420" target="_blank">📅 16:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71419">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1669b7ca35.mp4?token=fO5L6gncvLGwaXiMekO3KP_Cv3tqZWXs5VVOou_pUqt6ceUZmRYbXl4gHPNZS5bcfLie0tiNmrpndJNCM7LZwPqPfM7WcRdkHfT5oO-AGBwN-omuODrBiKfjaAj6puXsc3MQm9wuoNyTCSJOPWICm6OYGmfI5YHb5XDcpCbueV5lh_IMwW6cbfzMAnRZJG97MTThwsKzcJS2A5C3C4TS6dzNEayrgyhI-JnhQ9tB7m88Z5OnAKYcnO-NWy1ZtWXydV0bUZnzKwCzheTkISvjlDMtLe_f8QnHJt9_NL5VpncLVlKjeVBBN_TT6c1QCgTvoOEeec5CubrPm9K-nfkyHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1669b7ca35.mp4?token=fO5L6gncvLGwaXiMekO3KP_Cv3tqZWXs5VVOou_pUqt6ceUZmRYbXl4gHPNZS5bcfLie0tiNmrpndJNCM7LZwPqPfM7WcRdkHfT5oO-AGBwN-omuODrBiKfjaAj6puXsc3MQm9wuoNyTCSJOPWICm6OYGmfI5YHb5XDcpCbueV5lh_IMwW6cbfzMAnRZJG97MTThwsKzcJS2A5C3C4TS6dzNEayrgyhI-JnhQ9tB7m88Z5OnAKYcnO-NWy1ZtWXydV0bUZnzKwCzheTkISvjlDMtLe_f8QnHJt9_NL5VpncLVlKjeVBBN_TT6c1QCgTvoOEeec5CubrPm9K-nfkyHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رقابت رژیم جمهوری اسلامی با اپستین در کثیف بودن:
یه مرد ۴۲ ساله دختر ۱۴ ساله رو به عنوان زن سوم صیغه کرده، بچه حامله‌ست است و داره سزارین میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71419" target="_blank">📅 15:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71417">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97f71ba05.mp4?token=SK22HcmJlcSwwEHByOB7AAih6nWPXFs6mEXpvPDgVBdLEP3cviPeKeS2mJVuhTnbDST21kph0w45zPopWJHbD0D9eJYNRQoHnaC8uUxVdxlCf443CtHg3CxCvZTf3H1R3xQhrycVIJp9lUx_4mU3kJ58dWRuQe0o30Ia9-4OsI8eHl4rvcCrDcEmXCmGsdX-7PFMTw8wsMKi0lcPFXSPDbb3oXV-jIVzMTYQEWXiGUZtnbV_Rcuj-kigwsSayOHsiTeYhgZ2BDkCVpcUVX40G5ZXISheMoM6RavpaWG1VYJkcNbrrSmCiRSmN0YX8l94ZeT4Qj7-pd2_0S958jLJvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97f71ba05.mp4?token=SK22HcmJlcSwwEHByOB7AAih6nWPXFs6mEXpvPDgVBdLEP3cviPeKeS2mJVuhTnbDST21kph0w45zPopWJHbD0D9eJYNRQoHnaC8uUxVdxlCf443CtHg3CxCvZTf3H1R3xQhrycVIJp9lUx_4mU3kJ58dWRuQe0o30Ia9-4OsI8eHl4rvcCrDcEmXCmGsdX-7PFMTw8wsMKi0lcPFXSPDbb3oXV-jIVzMTYQEWXiGUZtnbV_Rcuj-kigwsSayOHsiTeYhgZ2BDkCVpcUVX40G5ZXISheMoM6RavpaWG1VYJkcNbrrSmCiRSmN0YX8l94ZeT4Qj7-pd2_0S958jLJvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از مراسم ازدواج فوق لاکچری «سامان گوران» بازیگر؛ کمدین و مجری صداوسیما
سامان گوران ۲۶ مرداد ۱۴۰۴ در صداوسیما: نتانیاهو از موتوری جنس میگیره که میگه برنده جنگ شده. نمیزاریم آب خوش از گلوی اسرائیلیا پایین بره.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71417" target="_blank">📅 15:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71413">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gyThFtJs6oWSP2GuJvrZi4lI0nTUUzFun8EvFVR7GFvUl5ZcufzOosoMn9MuQDOE0eEaiqHjPC7K0ZxwSVRDCuS9K4EBu0e56q_zPr8nVH3lTlV-7S3PAmO58t4Kga-9Pil4es5aptIejrSSEBHKMDEg0TMc4DHmP5e-Bqr7Yn__s487Drqj0tkHKG_ouJa5AhbyiPqVzPMc5a9gCYHXvH7p6DIw1zHYHh_MtFSXw6HVugqHDhKQ_GnhbiqVbu8QTpJ__s1Qjiir1tlhn5A2M_N7WznLDOMBcA6So4aS6RJs4mdsjZ0NiNugYsiH4Kh8wtUVekSa4liZWC2j2nI_9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tVgGDOEyIWPTMU6VWJEvdv9kJTpvCgxDZZXmqwzSHbOyXo8iRZNRHCyqxn9AhPYHWoxKYr66Sx1M_LcqY8BWtRAs6NTHfRYjQkZHKnKZLfahs-DpCunnt7GykJGDYeLGqveZhuz31N2LbF6TrzKOzVPBkAj1JMm07xOrXL66xE0fwzMzw485DKNnMcDgcd5xkDkD2N3P91g0KWk_VaiDmQi2376tmaOuFtNUSoBYM-wVkEiYc0gMbqdKuPjNgG5uzeAzAvbpUxKO_MdpJem_dE2BjhBHSk0ffCpPq7nYJuXvm_DC9vLChAMEBjODLyq3QgE1U1v2Jx5lJAWVsFwb1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IFH0KhcWqjT365c3F5xb7HlvlWQoZk1hyoN48wtCRB6LG1wGO90_dEy1KzPbbbPyWH3afpyjFgpSnS936-IUz9MJMQl0rNrNFXx4_Ly-GqB334uCbm6NBrWOso0XZzd3V1O8PE8qPn9oZx1ZDzNI45xAA4d99kH4bV-1kXZKYEHvT7anXHywJ-cxMrb6ourJg3i0XXXAN321OhC7z3S23dRL3WMLOKAdfhWoV42PCkx4QFxBeNhexERRPQrn6KpOAbewKMFi0xyiHULT-Lv6grPa7MwmwwwOvjlskKIDxtERj9d6O4M4lLc3vZkl3_9VhlRIz3TtjKPl1KEdODDskQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fMXjK69jv_6QlGzE3gY8WHQYjzLWXSTBY2M7jO68dWR51MfAXZq0wXGI0ubmUWQSO1LyLIopizZ-XXkGf446gXzsDr22Gh03HT1LHTXxuxb-Oq_gqOpK_HHexGy_SHVCIzqi1g5fsWxQQBUfvftnYRsGiHKAmhzm0yCpgSqb9O5jAS8j4_H0zbtXWpOJqHDakqejm9-HUgA5bBoKF6yC6H8OhxLXcBrfRmEOCONCdjrDcs3aszlf-VV66XDwM4wrt3lCCbSQvbBxleef7uSlWkrGXENMQVcLzilGvIcrlAz1X9h8wHlZ6OSsxpYmvb-q3K9yG7EK6uITqVoE2iomyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇯🇵
👀
شب‌های ژاپن هم قشنگه
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71413" target="_blank">📅 14:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71412">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d4414bb2.mp4?token=Q24n-pTxQ39qWwUvIHiZWgyQjfgkdt5JW0VqJFtFDkBuFpZ2XsIEMkOXCA-ssEm3G4IkDB5ajK1rOVho_-wSQ3i7hgUXXKbSUUdqO5B6W6DAJctG4BlxcaoUgKLxek5Sl3qu0RqKc2d3cGmC8ybeon8V32atGsPcDSUD3-6ECt99U0kVzvPE8524J8q2rIRwVTYpzFbtg1cmvJm1FHcHHoXpxSRKUvLqjqqLUHvef865FiaNz6OTJn9mooDuncWKO0r5ae5czqfthaCZIk_mURpyfx4x4uffrcz47OkVS65k9BjNtGD_7C36zdsbznKcYCNavkIbt5-jewYnsgpCYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d4414bb2.mp4?token=Q24n-pTxQ39qWwUvIHiZWgyQjfgkdt5JW0VqJFtFDkBuFpZ2XsIEMkOXCA-ssEm3G4IkDB5ajK1rOVho_-wSQ3i7hgUXXKbSUUdqO5B6W6DAJctG4BlxcaoUgKLxek5Sl3qu0RqKc2d3cGmC8ybeon8V32atGsPcDSUD3-6ECt99U0kVzvPE8524J8q2rIRwVTYpzFbtg1cmvJm1FHcHHoXpxSRKUvLqjqqLUHvef865FiaNz6OTJn9mooDuncWKO0r5ae5czqfthaCZIk_mURpyfx4x4uffrcz47OkVS65k9BjNtGD_7C36zdsbznKcYCNavkIbt5-jewYnsgpCYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
یسرائیل کاتز وزیر دفاع اسرائیل:
به مناسبت سال نو یهودی، می‌خواهم برای جامعه یهودیان ایران سالی نیکو را آرزو کنم و برای آنها سالی خوب و امن آرزو دارم. شما بخشی از تاریخ پرافتخار یهودیان هستید و همیشه در قلب ما خواهید بود.
و برای مردم ایران آرزو می‌کنم که در سال آینده، ایرانِ آزادشده از سرکوب و استبداد را به خانه خود تبدیل کنند.
با توجه به این احتمال که به دلیل خفگی اقتصادی و فشار سنگینی که ایران تحت آن قرار دارد، تصمیم بگیرند علیه اسرائیل اقدام کنند، به رهبری ایران هشدار می‌دهم: هر حمله‌ای به اسرائیل، به هر دلیل و در هر مکانی، با پاسخی قدرتمند مواجه خواهد شد که ایران را با ضرباتی سخت‌تر از هر آنچه تاکنون متحمل شده است، هدف قرار خواهد داد؛ از جمله تأسیسات انرژی اصلی آن که منابع و توانمندی‌های لازم برای ماشین جنگی و تروریستی ایران و آسیب‌رساندن به شهروندان اسرائیل را تأمین می‌کنند.
به دستور نخست‌وزیر و با دستور من، ارتش اسرائیل آماده و در حالت آماده‌باش برای اجرای این مأموریت است.
چنین ضربه‌ای ایران را ده‌ها سال به عقب بازخواهد گرداند و رژیم آخوندها را بیش از پیش متزلزل خواهد کرد؛ رژیمی که مردم ایران تا این اندازه آرزوی سقوط آن را دارند و مشتاقانه در انتظار فروپاشی آن هستند
.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71412" target="_blank">📅 13:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71411">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZr7BW2VKIck1gbmqMFHVzYSxdf6Xqd1rmCn_nGLcuF6YbQxrk_DxCbQ7y6oEh1Y8XAhxzKcnSwqZG-Jimz55XOKep-Hkb01ZyykIIqB6DFoJgMJyosB7N7tm4fC2TvzNI1h_tKNZH9epj9eq2MtdQzqESQ_f98pfRC0MoZyAZie_-oTrU0fUiW1ocOAJhAIasauxq0w1sR7CMEpkn2BZ6gZSbQEoeAR-6oeuXetvevcznyewyWoNcFGLNV7gH26GxhyfbLNgIyrLKS8Nzlh3atxbN_VI5eQmYQB5Hvx5FVm8uu1i88hidfFN9ZhdHjVM4zzjHvib1SsHhmcUC8uqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
توییت سفارت جمهوری اسلامی:
سرآشپز رضایی در حال آشپزی‌ست..
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71411" target="_blank">📅 13:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71410">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb607ca379.mp4?token=sOv47CbjaAClL4ytZjlJwcfuRtYJOZ9_BK-KgPWkx2Xu1dD9tHkDltvDqhyYZCnPnsL-ae8qEHA3j5KcnBCfTlgS1rIrGHZG9SsJlMeFCb62PcR-1qQPFk_y4hGLBmhiF9i92zit1ZZCx3q0GkweZEDUwCDvaMNbZ9W8Gmu79aGUzcgAsB_-eFP4eBn4HWNsNaYGx9OsuQhCS1DmUe3yCaQbDWXXhMXtlNd8v4J3VJfxOT8m9EDpGrGs1p7vqA29iMnrVhTGcSPT7URYAx2yllvfRg_dxuIgUh1_jylO5DaEvETiS_uQyKsPrzM4Azvwg55wcfgbL40wv7D6MhijPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb607ca379.mp4?token=sOv47CbjaAClL4ytZjlJwcfuRtYJOZ9_BK-KgPWkx2Xu1dD9tHkDltvDqhyYZCnPnsL-ae8qEHA3j5KcnBCfTlgS1rIrGHZG9SsJlMeFCb62PcR-1qQPFk_y4hGLBmhiF9i92zit1ZZCx3q0GkweZEDUwCDvaMNbZ9W8Gmu79aGUzcgAsB_-eFP4eBn4HWNsNaYGx9OsuQhCS1DmUe3yCaQbDWXXhMXtlNd8v4J3VJfxOT8m9EDpGrGs1p7vqA29iMnrVhTGcSPT7URYAx2yllvfRg_dxuIgUh1_jylO5DaEvETiS_uQyKsPrzM4Azvwg55wcfgbL40wv7D6MhijPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
انهدام پهپاد شاهد روسی به وسیله‌ موشک اوکراینی
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71410" target="_blank">📅 12:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71409">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇺🇸
ترامپ درباره ایران:
باید بگویم که این به لطف «نیروی فضایی» (Space Force) است؛ پروژه‌ای که فرزند معنوی خودم محسوب می‌شود.
از همان لحظه اول، ما می‌توانیم همه چیز را ببینیم.
حتی می‌توانیم برچسب روی کت آن‌ها را هم بخوانیم؛ «محمد الفاید»... «میامید» (Miamid)... البته هیچ‌وقت «میامید» نیست؛ هیچ‌وقت «محمد جونز» هم نیست.
«محمد»... «محمد العزوری». و این نام دقیقاً روی همان برچسب نوشته شده است. ما می‌توانیم آن را از فضا بخوانیم. باور می‌کنید؟ از فاصله هزاران مایلی، داریم نوشته‌های روی لباس یک نفر را می‌خوانیم.
ما دقیقاً از اوضاع خبر داریم، اما متوجه تحرکات مختصری در منطقه «پیک‌اکس» (Pickax) شدیم.
به ایران توصیه می‌کنم که دست از شیطنت و کارهای زیرکانه بردارد.⁩
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71409" target="_blank">📅 11:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71408">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f498f58530.mp4?token=nldc6oqBcwWuJEM8g6z1-hkzGSWD9IgyievpZ_iGmknmbItl1zo7BKbyTQVH_ojG1AVgXCsUEua8GTcjvwJtqpFHgwMVgZguYOYp6EshO_wNFdWGpAYIRT6N3yGCu76MU8c9oS7KZ13Ya-tMVG3g2bdFiqZ6FQkaNTjBuifTq6ebbRfl-PFkyENqduvGpcdOTg5b3Bsh5FUevhuZE6VVVGmNRKAXNxUT_24Ir0tJ4fG-8WgjHSrcKzY2jEmLwXQv7OhBrghvYE-_a2pSmsxe6gxEWRTEEbLwbMC-c969aDXAhe1zk9fiEUXGiTXuODncS5sZLu9d4PU5pSQXjLrMTQCJ9epCBS4U4jSLg8q2C2SQ2TPDfuDK4ibeS4n4WdSgKJ5j57BhEaBRWujmRbF1Z1c99rssjONY6rAwS6ZX-mv7BvjlWI_FgpsrKqlvd627yFZVlb62Y-NHoNnLLR8OaLVwNAgy9R5FFcNmblEuLRRJf55xQeSZPZQxBDZ1fz6b1VuBBgi8lHVOjKXqZpE_0AYaibuMUP4g4a8xXgk0_I6lvYzWXHO1H1eWWamudSQS4r29t7SHpxHyElAoiEfwDSZxyT-l7vdsXozZ15QmmL1YS8TPj_rmRKRCI2KYJ0P-riHaSEF94aZQpDO7LNMj2YTme4N8USsbCi5BAxfhuRg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f498f58530.mp4?token=nldc6oqBcwWuJEM8g6z1-hkzGSWD9IgyievpZ_iGmknmbItl1zo7BKbyTQVH_ojG1AVgXCsUEua8GTcjvwJtqpFHgwMVgZguYOYp6EshO_wNFdWGpAYIRT6N3yGCu76MU8c9oS7KZ13Ya-tMVG3g2bdFiqZ6FQkaNTjBuifTq6ebbRfl-PFkyENqduvGpcdOTg5b3Bsh5FUevhuZE6VVVGmNRKAXNxUT_24Ir0tJ4fG-8WgjHSrcKzY2jEmLwXQv7OhBrghvYE-_a2pSmsxe6gxEWRTEEbLwbMC-c969aDXAhe1zk9fiEUXGiTXuODncS5sZLu9d4PU5pSQXjLrMTQCJ9epCBS4U4jSLg8q2C2SQ2TPDfuDK4ibeS4n4WdSgKJ5j57BhEaBRWujmRbF1Z1c99rssjONY6rAwS6ZX-mv7BvjlWI_FgpsrKqlvd627yFZVlb62Y-NHoNnLLR8OaLVwNAgy9R5FFcNmblEuLRRJf55xQeSZPZQxBDZ1fz6b1VuBBgi8lHVOjKXqZpE_0AYaibuMUP4g4a8xXgk0_I6lvYzWXHO1H1eWWamudSQS4r29t7SHpxHyElAoiEfwDSZxyT-l7vdsXozZ15QmmL1YS8TPj_rmRKRCI2KYJ0P-riHaSEF94aZQpDO7LNMj2YTme4N8USsbCi5BAxfhuRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
دو نکته وجود دارد. اگر من برجام را لغو نکرده بودم و اگر آن‌ها را با آن بمب‌افکن‌های فوق‌العاده‌مان — آن بمب‌افکن‌های بی‌نظیر B-2 — هدف قرار نداده بودیم، الان آن‌ها سلاح هسته‌ای داشتند. و من مجبور بودم با عنوان «رهبر عالی» خطابشان کنم؛
مثلاً: «جناب رهبر عالی، حال شما چطور است؟»
اما حالا دیگر نیازی به این کار نیست. اگر آن‌ها سلاح هسته‌ای داشتند، من به رهبر عالی زنگ می‌زدم و می‌گفتم: «جناب رهبر عالی، حالتان چطور است؟ آیا کاری هست که بتوانیم برایتان انجام دهیم — البته به جای اینکه حسابی بمبارانشان کنیم؟»⁩
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71408" target="_blank">📅 11:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71407">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1bfc54b65c.mp4?token=dJfihuujoju1E4Plk2LPfpbyDhYz9GBFens1JEs1fEEkujzlHyycHijZ_1gITt6gHU8j5Ew4ZPvXKb7FlhqlB0xxUK4uk8-IuJsAUfh-pH11wpwPqE95qPlwn-VB67MdMiu0asoqJus-aNO2HbibO9_l3O9kV5sLofpBm_OQ8acA5ngQtk1-ivTW_tyaCIuxkqEkRXC0fEtmP_yCWZzhE-EejVAr9TiLlngg6ysre6i7HK8aZJ64lfe9yLrpfXbzw03_jgar1Z8AXe-IAevJhnfa6rZ852waNCbatk5JVVwYknKwMYwd-8KqwEYuH5MIv1YQCAuZU5tGHG7c5HR2OYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1bfc54b65c.mp4?token=dJfihuujoju1E4Plk2LPfpbyDhYz9GBFens1JEs1fEEkujzlHyycHijZ_1gITt6gHU8j5Ew4ZPvXKb7FlhqlB0xxUK4uk8-IuJsAUfh-pH11wpwPqE95qPlwn-VB67MdMiu0asoqJus-aNO2HbibO9_l3O9kV5sLofpBm_OQ8acA5ngQtk1-ivTW_tyaCIuxkqEkRXC0fEtmP_yCWZzhE-EejVAr9TiLlngg6ysre6i7HK8aZJ64lfe9yLrpfXbzw03_jgar1Z8AXe-IAevJhnfa6rZ852waNCbatk5JVVwYknKwMYwd-8KqwEYuH5MIv1YQCAuZU5tGHG7c5HR2OYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
املاکی:
به نظرم باید اسم آن تنگه را عوض کنیم. باید آن را «تنگه ترامپ» بنامیم.
بالاخره باید سودی هم برای من داشته باشد. قرار است نامش «تنگه ترامپ» باشد.
خانم‌ها و آقایان، می‌خواهم خبری را اعلام کنم: ما آن را «تنگه ترامپ» خواهیم نامید و مطمئنم که رهبران ایران از این بابت بسیار خرسند خواهند شد.⁩
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/71407" target="_blank">📅 11:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71406">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2660237e39.mp4?token=vjBH-v5L7KGzL06FAkUEWe_7wpbyIyeOQfKGAXCRDSZN9GQe7TyLSWraFjmSFj9U_IyDT_03GgjvcNxYQ37DVTZ89Jb9YGBYNu5cDI_8TIEXcnEgmbiNGBWCamkTpChvFVGvrqUM5FQT790R8Res8nkGtXi6bIyDVf0go-r55pfLKdUrAGwa-Pdl8mpI6t8V_vGwqkHApIAXYrz3mCng__QpRdWhdfkOprX0h82ZTo_YrlBytwnun-uLqoNzJAoKRl8ZfSOi-kaC8PKLqoCe9L-xExVZzNBqX8KmkGYajZOa1moQLd4RLIe4AbCPicYEaMPjeJMBz4oCWG1IxU1f8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2660237e39.mp4?token=vjBH-v5L7KGzL06FAkUEWe_7wpbyIyeOQfKGAXCRDSZN9GQe7TyLSWraFjmSFj9U_IyDT_03GgjvcNxYQ37DVTZ89Jb9YGBYNu5cDI_8TIEXcnEgmbiNGBWCamkTpChvFVGvrqUM5FQT790R8Res8nkGtXi6bIyDVf0go-r55pfLKdUrAGwa-Pdl8mpI6t8V_vGwqkHApIAXYrz3mCng__QpRdWhdfkOprX0h82ZTo_YrlBytwnun-uLqoNzJAoKRl8ZfSOi-kaC8PKLqoCe9L-xExVZzNBqX8KmkGYajZOa1moQLd4RLIe4AbCPicYEaMPjeJMBz4oCWG1IxU1f8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
اپل از AirPods 5 هم رونمایی کرد؛
▫️
ترجمه همزمان و زنده
▫️
نویز کنسلینگ فعال قوی‌تر
▫️
صدای فضایی شخصی‌سازی‌شده
صدا رو جوری تنظیم میکنه که حس کنی از اطراف و جهت های مختلف مياد؛ مثلاً تو فیلم انگار وسط صحنه ای تنظیمش هم متناسب با گوش و سر خودت انجام میشه.
اکولایزر تطبیقی نسل جدید
ایریاد خودش لحظه‌ای صدا رو بررسی
میکنه و بیس، زیر و بم و جزئیات صدا رو خودکار تنظیم میکنه تا بهتر به گوشت برسه.
تا 5 ساعت شارژدهی با نویز کنسلینگ روشن
💸
قیمتش تو آمریکا 149 دلار اعلام شده.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71406" target="_blank">📅 11:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71405">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71405" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71405" target="_blank">📅 11:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71404">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSDeMxQcbFdLP_olH4g9Or9B6N1RQ1F7phUbzEAea8D0CDLcSCdYIEg_rMqO-ayFjECwJSyD11iemkimgP-NT9uJ-Tvl_o_p4_PChr5sDIsf2GEEGszU4kVtxI0TmraCJW8De2dFtmYHeVpeZZKKm7qb5WcPI0s4j9ZI2-6pdo7xolUWUoOXwEzRPXOs9ehoVnv5XPsecGuAo7MN3STC54ZGU9Z4I6oUd-Y-VvVyNmyTAmse8Ua6ACCCNQWhKZsU1NOTYiERZxVyHiriSCB_3diNxbltRiuD7s3JlkN5zcDrCJ_y7HQADYyhep6dbBMVXcVjdzc6w60cbwKpQsOCDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پیکان
🆚
استقلال
⚽️
رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم
در ۵ بازی اخیر :
⚽️
پیکان : ۲ برد، ۲ تساوی، ۱ شکست
⚽️
استقلال : ۲ برد، ۳ تساوی
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71404" target="_blank">📅 11:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71403">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86c3602295.mp4?token=Au3bobJSnBQJ945iUX0r-mGKgNBqtvUsvbTjY5xinn9iJ9cijweer9VGFDskqLOoY3H-Od58HLV-f-cr4z_kFfqNn3xLyJ6C-XKqpNHjdJRQNHO7k_G5LOcb0ok36i7p78DueOzW8OaEWO4S3KjgHA-wkHes0M9Q4Yu_6n3dV9PjZN9x11Gs_eppwJYkF6B6KqUbxwZ1ciwzglNhxvim7BPhy9tx0f4PME39xMokKdMGVcqQKVf1iRu1DwEaSLf0MG5TvhByU6LXYLR-zB_A_u95lEmkPRtu-BXcQjDOd7oJ1ZciRA9H26J_Cr5Ue2GrrasNjqwk1qQ617U9JyKTaA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86c3602295.mp4?token=Au3bobJSnBQJ945iUX0r-mGKgNBqtvUsvbTjY5xinn9iJ9cijweer9VGFDskqLOoY3H-Od58HLV-f-cr4z_kFfqNn3xLyJ6C-XKqpNHjdJRQNHO7k_G5LOcb0ok36i7p78DueOzW8OaEWO4S3KjgHA-wkHes0M9Q4Yu_6n3dV9PjZN9x11Gs_eppwJYkF6B6KqUbxwZ1ciwzglNhxvim7BPhy9tx0f4PME39xMokKdMGVcqQKVf1iRu1DwEaSLf0MG5TvhByU6LXYLR-zB_A_u95lEmkPRtu-BXcQjDOd7oJ1ZciRA9H26J_Cr5Ue2GrrasNjqwk1qQ617U9JyKTaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
رئیس بی غیرت دانشگاه سمنان: از همه دانشجوهای عراقی معذرت میخوام، قول میدیم براشون جبران کنیم!
دانشجوهای عراقی فرزندان ما هستن و نمیذاریم کوچیک‌ترین آسیبی بهشون برسه.
اگه خدایی نکرده یوقت اذیت شدن معذرت میخوایم و بهترشو براشون جبران میکنم.
تمام افرادیم که برای دانشجوهای عراقی مزاحمت ایجاد کردن، بازداشت شدن و انداختیم‌شون زندان.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/71403" target="_blank">📅 11:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71402">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1423e28a88.mp4?token=cVpmZ0qJ7A64GfuEZDPtMnZW4Uk3aIXT_btEbILUZ6Ezcdq0qWFxIpv0As0mJuzwVamo-s9NrwjEyu16ldTaIuqn3GyHgQs-ZX7D5NGZh9ceWZZ7IspD1mtIjxTyXETGjrufWFbxt1rl7-mLaIPoZ9U1_jvCsliBsSvhNCNkd5N_-nUBHp96PIUZD5i5hgRGmJSbJYsPZemHAJ5yP4Yp9zAX3MM3o7AuZ9VPPBgYlzn00WqWq15Yzag8WuGf8u3MeiTpjzyCmHZ8S5wYZ53sTX1ndx5bD-OQU4ZPoWv_9gLgRl4JqnAXuEFQRUKDBFG6U80jWBh-E8VSJ8Egf6b8YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1423e28a88.mp4?token=cVpmZ0qJ7A64GfuEZDPtMnZW4Uk3aIXT_btEbILUZ6Ezcdq0qWFxIpv0As0mJuzwVamo-s9NrwjEyu16ldTaIuqn3GyHgQs-ZX7D5NGZh9ceWZZ7IspD1mtIjxTyXETGjrufWFbxt1rl7-mLaIPoZ9U1_jvCsliBsSvhNCNkd5N_-nUBHp96PIUZD5i5hgRGmJSbJYsPZemHAJ5yP4Yp9zAX3MM3o7AuZ9VPPBgYlzn00WqWq15Yzag8WuGf8u3MeiTpjzyCmHZ8S5wYZ53sTX1ndx5bD-OQU4ZPoWv_9gLgRl4JqnAXuEFQRUKDBFG6U80jWBh-E8VSJ8Egf6b8YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف پدر بزرگش چند سال پیش فوت کرده الان ی چمدون پر از پول از پدربزرگش پیدا کرده که واسه ارث گذاشته بود و پدربزرگش تو چندین سال جمعشون کرده بود همشون صد ریالی و دویست ریالی ان و جمعا ۲۰۰ هزار تومنن‌
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71402" target="_blank">📅 10:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71399">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13a43f0b92.mp4?token=NapjnNwUhgX29c6Nezq8oVQ0_gBnsa90RgbS9GxmpUM8qzA1oKnTCU1fSRlJJYuNz11rGEYvV6TNYWruPcqW8Umd95BfMi--T3aCX7O8ILU5TEllYsAqBF1No9RaZSQctSmsEiRR37QMwIQ0acAZxNhULoKmRgR6yS0YLOXyE341q-SkS0hvs53JfqTMRB4CHYQOvF-z8T3xUOB0M5BT8VAZeCAECAojoWvU8GTVGFNb-S-jvguDf54pYm9gZPI4yu5s2MpydH1tPjfNwd4WfQ71G-jDykuZmdQyOERYy81rViY2Cpacy68eLC_x_f664DjkKpoy0cm3vTTH8SoZVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13a43f0b92.mp4?token=NapjnNwUhgX29c6Nezq8oVQ0_gBnsa90RgbS9GxmpUM8qzA1oKnTCU1fSRlJJYuNz11rGEYvV6TNYWruPcqW8Umd95BfMi--T3aCX7O8ILU5TEllYsAqBF1No9RaZSQctSmsEiRR37QMwIQ0acAZxNhULoKmRgR6yS0YLOXyE341q-SkS0hvs53JfqTMRB4CHYQOvF-z8T3xUOB0M5BT8VAZeCAECAojoWvU8GTVGFNb-S-jvguDf54pYm9gZPI4yu5s2MpydH1tPjfNwd4WfQ71G-jDykuZmdQyOERYy81rViY2Cpacy68eLC_x_f664DjkKpoy0cm3vTTH8SoZVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
«موسی غضنفری آبادی» نماینده مجلس؛
فقط به خاطر این کلیپ کوتاه ۱ دقیقه‌ای از «شاکر بوری» بلاگر اینستاگرام شکایت کرد و به ۱۳ ماه زندان محکومش کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71399" target="_blank">📅 10:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71398">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNQNOdAAhAbNum5Z9eGKuA5V6z1AQVaZfdxZadcIoNTjO8NEludD0AteRrvwFgJwmqVRFJNuIG0I0B_qXJrKEpoSYTft2oUXIN5KaewoaXs2ZC7kzDnStJCZ_gBnQLmLd8cjHtMwEE8WK0UbKdxGctmTFMaHN3z1nXxv9MFYeAjvoU6EBJ0w1YkXedUE55PtyCf6_uJ_F88Lkbya3fQ5QawdOo_cZVJGndZ7vcjShO2tvngjxo9a9vFIcEvBX25SPHqo8Kz80tMAdyXnLgbEnLIHwhrUlgaMTmT7_bfm3KXitHLQxEmp9YohQXt4gzjC2_jlgH9UtybMDa6eAZMe6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇵🇰
🇸🇦
رویترز:پاکستان در پی حملات گسترده گروه حوثی‌های یمن به عربستان سعودی، پیام هشدارآمیز ریاض را به ایران منتقل و از این کشور خواست تا حملات حوثی‌ها علیه عربستان را مهار کند.
اسلام‌آباد پیامی به تهران ارسال کرد و از آن خواست تا با استفاده از نفوذ خود بر حوثی‌ها، از بروز یک بحران منطقه‌ای گسترده‌تر جلوگیری کند.
به گفته یک مقام ایرانی، ایران در پاسخ اعلام کرد که «کنترلی بر حوثی‌ها ندارد.»
با این حال، دو منبع ایرانی به خبرگزاری رویترز گفتند که تهران حوثی‌ها را به تشدید حملات تشویق کرده و وعده تأمین بودجه و تسلیحات بیشتر را به آن‌ها داده است.
پاکستان اعلام کرد که هرگونه نقش نظامی این کشور ماهیت تدافعی خواهد داشت و بر حفاظت از خاک عربستان متمرکز خواهد بود، نه انجام عملیات در یمن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71398" target="_blank">📅 09:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71393">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YEmsJhIJmQ19hYeTPQTHZ-X58wGcyM71aOlHPQB-lj9GuaqesIQhkbq_5coDzMAnyal486kCsv3INFPDQPhkBHJX9VzmQFdpJtBytwVGk10ABDrI19Wf2eTFrMHNnVwWM0QvAhbmy7FQPeh1ocnUYVrw8FXYPBz2W7i7UNe4iVBTdDcSGOqahM7AXQoAAMgXllk7_ZAeU-rhRLhAg_W0WdwTtR_IDQFaR8aiKy3CfN_qB49E2fjlBCJmdDnxdJUgFhbQvGcl53ym8ebaxOe5UqJUgliSThYEB2Jqv8fGEgZxS89DJkVmDbBjjC9G8HXF0WAbxRQC8TDaWPX44smKhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UYKDpPfVyRL3WiI7Og9rWwntqTor11nlw1loVBsfnq_lsvN-2RbDSD5LfOCA6xcjC8-xfX7z64U6W-sLn8ab0BjbxScZBhEqJd97BFVBkFnFb4kYIXCoYe6GgiaqNEDYp5m8sZ2zdz3v2hIByxuRS_BoC3RSZrMyrUl7_4VQ0ocKNMEUA2mmzNeExGvPKMVHnwFCS9BEpchSomnAE4iQwtvXA4MrksmPZGTpc3BvV6m4khqsssct0UmCe9cY0jueedrnD5CszwznRticb7DSbbW_ga6o1jTguOedlb40RlVYXMKk6TFAvGtVFyp29ch56JNmP1dlAkS4WPtQrvQZ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hexg6RE15Or6bOEOW7zVO5NBcNKyMp1hzH9f5SNNPhrq7hMJTFrSajG3bC2PwR9LZayhF2tNr2hCbAw7ImX074ZpIMf4ZOWKrOpm2joidsAeQlUeUetdTJ7as1PnK5Hk28vswfn2HFTdDJLvMDG1XwpL1Qmjf2sMVhMou8lPkSPSRXFv5Jx1C3uhn2NztD08FA9yYLsjjgDQj2ifCaJy31Pyh6ywdMa-xFlrT1T3Ul1Q8mBCu7VK5OEDPkpXvsdaJqNTWKke1nqVzjGtA5aieyi7GuvmHCJz-EVIqJYbVL844heCHrcfN_9pSv5FNxM11IpN9FnUtdNTLwAERD5T2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MWKnYQU9hiAS7OmkRuV31Da1h6fptgSlG08vZSZDT-mWvpFkQ1RTWYux0nSil_R5MYC_uIfJ8GJwcuHmNZFspwlO2fwakOj1ljomihElaDrf2rj5idkyRLzu0LezXtsBOqnD1CknrgtvrxGC9nJ0NwQ9WVe7L6fHi3ZE-Pee7Gwtj-kG18YYP-2bYnwoUsZk_XAPbERlZr-lNEQW3xPWQJhXzRXVMiV4PTQcvzt_ROmemRdDvxw-nqh8NjgQDWom3P1Ov73-MtcjwcF12foiIc_vZdmJuo_RTSWzS-rKQUxCMT94KSGnB_aJ18sOLJ_CTizlQBGvrZxbVE4M5sgcLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5fed9d1b.mp4?token=WbSpEn8tVdnxOaNcWEIH8uXMjaouZ0X4kUNctioW_xHOsiTXnk8pf3b_e5nKqAociPTmDWd7dwRgYHiBS17Y-GybzRVBys5Rvdm6rDHwM-61UNw9PrXRUlIuVID7x-axsvMijSxHGOQD8vqD_2M8gVK9jF3J41Y6Dk7HKxO5LkwgFVqRH1u0h7xaQykmyUmGT2DUdsNP2X67ycVSwOxaWM3V0eKs1W7kQW11O_KcH0Z8RSHLjqZDhGMLHrJzL6WKWQoFVYLS9bBj6X7yUUwNgoPgK1upeLPX8kNojKR8x1xqK5_QxOX3v6YeKxH23LUSr2Db7xvTSmqmJ1QhH_pEVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5fed9d1b.mp4?token=WbSpEn8tVdnxOaNcWEIH8uXMjaouZ0X4kUNctioW_xHOsiTXnk8pf3b_e5nKqAociPTmDWd7dwRgYHiBS17Y-GybzRVBys5Rvdm6rDHwM-61UNw9PrXRUlIuVID7x-axsvMijSxHGOQD8vqD_2M8gVK9jF3J41Y6Dk7HKxO5LkwgFVqRH1u0h7xaQykmyUmGT2DUdsNP2X67ycVSwOxaWM3V0eKs1W7kQW11O_KcH0Z8RSHLjqZDhGMLHrJzL6WKWQoFVYLS9bBj6X7yUUwNgoPgK1upeLPX8kNojKR8x1xqK5_QxOX3v6YeKxH23LUSr2Db7xvTSmqmJ1QhH_pEVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
شرکت اپل با انتشار این ویدئو، رسما و شرعا از آیفون 18پرو رونمایی کرد؛
🎨
این گوشی تو چهار رنگ عرضه می‌شه:
• زرشکی / شرابی (Burgundy)
• مشکی تیره (Deep Black)
• آبی یخی (Glacier Blue)
• نقره‌ای (Silver)
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71393" target="_blank">📅 09:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71392">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71392" target="_blank">📅 01:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71391">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T-TZ_Xd-aaTN7X_krSYoHGILZo6nytd4ti2rvUo4nGFBv0O7vbPlYoY9OdOhcIb_cs2VI2zYtCONYMDTNOJs27f6kFKRdDyHSV2ULcJNeZSxUoKCXndTWs7-fvItTRzXqLjUF7_P2XmmxpJLo0-QSM0HWxtlCc1-QPXWOKNepjBiIA110k30zD6857zy7nkd8RywZoyYm9QkmDOJjUAnaAE3nEN5btJ55V-8T9FZO60PwoEH68raw0QdPTLcYheFozsbCJgN5eiBSp4bIN9TX-MNrWNCUrcsTGuAsMjbK0EzojL_DdCCQUgbUnGmf8IAilIzufGXGuzNxjn6cuPFxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71391" target="_blank">📅 01:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71389">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iRiLvjR0nc6Z8viAaoSmtKCMfulY1amIjsUhs-Y3-ploSBUHl3QS6LXHIn1SIcwTdgd4-0LhJjpWwiPezPlsyz9fzqY8XzXUpFlnmg0dcEAwDk8fS9Yo6stFwj5FUb4dInUmIpBslo3N87grOTgE3huZg84mNBQIiROXFTSRRL_oQw9PHPVbHejiQQ6YSZU2cyOP-jknpBRK16W9FtiybKd0nFbgWCrblTey2QZE5CR1iZC9rUIPK_4ipxXnYcZIGq4D43adtQcZWAJONzYW45XMtY__wJ0yhDVM8E3h45kFOe7SfvD_H3Hub1b9WBuX5tb3Q4YZhJn0qmK9vDZPkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EnAP-ED9c9mvJ2v55lrUUj8lhM1VMxx-qFvm7cecU2dt7VFpAwDJb9WLHe1hixRGEYAQeeTOR3TOifeF41VFHJxFMd6KYDE96SWUosTAChv1axhiYafJAqGxlkbXbcIAEgw1R8L5pSKpRIcrq9wBOvZhMTr6iZ5RhOHyaYR2JnvlGQhhUhR-p5FgoyXrsruJol4zxYvi8tUUkwfVuWTVU38YP7xa6rmjq4eTjgop7tiqTvXn7sL9KRa1ru6xI0vsW2g4OIaalQ7y-V3Q0PSDCd8IJiALzNm1bI7FWYD_HkEvogaCM0baBoO1T1qv5kM_PwZ8BTjKls-V3Bi0zlLkeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
به گفته منابع عربی حوثی ها وارد منطقه حیس شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71389" target="_blank">📅 01:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71388">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
فارس:دقایقی پیش صدای چند انفجار در مناطق ساحلی سیریک و قشم و مناطق ساحلی شهرستان میناب گزارش شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71388" target="_blank">📅 00:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71387">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
گزارش ارسالی از قشم:
قشم هم در خونه ما لرزید
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71387" target="_blank">📅 00:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71386">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
دقایقی قبل صدای یک انفجار مهیب همراه با لرزش زمین در کوهستک (هرمزگان) شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/71386" target="_blank">📅 00:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71385">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/240fbc3c81.mp4?token=GVPC31tjmT1QA11ES_W80M3ypAezOvQfhDA8b2-WR6_JOECPR96jHLgymAnzLtqbivdPbh9l5epjHXw-EHfiyakRv8WLDaTgdaVFBKM-frQGj02K7sRxnL14V6KapnF4-2PkbBJnKk1rDGnmeRdLRWW5yVHraDlKSME4Rr1LHRuTHdcgXL_hX1oCCgctWzQ55H1CzSEs-ssu_VLnE1Shs3qjcjOdls3s7MwHNovfhstInsAdoS-gbwbzJQW2SjAV1Gal4K6WF7fd4HFKoOBELaLvyGgPGsFyj7deBxOVuny_UF2Y6TuRB8gF0lE_JvwSMC-08XPXdTH-c9Zo1amikg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/240fbc3c81.mp4?token=GVPC31tjmT1QA11ES_W80M3ypAezOvQfhDA8b2-WR6_JOECPR96jHLgymAnzLtqbivdPbh9l5epjHXw-EHfiyakRv8WLDaTgdaVFBKM-frQGj02K7sRxnL14V6KapnF4-2PkbBJnKk1rDGnmeRdLRWW5yVHraDlKSME4Rr1LHRuTHdcgXL_hX1oCCgctWzQ55H1CzSEs-ssu_VLnE1Shs3qjcjOdls3s7MwHNovfhstInsAdoS-gbwbzJQW2SjAV1Gal4K6WF7fd4HFKoOBELaLvyGgPGsFyj7deBxOVuny_UF2Y6TuRB8gF0lE_JvwSMC-08XPXdTH-c9Zo1amikg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛پست جدید دونالد ترامپ در تروث سوشال:ترامپ ویدئویی منتشر کرده که در پایان اون بخشی از سخنرانیش در زمان آغاز حملات مشترک آمریکا و اسرائیل به جمهوری اسلامی آورده شده که میگه:
🇺🇸
ترامپ:
این رژیم به‌زودی درخواهد یافت که هیچ‌کس نباید قدرت و صلابت نیروهای مسلح ایالات متحده را به چالش بکشد.
🎙
سخنگو:
او به جهانیان یادآوری کرد — همان‌طور که بارها و بارها گفته است — که آمریکایی بودن، نمادی از چیزی شکست‌ناپذیر است.
اگر آمریکایی‌ها را بکشید، یا هر جای این کره خاکی آن‌ها را تهدید کنید، ما بی‌هیچ عذرخواهی و درنگی به سراغتان می‌آییم و شما را از بین می‌بریم.
ما آغازگر این جنگ نبودیم، اما در دوران ریاست‌جمهوری ترامپ، آن را به پایان می‌رسانیم
جنگ آن‌ها علیه آمریکایی‌ها، به انتقام ما از آیت‌الله‌شان بدل شده است
🔴
ترامپ:
خطاب به مردم بزرگ و سرافراز ایران:
لحظه آزادی شما فرا رسیده است.
وقتی کار ما تمام شد، کنترل حکومت را به دست بگیرید؛ این حکومت از آنِ شما خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/71385" target="_blank">📅 00:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71384">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71384" target="_blank">📅 23:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71383">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/364cd7494f.mp4?token=CEK5UP7gxDk0F2RFRoJxNjTPEoYNWdoZVlmtupZ-t7hCbC7GdALQkKCGj8TpYHdobiJdBPecJqwPPfCnQ77rFK3OgvFnYfFqhJwnkD_AQKYZo0aO8WY-H8hYaDz88Q-K6J7hxAAvuT4lIiTOOWpHayL7Xdcq1LpAMk3CKeaV10DKllJuK8UreZ602OYkO1XCXRS4RmUgwdTaUFC54wKb6cXxWwJ01OrVHNZzXC7OcxAzZTJl4osTpuKuLUHSOvi9SBef9L8vAhgGv800tiT2zVwRpB4MImMmc4EmJNLV-DkGeeDZ6G3UsPMUg4U_W2jrKJW4f_5TC8bvFCkgpBX1ozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/364cd7494f.mp4?token=CEK5UP7gxDk0F2RFRoJxNjTPEoYNWdoZVlmtupZ-t7hCbC7GdALQkKCGj8TpYHdobiJdBPecJqwPPfCnQ77rFK3OgvFnYfFqhJwnkD_AQKYZo0aO8WY-H8hYaDz88Q-K6J7hxAAvuT4lIiTOOWpHayL7Xdcq1LpAMk3CKeaV10DKllJuK8UreZ602OYkO1XCXRS4RmUgwdTaUFC54wKb6cXxWwJ01OrVHNZzXC7OcxAzZTJl4osTpuKuLUHSOvi9SBef9L8vAhgGv800tiT2zVwRpB4MImMmc4EmJNLV-DkGeeDZ6G3UsPMUg4U_W2jrKJW4f_5TC8bvFCkgpBX1ozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
⭕️
پرزیدنت ترامپ:
انجام کاری بسیار فراتر از توافق هسته‌ای.
چیزهای بسیار بیشتری از هسته‌ای وجود دارد.
ما به توافق هسته‌ای خواهیم رسید، این ۹۹.۹ است، اما چیزهای بسیار دیگری روی میز خواهد بود که سه ماه پیش روی میز نبودند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71383" target="_blank">📅 23:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71382">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8c1afb2e.mp4?token=IkcD5r_tvmhvOuneo8f0_qYj-4PQpotPPcZLG6NXWICYDmD7-6zG6LMGKzcoch52d_soqxPWhmsFJ0LA1QSRyF9CPuKilLheV8OtOfR3TrUo8Bm98YfpUx87AOeRTdOxx0mgKCycI9HfP3NDngQ9eqToaZlfe2PBu4X9dvvFZ2ub1WoydSUQWNjeBef3XyCX2fgowbyKwJ1sNZ0N-Wdmzr-tAbxDS56M4IWuy_oJ63_gfaHjCWdCo7fCmI6TZUm5bWj5jsMLN-VEqLdGko3clZ-JQ138jGw_PPczmvLsswIWYkJNZ3czZQq6EfEMoZibtmfjvph9EmJ1bwyYKkDo43A0l_R4Q8nwz4Ujm0opdG68kjB9BSK8sGDIrbub0885UYtF8oheqn6tccbrxY9OWgd9H6-8mkHju9dyU-Giu_Jobpy1aOjWmBnMfkICsOa78x35R4n4CQ4bE5qaBAWq0S20gqtKsA7LLzZhs39td3GolBB5YQiuCs9lI7rgCRTE5YGRYL9KsA7x7PzYDz0PQn7-VdoOGjjIhcZw_OMGWQJhCBZXSW7JVGID54DMRgBryE-HNWc3bfE7K1IGYrQsspSRtRgaTRSpFdKnHyrIWZygHEjm2BB6LD2Qh2TqL3Bc0F5cENRlptVTDmXEPhy1Vi-0qkXFBjXnCK0STjixfT0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8c1afb2e.mp4?token=IkcD5r_tvmhvOuneo8f0_qYj-4PQpotPPcZLG6NXWICYDmD7-6zG6LMGKzcoch52d_soqxPWhmsFJ0LA1QSRyF9CPuKilLheV8OtOfR3TrUo8Bm98YfpUx87AOeRTdOxx0mgKCycI9HfP3NDngQ9eqToaZlfe2PBu4X9dvvFZ2ub1WoydSUQWNjeBef3XyCX2fgowbyKwJ1sNZ0N-Wdmzr-tAbxDS56M4IWuy_oJ63_gfaHjCWdCo7fCmI6TZUm5bWj5jsMLN-VEqLdGko3clZ-JQ138jGw_PPczmvLsswIWYkJNZ3czZQq6EfEMoZibtmfjvph9EmJ1bwyYKkDo43A0l_R4Q8nwz4Ujm0opdG68kjB9BSK8sGDIrbub0885UYtF8oheqn6tccbrxY9OWgd9H6-8mkHju9dyU-Giu_Jobpy1aOjWmBnMfkICsOa78x35R4n4CQ4bE5qaBAWq0S20gqtKsA7LLzZhs39td3GolBB5YQiuCs9lI7rgCRTE5YGRYL9KsA7x7PzYDz0PQn7-VdoOGjjIhcZw_OMGWQJhCBZXSW7JVGID54DMRgBryE-HNWc3bfE7K1IGYrQsspSRtRgaTRSpFdKnHyrIWZygHEjm2BB6LD2Qh2TqL3Bc0F5cENRlptVTDmXEPhy1Vi-0qkXFBjXnCK0STjixfT0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
در مورد ایران؛ آیا انتظار دارید که [چنین روندی/مذاکره] زمانی آغاز شود؟
🇺🇸
ترامپ:
راستش را بخواهید، جف، ما به دنبال چنین چیزی نیستیم.
در ابتدا می‌خواستم به توافقی برسم، اما اکنون کار از آن مرحله خیلی گذشته است.
در حال حاضر چیز زیادی از کشورشان باقی نمانده، بنابراین ما به دنبال آن نیستیم.
بله، شاید مذاکره‌ای صورت بگیرد، اما این چیزی نیست که ما در پی آن باشیم.
🔴
این جنگ بلافاصله پس از انتخابات ما پایان خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/71382" target="_blank">📅 23:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71381">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088801b967.mp4?token=aksucCcgjxnuj2EHQEicEBfDUzCFpd3t0GQlRpZcrj8IXRCIrIuP3gpaidv1LAetq6GAimxQvMprPacQAgfop8hOGqM51yAzLkIALXIfQkijV4jNqMT0L6YPsaPlRDTuOqtaAFkwqDl3t1PQeN93kijMXoekWwzZW6jVVcbxfYLXewowOkyOZJjR3YM6SVpP4SRrbsff_cM2M3ThOQovds4Hny3FOOSFiKDZPLrsiGj0HM4_3ggXK0w4_0SfheTmc7nvpXXhu8nVYi_8qOd9qOh6st3dFePkUghz_qy6u_35RQOOkUmnMIhRF8fx76h_VraFBZgcykOJAfvfaBj4R361xelX8jHBanwKZy0bxFa-MSWoYXolJOGCHlCMLV9dMGVhpTDBQROmDbBmFYrfPq0GViD4aTMQgkkyWjlgB77TsQQG3FmUIT_VXXIvz-l7ZGUfeji1e6aIU_Z9DZ2PWs1Bxmba3srbq9pi3MDtyS72TCwnuI2Q4qdSZ20xMRPRWiCFIOPSWGXlW2ewl0fqIzzh9v039DqNIwcL65_u3cAJJIvDc57235sHtdo3-8zbpR-MsmXdz8akaGVGD9NAIlSAFa6qiriJWwkAqv75P3N3WXBh9BezcXeh6SWZfwgUiSOG0UwZrXtl4F6GiIzLS0lHZpxOvqPC38rn-IffNy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088801b967.mp4?token=aksucCcgjxnuj2EHQEicEBfDUzCFpd3t0GQlRpZcrj8IXRCIrIuP3gpaidv1LAetq6GAimxQvMprPacQAgfop8hOGqM51yAzLkIALXIfQkijV4jNqMT0L6YPsaPlRDTuOqtaAFkwqDl3t1PQeN93kijMXoekWwzZW6jVVcbxfYLXewowOkyOZJjR3YM6SVpP4SRrbsff_cM2M3ThOQovds4Hny3FOOSFiKDZPLrsiGj0HM4_3ggXK0w4_0SfheTmc7nvpXXhu8nVYi_8qOd9qOh6st3dFePkUghz_qy6u_35RQOOkUmnMIhRF8fx76h_VraFBZgcykOJAfvfaBj4R361xelX8jHBanwKZy0bxFa-MSWoYXolJOGCHlCMLV9dMGVhpTDBQROmDbBmFYrfPq0GViD4aTMQgkkyWjlgB77TsQQG3FmUIT_VXXIvz-l7ZGUfeji1e6aIU_Z9DZ2PWs1Bxmba3srbq9pi3MDtyS72TCwnuI2Q4qdSZ20xMRPRWiCFIOPSWGXlW2ewl0fqIzzh9v039DqNIwcL65_u3cAJJIvDc57235sHtdo3-8zbpR-MsmXdz8akaGVGD9NAIlSAFa6qiriJWwkAqv75P3N3WXBh9BezcXeh6SWZfwgUiSOG0UwZrXtl4F6GiIzLS0lHZpxOvqPC38rn-IffNy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
لطفا شهربازی که میرین هر چی رو سوار نشین؛ بعضی موقع‌ها همچی مناسب نیست و شیطنتتون گل نکنه بخواهین یه تجربه کنین.
این فقط دیگه نریده بود تو خودش...
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/71381" target="_blank">📅 23:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71380">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0632abba0.mp4?token=pBur4a-deGVXVXT6sfGvL_s9QFpgv74GPzU4FNIGop-cbbo_KVYVIsA35yWY6nkzQb1GapEpHMfWXsYxvCosKs0H5-aFgtNKFF72lUqKJi0GBp-soBkeJD5I67jK57hlTHNfei56EOdTpxttlaOUkfzOKySPIFo-mIU7GFOGXCYqGThP_tYWsFCcRPzKfLbZi44jk8Szoi5wqZ7z1-OtwgU4KQ4sskFBa3CLYVWNmNUv30DPPza8X8i5TU2TOaeoqMQ87bMO8ue5VpoL1vB7EX4ZH_wvlWjONz0nhe5n2IXt28Zi2Fb7DFLtltF8XHlUxmc8xITH7k-vW9TPna1owjWa2c621myK9MLtNdmeGupBZFvKk6STRWcGgSgiPk6TAiBKWsA3N6UrQtSzQ-tKw9rcfZ_lAi1tZIkJJD6Rleezbt0KAHI78yB-7Q1V1zNkDjA1Ob9tGQjKBDia3sRAkZgiyo5iPK9RXusBKFGaZBA0bBOUsv312mL7P6diSyn1Gf7z0S2QAdNRoGfvshx9jF9naijZ1iqi2aefIQzFLVa7I8OT9C_QbtcwbH6NhbWptEKiNHhQIS1rQsCZHU0IVQbPyluCuaSlrSn5wIqtEmF5qGO9xgFqjZLSoZmXh88oTSqA5_dXoEX2nb_G6SM2osvmq8bF782m97-nsltQrcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0632abba0.mp4?token=pBur4a-deGVXVXT6sfGvL_s9QFpgv74GPzU4FNIGop-cbbo_KVYVIsA35yWY6nkzQb1GapEpHMfWXsYxvCosKs0H5-aFgtNKFF72lUqKJi0GBp-soBkeJD5I67jK57hlTHNfei56EOdTpxttlaOUkfzOKySPIFo-mIU7GFOGXCYqGThP_tYWsFCcRPzKfLbZi44jk8Szoi5wqZ7z1-OtwgU4KQ4sskFBa3CLYVWNmNUv30DPPza8X8i5TU2TOaeoqMQ87bMO8ue5VpoL1vB7EX4ZH_wvlWjONz0nhe5n2IXt28Zi2Fb7DFLtltF8XHlUxmc8xITH7k-vW9TPna1owjWa2c621myK9MLtNdmeGupBZFvKk6STRWcGgSgiPk6TAiBKWsA3N6UrQtSzQ-tKw9rcfZ_lAi1tZIkJJD6Rleezbt0KAHI78yB-7Q1V1zNkDjA1Ob9tGQjKBDia3sRAkZgiyo5iPK9RXusBKFGaZBA0bBOUsv312mL7P6diSyn1Gf7z0S2QAdNRoGfvshx9jF9naijZ1iqi2aefIQzFLVa7I8OT9C_QbtcwbH6NhbWptEKiNHhQIS1rQsCZHU0IVQbPyluCuaSlrSn5wIqtEmF5qGO9xgFqjZLSoZmXh88oTSqA5_dXoEX2nb_G6SM2osvmq8bF782m97-nsltQrcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛پرزیدنت ترامپ:فکر می‌کنم جنگ بلافاصله بعد از انتخابات تمام می‌شود.
دلیلش چیست؟
چون دیگر نمی‌توانند دوام بیاورند.
آن‌ها به‌شدت تلاش می‌کنند بر انتخابات تأثیر بگذارند تا گروهی ضعیف و مطلوبِ خودشان سر کار بیاید؛ کسانی که کاری به کارشان نداشته باشند و بگذارند به سلاح هسته‌ای‌شان برسند
تمام خواسته‌ی آن‌ها سلاح هسته‌ای است، و اگر به آن دست یابند، کل دنیا دچار دردسری بزرگ خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71380" target="_blank">📅 22:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71379">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f6c19e60d.mp4?token=cv0ZK362s2QM0yT83-HzZiXgzGZEaNlQfvmzSEBbSmOfo3_y3v74rVi3wRf7C-TexCaZ2FY2B7XTDVmkCx7ZdzfACRxFede9vGj3oWNOpiFkxsLMkPDE9nVcKtTuhPAhosxWUO_NieoWmEL1AdvJ-NsKUjHqcyxMLjIO9OYVcwSbUddWr7uiqDxthh0c0FKQdublEYRLDzJuhmmTWH7sYxGCTLmFLdaST8yaiDwn99u9BvisfNPNG8Ykm4vElFyIXWZQNUvgMMUlf-B-RozYSgFmprNeLwrFtolu8CgULpzluptPSRD6ZJPPIJn8rtY3qQich-YfB-7NP_GmiKsBzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f6c19e60d.mp4?token=cv0ZK362s2QM0yT83-HzZiXgzGZEaNlQfvmzSEBbSmOfo3_y3v74rVi3wRf7C-TexCaZ2FY2B7XTDVmkCx7ZdzfACRxFede9vGj3oWNOpiFkxsLMkPDE9nVcKtTuhPAhosxWUO_NieoWmEL1AdvJ-NsKUjHqcyxMLjIO9OYVcwSbUddWr7uiqDxthh0c0FKQdublEYRLDzJuhmmTWH7sYxGCTLmFLdaST8yaiDwn99u9BvisfNPNG8Ykm4vElFyIXWZQNUvgMMUlf-B-RozYSgFmprNeLwrFtolu8CgULpzluptPSRD6ZJPPIJn8rtY3qQich-YfB-7NP_GmiKsBzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شاهد حملاتی در تنگه هرمز بودیم.
🇺🇸
پرزیدنت ترامپ:
خب، این حملات... این حملات کار ماست. ما 9 تا از کشتی‌هایشان را از کار انداخته‌ایم. بله، می‌توانم بگویم که این حملات از جانب ما انجام شده است. اما... و خواهید دید، خیلی بیشتر از این‌ها خواهید دید... وقتی که به آن ضربه بزنند؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71379" target="_blank">📅 22:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71378">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c27e89aeff.mp4?token=fK3xwuvt4BbjspI1YEiBPlSwNLVYAs4_vi4Vei2v00u2lE9K-geqqFhj-tJbuzmGmoo6N2sxi1gws1yBepPmS6DiaZK_VqZonQVBkezCxY_I52SV4LxylZoSlrJoFcBqwu4sa_SfW1Hc3YNOjVDH8rgJp3yygotOlKf83DmlJvNcwG7hAvvAneqmJ0Nxp_kUuqW7ZG08djb7IZ4OatYoTuFVKXGMECi9dD3r9KEqtCw818OWezgqDs_pRg17VbTSYjQlppXzINbyAfeqaO2tlaOpIIvNjDNcw7K_WNKOglLJLNKg2GwEXs4TBiqV56wWmzT2pkbGsFQ7r8HM5FMUkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c27e89aeff.mp4?token=fK3xwuvt4BbjspI1YEiBPlSwNLVYAs4_vi4Vei2v00u2lE9K-geqqFhj-tJbuzmGmoo6N2sxi1gws1yBepPmS6DiaZK_VqZonQVBkezCxY_I52SV4LxylZoSlrJoFcBqwu4sa_SfW1Hc3YNOjVDH8rgJp3yygotOlKf83DmlJvNcwG7hAvvAneqmJ0Nxp_kUuqW7ZG08djb7IZ4OatYoTuFVKXGMECi9dD3r9KEqtCw818OWezgqDs_pRg17VbTSYjQlppXzINbyAfeqaO2tlaOpIIvNjDNcw7K_WNKOglLJLNKg2GwEXs4TBiqV56wWmzT2pkbGsFQ7r8HM5FMUkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
کمی بعد، اما درست بعد از انتخابات، چون آنها دوست دارند اوضاع به این شکل باشد، اما درست بعد از انتخابات، قیمت نفت رو به کاهش خواهد گذاشت. قیمت‌ها پایین خواهد آمد و فکر می‌کنم قیمت بنزین را پایین خواهیم آورد، به زیر ۲ دلار در هر گالن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71378" target="_blank">📅 22:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71377">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/34c7f74659.mp4?token=cZWRJoHSczaHe3vpiYaAzqTMtiTZxkBPFGdM3qO1o-8Q2gEgwVceiOPHPkcOmrcN4bFBvP85SQB3FuNl_jUJx0eVfY-faGqHaKXlq2c-ej4EX8VEMdDAMrxfYo9TgRynA_uxK1WAKYxMhB7GTBaNtcCw_VnFhuSzUpZbU283mBcj03yxPWkbXt3FcU9Hh0ll39uKwXHFF2zl4DTbQ0CPJqKIK-PpBlzj2uZSyL7_v-vNTgyPB_GIQum6oN83kEWXZINq1965gegXbhGpnNPsHLGWkMvArVEAptw0i8pI1IRaC6-p5aIN4-mgzOvH0pLP163Ig427eRYkzszSTcpINA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/34c7f74659.mp4?token=cZWRJoHSczaHe3vpiYaAzqTMtiTZxkBPFGdM3qO1o-8Q2gEgwVceiOPHPkcOmrcN4bFBvP85SQB3FuNl_jUJx0eVfY-faGqHaKXlq2c-ej4EX8VEMdDAMrxfYo9TgRynA_uxK1WAKYxMhB7GTBaNtcCw_VnFhuSzUpZbU283mBcj03yxPWkbXt3FcU9Hh0ll39uKwXHFF2zl4DTbQ0CPJqKIK-PpBlzj2uZSyL7_v-vNTgyPB_GIQum6oN83kEWXZINq1965gegXbhGpnNPsHLGWkMvArVEAptw0i8pI1IRaC6-p5aIN4-mgzOvH0pLP163Ig427eRYkzszSTcpINA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه هموطن بعد از گرونی بنزین زد به سیم آخر و از بالا تا پایین مسئولین رو یکی کرد.
حاوی الفاظ رکیک، هندزفری لازم
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71377" target="_blank">📅 22:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71376">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8P5x5As7lORwRyalpjxsFZ4SVMuszXUrZsJMkGycGr6IC8739Hkm5bnUQls7U9IX2DM-Y5whLG5dB61GiIDp-D5J88AFSSlpzv5A-zlQUA1pyhvjHm7ZeD6Lqa7inzlA9ejMsTVLwOMG4aBqzq4ItamfqXmu5ho0FCe4T805T46KnjV-8sCxoluM4KbyJgQhlJJ72-Xjnp9IMzILvHUMLa1uBMeh_ilUoM7taO-tmsMD-W5WpmbNPq_WwY70E4Y7FvdZUrOSfq1Jyc3C534mnHe8XT7euUMuBKs5Fnl4jGx-qVqWoHGB-645A0hrt2vtpqdBuzjg1EHi918vr2Z9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
🇺🇸
🇺🇸
به گزارش «نیوزنیشن»، دونالد ترامپ همچنان در «بال غربی» (West Wing) حضور دارد و طبق برنامه، هنوز عازم دالاسِ تگزاس نشده است.
ترامپ در حال دریافت گزارش اطلاعاتی به همراه جی‌دی ونس (معاون رئیس‌جمهور)، پیت هگسث (وزیر دفاع) و ژنرال دن کین بوده است.
احتمال می‌رود این جلسه پیرامون موضوع ایران باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71376" target="_blank">📅 21:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71375">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22f299161.mp4?token=VBDFXdRo_iYORQ_RTHrO0lXwbVow4XOTNvPL__I3O85gb9z_7JEi2g2f6HJXKEQvZrJEXHAmh3dD4gK6DsXIRB8RNEd8kPVuj0Bw6Fv3pYsWr3MB3iLxgHvTFglb1l7R5vukSUzQg5wHKtaj3-x7KD0juoa8NSHog-WId0Bd7o7bdqvzSjLLmLJXx82XdXkOA0vqcYv3yyXjnaprbvN3TNyTgjacLVF-OG_cPGFYXhZZLNeBvc4IB3iwnperKog1u284XCvNenWI29qxn5v2u3DZVIdVhmvTD26NvL67ZPEKYNUXmoL9hVKZdcuxhT5kkIoaDoOAcjf-y7z-nm7pCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22f299161.mp4?token=VBDFXdRo_iYORQ_RTHrO0lXwbVow4XOTNvPL__I3O85gb9z_7JEi2g2f6HJXKEQvZrJEXHAmh3dD4gK6DsXIRB8RNEd8kPVuj0Bw6Fv3pYsWr3MB3iLxgHvTFglb1l7R5vukSUzQg5wHKtaj3-x7KD0juoa8NSHog-WId0Bd7o7bdqvzSjLLmLJXx82XdXkOA0vqcYv3yyXjnaprbvN3TNyTgjacLVF-OG_cPGFYXhZZLNeBvc4IB3iwnperKog1u284XCvNenWI29qxn5v2u3DZVIdVhmvTD26NvL67ZPEKYNUXmoL9hVKZdcuxhT5kkIoaDoOAcjf-y7z-nm7pCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🤡
اوستاد خوش‌چشم تحلیل‌گر ارشد صداوسیما:ما به سوی یک درگیری تمام‌عیار و کوتاه‌مدت در پاییز می‌رویم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71375" target="_blank">📅 21:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71374">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jmt8FpEHoWFNw7ufemk_MA2HjqwR3Vk5ScC2R2nhaJkFsKqmQWm_Jb8p6NoVT2XVV7cB55C7BZ8tk6f9DwVNgvD3U3JIiizWaFHGOaBC-vHnVD2RSDCHvq1e0U2gyiDHzb1E52zKEB_Q3F_L12K2haEvUa5zBjIKemG1alqmTH1E4RAnB1ZJpDHxNKxpxuwuDk_ibyEL1wPPvF_8te6_YiIxS32vS14L0PF0yKjljxyXD1zkNShJxF57UEQXwrKHG3VnGStiq41jKYzQSKZ5wqKXSvYSPNE-gpCWWGY3B11afyRUjXjtOVGTvdZmlPmbLc8ipahg7bmkaDcQOOCikw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
تصویری زیبا از رعدوبرق دیشب تهران.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71374" target="_blank">📅 20:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71373">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69c9063c46.mp4?token=iuyIWCLDWIP_1l95clrD_Q0c1YH2_qMUnTIzljskxiM5cK9A-spX-zdj2vTwV-f-eVtnfSv3XFwP13lhrNVkLol7Y6OfIygkQiAGbnubwgIpnKTqtVC1FxPvk863wyK9x6eBrrXlS3-rTdokiD8QwpWTUDfh-UyHEdD0FopHfxh1y-hHJm9hkgyoLS88F6jwceaQd3NfU_RaCHFkScMABICacUfrEfeD_aKv-fwc93zEQBogIk66zu4muLNesmB4DqEHrYnsu2E5WikFl-2O3NvPe9jAGAbTC1lqqgHPIvVF9j6tk_gyrwyioUWFtkq83bU2sL9-wcIA-kbsGKGNYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69c9063c46.mp4?token=iuyIWCLDWIP_1l95clrD_Q0c1YH2_qMUnTIzljskxiM5cK9A-spX-zdj2vTwV-f-eVtnfSv3XFwP13lhrNVkLol7Y6OfIygkQiAGbnubwgIpnKTqtVC1FxPvk863wyK9x6eBrrXlS3-rTdokiD8QwpWTUDfh-UyHEdD0FopHfxh1y-hHJm9hkgyoLS88F6jwceaQd3NfU_RaCHFkScMABICacUfrEfeD_aKv-fwc93zEQBogIk66zu4muLNesmB4DqEHrYnsu2E5WikFl-2O3NvPe9jAGAbTC1lqqgHPIvVF9j6tk_gyrwyioUWFtkq83bU2sL9-wcIA-kbsGKGNYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
⭕️
#فوری
؛شورای حکام آژانس بین‌المللی انرژی اتمی امروز، ۹ سپتامبر ۲۰۲۶، قطعنامه‌ای را تصویب کرد که بر اساس آن، موضوع هسته‌ای ایران به شورای امنیت سازمان ملل گزارش می‌شود. این نخستین ارجاع از این نوع در حدود ۲۰ سال گذشته است.
۲۳ کشور موافق قطعنامه بودند.
روسیه، چین و نیجر مخالف بودند.
۸ کشور ممتنع دادند و یک کشور رأی نداد.
🔴
قطعنامه با ابتکار آمریکا، بریتانیا، فرانسه و آلمان ارائه شد.
دلیل اصلی اقدام آژانس، عدم توانایی بازرسان در راستی‌آزمایی کامل مواد و فعالیت‌های هسته‌ای ایران و پاسخ نگرفتن درباره آثار اورانیوم کشف‌شده در برخی سایت‌های اعلام‌نشده عنوان شده است.
آژانس همچنین می‌گوید به دلیل محدودیت دسترسی، نمی‌تواند با اطمینان درباره میزان و محل ذخایر اورانیوم غنی‌شده ایران اظهار نظر کند.
⚠️
اقدام بعدی در شورای امنیت خواهد بود و هرگونه اقدام الزام‌آور جدید در آنجا با توجه به حق وتوی احتمالی روسیه و چین با موانع جدی روبه‌روست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71373" target="_blank">📅 20:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71372">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fc965eb9f.mp4?token=EYrRVtj3DjCeoDDF6DIkNkxYA_Ma5YavdbxgncOj5cOy876GXGAV0n_E59fdoEg6AyqOcCzmdVwClzgpraev-wRyYOuk5s7jCX-TPSOqlgwNo4iAEhR8-974w2vcFbflPLCGioKC_oPoW8lfHMgT4twDAjKoc5J9QYNa2ISnWHJrlAQTK8w4ezGkz_Ca-w2-WTAVfQY8IwYTbcdlh4fbRgSi7lYBZp7jOsqYcWYlTYAukR_sZpyNXbF4th2bwN7P5sPD8wukzy11V9itzTUfop2LGTmpkYAtyc0Ie10H_duSYx6b100x3MnoLWZ1XBByiVXWDnDzukpLMQKAhlmQaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fc965eb9f.mp4?token=EYrRVtj3DjCeoDDF6DIkNkxYA_Ma5YavdbxgncOj5cOy876GXGAV0n_E59fdoEg6AyqOcCzmdVwClzgpraev-wRyYOuk5s7jCX-TPSOqlgwNo4iAEhR8-974w2vcFbflPLCGioKC_oPoW8lfHMgT4twDAjKoc5J9QYNa2ISnWHJrlAQTK8w4ezGkz_Ca-w2-WTAVfQY8IwYTbcdlh4fbRgSi7lYBZp7jOsqYcWYlTYAukR_sZpyNXbF4th2bwN7P5sPD8wukzy11V9itzTUfop2LGTmpkYAtyc0Ie10H_duSYx6b100x3MnoLWZ1XBByiVXWDnDzukpLMQKAhlmQaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇦
🇾🇪
ساعاتی پیش، چندین حمله هوایی عربستان سعودی در حمایت از عملیات «شورای رهبری ریاست‌جمهوری» (PLC)، مواضع حوثی‌ها (انصارالله) را در جبهه مأرب یمن هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71372" target="_blank">📅 19:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71371">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71371" target="_blank">📅 19:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71370">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4ebfee62.mp4?token=sQ-kB8zsbUe9O5OL4U0NNApGJ-fy3U5rO-z8IDIF-cHCxvOpW-F84FkBaxK3aXt7P86ZPOgdg7DhEy8WdtYb1VJeyKfn3zLDoFCXZ2eiZMqlkQPbOc-34QMv3wkcfMYdSoRGBsI0GSYiNg5V1jqPAVnYyEcesSm_q-STvKyRlBja8vvGG3pUUuXo5y1BjghrEARiG1_behb6IGTIwyqh_Bfrl8txnNIp7ZDMDLFP1NLisjwW-JP_ZpjkVeZ9KcCZ0nYFn9cdSRS8Y1c0sFbmzItfDPpLE-NKjT0LFuYHVJKPLrd-hUS3VeLrzXqE1n5H_NB7Jgv70ilJK3nHDtxPgqRgEQSu3f1l6HepJ7uq20dDHoB4BIZB7clf6n8G0tG1Jj3wjgnPxOLufY9_3fOBhTf0U3hGa5JkJ8QDg0xmmSRuAwIpWpoIZ4XW8UIwnDVD7K6TcQ53FMXvK1PyppNmRNCr2C3KXH_ukBSfPCDgnN41w16Rk_ZKqH5zWPj-WuOSkqkRslrs0fwf8lUcAG8AR5pyrR39qeRdvJ01M5XGOPrOLsTFmTgMY2K99E7G1lPqFFGfElqgxIcfEH8SIWt3IYtokXdsvdN6gMv228zZDqUItOPSgwXl8C9Twrb8-E89pD_5bu_4Fn5Qs3K0a6slh-Mt0ff1Pvrnlh66Ey1mKJE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4ebfee62.mp4?token=sQ-kB8zsbUe9O5OL4U0NNApGJ-fy3U5rO-z8IDIF-cHCxvOpW-F84FkBaxK3aXt7P86ZPOgdg7DhEy8WdtYb1VJeyKfn3zLDoFCXZ2eiZMqlkQPbOc-34QMv3wkcfMYdSoRGBsI0GSYiNg5V1jqPAVnYyEcesSm_q-STvKyRlBja8vvGG3pUUuXo5y1BjghrEARiG1_behb6IGTIwyqh_Bfrl8txnNIp7ZDMDLFP1NLisjwW-JP_ZpjkVeZ9KcCZ0nYFn9cdSRS8Y1c0sFbmzItfDPpLE-NKjT0LFuYHVJKPLrd-hUS3VeLrzXqE1n5H_NB7Jgv70ilJK3nHDtxPgqRgEQSu3f1l6HepJ7uq20dDHoB4BIZB7clf6n8G0tG1Jj3wjgnPxOLufY9_3fOBhTf0U3hGa5JkJ8QDg0xmmSRuAwIpWpoIZ4XW8UIwnDVD7K6TcQ53FMXvK1PyppNmRNCr2C3KXH_ukBSfPCDgnN41w16Rk_ZKqH5zWPj-WuOSkqkRslrs0fwf8lUcAG8AR5pyrR39qeRdvJ01M5XGOPrOLsTFmTgMY2K99E7G1lPqFFGfElqgxIcfEH8SIWt3IYtokXdsvdN6gMv228zZDqUItOPSgwXl8C9Twrb8-E89pD_5bu_4Fn5Qs3K0a6slh-Mt0ff1Pvrnlh66Ey1mKJE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پسر‌بچه ارومیه‌ای که چند وقته به شدت ویدیو هاش وایرال میشه موزیک جدید داده بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71370" target="_blank">📅 19:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71369">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696aa56e23.mp4?token=dXE6odFJdYUBkSVj9uas1oBfkqZkExFKs_vwYAmfMoECvj8Uj9zfiZkRc8tf-uPxIj-nSdNFwpk7ZOJG7vE88Nv2qZfsVDvxyuS5pB-oTcb6UoDS9BH4PzeVo5PA2y9-Twzvzt2BXJy2gF3wy2rTVTd6OG62wxNZiAQ_cdrQAeIiuf60U3BYubpIZgAcL4menFftIKX8IWzch1YbLZ6RLsodxq1h7K8tlunswpcUpf9jm2NIAnWapHaWR9LuDH-6KC-IeUXV-QgQKN33fRqnvdFdU7E-BLgscg2B3b8V8Fxgk9haQBq5I7dPfkXiSnygCslWv5ZR5aIZK4HsEyYulw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696aa56e23.mp4?token=dXE6odFJdYUBkSVj9uas1oBfkqZkExFKs_vwYAmfMoECvj8Uj9zfiZkRc8tf-uPxIj-nSdNFwpk7ZOJG7vE88Nv2qZfsVDvxyuS5pB-oTcb6UoDS9BH4PzeVo5PA2y9-Twzvzt2BXJy2gF3wy2rTVTd6OG62wxNZiAQ_cdrQAeIiuf60U3BYubpIZgAcL4menFftIKX8IWzch1YbLZ6RLsodxq1h7K8tlunswpcUpf9jm2NIAnWapHaWR9LuDH-6KC-IeUXV-QgQKN33fRqnvdFdU7E-BLgscg2B3b8V8Fxgk9haQBq5I7dPfkXiSnygCslWv5ZR5aIZK4HsEyYulw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز تو بجنورد، فردی که سال‌ها با معلولیت شدید تو یکی از خیابون‌های شهر دیده می‌شد و مردم هر روز بهش کمک می‌کردن؛
به محض دیدن پلیس کامل درمان شد و درلحظه به‌طور کامل کاملاً شفا گرفت.
طبق گزارشات این فرد روزانه چیزی بیش از 20 میلیون‌تومان درآمد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71369" target="_blank">📅 18:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71368">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8d769b56.mp4?token=Z0um93OSBikt8Se_5LdHxvY4oVVjNkFsDyg6az0Y3uc2M2JcUQVBj00iKNwnA7Q7sxnqowsWZnXPOXn3Lki2S4kx-wU6hZiEW2d8i8XD0BLGK4DSJyRhEYa85MwnwJRQwQ4YDSt-ElDFkDRQi43XjoNvSZS39bEsntyuY08gMx6bWC4pmGoRi3KS3oXWSGOtT8zH_nppRmHQ4WBOjiAqVEItakM1qQV6rrq0dRJPGTamn5v_buIwJ-fMX4EfiuQ7yYjO0Yu1rR4Aq7Jm3WGO5UswnEU5UAL1jc3teAhK452KOmMv76cywkhOSboZBbsIw8aJdBJQ6K3TtSvpj_OtMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8d769b56.mp4?token=Z0um93OSBikt8Se_5LdHxvY4oVVjNkFsDyg6az0Y3uc2M2JcUQVBj00iKNwnA7Q7sxnqowsWZnXPOXn3Lki2S4kx-wU6hZiEW2d8i8XD0BLGK4DSJyRhEYa85MwnwJRQwQ4YDSt-ElDFkDRQi43XjoNvSZS39bEsntyuY08gMx6bWC4pmGoRi3KS3oXWSGOtT8zH_nppRmHQ4WBOjiAqVEItakM1qQV6rrq0dRJPGTamn5v_buIwJ-fMX4EfiuQ7yYjO0Yu1rR4Aq7Jm3WGO5UswnEU5UAL1jc3teAhK452KOmMv76cywkhOSboZBbsIw8aJdBJQ6K3TtSvpj_OtMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بازی مناسب برای جوانان خاورمیانه ای:
یه سایته یه بازی ساخته، میری توش بمب اتم مورد علاقت رو انتخاب میکنی و میزنیش تو شهر مد نظرت و بعد بهت میگه چند نفر رو کشتی
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71368" target="_blank">📅 17:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71367">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDEVo7J9mMMRmTuZ6ubRUSiZHS9_ClPGO3T_30jsZSDqIcXhIJJ5CGt-eoSrypWlzJXhlRE6_xlx_6BC7DrENqSt1WHcFxLolNnox2eR3xW8CMJVyDj50wnJr4ZKRKB-zIsuLpCy-Cl8SYqH05M8wvlcOOolb9RkurxPBxzGfpsCNNf8tMFh111Pg8Z1WI-y9BkMioVi2lQ4yzJg7EV3dIELVibJl991nBLyUqsYv6N3iQjahtbIn1n6YIc37TOpY9justD1hMWPFC-53qJcjXFivrlNji8N-w6b_Qa3zOC6jbfCfPznUmTquHx2buYmRbu8Xmi8f-LQwUdoNOC_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇺🇸
📰
سی‌ان‌ان:ایران به سرعت در حال ساخت یک تأسیسات هسته‌ای مشکوک است که در اعماق کوه گرانیتی نزدیک نطنز - ملقب به "کوه کلنگ" - دفن شده است و تصاویر ماهواره‌ای افزایش ساخت و ساز در سال 2026 را نشان می‌دهد.
این سایت احتمالاً برای محافظت از سانتریفیوژها یا کارهای غنی‌سازی فراتر از دسترس بمب‌های سنگرشکن فعلی ایالات متحده طراحی شده است.
ترامپ تهدید کرده است که به آن حمله خواهد کرد ("ما ممکن است خیلی زود کلنگ را بزنیم")، اما بزرگترین بمب غیرهسته‌ای پنتاگون ممکن است به اندازه کافی عمیق نفوذ نکند.
نشانه‌ها نشان می‌دهد که ایالات متحده در حال حاضر روی این مشکل کار می‌کند: یک روز قبل از شروع جنگ، یک آژانس سلاح‌های کشتار جمعی پنتاگون قراردادی اضطراری برای تعمیر یک تأسیسات آزمایشی زیرزمینی که در گرانیت در وایت سندز حک شده بود - مرتبط با شبیه‌سازی حملات به عمیق‌ترین پناهگاه‌های ایران - امضا کرد.
یک بمب "نسل بعدی نفوذگر" در حال توسعه نمونه اولیه است.
تحلیلگران CSIS می‌گویند کلنگ هنوز عملیاتی نشده است، اما ساخت و ساز از حفاری به ساخت و ساز داخلی و سخت شدن تغییر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71367" target="_blank">📅 17:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71366">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6e3b3343.mp4?token=jUdDB8XJ6_BeRv26KTw_i2r3CS4rfgyMjWfrysVH8JTjTPUMpKs6VcrGsbrAyjQiwy7iznLf7ZQn8aMIwbS-xlgs-bxb2A9D3EAEb-fFcRIF0yEUL2PdvHhosvBFvwWwHqh7ByAsFW58ul9dJsi3Azyelyy_AoFQFo0TUNGqoq19ewiKrfbmwqPrFfp-XceTc_WiL7C0kzJoBTe3rV_9oUBbzgHSWXPCpPKlgtcl6f_myAw813UaghPWcsaUpxry9EH9JhgmF_tbfF3-4SYX-iwh_uxZ0xi9YJBfsKV39cc0dK4iFEqXxET1pmZ4PN8oaCL12nxDYTLsuZLUnNT03A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6e3b3343.mp4?token=jUdDB8XJ6_BeRv26KTw_i2r3CS4rfgyMjWfrysVH8JTjTPUMpKs6VcrGsbrAyjQiwy7iznLf7ZQn8aMIwbS-xlgs-bxb2A9D3EAEb-fFcRIF0yEUL2PdvHhosvBFvwWwHqh7ByAsFW58ul9dJsi3Azyelyy_AoFQFo0TUNGqoq19ewiKrfbmwqPrFfp-XceTc_WiL7C0kzJoBTe3rV_9oUBbzgHSWXPCpPKlgtcl6f_myAw813UaghPWcsaUpxry9EH9JhgmF_tbfF3-4SYX-iwh_uxZ0xi9YJBfsKV39cc0dK4iFEqXxET1pmZ4PN8oaCL12nxDYTLsuZLUnNT03A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر مسی رو پیدا کرده بهش میگه بگو علی تولدت مبارک
😔
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71366" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71365">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71365" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71365" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71364">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjosYkH8G1Xq84LUABy2uZCxrrS790dEDhguaAsiRULwC7iOp_7QNMtebxY4IGcFilrt4KSoYBFngHUX38np45Oqtk-Tc6kzSBaIMWJiLolyLOYHUte2AHtXnHZOyzVeUUAo0dPmBgF5qhr-qTm-c0lcCK-qHdHGSt0tSj3_-J63RkBxggjA-m0aVUHFvvnKBQT69pr8MFOCiwn7zra32CQrWi0e1teGIg5jSXBjozDOzaS3BuAY1XZOad-sGjva_G30E1zdXgR8KCzN5Ixt9K8ypETfu7JqMo4eGaGqbFJXo3bZ9L4m2yLbKmHFX5oevIbWZ_X5uAPfQ-zBSjhvIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آرسنال
🆚
ناپولی
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در ۵ تقابل اخیر:
⚽️
آرسنال: ۵ بازی ۳ برد، ۱ تساوی، ۱ شکست و ۷ گل زده
⚽️
ناپولی: ۵ بازی ۱ برد، ۱ تساوی، ۳ شکست و ۴ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71364" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71363">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146bbc1159.mp4?token=pSmYVPvejs6fSw7CayEPSGMQSArSv_a00gvxUu7v2PCWUQoDE95IQTiORDn0byuKo7jrhQnntCJ5JJ5PwR42yPGCWa9uF1lPgg4O0uFb4bcfhWnzaGVPYrjX42q66XJG-1xjLuuFP0JEVkFckSxC4tZlD1frq75l7zr5d9sFbsDJ3LZl426IkVdHMsZ6SZwDtvdboF93Unh1aPhPLLDafs3hKyJcPcUU6HwhvWbN6E7IoU_nYsRHE_nvrS4Liijl4zMxOEdpc6qDtZz_1kvKIMZBt6m995T5KvtXkl0Udf_uED2IbBm9BxQJIUcfA-RZMwXW6NnrFquYCT9fn9c75Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146bbc1159.mp4?token=pSmYVPvejs6fSw7CayEPSGMQSArSv_a00gvxUu7v2PCWUQoDE95IQTiORDn0byuKo7jrhQnntCJ5JJ5PwR42yPGCWa9uF1lPgg4O0uFb4bcfhWnzaGVPYrjX42q66XJG-1xjLuuFP0JEVkFckSxC4tZlD1frq75l7zr5d9sFbsDJ3LZl426IkVdHMsZ6SZwDtvdboF93Unh1aPhPLLDafs3hKyJcPcUU6HwhvWbN6E7IoU_nYsRHE_nvrS4Liijl4zMxOEdpc6qDtZz_1kvKIMZBt6m995T5KvtXkl0Udf_uED2IbBm9BxQJIUcfA-RZMwXW6NnrFquYCT9fn9c75Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
دیروز تو سمنان عرزشیا برای مجتبی خامنه‌ای جشن تولد گرفتن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71363" target="_blank">📅 16:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71362">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ece16841.mp4?token=kAeCXQiZ6JEnGXYYoK_mob9G9l1Sat4GNWsOWlCPAh_UU8PswtF4RUpn5jxmYSECpHSZEGD16kVTFbbiqkc9lT6ISJ0dPs2WP9ir3m8TH4mVrp7B-prHLeHA0GAKLUwLd16KaHNQRq6767Q_BUJj6dRRIOYYSWT4Kq3hsu5_dsqAKgDYixbsSnAcno4GKGdjmL_ssJTPGKYKztZXCYPnT_aulfQwHKUmaPbkV88E5mGUuYRoxtM3hRM7m_-KZjsuRdFF0gwddfEmaFRzo3pi8RJqSLqp6UlmydMqi81EawXkSd0hV9Cvb89QHSduPKUKljywN33Rbezvz4h_NNZU5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ece16841.mp4?token=kAeCXQiZ6JEnGXYYoK_mob9G9l1Sat4GNWsOWlCPAh_UU8PswtF4RUpn5jxmYSECpHSZEGD16kVTFbbiqkc9lT6ISJ0dPs2WP9ir3m8TH4mVrp7B-prHLeHA0GAKLUwLd16KaHNQRq6767Q_BUJj6dRRIOYYSWT4Kq3hsu5_dsqAKgDYixbsSnAcno4GKGdjmL_ssJTPGKYKztZXCYPnT_aulfQwHKUmaPbkV88E5mGUuYRoxtM3hRM7m_-KZjsuRdFF0gwddfEmaFRzo3pi8RJqSLqp6UlmydMqi81EawXkSd0hV9Cvb89QHSduPKUKljywN33Rbezvz4h_NNZU5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مراد ویسی:
جمهوری‌اسلامی سربه‌سر اسرائیل نمی‌ذاره، چون می‌دونه اونا نمیان "نفت‌کش" بزنن.
اونا میان "نعش‌کش" راه می‌ندازن
.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71362" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71360">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2Y3plP9TaJdvVEyHHkPrvhGARfVgBDZQS8fq_btU74bhpRyRwsb0GgWrGyrajEAeVLgAsnGFxvea1Rm6DNrRPTYd5wkpRmFUtnhmnyaWPrvo8Ligh0MgZE7qm0yD5ywyYufNMVOY_YJnPNTaR_M9W8KKpysJF5jmDHqHKLNestckLhfRgEsIGRl-_GdMUbfzOkLzg1wUE7SsXZk_knR3H6zB9uP2GxjQMLuNIbI9r7Rx_V3GlkNQQPHO6BoTHeY_ZybS-7WcNYm1kzm_vr8adhv7YptehEjGW8VCZjUZ7CZCFpezBgqfc-4c2tm0-hTNl-FLFrt_kwkPijm3foczQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f399e219.mp4?token=c__-SeRa_Ar5Di_8itrjh6NXuSDo-4qi1Br_ErowTDrTQEP0OHcIsJCF_hiv0waCWCIluyxk2saVwRzF9o3SRbUTJcidh7q3hL1M0Tb7m9Df3csGW_WUBjagRkK3zvL2JWuRlEHRuWFccbmYyGDTk2asXbZhQjjlzUrqL82gHfAP7r8OLZihiNGjv8yeFhvgPZgw-WjOLsVFMyfMRniDZoKWSTTwBcYh4qDvPhmhByI4R0ZnMiCOkZ8kXVdAqWM5nGdu_j_XgzJI04dt-FBFkdTE0CgCAZIeWy7bRztlqBVbhFVn3uwottiWfoaZ2nztSMYQ2U3RheS4yUvchRav_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f399e219.mp4?token=c__-SeRa_Ar5Di_8itrjh6NXuSDo-4qi1Br_ErowTDrTQEP0OHcIsJCF_hiv0waCWCIluyxk2saVwRzF9o3SRbUTJcidh7q3hL1M0Tb7m9Df3csGW_WUBjagRkK3zvL2JWuRlEHRuWFccbmYyGDTk2asXbZhQjjlzUrqL82gHfAP7r8OLZihiNGjv8yeFhvgPZgw-WjOLsVFMyfMRniDZoKWSTTwBcYh4qDvPhmhByI4R0ZnMiCOkZ8kXVdAqWM5nGdu_j_XgzJI04dt-FBFkdTE0CgCAZIeWy7bRztlqBVbhFVn3uwottiWfoaZ2nztSMYQ2U3RheS4yUvchRav_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⛈
⚡️
ویدیویی که یک هموطن ساکن مازندران از وضعیت چند شب پیش آسمون مازندران منتشر کرده و نوشته؛
تو تاریخ مازندران چنین رعدوبرقی که بی‌وقفه ۳ساعت بزنه نداشتیم
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71360" target="_blank">📅 15:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71359">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rka_vpbUnDngKtSYa41ShCtODap6t-amYxsnQ1Lggzg0RmLdp7lIhNLK9hoWro5MFL2HW8xKhR70QDM6zd29vgK7rqg5kjdDzxp3B3Sx8ACZ_XtxEMkMbNvsIutEexCF9SQlwDm4oOnsKfURjdXfnouFZ6FbLWvR1eWF4EA5mmg_sb7CX614HZ0sdNnomIBPW1pYpG2lIto7Zqt4ORdX1iQW1QdM_mofosCz5MLAtS9g5ql3_J66MsCkrvO-cHF-8efTuSq6sk_4NOi5Fb8vthh89yTJctiI3mLvEhAsDocJmjuMkYB5Mfnwp1oLTnpk9Ny0JTKj-zv3jv_fzgiTww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
🇺🇸
#فوری
؛سخنگوی سپاه پاسداران شروط جدیدی را برای پایان دادن به جنگ مطرح کرد؛
🔴
اگر دشمن خواهان پایان این وضعیت است؛
۱_ضمن توقف کامل جنگ، از تهدید مجدد دست بکشد
۲_ارتش رژیم صهیونیستی از لبنان عقب‌نشینی کند
۳_محاصرهٔ یمن پایان یابد
۴_۲۴ میلیارد دلار دارایی مسدودشدهٔ ایران آزاد شود
۵_از هرگونه مداخله در توان هسته‌ای و موشکی کشور دست بردارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71359" target="_blank">📅 15:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71358">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf337ab4f7.mp4?token=YxU0gSEThlJtnRG3gyVB3-WNSumYiDALqydgR7fuhsEzspdTu_OVZbGplDXxSAhnAb9u7TUz02ttXNdIQNNaRnGwDbF9biomzPgXmXa9gPoDqSKkMuwmQe1cBReCSy1w9V5D3sIcvmuEJA8LNTqCnQ2DG8GMdUqNgEe7oXQuLOa1BrR264Wzy5a9FPsmBOb6740_7nbAmHaPQH-TXambiCP6nIjS9qgu5DWlP-MufBk84IUC_JyRofyhION1lUd1N9_R0RPW-T2m3JRJdoJvHQBOIbWJNLx4aYiEiPfMLsEI0zGXRgPHjXdxExJFt4yLtzN9j-uwmPvntnprQ-_kMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf337ab4f7.mp4?token=YxU0gSEThlJtnRG3gyVB3-WNSumYiDALqydgR7fuhsEzspdTu_OVZbGplDXxSAhnAb9u7TUz02ttXNdIQNNaRnGwDbF9biomzPgXmXa9gPoDqSKkMuwmQe1cBReCSy1w9V5D3sIcvmuEJA8LNTqCnQ2DG8GMdUqNgEe7oXQuLOa1BrR264Wzy5a9FPsmBOb6740_7nbAmHaPQH-TXambiCP6nIjS9qgu5DWlP-MufBk84IUC_JyRofyhION1lUd1N9_R0RPW-T2m3JRJdoJvHQBOIbWJNLx4aYiEiPfMLsEI0zGXRgPHjXdxExJFt4yLtzN9j-uwmPvntnprQ-_kMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
📰
یک فایل صوتی که اختصاصی به ایران اینترنشنال رسیده است، نشان می‌دهد یک هواپیمای نظامی آمریکا در مکالمات رادیویی به نفتکش جمهوری اسلامی هشدار داده به‌دلیل «رعایت نکردن محاصره نظامی» در بنادر و سواحل ایران، موتورخانه آن را هدف می‌گیرد و خدمه باید در ۱۰ دقیقه موتورخانه را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71358" target="_blank">📅 14:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71357">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Re2ogj7luh6f6ps2sdWdk5XxbJLKRa-6cEKL8bGkyUC5Ir1QjcO4glXhMJDKp6b2srQXC7WTlmZVx4wGsxIlS29Yfh126PKEyPf-L4XDY_0h4ujXKocijQIM2JWkWXqurdnoAfa2NSko64qE0ki5XkZMIyQqU4hOhrLFSRisO7Xy_zPz6kiz5Yxm1bbqpEvMpkiEsA0_c56iXb7bJFHPA-wHIa4ENEMfxJfO_AtR4CMb7sCnrgrchDPf2n5n7TKYxdfz7MkSepwBPlfbv0oxgNrlbl9PlqoVYfhYRYdtqEUor4sxVEadGJPkyLdlXgtqD0wt1-ckN56-Ios0b2MG8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارشی مبنی بر وقوع حادثه‌ای در ۲۸ مایل دریایی جنوب شرقی «الفاو» در عراق دریافت کرد.
فرمانده یک نفتکش گزارش داد که این شناور مورد اصابت پرتابه‌ای با منشأ نامعلوم قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71357" target="_blank">📅 14:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71356">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuWsYFZ4g5MBRTGiJq_z9FJtSBgeUwObXqWx3Uc0KzhWnQ-A8KyiUOo72EjO01GoZb-DmH8O6FHhvqTJKAFDvGlAS7q6w8WivmPgsHt7PKm6smPolpPQZsInIi4MVhGKjui6hfj84JQ9X4cig_lPxeeJJ9vWs-Z7lFvS5p2PmvcqQpkMSl2KJR5xFO5wbumfIx5K2pBfUMwrjN88_fm-Uxr1XsF-tI1LQ4__Xz4Q0eu754VfAJgkUTVRO2PeAFS0gDsuUjH6uQvu0YeIhGqDSHbDLUAWGCDsBnGCulL7xmpOsm9kovk3c2ltYftfXJBRaoW60rPJpAx3Cag6TJ2AtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💸
🫵
دقایقی پیش دلار و تتر به شکل عجیبی تا 241,000 تومن بالا رفت و دوباره برگشت و الان 234,000 تومن هستش...
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71356" target="_blank">📅 13:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71355">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLiz-nbbFKYjl4-6vitwjOsGC04W8fbM7l1VApmgD1knfqpNHtzYJICiVAXOkld8svbcvg9KyI4PawJXb6E7BKcA7gBZGTaXR61lL5HPe9IyNt6it-SSvggNeWS8TU3FCX0w9OTDiUg7hMr8VXITlAIKeNxmREVpF1-6Xmk9nbzekNnMOkmZAGIhfTzBweg5IP3VJqIEwChWZyRYtHRdl3UOwPFKOh14Wa9SdBIlj8rRfbiSI0fWZioqIfjXxkYdjOxAt2G-UEJZt6ki0oyQ7_CARMj6uLSjzhBeS854BrTGR3sgH5DlwfmRUyyQwsAQVqfYgocpMxbwg2gYYtv37Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
〰️
فرماندهی مرکزی ایالات متحده:
❌
ادعا: نیروهای سپاه پاسداران انقلاب اسلامی ایران (IRGC) مدعی شده‌اند که به دو ناوشکن نیروی دریایی ایالات متحده در خاورمیانه حمله کرده‌اند. این ادعا کاملاً نادرست است.
✔️
واقعیت: هیچ‌یک از شناورهای جنگی نیروی دریایی ایالات متحده مورد اصابت قرار نگرفته‌اند؛ تمام تلاش‌های سپاه برای انجام حمله با شکست مواجه شده است.
در همین حال، نیروهای آمریکایی تنها در هفته گذشته موفق به انهدام ۱۰ نفتکش ایرانی شده‌اند. این شناورها بخشی از یک شبکه پنهانِ چند میلیارد دلاری بودند که بودجه سپاه را تأمین می‌کند و ایران قادر به محافظت از آن‌ها نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71355" target="_blank">📅 13:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71354">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf3721b8d8.mp4?token=GybsYJyN5Fba0__WP5jYamFG-SAOnzcolSIh1-tTOKxUmD-6pFNpoJql6nRZ7_4tlv-pMGmbWTIlvegdcCwCN6JLlPry1YKRhN8X9NC-ZbNQjkXndEvk3noASEo04nvMNIsSZUOZPmrcD-eDTB5zQTUPGRjZPeF8jBxc8jFhGNep4wnYsYS1LwQHgFyPTe6BDXYpNI4xcasGKOHO0siVHEZoVTp633YntabFZDuuHPNMUgiBggOkJox0L1Q-Suyg1iWMhn9SXyPQSLug7H_Jz0tCQPWv3HcLzSTb97vCI-H9g_Z1QudKXO1nzJel7ie_PDJ6QTy7CtW3KcL3SPbxZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf3721b8d8.mp4?token=GybsYJyN5Fba0__WP5jYamFG-SAOnzcolSIh1-tTOKxUmD-6pFNpoJql6nRZ7_4tlv-pMGmbWTIlvegdcCwCN6JLlPry1YKRhN8X9NC-ZbNQjkXndEvk3noASEo04nvMNIsSZUOZPmrcD-eDTB5zQTUPGRjZPeF8jBxc8jFhGNep4wnYsYS1LwQHgFyPTe6BDXYpNI4xcasGKOHO0siVHEZoVTp633YntabFZDuuHPNMUgiBggOkJox0L1Q-Suyg1iWMhn9SXyPQSLug7H_Jz0tCQPWv3HcLzSTb97vCI-H9g_Z1QudKXO1nzJel7ie_PDJ6QTy7CtW3KcL3SPbxZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
پرسنل نظامی جمهوری اسلامی:
رفتم یه شونه تخم‌مرغ رو گرفتم با یک کیلو میوه شده یه میلیون تومن. حالا نمی‌دونم بیست‌وشش و خورده‌ای هم دریافتیمه.
مثلاً بیست هفت هشت تومن سر ماه به ماه میدن به ما. مردم چکار کنن؟ خب دیگه یارو میاد بیرون حق داره اعتراض کنه دیگه. به جز این که اصلاً راهی نیست. بعد هزاری انگ هم می‌چسبونن که آقا یارو تروریسته، فلانه، بسانه.
مرد حسابی مردم گرسنه‌اند. خودتو زدی به اون راه. من با این لباس دیگه قشنگ با این لباس نیروی انتظامی ناراضیم. وای به حال مردم. یعنی قشنگ میری بیرون خشم و نفرتو تو چهره مردم می‌بینی.
می‌خوان جرت بدن منتها نمیتونن. یعنی همین الان میری بیرون اصن یه جوری‌ان نگاه نفرت‌انگیزشون نسبت به این لباس قشنگ معلومه.
حالا یه عده خودشونو به خواب خیال زدن. بابا دیگه خجالت بکشین. بی‌شرفی یه حدی داره. مثلاً انقدر. شما دیگه رسیدین به اون سقف. یه کم خجالت بکشین. یعنی اصلاً من نیروی ناراضی‌ام. وای به حال مردم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71354" target="_blank">📅 13:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71353">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMVDR9hGSO8Bx-_MCGgKOF0oov_KkoXgh5W9oyvB-h_18gqZUFWE333B-QOJmRMO-7bB35Mv2SW_E17wupf-f0EmQ362m3fYJR9N44Xq88iEDeFDMLTIxQNDmfVjp9DpW68Y_LpfNuUz6-20oqlwRH5bGJXo924TwP1Ans3WdTYdAYF8msCGa0xr8zaf4Tvu-ZNmBeKVFajzCh5y6qeI2bglXQXgGBnOofkTXrdTN1KrEw0ChdE411Z9EdEXT0vDWHsJm5OrbihegQSXWu1BqBWF76mJo_9zct0FyCNJ-wk-8Wn3LmR3fBGhtKGEVOCkhkMKf1nH9x4IKploMYQ3Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارشی از یک طرف ثالث درباره وقوع حادثه‌ای در فاصله ۲۴ مایل دریایی شمال غربی بندر راشد در امارات متحده عربی دریافت کرده است.
فرمانده یک نفتکش گزارش داده است که شناوری را در وضعیت مایل (کج‌شدگی) در حالت لنگر‌اندازی مشاهده کرده است؛ وضعیتی که احتمالاً نشان‌دهنده ورود آب به داخل شناور در پی اصابت پرتابه‌ای ناشناس است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71353" target="_blank">📅 13:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71352">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71352" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71352" target="_blank">📅 13:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71351">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPf2p5tpO7Rzs4x7y-jGI5Ft8BO2ybghSm61nFDrOyW1zVDOqz7oXGUbtkrUBulFcf-R1m05mpvpdCzSyxvLnBtyCzmjC2axEgqO-6x-prtF6Ph4HsL2I1YtziyAPoIwXpkvItu2rKzyMilzruE0s_xc_wHNqm4Ec2BvIPzMi9EwGAzGON2T2T-0Wcjjz2TK68nkhPQDnnndBSd1vygphd-xYAn1s4gLWwRjPuddRzp8JlRTZvr707-avsPrCfq35ZSzkLx1nA-rFsvFx4--7yceXlxFQFVAmyy6tjtRGe1338k_Tm0ivf1STx3ChKN2Z7MNN8a5lymkO92WZJZKfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
اتلتیکو مادرید
🆚
لیورپول
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در تقابل‌های اخیر:
⚽️
اتلتیکو مادرید: ۵ بازی، ۲ برد و ۳ شکست، ۸ گل زده
⚽️
لیورپول:  ۵ بازی، ۳ برد و ۲ شکست، ۱۰ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71351" target="_blank">📅 13:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71350">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbWtk4unUABPti_ngttjnMXB0K_iFjjRbhZuSTMXOoPkuzo6cIdM41YYSHHXe2EAP0YBGDgBoXY6zNzVtBlx9lT2T5hwzYz1Xekb22f_ntqdhaKDIoDdA7gigkoJoHy6WXeTUutJv0DlQjXPBbjUb1QTu1vyMVvpnZssG9xKRzwPmPz2ypPm2l-CH7X-MajSIqE8xbSlutvJAP62QUAJgdYMOGLsVTiLhUjykWauRq2G7beWKBJ3fosK77olFDEXuJv9PMObTFhO68ZW13vIKZKqrpopTLirj5HVE-UeQ6ywdijhs3ohrTtlFnnN6efT74UykdwpFmU6tugkVewqVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📈
قیمت نفت خام برنت برای نخستین بار از ماه ژوئیه، به بالای ۱۰۰ دلار در هر بشکه جهش کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71350" target="_blank">📅 12:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71348">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9kqwHDotsvMtRd4PJngFVKbkySa9GE9u7VseuB29SgWfHwjrVWJ1JR2vkF6nien0Rl5gLtWYgkPgD6kHU9Fm4DlxxHOwFbhLtQGB9z0eKZHBBH0gIkBDItHBDIAITrpM2bTMdr1OqUYCubZly7QMptCxdmRxbWziizHJjRyjgXegltHs4myLHeyAHc6o8NJBYLAks2bjffUePnDxbhdwZDWsNaGzUjv4vQTrD95Jk56GXTPxjS3IeJoYSCLmVM7Askdo3vZv-_JOZdFpIsmF3KwQ34XqDkwWX1b5ux9OlpHJjYuw44vsMhkHL5nofrNxRLHtZ9XWDeaLRyV_AWR_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c11c683d6.mp4?token=JRW05S9wuKpKlzu6xrne8eR-IBqKvM5TilS9ehDfpj3pQDqkObbu_dMIp640crFwRofduhmlZGH7M6zHSwDUYl6kq1LtCVNxx7bYRFQgwsgdpeKcdOwS-gfClCWHZXFetgrynzCQwsPiTDLM_1GvA2gty6YUqDgBLLEzLqXqTt9QOgCR_i6jYNlq7GZ1ximldisRJLn4dH_wflRSXj8ZZIeN7T8SlXptFuBEsq7WIV928c-W0ta-u_u_f9kQEPFIB4iWqKs7S15p-D0E6kafALsdb3j9laznRZrUCkTRpbc50uPhcz6WQxVaonGFCCZ1vQBoW0dYYDGrj1U7TmRq6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c11c683d6.mp4?token=JRW05S9wuKpKlzu6xrne8eR-IBqKvM5TilS9ehDfpj3pQDqkObbu_dMIp640crFwRofduhmlZGH7M6zHSwDUYl6kq1LtCVNxx7bYRFQgwsgdpeKcdOwS-gfClCWHZXFetgrynzCQwsPiTDLM_1GvA2gty6YUqDgBLLEzLqXqTt9QOgCR_i6jYNlq7GZ1ximldisRJLn4dH_wflRSXj8ZZIeN7T8SlXptFuBEsq7WIV928c-W0ta-u_u_f9kQEPFIB4iWqKs7S15p-D0E6kafALsdb3j9laznRZrUCkTRpbc50uPhcz6WQxVaonGFCCZ1vQBoW0dYYDGrj1U7TmRq6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این دختر یکی از پشم ریزون ترین خودکشی هارو داشته:
دو روز پیش "پایال دِوی" داشت اولین فتوشاتشو برای یک مجله تو حرفه‌ی مدلینگش انجام میداد که یهو وسط عکس برداری تصمیم میگیره بی دلیل خودش رو تو رودخونه پرت کنه.
ویدیوش خیلی عجیبه و بعضیا میگن امکان نداره این خودکشی بوده باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71348" target="_blank">📅 12:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71347">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/032667483d.mp4?token=d3Wft6MznGtZ7XG8PdaFVgohNu4Jg60ffMvPvH12vAueOVd_7WC76Njm8wyF6wLsCAfSr193NJC9-GnvrQVXhUgHpl7upEMtAiklWNKYGMmKjYi3X8oQXd-PTKp5iMHYP34qvD27vl2jvB1c29wFSiZR5eU8aXGMRyDbMM3HSNWfFPDREfwzACQkJ8VJa-mMntFAzutEFCX9fOi-eUcijNOiVpYJLIn37MGoApJZHPbXB8EfvW5oEDrEjuWVY8fZ4P9C-j3lUD7SvlfgbmqJ1A1WEgH2yFIKpPTQK-kPhAaSNKbsEiA4m0LkoL0JVpHBw5M3AhCq6vvS3l_sj7HBfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/032667483d.mp4?token=d3Wft6MznGtZ7XG8PdaFVgohNu4Jg60ffMvPvH12vAueOVd_7WC76Njm8wyF6wLsCAfSr193NJC9-GnvrQVXhUgHpl7upEMtAiklWNKYGMmKjYi3X8oQXd-PTKp5iMHYP34qvD27vl2jvB1c29wFSiZR5eU8aXGMRyDbMM3HSNWfFPDREfwzACQkJ8VJa-mMntFAzutEFCX9fOi-eUcijNOiVpYJLIn37MGoApJZHPbXB8EfvW5oEDrEjuWVY8fZ4P9C-j3lUD7SvlfgbmqJ1A1WEgH2yFIKpPTQK-kPhAaSNKbsEiA4m0LkoL0JVpHBw5M3AhCq6vvS3l_sj7HBfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گویا طبق فتوای جدید حضور نداشتن تو اجتماعات شبانه، غضب الهی رو در پی خواهد داشت و تو زندگیتون ذلت و خواری میاره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71347" target="_blank">📅 11:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71346">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDsRomdsobuHVt8i2xADENYK57iuu2FpVztG128JdpCqyc8PTNgg_ZN-twq2EspgsBlL3mboUuov27JtahdFsBdc2btV6NAN7RUSOKRnoJIe5fV9oc6Yl2v1SZVaKYqbpsHpBzlsF0RUw2xxEHnmiuqd05A9L_iS948qoFuxGSZyT8VLm0KnteUDwUnCr9_aN3QOKdlLQbB1qhwpLuWgoan4U57rOQIJFt767eeDc-aou3NN04ycAGheG4PTe0rpY_VSGKSiFdJeP0JLkg3qTLP7LH2fL5ZXIUAcMpJHSWAiIBMjXAJ1tnk7cFfIGRbH4CZkZDUMeOWgXjMB7Iv9SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
♨️
دوازده کشور با صدور بیانیه‌ای مشترک، ممنوعیت‌های ملی تجارت کالا از شهرک‌های غیرقانونی اسرائیل را اعلام کردند؛
🇫🇷
فرانسه
🇬🇧
بریتانیا
🇨🇦
کانادا
🇩🇰
دانمارک
🇪🇸
اسپانیا
🇫🇮
فنلاند
🇮🇪
ایرلند
🇮🇸
ایسلند
🇳🇴
نروژ
🇵🇱
لهستان
🇵🇹
پرتغال
🇸🇪
سوئد
مکرون، نخست وزیر بریتانیا برنهام، و نخست وزیر کانادا، کارنی، توافق کردند که وضعیت با خشونت «بی‌سابقه» شهرک‌نشینان و گسترش شهرک‌سازی رو به وخامت است و به طور خاص پروژه E1 را «غیرقابل قبول» خواندند.
آنها از اقداماتی که قبلاً توسط ایرلند، اسپانیا، هلند، نروژ و بلژیک انجام شده است، تقدیر می‌کنند.
این بیانیه از اسرائیل می‌خواهد که فوراً گسترش شهرک‌سازی را متوقف کند، شهرک‌نشینان خشونت‌طلب را پاسخگو قرار دهد و اتهامات علیه نیروهای اسرائیلی را بررسی کند.
آنها «قاطعانه با هرگونه اقدامی که منجر به الحاق سرزمین‌های فلسطینی یا آوارگی اجباری شود، مخالفند.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71346" target="_blank">📅 11:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71345">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcf294068.mp4?token=LhxYk2LziHH5gQDW4CvWPufq3_Z4SFNm82XqoFUKL-9nF39EC8gCYs6pb5b0uQSA01r1BAQWOikF9xapIXlJcnxeblYI8QfgGTyteYTUoE2-L9L-EOcFpXBjMzq08Mxyg65Yr5tcsT9CDzco0pLeIfzL0xO3aebl2qRByazzB8phZF4JsyTMfmC1SYhR5Ods2rZy58WPII19hqt4w9pPDEtcZ2CqOuCkidHblurV9rBWqN6JTNLOT7tcwOmYnetIMveE_DhAGqsXtSUFCFDxt8NjeSotKzqFVDGxLSLbFfC5uXk9kqhWXo7uhYC99-vb_-rSsz0bdYwZL3l3LAAR-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcf294068.mp4?token=LhxYk2LziHH5gQDW4CvWPufq3_Z4SFNm82XqoFUKL-9nF39EC8gCYs6pb5b0uQSA01r1BAQWOikF9xapIXlJcnxeblYI8QfgGTyteYTUoE2-L9L-EOcFpXBjMzq08Mxyg65Yr5tcsT9CDzco0pLeIfzL0xO3aebl2qRByazzB8phZF4JsyTMfmC1SYhR5Ods2rZy58WPII19hqt4w9pPDEtcZ2CqOuCkidHblurV9rBWqN6JTNLOT7tcwOmYnetIMveE_DhAGqsXtSUFCFDxt8NjeSotKzqFVDGxLSLbFfC5uXk9kqhWXo7uhYC99-vb_-rSsz0bdYwZL3l3LAAR-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
〰️
سنتکام:
کشتی «ریسکو» (M/T Riesco) در تاریخ ۸ سپتامبر در خلیج عمان غرق شد؛ این کشتی پس از تلاش سپاه پاسداران برای حمله به یک ناو جنگی نیروی دریایی ایالات متحده، توسط نیروهای سنتکام (CENTCOM) منهدم شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71345" target="_blank">📅 10:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71344">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/128e77e5cf.mp4?token=FnnE-xLoI4Zu2NIuDblDIlso2AC12kHEmo4Ee3cVKKJFp_D5QuemsK2i_Oeo95f3fxi9Q98bHi_bopjKoOa-VCpst16rlytf4IMRcCxr01cu9QPrCVJyC6hfvu-Ji6XRPyyGv8vz2ToFI2AxFYtPf27PRHQe-0RAdcIgN2N60NjulhwK2IZJM1246mcBCb1KiVPWq1idsKNchxaMDW1N_xZvpOfae3IDqL5sEsaGANKpkgqRIZbjiaug6CF_tBTeTXvJveXXRVabIe5QqXCZb6baCe_r09keVQn801sEhOnRJsZJVZMPc0UnOPHecJIjqoSTvtG3CSkotIVrbg_nJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/128e77e5cf.mp4?token=FnnE-xLoI4Zu2NIuDblDIlso2AC12kHEmo4Ee3cVKKJFp_D5QuemsK2i_Oeo95f3fxi9Q98bHi_bopjKoOa-VCpst16rlytf4IMRcCxr01cu9QPrCVJyC6hfvu-Ji6XRPyyGv8vz2ToFI2AxFYtPf27PRHQe-0RAdcIgN2N60NjulhwK2IZJM1246mcBCb1KiVPWq1idsKNchxaMDW1N_xZvpOfae3IDqL5sEsaGANKpkgqRIZbjiaug6CF_tBTeTXvJveXXRVabIe5QqXCZb6baCe_r09keVQn801sEhOnRJsZJVZMPc0UnOPHecJIjqoSTvtG3CSkotIVrbg_nJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🇮🇷
مهران رجبی:
اونی که نمیاد تجمعات باید بهش بگی فازت چیه که نمیای ؟
این وظیفه ملی و دینی ماست و باید بیایم کف خیابون
ضرر نداره بیایم و شما کاری میکنید که کفار ناراحت میشه پس بیاید
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71344" target="_blank">📅 10:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71343">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a8a7be1a9.mp4?token=eVd1JkLKzAbgmiljruATixM_wkJhGHl0gGfERY02I8C02B7WPX4ivh7e52dP3I57wcG6zPn_NGduvHbIHnhUR09d9u7INdS6nqWigFVbI9Iet5wEx3Eq9iaW1PMVPhu-o2K9CuZC7rztVgF1mroBV2wqdGIFDJjIhi69RPeRA6UspWZLe8qbt2gNqzBIp4Pu2CEn43_V6K8IscHXQkGgDM8P-v0SwPBPPUglkC1YJCSmjbS_RZAXJIjUHLF7sDdbGXyYK1Pfj6Fmng9OOqqtvmo0DqLc0AMw3H90r0RAPgVVa_ZIYErc_Hlkzu95MLQM9TeNDxez8k9n4ofLg5mSKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a8a7be1a9.mp4?token=eVd1JkLKzAbgmiljruATixM_wkJhGHl0gGfERY02I8C02B7WPX4ivh7e52dP3I57wcG6zPn_NGduvHbIHnhUR09d9u7INdS6nqWigFVbI9Iet5wEx3Eq9iaW1PMVPhu-o2K9CuZC7rztVgF1mroBV2wqdGIFDJjIhi69RPeRA6UspWZLe8qbt2gNqzBIp4Pu2CEn43_V6K8IscHXQkGgDM8P-v0SwPBPPUglkC1YJCSmjbS_RZAXJIjUHLF7sDdbGXyYK1Pfj6Fmng9OOqqtvmo0DqLc0AMw3H90r0RAPgVVa_ZIYErc_Hlkzu95MLQM9TeNDxez8k9n4ofLg5mSKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از طویله مجلس
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71343" target="_blank">📅 09:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71338">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lU3_bK9OTkvuq-_yTHAKU_DM18a2It93PYmVbbQuC2X_ZVB-50VYgn2WGN_-hHtemAlkKB7USywDgCw5Nk4YRA1k0bTmR4Iyt2gsSv9Xz_bqf-J5jAy9M2nx5NbQKtt3Fb_obkHixLMDbADGP3CBB55R5y6VS1k_Sa0jOrN7Z9dUnmwHJC-9NAPR6_Y-w3-_WFbvqdh7a-p_6Vcym1uMgCskS_UyhMz7TONtptvcj_yKpiyHZKhDciWwE_dHNXfHjZOhatcT9yoHyarSIZDGpvZXNyl9k3yi12PmIHP7KEAeoBNZPtosJo6usVYMipMyZHX82AYQb5WkmSTXpTPEKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bv53tz9pL9f1VpWc90ajq-yWDI-v7txSNQnFdHRz0jeTVvYO4KuoGMA1uhiQgAhHQ_9HhMmBu5F7iDO84_NIJWgkU1-pYPZSdP46dorELhA9drPqRHJn0lp2yBJLvVdFjbPaIpt0X9Qfes6ZQSu5FTzHzN6pymd5JI-pTyylP8BAOVmGar62-vswvpury5ULWLFT1GRoSInUIyQ1tI-VRV7hs51pbnHPpn7rgwWI6WJkbGglmsDoOwSf2wvjYAoeNcpzb4oisQoitVbs3HCOlx81aUp187sMjkCbXrMPK-zKqRsiLKsCpmgIjaF-mR1DAEL33i5EYWpV_QjKx5tN5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/APJ0PV8eH61SQGXMbS31EjcmrYqmXKUS4_5QGu7JvTONMJXAinQS46YkZHOfGyDD8WEnrvLyU2h1O4laOEsx8uLJB5HZ74kMP_4kbPBVtXnNatg34y9iDppfH-n8rL5CxU1Hf3oE_vpvHjffnL1d252jiid9uNEiSkD0NbVtSFUpFqGZYAgL1QjpZnBvFbmnr2h2haiAY99m39HMD768emlpFreiUTb2FvbDk9s9RcJHQxOWGcu8hhKvMbEEIcd7UfH4TrO4K_mtbYNr_Jm6T3aS32o-s7RCdnFaHEYsd7nVgzO5meF6fLzWQ2yOF4hM0k8Tj1FuAumPHL579sWyQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RHezhQdt3uuCC5zMHcGEji8wxOtPBddT84BwGwbFK1OWCGM6HcW7ER8JRbuX1fUDhxXKhKI8ceUlCfNz82YpWgoMifnPwzekPMRcbRzMO7gePIqON-3Z15C7rpZgUXaSvCT8oSzE8Nbe7BIn1x1q6RwxOJgMB-AfLjFColEJs1yz-Kzhc4TGTVa5sOS8jQQpEUCU02H_xQhtI--oPhezGdyyY2QLhv6HNu3usuxGAYPw5H72wEQwZie4hxx7LG3qDMHtx3_c_FSR_Ya6U7xZIugHgxj0ayYw4HXtJIS8KFwI3yp5XDdxZA62v9H0RPqyyF5O_hBqntMLBHymeLRTZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pZzjGBhYGg7YIvB2sWsbLbZ3xVBPhxcJBZgwhF9h0Ylu9XuNp5zRWHrje-XzmQGeoDzh8ffeeUAPj-X9pYTaj2YNI6LNugZacskxCkhpPrtKfiFsdfBYuhK_zozv2QruT3rqb5g_elSnN5rBn3ryRIeenoQz8jDBqhXaaNyxyjwQDra5TX5BYpIptzcvKz3TlQSjk9djWHy8olb_9mQZYtLeq9nFiNsty9oKnlm3fYlqZgTpJ3TZxYNw2pw30fZWGZBZsCD6bOou33zwQPMWRaJ_fNok290bP42VOTjLu04iYH_66LgqvmkcAltWhTWd5A8UhCCtlskirtfhg8bskA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
🇮🇷
🇺🇸
سپاه پاسداران تصاویری از زیردریایی‌ بدون سرنشین آمریکایی که به عنوان غنیمت گرفته منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/71338" target="_blank">📅 09:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71337">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار ۱ دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71337" target="_blank">📅 01:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71336">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfJbzGvHemyMx9k6iNXe_O2umTQf7yfcqFSClJzb0B16GeXb6k4r_6fTJemLMh_QOOZPRzHIiISbD5aEtRwzZGf77XzmENnwuUbz91vhJ1ajg4NOyLTSl6vXeQRqcXD0uMyKbtBYzvFCDrl3OHy86SRdecK-BHi-aD7kn2Xq-qZOlJQvW2dApj8QqsyB68G1ug66Nh_kELH2wuU0gaSH8dOjFlzwOGJ0AZLNwxDcrMaTkJAPbqPKn1OKvYNbZLsqb2porSvK3Kd1-yV8zWpM3fXG0zyvNakRdh_8in89HLp3ggdwM5iiUYw2ihUsNENDRqmG22ZiNmSnlwfC88VJzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار ۱ دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71336" target="_blank">📅 01:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71335">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
〰️
#فوری
؛سنتکام:
نیروهای سنتکام در تاریخ ۸ سپتامبر پنج شناور حمل نفت خام ایران را منهدم کردند؛ این اقدام پس از آن صورت گرفت که سپاه پاسداران انقلاب اسلامی طی دو روز گذشته، دو بار یک کشتی جنگی نیروی دریایی ایالات متحده را با موشک‌های بالستیک هدف قرار داد.
کشتی جنگی آمریکا با موفقیت از حملات تلاش‌شدۀ ایران گریخت و به گشت‌زنی در آب‌های منطقه ادامه داد.
هیچ‌یک از پرسنل آمریکایی آسیب ندیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71335" target="_blank">📅 01:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71332">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
📰
خبرنگار العربیه:
چندین موشک ایرانی در جنوب سوریه رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71332" target="_blank">📅 01:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71331">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/665d19bf87.mp4?token=uuJkX280M3ufbCB3eFpnFz9B-HrF_bGI9pqwjrEAxJCEtaUQu9ZsfMCszrtRDJ61M_5qjwzYuflxfVkGg4c24k7-Rlk70rnNVW5cQOr4Z2IGAj56wPjI-C7kPOGTbfQOmqu_0xJ9CYStBO_Y255G-snA2IkH8R0Nl2XKOisV2v2L-6IYSnuEY5TBy8Wb_PdCtdeYuAlQqY3Dd38_96fnfX9UQfl6dExksGQmgpMhAhi2vcueguhqcmkGk_s_S8VW5tPzdnqtta4Y718_MhjelgiS_Ac3EcJXGmVKNZDJ0dAofRXn_no1O2sDMd9PmwHFPJeAl7M0DM6ZH9AUAWFUnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/665d19bf87.mp4?token=uuJkX280M3ufbCB3eFpnFz9B-HrF_bGI9pqwjrEAxJCEtaUQu9ZsfMCszrtRDJ61M_5qjwzYuflxfVkGg4c24k7-Rlk70rnNVW5cQOr4Z2IGAj56wPjI-C7kPOGTbfQOmqu_0xJ9CYStBO_Y255G-snA2IkH8R0Nl2XKOisV2v2L-6IYSnuEY5TBy8Wb_PdCtdeYuAlQqY3Dd38_96fnfX9UQfl6dExksGQmgpMhAhi2vcueguhqcmkGk_s_S8VW5tPzdnqtta4Y718_MhjelgiS_Ac3EcJXGmVKNZDJ0dAofRXn_no1O2sDMd9PmwHFPJeAl7M0DM6ZH9AUAWFUnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسمون اردن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71331" target="_blank">📅 01:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71330">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf482be15e.mp4?token=YGYgVyLN4aTuB1wS73C3Bn1aA8G2JoKVVEjtlI8pHjXv-ShvE3AsIjS9HvdtO04aa6BxQIJ62DUup_2UGBQpq50LOroCvBS1eKmtsGzRhZV8bW-ZMqltMIZuiS688JjLRHcHLIUiVayp0_gX6spsuMvHDG4uje4HrQjGCy5FSwa4Ougzek3axoDNwqaNUp3teKrz8bsavY4GYvnY4DLKCYEQREe20iOoinwg6OypXxGRdrSToAw5-UoLzYokbLWqz-q1scqT0rb1eW14O--GDR4qRMtatYsdXYYr0quT4WsYERjI4aKcUonrCHCjz0tGx6dbTiTQAvVP-Yl_eGJ7Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf482be15e.mp4?token=YGYgVyLN4aTuB1wS73C3Bn1aA8G2JoKVVEjtlI8pHjXv-ShvE3AsIjS9HvdtO04aa6BxQIJ62DUup_2UGBQpq50LOroCvBS1eKmtsGzRhZV8bW-ZMqltMIZuiS688JjLRHcHLIUiVayp0_gX6spsuMvHDG4uje4HrQjGCy5FSwa4Ougzek3axoDNwqaNUp3teKrz8bsavY4GYvnY4DLKCYEQREe20iOoinwg6OypXxGRdrSToAw5-UoLzYokbLWqz-q1scqT0rb1eW14O--GDR4qRMtatYsdXYYr0quT4WsYERjI4aKcUonrCHCjz0tGx6dbTiTQAvVP-Yl_eGJ7Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
مهمات خوشه ای سپاه در آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71330" target="_blank">📅 01:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71329">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🇮🇷
نایا به نقل ازمنبع ایرانی:
سپاه پاسداران انقلاب اسلامی، دقایقی پیش، موشک‌های خیبرشکن را مورد استفاده قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71329" target="_blank">📅 01:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71328">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee276f397f.mp4?token=KEImpUT7kB4q1CQru2xEVtNqmzxaVjUt84psoQDWZeCd26tFIF6Tey_zxLPt14YDfqthM4NjUkv7sMgk5ug26LspqA3nu6ioL3U21mtnJt0l2iPYcm7dGXRdLc13Ow8J6BBSCmTJGQdENCh2xiShSExT5ym7XwPRKSfQL2tyEtQH_eJQ62P17k-kjwnTSOFjHtkfz5TgswZaTV58DNrCdz3nSwsi8bZyhf7czZDAKQydyy9X6cTsKWxI20pt5mB-3J22J7-f31qsJW30RHEGZxR0wfx6z_bt6SNYZjwZ1UKZCJTIKcB-tHEuJTGbXWkJ1B-uXWxs3OehINlGduZBVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee276f397f.mp4?token=KEImpUT7kB4q1CQru2xEVtNqmzxaVjUt84psoQDWZeCd26tFIF6Tey_zxLPt14YDfqthM4NjUkv7sMgk5ug26LspqA3nu6ioL3U21mtnJt0l2iPYcm7dGXRdLc13Ow8J6BBSCmTJGQdENCh2xiShSExT5ym7XwPRKSfQL2tyEtQH_eJQ62P17k-kjwnTSOFjHtkfz5TgswZaTV58DNrCdz3nSwsi8bZyhf7czZDAKQydyy9X6cTsKWxI20pt5mB-3J22J7-f31qsJW30RHEGZxR0wfx6z_bt6SNYZjwZ1UKZCJTIKcB-tHEuJTGbXWkJ1B-uXWxs3OehINlGduZBVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گویا سپاه توی حملات امشبش از موشک خوشه ای استفاده کرده
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71328" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71327">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f211389571.mp4?token=ArC_8XGfZAT-rYKx_iv1DbpD1arty3_sClTH806oR6uElhejFU_fDkdbN-VHw-NKMzyLHOeAToojjrrH-a8QMS2HhpeM9-8VvWjxUMUka9rMhfKBdNsenwVb_6eANrBFCvDIpXz-ySPJuF8totYRAc_EUcpVw0jukJ-RCvew4pKTvFDAalz_nSslwTZy2HG6779FCm8CW2q7OFZCZDYX3XKlAe9IEQzRXdtg1X5-lfmlmO60hD7rpffInFRtHACK3_gf1ROqUhcbBdCExkrAkZvTXmKkKpDbPH4F7PS7KgK5vBn154ZxTUO-knndc2pTZ2Om1atqfQZs7Xvib82Cpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f211389571.mp4?token=ArC_8XGfZAT-rYKx_iv1DbpD1arty3_sClTH806oR6uElhejFU_fDkdbN-VHw-NKMzyLHOeAToojjrrH-a8QMS2HhpeM9-8VvWjxUMUka9rMhfKBdNsenwVb_6eANrBFCvDIpXz-ySPJuF8totYRAc_EUcpVw0jukJ-RCvew4pKTvFDAalz_nSslwTZy2HG6779FCm8CW2q7OFZCZDYX3XKlAe9IEQzRXdtg1X5-lfmlmO60hD7rpffInFRtHACK3_gf1ROqUhcbBdCExkrAkZvTXmKkKpDbPH4F7PS7KgK5vBn154ZxTUO-knndc2pTZ2Om1atqfQZs7Xvib82Cpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعالیت شدید پدافند در آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71327" target="_blank">📅 01:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71326">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
از اکثر نقاط کشور به سمت پایگاه های آمریکا موشک شلیک کردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71326" target="_blank">📅 01:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71325">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d314b4d1bf.mp4?token=AYjBxlgkxFa9APS4UBZZfCLBaeG53bZVOlk2WezVddmp5GOWmCvE_yOMomh6A8zHwzLL5Iz-RoRDVyXYld3Lyvp3mkHdY-AXo8fQSFdO48xLYX8v-S80yFw84rhyJ_VHkarJ2nd07MJqLoxp1oeT5g5RZbe8Y_E_wvTHkIu-gcOSRERYQIsjc0juc4qALU_5XuWYOBJjrbV10knS8t4SWQMpLpt39HQw08ZWtnk-idHGgXfnXF4tqCU3TiFb-BRg6eKDJ179K8KvHUE6CVEMHsFfNEn1du9SQTF_2d_5641UbcMr6_OsnWs6noagj-od1QjNMjhryseXEeZCp9KKmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d314b4d1bf.mp4?token=AYjBxlgkxFa9APS4UBZZfCLBaeG53bZVOlk2WezVddmp5GOWmCvE_yOMomh6A8zHwzLL5Iz-RoRDVyXYld3Lyvp3mkHdY-AXo8fQSFdO48xLYX8v-S80yFw84rhyJ_VHkarJ2nd07MJqLoxp1oeT5g5RZbe8Y_E_wvTHkIu-gcOSRERYQIsjc0juc4qALU_5XuWYOBJjrbV10knS8t4SWQMpLpt39HQw08ZWtnk-idHGgXfnXF4tqCU3TiFb-BRg6eKDJ179K8KvHUE6CVEMHsFfNEn1du9SQTF_2d_5641UbcMr6_OsnWs6noagj-od1QjNMjhryseXEeZCp9KKmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
موشک ها در آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71325" target="_blank">📅 01:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71324">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
ارسالی از اصفهان:
از نجف آباد دوتا موشک از اصفهان ۴ تا
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71324" target="_blank">📅 01:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71323">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6edcd17216.mp4?token=W4qN1eWUtnWjl_RW13kEe8u2ST2MtzGCa_2zq7oc6lYyAgFfxQPbEs_AHF0qQCYs4xWgFD-hoNvysrdsEwKv0azVGtJZTl-1ibbpVtCI7LUDSeAgwHu6JDcPG2zHKS6wTSqFKQ53oWvZ-xvMZ7t6gbOdiuXvKbYp0hIp5mJ5Y1_UtyVoxkH-arDo-ZI36Q8BoAh21q8LlY00mLx4dAoi6X4MP68d0QFI-4pt2yzeNPI3Or6b7eiibSBu8ZRrAPJM94ijDo3dlgoxwNi3yFBXbFL45NXpurHeT_N5_uoi2P-Quf7i3Vf7L5dM_Ad-9mrchye5llxMwcVwbsESqWEVkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6edcd17216.mp4?token=W4qN1eWUtnWjl_RW13kEe8u2ST2MtzGCa_2zq7oc6lYyAgFfxQPbEs_AHF0qQCYs4xWgFD-hoNvysrdsEwKv0azVGtJZTl-1ibbpVtCI7LUDSeAgwHu6JDcPG2zHKS6wTSqFKQ53oWvZ-xvMZ7t6gbOdiuXvKbYp0hIp5mJ5Y1_UtyVoxkH-arDo-ZI36Q8BoAh21q8LlY00mLx4dAoi6X4MP68d0QFI-4pt2yzeNPI3Or6b7eiibSBu8ZRrAPJM94ijDo3dlgoxwNi3yFBXbFL45NXpurHeT_N5_uoi2P-Quf7i3Vf7L5dM_Ad-9mrchye5llxMwcVwbsESqWEVkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند اردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71323" target="_blank">📅 01:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71322">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
گزارش ارسالی:
از زنجانم موشک زدن همین ۱۰ دقیقه پیش
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71322" target="_blank">📅 01:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71321">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DT-HKm9Y4mZDuofA0shkm7696AvDbA0UN2TjwQCNktxvniLh10vAZ5ptv3hyV6Z5blUVi0Q-5xdhLObJG_m4qwu_106Qvwv5AGnktnoaD5T--PwVnMADAUbMePhoDMYoayMujJG_qBgl6NoB_NFbbztOtqPlg_kSTntQTMCkEnojzzglqpyLKXvhkH82hmB7SojsKcT2XEh-ZbOEnQo5ZGoSEgztlVA9F7PSkMT5qsFB5439FS68a8ebh60AoXog54sQy1ScT_wGTB4zLbsJw18yGS6Syoq9EgQ_aD_U5JvjCcamG-gkrmvw4H8Q1q4XgJSxSGb3er6xTU50uGFd0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ارسالی از نجف‌آباد
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71321" target="_blank">📅 01:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71320">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc98612785.mp4?token=c3E-WSid3hHS2iKMIM8BtvlRScvc8ILPl5IKZu4hHOf1hePGHTsjCylzjn_WgSsHOQouOUqXJuayKvH6vThEinaBruuY2YzctqUyVbdf6Oz_hV17W18rfwlkhwbnPHZNIGR0BLvm__XezJh4JBoDWkpjOzyw--XG0CwZ0eC0gCy6bNVMYuBmSsfoMY5hs53DqEBNyuFA6oFMrQYyzY3wlIGf-dAaqqSgKDV6xiacxhtDgyAT2j_kMUo7pwzF2CmMLwh1oceyW4n9xUy0iyT7TvDSdKaaZ_Q8vZoUVicCQRjdIFnIxRv2txbZhy8-xYJcL2F0-M-JWkI6GxUiQJTV9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc98612785.mp4?token=c3E-WSid3hHS2iKMIM8BtvlRScvc8ILPl5IKZu4hHOf1hePGHTsjCylzjn_WgSsHOQouOUqXJuayKvH6vThEinaBruuY2YzctqUyVbdf6Oz_hV17W18rfwlkhwbnPHZNIGR0BLvm__XezJh4JBoDWkpjOzyw--XG0CwZ0eC0gCy6bNVMYuBmSsfoMY5hs53DqEBNyuFA6oFMrQYyzY3wlIGf-dAaqqSgKDV6xiacxhtDgyAT2j_kMUo7pwzF2CmMLwh1oceyW4n9xUy0iyT7TvDSdKaaZ_Q8vZoUVicCQRjdIFnIxRv2txbZhy8-xYJcL2F0-M-JWkI6GxUiQJTV9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ارسالی از اصفهان:
حداقل چهار/پنج موشک دیده میشه توی آسمون
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71320" target="_blank">📅 01:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71319">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c50434db49.mp4?token=fQCD0qJMz_Wu7XcPobkkL_ciQGgGs49ZCrKpNAc1uH5iILtlWHUpWWGh-sJu-Qvc4w_NE3dTLbOpXyfF7fpT5qdhpj_GTn-6jGqvts0E6hW8B_VItaMAZU9F8DsZBFUHQ8uFJGhfcJ84goRL0r_1Q2e_NuKAWv47bsA1X_f85c0ygFPXj1m6T987Y2qcnV6xNvD2NnHNsuUdQ3IcMvWFKI7HEx1Bv6OkdgCgGVAvyXaqX503Hi2oc7um8daNFI0Fky2tuQfm8LMWyMrFPB8KRoEJDopMRAdMNY1iusTFJjHJMyeB1hKBHxtf5_jLLp24cJ94tNbYisPHK5vuuw6fTg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c50434db49.mp4?token=fQCD0qJMz_Wu7XcPobkkL_ciQGgGs49ZCrKpNAc1uH5iILtlWHUpWWGh-sJu-Qvc4w_NE3dTLbOpXyfF7fpT5qdhpj_GTn-6jGqvts0E6hW8B_VItaMAZU9F8DsZBFUHQ8uFJGhfcJ84goRL0r_1Q2e_NuKAWv47bsA1X_f85c0ygFPXj1m6T987Y2qcnV6xNvD2NnHNsuUdQ3IcMvWFKI7HEx1Bv6OkdgCgGVAvyXaqX503Hi2oc7um8daNFI0Fky2tuQfm8LMWyMrFPB8KRoEJDopMRAdMNY1iusTFJjHJMyeB1hKBHxtf5_jLLp24cJ94tNbYisPHK5vuuw6fTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو ارسالی:
همین الان از دماوند موشک زدن
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71319" target="_blank">📅 00:59 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
