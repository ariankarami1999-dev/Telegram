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
<img src="https://cdn4.telesco.pe/file/dL9sMLxqA4yDGGTsZhOrp9saIv2hCznBtK5sqbXZUHHLYRfW7Sa7-BvTY3nQz_tTNWeN52cYqShsiJjEPTlyXiDt0LLAoeItlT021Q9U5CYHb8E58HbvVcKiCD17jy-XDd0UbXrtTd8StZffNfVq2Y5rivJNvEdPPSEfNACBkhDVF10voTlYota7a-qR3UqpIzfHiTFPaXtxGP8xEckVMDXkhW5A98CqV0cj6_QRHIyovEwHA9VkTgGHjUbARCLMq1BHr4pLaHYgBPFMPP24cOeGnMAQsrOov_pbUxQOlstxQufGyoLGpKQTBxKP1Ovd9XFi3dV-FFrr_2CI0GYDAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 404K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 00:28:36</div>
<hr>

<div class="tg-post" id="msg-18627">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3945766522.mp4?token=r5jJYKY_Vg81o25td3vtEJbdEkEMfhSFvIO0l4ti0DIJAMxO3vJviMxpyv4d7D0XearvKlXjH_9jeWPGUjpvD7H8pIUsC7zPRn--rjQANv0s_lAt65-HXMX99EYFHh3mDuHPyuGqXdM-QOB_F5zqWPx-6NIV-L-BUP-0TU6ZNBQlTDdxJ0ehfbEB8lVVS5zVLV554rCItI7U8zy51VLKjTxZJnH4dgkHolWABu62vb1uIdO27gorhscnoIOKOP_K3PHIKIRLdBrzvl1iyIGMSRZybKpiDmPvrH_Ur4m0zpZg7sAxMsO7jAIsYOguGgKHPTNZVn2tDuy9FBChgZyDJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3945766522.mp4?token=r5jJYKY_Vg81o25td3vtEJbdEkEMfhSFvIO0l4ti0DIJAMxO3vJviMxpyv4d7D0XearvKlXjH_9jeWPGUjpvD7H8pIUsC7zPRn--rjQANv0s_lAt65-HXMX99EYFHh3mDuHPyuGqXdM-QOB_F5zqWPx-6NIV-L-BUP-0TU6ZNBQlTDdxJ0ehfbEB8lVVS5zVLV554rCItI7U8zy51VLKjTxZJnH4dgkHolWABu62vb1uIdO27gorhscnoIOKOP_K3PHIKIRLdBrzvl1iyIGMSRZybKpiDmPvrH_Ur4m0zpZg7sAxMsO7jAIsYOguGgKHPTNZVn2tDuy9FBChgZyDJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو حمله به سایت موشکی در جاده گراش لار شرق استان فارس
@WarRoom</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/withyashar/18627" target="_blank">📅 00:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18626">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پدافند نجف آباد درگیر شده
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/withyashar/18626" target="_blank">📅 00:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18625">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پرتاب موشکاز لار ، جنوب شرقی فارس @WarRoom</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/withyashar/18625" target="_blank">📅 00:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18624">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گزارش‌ انفجار لار
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/withyashar/18624" target="_blank">📅 00:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18623">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90e84e1a0.mp4?token=IBbMdNRzMgwOomU5pct8VT3Krb7RoYtC42zTQUjxHZ0jzMjJZbApOxDGVsWpmEqIPWo54cWbOheRASpRNx_UngoKKaHD6s9RPjx-nM5PUkrgZoaQ__WDu1EHz9TCeYxAsu4PBJhHo1rO7C9N-aGqB_ytQ4GS-BMpX_gLMz_adpjIaOpEkZ7riUW64CA08RJK-ktRDx_l573uCnKnX8hASpMROEItu9YalxfpvKlzeYBWqmO4FFA0JY_7pnzzmt6bnC5CSlHXTyHXdsFpZbljQNSjKffwqAAczbArpsIRddWNZTc8KQIPxWdP3R8Qx6-usaASN18eWGZnPGfmaj5irg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90e84e1a0.mp4?token=IBbMdNRzMgwOomU5pct8VT3Krb7RoYtC42zTQUjxHZ0jzMjJZbApOxDGVsWpmEqIPWo54cWbOheRASpRNx_UngoKKaHD6s9RPjx-nM5PUkrgZoaQ__WDu1EHz9TCeYxAsu4PBJhHo1rO7C9N-aGqB_ytQ4GS-BMpX_gLMz_adpjIaOpEkZ7riUW64CA08RJK-ktRDx_l573uCnKnX8hASpMROEItu9YalxfpvKlzeYBWqmO4FFA0JY_7pnzzmt6bnC5CSlHXTyHXdsFpZbljQNSjKffwqAAczbArpsIRddWNZTc8KQIPxWdP3R8Qx6-usaASN18eWGZnPGfmaj5irg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپاد دیدبانی رژیم در آسمان شیراز
@WarRoom</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/withyashar/18623" target="_blank">📅 00:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18622">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اصفهان صفه کوه لرزید
🚨
🚨
🚨
🚨
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/18622" target="_blank">📅 00:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18621">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گزارش انفجار اهواز
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/18621" target="_blank">📅 00:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18620">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">صداوسیما: صدای ۳ انفجار در بخش بمانی سیریک شنیده شد
@WarRoom</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/18620" target="_blank">📅 23:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18619">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ma_wnLdTPUarvlfkjvYrNJhuy1jVHcA4bwuFEspYQj-uqJPwt5tXLVNM52wyzm2aDQ_HJJDCbTKyxGaFRXCpFZK7s11D1MD6NeH1Ta0szfbQsuDslztfwWI8R9LFwVCxLJbTFHscRRq4Mu7DG9pRP1QtPk8jB3RtOquVGsKkjlMOzMuvof97VQJpl6gqa0Z3o1J8Vje9_lzwwbrYsos3yRREr-eHWHAftvDk0pdiLOOoxy6HFs-ZZqD-He0qMUod7u8Dfbggy5SZ2EaOgpO7OOlPP1cpwEC_lW9iEqDx342vCJ8m1ZSAA4bl7kuXGWkCbr1bg943uOzX65o0o4-XMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایگاه الحریر امریکا شمال عراق در
آتش
@WarRoom</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/18619" target="_blank">📅 23:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18618">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">انفجار بندر عباس
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/18618" target="_blank">📅 23:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18617">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">صدای انفجار اندیمشک
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/18617" target="_blank">📅 23:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18616">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">صدای انفجار چابهار
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/18616" target="_blank">📅 23:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18615">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سیریک رو همچنان میزنه
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/18615" target="_blank">📅 23:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18614">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">صدای انفجار اهواز
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/18614" target="_blank">📅 23:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18613">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گزارش انفجار کنگان
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/18613" target="_blank">📅 23:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18612">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">انفجار وحشتناک قشم
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/18612" target="_blank">📅 23:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18611">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سپاه خورموج رو زدن
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/18611" target="_blank">📅 23:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18610">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گزارش صدای انفجار ‌اهواز
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/18610" target="_blank">📅 23:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18609">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">انفجار در ‌قشم
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/18609" target="_blank">📅 23:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18608">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بندر عباس
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/18608" target="_blank">📅 23:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18607">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بوشهر
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/18607" target="_blank">📅 23:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18606">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دوباره سیریک
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/18606" target="_blank">📅 23:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18605">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سیریک زد الان
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/18605" target="_blank">📅 23:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18604">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">۳۰ دقیقه پیش ۲ گزارش از انفجار در اهواز داشتم
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/18604" target="_blank">📅 23:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18603">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سنتکام اعلام کرد
امروز ساعت ۳:۰۰ بعدازظهر به وقت شرق آمریکا (ET) (۲۲:۳۰ به وقت تهران)
،
هفتمین شب متوالی
حملات خود علیه ایران را آغاز کرده است
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/18603" target="_blank">📅 23:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18602">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سنتکام : شروع کردیم
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/18602" target="_blank">📅 23:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18601">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48b7df7221.mp4?token=p9OGaNHGYZc6_R5IIFd5dpRODe1AHz1KtxEmKhTiFqQlbUtkuTWeWhC2-9gQi23yonqY43dVHNesg0qD_TdaSMb0NjYDoedM5kVW_9rXqbFEgMIskTI_TB_6X06EGxrHXbkX2bL7Zl1XXadmt9aSeKem-UZCK8dgpIwxbBefhqqSLV5isG_e2d-kkdyHJjVp7-wbM9F4h9C-dODT1xml3p_6l6T85FoPuikNMVstF-lg7AChbLZbsrPySfFZHR0aNp3NoHd9bPKKVBM63FQH-j8_2MKyUquaHQwOy0DEPokzGbzq3Wzy6wiK0_6tp3yKdV4Y6iF-kM4T6d5oNmEFoaZNsjxz0ZYOmiysYntoFfdczobR8V5Ey-x-Ked4G-Uk4keR4FRxpnnI11mDviQCa2M7DbUCxIfZvCWihxo16n16cZdgyTHD5AlSEG3v4Fzu7CpXn63KOGadL_EGqDa_v3uNQUIpTc5q9O9DRYWdmfw1PAIc4DhytFOEXCVXp8Rg9tz8D5GCwz_rh0TtZHqX_psenMjrtM0-k1ohq8pwIrGIXp1_3jfzb8kqnaLTf43eb6AXh2DSEC0_BecteZObAuVxcG34y_i6hLeWkVsZKdpZOXGkfvNSKBUfbjxcY3fl06skJvapA9LO8wUN3v2Jmg_sSKttoJrhuT9zTarMHwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48b7df7221.mp4?token=p9OGaNHGYZc6_R5IIFd5dpRODe1AHz1KtxEmKhTiFqQlbUtkuTWeWhC2-9gQi23yonqY43dVHNesg0qD_TdaSMb0NjYDoedM5kVW_9rXqbFEgMIskTI_TB_6X06EGxrHXbkX2bL7Zl1XXadmt9aSeKem-UZCK8dgpIwxbBefhqqSLV5isG_e2d-kkdyHJjVp7-wbM9F4h9C-dODT1xml3p_6l6T85FoPuikNMVstF-lg7AChbLZbsrPySfFZHR0aNp3NoHd9bPKKVBM63FQH-j8_2MKyUquaHQwOy0DEPokzGbzq3Wzy6wiK0_6tp3yKdV4Y6iF-kM4T6d5oNmEFoaZNsjxz0ZYOmiysYntoFfdczobR8V5Ey-x-Ked4G-Uk4keR4FRxpnnI11mDviQCa2M7DbUCxIfZvCWihxo16n16cZdgyTHD5AlSEG3v4Fzu7CpXn63KOGadL_EGqDa_v3uNQUIpTc5q9O9DRYWdmfw1PAIc4DhytFOEXCVXp8Rg9tz8D5GCwz_rh0TtZHqX_psenMjrtM0-k1ohq8pwIrGIXp1_3jfzb8kqnaLTf43eb6AXh2DSEC0_BecteZObAuVxcG34y_i6hLeWkVsZKdpZOXGkfvNSKBUfbjxcY3fl06skJvapA9LO8wUN3v2Jmg_sSKttoJrhuT9zTarMHwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افزایش گسترده تحرکات ترابری هوایی نیروی هوایی آمریکا به‌ خاورمیانه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/18601" target="_blank">📅 23:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18600">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ارتش کویت: حملهٔ رژیم ایران منجر به هدف قرار گرفتن تعدادی از تاسیسات و اردوگاه‌های متعلق به ارتش کویت با استفاده از پهپادها شد. در نتیجه، تعدادی از پرسنل نیروهای زمینی کویت در حین انجام وظایفشان مجروح شدند.
همچنین، تعدادی از تاسیسات حیاتی و مدنی، از جمله یکی از ایستگاه‌های تولید برق و تصفیه آب، مورد هدف قرار گرفتند. این امر منجر به وقوع آتش‌سوزی و آسیب رساندن به تعدادی از تجهیزات ایستگاه و واحدهای تولید برق شد. علاوه بر این، ترکش‌ها در تعدادی از مناطق کشور پراکنده شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/18600" target="_blank">📅 23:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18599">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اگه ویس های چنل رو گوش کرده باشی امروز سوألی نمیکنی
😁</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/18599" target="_blank">📅 23:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18598">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دونالد ترامپ، در دفتر بیضی شکل خود با دارلین گراهام، خواهر لیندسی گراهام که موقتاً جایگزین او شده است، دیدار کرد و از او خواسته است تا در انتخاباتی که در ۱۱ آگوست برگزار می‌شود، به طور دائم در سنا نامزد شود و گفت «امیدوارم این کار را بکند، هیچ کس بهتر از او نخواهد توانست میراث برادر عزیزش را گرامی بدارد. دارلین از خانواده‌ای فوق‌العاده می‌آید و در تمام زندگی‌اش برنده بوده است. اگر او موافقت کند، از حمایت کامل من برخوردار است.»
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/18598" target="_blank">📅 23:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18597">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وای نت عبری : تاکنون بیش از ۶۰ هواپیمای سوخت‌رسان آمریکایی وارد اسرائیل شده‌اند که ۳۳ فروند از آنها در فرودگاه بن گوریون مستقر شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/18597" target="_blank">📅 22:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18596">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17da528eaf.mp4?token=dZWSjIoJl4BkIYA2Oa7GdbFiD1uK4jnacwW_CCnsaPCldrxid3TB2No_-94yCymHe9JiTBX4IpG4eCEqzX0tN-BRQ6esUtxCdYM9r9E2lmRJIeGgfKAefHpEQv_Dotn2OoTYhpJ65uQKEvS1sN9DD3Wid3BnPH9MBJcUY3YgXryrbZYxplcv0Bkxb54tDdUIPISzTak24zXvQ8BSOoSWAAJNT8PBTFswISPy0iHS0nU1TJ1Mdyn9HNV18OzVrXlZ5DR-5x5pCHnuCAtJwsBYepIVxpwd8Ns6H-xBNo0xxc6PWYD6og8noomj1OQSxhkr--bcZRaRNbQ1JcYKH7vxTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17da528eaf.mp4?token=dZWSjIoJl4BkIYA2Oa7GdbFiD1uK4jnacwW_CCnsaPCldrxid3TB2No_-94yCymHe9JiTBX4IpG4eCEqzX0tN-BRQ6esUtxCdYM9r9E2lmRJIeGgfKAefHpEQv_Dotn2OoTYhpJ65uQKEvS1sN9DD3Wid3BnPH9MBJcUY3YgXryrbZYxplcv0Bkxb54tDdUIPISzTak24zXvQ8BSOoSWAAJNT8PBTFswISPy0iHS0nU1TJ1Mdyn9HNV18OzVrXlZ5DR-5x5pCHnuCAtJwsBYepIVxpwd8Ns6H-xBNo0xxc6PWYD6og8noomj1OQSxhkr--bcZRaRNbQ1JcYKH7vxTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن کج بند : اگر حملات ایالات متحده در دو تا سه روز آینده ادامه یابد، نیروهای مسلح جمهوری اسلامی از مرحله بازدارندگی و پاسخگویی فراتر رفته و وارد فاز «تهاجم و نابودی کامل» خواهند شد، به طوری که پایگاه‌ها و سربازان ایالات متحده فراتر از مرزهای سیاسی تعقیب و مستقیماً هدف قرار خواهند گرفت.
ایالات متحده باید بداند که استراتژی فرسایشی «جنگ و مذاکره» به بن‌بست رسیده است و در روزهای آینده، شدت حملات ایران افزایش خواهد یافت.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18596" target="_blank">📅 22:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18595">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">فاکس نیوز : یک گزارش محرمانه که برای ریاست‌جمهوری ایران تهیه شده، نشان می‌دهد تنها ۹ درصد ایرانیان از حفظ وضع موجود حمایت می‌کنند؛ در حالی که نزدیک به سه‌چهارم مردم خواهان اصلاحات عمیق ساختاری یا تغییر کامل نظام سیاسی هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18595" target="_blank">📅 22:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18593">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e2f05b5ce.mp4?token=SRPNGrvnYJzD96l-l7Rdnk07cg7WEJPk_Yfc93U4AVOYtiFEeFUoPWDbA5QYenB35wJzK6ejnFCesCzXpYo9QmAfje9eWFRZU7kS9iSUKcs5jlbO1h69mHD6UsasNQK0leUZtY_X944WQqmm4Rw-yoWO6b-FSlEUbBaryyxfip4nxoELkvYtxHDRu0xuNKAR98sd3LxbCcfwxZ0t8lbmXhyTpgUeGF6iywB0PH0a-D6sl36e_ggfXcvWZuTCSALeyFlxya1YmW2QeR2Q-8gZsuZiNnzt2L7zT2p3PN9UmwRaKb0bT_4wpeeFRjrFt3F2TAVPH8bG3tnSVQi--Rc7KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e2f05b5ce.mp4?token=SRPNGrvnYJzD96l-l7Rdnk07cg7WEJPk_Yfc93U4AVOYtiFEeFUoPWDbA5QYenB35wJzK6ejnFCesCzXpYo9QmAfje9eWFRZU7kS9iSUKcs5jlbO1h69mHD6UsasNQK0leUZtY_X944WQqmm4Rw-yoWO6b-FSlEUbBaryyxfip4nxoELkvYtxHDRu0xuNKAR98sd3LxbCcfwxZ0t8lbmXhyTpgUeGF6iywB0PH0a-D6sl36e_ggfXcvWZuTCSALeyFlxya1YmW2QeR2Q-8gZsuZiNnzt2L7zT2p3PN9UmwRaKb0bT_4wpeeFRjrFt3F2TAVPH8bG3tnSVQi--Rc7KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جهنمی سلیمانی عراق انگار که آتش فشان فوران کرده ! بی شک اگه کرد ها تو پلن نبودن اینجوری نمیکوبید پشت دست خیلی خبره !
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18593" target="_blank">📅 22:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18592">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">چهار سوخترسان از اسرائیل بلند شدند @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18592" target="_blank">📅 22:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18591">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbBWPYjLLwmdeFJ1Txn1mq7S0PSzfBpCMFYFBGJ9sSNZIH9AtfTkvgDBs0tM0LcLU3c4yz4Ba7mIDjfsDsB4ihWVYdbbhImwGANGsMqCc9zDucjzTrq8sHGB7gNQCHNnbz-HB-ntGM6G3aViJaDeR45LkDrQV7V27gsL3_O3HcIDu7RuvkhW6JtYXh9tzAfc6j99yMEGhowF_V2IcZm8BV2ejag6hzg9vwMRGtEa7Ys7AdjEeFEDuDvafAJU84oSnBUMIjO18Qeaoe2ap3yW47J9xrrwi-hD41SqYY-GWWCvKoex8D4APiSgOKbVHoVH0a8ugxy8mnF8bNTKJCF5qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چهار سوخترسان از اسرائیل بلند شدند
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/18591" target="_blank">📅 22:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18590">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3z35BVT_8b1i2q6bwvT_WLB0oTg6FvKi78nQKuJ5fCsMZE6kxTyxc7AlIVqREEZjtEo09a0NGA88UN9RsHplYAz9f01bUqc-4odU0x9vGawY3btAyZr1c5lDS7KK2KWSCCsTovs9KiCTyfr9cNW3F-yFrTlrF05FsBok6826GDzfk4tx2p5posqbkmCg5U-Rgcch6cfesvxwDOVM22B0NjlhyXWFZ3RNu7E_tuCaqRESzHEFP5GidMCuPXvQmXx18HzrfWhHec9AK-ogbrbTyCSZHfHrb6h0QnKPiYt-ejChRx3PvfblINhO4_g26dlyzQyqSinGxKW2AkTmk1uFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود در سنندج
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18590" target="_blank">📅 22:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18589">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SC6aWuQj8uIxCIfBB0StMYfSgQnbhcrbsoADlMD1SKctTS7JI3mbt9OHFG4mhOFZyVWTzl2MJ7cUqQk-NaMEb7OakEP3JZKxZpQvncJo0q-5PhFKRITLR-wp2aa4KW2a_YwVOqKCxpO6Xj9PJpgVZ780Q4gv4IVE-tsGtxl1Y45cmhTlYSNnPrT42soohU2D40L2l7ucb_MY2hcJdclqplFZ7lwPtXsqby47PWtXAfJKVj7PlEeiv_Cq7Z5k_PlNRfH2Y3P4URD1alfGRC4TwGzQ0f477k0v8GmY40xNsZ_yFbbOeXMPOmrfxjMhm9uFKcq7Fy1jTvgG8689V784sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم سنگین آتش در انبارهای مقرهای گروه‌های کرد مخالف جمهوری اسلامی در اربیل و سلیمانیه عراق ، کل کوه در آتش میسوزد این گروه ها از مدتی پیش به کوه ها پناه آورده بودند و پایگاه ساخته بودند
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18589" target="_blank">📅 21:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18588">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/18588" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18587">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">حقیقت یاب اتاق جنگ
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18587" target="_blank">📅 21:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18586">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گزارش انفجار جدید در بندر عباس و یع صدا هایی‌در ‌بوشهر
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18586" target="_blank">📅 21:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18585">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">خبرگزاری تسنیم: هم اکنون حمله موشکی سپاه به یک کشتی تجاری در تنگه هرمز.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/18585" target="_blank">📅 21:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18584">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">با حملات پهپادی/موشکی آتش‌سوزی‌هایی شدیدی در پایگاه‌های گروه‌های  کرد مخالف جمهوری اسلامی در شهر سلیمانیه رخ داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/18584" target="_blank">📅 21:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18583">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اتاق جنگ با یاشار : وضعیت انفجاری ‌منطقه
🚨
🚨
🚨
🚨
🚨
💥
۴۰۰ هزار نفر در اتاق جنگ با یاشار! سپاس از همراهی و اعتماد شما. این تازه آغاز راه است.
🎉
400,000 members in @WarRoom with Yashar! Thank you for your trust and support. This is just the beginning.</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/18583" target="_blank">📅 21:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18582">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‎ وال استریت ژورنال:آمریکا جنگنده‌های خود را از اروپا به خاورمیانه بازمی‌گرداند
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/18582" target="_blank">📅 20:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18581">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">۲ انفجار بندر عباس
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/18581" target="_blank">📅 20:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18580">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گزارش انفجار بندر عباس
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18580" target="_blank">📅 20:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18579">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آکسیوس: مقامات دولتی ترامپ به اسرائیل اطلاع داده‌اند که
ده‌ها فروند هواپیمای تانکر سوخت را به این کشور اعزام خواهند کرد،
این اقدام در آستانه یک گسترش احتمالی عملیات نظامی علیه جمهوری اسلامی ایران صورت می‌گیرد. سه مقام آمریکایی و اسرائیلی این موضوع را تایید کردند."
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/18579" target="_blank">📅 19:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18577">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsKoFAfa67d_K9ykYfbQQrqg-n_KE8i9038JVLaWpkjtCqq6PqS7gfVrissO0u4nUdspdLYMP0mtz7BvDwNfFr2ABU6UWhapaYB1eiyUMbm4-dEqEspq6m-nHaCmltGdVu6gK5Oo2ZQvSmU1O1lyk5FJWeDPKFhDnQjFk5EQHuRTIpLxQfga9hhV6yR1OGs8-yK3Ww7xCzM_dYkz8HedrFfdQStaxy87_5hTCcJgYljTb33v_2xn438UGIpzAKsKxZgtRV4MbuYJUAmA2i2trBQjPvIQDgAJO8zjlQWBkMH9LZzv9mdqXetz-AmOxcotTi7x2zQGAyEXUt5OvaYsQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57565771c4.mp4?token=O0UX4C2dUg5Y_WgN6w8yuyzxiYk--3UEjtFBpd24DDEfhgziQ5C2-88GXmPuIvacJlyJ3OvWyYwhYESzqzptMUw2w0oqFsMb3HOtG55beXZQ1DBqk7lECl0fy-czFRDXJfzZy1WwTlFyCdMUdygifsjz0KUS9LGI0t--7bJPfmQhhJBCVExZpC9QN34mV6i1eEG00V6oq8bmwmRy5Aaa4oLG1YRZcL9Wa55Jha36C2sU4jPP-yZ9mdMo7KbejRchVX3lJxg2Ovp8-elJyNpp-yX9FAdibmQx1E9wqpjNYCFG4s0aBc6aLdmC3J_HyQyKj5ZYqRVqhJNYtYSzzzcYhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57565771c4.mp4?token=O0UX4C2dUg5Y_WgN6w8yuyzxiYk--3UEjtFBpd24DDEfhgziQ5C2-88GXmPuIvacJlyJ3OvWyYwhYESzqzptMUw2w0oqFsMb3HOtG55beXZQ1DBqk7lECl0fy-czFRDXJfzZy1WwTlFyCdMUdygifsjz0KUS9LGI0t--7bJPfmQhhJBCVExZpC9QN34mV6i1eEG00V6oq8bmwmRy5Aaa4oLG1YRZcL9Wa55Jha36C2sU4jPP-yZ9mdMo7KbejRchVX3lJxg2Ovp8-elJyNpp-yX9FAdibmQx1E9wqpjNYCFG4s0aBc6aLdmC3J_HyQyKj5ZYqRVqhJNYtYSzzzcYhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویری از حملات امریکا به مرکز توزیع خط ریلی بندرعباس
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/18577" target="_blank">📅 19:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18576">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بیانیه ارتش : نیروهای ویژه تیپ ۶۵ نوهد با انجام ۱۱ عملیات و ورود به خاک کردستان عراق ۸ نفر از فرماندهان ارشد گروهک های تجزیه طلب رو با موفقیت ترور کردن و ۳ مقر مهم نیروهای تجزیه طلب رو بصورت کامل تخریب کردن
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/18576" target="_blank">📅 19:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18575">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cdac5e1f0.mp4?token=gbpee8JwsBXPBFKifNV2an2tHHeGvQitKZOmMxhL-BYqzwHIXwTsSwLcPDasE25xFNNQeigeunkynVaUROyLMmUuOYDZ2QJqFZ6ZluF2ufLqOB0BJwh2YU9xi-I8HhQ0aFUjCBhu7WY7gfGW-A9H5Xa4OLBpSDB5d-TIHKVMe5r1yYGscUCD9IXZeZwZP2U_CGK4I8sdNQ8Bio_7waYGqutH_Wkt5DYBGc2ocT5OnqmR-jjmty1t5iKouGn1SNFLqCMKnyY9kisa9K87iaObjGBbS4hMVazT3bJeCb0xhghdbGrvI1lxxpief9K6opURWGSLAextnvXgp8mnj4T68Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cdac5e1f0.mp4?token=gbpee8JwsBXPBFKifNV2an2tHHeGvQitKZOmMxhL-BYqzwHIXwTsSwLcPDasE25xFNNQeigeunkynVaUROyLMmUuOYDZ2QJqFZ6ZluF2ufLqOB0BJwh2YU9xi-I8HhQ0aFUjCBhu7WY7gfGW-A9H5Xa4OLBpSDB5d-TIHKVMe5r1yYGscUCD9IXZeZwZP2U_CGK4I8sdNQ8Bio_7waYGqutH_Wkt5DYBGc2ocT5OnqmR-jjmty1t5iKouGn1SNFLqCMKnyY9kisa9K87iaObjGBbS4hMVazT3bJeCb0xhghdbGrvI1lxxpief9K6opURWGSLAextnvXgp8mnj4T68Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : در
۱۶ ژوئیه (۲۵ تیر)
، نیروهای آمریکایی با موفقیت
برج دیده‌بانی بندر شهید کلانتری چابهار
را منهدم کردند؛ برجی که بخشی از شبکه نظارت دریایی در امتداد سواحل ایران در
دریای عمان
بود و به ادعای آمریکا،
سپاه پاسداران
دهه‌ها از آن برای رصد و هدف قرار دادن کشتی‌های تجاری عبوری از
تنگه هرمز
استفاده می‌کرد.انهدام این برج به‌طور مستقیم توانایی سپاه پاسداران برای هماهنگی حملات علیه خدمه غیرنظامی کشتی‌ها را کاهش می‌دهد
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/18575" target="_blank">📅 18:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18574">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دقایقی پیش فرمانده نیروی دریایی سپاه به آمریکا هشدار داد:آمریکایی‌ها با هر لحظه که می‌گذرد،به لحظه سرنوشت‌ساز برای عملیات علیه یگان‌های دریایی فرماندهی مرکزی ایالات متحده در آب‌های این منطقه نزدیک‌تر می‌شوند،فقط منتظر بمانید،
ساعت صفر نزدیک است.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18574" target="_blank">📅 18:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18573">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e9ed530a7.mp4?token=dbOmx9-PbX-sQlO3uP6YUXrp0UwHEe3hVKZInVPX-Ww819KVX5LszijW3EdtqtHUN49h51fzo4TWFFOzbsBp0r7AFWvYgNg2MDMQeh9KOH45E5u0RtiZhny-rMUIqOB-rQtI0lOVlHXX6u2j8LHfAsnhOvjMDHor-LVRA4H4gHCL87Xhx38BZHnEOUaVf4RyLzPjqTMw5IJL4GsWNWrZl2znbbNE2UfiiFmr7q9rw6y5-4lniEiYVlW-BqJs8bZkT-9vmKgTx5NS2jqBH-6pFAxQMU2Fcth89AcX-EkPYtQzalxL5_gnqEq81abWmc6zUt0FwaYki8GwGoTR_-A5Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e9ed530a7.mp4?token=dbOmx9-PbX-sQlO3uP6YUXrp0UwHEe3hVKZInVPX-Ww819KVX5LszijW3EdtqtHUN49h51fzo4TWFFOzbsBp0r7AFWvYgNg2MDMQeh9KOH45E5u0RtiZhny-rMUIqOB-rQtI0lOVlHXX6u2j8LHfAsnhOvjMDHor-LVRA4H4gHCL87Xhx38BZHnEOUaVf4RyLzPjqTMw5IJL4GsWNWrZl2znbbNE2UfiiFmr7q9rw6y5-4lniEiYVlW-BqJs8bZkT-9vmKgTx5NS2jqBH-6pFAxQMU2Fcth89AcX-EkPYtQzalxL5_gnqEq81abWmc6zUt0FwaYki8GwGoTR_-A5Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قرارگاه سپاه در راسک که در اثر حملات آمریکا ترکیده و فقط تابلوش باقی مانده.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/18573" target="_blank">📅 18:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18572">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سیتنا: با پیگیری‌هایی که انجام دادیم، خبرِ "آمادگی دیتاسنترها برای قطعی اینترنت" که از صبح داره وایرال میشه صحت نداره.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18572" target="_blank">📅 18:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18571">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAp12P558Wh4gApltgY6aQ9XnCiqWrBVDTm7ndCkguufwjxPDEzmgU9_2pI__MVnHlpsuRvhmy1hwnb-UCl7FbttJo8hPZw3DCKetLAE5KgOOcv4Cckssfh_Avy3nwQnKhoQOOt-3cdGXK036475Dt1ncRnAF9Ha6dfpA6KUAuQ0m4Wg9-1RYtYuODxxAK900CtrFM5W3HNQ0OfEaDZW7kkShNWU9YKoM1B_FmBXj2L-Lr_Z4XTyFzj3N6i-wxLWW7DA3fr4GvSG_7ByabpDNoqCYZuplQDiUqYg7PCOVcVcIQkBtikBjVli6TuMDXDgjMB6CCjmuD7IVliRTcByog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل : «عملیات همچنان ادامه دارد»
یک فرمانده گردان حماس که در نگهداری گروگان‌ها نقش داشته و دست راست مقامات ارشد این سازمان بوده، به هلاکت رسید.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/18571" target="_blank">📅 18:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18570">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3z2Fqcu-rcN2djclJI6YCosBLXrykGY0pFsg1I3Sv7e2hQHH8J7MQhNPvuevgEXEjKZf8rUkljIK_AfbFTAdNcaAcHkxkvQ_9XreMmO7NmUi_oSqrSC6I8QlxQjt_NrD6STnF8gvnlRxP_i271hoSk9iqsEA8ZJJq2izIXekLogUB44rpUdJ6ayOfBeEN6u2YWT2WrlgZ137FfbAbOzQsRopTezx0BfT49jzxoqRHNeUxbpvVmVZyqZFTo47zhQL2ThxQTh-qa7HoYWdTaGrOiCjtx8kzHq35KplYh9tVH5SYb3PwP2XKA7TQc8oKVDBpyPVxi5Pp95g4-_fjObXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏۶ فروند F35 طی ۲۴ ساعت گذشته از پایگاه هوایی اندرسن در گوام به خاورميانه اعزام شده اند.
@WarRoom
پایگاه هوایی اندرسن (Andersen Air Force Base) یکی از مهم‌ترین پایگاه‌های راهبردی نیروی هوایی آمریکا در اقیانوس آرام است و در جزیره گوام قرار دارد.
گوام (Guam) یک جزیره در غرب اقیانوس آرام و یک قلمرو وابسته به آمریکا است</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/18570" target="_blank">📅 17:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18569">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حقیقت یاب سنتکام: به‌دنبال گزارش‌های رسانه‌های ایرانی مبنی بر اینکه نیروهای ایرانی به پایگاه التنف در سوریه حمله کرده و نیروهای آمریکایی را اسیر یا کشته‌اند، ستاد فرماندهی مرکزی ایالات متحده (سنتکام) می‌گوید هیچ‌یک از نیروهای آمریکایی در منطقه اخیراً کشته یا اسیر نشده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18569" target="_blank">📅 17:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18568">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بر اساس گزارش خبرگزاری رویترز که از منابع مطلع به دست آمده، پاکستان در حال مذاکره برای یک توافق دفاعی گسترده از کویت است، در ازای همکاری در زمینه انرژی.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/18568" target="_blank">📅 17:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18567">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">قدیمی‌ها یادشونه من اینارو هر روز که کم میشدن قبل جنگ اعلام میکرم
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/18567" target="_blank">📅 17:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18566">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">استوری روز قبل حمله !!!
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18566" target="_blank">📅 17:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18564">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a267a27341.mp4?token=Hr-9yNFWeUtsRvjTmRo8ZOlZ0pfO9BsKmfWzIh-K5tvpPTFWPAO9ySNz7bwsAOsfwUaHAiEzOYiR8VkXAOxI2bR65FybgcuBWPYsCEYU2e2-Z1Yqvenc7_dvW2UW1-t1hKMk3wGdicfiJx6OtsX7y0ZYgQcl1ln2fdGFWiA6VkZxi310seH0jtP8CEB-aqBTFXz3cIFNl1cZxKSMvrKU46SQB1YKR4tZWab-tuxdPLJ0seoDRZ_TcrkwpBbVhbSz8ZgOYTHhaRmC2hmaJxmP0jVYNHhcChaArCnKvim-sTC5pGbMSbg9zLqwac3Ejh0Vusgz26HaznE4BQdemQ1aCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a267a27341.mp4?token=Hr-9yNFWeUtsRvjTmRo8ZOlZ0pfO9BsKmfWzIh-K5tvpPTFWPAO9ySNz7bwsAOsfwUaHAiEzOYiR8VkXAOxI2bR65FybgcuBWPYsCEYU2e2-Z1Yqvenc7_dvW2UW1-t1hKMk3wGdicfiJx6OtsX7y0ZYgQcl1ln2fdGFWiA6VkZxi310seH0jtP8CEB-aqBTFXz3cIFNl1cZxKSMvrKU46SQB1YKR4tZWab-tuxdPLJ0seoDRZ_TcrkwpBbVhbSz8ZgOYTHhaRmC2hmaJxmP0jVYNHhcChaArCnKvim-sTC5pGbMSbg9zLqwac3Ejh0Vusgz26HaznE4BQdemQ1aCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق تصاویر ماهواره‌ای بیش از 20 فروند هواپیمای سوخت رسان آمریکایی حاضر در قطر این کشور را ترک کردند.
چنین اقدام مشابهی در روز های پیش از جنگ نیز مشاهده شده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/18564" target="_blank">📅 17:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18563">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18563" target="_blank">📅 17:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18562">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">هم اکنون جمهوری اسلامی بازهم به اربیل حمله پهپادی/موشکی کرد ، همچنین شنیده شده چندین انفجار در این منطقه گزارش و تایید شده
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/18562" target="_blank">📅 16:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18561">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">آی 24 نیوز:ایران از حزب‌الله و سایر گروه‌های متحد در منطقه خواسته است تا در حالت آماده‌باش کامل قرار گیرند،زیرا درگیری‌ها ممکن است در هر لحظه‌ای تمام عیار شوند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/18561" target="_blank">📅 16:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18560">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f38997170e.mp4?token=rINYAtLkbnkDJwv3AieCWmx3D59kcLDXO2oo9ntuDw-wEBhoY2T5UV7nq9QEXbAkNDY3DYaG1fKdYCBegauTE9xziOobaP4rophezv1dW9etPzO_bBuSz3841JlHt5eO_hpDY6GQIXYoiqhYKxAKMf_hGKrU6DJCaQn3ycP7bnIUrHCGylZHdMoQGiLuL7RmofmQzE5hlnl2rA-Oj6rIACOFGSTZjS3ZH6NKm9SeAHa40oAGEGwYLo8Z7fuBbbAUHRuRvMRr3LPCMh1r2JhkYT6imcd5-iPeHGsY-Qi4Ny2tRsmfd0Q_nFM0sgHiibGsZRwI0HiSvDKzmSAIw0ia2pqQCbqIV4iP9u2lLo69Nn8OIA0TOwLmdGMR7DdIh3G2gMxV8LtOwiWaJbUrpzuRoBLI8nMcFYZJBJqXAlvL0onh6_ew2emp4FMy2l9HVVy9OpuCZxmw08ieLD4cAuXmMd398vMI4g7gfac6F28H1-W9g_sbWGCJ0p_ZT9cOGohG4f1ItI5zI3jgRNbW9tQgkUO7seqxUVMUM5GSmaT1mvcx3ZNmhh614oA5N1to82KoWJqX0RN00NcjE_As_SPRhiuoAQgFR3TAhHvJPoPO2hNDAZc6jpu-odrAfnx8kFLXjdNALy2WXEq8oEh1LAt7Mg8f7egJj7rejESVjVZrb7s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f38997170e.mp4?token=rINYAtLkbnkDJwv3AieCWmx3D59kcLDXO2oo9ntuDw-wEBhoY2T5UV7nq9QEXbAkNDY3DYaG1fKdYCBegauTE9xziOobaP4rophezv1dW9etPzO_bBuSz3841JlHt5eO_hpDY6GQIXYoiqhYKxAKMf_hGKrU6DJCaQn3ycP7bnIUrHCGylZHdMoQGiLuL7RmofmQzE5hlnl2rA-Oj6rIACOFGSTZjS3ZH6NKm9SeAHa40oAGEGwYLo8Z7fuBbbAUHRuRvMRr3LPCMh1r2JhkYT6imcd5-iPeHGsY-Qi4Ny2tRsmfd0Q_nFM0sgHiibGsZRwI0HiSvDKzmSAIw0ia2pqQCbqIV4iP9u2lLo69Nn8OIA0TOwLmdGMR7DdIh3G2gMxV8LtOwiWaJbUrpzuRoBLI8nMcFYZJBJqXAlvL0onh6_ew2emp4FMy2l9HVVy9OpuCZxmw08ieLD4cAuXmMd398vMI4g7gfac6F28H1-W9g_sbWGCJ0p_ZT9cOGohG4f1ItI5zI3jgRNbW9tQgkUO7seqxUVMUM5GSmaT1mvcx3ZNmhh614oA5N1to82KoWJqX0RN00NcjE_As_SPRhiuoAQgFR3TAhHvJPoPO2hNDAZc6jpu-odrAfnx8kFLXjdNALy2WXEq8oEh1LAt7Mg8f7egJj7rejESVjVZrb7s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو شبکه خبر مجری زنگ زده به هتل کرون پلازا عمان و داره جاسوسی می‌کنه ببینه  چی شده
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18560" target="_blank">📅 16:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18559">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">رحیم پور ازغندی نماینده خامنه ای اول در شورای انقلاب فرهنگی:
اگر جنگ نباشد اغتشاشات شروع خواهد شد!!!
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18559" target="_blank">📅 16:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18558">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سخنگوی سنتکام، به شبکه تلویزیونی الجزیره گفته است که حملات ایران به کشورهای حوزه خلیج فارس «هیچ تأثیر عملیاتی بر نیروهای ما نداشته است»
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/18558" target="_blank">📅 16:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18557">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgovY54a4x0TJeC666iRV9qT6wgnTGEBkwelFlCqm1KkKExLNFV_QbQR4NzYxBaL8r-6P35boQxcJtE9_n14ft5CT0DZpW6QEDxsiHia3zYm40xvXSGjM77xUxn7LhaFdhiCuVc54OKdBYjQMob-M23suVbX4tijGenLi-58OS-J4Ku1u9FKl_m231xSpmBVqbFliDt5qPswJrM_fo1UyUWWZLBem2Fm2JStODTozwlfz3TGjjm2PlJZe9st_Mqp0WKPlLHCr33Mvf6HsSvFtRNCpb9RE_SYYFlJHgS0em8bcfTItVT75On4L2F9hkI-_zq24MRvW_EO5FyByYQ1xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :سخنرانی دیشب بازخورد خیلی خوبی داشت
لایحه «نجات آمریکا» رو تصویب کنید، ممنون
@WarRoom
لایحه «نجات آمریکا» ترامپ (One Big Beautiful Bill)
است. این لایحه حدود
۳.۴ تریلیون دلار
اثر مالی دارد و شامل این موارد است:
کاهش مالیات‌ها، افزایش بودجه مرزی و امنیتی، تقویت ارتش، هزینه‌های انرژی، تمدید برخی معافیت‌های مالیاتی ترامپ، افزایش بودجه اجرای قوانین مهاجرتی، و تغییرات در برنامه‌های دولتی مثل Medicaid و کمک‌های اجتماعی</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/18557" target="_blank">📅 15:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18556">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18556" target="_blank">📅 15:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18555">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">⚔️
💥
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18555" target="_blank">📅 15:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18554">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">آی‌۲۴نیوز: طی حملات دیشب آمریکا، هفت پل و ایستگاه ریلی قطار در ایران موردهدف قرار گرفتن.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/18554" target="_blank">📅 15:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18553">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPJ8fBmOHva7fZWCNaKAmwU8P8KxSOGNsSIGtISkBaoZejUGiusMffPnXevBD-gKhlKI6nRzrvdYnLS_x_1Aj2Eq47zX3nF28ebPb3G-tqH4CPDmXPELWZ__vyAjHrkw5dJ4PedVTohUM59d2nyPS_oeZNHFv1NdwRcFgE28rrjFGTtOhmYHP-WZBGog1FERjvdvN74Uv5-dFPBdDIrb61s-NjoSsBrLR08-0MEfpsLtWT1G2Bt_2SYSCq5rG6m_G81QbaRluSIVOKzkXVGrcFhmtjCJqqz-IiyFeF8c_Wu12jXg9RuKdpJx-HjNqPOV-m_q-ra6WmwSit1F_q8Law.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در بندرعباس مردم قایق‌هایشان را از اسکله بردند و جلوی در خانه پارک کردند!
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/18553" target="_blank">📅 15:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18552">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Remix Az Asemoon Dare Miad Ye Daste Hoori ~ Otaghe jang</div>
  <div class="tg-doc-extra">Yashar</div>
