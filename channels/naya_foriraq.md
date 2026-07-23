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
<img src="https://cdn4.telesco.pe/file/RWfWfb1S_AxWny7SMXdS8xIzVhAdvqceyAnEkfmKSY_B4lRr16z7cBpoAGWaZL6FMk98EiDsWZaLKs33w7NSNEZKwOruzvmRgU-g3Lkefd3jz6SLYVE0N7tUaNL6JTXfeAmsY9PZAFvQ5vxkTqPj5g6XSx3l0Ev49k-Emk94Jayd_XUBKAtyMRbv3_INgVJ0CQt7AaroT3XYRIWZixdXxDyJ6ZUqE4VHX6zmRerIK80dUdDVXZxar7J2eNex4tedoHVlq_g06wl2tmzjwhG8oeZnvCugfomFxChUWfzr1PTUn_XQnVvnY-rIZQPRBzd1usBsYGYLBCVYXEaBNSLN_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 271K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 11:27:00</div>
<hr>

<div class="tg-post" id="msg-85021">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏روبيو: يبدو وكأن الحوثيين ينخرطون بالنزاع</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/naya_foriraq/85021" target="_blank">📅 11:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85020">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سلسلة من الانفجارات المتتالية تهز الأردن وسط فشل منظومات الدفاع بالتصدي للصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/naya_foriraq/85020" target="_blank">📅 11:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85019">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">انفجارات تهز الأردن</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/naya_foriraq/85019" target="_blank">📅 11:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85018">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">انفجارات تهز الأردن</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/naya_foriraq/85018" target="_blank">📅 11:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85017">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تفعيل منظومة الباتريوت في قاعدة العديد الأمريكية</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/naya_foriraq/85017" target="_blank">📅 11:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85016">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انفجارات تهز قطر</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/naya_foriraq/85016" target="_blank">📅 11:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85015">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/naya_foriraq/85015" target="_blank">📅 11:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85014">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8009f4f178.mp4?token=ebKRXqP6lTQqFoBxMu1VPcxQJjJg6Rppcg_AWoOZ-pIyWu9h6qGjbE1M-9ZG8H8wjHXLQx-RKivnveeGzwsPDTqLhCFkN6uCxZ1ed9m84GoT0E2nsfJcPFq6MMMf2IJIGGILagruw-OMX6YkRt_nzfuSr08Wb_8mFuzFJP7duDyL7c24QdeJij9E3Tv3XNx35E1E8TEC-c5caDnqBNjJK4Id4X5LmebH37Za5fLc2pJJZMwMQ64qZqm9T9TrwYG9vvjpTYl3Es43njh4I7woi-Yy0U20vg87tN2HGekAlYIfjZtO-Dz321w0pHyPbRwYhOvzUOzAfotL_BkPLP1qCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8009f4f178.mp4?token=ebKRXqP6lTQqFoBxMu1VPcxQJjJg6Rppcg_AWoOZ-pIyWu9h6qGjbE1M-9ZG8H8wjHXLQx-RKivnveeGzwsPDTqLhCFkN6uCxZ1ed9m84GoT0E2nsfJcPFq6MMMf2IJIGGILagruw-OMX6YkRt_nzfuSr08Wb_8mFuzFJP7duDyL7c24QdeJij9E3Tv3XNx35E1E8TEC-c5caDnqBNjJK4Id4X5LmebH37Za5fLc2pJJZMwMQ64qZqm9T9TrwYG9vvjpTYl3Es43njh4I7woi-Yy0U20vg87tN2HGekAlYIfjZtO-Dz321w0pHyPbRwYhOvzUOzAfotL_BkPLP1qCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاق صاروخي مجدداً من إيران نحو القواعد الأمريكية في المنطقة</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/naya_foriraq/85014" target="_blank">📅 11:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85013">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfq015XJsvvh1iAjvq0WomtJLuzZUMIFz1Fma2VKnRe49qMUYThLtbjhnne_XKKym2IKeOzPrYk0eQr-TBbMxUuO_ZL1bA-85uXulTD1kTIrACCZ0c72y_1SqAZewwGWT4xb5z7O8XxOz48kzDixo1Ect3zbXAYId2yp2wnr8IR4Lg_zCCMTJvQsoH44VMDho6KYpz5GVMU9MLDFhea9_8Ag-rgLNwHdMnCICHAnTmj53qpUUovz_j4mJF9GgToE-CV0CESC7r7JyTYHvtcNP-JuytzCcLKXMUQcMoDajIlbBE3u_3nQABM0Ie-K2AS60H99zWudTSQkxAw0IUFvXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إطلاق صاروخي مجدداً من إيران نحو القواعد الأمريكية في المنطقة</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/naya_foriraq/85013" target="_blank">📅 10:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85012">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">الاتحاد الأوروبي: استثناء لنقل الغاز الطبيعي المسال الروسي إلى دول ثالثة لمدة عام واحد مع التجديد التلقائي.</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/naya_foriraq/85012" target="_blank">📅 10:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85011">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇶
🇮🇷
رئيس مجلس الوزراء العراقي يغادر العاصمة بغداد متوجهاً إلى طهران في زيارة رسمية إلى الجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/naya_foriraq/85011" target="_blank">📅 10:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85010">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVzXJbN1cF4ABZxvPhMh7b_N0Se1L2vKMhybt9LMZqWP1H6p0S9eWbC_XnlZlYqp94s10cYzEMcNzVQW9m9dX4-27YNhBmozI6camQnRXaZzCB1qxchkAd185zq63X4PNXdAjCqr80S7nhIuXRfHL9XaA909Y5gCy9pAXW5PNnfOwAHJOD8k7yi9VazF6tisft7cEcxKb_c8uIVPh4KEnfNNtoi4WWkADsrsH5IOaJK7B-Lb0xBaqSVOAxQkdXchq7IclJeLjJB5nPOtp5wAwp60thOIB1KXLAyRw3LBZMqmmdZBnnPQ4Im7F1dmD_p9SUi9WfwjgbUis4BJ6exMIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد لتحليق الصواريخ الإيرانية قبل وصولها نحو أهدافها</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/naya_foriraq/85010" target="_blank">📅 10:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85009">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzKeBz6mWC1LKC0oEwvx8IeEybYwSM1d2L1Ig8nSN_I5pHetv691DRkxXKgxvVQgKSo_0kr9Tz0aij8UfQ2LNrslmYBYO4cBBjL90sssDM9H2HYqzgOhVkbxXBU9SO35XWCAvtN167o45iDGjaMz-9UTx7QaeVwUvVk5vrW31m2guVjWtSh7EnYv3sR9GxUM6t2PyuPzE6QvuFt6OCJaAEXAEZczjm2bxS3IgKMcJibLFnATcA8V42GaboHg8VeWNdHIq9psjeWD8Ckqt-TTOE5F1PwkRVYLN3sfq2IsU1Kn3oNyxJRuKiq-GoqRcHwu5i23oPyaY2VRUpde0ohn8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاق صواريخ من إيران</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/naya_foriraq/85009" target="_blank">📅 10:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85008">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0J0RXzsGaopyeCGds_4d16G9WJAITu4rBNtEREyE4ARGmRJRcIBnzvpamhJU8XfeUAJDidb0AP-w3pMDPw-2Du27812SD1YGCjcRsKsvYp66ffFU9AzWkWckieo01hRAppX9DK_UvFhqXJOLtuGCj_QqXGkGSR7K6YAkliGfRJsCtB2qlGh8V241Gul6x1ILdXnXDC5vdRP_CR-BQOFsScunSs-4itFIMLhtkiCmmQj6iiW2aYp1agDVellwzGbvJhRqeIJUQ6LcKNRUtWKMVqj9FDk82MpJQ5lvofaxVlaImtowYbOAmTBIfLuhgZeVQYnqnNxgZD6y2yK9Y6bXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاق صواريخ من إيران</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/naya_foriraq/85008" target="_blank">📅 10:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85007">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/naya_foriraq/85007" target="_blank">📅 10:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85006">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bac3f27363.mp4?token=pLJDRs5XTFWNa2v8ead2QzX0THOkBBoet5-azSQDeHtST-fRZBTx94Td0eBL3edUQBhrMNajATJ3AX8bUfeAhNzyE2D2QKt7L9R2q1pPwFyMrZEAMduLl1mHYJPN6HEW3xWYpg35nI8_SSMAKcVXgVTXMP7BLY9T9sqPAAm6MFv6-aVNDzTNZgBSiOYyuZMDv2G2kaI3L_7Z_7GsSHKfDvmfuKkRN9l-yFU0SWeF2FV2Stl4g8b-oWa6sRhPUX_bnHXl4ZPZDI9WKyQOBmq-wez30P6MjfUdxdBTxJcSofDIPW5IVkoIxA5OpFBDmKQLUHu2Qk3e4x9BvoQUY9IOjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bac3f27363.mp4?token=pLJDRs5XTFWNa2v8ead2QzX0THOkBBoet5-azSQDeHtST-fRZBTx94Td0eBL3edUQBhrMNajATJ3AX8bUfeAhNzyE2D2QKt7L9R2q1pPwFyMrZEAMduLl1mHYJPN6HEW3xWYpg35nI8_SSMAKcVXgVTXMP7BLY9T9sqPAAm6MFv6-aVNDzTNZgBSiOYyuZMDv2G2kaI3L_7Z_7GsSHKfDvmfuKkRN9l-yFU0SWeF2FV2Stl4g8b-oWa6sRhPUX_bnHXl4ZPZDI9WKyQOBmq-wez30P6MjfUdxdBTxJcSofDIPW5IVkoIxA5OpFBDmKQLUHu2Qk3e4x9BvoQUY9IOjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇰🇼
مشاهد من قاعدة علي السالم في الكويت حيث لا تزال النيران مشتعلة في القاعدة بعد دكها بالصواريخ الإيرانية.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/85006" target="_blank">📅 10:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85005">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">📰
رويترز عن بيانات ملاحية: 3 ناقلات محملة بالنفط متجهة إلى الصين والهند عادت أدراجها من باب المندب يوم الثلاثاء</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/85005" target="_blank">📅 09:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85004">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">📰
رويترز عن بيانات ملاحية: 3 ناقلات محملة بالنفط متجهة إلى الصين والهند عادت أدراجها من باب المندب يوم الثلاثاء</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/85004" target="_blank">📅 09:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85003">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔻
مصدر امني لنايا
مبنى امني كويتي تعرض البارحة لهجوم بمسيرة مفخخة انطلقت من داخل الكويت ؛ المبنى تعرض لمسيرة كواد كابتر على ما يبدو من الخلايا النائمة من الداخل ..</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/85003" target="_blank">📅 09:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85002">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/85002" target="_blank">📅 08:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85001">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/195d4cf273.mp4?token=nK0YiQgpMQzmGBeKINttSziwOFnKrHjdlCVpQBu-6oxK53GHXqBXGXpcrnc3RliyNS4wTK_Dsi97RclkAK7wAIi8nWMUk6x7bRa7FcH041aN4v3N_eAUNYOXPh2EYQPvmtlOU4hW8ApKRCR68-6gjUVN99sOsYhB-Jkd9KqztntV8Jlj683wCIZKX1EQs7_JTELc2afbbY1KW0d6DwSM7wvNWhyyq_kY867NQz1OULsidIZEkf72323riGa0KPHj17DKBytqMqXDjMKrJfXHJ_Of7cwc_VJr3nhsZC7h-ytMNGlx0fJQKodeoEfd08sNjd2MuZF0GpBoIm8KON46zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/195d4cf273.mp4?token=nK0YiQgpMQzmGBeKINttSziwOFnKrHjdlCVpQBu-6oxK53GHXqBXGXpcrnc3RliyNS4wTK_Dsi97RclkAK7wAIi8nWMUk6x7bRa7FcH041aN4v3N_eAUNYOXPh2EYQPvmtlOU4hW8ApKRCR68-6gjUVN99sOsYhB-Jkd9KqztntV8Jlj683wCIZKX1EQs7_JTELc2afbbY1KW0d6DwSM7wvNWhyyq_kY867NQz1OULsidIZEkf72323riGa0KPHj17DKBytqMqXDjMKrJfXHJ_Of7cwc_VJr3nhsZC7h-ytMNGlx0fJQKodeoEfd08sNjd2MuZF0GpBoIm8KON46zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
ردًا على استمرار الاستفزازات والانتهاكات التي يرتكبها العدو اللئيم ضد بلدنا، نفذ الجيش الإيراني، في المرحلة الثالثة والعشرين من عملية "صاعقة"، قبل ساعات، هجمات مكثفة بالمسيرات الانتحارية على مواقع انتشار مستودعات الذخيرة والمعدات اللوجستية للجيش الأمريكي "الذي يقتل الأطفال" في قاعدة الدوحة، ومخازن الوقود في قاعدة علي السالم، ومستودع الذخيرة في معسكر عريفجان في الكويت.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/85001" target="_blank">📅 08:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85000">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-pwauMQ-BC-rTAL-lQuS45FvGkJ1JoPjq5zEsLXIta9IssfbY7LG6UrVDmHLTqRUC_QWyCinVVLmkMkPIhva8pWTdAtYf7E6WTyR6lglDxIjfNVboT1wjyAb4jPbrPqHnrHV-7_S7uNs_Z3cuGu5faZoHc3PmkUO0gT5QezomwSzb5TwTXvnzdYeLP0XHHOoF8uziprdC4aVBIKDn01_MVs-Vmqr7vWbMNwKjhvQCc8D4F2T0RlZoYU7khao3e28ZGkVGEcT_h4ic4_uxCpZTI9Ei97seq7Vai7Zou2l77yjO7DT9zH2BjwOBWuwHHYG2y6JEX7XjxzUcgbEB03hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
استمرار ارتفاع أسعار النفط إثر تزايد حدة الصراع في الشرق الأوسط حيث وصل سعر برميل النفط الواحد إلى مايقارب 97 دولار</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/85000" target="_blank">📅 07:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84999">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇺🇸
تقرير عن صحيفة أمريكية:
في هجماتها على القواعد الأمريكية في الشرق الأوسط، استهدفت إيران أماكن الطائرات المسيّرة، وأنظمة الرادار، ومساكن الجنود، وغيرها من المنشآت، وفقًا لتحليل مرئي للمواقع التي تعرضت للقصف. وتشير هذه الهجمات، التي وقعت خلال الأسبوعين الماضيين واستهدفت تسعة مواقع أمريكية في أنحاء الشرق الأوسط، إلى أن إيران لا تزال قادرة على إلحاق أضرار بأهداف محددة بدقة. ويأتي هذا على الرغم من ادعاءات البيت الأبيض المتكررة بأن القدرات العسكرية الإيرانية قد تضررت بشكل كبير أو دُمرت.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/84999" target="_blank">📅 07:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84998">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03b60f00f7.mp4?token=a6x1Du2gwu-yS22Upfh3gPhNj5EjTbBoVD6GlLwievDtpvyxjBhtmvyaNfUfm5euWWDT9jpx9MAx-TJpsY9lwDwm8lSs9YIcmNFrikLcGyBsPmgodEJJURiwCgnsCw0L2ATk-Rr4a3keC21NhdmOnz7fWvmnyS93FdP_d_NiefpYSSNHEHBwn2mkYNYOou38Z2di2wveNmMCv0m0BYCw9QxWdlOn4ykQge2QC4kAJ31ymOn1AypuTMISRy01UvzYPDkebiz4DGtNbtNUIfpZbr-fQM4hIE9YnqXfoFnN4CzcvWURG__qwXPSW4Sp31KLemCJDZ07nuSixbFvWUbMsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03b60f00f7.mp4?token=a6x1Du2gwu-yS22Upfh3gPhNj5EjTbBoVD6GlLwievDtpvyxjBhtmvyaNfUfm5euWWDT9jpx9MAx-TJpsY9lwDwm8lSs9YIcmNFrikLcGyBsPmgodEJJURiwCgnsCw0L2ATk-Rr4a3keC21NhdmOnz7fWvmnyS93FdP_d_NiefpYSSNHEHBwn2mkYNYOou38Z2di2wveNmMCv0m0BYCw9QxWdlOn4ykQge2QC4kAJ31ymOn1AypuTMISRy01UvzYPDkebiz4DGtNbtNUIfpZbr-fQM4hIE9YnqXfoFnN4CzcvWURG__qwXPSW4Sp31KLemCJDZ07nuSixbFvWUbMsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الجيش الامريكي:
في تمام الساعة 10:30 مساءً بتوقيت شرق الولايات المتحدة يوم 22 يوليو، أكملت قوات القيادة المركزية الأمريكية (سنتكوم) جولة جديدة من الضربات على إيران لليلة الثانية عشرة على التوالي.
استهدفت القوات الأمريكية مواقع عسكرية إيرانية، شملت قدرات بحرية، ومواقع تخزين صواريخ وطائرات مسيرة، ومواقع مراقبة ساحلية، وأنظمة دفاع جوي. وتُضعف هذه الضربات قدرة إيران على مهاجمة البحارة المدنيين والسفن التجارية.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/84998" target="_blank">📅 06:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84997">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86300c639c.mp4?token=nPMGFaB9MK45oZ5SoAvQem5Fn6iIJtuibiGT1oPiSbRIilnhbMn1QMIq0GsULFDEZzzllMeDoLSiLaUbl18bixAvCoXVF8QRxuXlzBK0ur5GKVZLBHND5rgiA08-EJAVch2Gcmsr7sZKk-a5z8uxCB6q-udLPYAwYCtfKvtpt_yOwDE4cdEaLrb7wfdvIJIph4VaZbJ0IF9IMCUxcyjfebqFYhNB6aunn0rdWAgwrzsYHjllYMjmKlB0drfCK-YPPOoPVuCITJvfgTBZELte3RtYPW9ksifi6HjwXww4HG_ahsFFX7ixdLBN1kAY3Xv5sU93J-RLLOM68WqmBzHTkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86300c639c.mp4?token=nPMGFaB9MK45oZ5SoAvQem5Fn6iIJtuibiGT1oPiSbRIilnhbMn1QMIq0GsULFDEZzzllMeDoLSiLaUbl18bixAvCoXVF8QRxuXlzBK0ur5GKVZLBHND5rgiA08-EJAVch2Gcmsr7sZKk-a5z8uxCB6q-udLPYAwYCtfKvtpt_yOwDE4cdEaLrb7wfdvIJIph4VaZbJ0IF9IMCUxcyjfebqFYhNB6aunn0rdWAgwrzsYHjllYMjmKlB0drfCK-YPPOoPVuCITJvfgTBZELte3RtYPW9ksifi6HjwXww4HG_ahsFFX7ixdLBN1kAY3Xv5sU93J-RLLOM68WqmBzHTkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في ميناء جاسك جنوبي إيران</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/84997" target="_blank">📅 05:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84996">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انفجارات في ميناء جاسك جنوبي إيران</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/84996" target="_blank">📅 05:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84995">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">استهداف سفينة قبالة السعودية</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/84995" target="_blank">📅 05:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84994">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇺🇸
الخارجية الأمريكية مجدداً: ‏
تحذير عالمي: نظراً لتصاعد التوترات في الشرق الأوسط، لا تزال البيئة الأمنية معقدة مع احتمال حدوث تصعيد غير متوقع.
ينبغي على الأمريكيين الموجودين حاليًا في الشرق الأوسط توخي الحذر واليقظة التامة، والاستعداد لإلغاء الرحلات الجوية، وإغلاق المجال الجوي بشكل دوري، واحتمال حدوث اضطرابات في السفر. وقد أرجأت بعض شركات الطيران في المنطقة استئناف رحلاتها المجدولة سابقًا، بينما ألغت شركات أخرى بعض خطوطها.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/84994" target="_blank">📅 05:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84993">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇷
نائب محافظ خوزستان: شهيدين و11 جريح حتى الان جراء العدوان الأمريكي الغادر على منفذ الشلامجة</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/84993" target="_blank">📅 04:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84992">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBl4gGxs0bBbxbvZfdGjsQvUj0-NZcAmTwDuNEuni1Iqko7KBlgUXhTj_7SVyXjs5rmtR5zN71ltwkdnSvIJR9RfyJmRj4to82kzlaky6HVm1JIh2NKiD_KeZW3DWGSM14frrY-i-z-wRH03dTT7waPLqmCm-GBjWb8Lqxi1mSwFHoyYWmZnAeqg3KPF0S1U4NYMh_Km_kS0EjM07oQUnFN5utW5pbbURP-hOtORHT8edtPe4Cbb-kXdWZT4fNiZPKfPX_eLkE4Vm8mtLjeNw-ZiMgB_kjP7pfIpnpjIRIR2olMHYJiugmGhV0AGcRPitMUR4NR8zbVYub7Fk1eACw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏تقوم طائرة الإنذار المبكر والتحكم المحمول جواً من طراز E-3G Sentry AWACS التابعة لسلاح الجو الأمريكي الآن بإصدار إشارة 7700، معلنة حالة طوارئ بعد قضاء ساعات في العمل فوق السعودية.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/84992" target="_blank">📅 04:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84991">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">توثيق يظهر وجود مدنيين في مكان القصف الأمريكي الغادر على منفذ الشلامجة ماأدى إلى إستشهاد عدد منهم.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/84991" target="_blank">📅 04:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84990">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b305e0fb5c.mp4?token=VG4cOnPxsQq61nopAMuB1iwpceWe70CNcOkYiKppI5qESYnBP0-9uLhArvOlW4XNHavw01B9OiDHvvdd66y7FChEU7SUYHgLOYe7mvV0NVm8MjJ_5NxsMy24mr4ddp5QSDjO5aZK0XZVFh7R9lWEBVckYHepWlKPbz-k3fjxN0yXEPskIgEuf-1LiuSqF3UcXDWsWVxP2rNLHURkG1QTci4fuS-bUWS3QMoeeIBuzvKeZWHxGQFnRJYi9O3ZpTdDKXsJigzVpG9JO5fP4Xg9a67laXmDTqWmGqJu3FARWIQsRtzxtQcR2uU36-4QFS3pXK7bIjRryZtToCDW_YX91g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b305e0fb5c.mp4?token=VG4cOnPxsQq61nopAMuB1iwpceWe70CNcOkYiKppI5qESYnBP0-9uLhArvOlW4XNHavw01B9OiDHvvdd66y7FChEU7SUYHgLOYe7mvV0NVm8MjJ_5NxsMy24mr4ddp5QSDjO5aZK0XZVFh7R9lWEBVckYHepWlKPbz-k3fjxN0yXEPskIgEuf-1LiuSqF3UcXDWsWVxP2rNLHURkG1QTci4fuS-bUWS3QMoeeIBuzvKeZWHxGQFnRJYi9O3ZpTdDKXsJigzVpG9JO5fP4Xg9a67laXmDTqWmGqJu3FARWIQsRtzxtQcR2uU36-4QFS3pXK7bIjRryZtToCDW_YX91g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
استمرار توافد زوار أبي عبدالله الحسين عليه السلام من الجانب الإيراني إلى العراق عبر منفذ الشلامجة عقب العدوان الأمريكي الغاشم.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/84990" target="_blank">📅 04:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84989">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49dc03cc40.mp4?token=soYOBBZsP-e56mgepUE5lcxFKcm4O1ESGGIf4lcPML_Y90K_z5Iux7ZBP8b4lBbKZd4fCh6mgSiRXIRNXcPpxyCXvuAsq-soAeMIb9-bk1qy9IrAMMYW5VYChJiw5AOqHDV6YszaYaD0FNYF0B310mMrj7KvGuJUTC_4rvcPrYeC10lYjC7C-6lppsKRQANNXFSEWT8PKEkQhVxpKJfWLW9-ALIeHEM7hnMwz2API15tnq66OUaaP-OTcHUdrU_Xc_sYeQXVMC4xpsNscmd9StvwbAFcWDzrEnJXSAPCsYHXCexXH627ato_-ke7QjNuF4pf69QPC3L3bmbhZZXdOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49dc03cc40.mp4?token=soYOBBZsP-e56mgepUE5lcxFKcm4O1ESGGIf4lcPML_Y90K_z5Iux7ZBP8b4lBbKZd4fCh6mgSiRXIRNXcPpxyCXvuAsq-soAeMIb9-bk1qy9IrAMMYW5VYChJiw5AOqHDV6YszaYaD0FNYF0B310mMrj7KvGuJUTC_4rvcPrYeC10lYjC7C-6lppsKRQANNXFSEWT8PKEkQhVxpKJfWLW9-ALIeHEM7hnMwz2API15tnq66OUaaP-OTcHUdrU_Xc_sYeQXVMC4xpsNscmd9StvwbAFcWDzrEnJXSAPCsYHXCexXH627ato_-ke7QjNuF4pf69QPC3L3bmbhZZXdOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
على الرغم من العدوان الأمريكي الغاشم.. مصدر إيراني لنايا: حركة مرور زوار الإمام الحسين عليه السلام في منفذ شلامجة الحدودي مستمرة.  "لو قطعوا أرجلنا و اليدين...نأتيكَ زحفاً سيدي يا حسين"</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/84989" target="_blank">📅 04:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84988">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccdaf35a1f.mp4?token=TnVc64yxOgijYKsakOCLwnP1ny2545VZBi76iFeinrEwiHhYBg3sSE6_g7gGKmLIDPO4rucTvR-Ji0sZRMriXhzrjm0nctMtEXKtE_iFjHVX1qZ-Otn3VBLCNSwwpn3NDj5Ng2Kn1-9-BrtKncA0vsRNRB6iRRzwuMHVlAU2nfvK82pNVzdpi92ikcZ7cdhiyTMOm8jB2fhGFyyVQn-6zOIhHHVJ4urcnGSGDuBLh2Nji-rMzA65TaAa6VDMg3xgZIeLVvvADg5SU_rIwo_Qbl3ZpyXe2fCyKOTmwBy3heBPqU-YiSnSt-cH0gNd3AQ0fOZ_VxOifLG68hSoU6aQLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccdaf35a1f.mp4?token=TnVc64yxOgijYKsakOCLwnP1ny2545VZBi76iFeinrEwiHhYBg3sSE6_g7gGKmLIDPO4rucTvR-Ji0sZRMriXhzrjm0nctMtEXKtE_iFjHVX1qZ-Otn3VBLCNSwwpn3NDj5Ng2Kn1-9-BrtKncA0vsRNRB6iRRzwuMHVlAU2nfvK82pNVzdpi92ikcZ7cdhiyTMOm8jB2fhGFyyVQn-6zOIhHHVJ4urcnGSGDuBLh2Nji-rMzA65TaAa6VDMg3xgZIeLVvvADg5SU_rIwo_Qbl3ZpyXe2fCyKOTmwBy3heBPqU-YiSnSt-cH0gNd3AQ0fOZ_VxOifLG68hSoU6aQLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد حصرية  لحظة تنفيذ العدوان الأمريكي الغادر على زوار الإمام الحسين عليه السلام في منفذ  الشلامجة الحدودي.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/84988" target="_blank">📅 04:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84987">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3d5fe3494.mp4?token=KmvlcduRwj8By3qjIa507r6dmRXSgmzJtpxDZyaLoAi4_MO4O_0OMbnDPzj2Qsd1WTOmwspMLv2XbqBIT-wgsEIhDNgDR8eDUNMJWsoRvY7iPuPeD41efvx9nYVSJ4gbjmTBkfUjF7At38XGuOwGLHeMBdy1jiNiUlLuFiXuFB-qglq0wUnHS8xZEm9mfPHgAaHj0Fc1BkHsnYETA6iltPf7C3zf45klh_kOQYe3jEkEHkucX0KJNoBLlIvHpg5h6ZJCO55c8Ro7HxwFWscbSGxtFE2IoxJy5bA1dOB2Q85yOE2oWM81bwa0lyNHTHknRfAyXBaPHmjYd9Lz67j6OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3d5fe3494.mp4?token=KmvlcduRwj8By3qjIa507r6dmRXSgmzJtpxDZyaLoAi4_MO4O_0OMbnDPzj2Qsd1WTOmwspMLv2XbqBIT-wgsEIhDNgDR8eDUNMJWsoRvY7iPuPeD41efvx9nYVSJ4gbjmTBkfUjF7At38XGuOwGLHeMBdy1jiNiUlLuFiXuFB-qglq0wUnHS8xZEm9mfPHgAaHj0Fc1BkHsnYETA6iltPf7C3zf45klh_kOQYe3jEkEHkucX0KJNoBLlIvHpg5h6ZJCO55c8Ro7HxwFWscbSGxtFE2IoxJy5bA1dOB2Q85yOE2oWM81bwa0lyNHTHknRfAyXBaPHmjYd9Lz67j6OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عجلات الإسعاف تجري عملية إنتشال الشهداء والجرحى من مكان العدوان الأمريكي على منفذ الشلامجة الحدودي</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/84987" target="_blank">📅 04:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84986">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8e0fb0bb1.mp4?token=DeEQKpNEbjrcgc8XmYp4e-nup9TweLLn_LUKpH_VLTxORMnWQ2_JVAQ0CasIGwpxUQGthzbeW0MJ9BwMZ3GSS89GSpNogBii82xZljPtLoSXq_01X93S7me2vQWubV0vTDehVjhFFNwhI7JF13Bvob8AThzBHXDlGR9RBNW7cxh9k6axbYu93po6yWXAWDdrW0Chakkg8nLduXnNc-f-ZRGI779pZQK9NzZZ9CjdHfABNkzr6ORxAZcPtcldhRz4IMLsGP2_bQfxxyUEHYBmDn0DARHG8IxkXNQwRWaO_UdpeV1VdJXLt4UAdWHi5SZtRPfKE2faASu4uK0z-5e6JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8e0fb0bb1.mp4?token=DeEQKpNEbjrcgc8XmYp4e-nup9TweLLn_LUKpH_VLTxORMnWQ2_JVAQ0CasIGwpxUQGthzbeW0MJ9BwMZ3GSS89GSpNogBii82xZljPtLoSXq_01X93S7me2vQWubV0vTDehVjhFFNwhI7JF13Bvob8AThzBHXDlGR9RBNW7cxh9k6axbYu93po6yWXAWDdrW0Chakkg8nLduXnNc-f-ZRGI779pZQK9NzZZ9CjdHfABNkzr6ORxAZcPtcldhRz4IMLsGP2_bQfxxyUEHYBmDn0DARHG8IxkXNQwRWaO_UdpeV1VdJXLt4UAdWHi5SZtRPfKE2faASu4uK0z-5e6JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
على الرغم من العدوان الأمريكي الغاشم.. مصدر إيراني لنايا: حركة مرور زوار الإمام الحسين عليه السلام في منفذ شلامجة الحدودي مستمرة.  "لو قطعوا أرجلنا و اليدين...نأتيكَ زحفاً سيدي يا حسين"</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/84986" target="_blank">📅 04:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84985">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">من العدوان الأمريكي الغاشم على منفذ الشلامجة الحدودي بين إيران والعراق</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/84985" target="_blank">📅 04:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84984">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">2 شهداء كحصيلة أولية جراء العدوان الأمريكي الغاشم على منفذ الشلامجة</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/84984" target="_blank">📅 04:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84983">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a666f918cb.mp4?token=ReZ6mp_0Jqyn1pqQMNPZbMXkf3Z87JanTxPUuu6f1NwS2kNMzN47TqKXfNTsL6clEAovHnuffmKmIWLKkEXefZa7CzO7zdKW-WRDVHyf0RCYXopDpX-C4mCJ7OfqDEO9oQtWJ0itF__ocu7hC-wQX6laIHc4SmeZHbFOG5W5W7aJmekssQSptXtMA8sD0K2hbA1R-F995TaYSgcMK9T0MCOKl-y25ufJuMKSb2BT8Wr46ft9oVhl0lAsI7-NEWcOITKfzACkT460TnkF9GFtKBz3B-GJzPE0g6REyfNymD1ipyWVZ7WfmHDI4eYTWRDkHi9rxW1BbRQhvvibYO_8ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a666f918cb.mp4?token=ReZ6mp_0Jqyn1pqQMNPZbMXkf3Z87JanTxPUuu6f1NwS2kNMzN47TqKXfNTsL6clEAovHnuffmKmIWLKkEXefZa7CzO7zdKW-WRDVHyf0RCYXopDpX-C4mCJ7OfqDEO9oQtWJ0itF__ocu7hC-wQX6laIHc4SmeZHbFOG5W5W7aJmekssQSptXtMA8sD0K2hbA1R-F995TaYSgcMK9T0MCOKl-y25ufJuMKSb2BT8Wr46ft9oVhl0lAsI7-NEWcOITKfzACkT460TnkF9GFtKBz3B-GJzPE0g6REyfNymD1ipyWVZ7WfmHDI4eYTWRDkHi9rxW1BbRQhvvibYO_8ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان الأمريكي الغادر الذي طال منفذ الشلامجة الحدودي أثناء مرور وعبور زوار الإمام الحسين عليه السلام من إيران إلى العراق.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/84983" target="_blank">📅 04:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84982">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/653394b365.mp4?token=WivgHCzhRZDVhKtyY8nFEVXSx6IdQc7dFaXDolvBG3jamt5t_3Q8VatI8v_X0yui-bFrv8bzMHHWzaqU_8_P9b5E-brngKPWNyvOkFDyxwr4G9Njp0ACDRcZ5fGcZ1mQ1RZtfBrLz_4gRgn4AU2jXMpPH1soMCZ00Poo72SMRE81RWKvOBs-DwRPiaRFeYGkSiNCMVX0LCMc4WGSasAS2Z_RB1I5x-Lbwnz4-Osrhwf2YLcDqdSUTzE8JzBWuxntTEdKvijHwoYq4YpLiMmEUlqlKREj34KcpIAYHL6YAcOfS1ZsMTfEDMV-lnZFOQz92ocJRt3c6oAV4e5P8OfyGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/653394b365.mp4?token=WivgHCzhRZDVhKtyY8nFEVXSx6IdQc7dFaXDolvBG3jamt5t_3Q8VatI8v_X0yui-bFrv8bzMHHWzaqU_8_P9b5E-brngKPWNyvOkFDyxwr4G9Njp0ACDRcZ5fGcZ1mQ1RZtfBrLz_4gRgn4AU2jXMpPH1soMCZ00Poo72SMRE81RWKvOBs-DwRPiaRFeYGkSiNCMVX0LCMc4WGSasAS2Z_RB1I5x-Lbwnz4-Osrhwf2YLcDqdSUTzE8JzBWuxntTEdKvijHwoYq4YpLiMmEUlqlKREj34KcpIAYHL6YAcOfS1ZsMTfEDMV-lnZFOQz92ocJRt3c6oAV4e5P8OfyGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أمريكا تستهدف زوار الإمام الحسين.. تصاعد أعمدة الدخان عقب عدوان أمريكي غادر وغاشم على منفذ الشلامجة الحدودي بين إيران والعراق.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/84982" target="_blank">📅 04:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84981">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مجدداً.. عدوان أمريكي على مدينة بوشهر</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/84981" target="_blank">📅 04:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84980">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a29c1cb506.mp4?token=QbvI05Le15kmE_CXQQhz8KrWs8e_sVyBCqvhOT3KWI8QJ_pvGoVG2XGbW91lzCDEc6whE6ZW1SnTDeajdzxAwfN8FKw_WFuoN1yYqOGXhd83H0cITcEzsZZ_V86B0x92pNESxCSC4CeOFA2Llxygpkr2KJeJykVwpT7OTdt_o7jMLhkZDPnuYl9aDQqB6mr0go3mKhPUBdctkj_7XUHk4Vcfml3lfv2PkQL8g_amI4AN8x3QUrTo5dktRPf8PiK3puJ1jNPWhtTx7cn7enTMKJvGX6L2QJJ3vYcdXitU9gi7Z2OXEHhid_cxz5k7kD_bSWfcdGK2vSAFzXtj6LTX1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a29c1cb506.mp4?token=QbvI05Le15kmE_CXQQhz8KrWs8e_sVyBCqvhOT3KWI8QJ_pvGoVG2XGbW91lzCDEc6whE6ZW1SnTDeajdzxAwfN8FKw_WFuoN1yYqOGXhd83H0cITcEzsZZ_V86B0x92pNESxCSC4CeOFA2Llxygpkr2KJeJykVwpT7OTdt_o7jMLhkZDPnuYl9aDQqB6mr0go3mKhPUBdctkj_7XUHk4Vcfml3lfv2PkQL8g_amI4AN8x3QUrTo5dktRPf8PiK3puJ1jNPWhtTx7cn7enTMKJvGX6L2QJJ3vYcdXitU9gi7Z2OXEHhid_cxz5k7kD_bSWfcdGK2vSAFzXtj6LTX1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان الأمريكي على منفذ الشلامجة الحدود</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/84980" target="_blank">📅 03:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84979">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rxgf2b1iucseryZsWTKUaYpcAzPO7vmoWJ7aPknhU_lC1b6-Yraso6AqxCVIVO-x1BAbDQnlZhzoDejoZ11S5pGS_jhzf6frgJQr0lonfU_dYFe8q_vCgAEtoh8f4Ytl-39n5LrBzqgkxjec6mclJ46neLYo-6k_dbidzwevSBJdAnJwZ9JzFLhuFCqcUkMT4D4onBtZ2FpnehrKUv3-b_rFLnOlb_QrflizNJYrx9Ea2v8J4eNIy3hbRvNWaqhPjpMyKeiRUNwKG7opmo682OLkxXg94nTFR8HDRpCJ_v-hXma9S4E6Dh1de36iEIOJn5Ur075n0vRVnRevK-RYIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من العدوان الأمريكي على مدينة "اسلام آباد غرب" في كرمانشاه الإيرانية.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/84979" target="_blank">📅 03:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84978">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b220c708f.mp4?token=MbKAGuDo6No3g3ZGuifWt3u1aL7H-4PzcmbRz3qmil3LtgzktE6d3jipNpfMmORXsiF4uLc4M-n1e0vwK2bv8mkT9oXezqIvlcLmjhZPwB2Pe_Jn8Vh-56h0bFxuoC5K5-eJfA7FH7Ynbq2RpmWAbEQGEojRe74mNI5wtZMPmwMdknmE_q3gqpB4gQ8uUK8kuDT2MbOJZEsbz0DCD3qhXcqWNwTQRwRzRebRClW_jPNioFPk5BIPaOKH5lSZwX59QiE6XtE7BRkFPa_R_KrP1cOEgIGjckH0IUXhOqPejy4njUQ6Gi4Xn9UYXNKaKHIhe0KBimqDfwP9YOdgCr1h2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b220c708f.mp4?token=MbKAGuDo6No3g3ZGuifWt3u1aL7H-4PzcmbRz3qmil3LtgzktE6d3jipNpfMmORXsiF4uLc4M-n1e0vwK2bv8mkT9oXezqIvlcLmjhZPwB2Pe_Jn8Vh-56h0bFxuoC5K5-eJfA7FH7Ynbq2RpmWAbEQGEojRe74mNI5wtZMPmwMdknmE_q3gqpB4gQ8uUK8kuDT2MbOJZEsbz0DCD3qhXcqWNwTQRwRzRebRClW_jPNioFPk5BIPaOKH5lSZwX59QiE6XtE7BRkFPa_R_KrP1cOEgIGjckH0IUXhOqPejy4njUQ6Gi4Xn9UYXNKaKHIhe0KBimqDfwP9YOdgCr1h2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في محافظة كرمانشاه</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/84978" target="_blank">📅 03:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84977">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/criDKsNFabFvHoSXTA0ZNvfvjGZSCUwKxvegFTSbw0bDQ8UaE78XPq1jHSi9GoOeoN99vRZN97f-hoik48MWFIB73xPCk0hdrDr8cnOxqozzeqAqAXymPIQ5wpUU3CaVvRtAVGOwbudmnLaNS0XQxxYAZA_PYIT5GHQsry8imeBPbGH9J_lYAmFH0eNCwUJ1qZD3Ipj4Pk71SDqSl0FrXhmjVdjzpnGzzfrDiDNicxFz5mFp6Q-tfWB8j0V6olEok_iMwtTxMPGEOuuG6lC01Ic0m1mh6zY29V5BbuhLneePfraRAXIk5Bk78aVUHPt-pn-ZpF6gU2gH6nRJo0PrwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طيران مسير يحلق في اجواء منفذ الشلامجة أثناء تنفيذ العدوان الأمريكي</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/84977" target="_blank">📅 03:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84976">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">انفجارات في محافظة كرمانشاه</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/84976" target="_blank">📅 03:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84975">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3402cb9cd2.mp4?token=v_ciKfYz8u1TPZ3PCKLOWubD-c_A15h-9HvddZGoUOhRxOIdMNlJBukAeByAdd9AeyNdVk9aw7pR3tMrpaC2N949ADhJH2r78vq2xT9RNU519Z-GJjO-9uxmnpQkL-NXweDeSqrDobia0FZc-e9qW_AhhLdTA5aGbG4JkN3us-8uHOE2zw5Quf7opVeL-wQvScL5iK9N6nJwfsUxCNoZwzcF-lsQZOvmd680-bSQ97xLysNiPENP5cEREYMmFSZ7X2NgT22SCGXs0Pn2Ovrn49NY9r0-N-Noj3pzF8fj5oNlhcke-TIMcqeyzfsfq03P1Et6JEaLEJaDeaDQlXifJoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3402cb9cd2.mp4?token=v_ciKfYz8u1TPZ3PCKLOWubD-c_A15h-9HvddZGoUOhRxOIdMNlJBukAeByAdd9AeyNdVk9aw7pR3tMrpaC2N949ADhJH2r78vq2xT9RNU519Z-GJjO-9uxmnpQkL-NXweDeSqrDobia0FZc-e9qW_AhhLdTA5aGbG4JkN3us-8uHOE2zw5Quf7opVeL-wQvScL5iK9N6nJwfsUxCNoZwzcF-lsQZOvmd680-bSQ97xLysNiPENP5cEREYMmFSZ7X2NgT22SCGXs0Pn2Ovrn49NY9r0-N-Noj3pzF8fj5oNlhcke-TIMcqeyzfsfq03P1Et6JEaLEJaDeaDQlXifJoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أولى لحظات العدوان الأمريكي على منفذ الشلامجة</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/84975" target="_blank">📅 03:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84974">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">عدوان أمريكي على مدينة انديمشك</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/84974" target="_blank">📅 03:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84973">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34216a257c.mp4?token=LSeKA_pVC9q51xIeMis0D1bRpdfNh4RqaIQoNg4XMIPXxQ7o--UMl-QEuJXDR0SxPbX6zOfZHksplLMj3dR3sKvlzRQxPa19G20vwoxq7VuMaGcgFKz7x3UpoPY7riuXav5plK7krvWXXFDSbkFx8F0QyePYXqQNkJI_86AFSGvVVbjUjrBE6mynrkozxL88JISgxkba4YTP2GEBPZOGWdmssJet9IyCz_vaW7NzjD5n9IrqosdXj4RhsfFIGsZpFeIfBRx7Ih8y4dmCcIhbFA3Ksk9ut9YkuekQlBCU0sZ60oojwNoQsnq6DcG1MszxXjq3ZHu01oP-9mfqw6E0_jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34216a257c.mp4?token=LSeKA_pVC9q51xIeMis0D1bRpdfNh4RqaIQoNg4XMIPXxQ7o--UMl-QEuJXDR0SxPbX6zOfZHksplLMj3dR3sKvlzRQxPa19G20vwoxq7VuMaGcgFKz7x3UpoPY7riuXav5plK7krvWXXFDSbkFx8F0QyePYXqQNkJI_86AFSGvVVbjUjrBE6mynrkozxL88JISgxkba4YTP2GEBPZOGWdmssJet9IyCz_vaW7NzjD5n9IrqosdXj4RhsfFIGsZpFeIfBRx7Ih8y4dmCcIhbFA3Ksk9ut9YkuekQlBCU0sZ60oojwNoQsnq6DcG1MszxXjq3ZHu01oP-9mfqw6E0_jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أمريكا ترتكب جريمة حرب جديدة بعد إستهداف منفذ الشلامجة المكتظ بالمدنيين.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/84973" target="_blank">📅 03:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84972">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e89fd739.mp4?token=QEPeKAnuMkRj9bbV0tHdTKwAih71xMIE5fV0HK0M6XS33xWHv5EL8IQdn-2EsGJ8o3_WY-N5cz-yd5YTG-wZAtqmL_vrY-PRlC2P8Z0e2xFxxcWtbKNrzoPZTk7uv27ONMC559kn0k0If9L9DVqFgxrtpx1oZMw4l5kJuO4iWxxgYBMYqhPRMHXuo9SUyTQwV1pVYbRuwzHihqja0kC_ZTDz7DSpt-iSMF2skxfDsaKvfzUIlHFhRD4vrNfAKJvHJBxj4ZnJhVyIKVv9GFYHFB_qUKND7Tfy8qIderXCYOmX7Coexl01aEfHSFEhWRGYqqJg_vDKg50gkayY5WxmHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e89fd739.mp4?token=QEPeKAnuMkRj9bbV0tHdTKwAih71xMIE5fV0HK0M6XS33xWHv5EL8IQdn-2EsGJ8o3_WY-N5cz-yd5YTG-wZAtqmL_vrY-PRlC2P8Z0e2xFxxcWtbKNrzoPZTk7uv27ONMC559kn0k0If9L9DVqFgxrtpx1oZMw4l5kJuO4iWxxgYBMYqhPRMHXuo9SUyTQwV1pVYbRuwzHihqja0kC_ZTDz7DSpt-iSMF2skxfDsaKvfzUIlHFhRD4vrNfAKJvHJBxj4ZnJhVyIKVv9GFYHFB_qUKND7Tfy8qIderXCYOmX7Coexl01aEfHSFEhWRGYqqJg_vDKg50gkayY5WxmHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">2 شهداء كحصيلة أولية جراء العدوان الأمريكي الغاشم على منفذ الشلامجة</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/84972" target="_blank">📅 03:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84971">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔻
مصدر لنايا: ارتقاء عدد من الشهداء جراء العدوان الأمريكي الغاشم على مقر للجيش الإيراني في منفذ الشلامجة الحدودي.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/84971" target="_blank">📅 03:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84970">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33a2e2e1ca.mp4?token=hcSVVd-6ZYbf5RdX6p7m9UchvC208edFztwIydbb59RgXvL7Er5nefE3topkBy7Ju4It1D0Ijhx_moZ7iU5BSZIVj07kOpikA1NE1AcjGKT6zp1uggcf_8Ea1h-rEr7awcoSO_oIrYfRmmBKxC4pddwFuaJ-fDaXX5y12gL_LEXAKduG7MYR_Iq-rwMKoEcqs8l-m_d5wZCTTCnPeKgWgyJRWGLzvPMHURk-FcY9--qbRw4Jz6W5UOBYbAZ6cYQ4wJjQ0avhCqwPICNxAKhLEU1PQr6dRqx6hcbu_CNH-qUk7u1KYMklQtgGBtvuf7N7wTwo_0p4it28JzriX341FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33a2e2e1ca.mp4?token=hcSVVd-6ZYbf5RdX6p7m9UchvC208edFztwIydbb59RgXvL7Er5nefE3topkBy7Ju4It1D0Ijhx_moZ7iU5BSZIVj07kOpikA1NE1AcjGKT6zp1uggcf_8Ea1h-rEr7awcoSO_oIrYfRmmBKxC4pddwFuaJ-fDaXX5y12gL_LEXAKduG7MYR_Iq-rwMKoEcqs8l-m_d5wZCTTCnPeKgWgyJRWGLzvPMHURk-FcY9--qbRw4Jz6W5UOBYbAZ6cYQ4wJjQ0avhCqwPICNxAKhLEU1PQr6dRqx6hcbu_CNH-qUk7u1KYMklQtgGBtvuf7N7wTwo_0p4it28JzriX341FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مساعد الأمن والإدارة في محافظة خوزستان: قبل قليل، تعرض محيط محطة نقل الركاب الحدودية في الشلامجة لهجوم صاروخي من قبل العدو الإرهابي الأمريكي.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/84970" target="_blank">📅 03:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84969">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇷
مساعد الأمن والإدارة في محافظة خوزستان:
قبل قليل، تعرض محيط محطة نقل الركاب الحدودية في الشلامجة لهجوم صاروخي من قبل العدو الإرهابي الأمريكي.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/84969" target="_blank">📅 03:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84968">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔻
مصدر إيراني لنايا: العدوان الأمريكي طال مقر استراحة عناصر الجيش والشرطة الإيرانية في منفذ الشلامجة الحدودي بين إيران والعراق.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/84968" target="_blank">📅 03:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84967">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔻
مصدر إيراني لنايا:
العدوان الأمريكي طال مقر استراحة عناصر الجيش والشرطة الإيرانية في منفذ الشلامجة الحدودي بين إيران والعراق.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/84967" target="_blank">📅 03:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84965">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iiZsnDMoDFtWIQE9p5iRGLT-f6tOhpBkQUrN7sjLJG3ePS8cO4CKKJ12vVHI1wuJpqPgguT0E--kQ9N8_248NaSS2MFu6NXr9jbf4FBg7Ro35LfPgeqDv35K_ba9Ow7kQPipnJGUvNrV3rpMROPid9zolovVK7Z7efVs2zpfnOh32Yxb7cplv_ztXHvTdluY2KniVC8RKBFRK6Fs69xQZx0EL4eqeKiCqpm3SsXIlj3G8_5oj3AjDtJN08QovYINh7lzD8ud7pecIRCC1GzGx2_-gpuff8bFtqsQlQqHk_LXmaCfPqeQLKmZ9rGhclJLZV_YzbVMGzpEjN65V6xKDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IXjoAw9fY9tQYI8Bp4oyfk3evgXLAjVpo5fkRZim6kmtdjgi2cyaD3rk0Go8lNjBm--zMS301YvXNgeKnNzZMzF6fOxgXWCtgZrBBJC5wYE5x92OGyAZBHGxNZkXuK_X6lmr5a12nZ2UYePcrzpZlJ9VydAzKoCHiZDR2oKcbKhlCiiEOvALaNH0IdO0ykEx-4Z0vFljaCYiSfWDPqrJ3FvxOxvqeVM9sFXjp7XevQant44EHe97eJ8zNGWbrGH-NfpiRuOwn3QyBARDJD1WsGtq9TKzEEgvDpOA20wuuJRT7C7KklWNj3zg7nJAIs27QMpR9Jo12gR_PoG33ZgyQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاعد اعمدة الدخان من منفذ الشلامجة الحدودي</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/84965" target="_blank">📅 03:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84964">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/377fb136c5.mp4?token=iNt2R_ysmy2a-GSyBE0xh0StTg1DABibc4FkqyAm3xmwJ8a4ME7cAvLpOQjaUwY5o_b9dRQRpbU86k5XOcb6KQBtiOJWeqMzbehpuZe661kH4N5qenCaHRg-oraBsblg-lLmDiD1pvbpD2Gdo_QZWHuBzDu4PJNG2OAMRTkjLUj5Q9NkBaBYq2c-6LYovV__Z3SEsnki8NigffZLmmKwu2I5YY4VXUezr6G_2eP5NFS7ivka2iFbOfj8FbPkDfE6fHIbhuFXSUdjxwgeh5muVDSbfyPExwvpz0o3QWCnlRwE_QbYMeqa38y-J8s_jZK03Al--QLHITYwMbOjKNVmog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/377fb136c5.mp4?token=iNt2R_ysmy2a-GSyBE0xh0StTg1DABibc4FkqyAm3xmwJ8a4ME7cAvLpOQjaUwY5o_b9dRQRpbU86k5XOcb6KQBtiOJWeqMzbehpuZe661kH4N5qenCaHRg-oraBsblg-lLmDiD1pvbpD2Gdo_QZWHuBzDu4PJNG2OAMRTkjLUj5Q9NkBaBYq2c-6LYovV__Z3SEsnki8NigffZLmmKwu2I5YY4VXUezr6G_2eP5NFS7ivka2iFbOfj8FbPkDfE6fHIbhuFXSUdjxwgeh5muVDSbfyPExwvpz0o3QWCnlRwE_QbYMeqa38y-J8s_jZK03Al--QLHITYwMbOjKNVmog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد اعمدة الدخان من منفذ الشلامجة الحدودي</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/84964" target="_blank">📅 03:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84963">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">الله أكبر
🔻
الحرس الثوري:
واحدة من ثلاث سفن متورطة كانت تنوي عبور مسار غير آمن في مضيق هرمز اشتعلت فيها النيران، بينما عادت السفينتان الأخريان بسرعة إلى الخلف.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/84963" target="_blank">📅 03:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84961">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca89d96130.mp4?token=gjOqxtUpnp-MH_63r9RTAiTd84gkl2sgBq--qMAhHDserYoQn9KfgZwaBW3ZDX1GAvDSiZkePKurryS06oXwJ_VT8D7d0Svu63uO4dacUtk9TRmqlFcrFJRtgOFx-ugnqaMRMMnWKBWtD1pVglhLCNzdBwRcbPntFl0u_x_LIkNEtZgrzpWKtpnikK5HUBgXR84y7J5MEwSZeAmPYAOWujPmvLYyr8G9cRcTWlUdp-TR0EATtDTVOsE-AQby-lhszrJ_GZ60414SKMrpRYh8EbDQayciGAr57vHFEQ9faUIreSjalsPwKkrxlCWAQs9s3iAvWgHkZ2ydyRbIgeEETw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca89d96130.mp4?token=gjOqxtUpnp-MH_63r9RTAiTd84gkl2sgBq--qMAhHDserYoQn9KfgZwaBW3ZDX1GAvDSiZkePKurryS06oXwJ_VT8D7d0Svu63uO4dacUtk9TRmqlFcrFJRtgOFx-ugnqaMRMMnWKBWtD1pVglhLCNzdBwRcbPntFl0u_x_LIkNEtZgrzpWKtpnikK5HUBgXR84y7J5MEwSZeAmPYAOWujPmvLYyr8G9cRcTWlUdp-TR0EATtDTVOsE-AQby-lhszrJ_GZ60414SKMrpRYh8EbDQayciGAr57vHFEQ9faUIreSjalsPwKkrxlCWAQs9s3iAvWgHkZ2ydyRbIgeEETw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اندلاع حريق مجهول بالجانب الإيراني من منفذ الشلامجة الحدودي.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/84961" target="_blank">📅 03:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84960">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇷
🇮🇱
🇺🇸
سي إن إن:
مدير الموساد الإسرائيلي شارك الأميركيين معلومات تفيد بأن منشأة "جبل الفأس" الإيرانية موقع محصن تحت الأرض وتم ربطها بالبرنامج النووي.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/84960" target="_blank">📅 02:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84959">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇺🇸
وزير الخارجية الأمريكي:
ما يحدث الآن واضح السفن تحاول العبور عبر مضيق هرمز ويتم تفجيرها من قبل الإيرانيين.
الاتفاقات مبنية على الامتثال وقد أبرمنا  اتفاقا مع ايران ثم انتهكته ولم يعد ساري المفعول.
نبقى منفتحين على الدبلوماسية والحل التفاوضي لكن يبدو أنهم غير جادين في ذلك حاليا.
في اليوم الذي كان يفترض أن تصدر فيه إيران البيان استهدفوا سفينة وضربوها.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/84959" target="_blank">📅 02:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84958">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnJT2lKRZiHaf9GoabIYoMTE-KkGnmrWL_YskOhogI33JYtQ5g1gA6O7lB4Nuwz_JtfOHgALgjFByTFmx0lL6Zt1ftPHhLjUY21yZP6dY2Z5qhqWdcaHhme7RpvMNFJMZzgN7xDCILv8DzesJmkt_9Lz0DqIIdKp-kVIz-X6PeUIeU_kOnT2Q2GKieVALkaUIZnSOLMxQ2EZ4snxiADAUGbsavDMa2PmTiH_MOjyMeZGA874dSLohYQZhnYHl3XRW6v-3A1GxbLdBnyX6RcUJgNCkM1UWlWAnAwehpsmXhp_nFl2Mc8Xvlo7mXGjSfCT6tvv_SVkI-bRmmzrdH73ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الطيران المسير الإنتحاري يستهدف القواعد الامريكية في الكويت</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/84958" target="_blank">📅 02:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84957">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سماع دوي انفجار جديد في بوشهر جنوبي إيران</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/84957" target="_blank">📅 01:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84956">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇺🇸
الجيش الامريكي: ‏
في الساعة 5:30 مساءً بتوقيت الشرق الأمريكي اليوم، بدأت القوات الأمريكية في إطلاق المزيد من الضربات ضد أهداف عسكرية إيرانية بتوجيه من القائد الأعلى. ستستمر المهمة لتدهور قدرة إيران الإضافي على تهديد البحارة المدنيين والسفن التجارية العابرة للمياه الإقليمية.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/84956" target="_blank">📅 01:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84955">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/84955" target="_blank">📅 01:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84954">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/84954" target="_blank">📅 01:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84953">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/84953" target="_blank">📅 01:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84952">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohkkwYTLB_0-bm9pX3gfPdvGdSddOgsN_yJ3G8Ee4nrzyYXsSavLGEjD99AGW22SH6Wxd-JLd1BMa3W9jMQKH32yDPIuGKV_PahwJcniRMM_NbBpvnc4vjt1AzpJ8TYIWMfCxEgc9mT918_9zyAkolovMBvJqRclBx4JMeuEmO6JsUfWFDfThsS5S8BgjR11Oo41StheyDocCKCX1INTSO3cLnbmQj-3HH8xgCg7nBIMIy5ZZYh2Ft8TTHKKzRLzeF4XL8uXcXlsM5cs0ijema6XQH6Tz1fsN8BHpWuHTKKfeqHexiEboe1Jjji9DSAzPmhwWdECvOYwzx5CdTh2Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد ان كانت تعتقد انه ُ قتل في الموصل ؛ استراليا تعلن عن العثور على ارهابي من داعش في سجون العراق</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/84952" target="_blank">📅 01:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84951">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQ-lMqHFjjlMJPSmk64UIK7RaUtEo9h7igw2JT3TEYlDDomEJXisMvfgr9PxfO-VvRq3_KX0i2v7SmrXIlWRyleIvC2URLODIhV_Ammr7zZH0aWkb3uHiOFGCEtq8Z_dnBWzZYQOwqmLoPoGG2WkWayg0WVxyKnKpJGyJ828a0AtWC0rroADQ3Bv1hQg-a9a79jfVDFur5S_qYTJfcqn3yYHAh6qbO-1zGtDWEJXi3LMGlwJ5OW2K8VJq1zKxttPMCIRiPXzbKVbAT3Irl8R2jO2492AD7vDWoIAoJk_o8xywkhPjlQ4v8JZy-zEi79qJ_KYMaw2qdk0iBd0Fj6eeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية: ​ نفذتِ القواتُ المسلحةُ اليمنيةُ عمليةً عسكريةً نوعيةً استهدفتْ سفينتينِ نفطيتينِ سعوديتينِ خالفتْ قرارَ الحظرِ الصادرَ عنِ القواتِ المسلحةِ في البحرِ الأحمرِ إحداهما تحملُ اسمَ "ENCELIA" والأخرى "LAYLA" وذلكَ بعددٍ من الصواريخِ…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/84951" target="_blank">📅 01:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84950">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية: ​
نفذتِ القواتُ المسلحةُ اليمنيةُ عمليةً عسكريةً نوعيةً استهدفتْ سفينتينِ نفطيتينِ سعوديتينِ خالفتْ قرارَ الحظرِ الصادرَ عنِ القواتِ المسلحةِ في البحرِ الأحمرِ إحداهما تحملُ اسمَ "ENCELIA" والأخرى "LAYLA" وذلكَ بعددٍ من الصواريخِ البالستيةِ والمجنحةِ والطائراتِ المسيرةِ وكانتِ الإصابةُ دقيقةً بفضلِ اللهِ وعونهِ وتسببتْ في نشوبِ حريقٍ كبيرٍ فيهما بفضلِ اللهِ.
وفي نفس السياق فقد أجبرت القوات المسلحة اليمنية ما يقارب عشر سفن على التراجع والعودة.
​إنَّ القواتِ المسلحةَ ستواصلُ عملياتِها البحريةَ ضدَّ العدوِّ السعوديِّ وإنها مستمرةٌ في فرضِ معادلةِ "الحصارُ بالحصارِ" .
وتؤكدُ للعدوِّ السعوديِّ أنَّ أيَّ حماقةٍ أو عدوانٍ يستهدفُ به بلدنا فسيقابلُ بعملياتٍ كبيرةٍ في عمقِ أراضيهِ وستكونُ عواقبها عليهِ وخيمةً بإذنِ اللهِ وقوتهِ.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/84950" target="_blank">📅 01:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84949">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انفجارات جديدة في ميناء سيريك جنوب إيران</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/84949" target="_blank">📅 00:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84948">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">انفجارات في درعا السورية</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/84948" target="_blank">📅 00:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84947">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دوي انفجار في مدينة ماهشهر جنوبي إيران</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/84947" target="_blank">📅 00:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84946">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVTvFF2wEWN724DkeHG7va6-gCmL6C95sGYvYRdQ5aZD-CIkWk7zV9tgdPOqSOqs9zlP0rHitMN_xBbsFGxtTUrelmYWTqfm1y9XE3zfNTaLYEcje4Ga2IjqTUiCMj9GrkbBYnm-7sCIH9AniRD4vBbeZhevbL7Ezpp10dQmYnVTea5ZNdQH-obPPTDmsOTHHw6KPZgeDdoK-V_vSI7-fbdh-n0jz67M5-5VH0f4cXpzdzvWgaAOzXK2Ftim_qz5omCNMoxjsu0DC2yGhK_IjvXSChgbRHdCWJxX_dW1tdHe_F-P3JkUfLsmJdu9XhVavp9UcKd8iJmOKK9-MqtICA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهداف سفينة قبالة السعودية</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/84946" target="_blank">📅 00:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84945">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انفجارات في مدينة بوشهر جنوبي إيران</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/84945" target="_blank">📅 00:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84944">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">استهداف سفينة قبالة السعودية</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/84944" target="_blank">📅 00:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84943">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/84943" target="_blank">📅 00:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84942">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇺🇸
اسوتشيد:
‏مجلس النواب يتبنى مقترح ميزانية بقيمة 95 مليار دولار لتمويل الحرب على إيران وأولويات أخرى للبيت الأبيض.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/84942" target="_blank">📅 00:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84941">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇷
سماع دوي انفجار في سيريك</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/84941" target="_blank">📅 00:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84940">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇷
سماع دوي انفجار في الاهواز.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/84940" target="_blank">📅 00:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84939">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇶
انفجارات في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/84939" target="_blank">📅 00:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84938">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">وزارة الطاقة الأميركية: أميركا والسعودية تتوصلان إلى اتفاقية للتعاون النووي</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/84938" target="_blank">📅 00:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84937">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">محمد القحوم | زامل تنورة | 2023 Mohammed Al-Qahoum</div>
  <div class="tg-doc-extra">محمد القحوم | Mohammed Al-Qahoum</div>
