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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 15:05:25</div>
<hr>

<div class="tg-post" id="msg-71417">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 953 · <a href="https://t.me/news_hut/71417" target="_blank">📅 15:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71413">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gyThFtJs6oWSP2GuJvrZi4lI0nTUUzFun8EvFVR7GFvUl5ZcufzOosoMn9MuQDOE0eEaiqHjPC7K0ZxwSVRDCuS9K4EBu0e56q_zPr8nVH3lTlV-7S3PAmO58t4Kga-9Pil4es5aptIejrSSEBHKMDEg0TMc4DHmP5e-Bqr7Yn__s487Drqj0tkHKG_ouJa5AhbyiPqVzPMc5a9gCYHXvH7p6DIw1zHYHh_MtFSXw6HVugqHDhKQ_GnhbiqVbu8QTpJ__s1Qjiir1tlhn5A2M_N7WznLDOMBcA6So4aS6RJs4mdsjZ0NiNugYsiH4Kh8wtUVekSa4liZWC2j2nI_9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tVgGDOEyIWPTMU6VWJEvdv9kJTpvCgxDZZXmqwzSHbOyXo8iRZNRHCyqxn9AhPYHWoxKYr66Sx1M_LcqY8BWtRAs6NTHfRYjQkZHKnKZLfahs-DpCunnt7GykJGDYeLGqveZhuz31N2LbF6TrzKOzVPBkAj1JMm07xOrXL66xE0fwzMzw485DKNnMcDgcd5xkDkD2N3P91g0KWk_VaiDmQi2376tmaOuFtNUSoBYM-wVkEiYc0gMbqdKuPjNgG5uzeAzAvbpUxKO_MdpJem_dE2BjhBHSk0ffCpPq7nYJuXvm_DC9vLChAMEBjODLyq3QgE1U1v2Jx5lJAWVsFwb1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HA26e_00GHZSeB56cqYePcK5z1Z0vGewfDoezZhjyqEM7ibRCxQzUVYZGhCN6RNXP4w_WAoekYw3nQOTX5jBAAlf45X7izRJefZH8kdsNgd1X5sW_rGN-dnSx7MAhbNlZUOpv5jrwV2zAiLkJwyRvqH9RqTv-fBH65VG68kFwDxe2jO4roSlwqr7PfOnYZJ82O7VFY3QKekUR5tux-6cypWXJS1I-E-4uoQUxh-ulGROpK96j-azZ0HeIEPWiZ0BM9WddJQUhOL1yjkRTIgb80g6oc1o8XPwHxO5oo5wIWJ2onb-Xy589uTdPJRRyJeXUDI36-HOr4rES1GGBPdT4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fMXjK69jv_6QlGzE3gY8WHQYjzLWXSTBY2M7jO68dWR51MfAXZq0wXGI0ubmUWQSO1LyLIopizZ-XXkGf446gXzsDr22Gh03HT1LHTXxuxb-Oq_gqOpK_HHexGy_SHVCIzqi1g5fsWxQQBUfvftnYRsGiHKAmhzm0yCpgSqb9O5jAS8j4_H0zbtXWpOJqHDakqejm9-HUgA5bBoKF6yC6H8OhxLXcBrfRmEOCONCdjrDcs3aszlf-VV66XDwM4wrt3lCCbSQvbBxleef7uSlWkrGXENMQVcLzilGvIcrlAz1X9h8wHlZ6OSsxpYmvb-q3K9yG7EK6uITqVoE2iomyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇯🇵
👀
شب‌های ژاپن هم قشنگه
@News_Hut</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/news_hut/71413" target="_blank">📅 14:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71412">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/news_hut/71412" target="_blank">📅 13:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71411">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZr7BW2VKIck1gbmqMFHVzYSxdf6Xqd1rmCn_nGLcuF6YbQxrk_DxCbQ7y6oEh1Y8XAhxzKcnSwqZG-Jimz55XOKep-Hkb01ZyykIIqB6DFoJgMJyosB7N7tm4fC2TvzNI1h_tKNZH9epj9eq2MtdQzqESQ_f98pfRC0MoZyAZie_-oTrU0fUiW1ocOAJhAIasauxq0w1sR7CMEpkn2BZ6gZSbQEoeAR-6oeuXetvevcznyewyWoNcFGLNV7gH26GxhyfbLNgIyrLKS8Nzlh3atxbN_VI5eQmYQB5Hvx5FVm8uu1i88hidfFN9ZhdHjVM4zzjHvib1SsHhmcUC8uqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
توییت سفارت جمهوری اسلامی:
سرآشپز رضایی در حال آشپزی‌ست..
@News_Hut</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/news_hut/71411" target="_blank">📅 13:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71410">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/71410" target="_blank">📅 12:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71409">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇺🇸
ترامپ درباره ایران:
باید بگویم که این به لطف «نیروی فضایی» (Space Force) است؛ پروژه‌ای که فرزند معنوی خودم محسوب می‌شود.
از همان لحظه اول، ما می‌توانیم همه چیز را ببینیم.
حتی می‌توانیم برچسب روی کت آن‌ها را هم بخوانیم؛ «محمد الفاید»... «میامید» (Miamid)... البته هیچ‌وقت «میامید» نیست؛ هیچ‌وقت «محمد جونز» هم نیست.
«محمد»... «محمد العزوری». و این نام دقیقاً روی همان برچسب نوشته شده است. ما می‌توانیم آن را از فضا بخوانیم. باور می‌کنید؟ از فاصله هزاران مایلی، داریم نوشته‌های روی لباس یک نفر را می‌خوانیم.
ما دقیقاً از اوضاع خبر داریم، اما متوجه تحرکات مختصری در منطقه «پیک‌اکس» (Pickax) شدیم.
به ایران توصیه می‌کنم که دست از شیطنت و کارهای زیرکانه بردارد.⁩
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/71409" target="_blank">📅 11:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71408">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/71408" target="_blank">📅 11:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71407">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/71407" target="_blank">📅 11:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71406">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/71406" target="_blank">📅 11:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71405">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/71405" target="_blank">📅 11:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71404">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/71404" target="_blank">📅 11:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71403">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/71403" target="_blank">📅 11:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71402">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/71402" target="_blank">📅 10:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71399">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/71399" target="_blank">📅 10:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71398">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0uwcYj4hrN72x4kbYJxArznDEFpuJt5NvrDKAHpvIx7IWvwwg6kzm4Z28Zc3vdNDR9MQMXfFUbYRqQOBu_69hzYHkreinsjiJfDwSTw9ghnH_7QagbLs07X813NjROifIdr_AP4zPgPERT9chHrXbRMZNCa8Vz8t5-JuRwkzIUGw9g7p8xJbdeAuAogc9SKqIzt7uZnOOyzcs9mcuBl-c2_CXi1H0vyXpTSuFMWx5qyFeOgI1FrdZD4O3jeuL_EWkRH_9pKaQa9PG5uzSNuqvcDskbNaG6yeYFEOzBsOfa3bczCZsqh-WfzRcOhJCPZ0IH8ro_fulMW_PesaE66Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇵🇰
🇸🇦
رویترز:پاکستان در پی حملات گسترده گروه حوثی‌های یمن به عربستان سعودی، پیام هشدارآمیز ریاض را به ایران منتقل و از این کشور خواست تا حملات حوثی‌ها علیه عربستان را مهار کند.
اسلام‌آباد پیامی به تهران ارسال کرد و از آن خواست تا با استفاده از نفوذ خود بر حوثی‌ها، از بروز یک بحران منطقه‌ای گسترده‌تر جلوگیری کند.
به گفته یک مقام ایرانی، ایران در پاسخ اعلام کرد که «کنترلی بر حوثی‌ها ندارد.»
با این حال، دو منبع ایرانی به خبرگزاری رویترز گفتند که تهران حوثی‌ها را به تشدید حملات تشویق کرده و وعده تأمین بودجه و تسلیحات بیشتر را به آن‌ها داده است.
پاکستان اعلام کرد که هرگونه نقش نظامی این کشور ماهیت تدافعی خواهد داشت و بر حفاظت از خاک عربستان متمرکز خواهد بود، نه انجام عملیات در یمن.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/71398" target="_blank">📅 09:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71393">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hAiNYdmyDj4p0EB1cCFd_B36Ge3IdZB0aG5zWbKvVIx1dTA_Tf6SfuuFYf1pxKA6_qO4ykShaaXQGRF8_r5TJf4AOlb4lVcycSkG1pomECea2wvmn7Eiz9qvqIDi81LNb1fDuA5jMEuQK8zciPBGVE9bIvweaRV7xTHqeFgcnWB2NBI7pQU0T40Fs9zs_BS9mm0S7G5knno8wnQ1IEivNSbPBrO7hucy9ODmhKsEMRcKa0bqTzFaImv_cnx-DOr3syh7chY6BBhGZOoDi4dkHNF6klHf0RarfG6f1bIewO63JP34fB14Bxbo0zFyKnuSKqz2ADM1monrdcmv33mnPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZtPMy6sHCDW88EpGGew5eyznokVXl-gWoHUV9c0uZbO26mMuIkmIRadpcmmJ2CV6pS1rWNBU9U1rS3KRpZDES3IjSBNyDZd6QLR-5yo-BpCLnCQD1qy7gbXREnOvOx0W11WvMOivgtYpUWy7ADnLGOOemqyWlVlnMDmX-hqC4-kDQ-OYEQX97nRKZnL_vwVvCklNY_EsyZJExE-Yq1f2rxLRyo6gdn2E0vqKr9JZV6W37GzojQ1tfDvTF33E42ab0njFlE-bLx858AfRz7MlDcdX4C1oyRceE_IQPuQUPreC52M0IhV8qYLd2ozFXDcWtuJphP7GD_A5U5R2LaL8bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5Lk6n7UH3IiY-l5ItRif8WOhz96T5Z9s9oALjRF0osuNo3z-3OkMN6dYjVPxC2lLXyMVNVSsZ7NkxCUlGeXIi3Ajbh4pVkGWxWozVTqjSQuilerpjyWMMsBxzsb0Xhu55Q1iJW56_8nfEYje2JZRs35_LuFMH8zHnYcXrks0A3sI9A8KNBzKTO1b5vR6AZkovUc-zBNN4iom34qlxCVxKIURkzgGR1CXWKZVSf8enO3syFHPaeBms3KHIHMR4SnGxn_q3b74jzFSLDvP-6jL76EiWeQ_kKPiKvbQDkDNVybaovPjq9R2xaAk2QhYaZ1KuDLaUFTFQSWfN3SWcyUQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m0nNbnxcQV32jH-RRnfQTS7DHvmGWgty4hymNcd-GxLJLC3IJoAu2ybPLuUAwwjiBnpuLtMiAUiiV-_04qNYhEmUmRTYISwiirmWKMPD84hIXBwXCQI04_VWIPr7g70y8FmA91SsbAoTpsPIUBPY0--pFUfLHd5TNaeHYwYAogCNqzdKqJQCBE1IBONGnAJjSc8aLfVF4ebZXLTijZFUQSesE59cUoA5-QHVUcCvz7Edc_KM_56cXqmJ2bLn7LMSdRObXp4DQmZ9xTr-NwkPxCGgE1ROTDtKxrk_JB6vWhWcYrteCcjrPzKUx1tYsTqh3-Xr8S5XJKYQimHRtOUicw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5fed9d1b.mp4?token=vkS4kpETtVVmLYAKhUdmPW0H-tBNPsBtMXfZZI0PMiBzpuRXUQV40c6EKo86iQuSaz9eBZAKo9dIPCF6_4sCNwBziUt1_VWjRB4Bs6NEk0_69qgRyIRlmVGhKWlyPgEaJbX2b8C8K6d7P4M9oZQSoxMq6aR1P63uwCLT4GU_2iS7xS_-fYeJHHovfMRT_VSUAt-tSh2lNAoi258jIDM94vBB63B5BE4t4lsdfNJN60cTtd4MA0bSP5qYtCVF1RMr9oeP5ULxTL-5nAxhxbO-SYjmoXmp1x_2C7lk6LJ4tNH0BgKjFtMw9cE09jkRssbENkVCWDZye8kS3t7traw7_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5fed9d1b.mp4?token=vkS4kpETtVVmLYAKhUdmPW0H-tBNPsBtMXfZZI0PMiBzpuRXUQV40c6EKo86iQuSaz9eBZAKo9dIPCF6_4sCNwBziUt1_VWjRB4Bs6NEk0_69qgRyIRlmVGhKWlyPgEaJbX2b8C8K6d7P4M9oZQSoxMq6aR1P63uwCLT4GU_2iS7xS_-fYeJHHovfMRT_VSUAt-tSh2lNAoi258jIDM94vBB63B5BE4t4lsdfNJN60cTtd4MA0bSP5qYtCVF1RMr9oeP5ULxTL-5nAxhxbO-SYjmoXmp1x_2C7lk6LJ4tNH0BgKjFtMw9cE09jkRssbENkVCWDZye8kS3t7traw7_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/71393" target="_blank">📅 09:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71392">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71392" target="_blank">📅 01:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71391">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YiP3scPygf7TtU9kkNSQkddHBf1yDJYvsBCv0hQGxNsEGNGUuuJF685kUBOzbWBISeBbQamnWaJHrtzN4IZUNFyeZNkb0LE5K2Xcs4b_tdq0ycQbPs2Mu6_B918eQoeaWu3n_l6uwYL1JrQdivGT90AzOir71qES1VMe3dNKmYHH4asiPxJm87KDRsPCG_89hZdgh8BHilOOeuf1JJYIgD3gAtdmd9piBXKa4CNgXBPzDAoiItMzkglo7fWAZnHzICQLxhj-yvz_yOJWGz9zBd3lhCZF39U1TImM3M17FTzLt9VtvRB2RGpX9koEISGd0t29RqjNYoa4tQxQ0Io4eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71391" target="_blank">📅 01:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71389">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C3GLnIoprc-PEsnPW8108z5-34U6TYToSnRAhgEed-nHb68QgGdGaFELLcaaXirR7cS78WxmJgEiKooxSAD9r2mU_v0oi25FHBjW9C4x4YKv4z4QZiv-I45qZSS7KbHHQFDRYCzIPzzgrMQe5PAOqxocq9gtFLYMS_jJ0McAH-gV1qqp4IT9xdQE5Kt9NTFTtDfaGD_Nbcm8BcA8cC_jpOJmLIX5QV2jK80tmHYT-HA0btxR2mg1uyoRraqMM9PiaZQKt53mga5LHfMVC6SffVu4q69g5chp1qJyvcqAjpXkiYM9WEaJb8hKW9uLQ0-lFJkBfrWtYy5mW6kL5_WThQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X61ZyTFZj0tHRTiFRoaiW7SDYNLofDncnxZmEanK5mrpZVQaIrIAq7_3xLEN9Q-9JVWHlq7fmHKW0BEfb3xmHJQBpgRFRCcWjCM7ODkXZXgaTL7lvmlsRjoWI44kceWdhQAZUc-ndtXaubfLR2m6FXaGyIvYZ-2OyUDMU6Zkj8vYK-fPTokE8aTolHIjnk-6mZE3EiARA5yvDyVQ-3f2sLnUAQ-7Q2vIIbEYENQGIBaaIPlQ5xOuvlR4n81loJTWpoFj9P_P-HKTN08FN9BRZ64UtD6dSEejw0xrzqRl73tDXgSoTwqJI23Zzgduh1TnXxF7arGLCKoSyJUWRAauKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
به گفته منابع عربی حوثی ها وارد منطقه حیس شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71389" target="_blank">📅 01:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71388">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
فارس:دقایقی پیش صدای چند انفجار در مناطق ساحلی سیریک و قشم و مناطق ساحلی شهرستان میناب گزارش شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71388" target="_blank">📅 00:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71387">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
گزارش ارسالی از قشم:
قشم هم در خونه ما لرزید
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71387" target="_blank">📅 00:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71386">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
دقایقی قبل صدای یک انفجار مهیب همراه با لرزش زمین در کوهستک (هرمزگان) شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71386" target="_blank">📅 00:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71385">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/240fbc3c81.mp4?token=mncAUwasxpijFZP2k1NL2iK-_RL5EiJuO6NWNrtlgqr3G9cFGX6uIFA2AT5FNnaTQzFu1hF-pMtj3jrXaYvK4jO6b2H5czBjzg5qKxT56QpWyhkUYicQGc5SqoOxe3689FAzXSBTrn3ggXgI00G0HIXHT0yJJ-sKa7ejdG1kWPpONjFEdbztRwtSWvN4CmhDYMkBNtRBvo3v9rwcv3kwtyIDmyW1uXqBJmWT8nEoOR0-TbFzDGGFlykEvmWMeA-p1nK9dAwWounPXGJNM_qG0hpyB-ZgNmNGj4Gpx49Xk9noxu0jmJNadqmE2d2JIzpxA-ecduXffD1LhQgwNItpIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/240fbc3c81.mp4?token=mncAUwasxpijFZP2k1NL2iK-_RL5EiJuO6NWNrtlgqr3G9cFGX6uIFA2AT5FNnaTQzFu1hF-pMtj3jrXaYvK4jO6b2H5czBjzg5qKxT56QpWyhkUYicQGc5SqoOxe3689FAzXSBTrn3ggXgI00G0HIXHT0yJJ-sKa7ejdG1kWPpONjFEdbztRwtSWvN4CmhDYMkBNtRBvo3v9rwcv3kwtyIDmyW1uXqBJmWT8nEoOR0-TbFzDGGFlykEvmWMeA-p1nK9dAwWounPXGJNM_qG0hpyB-ZgNmNGj4Gpx49Xk9noxu0jmJNadqmE2d2JIzpxA-ecduXffD1LhQgwNItpIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71385" target="_blank">📅 00:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71384">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71384" target="_blank">📅 23:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71383">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/364cd7494f.mp4?token=NZCbj1jercCy7eNirCDNVjryrESWXS2ARQIz0C02V-xCzY50ljmC8rtjmrBp8z9ABUUZyVXoGVXCy01EsNuiYe7Sdn18CqwBID7lZwr4Jj9rYZHC_el8lwGK_v1MkHkbYfNbv-qJBjz61DQ-1gwjQh-broksJQGTOpFVMkH2aE9IRguD1hpfMJNM0dSsZQZkWF1LKpRQkPnXE7DwU-fvM-xLA1ze8sLvmc0goKaacxarNzxpTAQiINPArskGjeDcyQhU7HazB49QfmPo2el9rpPbSam_w9AsbqOQCpFV8BzR1zLrfLbF1wta25Pa5C7GR4Fx1wZNSqDCO8iHx0k7-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/364cd7494f.mp4?token=NZCbj1jercCy7eNirCDNVjryrESWXS2ARQIz0C02V-xCzY50ljmC8rtjmrBp8z9ABUUZyVXoGVXCy01EsNuiYe7Sdn18CqwBID7lZwr4Jj9rYZHC_el8lwGK_v1MkHkbYfNbv-qJBjz61DQ-1gwjQh-broksJQGTOpFVMkH2aE9IRguD1hpfMJNM0dSsZQZkWF1LKpRQkPnXE7DwU-fvM-xLA1ze8sLvmc0goKaacxarNzxpTAQiINPArskGjeDcyQhU7HazB49QfmPo2el9rpPbSam_w9AsbqOQCpFV8BzR1zLrfLbF1wta25Pa5C7GR4Fx1wZNSqDCO8iHx0k7-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71383" target="_blank">📅 23:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71382">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8c1afb2e.mp4?token=TdbaI533OtqtZ84qRBSYHNyIeVbKmZR1fM-MGeYofKr2UdShWdCWAb-mJvgXBydC-Bt9lWncUCp0eN0VrD3OXzesKeQ_V5DBdvYNZP_7l348CEMXWe20Tpi_cP7ve60EiadWdzZERe7mQ-SusXvaDd-nM4J7Ewg_3NeWAQxMdxh-WHiO-rEHhVrvAETeKex2SwC9b-ts4oKGWo0ZYjeaQ9vBVhYRmN5EZ8KbSt1EelH4uaSRQ73UvydPbg1QvDJo_nfADJjF_JWyA79BKJZFfXaID7sKxTe6uQaonf46_ObGQraBBBp2Y-D20962gsSvdQ_X4jm0wNKZiiy9LjwUJ6FHYFn7bhLUUj43QjrUvzxkCB6igxZFz6-VhMihqSLYs3tfF4FJwTa0UpLnO4hqdTg6TPVhrSbNFbSWO-qG2xrEVG-pyXt7DpKHcb1Fb4DkSBT2nPfy4T7jq1pd1RB2IXV_Y2V_VfPVSxqUv1ZKTrJ9QfXVfovrdupf3z-Ovrawxf8zf5tlaVfZpdLOBOKrG3WldBDUWmd3oRUSh9vqwoiWnbGq87LmPQFdntnGn3hzqsIeYlZCxJLaqH0ANUGIgQU01zwZqJgJu6G6ESqolwyHVf5z_TkIGT16kZRg9YNgkUFTUNCOxb0qDJ7b8T1r3_TlRjJm9KV64sMKGk36zeY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8c1afb2e.mp4?token=TdbaI533OtqtZ84qRBSYHNyIeVbKmZR1fM-MGeYofKr2UdShWdCWAb-mJvgXBydC-Bt9lWncUCp0eN0VrD3OXzesKeQ_V5DBdvYNZP_7l348CEMXWe20Tpi_cP7ve60EiadWdzZERe7mQ-SusXvaDd-nM4J7Ewg_3NeWAQxMdxh-WHiO-rEHhVrvAETeKex2SwC9b-ts4oKGWo0ZYjeaQ9vBVhYRmN5EZ8KbSt1EelH4uaSRQ73UvydPbg1QvDJo_nfADJjF_JWyA79BKJZFfXaID7sKxTe6uQaonf46_ObGQraBBBp2Y-D20962gsSvdQ_X4jm0wNKZiiy9LjwUJ6FHYFn7bhLUUj43QjrUvzxkCB6igxZFz6-VhMihqSLYs3tfF4FJwTa0UpLnO4hqdTg6TPVhrSbNFbSWO-qG2xrEVG-pyXt7DpKHcb1Fb4DkSBT2nPfy4T7jq1pd1RB2IXV_Y2V_VfPVSxqUv1ZKTrJ9QfXVfovrdupf3z-Ovrawxf8zf5tlaVfZpdLOBOKrG3WldBDUWmd3oRUSh9vqwoiWnbGq87LmPQFdntnGn3hzqsIeYlZCxJLaqH0ANUGIgQU01zwZqJgJu6G6ESqolwyHVf5z_TkIGT16kZRg9YNgkUFTUNCOxb0qDJ7b8T1r3_TlRjJm9KV64sMKGk36zeY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71382" target="_blank">📅 23:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71381">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088801b967.mp4?token=HnLbcj2nc3SAzfo0iwtlBncD62C9jXCMoQEvmyjRBBAHORuJwmLhl8_-6TdY9QiiWaEvm0ouJE8PRHUGpEoMTJA3ogX2el3tLXiT2iDOJSA365YOo2cMq-HutFRRptWrnjCZp955Vw4hve1FZWrHVOz-nI5iZFATWeVnr-spXNXaZ9QoKd5KXl_ukmnsA2jWkZ1aOuwvu_B6mZjns-wiQsz4CDgp3v2EQ4mx6lwrzLCfGEXYAgZVuOab0xDaOMVJpfwtBPekDo4ApuEnVhP9VgA-EiG9kDgWI9tdociMI9xQ8tKNuFtmcQ9Ixoc9GOJ7xbn_4Lz1rRm6eWYB-nnMtkHESg6lEmmg5Zmdt7Bs71EEsBoYb_zUPlfGHafNze8pDvdZGR5VHlmpO0_G1IPJKkbjy3ilxoP0C0DPQpECLQ5GDYZCJ3RqM1skWnxvWa0mHrAjyYUzU6Qw6at2cAoHd3u7_Tcu6hqBSTtf0CCosv62RDWIe6KriYkSicdgW9DjITU3h7v-5ETqWweSCaRu1Di8jx8Bwy3fcms_fh5TnompUbEVZHhsxw1JZk7MlVZ78mDqWT0CkCsiRqUgA1LUS3adx2mOSUYWGBYcWvC1lqlIzGTRVO0GFK9ERRdDdjUfV9jwMFdrnrJoZAhon9pzaOMxyffOW7Wq26OLeD1POlU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088801b967.mp4?token=HnLbcj2nc3SAzfo0iwtlBncD62C9jXCMoQEvmyjRBBAHORuJwmLhl8_-6TdY9QiiWaEvm0ouJE8PRHUGpEoMTJA3ogX2el3tLXiT2iDOJSA365YOo2cMq-HutFRRptWrnjCZp955Vw4hve1FZWrHVOz-nI5iZFATWeVnr-spXNXaZ9QoKd5KXl_ukmnsA2jWkZ1aOuwvu_B6mZjns-wiQsz4CDgp3v2EQ4mx6lwrzLCfGEXYAgZVuOab0xDaOMVJpfwtBPekDo4ApuEnVhP9VgA-EiG9kDgWI9tdociMI9xQ8tKNuFtmcQ9Ixoc9GOJ7xbn_4Lz1rRm6eWYB-nnMtkHESg6lEmmg5Zmdt7Bs71EEsBoYb_zUPlfGHafNze8pDvdZGR5VHlmpO0_G1IPJKkbjy3ilxoP0C0DPQpECLQ5GDYZCJ3RqM1skWnxvWa0mHrAjyYUzU6Qw6at2cAoHd3u7_Tcu6hqBSTtf0CCosv62RDWIe6KriYkSicdgW9DjITU3h7v-5ETqWweSCaRu1Di8jx8Bwy3fcms_fh5TnompUbEVZHhsxw1JZk7MlVZ78mDqWT0CkCsiRqUgA1LUS3adx2mOSUYWGBYcWvC1lqlIzGTRVO0GFK9ERRdDdjUfV9jwMFdrnrJoZAhon9pzaOMxyffOW7Wq26OLeD1POlU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
لطفا شهربازی که میرین هر چی رو سوار نشین؛ بعضی موقع‌ها همچی مناسب نیست و شیطنتتون گل نکنه بخواهین یه تجربه کنین.
این فقط دیگه نریده بود تو خودش...
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71381" target="_blank">📅 23:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71380">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0632abba0.mp4?token=pBur4a-deGVXVXT6sfGvL_s9QFpgv74GPzU4FNIGop-cbbo_KVYVIsA35yWY6nkzQb1GapEpHMfWXsYxvCosKs0H5-aFgtNKFF72lUqKJi0GBp-soBkeJD5I67jK57hlTHNfei56EOdTpxttlaOUkfzOKySPIFo-mIU7GFOGXCYqGThP_tYWsFCcRPzKfLbZi44jk8Szoi5wqZ7z1-OtwgU4KQ4sskFBa3CLYVWNmNUv30DPPza8X8i5TU2TOaeoqMQ87bMO8ue5VpoL1vB7EX4ZH_wvlWjONz0nhe5n2IXt28Zi2Fb7DFLtltF8XHlUxmc8xITH7k-vW9TPna1owkasB1Lyo07PASVBFJOlmFXWKe3z9haj__PtuwdaKZBtXomIHr4LlnJVA5ZaJFUa9VmEHVH_OnwHz6YzTu_TsirqpVpjjoEaf4FNxkjAOolpgBj-m-QIpKse0SeeaUNvzLlAo4P_0_O9TS68TuPAzXaszez5ecF1jN9fpVQlLRPcs36O6vUh38jAKSd0yhPXYFWTz3eXEZ0HXyDxgDQ53YTEBUHlVMNpGDEXOQzZAfX15EY079OH79x0wG2iDbZcd8XP8QoMnZsZGz70aWzWlEV5H4mdcv-KWGjdTPxsjXGQikyqqbLXHIclv6IbGoWXgA7XMMRm6LgpmU_reB44IdI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0632abba0.mp4?token=pBur4a-deGVXVXT6sfGvL_s9QFpgv74GPzU4FNIGop-cbbo_KVYVIsA35yWY6nkzQb1GapEpHMfWXsYxvCosKs0H5-aFgtNKFF72lUqKJi0GBp-soBkeJD5I67jK57hlTHNfei56EOdTpxttlaOUkfzOKySPIFo-mIU7GFOGXCYqGThP_tYWsFCcRPzKfLbZi44jk8Szoi5wqZ7z1-OtwgU4KQ4sskFBa3CLYVWNmNUv30DPPza8X8i5TU2TOaeoqMQ87bMO8ue5VpoL1vB7EX4ZH_wvlWjONz0nhe5n2IXt28Zi2Fb7DFLtltF8XHlUxmc8xITH7k-vW9TPna1owkasB1Lyo07PASVBFJOlmFXWKe3z9haj__PtuwdaKZBtXomIHr4LlnJVA5ZaJFUa9VmEHVH_OnwHz6YzTu_TsirqpVpjjoEaf4FNxkjAOolpgBj-m-QIpKse0SeeaUNvzLlAo4P_0_O9TS68TuPAzXaszez5ecF1jN9fpVQlLRPcs36O6vUh38jAKSd0yhPXYFWTz3eXEZ0HXyDxgDQ53YTEBUHlVMNpGDEXOQzZAfX15EY079OH79x0wG2iDbZcd8XP8QoMnZsZGz70aWzWlEV5H4mdcv-KWGjdTPxsjXGQikyqqbLXHIclv6IbGoWXgA7XMMRm6LgpmU_reB44IdI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71380" target="_blank">📅 22:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71379">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f6c19e60d.mp4?token=i5UAizQFPg6V6KN7djTZ9BQrpMUIxCyACEaAwp28EdmTrdLzhtMbNxlnZo_y1HvWM-10C8PJ-BLQITHjL315GmXxIdJpGKq3i3yQuKaQSOIwkXt71Hso4Ea5Ax0QfTsEMXiXkviQS5JsnZs4MjQdM8fVASwQyK2lXHmYxC2G8K1Vq-dTyVnH8W33dfeXROfE2KJIowu1CCirAhEWE5ovXAO89uLBXp5vaD6zzL3KkJ7H7tEhzm8KQXRfj6XD62uO3cMBJNjY2r5kNgGw-I2ftjGB7teFLkuNkoAIzm7uq8-MivRX1p4sQq7IsODb6Mq1AKfeFfyHMZ6cjj-uSOOElg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f6c19e60d.mp4?token=i5UAizQFPg6V6KN7djTZ9BQrpMUIxCyACEaAwp28EdmTrdLzhtMbNxlnZo_y1HvWM-10C8PJ-BLQITHjL315GmXxIdJpGKq3i3yQuKaQSOIwkXt71Hso4Ea5Ax0QfTsEMXiXkviQS5JsnZs4MjQdM8fVASwQyK2lXHmYxC2G8K1Vq-dTyVnH8W33dfeXROfE2KJIowu1CCirAhEWE5ovXAO89uLBXp5vaD6zzL3KkJ7H7tEhzm8KQXRfj6XD62uO3cMBJNjY2r5kNgGw-I2ftjGB7teFLkuNkoAIzm7uq8-MivRX1p4sQq7IsODb6Mq1AKfeFfyHMZ6cjj-uSOOElg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شاهد حملاتی در تنگه هرمز بودیم.
🇺🇸
پرزیدنت ترامپ:
خب، این حملات... این حملات کار ماست. ما 9 تا از کشتی‌هایشان را از کار انداخته‌ایم. بله، می‌توانم بگویم که این حملات از جانب ما انجام شده است. اما... و خواهید دید، خیلی بیشتر از این‌ها خواهید دید... وقتی که به آن ضربه بزنند؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71379" target="_blank">📅 22:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71378">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c27e89aeff.mp4?token=BYj5ZDcfcslyuQXV_tY2NHd7ME7UMGefEPksdh_MjCJWgf5UYJb75I7zQp9nKHUXS74xIADWhSz0229SQBeNCpSxXgg_GRHsTfildTm9o7MQ7_AfnwU3d-VydE_Cz6zI5z5Df0vcioIG3oIuKyqcZjXbritf215UNwIqprszhggvdbXaBoy2Zg-TwIiFfY5n926DrWVNClhOVq8QPwkUC0NFT6Dm3ifX8u4BvOrWdkoYnBbiBH2TFZu1WparJD881Q9OkCs93W9hJGcjJ_HUjS0Y09KLcnkhU4c157SbQokapbykpEeAn6eX5IxxN_US9NuxEUlqZ9qWyzFiXQYL_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c27e89aeff.mp4?token=BYj5ZDcfcslyuQXV_tY2NHd7ME7UMGefEPksdh_MjCJWgf5UYJb75I7zQp9nKHUXS74xIADWhSz0229SQBeNCpSxXgg_GRHsTfildTm9o7MQ7_AfnwU3d-VydE_Cz6zI5z5Df0vcioIG3oIuKyqcZjXbritf215UNwIqprszhggvdbXaBoy2Zg-TwIiFfY5n926DrWVNClhOVq8QPwkUC0NFT6Dm3ifX8u4BvOrWdkoYnBbiBH2TFZu1WparJD881Q9OkCs93W9hJGcjJ_HUjS0Y09KLcnkhU4c157SbQokapbykpEeAn6eX5IxxN_US9NuxEUlqZ9qWyzFiXQYL_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
کمی بعد، اما درست بعد از انتخابات، چون آنها دوست دارند اوضاع به این شکل باشد، اما درست بعد از انتخابات، قیمت نفت رو به کاهش خواهد گذاشت. قیمت‌ها پایین خواهد آمد و فکر می‌کنم قیمت بنزین را پایین خواهیم آورد، به زیر ۲ دلار در هر گالن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71378" target="_blank">📅 22:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71377">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/34c7f74659.mp4?token=NBNmLCCdQkqJVbn20bRJXswAXBF9xErgpIkcGNXDLHNYD8_uLvbVwYSn4FXg2J37rE-1kQ2odXYxPz-tlc8IN6Eg9tp4Yl_YVkDwDLGpNkRhWb5YXcN1e1bx0TJy1XAHdILB7KrWrDug2isC4dw91atl1ap53ptH_fPio9T35QFQmCKtCWGJxGr6YuKXNgAkugqD28w8O6518MSfhMVRsy7ycBTWPW9gbsV-1x2OCgpqOSzb5GQV6YdIUxr2ZJBnIKBBVmk2htBTFMEr_RjE4aVC7tNEhFKwFXcbXGIPXqMEaTnqA9oravMcWTl0KGFx713SwzKCfydKj1Xv9BPj9w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/34c7f74659.mp4?token=NBNmLCCdQkqJVbn20bRJXswAXBF9xErgpIkcGNXDLHNYD8_uLvbVwYSn4FXg2J37rE-1kQ2odXYxPz-tlc8IN6Eg9tp4Yl_YVkDwDLGpNkRhWb5YXcN1e1bx0TJy1XAHdILB7KrWrDug2isC4dw91atl1ap53ptH_fPio9T35QFQmCKtCWGJxGr6YuKXNgAkugqD28w8O6518MSfhMVRsy7ycBTWPW9gbsV-1x2OCgpqOSzb5GQV6YdIUxr2ZJBnIKBBVmk2htBTFMEr_RjE4aVC7tNEhFKwFXcbXGIPXqMEaTnqA9oravMcWTl0KGFx713SwzKCfydKj1Xv9BPj9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه هموطن بعد از گرونی بنزین زد به سیم آخر و از بالا تا پایین مسئولین رو یکی کرد.
حاوی الفاظ رکیک، هندزفری لازم
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71377" target="_blank">📅 22:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71376">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGBjchYjTo1VsigFjIPPFjAZAndno88yVrHfL9EinoHefCoWAUEfAfGrzpZzZuefo-f7GiQcdsAkxqlFsPkiQRv6pL9qWflMkuIhuNOx7ENoVqxeB-rDfQAcAl28iCKtk7vMGbygr8ccbFFMNXfAIJVtvI5_dHhsNjHWQuwGJ3_5UnWhhoBHsw0WH1NjrsW5dgcQ6r0zxUUUVR78Ty0m-S6hC33MvQRej0_eXbdH8Ef7nDGJsuj4ATA35Wl8HqsoUbiLTROR_7Y3sho-Z1gw0D-Fo2UwtHyooqRTRvJuOmYP8TnqH_WFDTYuKXF5Ki38u-7m7VwikZfG_vianrHj9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
🇺🇸
🇺🇸
به گزارش «نیوزنیشن»، دونالد ترامپ همچنان در «بال غربی» (West Wing) حضور دارد و طبق برنامه، هنوز عازم دالاسِ تگزاس نشده است.
ترامپ در حال دریافت گزارش اطلاعاتی به همراه جی‌دی ونس (معاون رئیس‌جمهور)، پیت هگسث (وزیر دفاع) و ژنرال دن کین بوده است.
احتمال می‌رود این جلسه پیرامون موضوع ایران باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71376" target="_blank">📅 21:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71375">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22f299161.mp4?token=c--xFjwwPjfI7-nKX6w09apkVJ3R-tf5EJpbNfJdk2IlpieoZxnIlez5hG5ulUkr9VpnuI9Cdt2VmEzFkGdASSdMskkrb7xkxOnB1_L125P9EabAx6Oe0aY4vlFUZd95i_lC3Gb1bP5CTduco4VAz0JqjU5lOKrinQZdprWZCk4_nfx4jXAhpJ9Q507Xx3EwCTGud4hLUeJDUERrurSpPucwdltL-ssigFVs8UnTPODsEKFsdwqVrHgU1g6wMU-t4BAcpCnJaI0g4NVnk0zO7UVd8--aQR8-Mtc1T-XpQZH7PgE06eb46TtBTWnOoynJGvqiYRihkxYkwghHZur9Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22f299161.mp4?token=c--xFjwwPjfI7-nKX6w09apkVJ3R-tf5EJpbNfJdk2IlpieoZxnIlez5hG5ulUkr9VpnuI9Cdt2VmEzFkGdASSdMskkrb7xkxOnB1_L125P9EabAx6Oe0aY4vlFUZd95i_lC3Gb1bP5CTduco4VAz0JqjU5lOKrinQZdprWZCk4_nfx4jXAhpJ9Q507Xx3EwCTGud4hLUeJDUERrurSpPucwdltL-ssigFVs8UnTPODsEKFsdwqVrHgU1g6wMU-t4BAcpCnJaI0g4NVnk0zO7UVd8--aQR8-Mtc1T-XpQZH7PgE06eb46TtBTWnOoynJGvqiYRihkxYkwghHZur9Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🤡
اوستاد خوش‌چشم تحلیل‌گر ارشد صداوسیما:ما به سوی یک درگیری تمام‌عیار و کوتاه‌مدت در پاییز می‌رویم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71375" target="_blank">📅 21:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71374">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rNOiIN7V-TVXvn0P-7r_pAQ_g4R1viyxVnoX3Z7c-zA0_RLjhJ5DgLzyPpAflCN4BpQGcotdMoh5Bw7H40w6YCf3JsXu5e5C_IkGW47A7A1Z0w4iJGXnYzH_AOkwWQE8cNk78D01dLSPoyxz0BqVlZUrlzfXSvQcTwKUJibH6lBQE4P_NQHozAiwhPdRGzQrBvBFXz-yEfmrSXA_HmRWgkFV3bk2Z2KtOzXqOhKupwuvlICCp0C1F_JdfNFo0DLDo_lY1DBRrFKVJU60KoGc1OKYjtMyieRh9HHAisSw0NEssvmOlCK93HsXqwR5Y1imZ-wqiW49TMouvVy7_sp6RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
تصویری زیبا از رعدوبرق دیشب تهران.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71374" target="_blank">📅 20:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71373">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69c9063c46.mp4?token=GvL6ypJg7W46w0Xe0gX_Y3CfRqJ2yb2gXRiZcxqboloUIdHRxwBL_W8OCZKkyPzhcPqu06aggrc0ol07_I9N178FpFSW06E6tDdN6GQKU6kDuzs75BmBpTjaF4bxtgGvfY8LaLYcfUux4gyjA8bnrKIQIOuccXV46paMn_ZyHugDEsddC2DVkpwjjL1eT6HxtXRj1QT_yaQhioQicvNle_Kxa96F_NPPi6asaC_pZ9KaK-eNEc-u-pEyAjHgiGWqDTfsepz2f2NQacbPj6H5epbbnA1le-nFfIgtMAl8Fh-7tOhtyeKfziFB1J8LBmJHeMDyKxOosbWoh3Mk07HofQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69c9063c46.mp4?token=GvL6ypJg7W46w0Xe0gX_Y3CfRqJ2yb2gXRiZcxqboloUIdHRxwBL_W8OCZKkyPzhcPqu06aggrc0ol07_I9N178FpFSW06E6tDdN6GQKU6kDuzs75BmBpTjaF4bxtgGvfY8LaLYcfUux4gyjA8bnrKIQIOuccXV46paMn_ZyHugDEsddC2DVkpwjjL1eT6HxtXRj1QT_yaQhioQicvNle_Kxa96F_NPPi6asaC_pZ9KaK-eNEc-u-pEyAjHgiGWqDTfsepz2f2NQacbPj6H5epbbnA1le-nFfIgtMAl8Fh-7tOhtyeKfziFB1J8LBmJHeMDyKxOosbWoh3Mk07HofQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71373" target="_blank">📅 20:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71372">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fc965eb9f.mp4?token=A8aVUNQCSIB7c9l5MXtXcf2JTvPF2HYGbgBJrYQK6xYSWi-1tlHrxBzuUQmsfpXVXHgnIwhikAUguxFwkWvuNhxLXw9yAQnab6iZjJmEfeK85mDZQG-k-FSvLRISOxvTr8TMNJoBcSi49L6k4gvfzM_sjcMHeQrJPEZ9DyvCz_iGKOhU3B2cHcGDyKiWufMtbgQxYq_h1PPDpzxuAntanECiyiThtNx4zeOhED1snx6JezhhwyMRKEP6Hone4rrmEKcTi8t2DzKxpcFnZNNoIQJmZZ3WAa4LW6fGjhhPLa0Soe1gAmrRrhwfFwCPgN-f4dk3xqWHdaQhC-FTfikuBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fc965eb9f.mp4?token=A8aVUNQCSIB7c9l5MXtXcf2JTvPF2HYGbgBJrYQK6xYSWi-1tlHrxBzuUQmsfpXVXHgnIwhikAUguxFwkWvuNhxLXw9yAQnab6iZjJmEfeK85mDZQG-k-FSvLRISOxvTr8TMNJoBcSi49L6k4gvfzM_sjcMHeQrJPEZ9DyvCz_iGKOhU3B2cHcGDyKiWufMtbgQxYq_h1PPDpzxuAntanECiyiThtNx4zeOhED1snx6JezhhwyMRKEP6Hone4rrmEKcTi8t2DzKxpcFnZNNoIQJmZZ3WAa4LW6fGjhhPLa0Soe1gAmrRrhwfFwCPgN-f4dk3xqWHdaQhC-FTfikuBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇦
🇾🇪
ساعاتی پیش، چندین حمله هوایی عربستان سعودی در حمایت از عملیات «شورای رهبری ریاست‌جمهوری» (PLC)، مواضع حوثی‌ها (انصارالله) را در جبهه مأرب یمن هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71372" target="_blank">📅 19:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71371">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71371" target="_blank">📅 19:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71370">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4ebfee62.mp4?token=sQ-kB8zsbUe9O5OL4U0NNApGJ-fy3U5rO-z8IDIF-cHCxvOpW-F84FkBaxK3aXt7P86ZPOgdg7DhEy8WdtYb1VJeyKfn3zLDoFCXZ2eiZMqlkQPbOc-34QMv3wkcfMYdSoRGBsI0GSYiNg5V1jqPAVnYyEcesSm_q-STvKyRlBja8vvGG3pUUuXo5y1BjghrEARiG1_behb6IGTIwyqh_Bfrl8txnNIp7ZDMDLFP1NLisjwW-JP_ZpjkVeZ9KcCZ0nYFn9cdSRS8Y1c0sFbmzItfDPpLE-NKjT0LFuYHVJKPLrd-hUS3VeLrzXqE1n5H_NB7Jgv70ilJK3nHDtxPgqAIDyxRaO5-3WQOrttPODZnbH64PPzm_bdeLxb0yzWVE7_Sa5XTVkyVuZrhaTxtuWdyYTvwijQzryxNsIZcLI9hVLtAt2CrYtnC8TZ_WTuoYEKhZAWpMb5tBZm7h5mtXntmt0iFaS7w_iRrEjkc75sir_ZY-wMrtp9V46OEsrzxzfhYRJYPzl3MvFKX2aPx4H8x4vQdFjS364_mZ5iv8jiZ25XA67PkWhne1mqtpNBkd7rtpdAaim8LWqUJNeTAGfxxCyB-MrKneMwMRzZuiwo8eMHgICPkKqCKeLzNgBUOW863Yam0VH7x78DRyy7XcPhuz9cBzcUTDU1Jqm78nIs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4ebfee62.mp4?token=sQ-kB8zsbUe9O5OL4U0NNApGJ-fy3U5rO-z8IDIF-cHCxvOpW-F84FkBaxK3aXt7P86ZPOgdg7DhEy8WdtYb1VJeyKfn3zLDoFCXZ2eiZMqlkQPbOc-34QMv3wkcfMYdSoRGBsI0GSYiNg5V1jqPAVnYyEcesSm_q-STvKyRlBja8vvGG3pUUuXo5y1BjghrEARiG1_behb6IGTIwyqh_Bfrl8txnNIp7ZDMDLFP1NLisjwW-JP_ZpjkVeZ9KcCZ0nYFn9cdSRS8Y1c0sFbmzItfDPpLE-NKjT0LFuYHVJKPLrd-hUS3VeLrzXqE1n5H_NB7Jgv70ilJK3nHDtxPgqAIDyxRaO5-3WQOrttPODZnbH64PPzm_bdeLxb0yzWVE7_Sa5XTVkyVuZrhaTxtuWdyYTvwijQzryxNsIZcLI9hVLtAt2CrYtnC8TZ_WTuoYEKhZAWpMb5tBZm7h5mtXntmt0iFaS7w_iRrEjkc75sir_ZY-wMrtp9V46OEsrzxzfhYRJYPzl3MvFKX2aPx4H8x4vQdFjS364_mZ5iv8jiZ25XA67PkWhne1mqtpNBkd7rtpdAaim8LWqUJNeTAGfxxCyB-MrKneMwMRzZuiwo8eMHgICPkKqCKeLzNgBUOW863Yam0VH7x78DRyy7XcPhuz9cBzcUTDU1Jqm78nIs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پسر‌بچه ارومیه‌ای که چند وقته به شدت ویدیو هاش وایرال میشه موزیک جدید داده بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71370" target="_blank">📅 19:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71369">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696aa56e23.mp4?token=F4kW1sC9NbybkpJf3P7f4LSKXBzReg2t5TopkSswMZq7c_RzDljKPgj4dXfWczl_YX4t92m7vqcSLATtEBMFb4idt1NXZsSAlfyXwE5g6Dj8aQ5oR3X-6BEyxrwh2tCCuo6sg3IneZV7V8jkLhVy7xoNbayqSE-OcNoA-FoWxvockqZjFp0IrtaHihNmr-lQg5dtUYzZEtXy8iV0pTRDDA_Zckft1wWcdTykEnG2ahBohWGcyKJV4LuMYuR_8Ptzxj4oFH2KP_9N-05ZAjWD8hVk8r_qZUikU4gv9dSU0IFlav096DBCJhLfL1oL0IKQu7vs-RJPCHQsjAOUBkYdKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696aa56e23.mp4?token=F4kW1sC9NbybkpJf3P7f4LSKXBzReg2t5TopkSswMZq7c_RzDljKPgj4dXfWczl_YX4t92m7vqcSLATtEBMFb4idt1NXZsSAlfyXwE5g6Dj8aQ5oR3X-6BEyxrwh2tCCuo6sg3IneZV7V8jkLhVy7xoNbayqSE-OcNoA-FoWxvockqZjFp0IrtaHihNmr-lQg5dtUYzZEtXy8iV0pTRDDA_Zckft1wWcdTykEnG2ahBohWGcyKJV4LuMYuR_8Ptzxj4oFH2KP_9N-05ZAjWD8hVk8r_qZUikU4gv9dSU0IFlav096DBCJhLfL1oL0IKQu7vs-RJPCHQsjAOUBkYdKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز تو بجنورد، فردی که سال‌ها با معلولیت شدید تو یکی از خیابون‌های شهر دیده می‌شد و مردم هر روز بهش کمک می‌کردن؛
به محض دیدن پلیس کامل درمان شد و درلحظه به‌طور کامل کاملاً شفا گرفت.
طبق گزارشات این فرد روزانه چیزی بیش از 20 میلیون‌تومان درآمد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71369" target="_blank">📅 18:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71368">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8d769b56.mp4?token=Djc2buSiJ0pCKkotMSHkZt3L0-kUTvmZ-c7GBLMj3R66acEyp0_GuCni1L1AUdsMG9rnQHlB2tIdYdVM--IN3FOhR8vpMo34rANzVOCE9pzfJtJpYlagqor2zutCOqBHMChSPPdrQQ4S6gcVlEay2a6PVg1CNvHay3O7Mv4XfX3PVH7S8YcX5dLQT7vabGTT3It52Rr_fCrzT9MtKAXP1X2Rg_0QmeUTulXnu8frH8Ynn-uk9DgU_76AdTYvzr-zcNKS_KT11xjjW-HwjlV488U0dAzzxvfn8T9bvQPFOTVuYllFbe4xXvOtr7_-uR8fLfYjWsphkacrPd1AnNxCJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8d769b56.mp4?token=Djc2buSiJ0pCKkotMSHkZt3L0-kUTvmZ-c7GBLMj3R66acEyp0_GuCni1L1AUdsMG9rnQHlB2tIdYdVM--IN3FOhR8vpMo34rANzVOCE9pzfJtJpYlagqor2zutCOqBHMChSPPdrQQ4S6gcVlEay2a6PVg1CNvHay3O7Mv4XfX3PVH7S8YcX5dLQT7vabGTT3It52Rr_fCrzT9MtKAXP1X2Rg_0QmeUTulXnu8frH8Ynn-uk9DgU_76AdTYvzr-zcNKS_KT11xjjW-HwjlV488U0dAzzxvfn8T9bvQPFOTVuYllFbe4xXvOtr7_-uR8fLfYjWsphkacrPd1AnNxCJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بازی مناسب برای جوانان خاورمیانه ای:
یه سایته یه بازی ساخته، میری توش بمب اتم مورد علاقت رو انتخاب میکنی و میزنیش تو شهر مد نظرت و بعد بهت میگه چند نفر رو کشتی
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71368" target="_blank">📅 17:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71367">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCrMBgiod3AAtxGHnbsryD4SYpptlUHSFRa-V4eusO2gWJ5zmVQkXtKk598FWyhcjiKI8xeuJYQXCN74ixaiUqzTG4vapo1m24_HDaLh3wY802KwzJppVwBZvhy3RYZSjRjDqJ4mIFLz2wtb828r5AsantxirbwjN_ZEua6FxsLRr0nXjSdfH_HUNAbvusccorzWJMM7kb4daWcd55XPvOa-GKIIxMEQVE8bXRx1Dg1y_Bf7s_rXWXEGHoI_m_dkxg51qyNqkxsDxT81JjOMX_2yW01Rxpksj4yxxY6jnLaNRsLVif4_VqZKHK1b2MpAUEyD_hGONBO5vBViXNFnYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71367" target="_blank">📅 17:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71366">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6e3b3343.mp4?token=A0YdovehugeydJExYFcX_1NGfFkb9_kFDCrNGdWS5Ft-yYcQlh_y_w4QbtJbsLSH2D6wgQG-7FWrsgJ600R9JrWGU4ri9NuE7JQUoji8OCDdlsJhOjid-IrFGR2TtNyeBQZSicQd5mh4MlIpz6Klw4_yMfgWNlwu2OIPx-viH0Iz4LA1HiAOolbhPiFEhMgDCkvDl5q3x3Fx1xoYE9qAwBDmJbBP5XMYGStibT0jvZH3Uat9sIv7-PBlKzZm5rEvbAH6YWc3_ubkGhaEcXB0ZV_GWL3NmTY1wewejRivFwE54IbMWTucH68doXXH4huFMzR-CyP0p7UHY8ap5RQDBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6e3b3343.mp4?token=A0YdovehugeydJExYFcX_1NGfFkb9_kFDCrNGdWS5Ft-yYcQlh_y_w4QbtJbsLSH2D6wgQG-7FWrsgJ600R9JrWGU4ri9NuE7JQUoji8OCDdlsJhOjid-IrFGR2TtNyeBQZSicQd5mh4MlIpz6Klw4_yMfgWNlwu2OIPx-viH0Iz4LA1HiAOolbhPiFEhMgDCkvDl5q3x3Fx1xoYE9qAwBDmJbBP5XMYGStibT0jvZH3Uat9sIv7-PBlKzZm5rEvbAH6YWc3_ubkGhaEcXB0ZV_GWL3NmTY1wewejRivFwE54IbMWTucH68doXXH4huFMzR-CyP0p7UHY8ap5RQDBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر مسی رو پیدا کرده بهش میگه بگو علی تولدت مبارک
😔
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71366" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71365">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71365" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71364">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/as6w2wIf2m3RlcQvoIHR7VI0mNPz1-liWmG17TY5haVDDzppgN6MbuOU9Hv5XgIRMJ0O1Lcjv7W5xMcK69mYKPqXjPFLosBFHr-CshWtBhbpI6phNuNfTc9y8ImmnSiP38LSi35z3-87uTdclg5Fae-_4ocuZ6fgWjooMSpmS65vCy7q1VXHcXMNczsuDb3Y0CgBusRiRJ-32t8_RVVGQKVoSRc0-AAkaU8vQ1YurkK0Or9rjsvqZkxZarCQwlq6cqw3Lj3P2savsbQPClY1BfE4iZip5b8l7NYp02Tl7FE2OmIzOxTcjtxcM5s85pE_ATTh-CETE7M1GjSiD-hohA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71364" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71363">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146bbc1159.mp4?token=hHuoz8uQgK3qBOENQsSa8Cvi20snGdWRlpxRtS0JTeyW2EsYk00IJMXxKtCsrT5sN6Vvyh-po5Rzib-SBDF6FWrytK5sqNb1kwtDaoKh6cBa11zthOypYvelqaOY5ysy6Opswm96E3SAB1OHttTIY1zBeOrj_CEQ9904Vg11747TY3balMTHb_UAcmj9UHWUr5tujKjRY5UlpaRVsXeoE06bOuPMBLkcOtT-xMmcyhVtBfvD3bta1RjrZhYxI8trcmCb5v7ai3Htfd1GwCmOBv4UWsrMbLFh03H8Z1ONoQVkDChMvuwQHyttxfQDJ3ebgaWqvBiwmV6pRqPY4CId3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146bbc1159.mp4?token=hHuoz8uQgK3qBOENQsSa8Cvi20snGdWRlpxRtS0JTeyW2EsYk00IJMXxKtCsrT5sN6Vvyh-po5Rzib-SBDF6FWrytK5sqNb1kwtDaoKh6cBa11zthOypYvelqaOY5ysy6Opswm96E3SAB1OHttTIY1zBeOrj_CEQ9904Vg11747TY3balMTHb_UAcmj9UHWUr5tujKjRY5UlpaRVsXeoE06bOuPMBLkcOtT-xMmcyhVtBfvD3bta1RjrZhYxI8trcmCb5v7ai3Htfd1GwCmOBv4UWsrMbLFh03H8Z1ONoQVkDChMvuwQHyttxfQDJ3ebgaWqvBiwmV6pRqPY4CId3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
دیروز تو سمنان عرزشیا برای مجتبی خامنه‌ای جشن تولد گرفتن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71363" target="_blank">📅 16:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71362">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ece16841.mp4?token=GokGvW-bZ7cqZyBcEKSGkGXYvy3BavgL29oqacy6VulXGoFwh5KiymuL12NDHLN2atatr2d8qdyYnjMoswkA-AZ33A2VwgaZaxgaZxH-c3u9LxaM01PGOx6gysKkiOwqiY0gY5ekLHcjQhaVrNmxrAg2EqJNRYVKlE3hbpxEg1hE3OowXC1KtttSuw96KtX4QzSG4RAgk6o7jXHfFLkL_Z9p8k7fS6dqWxayTqVhTCrGzOYlLHtU-m6a4ECZnnx1AHg6AWEyfRAp4zI7BZfZNGaA3lid1y8KnD8VqgRYYQZw6maUUG_vnL4m9iiYntORUbJNmoklvX-wAnvbgmOCRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ece16841.mp4?token=GokGvW-bZ7cqZyBcEKSGkGXYvy3BavgL29oqacy6VulXGoFwh5KiymuL12NDHLN2atatr2d8qdyYnjMoswkA-AZ33A2VwgaZaxgaZxH-c3u9LxaM01PGOx6gysKkiOwqiY0gY5ekLHcjQhaVrNmxrAg2EqJNRYVKlE3hbpxEg1hE3OowXC1KtttSuw96KtX4QzSG4RAgk6o7jXHfFLkL_Z9p8k7fS6dqWxayTqVhTCrGzOYlLHtU-m6a4ECZnnx1AHg6AWEyfRAp4zI7BZfZNGaA3lid1y8KnD8VqgRYYQZw6maUUG_vnL4m9iiYntORUbJNmoklvX-wAnvbgmOCRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مراد ویسی:
جمهوری‌اسلامی سربه‌سر اسرائیل نمی‌ذاره، چون می‌دونه اونا نمیان "نفت‌کش" بزنن.
اونا میان "نعش‌کش" راه می‌ندازن
.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71362" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71360">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBtC34mpGmiSxrADZdiCRA7mlUCVprzJhM0v5MdCyhQJR077Y67jlCo2TiC1zj9UaFIHKSYm_XAKc6C5mXHytuw3sxtEQDgaAxPyJXsepDi52XveqQQilP6EI0sfC6KW-UC8hbBqftH0COTD5gNdPQNs9rvcABZ-CKW_eC8pouCrUh6EeKctjjPVkCXARaHr3AUSVm-GdcFD7RldCwQimjLvjO9kvclVmLKViZYglQ_aehhEIX7rXP8146mmZkVS5ihnBi97J5dOZWYgo-QRRJD_PngKwCaBpWIf7tHA7kmu_wLnbl9BpD9N5vWfbymnuFoW6MqeaUfVg69_Dfcn-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f399e219.mp4?token=lgInCj1Xvn88BI4UgsTkI9J4Aq_h3p1_8pCjB5_sGrHclPgkr-SZt1IqDaHpsOcV9YothdpBh4HPGOAsQaRMC9wG1-i1bX5JlhguFLUe553HcIqoPq0Nl84RWVhan8yOEwjWZMWYOqxj1CHS9Rr6_mZ5VIy82ivyqY2W_4QtCHX9RI82_S5_Ht0JzjRmoC6taUmc8ViB6BPRQOiedf2CExcEQo7d1sUYIXKGJaBqGtLaozZoneRvvO7DneZK_mMwxDESuZMhYzQoZK4K9cjfiPEayU1UHvZTYgBUFGJtkxXf6vW-G_uy9S_xybADP-5qGYupRe9uvGYmILlA7D2KFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f399e219.mp4?token=lgInCj1Xvn88BI4UgsTkI9J4Aq_h3p1_8pCjB5_sGrHclPgkr-SZt1IqDaHpsOcV9YothdpBh4HPGOAsQaRMC9wG1-i1bX5JlhguFLUe553HcIqoPq0Nl84RWVhan8yOEwjWZMWYOqxj1CHS9Rr6_mZ5VIy82ivyqY2W_4QtCHX9RI82_S5_Ht0JzjRmoC6taUmc8ViB6BPRQOiedf2CExcEQo7d1sUYIXKGJaBqGtLaozZoneRvvO7DneZK_mMwxDESuZMhYzQoZK4K9cjfiPEayU1UHvZTYgBUFGJtkxXf6vW-G_uy9S_xybADP-5qGYupRe9uvGYmILlA7D2KFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⛈
⚡️
ویدیویی که یک هموطن ساکن مازندران از وضعیت چند شب پیش آسمون مازندران منتشر کرده و نوشته؛
تو تاریخ مازندران چنین رعدوبرقی که بی‌وقفه ۳ساعت بزنه نداشتیم
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71360" target="_blank">📅 15:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71359">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncbtoDlXHWDsh-gIOHlEueOijiTI2chTGEJw_e7As9v0TAFlmu2rddczogdKJqkUXVs-7lS0cXqO0M9wdU3ewbJtirivVFWP-hOz41tusA56iSqZ49qj3JmTnrLWw6waWbSuNrkjsP2gcOpv8UofubLr3gpxxXLeJSgOInYP9-0kQZ2y7SKH82ohCugYiqj-VksKco0qbA3MyWYXsIhmeMoIra50NSK9O8gLnM7wT5X-I_wQ7_1_PmcOwOSfvuUw5ibaHYIRYc9zn3K6zeKTITuiq_82oyXB_ecQ9JALMQtTrR4XHrQJ1Qlb0uYS-kHnaUk6x46UfpxvKF8IJzfOAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71359" target="_blank">📅 15:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71358">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf337ab4f7.mp4?token=YcxFg9C0ZO7NLP9FQ4Ed0VpRYMnQHexEgsebuldUEEo0znhRsoEH2jKjj2ZafrxwH3isLfJIUC_cuAEkgwvRRsxgUvQHuSbgRboxJuWqgVg1_5UwBgcmzOL-fTpTTKqiXFcMtAhomTB6Q4cpxIYMzaWZP4MoN5EBh8ndJmFaJVq8F4Lf8XGRHj-XHndj7sR300qtBWuR3I7GHE_tAxkQ6BzBpE_uHrtzsjdPUPIEp5i6WkJuQ_1YakO5qtLA_2LjS3TdH5TwIEVeCiQpUqZFqNNSOgKXiS3y4ZTJL2XxPso3X1teY84Wgs9rud7iFUOpq0PSIBk3kbfc32CWosQt2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf337ab4f7.mp4?token=YcxFg9C0ZO7NLP9FQ4Ed0VpRYMnQHexEgsebuldUEEo0znhRsoEH2jKjj2ZafrxwH3isLfJIUC_cuAEkgwvRRsxgUvQHuSbgRboxJuWqgVg1_5UwBgcmzOL-fTpTTKqiXFcMtAhomTB6Q4cpxIYMzaWZP4MoN5EBh8ndJmFaJVq8F4Lf8XGRHj-XHndj7sR300qtBWuR3I7GHE_tAxkQ6BzBpE_uHrtzsjdPUPIEp5i6WkJuQ_1YakO5qtLA_2LjS3TdH5TwIEVeCiQpUqZFqNNSOgKXiS3y4ZTJL2XxPso3X1teY84Wgs9rud7iFUOpq0PSIBk3kbfc32CWosQt2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
📰
یک فایل صوتی که اختصاصی به ایران اینترنشنال رسیده است، نشان می‌دهد یک هواپیمای نظامی آمریکا در مکالمات رادیویی به نفتکش جمهوری اسلامی هشدار داده به‌دلیل «رعایت نکردن محاصره نظامی» در بنادر و سواحل ایران، موتورخانه آن را هدف می‌گیرد و خدمه باید در ۱۰ دقیقه موتورخانه را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71358" target="_blank">📅 14:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71357">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hs5OqRlsCoiT-niNsfe4PhRU7ucYBx2n32i8zg8fetMog31K4luPSLCYrP8OQ1PIUZ7Vzb6cdcEzZOnzyHp43tmwn0hzaEfWDLNZil2imNOJX4LLEZlb6IVRhsXh5rLjG3Jim4gfOeDLzqv3BL1GY7mbSW8I-XmlEm990W7guAa9GA-EN-WjAKyf9SUMbJGEq5GyLyAPAUEs2aenn8eXV7LfC_Q0u8NHE-loJabjUm_8Zav0DmKd_HuOs0y2OXH1lti-Ff-ZY7PsjkPvsu0ialJ_jR2zwPIHMMuUrjqJzIBNP60cNqdRvG2vVOD38MARC-Wcjnv46lN11Iemkm3VhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارشی مبنی بر وقوع حادثه‌ای در ۲۸ مایل دریایی جنوب شرقی «الفاو» در عراق دریافت کرد.
فرمانده یک نفتکش گزارش داد که این شناور مورد اصابت پرتابه‌ای با منشأ نامعلوم قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71357" target="_blank">📅 14:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71356">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5kvfwIkfUAJVJoX9u6db9oQqDjve7pI604ie4CqPmf_jemMaagrXbHc-GjpG9u2n5B-P7hfvw0y4LSxZZhbrL-CYEiArAlAS5AlkgSAfQpaTNGYVQi7ECesm0zZ89WBmRjdL74mwzgy3SbPgfKOvcYUh6UbPbRK1QPSFw2QBzjonCyxYHFHszgAe1m3-CdmuEo68itJueOSCnyInedfsa_2unZQ163tEVB3upP_J4mg8Tf9Spmx0XjPJKfCfg7os20eTolQCXlkeJjGqMOxrr5vraUdlWYXpF9Av4sE2JzD_0i-Eyhf4TDhM77ZhtjazaYQjM5nqjpIDuJtxMdQhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💸
🫵
دقایقی پیش دلار و تتر به شکل عجیبی تا 241,000 تومن بالا رفت و دوباره برگشت و الان 234,000 تومن هستش...
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71356" target="_blank">📅 13:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71355">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IC9BED0DBb_F4qaGnCNIpIPYJICidHZPRcJG438x5P9BXxn3WA61eAQFMPhi3aKJQwrgp6QSX2FqncBHQ7Vc3CHp2U6BWN9fRfAaBoKQtlPZMMQESS62CpC0qg_rc9tupLvqiwTUNKDcYMXQCURn5Mu5HqlZdz-MSnNTz2w9133Z6a8ZtnwdSwwMw-_McL7gh6HUVuQFt8adMst7Imx18jaRhLdZ_jBcOLeo7PXZa0a9jZKBDJ3DBmmB4xonYKUTV9OQbYHfD5mqVyzHpz9Bc8oxFEdwMZoAdVeqypf3si1YIZ74ikyyoJ8-KOHNEBV_YZ_7W6XtgdNFJXx_BiPaaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
〰️
فرماندهی مرکزی ایالات متحده:
❌
ادعا: نیروهای سپاه پاسداران انقلاب اسلامی ایران (IRGC) مدعی شده‌اند که به دو ناوشکن نیروی دریایی ایالات متحده در خاورمیانه حمله کرده‌اند. این ادعا کاملاً نادرست است.
✔️
واقعیت: هیچ‌یک از شناورهای جنگی نیروی دریایی ایالات متحده مورد اصابت قرار نگرفته‌اند؛ تمام تلاش‌های سپاه برای انجام حمله با شکست مواجه شده است.
در همین حال، نیروهای آمریکایی تنها در هفته گذشته موفق به انهدام ۱۰ نفتکش ایرانی شده‌اند. این شناورها بخشی از یک شبکه پنهانِ چند میلیارد دلاری بودند که بودجه سپاه را تأمین می‌کند و ایران قادر به محافظت از آن‌ها نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71355" target="_blank">📅 13:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71354">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf3721b8d8.mp4?token=UiEdhCuw277dIIIcb2jQU_H_F-vpPNWdrfILF2ZjrZQOvKRQvOPwiHRzFfrodKyP6hpaS_VEkmJlRg6X-rfoaB1ZunNsuxRTgAk5namHzXfBlALTyOe4nGtSAB3UVurz66sbl0PNeZIsXcki_w0aEj2IcttIftvbJoCw16syj0L7nEs878pUZe09WGZ4YQqcmZUlRv6-S0Yn8WaISFRxmcOUASo1PPiBmVCB5WNBhRWSrWyd9DAGCxBGad0Kj-D7KOGid4k8u9yI5bTeDN0FyE6yeCTQnvO-4P65UPAfOsgbOSYHUocjqLdAGpwhA4EsuRkzlCuk4ie0HdF3c0iUag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf3721b8d8.mp4?token=UiEdhCuw277dIIIcb2jQU_H_F-vpPNWdrfILF2ZjrZQOvKRQvOPwiHRzFfrodKyP6hpaS_VEkmJlRg6X-rfoaB1ZunNsuxRTgAk5namHzXfBlALTyOe4nGtSAB3UVurz66sbl0PNeZIsXcki_w0aEj2IcttIftvbJoCw16syj0L7nEs878pUZe09WGZ4YQqcmZUlRv6-S0Yn8WaISFRxmcOUASo1PPiBmVCB5WNBhRWSrWyd9DAGCxBGad0Kj-D7KOGid4k8u9yI5bTeDN0FyE6yeCTQnvO-4P65UPAfOsgbOSYHUocjqLdAGpwhA4EsuRkzlCuk4ie0HdF3c0iUag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71354" target="_blank">📅 13:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71353">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMSoGHw2D87TOnmDtzkf3-2doc2dwihpUBAbLkfBp5BbqRcfM2ikOoJ_ae-YoDWmlzKdo-LliLWWm5VdZw585hFrDXs5lC6gQRLs_U_MDlbRktf8JHFWfYRZTjN4GIraGnomtPhvZVjU7FVoRgvqtOekuBxZSPflSjXLXzINjmqR8xDZ0WdQ30VILqHjyL7DXxptLv-xHP5MJX0aavMhFn3LSD0FCTJhq6cpRO3M0SKVsgFR6QKU26GnylDda6Es_U8YaNxT72RZKthFXF6-m-BewftohXmrLNYmLyZOHX_oKW8TmJ16MUxdqYaVfVpRi9GAgT33Mu8RrpMbaWdicg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارشی از یک طرف ثالث درباره وقوع حادثه‌ای در فاصله ۲۴ مایل دریایی شمال غربی بندر راشد در امارات متحده عربی دریافت کرده است.
فرمانده یک نفتکش گزارش داده است که شناوری را در وضعیت مایل (کج‌شدگی) در حالت لنگر‌اندازی مشاهده کرده است؛ وضعیتی که احتمالاً نشان‌دهنده ورود آب به داخل شناور در پی اصابت پرتابه‌ای ناشناس است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71353" target="_blank">📅 13:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71352">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71352" target="_blank">📅 13:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71351">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfP-eMVXExtuINn3GizcBFhk-xxuPSamQjPe8m-YTZAl_rSbuWlgc6S05ETBWiXdzBKMzxlXJgb2-ZJk7g4-NPpeF8i3EBFzhQhCMoNWIDfZUevc9koicq968LpijS7lR8UFubfiYHf4c-b9RPGjnhaU9q4PfhumD3GBglVSj4XQw6Y3b_gfqz9bBMF8dzeyBkRpGWTVj9Uc55n6fJjq6OUK09MTTBHXQrUqnJGbmlyI2yfzpjznliS5WsVj1FMrpPKNnHHikD30P55ERgx6y8IEfEUf3EPZXEbGKzxi9ThfWaSylTbG8Znp0hX-SxKHaeRkwMiguLai_6IGXiR_mA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71351" target="_blank">📅 13:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71350">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miD_foJd26yiZgDEWM0FLQ_GTggCMYYmQYxZXe6aortWYM-W-fLNppMwAwsNamB__1xIc67gKEdQ-CsGywGsOkphceuSkioZ6-XAlLoq5MANxWOZqQ9GZTDTQrMyUe_h7kz06I20G6297aY011M8CntppPj5Y4Ui6T_ee9cWDVEXpZ3zccoMP5dnPyh_bq0XOWZR_-AseC2BldSF_o2rosPBA89BAhb_kfv2yAyNO_nYJVhQhq0DodLuPtJYbbboGH2vHH9brVORBi3YD34ZL1jamwuS9PEDI1N7rlP9LKAMKtqQ5vGuDJ1pBk0rnnKQscOk6jbvpsO7F-svAqwmqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📈
قیمت نفت خام برنت برای نخستین بار از ماه ژوئیه، به بالای ۱۰۰ دلار در هر بشکه جهش کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71350" target="_blank">📅 12:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71348">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFnmr91i5vvifENGfAp0wOMhnMXZamoEp8PkUUkQY_9VL-h6LMIWlzu789ROezVG7qkWgPusRbZ_n6QP9Up4P8NgfA8yVeOmoyZ0tMi-Rt2MuOqXhbT1AbHK_nU1_I64B-izNvRp8qX0kw3wP6EMHIncOPdqW6uqhSywmTR8iIn0p0xhpxZmQn_RvPGev6-gr4AbaVKVaL1ELePyJPbdLuLpCouzQkBCurpU80NzvMZ05d_PYHN073F0kakrDxyCIWp8qcNRCE3IVgxWsNkRFGNCvdyw2xHFHtOt4oIZGpquZE3iK82TQ4G1Xld_8HL9-R_ZzNBir38NfNv-w4Qd0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71348" target="_blank">📅 12:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71347">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/032667483d.mp4?token=soGu9rsr51FEM-HE81h-nyDa5aGAHGXwqhIOS0yv8hSJAcXVZZ2UaHcpPynqbOCmUb39Lia1MOp_CVOdqc0pde4PwO7L1cy5W6GEBMfStSe6YljeSOPqW_yVx0fGHGrCdXZhCnr8Fc0h3YnuUfBwitlCPBDM6yVyLraqSMAFb2ucKfvlsPOanj44t4WvSamuLS70AdunnWnGSqLSlek7r8EUAdg-bea-px93TjQ7HKRsmSDocGHpqRWmpz_vh0mIU5V6YIYk52jOjyX2FBOh0-r9MCHhlz1NOBrFCi69xnI1iN39Lg2mY5Bzit-hwlfLtq3-bCtCe8DvDFdGoOm1iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/032667483d.mp4?token=soGu9rsr51FEM-HE81h-nyDa5aGAHGXwqhIOS0yv8hSJAcXVZZ2UaHcpPynqbOCmUb39Lia1MOp_CVOdqc0pde4PwO7L1cy5W6GEBMfStSe6YljeSOPqW_yVx0fGHGrCdXZhCnr8Fc0h3YnuUfBwitlCPBDM6yVyLraqSMAFb2ucKfvlsPOanj44t4WvSamuLS70AdunnWnGSqLSlek7r8EUAdg-bea-px93TjQ7HKRsmSDocGHpqRWmpz_vh0mIU5V6YIYk52jOjyX2FBOh0-r9MCHhlz1NOBrFCi69xnI1iN39Lg2mY5Bzit-hwlfLtq3-bCtCe8DvDFdGoOm1iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گویا طبق فتوای جدید حضور نداشتن تو اجتماعات شبانه، غضب الهی رو در پی خواهد داشت و تو زندگیتون ذلت و خواری میاره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71347" target="_blank">📅 11:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71346">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItO5KgUfDhZNjxicOOPZNs1aiKwj1PFaI_aKpj2ZA2W8IX8RtBBvNmW4eowmvWv2fJkH_1EOMW3oUuxW6GinUyCX2AxU7gkn1SRZLMhrQmwiqfMh8td5qJ13HAff4gnTYq2u2BmiKzAlTBSobPei_N0CJ_zKN5sFnD86GyoX8_gFJ83zN4iqDz_gE5gHT4F2qg2gkDZE0g_HyL_isj8LVRJ0mA0LLtyfEekQH7i886QPiHKXKv_HWIdXcWcROtS69LBIkhF7k3W3LcAdsiaNXmI6YOul6aAptj8ncpLUtLuG7DAxvK3GxkUaP4-jIM7aVEwzK0TP834d4J0Ajd4JVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71346" target="_blank">📅 11:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71345">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcf294068.mp4?token=QX_FwNM4gxMcLQHUTCwW72FlwFexpcoTA-lscTWAK_QdzcKHo5_7A8vEajiZw5Yu4S_qF-VH7dQycchNNSpzTyNhLsLU_3eBjzyIwtU8vMrDfLDICn_JguNScvAZoUe4Z6nUOLFmYRz_-MYZdClXK4-AKHBbSQzmJfZfMwyBJhWwgQgacwkchA4s2FCw7T9xNdylRzDPq86VhgiH5krzZfN1_eVRRJdatn9DQ1Jgq7kZ8ryGSKeXwY45B690g2gC4-jYeCPG2vQXCLN_3Qut6f8RqcV1_T-dqyAJOQAdw2zhlKIKlIGZZ_W2QMoxC3IroOoQ7D5ikk9YxmhsVJKfMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcf294068.mp4?token=QX_FwNM4gxMcLQHUTCwW72FlwFexpcoTA-lscTWAK_QdzcKHo5_7A8vEajiZw5Yu4S_qF-VH7dQycchNNSpzTyNhLsLU_3eBjzyIwtU8vMrDfLDICn_JguNScvAZoUe4Z6nUOLFmYRz_-MYZdClXK4-AKHBbSQzmJfZfMwyBJhWwgQgacwkchA4s2FCw7T9xNdylRzDPq86VhgiH5krzZfN1_eVRRJdatn9DQ1Jgq7kZ8ryGSKeXwY45B690g2gC4-jYeCPG2vQXCLN_3Qut6f8RqcV1_T-dqyAJOQAdw2zhlKIKlIGZZ_W2QMoxC3IroOoQ7D5ikk9YxmhsVJKfMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
〰️
سنتکام:
کشتی «ریسکو» (M/T Riesco) در تاریخ ۸ سپتامبر در خلیج عمان غرق شد؛ این کشتی پس از تلاش سپاه پاسداران برای حمله به یک ناو جنگی نیروی دریایی ایالات متحده، توسط نیروهای سنتکام (CENTCOM) منهدم شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71345" target="_blank">📅 10:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71344">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/128e77e5cf.mp4?token=Re5HQZ8IOnzfcAxwCATC9Pr2DzvfI8A8t1crmQUkswv8PBOOa12aJeqgnByuoWGqPhoi9EPDnesDcuImtiUky2VGMAv0F6kAYlSZY3UE1-ni6Z9KJLmuR-RD7WyiblZK1L0nfl6g6QApNEahC3mhbFj6mdlzsf_OTgD-nK7BeF9Yc8ZM9VS_jNavYONOJN5KygbQQn0WKjzs7hbpiUesd1u9w38me1Ed4dHK_qdIME9nzmuBMVW26PjGGI37wHqDf2Jao80rvDWKBn9vdHInAsKBBnkpAM9ug3koTXd3KIyGuAkyYWSnShCAviJ5SuW0EgCs5-SyJf0wLgr-risf-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/128e77e5cf.mp4?token=Re5HQZ8IOnzfcAxwCATC9Pr2DzvfI8A8t1crmQUkswv8PBOOa12aJeqgnByuoWGqPhoi9EPDnesDcuImtiUky2VGMAv0F6kAYlSZY3UE1-ni6Z9KJLmuR-RD7WyiblZK1L0nfl6g6QApNEahC3mhbFj6mdlzsf_OTgD-nK7BeF9Yc8ZM9VS_jNavYONOJN5KygbQQn0WKjzs7hbpiUesd1u9w38me1Ed4dHK_qdIME9nzmuBMVW26PjGGI37wHqDf2Jao80rvDWKBn9vdHInAsKBBnkpAM9ug3koTXd3KIyGuAkyYWSnShCAviJ5SuW0EgCs5-SyJf0wLgr-risf-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🇮🇷
مهران رجبی:
اونی که نمیاد تجمعات باید بهش بگی فازت چیه که نمیای ؟
این وظیفه ملی و دینی ماست و باید بیایم کف خیابون
ضرر نداره بیایم و شما کاری میکنید که کفار ناراحت میشه پس بیاید
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71344" target="_blank">📅 10:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71343">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a8a7be1a9.mp4?token=R9OuHcMT3ra1op7Wd_tWanWL-xjfIxjYbr04XiW9VBurbIUV1XjHk2dp0LcC__mz_fXCNrQoq6EFsDZTA6IK-NzXlgbzpLSrL-SG1kL4RXvCx5V7M7F47EiAaNqe8t3rYAtCQCeVR2AHNr964riF0-EkDqCNr7ejAmk0a6zbJWP5cceDRNGd11Ue6Z0HnVGd1nTeo6RRwAg26udzXsUqP9wvjLOXVzf5W9g9L718yM8TmXYvDhRcRS5fnOPdkl8w1hso8i-BLYONE0fQ80O9M31_bdpZFs2CDTTc5BMuQGY2MIoc2TQd2Q_ZHDlHLbp0wKhMkbpxyNJpZ5tJo5zcow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a8a7be1a9.mp4?token=R9OuHcMT3ra1op7Wd_tWanWL-xjfIxjYbr04XiW9VBurbIUV1XjHk2dp0LcC__mz_fXCNrQoq6EFsDZTA6IK-NzXlgbzpLSrL-SG1kL4RXvCx5V7M7F47EiAaNqe8t3rYAtCQCeVR2AHNr964riF0-EkDqCNr7ejAmk0a6zbJWP5cceDRNGd11Ue6Z0HnVGd1nTeo6RRwAg26udzXsUqP9wvjLOXVzf5W9g9L718yM8TmXYvDhRcRS5fnOPdkl8w1hso8i-BLYONE0fQ80O9M31_bdpZFs2CDTTc5BMuQGY2MIoc2TQd2Q_ZHDlHLbp0wKhMkbpxyNJpZ5tJo5zcow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از طویله مجلس
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71343" target="_blank">📅 09:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71338">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Plpr27Y9ASvXVuHrAgTKnRa8uPzTMatcfuwHjNXdfwLe2GuzHpWJ2rQ3HOG_AOxrq_UGfT_vYSuFJrRANll60z5us_JqJapNtEDMGhzXsRvmSuw3ZezUDPDXzzdpATXiWKHDYT2StTmPMyH2GOtMpXy4fV0kIwTy7H-dCZCU0ly5LFj1ICCTwfYUOF65pcV-vAdZIF4nsaCyD_U9DXWgE6S7YCPZvMuYNaXvUK1Pq0TV1en23LfhhcqYCIXpmqqafgSIeT8Ao3JHak4t5WVMJl49V8hPFuapMGXId9KnK89Yy18AihLCYtafgY2OY4fawDhl07hUKqDIcGldfz_Jew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aOPTQ2fGS3M84fQz7dLAHuIxysK5uQiyLmWu1bs2A0mbKBHhDHGWhHtjOVEFZDRS9JM6O77NgHSgFsiAdVYbYHEEc61wF4x2tM2Nr7Zq5-MfiEFaOfDiYdDdDuAXhonTQvFllCwgHoVF-pzFjkns25bfLyVBM6KhVrwglJjhWua4dI1c3zi9xF78nLhwkMnFerWlpwig4i8Fncq3f9-FLHcQa6bl5UEj2TCXodYKyJewWZCjtrEUpA8lkwQws7RIQ7Flwm6BQZOrd7PAIgnk9vaODIClooGpNZCoDghaP_ta6wbANmBSj_bTxXADcnzlSwQFJktr8p9tURlUIcKI6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XcIb1JNxDVZrbqojPpntP9SI7bX776Xn0uIxS-RDqOjlgTuBj6IuOXtw2H5O0chhwdpzPlV5QnT0R7GhRfbRvG7K63olHUJ_cIDgqobK12MdGaTkrErr-wslmNDTY1yA-HUsRkbPOCncyPIcHuApnXpzhY5Bfr8CDOhTFPwgsc6BRW9R-asiQo3PZeTSGpNjmyx_GcGrzStiB7fCL7QpD6eCcxuVtL03nidUZ1kmSWXE49aMIfScjAR2iMbtlFXrRg3wPPlXsmQSmMdk2663aAgxuZ6xD2ObtBweg2h6C960J2XrgOSLwLH0yae31Gio_SsgawdpNfSkzWVRayiMnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KVfCzUMLotsKHBAR638XxIdM1Itj259zABXoCfmd8xYn--tgqUDq3-9947HfHdtNRVOSgV2xKkQTyMgbnlw4L1omWqXm3FqMx7UxRtj_JeXsm12KA8_R5x7F9NyAFCKznmjhifo_jy-fav3y-pOIH7g6kmSBo-bHkRV0orkTxNwwwlhvd1HAOT7vpIFsaDbQOn20Jk3sDzaKTslpaUT_M2s09f62UeB9QpX9HIzfuntyP67-dXr0AayFibrbMsNKV4MoBIsqOnT_HxVVUtvDAYEkPouv44C_zezZBvRBaQkhLivzf1HF2yW9SAPxNa3PYqvY0_VM4l6-q9rF8IEZNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pZzjGBhYGg7YIvB2sWsbLbZ3xVBPhxcJBZgwhF9h0Ylu9XuNp5zRWHrje-XzmQGeoDzh8ffeeUAPj-X9pYTaj2YNI6LNugZacskxCkhpPrtKfiFsdfBYuhK_zozv2QruT3rqb5g_elSnN5rBn3ryRIeenoQz8jDBqhXaaNyxyjwQDra5TX5BYpIptzcvKz3TlQSjk9djWHy8olb_9mQZYtLeq9nFiNsty9oKnlm3fYlqZgTpJ3TZxYNw2pw30fZWGZBZsCD6bOou33zwQPMWRaJ_fNok290bP42VOTjLu04iYH_66LgqvmkcAltWhTWd5A8UhCCtlskirtfhg8bskA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
🇮🇷
🇺🇸
سپاه پاسداران تصاویری از زیردریایی‌ بدون سرنشین آمریکایی که به عنوان غنیمت گرفته منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71338" target="_blank">📅 09:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71337">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71337" target="_blank">📅 01:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71336">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFCiopjreyeml78AMOmgfBLQE_x87pm8vAndrZEiBlSi_zGJjstp7NP3pxQpTTsuZGE6hNH1w_sTctdmJGNN8lub2fGiiu8QeN4Vba8wLI07LqbKPx0Qx7rRJdro74Cusvqx6D53t4WBoM0OUGf7M5Ii2U5n7y6i3rAa7UW24VZ37O7I-jWxXk1_Pa-OkHosEfjVxF8SwQn8tTe_Bn4PqZze-FfKqjNxUlqnUj4PZVCh2awnXWt4mny5-ztbsT3IAYVLssu0ecJ5OdzLqkQkiL3QNWZJZFAY01x2K3iKvDKSGzMhpM2arqGWTkbraqPhmB7ctxkuturoXfxJsm1y9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71336" target="_blank">📅 01:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71335">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71335" target="_blank">📅 01:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71332">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
📰
خبرنگار العربیه:
چندین موشک ایرانی در جنوب سوریه رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71332" target="_blank">📅 01:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71331">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/665d19bf87.mp4?token=r_yEdVnatLnK5-ga4psA9H19Ie-_I6gUNvjKe4MS3uF5FnyL9fFHgI1DJnf6f21sTN4bmc7g47Mo6CDcljLjAYa-XbsvDO-h7ycEt7wQYGwIlYGsLOOpUkEcTdQS5fmBftvJ5YAk4zzCBMsI1u8_b_IGNN7XhI31_82XHTgLmZcC2NJ85XAp7q_qqHAbPzCui7trU34XKJ-O98ZStFZOjHjh5sHUj6zxKsLaJPPAxiUyQFMi6RI4TNHrIdNCgJ1nIShkkSzVYTJjqWYIQ-vXHDjiU-6u-eUwfJcU7ocNB12cfJa4xroKFA7kDKaWZoJExKQ59K498C3_1ag9G76TRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/665d19bf87.mp4?token=r_yEdVnatLnK5-ga4psA9H19Ie-_I6gUNvjKe4MS3uF5FnyL9fFHgI1DJnf6f21sTN4bmc7g47Mo6CDcljLjAYa-XbsvDO-h7ycEt7wQYGwIlYGsLOOpUkEcTdQS5fmBftvJ5YAk4zzCBMsI1u8_b_IGNN7XhI31_82XHTgLmZcC2NJ85XAp7q_qqHAbPzCui7trU34XKJ-O98ZStFZOjHjh5sHUj6zxKsLaJPPAxiUyQFMi6RI4TNHrIdNCgJ1nIShkkSzVYTJjqWYIQ-vXHDjiU-6u-eUwfJcU7ocNB12cfJa4xroKFA7kDKaWZoJExKQ59K498C3_1ag9G76TRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسمون اردن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71331" target="_blank">📅 01:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71330">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf482be15e.mp4?token=pSNXqfYyc7sYWLK2BClEEKbTYy562OwZwiEHX1Y5qsfmo-_Ty1ah9lZjeWiXN_DWRN-liDzSU6InFI0H9BRj2YspeUQX_z6b5JAQLdEGWlJ6QJRf7Bt_AsiBpNZeLsthzMkbOOLLaNb9_exfMrG6rIVBUqR5EEFO_gfwpDsqkz7UWP_xW9NgGXfnyywIMYmwaj6eQqwpX9B0r9Dv4lTF5vpLg6VKozUtUu3Zywhwq1dTjZIGT2HqzynK5jvjGwZKK4xREtiv438cYdQ_KE2SwEBkGDtNqpCHuCyXXkIbMgRSisrmHz5EgvoO8ulKOusoDjanBP_WbyPD7B9j9zlwuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf482be15e.mp4?token=pSNXqfYyc7sYWLK2BClEEKbTYy562OwZwiEHX1Y5qsfmo-_Ty1ah9lZjeWiXN_DWRN-liDzSU6InFI0H9BRj2YspeUQX_z6b5JAQLdEGWlJ6QJRf7Bt_AsiBpNZeLsthzMkbOOLLaNb9_exfMrG6rIVBUqR5EEFO_gfwpDsqkz7UWP_xW9NgGXfnyywIMYmwaj6eQqwpX9B0r9Dv4lTF5vpLg6VKozUtUu3Zywhwq1dTjZIGT2HqzynK5jvjGwZKK4xREtiv438cYdQ_KE2SwEBkGDtNqpCHuCyXXkIbMgRSisrmHz5EgvoO8ulKOusoDjanBP_WbyPD7B9j9zlwuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
مهمات خوشه ای سپاه در آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71330" target="_blank">📅 01:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71329">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🇮🇷
نایا به نقل ازمنبع ایرانی:
سپاه پاسداران انقلاب اسلامی، دقایقی پیش، موشک‌های خیبرشکن را مورد استفاده قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71329" target="_blank">📅 01:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71328">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee276f397f.mp4?token=vSn2eG2RYj8VXVESlagk_OYC_RaWF_Y8DBE9gR7aSez-5463F0J3CJY752RYT3Vgaq5DLXLG6I3j0lxM_uDsLrgTKduMkVlycJVMfNMTGuWsBMRmM_MrWQ0toChxhfWCLtMYZnWySmD3YEHC5xvkg6_XlXPESbJnx_lRPd5AHJQPYkL0biMamTXoGliCwfLinXrtJu75fEV16o9CsDrOrrdnn_sEq0fPKJ1iO6rrrwrAZBELgHvQ-N21VsOHhjXyRNNupDUXo6WMYiYU7bJppjkUtQMZY5n_idD2In7fn7hySCn26s2gc3TLeyXgd6F1_dOv5fjn5IwQk1E-EQ8H_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee276f397f.mp4?token=vSn2eG2RYj8VXVESlagk_OYC_RaWF_Y8DBE9gR7aSez-5463F0J3CJY752RYT3Vgaq5DLXLG6I3j0lxM_uDsLrgTKduMkVlycJVMfNMTGuWsBMRmM_MrWQ0toChxhfWCLtMYZnWySmD3YEHC5xvkg6_XlXPESbJnx_lRPd5AHJQPYkL0biMamTXoGliCwfLinXrtJu75fEV16o9CsDrOrrdnn_sEq0fPKJ1iO6rrrwrAZBELgHvQ-N21VsOHhjXyRNNupDUXo6WMYiYU7bJppjkUtQMZY5n_idD2In7fn7hySCn26s2gc3TLeyXgd6F1_dOv5fjn5IwQk1E-EQ8H_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گویا سپاه توی حملات امشبش از موشک خوشه ای استفاده کرده
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71328" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71327">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f211389571.mp4?token=U9F7-EAhikJzBTzDlOPFTzlZe5vio5zMO6phnhKB01hZWbUUVz9ZwAOMq3uu8MfFT-7nWDBQzbnTkO2qPlsdv1lyj8ABwiFUwTj7wfdJnO16k_eldJXeonub-dqt0X-a6xVoWQj4s9Wp8FZ3Efg-Hpj8utu0tvZ1xl3U61jkbQ_Rc9L2roOGk52hKIF9AN3qbkNVyF1-aLU6LCcnQgAL0HuZO6dNzX2uqEN2tK2yzTUkRTlUFlKll_Ms93ECDI7uHQfhxSlB6PuLOYodJaUNhnsdYM02m9oeXpLRtMVd6mxkGDLsf5NQFFaokd97Vqp667WqT8aHTpEVi3IdvYYH9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f211389571.mp4?token=U9F7-EAhikJzBTzDlOPFTzlZe5vio5zMO6phnhKB01hZWbUUVz9ZwAOMq3uu8MfFT-7nWDBQzbnTkO2qPlsdv1lyj8ABwiFUwTj7wfdJnO16k_eldJXeonub-dqt0X-a6xVoWQj4s9Wp8FZ3Efg-Hpj8utu0tvZ1xl3U61jkbQ_Rc9L2roOGk52hKIF9AN3qbkNVyF1-aLU6LCcnQgAL0HuZO6dNzX2uqEN2tK2yzTUkRTlUFlKll_Ms93ECDI7uHQfhxSlB6PuLOYodJaUNhnsdYM02m9oeXpLRtMVd6mxkGDLsf5NQFFaokd97Vqp667WqT8aHTpEVi3IdvYYH9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعالیت شدید پدافند در آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71327" target="_blank">📅 01:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71326">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
از اکثر نقاط کشور به سمت پایگاه های آمریکا موشک شلیک کردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71326" target="_blank">📅 01:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71325">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d314b4d1bf.mp4?token=IeD0cRkqE_xEGmejzmbS0GDiqhTxfJN7olOIFvpskDmP5bl_uhUqdni3RNpPWed7irdoG56Quvra3WY7RPB_3V5zszPhMNLWf-i8Ne7behyHJAznqVmF6Y-pOl-xfeinTle5Cq3s8Hx6L7RwErRmAWCgb-63DTyPTTHeXTUtnuBHzIP2SFpSv60iRMg2dJCbhGv8gNH4xDcFOfYKzMtWurzO5ARdBPQwYzJZewjgwD8OFBEc81_R3CrKY6q0ZxgaGGHgsFzXFo8sk9zzmi2D0Jt-1JjfswU4Q7KCmKdP2CBu4s1SkO-qvAbakbDhRWhCn_xzABVVLc8EWrRMt4nPfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d314b4d1bf.mp4?token=IeD0cRkqE_xEGmejzmbS0GDiqhTxfJN7olOIFvpskDmP5bl_uhUqdni3RNpPWed7irdoG56Quvra3WY7RPB_3V5zszPhMNLWf-i8Ne7behyHJAznqVmF6Y-pOl-xfeinTle5Cq3s8Hx6L7RwErRmAWCgb-63DTyPTTHeXTUtnuBHzIP2SFpSv60iRMg2dJCbhGv8gNH4xDcFOfYKzMtWurzO5ARdBPQwYzJZewjgwD8OFBEc81_R3CrKY6q0ZxgaGGHgsFzXFo8sk9zzmi2D0Jt-1JjfswU4Q7KCmKdP2CBu4s1SkO-qvAbakbDhRWhCn_xzABVVLc8EWrRMt4nPfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
موشک ها در آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71325" target="_blank">📅 01:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71324">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
ارسالی از اصفهان:
از نجف آباد دوتا موشک از اصفهان ۴ تا
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71324" target="_blank">📅 01:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71323">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6edcd17216.mp4?token=h9Kl2KySOSg_oGc_hFAPZYZ48VbjrWPQXks-_3WVYzswNtKx-Cc8Be0fUVUAhT4IdfBTIVqKklAL5F7u_F52EGgHAlxjKrJCjD_Fs74l6ZBef6VL1eoKVbZuOejRbVo50CMTFmFSwJ3Bsjw0QvyIRxXlJgANMZ47uPmHvbVAQQN1ndpU8FEFgh9a9YVaJc4acZBwFtsetxb3eEauT5i8Yng0tAn4rfvzKddOwphBQ49lhV8mB_h-wQFx_E8v1TQ89Z-TnDkbkpUj5KK8z1g8Ua-lPEkwE96thD_KNUYZrS8_UHl-V3oivtYfh1usicRd588v6uXf3diN4C9807iRmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6edcd17216.mp4?token=h9Kl2KySOSg_oGc_hFAPZYZ48VbjrWPQXks-_3WVYzswNtKx-Cc8Be0fUVUAhT4IdfBTIVqKklAL5F7u_F52EGgHAlxjKrJCjD_Fs74l6ZBef6VL1eoKVbZuOejRbVo50CMTFmFSwJ3Bsjw0QvyIRxXlJgANMZ47uPmHvbVAQQN1ndpU8FEFgh9a9YVaJc4acZBwFtsetxb3eEauT5i8Yng0tAn4rfvzKddOwphBQ49lhV8mB_h-wQFx_E8v1TQ89Z-TnDkbkpUj5KK8z1g8Ua-lPEkwE96thD_KNUYZrS8_UHl-V3oivtYfh1usicRd588v6uXf3diN4C9807iRmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند اردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71323" target="_blank">📅 01:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71322">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
گزارش ارسالی:
از زنجانم موشک زدن همین ۱۰ دقیقه پیش
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71322" target="_blank">📅 01:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71321">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rrlgm2vhi_-NVyfbwiLnCvuAQ8q2Rnn3mFDLaYcR-Vw5QIArSpwQ1UEwUaIdnYUBsrkCS-R1NKFI1k64hqlNJFaBPNP0TRyLgns4ckyjO-fkZRitJFX8_zAJce06QtqlVzqRMv3_XzUK7PS8kBzoHOzcv5OG-1P48yZNo8kHT-5XEAfuYDNjgW6Ecil_QSEdSRa6OJ1KZNnDhxsppmGYKMux4fvnUcrgr9_cuLIoX8iyhu9CohhAtacFpsTPCD6ZPBvQobCpx42ZWcJtOntAZqMBJbnl_oAL7TWVAr92c8ERV_VBVjKrg4EskJFhBd2DMHeTeoFHSNKe5uFDMEdqdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ارسالی از نجف‌آباد
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71321" target="_blank">📅 01:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71320">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc98612785.mp4?token=GBIYc0G_qaf7XjOyMjpdd19xa9zuOoCgq5tzyLHPWSBmjZE2AGruugGm3oqCvbqJvGC1CYRqsi70M5c7vNtRlmbdGFoiEQZZJN5l50bvzvlSF_Va7W__TXs1JhjA0tZ97elx3kH6VYov9a2lDzKoRkiZOifAO-Rlr_WZSlNaNJLxPN_6-OI8KbS5cqCOQJShFsRYL3r3_4kn5SLY--hKPsbJnoL3tXSj5r1DHTmqePCvrefTfPKJ339jDa5gfTD89p338EzJ3B9F4Spo-BNqsM4lEEw_3aT-jpTuf1nLHV7awdCzys4zwRJYxO8gJ834zWQ4Zptnd0c0gbhS55Uuog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc98612785.mp4?token=GBIYc0G_qaf7XjOyMjpdd19xa9zuOoCgq5tzyLHPWSBmjZE2AGruugGm3oqCvbqJvGC1CYRqsi70M5c7vNtRlmbdGFoiEQZZJN5l50bvzvlSF_Va7W__TXs1JhjA0tZ97elx3kH6VYov9a2lDzKoRkiZOifAO-Rlr_WZSlNaNJLxPN_6-OI8KbS5cqCOQJShFsRYL3r3_4kn5SLY--hKPsbJnoL3tXSj5r1DHTmqePCvrefTfPKJ339jDa5gfTD89p338EzJ3B9F4Spo-BNqsM4lEEw_3aT-jpTuf1nLHV7awdCzys4zwRJYxO8gJ834zWQ4Zptnd0c0gbhS55Uuog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ارسالی از اصفهان:
حداقل چهار/پنج موشک دیده میشه توی آسمون
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71320" target="_blank">📅 01:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71319">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c50434db49.mp4?token=f3c_AEmVJrXxWCxMB0Pof3YauoblhI_hsavg0tzp-kKcn5jIdSSCfXXX2K_qcDx4foaVmJ9zACbXaYnTkzRXsUoKSm26ZI441mBYl6mYI3aJp7n26R7R0ubE4BjR3DW4_doDK7XsGUf54ztE9-e1Xz7bv61HcZubJHvC0ulXp6n_q3X9C9Bk6HbMDx27399cPxurR4SzBopNnuNFMfKF7GsT-ASNaCb92et7-VOajgY_DXbQgnT42qMW--0Nnkz377ai6DTVk1MzstesSrutJjD2zYwQgJ4WAD3Mjq3nZHNFKiCF8nTZjH4cKkMH1yPlwrY1LlqCrNYYIjB4DJF8wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c50434db49.mp4?token=f3c_AEmVJrXxWCxMB0Pof3YauoblhI_hsavg0tzp-kKcn5jIdSSCfXXX2K_qcDx4foaVmJ9zACbXaYnTkzRXsUoKSm26ZI441mBYl6mYI3aJp7n26R7R0ubE4BjR3DW4_doDK7XsGUf54ztE9-e1Xz7bv61HcZubJHvC0ulXp6n_q3X9C9Bk6HbMDx27399cPxurR4SzBopNnuNFMfKF7GsT-ASNaCb92et7-VOajgY_DXbQgnT42qMW--0Nnkz377ai6DTVk1MzstesSrutJjD2zYwQgJ4WAD3Mjq3nZHNFKiCF8nTZjH4cKkMH1yPlwrY1LlqCrNYYIjB4DJF8wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو ارسالی:
همین الان از دماوند موشک زدن
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71319" target="_blank">📅 00:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71318">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
ارسالی از تبریز:
همین الان از تبریز موشک زدن
سایت موشکی امند
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71318" target="_blank">📅 00:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71317">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
چندین گزارش از خرم‌آباد اومد که صدای انفجار شنیدن./احتمالا پرتاب موشک
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71317" target="_blank">📅 00:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71316">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
ارسالی از بروجرد:
سلام بروجرد هم فرستاد
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71316" target="_blank">📅 00:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71315">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
گزارش ارسالی از اصفهان:
هفت تیر مبارکه اصفهان موشک بلند شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71315" target="_blank">📅 00:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71314">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqJ42icfAN3oFqUQUVqczgX8UZtZyWNn6oHacF38ehX3XZUAsvUn5mVcWZi66RwMtboPfhEPjCn8IIAiAMjqykOVkAeSLHbxdxJ5_sOXOmUeyjRvVtvXYxyRvz_aviQF2idAkuhAZx3XajTl_6Oh7iWbb7TuFaGmUblWp8HYmR-T1H8sJhoMiPEEq5neVndeFh_dDyS4ex3a-F2KUHwuR978LWLdeh24sVvS-x6zM3hWqZA1K_RGdqRkN_PSTYGYp_o0yVLSzElGdK3ZXZPQocXRNmjl1hqUpIAy8KFeqt0LXpbL0STSAQn2CtGnKcM4WRFj43NCQ8MbpHIcPyZulw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویر منتسب به اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71314" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71313">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
گزارش ارسالی از یزد:
از یزدم موشک زدن همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71313" target="_blank">📅 00:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71312">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
گزارش از اصفهان:
اصفهان الان زدن موشک نمیدونم شهر رضا بود یا نجف اباد
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71312" target="_blank">📅 00:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71311">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
گزارش ممبرا:
۱۵ خرداد اصفهان شلیک ۲ تا موشک همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71311" target="_blank">📅 00:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71310">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛صداوسیما:
دقایقی قبل نیروهای آمریکایی به یک فروند شناور تجاری در آب‌های ساحلی شهرستان جاسک حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71310" target="_blank">📅 00:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71309">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFtEPm5KoADigCQ3yLVRcKuFntzpk6IW9FKzXg8FnI1_D0g3RYWat_ZzYvUya809q0sW6lSEVLX2mlLOVgcvut5EI-y7sFzu44Gf_ByF1JiyY1nWzM0sofK4x0xkCSn4Uyk7qVgD2nAbmCIry1CGIQ43hRvm4b60CrMs859quHuRjEvwHMhQPbxWd3v3iWjFmvIhibnig3ha_XTnhSAkpeewI3YDCS2cE1RwZH_gEorRu_f1m6xs49jrH4WLqV-LnOSUEk0JfV6wr7c_M02RsLW1lbYZDVOdKM1uZdYdMmqNuIA2z7gBjCi-3eG3BqGaVGUnJynB0b7o-LYAJWmAEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
📰
وال استریت ژورنال:ایران ظرف سه روز، دومین موج حملات موشکی را علیه کشتی‌های نیروی دریایی آمریکا انجام داد، اما هیچ‌یک از شناورهای آمریکایی هدف قرار نگرفتند.
این حملات موجب نگرانی واشنگتن شده است، زیرا به نظر می‌رسد ایران از موشک‌های پیشرفته‌تری استفاده می‌کند که قادر به هدف قرار دادن کشتی‌های در حال حرکت هستند.
مقامات آمریکایی همچنین در حال بررسی این موضوع هستند که آیا چین یا روسیه ممکن است در شناسایی موقعیت ناوهای جنگی آمریکا به ایران کمک کنند یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71309" target="_blank">📅 00:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71308">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlxNpFnZVUdvLUm8S3Uq5CMdhASnPJ6uQD3TSTZtWDc6paQSZW2NwD-Td5mqmNubj-IUIdi0CsBS10mjh2wDe08o0GA5dsqCQjOT4I8YTOO6s8MCh7HERM3-_0Y8b_ij_cfrE6cDK_M2hwQj-wGwAWisq00KvBPFbtomuewWOuKvOHaPicuPx6u8nj77IyS_Rhi3y_ueVe2QpJa3soOdrY8gL5C63Qeqtw9JOtOcu8-JpBRQSTM_sk243Q0xW-4k_WasrBomZ4Qio0qsoowK5FE22ScW1E_YONtQzldQI_tMW-E8L47hLZffoZOx66Fts7qEt9lkaceoXt-imUmygw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
نیروی دریایی سپاه:
به تمامی خدمه نفت‌کش‌ها در بنادر و لنگرگاه‌های کویت و بحرین هشدار می‌دهیم که فوراً شناورهای خود را ترک کنند، زیرا این شناورها هدف قرار خواهند گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71308" target="_blank">📅 00:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71307">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsKFOAJi--lhgHh4lzFxei3vF-p-y0N2H-vrTZwq6G8dCSPGwxgqbWdAcFnBJ8s-6e9OWKbxm3SWY9PqgtZU1cxJ0u8BgXHSy8HRY0Tc6TCxzrM2JZWQYVHHy2unY05jRUEcdiJHkWGTSCtq2DAAqutOV5D09Yk0-aA59ceGG2dqnaWCCn8aL2--MEGSEEDIvuMGAgz4UXXwhF5lFosmW0HzFOuA_CDRVJTuqdJO9Ue8j_iYT2e4pp0eTDbjnQdZgBMbm42fJ7ktZkXj0ONVw8u-pW1YPBhiuAyh-7YyKq_ugo6hnOO7KZJWpp88CazNQ7Rtd96rM1FSapZSaBBeOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇺🇸
مصطفی نجف زاده:
آمریکا با هدف قرار دادن نفتکش‌ها در سواحل ایران و مشخصا خارک، علاوه بر اینکه می‌خواهد بازدارندگی معتبر در برابر رویکرد تهاجمی اخیر ایران در حمله به ناوگان دریایی آمریکا ایجاد کند، ممکن است گام تازه‌ای در راهبرد محاصره نیز باشد که براساس آن، قصد دارد حلقه فشار را از مسیرهای انتقال نفت به مبدأ حرکت نفتکش‌ها منتقل کند و صادرات انرژی ایران را از نقطه آغاز با اختلال جدی مواجه کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71307" target="_blank">📅 23:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71306">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
📰
فاکس نیوز:
امشب
برای سربازان امریکا دعا کنید
نیروهای آمریکایی به طور فعال در حال حمله به نفتکش‌های ایرانی در اطراف جزیره خارک هستند، به نقل از فاکس نیوز
ایران گفته است که در مقابل به پایگاه‌های آمریکایی حمله خواهد کرد، اما بدیهی است که ایران *خیلی حرف‌ها* می‌زند
امشب برای نیروهای آمریکایی در منطقه دعا کنید
و برای خانواده‌هایشان که بدون شک نگران پسران، دختران، شوهران و همسرانشان خواهند بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71306" target="_blank">📅 23:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71305">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114d9f6af1.mp4?token=vbxoySr7GQTBKKK2ovNRMWyWnOxG6rYFfZa85jCH_cS5_2NfUQ37jX8B2WUea1dywtCO7ZeUhIgVq8lLk1F-ZEkVJvdxiVa13VgAS1jjoFVX8Kh_FkK4-0s1vUy9FC3HWOlySFltSB7wXtQ3Rgagy-YiHGnCyfAzf1I7A_ar4pNnV9ordWN2f41Xz-guin0_dk56Vf2mGTP73ATfTHkzb1rsJzeZEF-6nx88tLEX6Ap2fSbsNyjBDfWF1hUo7g9MmDbNM26gzzOHiejk_KuOUUV2UuJOL-89_ChlycpVofrdA3OgKd6Fvrp0cGDuV6_se4ue-cSRvXARblIe_9alLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114d9f6af1.mp4?token=vbxoySr7GQTBKKK2ovNRMWyWnOxG6rYFfZa85jCH_cS5_2NfUQ37jX8B2WUea1dywtCO7ZeUhIgVq8lLk1F-ZEkVJvdxiVa13VgAS1jjoFVX8Kh_FkK4-0s1vUy9FC3HWOlySFltSB7wXtQ3Rgagy-YiHGnCyfAzf1I7A_ar4pNnV9ordWN2f41Xz-guin0_dk56Vf2mGTP73ATfTHkzb1rsJzeZEF-6nx88tLEX6Ap2fSbsNyjBDfWF1hUo7g9MmDbNM26gzzOHiejk_KuOUUV2UuJOL-89_ChlycpVofrdA3OgKd6Fvrp0cGDuV6_se4ue-cSRvXARblIe_9alLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این فیلم‌ لحظه‌ای را نشان می‌دهند که هواپیمای باربری آمازون در روز یکشنبه در فرودگاه بین‌المللی میامی از باند فرود خارج شد و متاسفانه ۵ نفر کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71305" target="_blank">📅 23:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71304">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f0bbe630.mp4?token=ukmp5TI8A2Q1WnRTbi0rC_EF4MZ3qOqXdWACnC7QQRx4Jo2Ex-h7kt76eQPz2iChXQe-S3KY3oZCLbUGZpWYnnWhuOpS0THSSWW-8caHGhJy0KMgl-T6eg9jn4cwSOM-Loy8fae3HCVQ-ht659FqvGiXWYuplcE_VfaCz86xFPVpOnM_JKCY4veOHfCJwG-tnHTgdTpXD1KuK-SqFF_usxpPjlHYlhSarhF2wttL62l3CHmBSfMH53UgkiXZZOIEsKGmTYEZwRaiYgfJji1uhnHB3axvi1d1y1yR062oMcJyWFrcn8K7Z6yasKN3HM6fD2vGqXVyHrQHuDzvhvcD-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f0bbe630.mp4?token=ukmp5TI8A2Q1WnRTbi0rC_EF4MZ3qOqXdWACnC7QQRx4Jo2Ex-h7kt76eQPz2iChXQe-S3KY3oZCLbUGZpWYnnWhuOpS0THSSWW-8caHGhJy0KMgl-T6eg9jn4cwSOM-Loy8fae3HCVQ-ht659FqvGiXWYuplcE_VfaCz86xFPVpOnM_JKCY4veOHfCJwG-tnHTgdTpXD1KuK-SqFF_usxpPjlHYlhSarhF2wttL62l3CHmBSfMH53UgkiXZZOIEsKGmTYEZwRaiYgfJji1uhnHB3axvi1d1y1yR062oMcJyWFrcn8K7Z6yasKN3HM6fD2vGqXVyHrQHuDzvhvcD-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
آیت‌الله بی‌بی‌سی از لندن فرمودن بنزین(۱۰ هزار تومنی) در ایران تقریبا مجانیه. این دقیقا عین جمله‌ایه که آیت الله بی‌بی‌سی برای مردم ایران پخش کرد!
تا حالا شده بی‌بی‌سی فارسی حقوق کارگران در ایران رو هم به دلار حساب کنه و نتیجه بگیره مجانی کار می کنن؟!
یا تورم رو حساب کنه و مقایسش  کنه با حقوق کارگر؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71304" target="_blank">📅 23:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71303">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3dcabadfe.mp4?token=DG0jAd3Z83BDfTQMwISNAAmLyTwwwyI136UIP1exet5wFwXYl16PNCa-d3jqroGeZKDzzVo96P4pwt-mxxPWq1CJSqDmzPbnQiivQ2pRVlhEn9f-kyy_TOyDTMz5p_fdBoS2S8pRMBxuQSzOqmR7AcNvz_P6dUWdnmA8pmtEtgoUPxRzw1mJU-APIyhXlqFeXy_bbCR55m0IoZPlrIrQyhUjMXtLyQznz1ctxApM3xsaAKnjyLREG9dNp6iSw0a9wenj6eKMhCbu6HHstvslQWITWvr7Alfm0tk4Y1J0rboSe_pq8jG9tgmvkyNsC3LR7J1aLlJ1eZOIQdOMdgYqWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3dcabadfe.mp4?token=DG0jAd3Z83BDfTQMwISNAAmLyTwwwyI136UIP1exet5wFwXYl16PNCa-d3jqroGeZKDzzVo96P4pwt-mxxPWq1CJSqDmzPbnQiivQ2pRVlhEn9f-kyy_TOyDTMz5p_fdBoS2S8pRMBxuQSzOqmR7AcNvz_P6dUWdnmA8pmtEtgoUPxRzw1mJU-APIyhXlqFeXy_bbCR55m0IoZPlrIrQyhUjMXtLyQznz1ctxApM3xsaAKnjyLREG9dNp6iSw0a9wenj6eKMhCbu6HHstvslQWITWvr7Alfm0tk4Y1J0rboSe_pq8jG9tgmvkyNsC3LR7J1aLlJ1eZOIQdOMdgYqWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
این روزا تور مدیتیشن و استراحت مد شده و طرفدارای زیادی داره
:
اونایی که مشکل روحی روانی دارن میرن درخت بغل میکنن و گریه میکنن
یا با حشرات توی جنگل و حیواناش اینا حرف میزنن حرف میزنن حالشون خوب میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71303" target="_blank">📅 22:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71302">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a391f5b86.mp4?token=gU3XwdrWncMmjzkExkc-_tG3LtFIr8La1gIed_pHWHrstOuKStUwv5dWjxvdA592hdjAbFqghqgXzliTalTFgmV_5UEdES3Zyj-4JyjasZ_Kv5gVnAeYZLidBof6Z3ZjRXkFXUxpph9GbTIQg45XdFq71L8XTE_pg4BG1O6qrjLKSotgc0iAi9zV4LxZFzl2If8FJKK4qEKlFynmLZN-QrrSeB2msa0RXpjddxamLgCzLwn9k8tRNRdCEJuFamc9NDnTMvcaWtnrzg6B6a30U6pOturd15uRZr1LkOr9rJIyesoLmhss7_aFZGSYc5QwSkhlHdnoAnuVRLxXppkbTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a391f5b86.mp4?token=gU3XwdrWncMmjzkExkc-_tG3LtFIr8La1gIed_pHWHrstOuKStUwv5dWjxvdA592hdjAbFqghqgXzliTalTFgmV_5UEdES3Zyj-4JyjasZ_Kv5gVnAeYZLidBof6Z3ZjRXkFXUxpph9GbTIQg45XdFq71L8XTE_pg4BG1O6qrjLKSotgc0iAi9zV4LxZFzl2If8FJKK4qEKlFynmLZN-QrrSeB2msa0RXpjddxamLgCzLwn9k8tRNRdCEJuFamc9NDnTMvcaWtnrzg6B6a30U6pOturd15uRZr1LkOr9rJIyesoLmhss7_aFZGSYc5QwSkhlHdnoAnuVRLxXppkbTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت وزیر خزانه‌داری آمریکا:
زمانی که بچه بودم و در کارولینای جنوبی زندگی می‌کردیم، خانه‌مان نزدیک یک مرداب بود.
گاهی مارهای سمی زیادی در حیاط پیدا می‌شد.
وقتی سر مار را قطع می‌کردید، مار می‌مرد، اما خودش نمی‌دانست که مرده است؛ بنابراین باید مراقب می‌بودید، چون سرِ جداشده هنوز می‌توانست شما را نیش بزند و دُم مار هم ممکن بود تا زمان غروب خورشید تکان بخورد.
اما وقتی خورشید غروب می‌کرد و هوا خنک می‌شد، تکان خوردن دُم هم متوقف می‌شد.
🔴
حالا مار ایرانی — یعنی همان رهبری — هم هنوز نمی‌داند که مرده است، اما در واقع مرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71302" target="_blank">📅 21:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71301">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc7c3d5f1.mp4?token=j0Bu9fVV27prGmFiylxdfFS9XUg0G1jPhvD3WDmgX2NuHakaHWVtzCHqfc8uP2DJnz83X_yg9-zsYE23Fw-xHeeGYQ8XGlYCBODMXzG8HMjQBHx7j-hFOKKt8eY56zoQHKnonLjJx7uyJwPjmdvl8zuEqDb5FItfKXzZn8R-_yWGw_DOSLCK5x33-KXnK-_Na0Qq7g8dNnFG4WCnAq_iwCrr0SO7wMsPgRyLB31rcE1ispeMPUYYFDuIuNv1eqhd3MYcozYMRtBzITvVv5zKj3JxwxedwfFvAif9ecwA9n4S1cX4nRFHtZlk_-Qi1sZwDspzsaVTyCc-bE8nd-MC_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc7c3d5f1.mp4?token=j0Bu9fVV27prGmFiylxdfFS9XUg0G1jPhvD3WDmgX2NuHakaHWVtzCHqfc8uP2DJnz83X_yg9-zsYE23Fw-xHeeGYQ8XGlYCBODMXzG8HMjQBHx7j-hFOKKt8eY56zoQHKnonLjJx7uyJwPjmdvl8zuEqDb5FItfKXzZn8R-_yWGw_DOSLCK5x33-KXnK-_Na0Qq7g8dNnFG4WCnAq_iwCrr0SO7wMsPgRyLB31rcE1ispeMPUYYFDuIuNv1eqhd3MYcozYMRtBzITvVv5zKj3JxwxedwfFvAif9ecwA9n4S1cX4nRFHtZlk_-Qi1sZwDspzsaVTyCc-bE8nd-MC_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اقتدار به روایت تصویر؛
🇮🇷
مقام جمهوری اسلامی:پمپ های قدیمی جا برای بنزین ده هزار تومانی نداشتند؛
یک صفر دستی اضافه کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71301" target="_blank">📅 21:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71300">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">از دیشب تا همین الاناست که مسلمونا افتادن به جون هم، شیعه های یمن، سنی های عربستان رو دارن با موشک و پهپاد می‌زنن، یعنی کشوری که خانه خدا اونجاست
عقل
🤯
#hjAly‌</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71300" target="_blank">📅 20:50 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