</div>
<a href="https://t.me/withyashar/18552" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
@withyashar
📱
https://instagram.com/yashar</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18552" target="_blank">📅 15:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18551">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دولت انگلیس بعد از اضافه کردن سپاه به لیست گروه های تروریستی:
از این پس هرکس در انگلیس از سپاه پاسداران حمایت یا با آن همکاری کند، ممکن است به ۱۴ سال زندان محکوم شود!
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/18551" target="_blank">📅 15:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18550">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">المیادین: بزرگ‌ترین شرکت گازیِ طرف قرارداد با یک شرکت گازی آمریکایی در عراق هدف قرار گرفت
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/18550" target="_blank">📅 14:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18549">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">چند گزارش از صدای انفجار ‌در ‌اهواز
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18549" target="_blank">📅 14:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18548">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdP7xASLORTQX6PsIH_jcY4kIrIL5UL-QTcIbkrnL5P4SYtGnlX-VwPGPVX9jDDtsibA0JhkPjiicXO0carkxdKog-kZbvU9iQEIo9aly2hK9LQha9NuAzkCFetHJdyT4Pv-ycHPEOy3J5HkYlx5yxOMbIXLcc_eqPEuDhJ0HwpBSeFIsPsBRyFv2S0U8h0LOAIoDejKNy0XhlUtOEHQOL8CBM9NgoBA7-mAvB9rUR3Z0bPJ2QcFo0lWHjYgemAX3ffOprslkto45mmJdcLAx1CwGWcmx_t2UQjxGx-gpoDObiz75gS4prVhvOh5NhB7F4cA3Pjt3q7CdEdJJGBdrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در 24 ساعت اخیر سرچ «لغو عضویت جانفدا» بیش از 5 هزار درصد افزایش داشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/18548" target="_blank">📅 14:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18547">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44c5aeeaa6.mp4?token=bvjP9iajQRLabp0VeckbDtAJ6mBDQZ_9vQqGxhxl3KmUTD9AD_vKX0lROPRKAV2LvVhslV4G9dlPL_MiDf3DoiHJlB5OmZpfcno8HIKFx3kCpQvVL7Io9Rp2RuA_zDS5b4TBl8HW_-IyDS-6ZGaEk_lrvhs4oX3RneF27q0znJfF03hOhp2UVNDizytNtOagb1KVGunujRC0u7TI2XgBPpXK2KIcRA0M3kNSDT4x-Z-Q4HgTYkteTSgc4Fqb6ftFrXpD2YpsddyiymgF_cRakroCkiZOSR3xD_wI8jrt-j_BArm0L_ND2_K7Y12lQQsYYJrmMKSnL0eb1CNzYmVeFQdj9IQqoRGfgnGg1vPf736xOOUS6J8JX9tS66hL7Cb2suZdcOoGxGwQpvUL41cYJVho5jPcIoJzgYJB5k2BqwHLDzzTWVYssCiga1awywCDGaY0uPQPQ2SGe5vv7IJ2umvigqfFbJVtKAOy-8DDzNGVGjUt24pWQAxQbeMhX9lk6YZUDY-f64TruBRO_K9qpFnP4OsLbfkKFTd4OUNKeSxXK3QYk-nqELE5JmnHp_gXNIBGi_wHW74TMqvZxAP0uQQ_ZhWzXUvYvuTSW39cmpnWc5T8mwcC3fWC-gShnJ3oFthInQzzUtPgeVIlh3yhLIhL03nTTmNYZuCMiWbszqU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44c5aeeaa6.mp4?token=bvjP9iajQRLabp0VeckbDtAJ6mBDQZ_9vQqGxhxl3KmUTD9AD_vKX0lROPRKAV2LvVhslV4G9dlPL_MiDf3DoiHJlB5OmZpfcno8HIKFx3kCpQvVL7Io9Rp2RuA_zDS5b4TBl8HW_-IyDS-6ZGaEk_lrvhs4oX3RneF27q0znJfF03hOhp2UVNDizytNtOagb1KVGunujRC0u7TI2XgBPpXK2KIcRA0M3kNSDT4x-Z-Q4HgTYkteTSgc4Fqb6ftFrXpD2YpsddyiymgF_cRakroCkiZOSR3xD_wI8jrt-j_BArm0L_ND2_K7Y12lQQsYYJrmMKSnL0eb1CNzYmVeFQdj9IQqoRGfgnGg1vPf736xOOUS6J8JX9tS66hL7Cb2suZdcOoGxGwQpvUL41cYJVho5jPcIoJzgYJB5k2BqwHLDzzTWVYssCiga1awywCDGaY0uPQPQ2SGe5vv7IJ2umvigqfFbJVtKAOy-8DDzNGVGjUt24pWQAxQbeMhX9lk6YZUDY-f64TruBRO_K9qpFnP4OsLbfkKFTd4OUNKeSxXK3QYk-nqELE5JmnHp_gXNIBGi_wHW74TMqvZxAP0uQQ_ZhWzXUvYvuTSW39cmpnWc5T8mwcC3fWC-gShnJ3oFthInQzzUtPgeVIlh3yhLIhL03nTTmNYZuCMiWbszqU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : وضعیت انفجاری ‌منطقه
🚨
🚨
🚨
🚨
🚨
💥
۴۰۰ هزار نفر در اتاق جنگ با یاشار!
سپاس از همراهی و اعتماد شما. این تازه آغاز راه است.
🎉
400,000 members in
@WarRoom
with Yashar!
Thank you for your trust and support. This is just the beginning.</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/18547" target="_blank">📅 14:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18546">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کپلر (Kepler) که به تحلیل داده‌های دریایی می‌پردازد: کاهش چشمگیر تردد کشتی‌ها در تنگه هرمز. دیروز، تعداد کشتی‌های عبوری به 8 رسید که کمترین میزان تردد در 3 هفته اخیر است.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18546" target="_blank">📅 14:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18545">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">هم اکنون یک اسکادران بزرگ از جنگنده‌های F-16 آمریکایی با استفاده از چهار هواپیمای تانکر سوخت، در حال حرکت به سمت خاورمیانه می‌باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18545" target="_blank">📅 14:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18544">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8008a8ae42.mp4?token=AwtrzhQPvCSIA3uCm5reSXG9zuHE7IFXYigrP6r3uQXz572rJNxKdBRYlczCETb7Qce8uPxdLTRxF5tU2oUWOm5zDGhZ2mTUNgv5xrWJnxooNpkEXYoVfqNwLXCPCAPICfBPK3YcZrQpQVAkJ2a4GSxa-L_yE2V6vduK5aUS_y1_uwFKbe3e62S3ZCMcZ6gVGs50dnAF9gsGhzjkGFzteDamAXc_NzN172lGL5XM_puax8YHKXXnXvMrokCUpuOOhDO-UR2sBKbe1rqAJISkWHT8Dw1Dfpx96nqGXEmKuC7vHR9tNvohJ8Jz16-B0T2pSRpKd6J_9kjeL6xtfrSimIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8008a8ae42.mp4?token=AwtrzhQPvCSIA3uCm5reSXG9zuHE7IFXYigrP6r3uQXz572rJNxKdBRYlczCETb7Qce8uPxdLTRxF5tU2oUWOm5zDGhZ2mTUNgv5xrWJnxooNpkEXYoVfqNwLXCPCAPICfBPK3YcZrQpQVAkJ2a4GSxa-L_yE2V6vduK5aUS_y1_uwFKbe3e62S3ZCMcZ6gVGs50dnAF9gsGhzjkGFzteDamAXc_NzN172lGL5XM_puax8YHKXXnXvMrokCUpuOOhDO-UR2sBKbe1rqAJISkWHT8Dw1Dfpx96nqGXEmKuC7vHR9tNvohJ8Jz16-B0T2pSRpKd6J_9kjeL6xtfrSimIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صف تانکرها در نزدیکی پلی که بمباران شده است
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/18544" target="_blank">📅 14:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18543">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OR6qerBkdDZlJPGKcLIQtyTDpd_Y6ivRQf5zAEeRum7RVGt1V1Djt1CiUiB8PVKqFPxlp1COfWxDK56B9s_s9NRMO1qBNOmJfqG-ExvMf52Sbq0v6YgQ1ZUfcSirn7JMk4ukiDkAZRkwPZ7feSwEqRGnZFHtiLzTeiq-CSywDDbpp1r_UQjDao8zHT2sopltXD9PG8LCfeozJOg-KlBaIA7W32PjrcA-NLeVGFHIlspG5ebgQmVyGMMED7HrwnVtMxEyxTHQacoogVPWmRozz-GZ69fMD-8gmSswW3GGZ36ZoGDEV2qumPn1sTwM6OR3FueLstbUH46sAXfWnss2kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تتر تا ۱۹۵،۰۰۰ تومان پرواز کرد و هم اکنون ۱۹۲،۰۰۰ معامله میشود
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/18543" target="_blank">📅 13:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18542">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/315ffdb490.mp4?token=WFEYCQ0Y231IzhUkiCKbPzVoI5-w52zt94KCgXguqecQwi3CfXDJmbj6WxFkaa_S8XM9VpDCl1Fzx6tcEtShcwoDxaYGaerPbC4iIXHP_ykqpz43Ktnav6SQ7HYN-uh4Y5fHVGEhQ22POc39M7DCxz8t9nyrxjdMNI0xqte05MwSMapOrgwaLXMG1ITV5Y-GEEkFlwfmEJ22oXjIIifJhdMBkPPNHIgLPbQ-s_hJDHEGM5lnAXAVRpnDJdsWLgN56awAcDh_xtSG9THMdt5eYu0vQXZr67OvpbeHVu47svRxK5KqI0pN1ByEkggrp4aCzcTYeYFGj54z3iLY6aTbhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/315ffdb490.mp4?token=WFEYCQ0Y231IzhUkiCKbPzVoI5-w52zt94KCgXguqecQwi3CfXDJmbj6WxFkaa_S8XM9VpDCl1Fzx6tcEtShcwoDxaYGaerPbC4iIXHP_ykqpz43Ktnav6SQ7HYN-uh4Y5fHVGEhQ22POc39M7DCxz8t9nyrxjdMNI0xqte05MwSMapOrgwaLXMG1ITV5Y-GEEkFlwfmEJ22oXjIIifJhdMBkPPNHIgLPbQ-s_hJDHEGM5lnAXAVRpnDJdsWLgN56awAcDh_xtSG9THMdt5eYu0vQXZr67OvpbeHVu47svRxK5KqI0pN1ByEkggrp4aCzcTYeYFGj54z3iLY6aTbhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل مسیر به گچین و بندرعباس
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18542" target="_blank">📅 13:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18541">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خبرگزاری CNN: ترامپ در حال دریافت گزینه‌هایی برای گسترش عملیات نظامی آمریکا علیه ایران است
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18541" target="_blank">📅 13:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18540">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ونس به NBC نیوز : فکر نکنید کنترل امنیت تنگه هرمز کار آسونیه؛ این کار حسابی دردسر داره، چون با پهپادهای ارزون‌ قیمت خیلی راحت میشه کشتی‌ها رو هدف قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18540" target="_blank">📅 13:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18539">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سپاه: جنگنده‌ها و سوخت‌رسان‌های آمریکا در اردن و مواضع آمریکا در کویت را هدف قرار دادیم
سپاه پاسداران اعلام کرد در
موج ۱۴ عملیات نصر ۲
و در واکنش به حملات پنجشنبه شب آمریکا، با موشک‌های بالستیک و پهپادها جنگنده‌ها و سوخت‌رسان‌های آمریکا در
اردن
را در دو مرحله هدف قرار داده که به ادعای این نهاد،
چند فروند سوخت‌رسان و جنگنده منهدم و تعدادی دیگر به‌شدت آسیب دیده‌اند.
سپاه همچنین در
موج ۱۵ عملیات نصر ۲
مدعی شد علاوه بر
انهدام سکو و موشک‌های هایمارس در کویت
، با حمله موشکی و پهپادی
چندین محل استقرار نیروهای آمریکایی و «ضدانقلاب»
را هدف قرار داده است. این نهاد مشخص نکرده منظور از «ضدانقلاب» چه گروه‌هایی است.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/18539" target="_blank">📅 13:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18538">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d31df15619.mp4?token=AWQ97YN4GDgWMTea3328BKnP0DjMy8rXLB-XXjvsEEMuqEqyIo3EwH1rCspJ6W0hjZlxaEzErk4PJlJuVUo4XRXsgIddNOTN6Q5WojprVG9a6fWTXB92cvD1FPR7QoMVf5gHG-dgHZ4vlEYeW7u6Cb2eL7EtH61gB-mvT7bWWuUs2NVzMvkUy_jLNQEW4g4bq_5eflBEpKHhfRn6Pc-j9lRIARiyBGfzuT7NRFCKjiPJQLF4CswntERmksMEWKgTccwXvTFzWpXxYFXB9kqSeMOtvmvyUbOJ7nmfN-gUXIAiOZ5FuSgepbsuxkcTkY1ftMWObHeiH_S5IRQGAtTgEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d31df15619.mp4?token=AWQ97YN4GDgWMTea3328BKnP0DjMy8rXLB-XXjvsEEMuqEqyIo3EwH1rCspJ6W0hjZlxaEzErk4PJlJuVUo4XRXsgIddNOTN6Q5WojprVG9a6fWTXB92cvD1FPR7QoMVf5gHG-dgHZ4vlEYeW7u6Cb2eL7EtH61gB-mvT7bWWuUs2NVzMvkUy_jLNQEW4g4bq_5eflBEpKHhfRn6Pc-j9lRIARiyBGfzuT7NRFCKjiPJQLF4CswntERmksMEWKgTccwXvTFzWpXxYFXB9kqSeMOtvmvyUbOJ7nmfN-gUXIAiOZ5FuSgepbsuxkcTkY1ftMWObHeiH_S5IRQGAtTgEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏کل وزارت صنعت معدن تجارت این روزا:
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18538" target="_blank">📅 13:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18537">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca43767734.mp4?token=ViZKKC3vueqCYvLN2dpV8QAOQlj1qYckH5cRXSJdEaWGWB3_Ye8RSI2osfr8zUMyGfuCRCfrYWXGdTSXWuo9973x37Z-9gvqGrYaI7WwJBCFhTXEvKiBAkO5b49Ns88EZYy4Uw5xNKTyBxHNuUpMMbevH2YfxpgjiPm2BnL2v6RCF60Dx08ev72tW4nhHtFtlLMUdFYWiX3oNJXTNAzmKmsznL0USNDSnrOkSXR0JCa60AtAeokXqIY_I2BdIir5IuX_WXd0pA2k40mo_ddCYdXyENyzKwrMiSUvXZHUnA8lyYV6RLfi88kLAHFtvVXR2XnE6N1KFckbNKlmZz4FYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca43767734.mp4?token=ViZKKC3vueqCYvLN2dpV8QAOQlj1qYckH5cRXSJdEaWGWB3_Ye8RSI2osfr8zUMyGfuCRCfrYWXGdTSXWuo9973x37Z-9gvqGrYaI7WwJBCFhTXEvKiBAkO5b49Ns88EZYy4Uw5xNKTyBxHNuUpMMbevH2YfxpgjiPm2BnL2v6RCF60Dx08ev72tW4nhHtFtlLMUdFYWiX3oNJXTNAzmKmsznL0USNDSnrOkSXR0JCa60AtAeokXqIY_I2BdIir5IuX_WXd0pA2k40mo_ddCYdXyENyzKwrMiSUvXZHUnA8lyYV6RLfi88kLAHFtvVXR2XnE6N1KFckbNKlmZz4FYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایگاه هوایی  عقاب  در جنوب که در زیر کوه ساخته شده و قرار بود از جنگنده‌های نیروی هوایی ایران در مقابل حملات هوایی دشمن محافظت کند با حمله مواجه شده و تونل‌های ورودی و خروجی بسته شده
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18537" target="_blank">📅 13:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18536">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc0c4907fb.mp4?token=RrHbvdaqvNvwGf13R2p-hfDruXzOywqdJOHbMoyDoUMfIB-doqHbdk-W8jk1z2_zp9IYa69VMzHKOHxEBuOj5RbRO2XDEy7nl6bH4Qum7p8u-DcdYuU5fV9XhIuJejKcCh9tI0E2cGhV9Du1WsvtKjhXZEFMrbhkP8EDqULzhM0W8UGqXXx55PEIWkSzVQhscbprf9sgzZmDomVobiU48SpG8BN4os2eF-SNgXy3SVvamGTtNWMCc1d2JzwtRTNjG4zBibzXvbNy9ZzOTNg6gYmBTbmrI6qyb0ysxydsxFcegdhYPz-eqMBzEkO4gM6Can6uv0tsXr2IsSmftwkVGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc0c4907fb.mp4?token=RrHbvdaqvNvwGf13R2p-hfDruXzOywqdJOHbMoyDoUMfIB-doqHbdk-W8jk1z2_zp9IYa69VMzHKOHxEBuOj5RbRO2XDEy7nl6bH4Qum7p8u-DcdYuU5fV9XhIuJejKcCh9tI0E2cGhV9Du1WsvtKjhXZEFMrbhkP8EDqULzhM0W8UGqXXx55PEIWkSzVQhscbprf9sgzZmDomVobiU48SpG8BN4os2eF-SNgXy3SVvamGTtNWMCc1d2JzwtRTNjG4zBibzXvbNy9ZzOTNg6gYmBTbmrI6qyb0ysxydsxFcegdhYPz-eqMBzEkO4gM6Can6uv0tsXr2IsSmftwkVGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت همین الان پل بندر خمیر که کامل از بین نرفته و خودرو سبک عبور میکند
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18536" target="_blank">📅 13:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18535">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حوثی‌های یمن به یک کشتی در تنگه باب‌المندب حمله کردند @WarRoom
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/18535" target="_blank">📅 12:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18534">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ادعای اینتل‌واچ: سناتور لیندسی گراهام توسط سم نوویچوک تماسی
(استنشاق، بلع یا تماس پوستی)
کشته شده است
.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/18534" target="_blank">📅 12:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18533">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کانال ۱۲ اسرائیل : موج بعدی حملات آمریکا قراره خیلی شدیدتر باشه و‌ احتمالا تهران و بقیه شهر هارو هم بزنه.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/18533" target="_blank">📅 12:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18532">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حوثی‌های یمن به یک کشتی در تنگه باب‌المندب حمله کردند
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18532" target="_blank">📅 12:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18531">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کویت اعلام کرد که یکی از ایستگاه‌های تولید برق و تصفیه آب مورد حمله ایران قرار گرفته است، که این حمله خسارات زیادی به واحدهای تولید برق وارد کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/18531" target="_blank">📅 12:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18530">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/896d0f778e.mp4?token=pnKcLbKNaRCq3oQkoYaKw7R1nIb2cEM20V0FBNIpp0xB17s-ggfMd7tI2HoOu5Gh7gdwW3R9oxLlYs9xFo3vNMulx5pap9TC_ORRsyh2A0_rzE5TFt97c-y-FaW7ntBFeH3hMVzpjpXdT1YtgEiDRu3MIoGCQK4heJU5m5kcEpoLYz3idqqBs4tVE8A6zYlrjlnUiEarr4V5gqoK1fYztdY9qcNNe15dUzGD0VxIbDnRcgz5_EOPodf_4QvaBd_-B0em2eIHP8KXvShd8OsTyKthYN6ohHsQ4VapdrY7yYZOpXwlHiG5iw9CnOkHUrBjczE-CwBHMT2yQXTBAQisXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/896d0f778e.mp4?token=pnKcLbKNaRCq3oQkoYaKw7R1nIb2cEM20V0FBNIpp0xB17s-ggfMd7tI2HoOu5Gh7gdwW3R9oxLlYs9xFo3vNMulx5pap9TC_ORRsyh2A0_rzE5TFt97c-y-FaW7ntBFeH3hMVzpjpXdT1YtgEiDRu3MIoGCQK4heJU5m5kcEpoLYz3idqqBs4tVE8A6zYlrjlnUiEarr4V5gqoK1fYztdY9qcNNe15dUzGD0VxIbDnRcgz5_EOPodf_4QvaBd_-B0em2eIHP8KXvShd8OsTyKthYN6ohHsQ4VapdrY7yYZOpXwlHiG5iw9CnOkHUrBjczE-CwBHMT2yQXTBAQisXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همکنون با صدا درآمدن آلارم حمله هوایی در دوحه، پایتخت قطر، پدافند مشغول دفع حملات است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/18530" target="_blank">📅 12:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18529">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آلارم حمله موشکی در پایتخت قطر دوحه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18529" target="_blank">📅 12:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18528">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e27b43e6c.mp4?token=JCNAJ1-Tyt_gefVuNo-FgZhZnUfojwtj4sovZR8fwQttW9clvxYnGSwF6bb-79WQ9dSNOoP2iRdptUksZy3nnZP1qs1kZczMfGMS8Weky9ZlX3YkEXKF2kGAhykfvPy7QmAJ_PED33EepRaFFvZnK9xT_Joln_LeFTC5TjCwHvMVBxT3iiBXuNIXa_bFQeDmA4I78ldt1B9t3Esy4-ql8IfG9WoMbwvc04saVZPPlhg22k8OqxXMwUrEO3rNuEMKy2k7mHwYyB9-iJ6XwgXbgEhTadOjJ1BUrUArhYjVzn3xdVltFaKICix0R8LaJ1c2jI50a1SGZkutgrZJfcdW_2U-Xo5_Awi7PIaSYJoIxBFyzdb4DWzlgm-mvAHZ9fRQQrzFtCrT-R63Z_5Wu1uMBEvwGuIpa55y9scKMpTKqgBh890bjHWAiPIsQXJapSkyPEFIAiuPAVs2osawPJ5TmQxJGehkM_qMs63WFH2-4E5ZeeczV-7vrpvZWOV8ZmsDLJK876Wxc57jmonveuBjbll_sgP8W33aWOShxqq2T2mkjshmCEu_y_fr194z_xddIMdMwntrOvGjjAOCVErPlqoQh4j7IhF5zVU0jGC3G_6yE6WiVkp1qGku0B1TgNLRvGCwnE6Bzegl3tAgu-vRZcJlLa-YZmRWGt9OW3N-Z8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e27b43e6c.mp4?token=JCNAJ1-Tyt_gefVuNo-FgZhZnUfojwtj4sovZR8fwQttW9clvxYnGSwF6bb-79WQ9dSNOoP2iRdptUksZy3nnZP1qs1kZczMfGMS8Weky9ZlX3YkEXKF2kGAhykfvPy7QmAJ_PED33EepRaFFvZnK9xT_Joln_LeFTC5TjCwHvMVBxT3iiBXuNIXa_bFQeDmA4I78ldt1B9t3Esy4-ql8IfG9WoMbwvc04saVZPPlhg22k8OqxXMwUrEO3rNuEMKy2k7mHwYyB9-iJ6XwgXbgEhTadOjJ1BUrUArhYjVzn3xdVltFaKICix0R8LaJ1c2jI50a1SGZkutgrZJfcdW_2U-Xo5_Awi7PIaSYJoIxBFyzdb4DWzlgm-mvAHZ9fRQQrzFtCrT-R63Z_5Wu1uMBEvwGuIpa55y9scKMpTKqgBh890bjHWAiPIsQXJapSkyPEFIAiuPAVs2osawPJ5TmQxJGehkM_qMs63WFH2-4E5ZeeczV-7vrpvZWOV8ZmsDLJK876Wxc57jmonveuBjbll_sgP8W33aWOShxqq2T2mkjshmCEu_y_fr194z_xddIMdMwntrOvGjjAOCVErPlqoQh4j7IhF5zVU0jGC3G_6yE6WiVkp1qGku0B1TgNLRvGCwnE6Bzegl3tAgu-vRZcJlLa-YZmRWGt9OW3N-Z8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خیلی وطنپرستی ‌نبین حالت بد میشه
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/18528" target="_blank">📅 12:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18527">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ورود تانک‌های ارتش اسرائیل در مناطق حداتا و حاریص در جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/18527" target="_blank">📅 12:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18526">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">علیرضا فغانی داور فینال نشد.
فیفا رسماً اعلام کرد اسلاوکو وینچیچ، داور اسلوونیایی، قضاوت فینال جام جهانی 2026 بین آرژانتین و اسپانیا رو برعهده داره.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18526" target="_blank">📅 12:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18525">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یک مسئول در حزب کومله کردستان ایران:
شش موشک به مقر ما شلیک شد، از این تعداد، سه موشک به مکانی اصابت کردند که در آن هشت نفر از نیروهای پیشمرگه کشته شدند، و سه موشک دیگر نیز در نزدیکی همان مکان سقوط کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18525" target="_blank">📅 11:59 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