</div>
<a href="https://t.me/naya_foriraq/84937" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دكوا عروش الأسرة المغرورة</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/84937" target="_blank">📅 00:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84936">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇾🇪
بيان مرتقب للقوات المسلحة اليمنية للإعلان عن عملية عسكرية نوعية.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/84936" target="_blank">📅 00:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84935">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">أنباء عن حدث امني اولي قيد التحقيق داخل الكيان</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/84935" target="_blank">📅 23:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84934">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">أنباء عن حدث امني اولي قيد التحقيق داخل الكيان</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/84934" target="_blank">📅 23:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84933">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/84933" target="_blank">📅 23:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84932">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇪🇺
🔻
تقوم القوات البولندية والألمانية بتعزيز الجناح الشرقي لحلف الناتو بشكل مشترك من خلال تركيب حواجز مضادة للدبابات بالقرب من الحدود الروسية.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/84932" target="_blank">📅 23:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84931">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc6512039.mp4?token=UDJ4KxML48nGMlZc2d7Ps4iwXGD3oLDncDWh1Jd7MGYoNA6Ul76V7pByowTdghd-Vxm48mtPbEjRkI0eUA92B0hH-RDsp6VnDM0301LTVzEYvWVJ347S-N79jT0nCt9xvb8ioEBRWELzl9Kvl8aptjbCdDtRAU7hymKmhQkwcH6Ujuya0tpYBqPCZv8G1mh9E7_EhaWT0lKgoHj0YqjD16i83P1V9TW3glNh4iz60JMmemgy3Rh22WPLWGOGV7rniHAEOn4AK6YGcm9beWGMOGuvT-Xtx5rl6Ehk3JCKJVeUCPtXglJ7ssmQQwoTDgMuBYmx0wfRfXEceAmP_uSudiOQq2EEYbeWyVqZ0qUBjUoY4EmKAPedOq9Pwq_eYSj22meLBfcmf9K1hjaIL6yalHK09jsHc0J-UzqR2q-me6E7dIUrCXuiIYj92UTm5fJeMw1ySxo2tqwLHJqRUA_jUy-o5dXJ4x3PfAg4COK4oG41Ld5-JC1NdXC0KGs_5iWbOI7qCgEd1J1Sut7qkZshsa5s0uDezuwNQrYGH9JzvTkvWaeLU8UhX_skO6Y9OBJHt5qjX841CZsGF2DhZFMGxHB1dG7hF7UBmmQ8GzqaKX1Ocs4mNTq9YDBmU0KnfAYPYht_lTB62ZCQ0TKqzl_A6O6KAYA6fOISjPWoJwIw5Mk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc6512039.mp4?token=UDJ4KxML48nGMlZc2d7Ps4iwXGD3oLDncDWh1Jd7MGYoNA6Ul76V7pByowTdghd-Vxm48mtPbEjRkI0eUA92B0hH-RDsp6VnDM0301LTVzEYvWVJ347S-N79jT0nCt9xvb8ioEBRWELzl9Kvl8aptjbCdDtRAU7hymKmhQkwcH6Ujuya0tpYBqPCZv8G1mh9E7_EhaWT0lKgoHj0YqjD16i83P1V9TW3glNh4iz60JMmemgy3Rh22WPLWGOGV7rniHAEOn4AK6YGcm9beWGMOGuvT-Xtx5rl6Ehk3JCKJVeUCPtXglJ7ssmQQwoTDgMuBYmx0wfRfXEceAmP_uSudiOQq2EEYbeWyVqZ0qUBjUoY4EmKAPedOq9Pwq_eYSj22meLBfcmf9K1hjaIL6yalHK09jsHc0J-UzqR2q-me6E7dIUrCXuiIYj92UTm5fJeMw1ySxo2tqwLHJqRUA_jUy-o5dXJ4x3PfAg4COK4oG41Ld5-JC1NdXC0KGs_5iWbOI7qCgEd1J1Sut7qkZshsa5s0uDezuwNQrYGH9JzvTkvWaeLU8UhX_skO6Y9OBJHt5qjX841CZsGF2DhZFMGxHB1dG7hF7UBmmQ8GzqaKX1Ocs4mNTq9YDBmU0KnfAYPYht_lTB62ZCQ0TKqzl_A6O6KAYA6fOISjPWoJwIw5Mk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: "هذه المناوشة الدائرة بيننا. أسميها مناوشة مع الجمهورية الإسلامية الإيرانية. إنهم يتعرضون لضربات قوية. ويريدون عقد صفقة. لكنني أقول إنهم ليسوا مستعدين لعقد صفقة. سيكونون مستعدين قريباً جداً."</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/84931" target="_blank">📅 23:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84930">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b79d0b62b.mp4?token=HG8xjT57kBlrXE0HmB2FODDgZwRzGiC_X_MX52T1J7j8gck138Ssqou5uOjCa6u2dcxBLRbTuvrC7wrbpSktRC0ycby6V_97G2e-gjyUkvW63IHFeunkY5UzqhUy8ETroS8u_sIFvmaziLDfkL4j4aNybEP2G5feoankMg2b-7cFwDBjBsXvzSJg4HoI4lCjvp1VHGLyua5D3bXtZ3jCAwvA8TNYdSbY7PawzSidnFQpTp8RSXbBL1g1Ae5Oh1V5zdJtw2r1oJXOTialoENQnodroh0-EsQ8p907SamJjCENty6jcd96WAUAe77Im-8wAHA1_DtqYHetcnNE2YcdiFJdBB_93jORPo6rQaqYwhR4rvNkyz5_JiD6Sm0GGb5sjKoysYB4-jebDFK2eCr3kHz2_NaurtVM5XwlrWb-M7SEKuNflMNeV46Myhi880Vn7bJJ0Dr-_tIkmNTa-bZEDNYWONIvLhLMO10saSKqLGzc-pTUa-XJH2BCkQ2aipDqnl5zo5CSuOfrTLOz1JmaSfmwO2KM-i4nXzol5YdIWDR5ZPj2ZtBBiiawdCoeImbNdbiSg6wg_t8Dbngpp-R9Cn3bqt_on0Ce1BzP6kEWxxtD8zqSzR7b1TPZQJAaLlW2nVGqzf3mu77JG8Q2TQicjnP8haO8lm1teKwDqvMIas8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b79d0b62b.mp4?token=HG8xjT57kBlrXE0HmB2FODDgZwRzGiC_X_MX52T1J7j8gck138Ssqou5uOjCa6u2dcxBLRbTuvrC7wrbpSktRC0ycby6V_97G2e-gjyUkvW63IHFeunkY5UzqhUy8ETroS8u_sIFvmaziLDfkL4j4aNybEP2G5feoankMg2b-7cFwDBjBsXvzSJg4HoI4lCjvp1VHGLyua5D3bXtZ3jCAwvA8TNYdSbY7PawzSidnFQpTp8RSXbBL1g1Ae5Oh1V5zdJtw2r1oJXOTialoENQnodroh0-EsQ8p907SamJjCENty6jcd96WAUAe77Im-8wAHA1_DtqYHetcnNE2YcdiFJdBB_93jORPo6rQaqYwhR4rvNkyz5_JiD6Sm0GGb5sjKoysYB4-jebDFK2eCr3kHz2_NaurtVM5XwlrWb-M7SEKuNflMNeV46Myhi880Vn7bJJ0Dr-_tIkmNTa-bZEDNYWONIvLhLMO10saSKqLGzc-pTUa-XJH2BCkQ2aipDqnl5zo5CSuOfrTLOz1JmaSfmwO2KM-i4nXzol5YdIWDR5ZPj2ZtBBiiawdCoeImbNdbiSg6wg_t8Dbngpp-R9Cn3bqt_on0Ce1BzP6kEWxxtD8zqSzR7b1TPZQJAaLlW2nVGqzf3mu77JG8Q2TQicjnP8haO8lm1teKwDqvMIas8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">يحيي ترامب والدي أحد الجنود الذين سقطوا مؤخراً والذين كانوا ضمن الحشد، ثم ينتقل فجأة إلى موضوع آخر: "معاً نجعل بلدنا أكثر أماناً وقوة ونجاحاً مما كان عليه من قبل. لهذا السبب أسميه العصر الذهبي".</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/84930" target="_blank">📅 23:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84926">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KqgG9nxNxl-rzt1kFGo0FOcu5TH5H3TLdyfuBVz40SOqbF7SQV0KtcwSaFLEzoechGhWy2KJNeNcfC8i0GszoqMEKXodHgLB0o_lqXOrDY2nswpCk_aHDIz_y22UqvHS7CiIEMx_WAmn_vrHUjmtIDap1VnxXj8xVkXdIzJiAEW-rlhrfQuuyfpeDV-YidNmy5AHC_uHenWetPtU8usdyiBnQ0KMWLkwAFCrHNjzwEWdx1HO3iL9n1uzuD3kU4URgtgHsbOkPd4hSQIzDcI6BBwuyaRwq2p4LLlo-8WqHmWq81npJK-FswKicxsv2bDNj1T3ilxxnZVeerddrq5MXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qu6Aj5jdGzUfETDYuh_l7BIf5RI0nwUE6TsiwSkPUrbsIZl0Cqyv6a9dUuWAm2dHCEfwEZPoeHLd8adG36w1IcDrpwlUuoPCLa2N9joe5d85jK1m9gnlakRSWVjFDF6DISNm4XRiwXFlLMd2bkhWGBKypg4WtCMeeByVkC-ZAeG181EUYHX3mPy2dZpgNwNz0EPDBv0MM1Mk_fpQGaELKzkAflMB9fOa3P5bRn5qScNkfi0-qMmrrJSCvDSxpwTM-KnxyNvc26hi9Sqy1A-xXmddtg8qI6Yt6o27U2oLo2Z4wM8Oa2SaRiRklDqdWIZN1CQx_TFz7TWAp2IrgnHb3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VCbVaeph1BUSbzTphe5jVolxkYo7JXHW55aAnH3T1X4_bsPE_vGKncx4nuUNIa5bEqNWgPe_lxUY0y1O0VdsMLL00yiMH1H_60up8ohePW7h0PW8WkxG8Ne6OyGeOEnjaVr7ilYQ_oM9MwueasXAvdYk4TGSrNPSd4rzuwFx0CMqPz6x4KyAF8i8RDYMUw27sbZ7t_pGh4pNjVHWBjZbqd703uzSfgNKSegwHizVv9WD7ScBtmNZJQ2jJAQkVL1D2cd_EglnEF_FBGqZJFccTKbstmOaw-3bPNIjr5axZfiCa__H3FUZIFKS4MXZC75i-LtfCokoGGiSNoicWdRshA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y2AiEM0DmOsOIJJ-9wozQzh10vbAD3Yc9eqVc53rjthTyE_AfMPgj12JosZh3_k_O78iHfQ1WcYJ8QA_6bzE0P9vZn9HbnpR8niCbZ5LNytF05hwItAmY64QKRnySj_6ieOxX-9ZntwW76I6t1mt5xiSNc1MhnOW_FaRym2UkU_ZQKDwmZm0epjfRwkLX9T3xoZ8vS4BxFD7y9s_FZg82zhaASfUkehKiARQM7AEocU30CL_dYv94XHIkvqpqP4zPCtw53vCcNsPzJAyjE31usmwXGLjhrJAuX0KxuCANkJA-uPdD14cjNaEaEugRA_Oj0iZ3AMOP0hhyvQh-gBThQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇾🇪
بيانات التتبع:
الحصار البحري للحوثيين على المملكة العربية السعودية في البحر الأحمر له الآن تأثير واضح على الشحن التجاري. لقد عكست العديد من الناقلات مسارها بالفعل أو قامت بدورات عكسية قبل الوصول إلى مضيق باب المندب لتجنب خطر هجمات الحوثيين.
- MICA (IMO: 9399935)
المغادرة: 20 يوليو 2026، من جازان
الوجهة: صحار، عمان
— LIA (IMO: 9417751)
المغادرة: رابغ، المملكة العربية السعودية
المغادرة: 27 يونيو 2026
الوجهة: ميناء سنغافورة
- بطل جديد (IMO: 9799147)
المغادرة: مرسى ملقا
الوجهة الأصلية: ينبع، المملكة العربية السعودية
الوجهة الجديدة: قناة السويس، مصر
— رودوس (المنظمة البحرية الدولية: 1024948)
المغادرة: ينبع، المملكة العربية السعودية
الوجهة الأصلية: مانجالور، الهند
الوجهة الجديدة: ميناء السويس، مصر
— أمازون (IMO: 9476654)
المغادرة: ينبع، المملكة العربية السعودية
الوجهة الأصلية: الهند
الوجهة الجديدة: ميناء السويس، مصر</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/84926" target="_blank">📅 23:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84925">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9ef37de5e.mp4?token=mLQ6NoYNaYFxPTXi7xgu0eWwqjzJUz-SLDTcN5fni7ipJ4fjWioX4anIxNan_3rqQbvPJwl6Hka4o-faQX1vQqDf_Yyq9xM9yYK1waRvsZhv5W1FUzJ6QLMue3eyPm3JTU2dNzqVlXHBdHByKvD07e19zOVcpy5QmyZ2L-dWe5qTOeo0kumZCw7gYGL-eeS3wwnn_wwDenNY_bqO-vMUbcgDCeiHUjsPl0FNrvqaRs1E3ms29iqXmUnNKp6WcFkEckPSE1qmVPtuFIAtH22cwbdEQ_nm5z3WHkzz-cu6mM_B7WxBwymbYybwpPGZhTS8NlfRN-G3KezcjY9cHF3e4RsmM_tuQ2YKjAcJg5xANB10QkXZh3MiBsUnMZWnP9xdi0N10HfB8S4ONOsFcFSZn1Vk7Di-EgzjlLODsgynAL3XlIZLd4tnU6cdGZyS9N81GsmwUHajByhN8Zysgj06qgvtZzn_mDtRqsEJzX2fKU888IIipGnpLk3VH4-a3ntcnssKzp2hAKg_XAEIVhdguST62E1J2ek2lPqD61ir2eht_VIccv5ONqqUarMmSoA4G8S5AjWvchtL_UcU47eebSs1v47_5yxrMNqwBR03O32UGIjgfmQhBTYyseQPVxwKOwK2lG4dIl72s-yab6-7GoUU3aHxMgLwjNEQhDYgrVY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9ef37de5e.mp4?token=mLQ6NoYNaYFxPTXi7xgu0eWwqjzJUz-SLDTcN5fni7ipJ4fjWioX4anIxNan_3rqQbvPJwl6Hka4o-faQX1vQqDf_Yyq9xM9yYK1waRvsZhv5W1FUzJ6QLMue3eyPm3JTU2dNzqVlXHBdHByKvD07e19zOVcpy5QmyZ2L-dWe5qTOeo0kumZCw7gYGL-eeS3wwnn_wwDenNY_bqO-vMUbcgDCeiHUjsPl0FNrvqaRs1E3ms29iqXmUnNKp6WcFkEckPSE1qmVPtuFIAtH22cwbdEQ_nm5z3WHkzz-cu6mM_B7WxBwymbYybwpPGZhTS8NlfRN-G3KezcjY9cHF3e4RsmM_tuQ2YKjAcJg5xANB10QkXZh3MiBsUnMZWnP9xdi0N10HfB8S4ONOsFcFSZn1Vk7Di-EgzjlLODsgynAL3XlIZLd4tnU6cdGZyS9N81GsmwUHajByhN8Zysgj06qgvtZzn_mDtRqsEJzX2fKU888IIipGnpLk3VH4-a3ntcnssKzp2hAKg_XAEIVhdguST62E1J2ek2lPqD61ir2eht_VIccv5ONqqUarMmSoA4G8S5AjWvchtL_UcU47eebSs1v47_5yxrMNqwBR03O32UGIjgfmQhBTYyseQPVxwKOwK2lG4dIl72s-yab6-7GoUU3aHxMgLwjNEQhDYgrVY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: لسنا بحاجة إلى مضيق هرمز.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/84925" target="_blank">📅 23:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84924">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0EaxOvU6K60IW7bH6FSlPQBlB3MgXaoL6BHLtVUnIxiRZLhznCorRuXmB-7g65Y5KTzPIVVKR5JqmrVNBExoyuoPEioyNvRRCh8OEN-GkmC0g8G1LBpPkD5YqxdplHYML-zOQlqMseiVc69xwDnU1uMY1OoCyillfdXZhHNA1ZYb8ovgFF8gN4LrSR4E1hn2cu3piJSqLF-CrrEf43h7tkKBaieFbXjMojpSQe_fCmf5qEg9NavxlFc_Wr0IkxTFVJPKT9sn5Uyc1w2KcDOQgQR876yaAMQOGjS0Y3cOoqL94gfB-HhnNGSJKQM3GZhrYguXyJ9NvNeZ4dyH58SKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب: لسنا بحاجة إلى مضيق هرمز.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/84924" target="_blank">📅 23:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84923">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ee8aaa461.mp4?token=AnTCu-K4MxexdJJZoHQCXeH0w5o86zXa35-s-tOXSi4e7Io7qdSIew7PBevSvxWdF15qAqZcrN-D6NaJbeQ7mTmWMq_zFcSU9d3ikRXrS5taNnWRGpYjzE9Zpv8Ux4CiOHI3zGZPlikYWgbAs1h70zVSuFAFc7JkqIKKjO6kyaeDS1Xod3a7jtIoiwSU46DqBx0uxMqjGabhrtJBD8Vi-U7dX1LpYbI6ay_ftvwvrDlsmzH2ZzZSnDzHpMIW0PXnrXYYGOXshHeqbkrE7f0IWCP-bxnxjyD589I55E3CCCvpy91ogwbSZUAaEVngOKxQZogqgzTk3c3gIZIB4FojNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ee8aaa461.mp4?token=AnTCu-K4MxexdJJZoHQCXeH0w5o86zXa35-s-tOXSi4e7Io7qdSIew7PBevSvxWdF15qAqZcrN-D6NaJbeQ7mTmWMq_zFcSU9d3ikRXrS5taNnWRGpYjzE9Zpv8Ux4CiOHI3zGZPlikYWgbAs1h70zVSuFAFc7JkqIKKjO6kyaeDS1Xod3a7jtIoiwSU46DqBx0uxMqjGabhrtJBD8Vi-U7dX1LpYbI6ay_ftvwvrDlsmzH2ZzZSnDzHpMIW0PXnrXYYGOXshHeqbkrE7f0IWCP-bxnxjyD589I55E3CCCvpy91ogwbSZUAaEVngOKxQZogqgzTk3c3gIZIB4FojNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: لسنا بحاجة إلى مضيق هرمز.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/84923" target="_blank">📅 23:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84922">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سفراء باكستان والسعودية والصين لدى إيران يجتمعون في سفارة باكستان في طهران.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/84922" target="_blank">📅 23:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84921">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">انفجارات عنيفة في سماء الأردن</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/84921" target="_blank">📅 23:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84920">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1Cg3EPE1kYF_wlRDmNnZlnOysqN8qYNjDBvnEYEe5fRY4nAfELxZl2pvA0Rw7Cq44JcWGh_G4KDP4qwDaLjz908ZfwWUZTi56s14bAIUvqZBpUi46RW4mXp9t4smtfEdgW3DqMzJqOqkGPaquLDkTt50nYzeWcn-dNxoNwEoQ72_N2dUKAA3kmtOKBBhIGT5p0cGg9JpV_piaECpZ6AOKhiwVhEXRTvGYBefhF_8cwS_v-5i6dOGuwF97ZozPib-7l1-OrALPZ8hpqGU8ZhBP035W4pD_3u2FGHBzv0EbMn1CAuhj9Hoy8S2Yx2KZQCL-1AW_-NRKlq2ZkxsNajQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشاط لطيران بريطاني في قاعدة اكتوريا في قبرص</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/84920" target="_blank">📅 23:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84919">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">انفجارات عنيفة في سماء الأردن</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/84919" target="_blank">📅 22:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84918">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/84918" target="_blank">📅 22:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84916">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a7e7b6617.mp4?token=o2N1KJokS4LNJnDDm0Ko3t0oT33xBvh6QX6yAdZcI0qgM-Axo0MNdJ3aQW7bIGuuqyq8bQwQnUNfQwoz4tZ1on9-tDRuv5XMvufGWpuMUz0bDdRWb8Scz8K6eMOdlBkwcn8HO3ciRAZixySDIjbonAJUhY4X7F0S-wTyXAVKdg-tA9nniQlg9IYyTnnqF-Z6TMlnq9IbY31wx6r5MGJjRpvO_ShALOeJKayf5fj5jKgVBKG7YDyullE_XJkmu8RWx_A2yT7aew9wUjljLKEQXJX_I0Sng37ofdbytsISdR5gC546uMh9LLhFhyZeqNKKqTaQGQV-fXBEW3BITpB7yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a7e7b6617.mp4?token=o2N1KJokS4LNJnDDm0Ko3t0oT33xBvh6QX6yAdZcI0qgM-Axo0MNdJ3aQW7bIGuuqyq8bQwQnUNfQwoz4tZ1on9-tDRuv5XMvufGWpuMUz0bDdRWb8Scz8K6eMOdlBkwcn8HO3ciRAZixySDIjbonAJUhY4X7F0S-wTyXAVKdg-tA9nniQlg9IYyTnnqF-Z6TMlnq9IbY31wx6r5MGJjRpvO_ShALOeJKayf5fj5jKgVBKG7YDyullE_XJkmu8RWx_A2yT7aew9wUjljLKEQXJX_I0Sng37ofdbytsISdR5gC546uMh9LLhFhyZeqNKKqTaQGQV-fXBEW3BITpB7yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار تفعيل منظومات الدفاع الجوي في سماء أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/84916" target="_blank">📅 22:57 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
