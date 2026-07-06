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
<img src="https://cdn4.telesco.pe/file/sjqaU07aHJT9aIsxjjxmbgbBhJdB-Z006c3Zp3ZZgNKvtpaZhAokryx4QHvxAa6PRAPcD8PmnMjyf1ilKG1CyIt5n4Ky8eD3QmoIcswgBypGEgLczJv3vCdYJmv6vhCaBQIfprnkBq0rAoCxtvLyZvDQt2yek-xybhzhNWxbPHchMk3_Vj485bh5RD9g0U4f5VLpTrDwQeLW0fixQYCDUhDiWJ-gxUeVOpaPp56QgvCIYxcZtWUQ9QrHZV7fm8niKkqsHUWUfhFhr1da2dPzsAxGaC7eVh1mtc4X1zWihxlO8w7J7L-uESNrSgMnqOXeVfWtVRJ53mGtbmUTCXlvIA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 338K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 21:40:27</div>
<hr>

<div class="tg-post" id="msg-16587">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36f95eb134.mp4?token=S7G6KcQLGCCJCh3MyUhOxq4u65TWf1_1tUv4tONCbOykYgaklOPMkFxf3HKfUH-FqdK-V5zlEzn5zMd55M_W73xzf1T6pfZ4Kj4fanw3KD9OQFMS-2F9FOusYdlCuVpZaUTIX6pykN8cJZ10gBl4tYNISv2K2Ja_C2_3PuHs7dimkl7WjCZgMqa0_RqxIAp97yPtUWTkGVuvrtjoggxjfBCwlLNHLqmAkT3PZVVlihCfIb22fMwq44_viKs4JoRLgwOs0jeMDqcZr_6hKECXWrnFKnJiK_0_XTQi_yyrH6KaDgUrlq0_NdBPy_IhHgFo04w2l6KzuMm_N3lgUQ6MYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36f95eb134.mp4?token=S7G6KcQLGCCJCh3MyUhOxq4u65TWf1_1tUv4tONCbOykYgaklOPMkFxf3HKfUH-FqdK-V5zlEzn5zMd55M_W73xzf1T6pfZ4Kj4fanw3KD9OQFMS-2F9FOusYdlCuVpZaUTIX6pykN8cJZ10gBl4tYNISv2K2Ja_C2_3PuHs7dimkl7WjCZgMqa0_RqxIAp97yPtUWTkGVuvrtjoggxjfBCwlLNHLqmAkT3PZVVlihCfIb22fMwq44_viKs4JoRLgwOs0jeMDqcZr_6hKECXWrnFKnJiK_0_XTQi_yyrH6KaDgUrlq0_NdBPy_IhHgFo04w2l6KzuMm_N3lgUQ6MYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکرون با عینک آفتابی معروفش که ترامپ مسخرش میکنه وارد سوریه شد
@withyashar</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/withyashar/16587" target="_blank">📅 21:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16586">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">رئیس‌جمهور فرانسه پس از ۱۸ سال وارد سوریه شد
یک منبع ریاست‌جمهوری فرانسه اعلام کرد که سفر رئیس‌جمهور این کشور به دمشق با هدف از سرگیری همکاری‌های اقتصادی و تجاری با سوریه انجام می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/withyashar/16586" target="_blank">📅 20:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16585">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a3ca4796.mp4?token=lGW1ZniRVT5tVJVXbnwlEoHL4DgHBXnSoQA4NDeWxT_p-XkoYyfcKbe1dUItkYMtVCojMpMj2HDbuB3rA7D_WwE_zdhOaBJjccxPdLaLf-LBht_B-RyzIqCGGF3XN-1p6EVM3GXrLEgsN7-op9tNoaOrMFEORdTaFKKd8lFLlbfw59bWE2p0dAXmPoHacGJh9KV37jG_YBdhqq2t0lgWU2ZsPrSBqbiE0HzSj2Sz3F_75O42hxmpiFux8yMmWz_hsRvmVCessRwpbWvCBUgYjzPEmji-cj4YzMX8TU32Dx5bz7_xJ2-oV1-gq6r678DEBpAc1Gogho54AtQwhrrOqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a3ca4796.mp4?token=lGW1ZniRVT5tVJVXbnwlEoHL4DgHBXnSoQA4NDeWxT_p-XkoYyfcKbe1dUItkYMtVCojMpMj2HDbuB3rA7D_WwE_zdhOaBJjccxPdLaLf-LBht_B-RyzIqCGGF3XN-1p6EVM3GXrLEgsN7-op9tNoaOrMFEORdTaFKKd8lFLlbfw59bWE2p0dAXmPoHacGJh9KV37jG_YBdhqq2t0lgWU2ZsPrSBqbiE0HzSj2Sz3F_75O42hxmpiFux8yMmWz_hsRvmVCessRwpbWvCBUgYjzPEmji-cj4YzMX8TU32Dx5bz7_xJ2-oV1-gq6r678DEBpAc1Gogho54AtQwhrrOqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنازه خامنه ای برای همیشه تهران را ترک و برای شروع تور ‌کنسرت ها کمی پیش به قم رسید
@withyashar</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/withyashar/16585" target="_blank">📅 20:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16584">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34927b66b.mp4?token=lfSKNQqUmD11BvQUw6DLJEA0VI5fHdQS6ypNP51v38ng1YyFRQAOtDad7wJXsHQ4pnm_ys5LG4Z1L_YafYCZC7YnZwNc24bfYE0JzVDM8E9vhmi7DIrdKCDKgMPff2L7uHL-sABDHMUKSaCKNWNP15s5IK_vLFdx3YMMFXKJpm36tD-SZPY50aTmIDaZSmxBg6TDrC1VQWKGuvmXNcWpSw7Q7u4l0_jV5qqcd6Gd3gErBbr8-p-z3Kv_zEZRKxyQ7GWx8xoRu-EVsnZe5GQ-RjNB7q8QeOT-3KH-d7TDA4CGE5dhUjehnhxR00VZSdParS9g1pYU2ybhnlmPlB7Nwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34927b66b.mp4?token=lfSKNQqUmD11BvQUw6DLJEA0VI5fHdQS6ypNP51v38ng1YyFRQAOtDad7wJXsHQ4pnm_ys5LG4Z1L_YafYCZC7YnZwNc24bfYE0JzVDM8E9vhmi7DIrdKCDKgMPff2L7uHL-sABDHMUKSaCKNWNP15s5IK_vLFdx3YMMFXKJpm36tD-SZPY50aTmIDaZSmxBg6TDrC1VQWKGuvmXNcWpSw7Q7u4l0_jV5qqcd6Gd3gErBbr8-p-z3Kv_zEZRKxyQ7GWx8xoRu-EVsnZe5GQ-RjNB7q8QeOT-3KH-d7TDA4CGE5dhUjehnhxR00VZSdParS9g1pYU2ybhnlmPlB7Nwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این نسل چی میخواد از جون ما ؟
اومده تخم مرغ آبپزشو بگیره…
@withyashar</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/withyashar/16584" target="_blank">📅 20:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16583">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8667c144e.mp4?token=qWPGzXijIEG2TSxn4XcDHv5rfbqE2BoYuLZN6AqUnia_ZP74GwcA7-yotbBemcIueJCSKwMVjoq6fvn7Iwi-Rvj5n3l4U5tXLqSeVZmm8vnJkz32J2_bruOS-FPiOrCXM4IAg45HPppV62Ma4q16foqzkIbNgK9W5sByOn3Out_ea9MhFXSJeQm-h9Nz3pWsyoxOOx3BxRNEynT8w4j1bkPuJKGMDVmpg2JBWYc4a5M2ZFeocrEqFgRaxRamc34IMdSFFQjqTXhtVmUMCAf7XJJbXMBy1I5JKHo6E9oNCifw2pUS0E0SqMZfz5JfB0__VcIlH-5s_tFStc77XHFgFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8667c144e.mp4?token=qWPGzXijIEG2TSxn4XcDHv5rfbqE2BoYuLZN6AqUnia_ZP74GwcA7-yotbBemcIueJCSKwMVjoq6fvn7Iwi-Rvj5n3l4U5tXLqSeVZmm8vnJkz32J2_bruOS-FPiOrCXM4IAg45HPppV62Ma4q16foqzkIbNgK9W5sByOn3Out_ea9MhFXSJeQm-h9Nz3pWsyoxOOx3BxRNEynT8w4j1bkPuJKGMDVmpg2JBWYc4a5M2ZFeocrEqFgRaxRamc34IMdSFFQjqTXhtVmUMCAf7XJJbXMBy1I5JKHo6E9oNCifw2pUS0E0SqMZfz5JfB0__VcIlH-5s_tFStc77XHFgFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش هایی از حمله و درگیری بسیجی ها با قالیباف در میدان آزادی  @withyashar</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/withyashar/16583" target="_blank">📅 19:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16582">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiOBNdlHcj2u7by0c4i4-lxjxQ63elvO7pHn28CxBpMxmkSdBgm70TGz9Fl9yWgWHr7xr6wzhBTtuezc94YEZ5WkDFHJXW4bnr5xogobq8Em1sYHqL9JVFeLLtTljoxu1iarqdS712jB9FVNWXsX4UM4jIqWM_FQ8GIBMl6L4jg9kZHPeCsXNGDkEWctlfAbZasGa9atOUPtsyddS5a570zWXU-b6AuaenMOsiNIPOtoOHQR82x8sDJeltZZeelVtqm4-z4HKEaZ_pKA7Zxnw4oLgJcjhEel9qfwOlExMSb4jcC00gi96D0yE932DCfKuer5lw7iXjdthyGwz1uZSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهام شرکت دل پس از اظهارنظر دونالد ترامپ مبنی بر اینکه «بروید و یک کامپیوتر دل بخرید» ۸.۳ درصد افزایش یافت
@withyashar</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/withyashar/16582" target="_blank">📅 19:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16581">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ : ما از ایران امتیازاتی گرفتیم و آنها باید به آنها پایبند باشند و ما همچنین اورانیوم غنی‌شده با خلوص بالای ایران را دریافت خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/withyashar/16581" target="_blank">📅 18:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16580">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2ae96c363.mp4?token=cmmPNKE5I2zG8nc56EnY60tWVZc36fezl1KT7qzG4yZx_MutWlD32sy57PcmYm161QaOiVSWffQcGB7LsP2a44DN091NflZoBWc-C1J3v0k1VnNcKCqJOFRe6iS_mNm_RanUF0lsVnkKOnP7DayEB2UNJ0J7239WirLqyIlTlLAhlnhk3F98NL1da_WsuDOyaTGoUnR38_W3m8HmoBPDPt457nSxgJ9BZvCORaS9OT2E6Gatkj-sutVKEzcIi6_tne0r48qkPyVrtyo-sTNNXRI4Cec7Kp7MBWxC3aZSwSzZNYL5YSeUaz_XyoIQGtzGf3CH0Bq5ycyf5Qn7iSb1lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2ae96c363.mp4?token=cmmPNKE5I2zG8nc56EnY60tWVZc36fezl1KT7qzG4yZx_MutWlD32sy57PcmYm161QaOiVSWffQcGB7LsP2a44DN091NflZoBWc-C1J3v0k1VnNcKCqJOFRe6iS_mNm_RanUF0lsVnkKOnP7DayEB2UNJ0J7239WirLqyIlTlLAhlnhk3F98NL1da_WsuDOyaTGoUnR38_W3m8HmoBPDPt457nSxgJ9BZvCORaS9OT2E6Gatkj-sutVKEzcIi6_tne0r48qkPyVrtyo-sTNNXRI4Cec7Kp7MBWxC3aZSwSzZNYL5YSeUaz_XyoIQGtzGf3CH0Bq5ycyf5Qn7iSb1lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بررسی ترافیک کشتی‌های تجاری از طریق تنگه هرمز طی ۲۴ ساعت گذشته که از طریق مرین ترافیک قابل مشاهده است، نشان می‌دهد که اکثریت قریب به اتفاق کشتی‌ها همچنان از طریق طرح جداسازی ترافیک (شمالی) ایران عبور می‌کنند و تنها تعداد کمی از آنها کریدور جنوبی تحت حمایت ایالات متحده از طریق آب‌های عمان را انتخاب می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/16580" target="_blank">📅 18:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16579">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39cbbf8bec.mp4?token=L0-jp0NcQOu_5AQ-49UNtekpl6eWdBr6J0bjD9VKzvZPQEex6Lct-XnMoOt4H_R0vTkgdJ1pp7ia8CL83Aivl02mBIwnZyJVLuXQvT6ztjktSeWZWO7mAAYy8PdeJUL8y_nrRPVB4JPNasP0x242m7putGZ4ATMzuGJrpQT915C6B3QtRXHQ5sCGUZvXULRNSwcvB2oTiWNoqT2uLBdSju_4dm3fY8m8niFelzSIhLMc6AFOav2oCFm6782PGKG5oE8Q04xzt_oZL8zfHQYgBkptdisxnPR0mywaU49Ul9Cnl7AYGQbprJWR59LnjPRrGi252DQoFmzMsj4UPEGIZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39cbbf8bec.mp4?token=L0-jp0NcQOu_5AQ-49UNtekpl6eWdBr6J0bjD9VKzvZPQEex6Lct-XnMoOt4H_R0vTkgdJ1pp7ia8CL83Aivl02mBIwnZyJVLuXQvT6ztjktSeWZWO7mAAYy8PdeJUL8y_nrRPVB4JPNasP0x242m7putGZ4ATMzuGJrpQT915C6B3QtRXHQ5sCGUZvXULRNSwcvB2oTiWNoqT2uLBdSju_4dm3fY8m8niFelzSIhLMc6AFOav2oCFm6782PGKG5oE8Q04xzt_oZL8zfHQYgBkptdisxnPR0mywaU49Ul9Cnl7AYGQbprJWR59LnjPRrGi252DQoFmzMsj4UPEGIZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد جنگهای پهپادی: چه کسی فکر می‌کرد که پهپادها به چنین عاملی تبدیل می‌شوند؟ آن‌ها ماشین‌های کشنده هستند.
شگفت‌انگیز است.
شما پشت درختی پنهان می‌شوید و آن می‌آید و شما را می‌گیرد.
و من صحنه‌هایی را دیده‌ام که نمی‌خواهم ببینم و نمی‌خواهم شما هم ببینید.
@withyashar</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/withyashar/16579" target="_blank">📅 18:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16578">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ: نیروی دریایی ایالات متحده بزرگترین محاصره‌ای را که جهان تاکنون دیده است، علیه ایران اعمال کرد و حتی یک کشتی هم نتوانست از آن عبور کند.
هیچ پولی به ایران نمی‌دهیم
@withyashar</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/16578" target="_blank">📅 18:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16577">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d1c3a4bd0.mp4?token=cyZ5vI6tobojHGPA3f9rfT0USClVX9w2pIehVRar6cpp2lqUplHOd9EwDEaQ-LN_nd8dER7aR_LwCB4Zu67G9aVxj_2V_dEpU6fvS-taptxgBWnuBh1slbQt6lQxD0W4Hd1PNAnEi31JeJ_AFVegC69MZlnfdaURMtUeWws0Hy5X-qQ4yyi8Ai1PjfqFB1PUk2aOe0mVVD65f6q5tD5r-RqQjZ00BFRaaA79c3tamLg6RZ_f2VcIPPwyGGoXxRSQ7wl-gZQ3q-idhrgzfApqPBdGghB_15_erKIXeAoXutTTTbtCT1Dg1DUq5v30l2S8eAO81mTOzV9EjIYceA8b0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d1c3a4bd0.mp4?token=cyZ5vI6tobojHGPA3f9rfT0USClVX9w2pIehVRar6cpp2lqUplHOd9EwDEaQ-LN_nd8dER7aR_LwCB4Zu67G9aVxj_2V_dEpU6fvS-taptxgBWnuBh1slbQt6lQxD0W4Hd1PNAnEi31JeJ_AFVegC69MZlnfdaURMtUeWws0Hy5X-qQ4yyi8Ai1PjfqFB1PUk2aOe0mVVD65f6q5tD5r-RqQjZ00BFRaaA79c3tamLg6RZ_f2VcIPPwyGGoXxRSQ7wl-gZQ3q-idhrgzfApqPBdGghB_15_erKIXeAoXutTTTbtCT1Dg1DUq5v30l2S8eAO81mTOzV9EjIYceA8b0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره اورانیوم غنی شده در ایران:
ما قرار است چیزی را که من به آن گرد و غبار می‌گویم، یعنی مواد غنی‌شده، به دست آوریم. من به آن گرد و غبار هسته‌ای می‌گویم.
من به یک دلیل بسیار قوی وارد عمل شدم و آن این است که ایران نباید سلاح هسته‌ای داشته باشد. من به دنبال تغییر رژیم نیستم، هرچند این همان تغییر رژیم است.
رژیم اول رفته است. رژیم دوم رفته است. و من فکر می‌کنم رژیم سوم منطقی‌تر است، اما خواهیم دید.
@withyashar</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/withyashar/16577" target="_blank">📅 18:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16576">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6831709af6.mp4?token=adc-0rJb2TNKYOhJD3RKR1E-3QcEj9q7oIigDN003uhYuJBKUvhkXPxexZlGEyLEpezTEpT3GZOj8zq-gOBP7Ys8V8KFpnX6gbSs3oDXjo0m_WJ_I4Hq45MInpYj0OgBkVxPcnNdYbJjuO7KOtOXSDj_BaEiMXx0BYYNbSlddUHfXZui6D3twZix9Zr_9VgjAUNLm87IBadGvKQUCN4J1ZtFTE2BULuO0hj8DQJb0SfELBCQf1CfG6iSP5JGuL6C02ZmIZv5OfLMdRkNZydufpyMzCARcEgThaFf9ARfHEs3jtWal1BVQLDv8INiNfSoXCf04cJ6Vh4hr0DQ0CedFVYgAZ2t4HXm3EROoctAvqf9jp-olePM5VcnKfky1M6Rx49KpSVwteg7eYjU7TLcCmi5UztCCNkn-5ZPortuQN3pzj0uk-WsfRbxZ31yjyTmtacIvama8PFCM3-TL3GrW1hCYzd1AvMw-IftDIqwdGVHXqHl7LY7mHBuC9uIg8HNT3vkAcf1jFROA32PjXU5pmZe3R8ax7ntu-Wbx_hNN1ZtktYgyuks2uCrevox0ltb6vy1pgnTioJYLvTxTZVzcFdj0BSYOu_heZrOPJy5HRxFCQcySh5b9fPLlbBjcjD1ILPnbjZTaPGXSBS7u171xTCJahJ4TxMSyPOyg9OZyhk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6831709af6.mp4?token=adc-0rJb2TNKYOhJD3RKR1E-3QcEj9q7oIigDN003uhYuJBKUvhkXPxexZlGEyLEpezTEpT3GZOj8zq-gOBP7Ys8V8KFpnX6gbSs3oDXjo0m_WJ_I4Hq45MInpYj0OgBkVxPcnNdYbJjuO7KOtOXSDj_BaEiMXx0BYYNbSlddUHfXZui6D3twZix9Zr_9VgjAUNLm87IBadGvKQUCN4J1ZtFTE2BULuO0hj8DQJb0SfELBCQf1CfG6iSP5JGuL6C02ZmIZv5OfLMdRkNZydufpyMzCARcEgThaFf9ARfHEs3jtWal1BVQLDv8INiNfSoXCf04cJ6Vh4hr0DQ0CedFVYgAZ2t4HXm3EROoctAvqf9jp-olePM5VcnKfky1M6Rx49KpSVwteg7eYjU7TLcCmi5UztCCNkn-5ZPortuQN3pzj0uk-WsfRbxZ31yjyTmtacIvama8PFCM3-TL3GrW1hCYzd1AvMw-IftDIqwdGVHXqHl7LY7mHBuC9uIg8HNT3vkAcf1jFROA32PjXU5pmZe3R8ax7ntu-Wbx_hNN1ZtktYgyuks2uCrevox0ltb6vy1pgnTioJYLvTxTZVzcFdj0BSYOu_heZrOPJy5HRxFCQcySh5b9fPLlbBjcjD1ILPnbjZTaPGXSBS7u171xTCJahJ4TxMSyPOyg9OZyhk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : یا توافق میکنیم یا کار رو تموم می‌کنیم، تمام کردن کار سخت نخواهد بود.
من ترجیح می‌دهم توافق کنیم چون نمی‌خوام به ۹۱ میلیون نفر آسیب بزنم. می‌تونیم پل‌هایشان رو در یک ساعت خراب کنیم.
می‌تونیم تأمین انرژی‌شان رو قطع کنیم، تمام کارخانه‌های بزرگ که ساختن، کارخانه‌های بزرگ، زیبا و مدرنی که پول زیادی هزینه شده بود. حالا دیگر پولی هم ندارن. ما پولی به آن‌ها نداده‌ایم.
می‌توانیم برق و نیروگاه‌های تولید انرژی‌شان رو، به قول من، در بخش کوچکی از یک بعدازظهر از کار بیندازیم. هر نیروگاهی از بین خواهد رفت و آن‌ها این رو می‌دانند.
@withyashar</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/withyashar/16576" target="_blank">📅 18:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16575">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ:من به دنبال تغییر رژیم در ایران نیستم و ترجیح می‌دهم به توافق برسیم زیرا نمی‌خواهم به ۹۱ میلیون نفر آسیبی برسد.
@withyashar</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/withyashar/16575" target="_blank">📅 17:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16574">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">کانال ۱۴اسرائیل: مأموران اطلاعاتی خارجی، مجتبی خامنه‌ای را در جریان مراسم تشییع امروز در نزدیکی میدان آزادی شناسایی کردند.
گزارش‌ها حاکی از آن است که وی با پنهان شدن در میان گروهی از افراد حاضر در جمعیت، تلاش کرد از ردیابی بگریزد.
@withyashar</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/16574" target="_blank">📅 17:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16573">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fx5Qb9zl5O4UgLEiUTLGlPe7aIhNfDDKTPlOFD1C7yut57YZChNF6MX6DlMQaKQIh88d57ArC1kjCRaxnaYVl3qB0CKXdr66WmYfuLqu0GNv8CcPX5kBshsX_kllVDtKm9oiszDQGXDjKJrHlvMfZ3r7uljsuLG8GWJ5xt9WrhAw46uqh5FBjFAqQ6JkcHCW3mFl3Y_Lznwj8hjhtiRC0BcoOBimLwGn5aaHZT4faHdp-NoI9KXU4FzVnTn7gCnUJhY2_7WNMqSoNnIhvkezld8ndB14UqzYg9dDV5EeAAT46w3huUqcggMDn_sPotLOyNEXogqj3cEalqFho0REcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن چاه وشی این استوری حقیرانه را منتشر کرد …
@withyashar</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/16573" target="_blank">📅 16:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16572">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مجری فاکس
:
چرا این حکومت هنوز توی ایران سرِ پاست؟
نتانیاهو : چون چند صد هزار نفر نیروی سرکوب داره که وسط روز آدم می‌کشن و شب هم مردم خودشون رو به قتل می‌رسونن
@withyashar</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/16572" target="_blank">📅 16:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16571">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a33dabae78.mp4?token=PejF73Gh-leUA9yCWIRchoilsE2hz02ZJ_br2vhTXyrYJMLGuJMRteYMwg-wtGr4zTEx3D03CiZZZ3FruIGH9BwSvgH4EWR8KoSCbvKOTrF8JdYN6oMLhFtLyZYkwEa6uMqJNZlnSqJk7btX5vaaB_oYDOBnte_ZiPlOp0N5vKSsak0HUPHdEopP7I9JXK0ulVtn1I4tpAS6RCx6UtJURYCUU-ducDO1ADbnuOzCw9RkrxDpulcr84-ISkPRTMzHdvG3StrNXLeuwhWIhMyNAIXHyW8WlSfAT5Q49QZqkwP3cxMs5XslZGnUaIqoX2SFXqGwARIcDGdUmlIYu2_Vf1MNchqjalHMBAFzrJGLbttP4v0A7WnpnHvSik2N2Z92eGiDm6xu3wbSdyNsroRUkMYVbqzd41bEHWBPQ8TPFZxpy1jNpYapfNsKs07HiJVZqEv5QntBah3CTctghQmJR6tSXTHV5Vwe7ar3Z2gnO3RrwjiSwArsytH6ufkvHv-2jEErBAXl7oQ8rSeNcBuBZBESAdhGMZ5wswgf0t7EiOkWkUCmygr8LB0UJKq9zXxiSYVwNCNbgZovOhXZnb9cRbKtU17CY7U0JFMt2xVAquHsAK2fKXJjGjfxCUxgem-TQMHKoFZC-cmu0GuWuAN4zuDZQLB0xhfnQskixepy6Uk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a33dabae78.mp4?token=PejF73Gh-leUA9yCWIRchoilsE2hz02ZJ_br2vhTXyrYJMLGuJMRteYMwg-wtGr4zTEx3D03CiZZZ3FruIGH9BwSvgH4EWR8KoSCbvKOTrF8JdYN6oMLhFtLyZYkwEa6uMqJNZlnSqJk7btX5vaaB_oYDOBnte_ZiPlOp0N5vKSsak0HUPHdEopP7I9JXK0ulVtn1I4tpAS6RCx6UtJURYCUU-ducDO1ADbnuOzCw9RkrxDpulcr84-ISkPRTMzHdvG3StrNXLeuwhWIhMyNAIXHyW8WlSfAT5Q49QZqkwP3cxMs5XslZGnUaIqoX2SFXqGwARIcDGdUmlIYu2_Vf1MNchqjalHMBAFzrJGLbttP4v0A7WnpnHvSik2N2Z92eGiDm6xu3wbSdyNsroRUkMYVbqzd41bEHWBPQ8TPFZxpy1jNpYapfNsKs07HiJVZqEv5QntBah3CTctghQmJR6tSXTHV5Vwe7ar3Z2gnO3RrwjiSwArsytH6ufkvHv-2jEErBAXl7oQ8rSeNcBuBZBESAdhGMZ5wswgf0t7EiOkWkUCmygr8LB0UJKq9zXxiSYVwNCNbgZovOhXZnb9cRbKtU17CY7U0JFMt2xVAquHsAK2fKXJjGjfxCUxgem-TQMHKoFZC-cmu0GuWuAN4zuDZQLB0xhfnQskixepy6Uk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‎نتانیاهو به فاکس : ایران حدود ۹۰ میلیون جمعیت داره
- به نظر من حدود ۸۰ درصد مردم از این حکومت خوششون نمیاد و مخالفشن
- ولی بازم چند میلیون نفر هستن که حکومت می‌تونه بیاره تو خیابون
- اون‌ها هم شعار "مرگ بر ترامپ" و البته "مرگ بر من" سر می‌دن
@withyashar</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/withyashar/16571" target="_blank">📅 16:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16570">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حماس: رئیس کمیته پیگیری امور دولتی استعفا کرد و این کمیته منحل شد. همچنین اختیارات این نهاد به «کمیته ملی اداره غزه» منتقل شده و تمامی مقدمات برای واگذاری مدیریت نوار غزه به پایان رسیده است. @withyashar
🚨</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/16570" target="_blank">📅 16:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16569">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwuoRGQ8XfDkuN1d18gpw_DS8HnHachji7PD10S8iPVpPPS1Wvp3ZI1AlU_7b0b8Qd0U2Cg8LwLJc_mtDt6MiiNpbiIJzmacEVtXj-q9OD1eWYVkRHlBul1BkYrzHPXqrilzrs7SMXn_nSg08WOmDx45_QkPw2xN25_AFtQGYHcbDVfbfTPa9lC8eVngXs3SQyH9D3vgGvQLTJWF55jAkO7PkinjRdwkZUh2pu-VykblquACTyhTP5khd2r-Xa85tvgOoft_alzEoIecwRKyHW-x5m5-DdTmWFAvYci28OYr1EFTOIloshI7PZWlqyhRYG5r43AelrEJmnTzfiLO_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور میم معروف این روزها در مراسم @withyashar</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/16569" target="_blank">📅 15:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16568">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">روزنامه الاخبار خبر داد: پرواز دومین هواپیمای ایرانی به صنعا در ساعات آینده
@withyashar</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/withyashar/16568" target="_blank">📅 14:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16567">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92eb08c456.mp4?token=pTz_kp5xZaN-RhHwj0ppJ1JwmyN34TbiFcQG99hsmzLLXPnNii3-bZIHtn2jW8sxaZzsJ-GrB_Ji7vyLcwRPMToYqK0kdaz6YqRRV0FebicOpKuXP2wUGykj5aA-qoOfQWtPFPcGcar-FLlPF3I1mP3k_F6mlHJGN3LLPSbYOL-caIU5YQ-pDq-ETHw-JiU7VANUnIli63wu3rLhLH2TzCSNwZVsEB3MCB8xHP3wNM7nWy0U5OuG7Gm2WB_N5QWOF5fOdkv9IgeNzSmvNs6uJ9baQoLu4-sf9tHp86ZS-XA2BJexJtoPkycVrdLRgaqdpdbq0d9n_AIY1hcQnxtwfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92eb08c456.mp4?token=pTz_kp5xZaN-RhHwj0ppJ1JwmyN34TbiFcQG99hsmzLLXPnNii3-bZIHtn2jW8sxaZzsJ-GrB_Ji7vyLcwRPMToYqK0kdaz6YqRRV0FebicOpKuXP2wUGykj5aA-qoOfQWtPFPcGcar-FLlPF3I1mP3k_F6mlHJGN3LLPSbYOL-caIU5YQ-pDq-ETHw-JiU7VANUnIli63wu3rLhLH2TzCSNwZVsEB3MCB8xHP3wNM7nWy0U5OuG7Gm2WB_N5QWOF5fOdkv9IgeNzSmvNs6uJ9baQoLu4-sf9tHp86ZS-XA2BJexJtoPkycVrdLRgaqdpdbq0d9n_AIY1hcQnxtwfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکیه در مسیر تبدیل شدن به جمهوری اسلامی تخت گاز پیش میرود
: ویدیو تعداد زیادی از مردم ترکیه در یک تجمع اعتراضی که هدف آن، وارد کردن یک ضربه به کیسه بوکس با تصویر نتانیاهو برای نشان همبستگی با ساکنان غزه  است
@withyashar</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/16567" target="_blank">📅 14:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16566">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گزارش هایی از حمله و درگیری بسیجی ها با قالیباف در میدان آزادی
@withyashar</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/withyashar/16566" target="_blank">📅 14:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16564">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hh48so0K2zxAF92UvjML3Lm_sbCCZX08Jh7k2inLmnga1p2Fz3Zln1sptFsnKPE5ofTDpSiI89mEAsKOJrnkcHnMjtwqeNXW2-UdLSjv_d5qLGw2pspAkb1ZLFZhRp3U-ouePyRsfmlKV219X-fyWc7dXZk9Q8pxXMbeHEA2XWxT4KygYNRIKBsBMHVSG-Zz3g5dosWmjHYwFM3-RwCQymUGHNIvo3-30u4r6jwKMJ1Uy1FTQIjG8RlopZ7XIPeNCsrU3Z-jsGUfPrQFO6wvK6QnbS1aPrvlDcp5TMg7MpHQW_qehFXUniP1FN5W_fcmkY_0Mik7ifya0mGoSD-LWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5278196c6e.mp4?token=ET8mNNLNjC9IENJS4XskEtpl3g4MFtivP3HPUza3qKW4BGpRMiIrFhMee3OU43_Jzrmym29Av0cpW80Zl6JL5ZfCPFQLUjIkA_hgSM5cQ_aoQWovBpoAJUQ7VDKuewHo7V8TWsTTfcW61AvO7-bDjMGNxbjDuoH7wsTr5NaM4C9uGcNOyaIaKO2SMfjn4Z9yIotuSs-99aO1aH-xiuTu0y6WdjUyh0JgQnRTD_rKG_L3QmUZmrCVIJOYWnkVkuRP1oBecZc1J3laks4DgxhFfa-4vi4ahu_WUzy9kWPIAji0UTlbnOBEyZ5H6lFRl0dt4x94HwuGZcLm9lEHgavOTnd4W-n4QfZSbYZMswOL2815O-C4N3dRBRa3gT-ZhfP6f_7rTGqDoo90IFYJxj_SDdMNefdvr0kUGXDfIjPN1uOmo7nJnsjLSXWe9wfq7FFpBySOYa-hlPMZXETBZs9Vi01Kf0R3s1KX4yq82f3XDjraLMgltVtz7R3kiNqssV82wdHd6vGZkOtLBa2qjlAK6ghtOp2QGiszzmmjEr3FiVUOUpeJF0MroI5n2Z7K_gMcin3bxcQI5yxMfONCtl5-c1V9Oa-dZl4WRovl2TQcIGzK3uiTBH0VL3SUgtr0cciQ7bQLMoVu12MMh7jXeUoFd-XFBrlC0KPD4oHle5a_al0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5278196c6e.mp4?token=ET8mNNLNjC9IENJS4XskEtpl3g4MFtivP3HPUza3qKW4BGpRMiIrFhMee3OU43_Jzrmym29Av0cpW80Zl6JL5ZfCPFQLUjIkA_hgSM5cQ_aoQWovBpoAJUQ7VDKuewHo7V8TWsTTfcW61AvO7-bDjMGNxbjDuoH7wsTr5NaM4C9uGcNOyaIaKO2SMfjn4Z9yIotuSs-99aO1aH-xiuTu0y6WdjUyh0JgQnRTD_rKG_L3QmUZmrCVIJOYWnkVkuRP1oBecZc1J3laks4DgxhFfa-4vi4ahu_WUzy9kWPIAji0UTlbnOBEyZ5H6lFRl0dt4x94HwuGZcLm9lEHgavOTnd4W-n4QfZSbYZMswOL2815O-C4N3dRBRa3gT-ZhfP6f_7rTGqDoo90IFYJxj_SDdMNefdvr0kUGXDfIjPN1uOmo7nJnsjLSXWe9wfq7FFpBySOYa-hlPMZXETBZs9Vi01Kf0R3s1KX4yq82f3XDjraLMgltVtz7R3kiNqssV82wdHd6vGZkOtLBa2qjlAK6ghtOp2QGiszzmmjEr3FiVUOUpeJF0MroI5n2Z7K_gMcin3bxcQI5yxMfONCtl5-c1V9Oa-dZl4WRovl2TQcIGzK3uiTBH0VL3SUgtr0cciQ7bQLMoVu12MMh7jXeUoFd-XFBrlC0KPD4oHle5a_al0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخی رسانه های رژیم از حضور جمعیت ۱۵ الی ۲۰ میلیونی در مراسم تشییع صحبت میکنن ولی اگه مراسم حج امسال در عربستان که فقط ۱ میلیون ۷۰۰ هزار نفر توش شرکت کرده بودن رو نگاه کنیم میبینم جمعیت چند میلیونی خیلی خیلی بیشتر تر از چیزیه که فکر میکنیم.
@withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/16564" target="_blank">📅 14:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16563">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پاکستان آبزرور : احتمالم میرود برگزاری دور سوم مذاکرات ایران و آمریکا در اسلام‌آباد در روزهای ۱۴ و ۱۵ ژوئیه (۲۴ و ۲۵ تیر) شروع شود
@withyashar</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/withyashar/16563" target="_blank">📅 14:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16562">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">توافق اوپک پلاس برای افزایش محدود تولید همزمان با بازگشت قیمت نفت به سطح قبل از جنگ
هفت کشور عضو ائتلاف اوپک پلاس توافق کردند تولید مجموع نفت خود را در ماه اوت به طور محدود و روزانه ۱۸۸ هزار بشکه افزایش دهند، همزمان که قیمت نفت خام به سطح پیش از جنگ ایران سقوط کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/16562" target="_blank">📅 14:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16561">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2U-riMSKWoIlRspRuPqV8_nuLGmqgOE3VoK_PUdX5IDaT2o7XPbMHtWfHTz5PMILZz10Swzdmf57_kU8OSLoeZwgqmZEmygzw4_BqPU-aSKgSxX4pHqs36MHcgifAjRYPMzLkD6eqMu95_N04Es-fUspf0-lfPTk0ADvL3RDL-oHQc1Iqpcj-8ewgGB245_ABNtdh9DEVS6mgzOCh9TWsYmTEpJ7I_9NqfuVGyyl7fXyI6bhSx8AKK-R_JkGqtAl3-rDYyrfp4B5HxLWID9L7JtZ94WTzFojENpAiNINs2qrmcXihP9G7arICo_fLb7nGDySFPvxQ83D9hGMj1KKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ: جمهوری اسلامی همچنان با مشکل فروش نفت روبه رو است
@withyashar
طبق این گزارش ایران ۵۸ میلیون بشکه نفت روی دریا دارد که ۹۰ درصدش رو هنوز نتوانسته بفروشد
از دلایل مهم این موضوع کاهش واردات چین است. از دیگر دلایل هند نفت ایران را یا روسیه جایگزین کرده است
اروپا هم در شرایط فعلی باتوجه به نگرانی از فعال شدن مجدد تحریم‌های نفتی از خرید نفت ایران خودداری می‌کند</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/16561" target="_blank">📅 13:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16560">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کره‌ جنوبی:ایران برای مراسم وداع با رهبرش از ما دعوت کرد ولی زمانی که میخواستیم هیئتی برای مراسم بفرستیم به ما پیام داد و دعوتشو پس گرفت و اعلام کرد حق حضور تو مراسمو نداریم
@withyashar</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/16560" target="_blank">📅 13:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16559">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpgapNDk4n1WjNxr1ivqpRwQBetlG9VzsWg6bkcrM9cgsX4nFZClwYx_FrW3tEKQvDPTPj3Cte2nHh4UJAfIQ5g_WOhQtL8iFkDvEPDQ9UkPw9bC79RXuR38CWZARTulLUsgWSffu6M-pUR0gJfn4Iw1odAqHbC5ajANhx4b5c4_4vf6H673ZukEq451iNhaB4gsSnE9RG-R0NH4KZp1h1t538dM0FyPIQZUxGQ5bie9jSi6l7OSA2xI6defsTV9Ls-SWGOrsTe7ICaWpKC56DEezK-5Zn_RdDiDv42Prh3h12UmJShGlULLHGA0qckCYMqVwsihySly8iFZp-wuLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور میم معروف این روزها در مراسم
@withyashar</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/withyashar/16559" target="_blank">📅 13:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16558">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دفتر رسانه‌ای دولتی غزه(تحت مدیریت و کنترل حماس): تمامی آمادگی‌ها و ترتیبات قانونی برای فرآیند تحویل و تسلیم سیستم دولتی، انجام شده است. @withyashar</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/withyashar/16558" target="_blank">📅 13:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16557">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دفتر رسانه‌ای دولتی غزه(تحت مدیریت و کنترل حماس): تمامی آمادگی‌ها و ترتیبات قانونی برای فرآیند تحویل و تسلیم سیستم دولتی، انجام شده است.
@withyashar</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/withyashar/16557" target="_blank">📅 13:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16556">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyyS4o7qKc4ylwLjniCk2y1CqoQQqNkap_SI-pdwCdqNyeAysYXRtT_dkEJyEq39KKbk0lO0WpKQMdmzTIKrlOhPYSRsoRtAMB_J2R5EFN8Ee1ivimSgXlFaKfPJ6Hmks4devIjN8jcEUTA-P-1MNxZUY9E32zclV6BdagikTliS20b0_ujpm6oYa7R6HYYTkm0IWB0bTC1nsWrXOYVl8azIuMh8lD8zrR77bJbOZT5w9fBTQAQLxxPnRdzT01rkDlcChVJn1wZeI4JvBKQIMAbkWi1S-7xiCbGN0cnWjxgUc7eLAY3jy3y_Mlc6NT9cT6ng1mb4sBywRZAkPOrP_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حمله پهپادی هدفمند اسرائیل در جنوب لبنان.
@withyashar</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/16556" target="_blank">📅 13:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16555">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59bbec746d.mp4?token=fCM8z1mxUVhkhL6YQf2K7J9OfrHA7cQk3l2TYEGhd-6wbF4bT-711AqSnItR5-OZrVl1GEVYChzSVdq1Y2KgClwzftRTp51eWSHgKvyLJpdOKAJo8EAJg3VgqoJJ_P0DMXarASSV25Yxbvy4O5Q-WWdE5Z1Xt-5EycyjCDYm9FjPhJeKDDtrjZ1JCy7CYV_8-tksMHXaqn-px10jzDAc8lhkhQXQJTTstyA4cic4jcYmaulbim0Ev2a1ytO95h4h9EMzRBSjtfmkSrxhBXpP_5htkV7XAZVcv-ejDB1cE_R1geDYOVhA6Lrqot4GJUwHXIoaKTVGqoHbnpv6NOHFPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59bbec746d.mp4?token=fCM8z1mxUVhkhL6YQf2K7J9OfrHA7cQk3l2TYEGhd-6wbF4bT-711AqSnItR5-OZrVl1GEVYChzSVdq1Y2KgClwzftRTp51eWSHgKvyLJpdOKAJo8EAJg3VgqoJJ_P0DMXarASSV25Yxbvy4O5Q-WWdE5Z1Xt-5EycyjCDYm9FjPhJeKDDtrjZ1JCy7CYV_8-tksMHXaqn-px10jzDAc8lhkhQXQJTTstyA4cic4jcYmaulbim0Ev2a1ytO95h4h9EMzRBSjtfmkSrxhBXpP_5htkV7XAZVcv-ejDB1cE_R1geDYOVhA6Lrqot4GJUwHXIoaKTVGqoHbnpv6NOHFPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویر ماهواره‌ای انبار مهمات پایگاه هشتم شکاری اصفهان که توسط BBC منتشر شده است، انهدام کامل ۴۶ انبار مهمات و سازه این پایگاه را نشان می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/withyashar/16555" target="_blank">📅 13:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16554">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خبرگزاری مهر: پزشکیان، قالیباف و فرزند رهبر انقلاب فردا در مراسم تشییع عراق شرکت می‌کنند
@withyashar</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/16554" target="_blank">📅 13:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16553">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کاتز وزیر جنگ اسرائیل:
خامنه‌ای که مراسم تشییع جنازه‌اش اکنون درحال برگزاری است توسط ما کشته شده زیرا او طرحی را با هدف نابودی اسرائیل آغاز و رهبری کرده ، اگر رهبر جدید هم از عاقبت پدر خود عبرت نگیرد به سرنوشت آن دچار خواهد شد
﻿﻿﻿﻿
@withyashar</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/withyashar/16553" target="_blank">📅 13:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16552">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0de6a03c0.mp4?token=mlPjf8VlEV7wxPpuxA5aZw9RA7CJHjrXBmr_CdcQQoDWInqjYEQq_mPL9t_1VEevjLRceIHvR9mCabbYCLGrkU8qpToEskv7jpESnV7Owrly-ZwTR0gLzFtYziRM_Vbnj0V9S-OyYrxpUEgz5b_Ejy_lb-GjipvfZ01K1BjyplNKXePV1CB8crNIKAa3Rygox9ehuG9qja0GnLtK1bFac4EsajzP5Ve-QElZv7RV0uNBwwBrhbAsamQsp5aa5gH_U32jSJ6yg92EiqzlnfRriv2LGtcCvFFA7Htycmw-5caXmbGBel7cWzzCdvw0r0O6L55dSAEA86YKlLAL52NnRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0de6a03c0.mp4?token=mlPjf8VlEV7wxPpuxA5aZw9RA7CJHjrXBmr_CdcQQoDWInqjYEQq_mPL9t_1VEevjLRceIHvR9mCabbYCLGrkU8qpToEskv7jpESnV7Owrly-ZwTR0gLzFtYziRM_Vbnj0V9S-OyYrxpUEgz5b_Ejy_lb-GjipvfZ01K1BjyplNKXePV1CB8crNIKAa3Rygox9ehuG9qja0GnLtK1bFac4EsajzP5Ve-QElZv7RV0uNBwwBrhbAsamQsp5aa5gH_U32jSJ6yg92EiqzlnfRriv2LGtcCvFFA7Htycmw-5caXmbGBel7cWzzCdvw0r0O6L55dSAEA86YKlLAL52NnRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با شما : یاشار جان سلام امروز تو مصلی بعد از پایان نماز ، بلندگو ورود مجتبی رو اعلام کرد اما بلافاصله هم صدای مجری قطع شد و بلافاصله آنتن ها برای مدتی قطع شد... @withyashar</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/16552" target="_blank">📅 12:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16551">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jah-1cPQMBAmvA5PfxhZS7K8dOke__8MyYDsW017rUdRzDsi1eHz0NgnX-23RWohpLmPAMAQXCdodYMwQ0aG-McQ7G21bENwtWHNf2Bcw2jGxL7z9hBbcdaDJRyN6JqpKA7fHX9kwvv0lVqvTF3HxEfP3UXUnEn28XTBvKVFg5PXDGp9QPWxRQJdYGzMBliQJue9C_ZjE7vkpi47vy1Qji2UM2O9pfiMt5pLPtmUGkwnYrUPZ0dnhGdbJPotqM0PPuYC_dKxI86-6Y9Ono-Jwo1zmG23YE8EEJH_XvU37yV-lxNDDd65OxxVfEmKrFZxj1qhP-_cacelus40LRIVVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به حملات خود در جنوب لبنان ادامه می‌دهد.
انفجاری در پی فعالیت ارتش اسرائیل در منطقه بنت جبیل رخ داده است.
@withyashar</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/16551" target="_blank">📅 12:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16550">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/061472f621.mp4?token=A7-yu_uWrDr2EX2O5RK1okboDpGdU4gH0MgHgPzLkhL3YW_zx1LgYWbVn2Laqyvc6GpZxFGesvCoZRo3ROP-IEc6Dn-_aD80PwY9lF_7K_AJoQ7xkM-8qbh1H3EScg41sKsoVZ8aokE0e5t55_rFyTQAOHfL8k1fAIObP9RJM4UtJuKi4DgOlN8WoLSlCzvV9XCrVqiJskjWGoS9Bl7AJQC0-XqPkdOGk40hWy4wmwnGFs7vWGaQmffyTXtMl-8NU6CrstxmGpAqCu0rgKFtF-DNwTyRa91lMJEiKM1mJ7UySDEMyYarReDVMltk6Ij4BYIwYHuuwo741yZeGGt6ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/061472f621.mp4?token=A7-yu_uWrDr2EX2O5RK1okboDpGdU4gH0MgHgPzLkhL3YW_zx1LgYWbVn2Laqyvc6GpZxFGesvCoZRo3ROP-IEc6Dn-_aD80PwY9lF_7K_AJoQ7xkM-8qbh1H3EScg41sKsoVZ8aokE0e5t55_rFyTQAOHfL8k1fAIObP9RJM4UtJuKi4DgOlN8WoLSlCzvV9XCrVqiJskjWGoS9Bl7AJQC0-XqPkdOGk40hWy4wmwnGFs7vWGaQmffyTXtMl-8NU6CrstxmGpAqCu0rgKFtF-DNwTyRa91lMJEiKM1mJ7UySDEMyYarReDVMltk6Ij4BYIwYHuuwo741yZeGGt6ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور دایناسور جنتی
@withyashar
انگار دارن به ۱۸ چرخ فرمون میدن
😂</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/16550" target="_blank">📅 12:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16549">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ab53f55a.mp4?token=na5zg8u8kkHa7NEQBy1prPt7vgcJ0Z9WJyxa5gSLhBzikfFjBVoQspiUf2eq-xkPoAphRYQ2yD8CJAenAitZifNLqT2LszQUXR0G69UmyNB9-awOaEukW4i5upGW0J9YKpGyisgrQm8FWlyesphK4hX6Iv430rdjOgMimOr_Yvm7sYJXNldfgGZ6L2dMV1qIadQSDyE2YwrUdIXcNEM15WJBEH8yMn4mWVqI-84ORRgnLOGdIw4B5OhEMDDVbnf1_d_3oOmy2K15W491x7mCoHcXACd96kqzKjjeGEer3j9H9EqFdPQ_rIusW66IbXq6oH-UWiAANexSaAi3C-yWaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ab53f55a.mp4?token=na5zg8u8kkHa7NEQBy1prPt7vgcJ0Z9WJyxa5gSLhBzikfFjBVoQspiUf2eq-xkPoAphRYQ2yD8CJAenAitZifNLqT2LszQUXR0G69UmyNB9-awOaEukW4i5upGW0J9YKpGyisgrQm8FWlyesphK4hX6Iv430rdjOgMimOr_Yvm7sYJXNldfgGZ6L2dMV1qIadQSDyE2YwrUdIXcNEM15WJBEH8yMn4mWVqI-84ORRgnLOGdIw4B5OhEMDDVbnf1_d_3oOmy2K15W491x7mCoHcXACd96kqzKjjeGEer3j9H9EqFdPQ_rIusW66IbXq6oH-UWiAANexSaAi3C-yWaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین ویدیو از احمدی نژاد
@withyashar
یاشار: من چیکار کنم کاپشن پوشیده ! روانی ها
🤦🏻‍♂️
😂</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/16549" target="_blank">📅 11:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16548">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c911eae2a5.mp4?token=TVCsUOpAhhpInQaVfZZ_BmU3860xf9JFNSN6_3naEQuL12fxTHsk_pzt6K4iwRJ8VPjvNREcCSFXSabXh6TRlluaKyp1tGBfRcEpw4GRhsGfe8GLVLy3FlQqEj7bpSW19RhFw05U_McZHAoZ7bCzd9h_Dh15j6O3Px3Z9d_Qr6FBDDq0-Fh8dPxtLTPWpU8mx835dHZU0B51a3qtaoiHhQyHa4ZKpifBAV5bsSfEREwjIFFr_RiUj_KJAkXoLmWmBIpJPbuxdbDZSt3WQZEKu5Z0uaxKx8y3mZbL2OyRxtL9emQ3nCo2btumyDFl673m6HWzuZQHHbNy4NyMlrGWwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c911eae2a5.mp4?token=TVCsUOpAhhpInQaVfZZ_BmU3860xf9JFNSN6_3naEQuL12fxTHsk_pzt6K4iwRJ8VPjvNREcCSFXSabXh6TRlluaKyp1tGBfRcEpw4GRhsGfe8GLVLy3FlQqEj7bpSW19RhFw05U_McZHAoZ7bCzd9h_Dh15j6O3Px3Z9d_Qr6FBDDq0-Fh8dPxtLTPWpU8mx835dHZU0B51a3qtaoiHhQyHa4ZKpifBAV5bsSfEREwjIFFr_RiUj_KJAkXoLmWmBIpJPbuxdbDZSt3WQZEKu5Z0uaxKx8y3mZbL2OyRxtL9emQ3nCo2btumyDFl673m6HWzuZQHHbNy4NyMlrGWwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودرو ضریحی عظما
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/16548" target="_blank">📅 11:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16547">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddbc5efdc9.mp4?token=ZA9ajhrEox7bZEb4rCnp2cM0YeT73gKspDq9nfmhNZt98g7lYMOTpID30gbEnvtrNjDgwayPz7CmaQI9DI-8YYZwuOpdqDLfsRbTHNbisQuh2v2S2K9QHRPTNYmPRnBo6upVI9o7wWLrVz0ABbp4tIvxy1rbFgvyXLgNOH8BA-Ij9_6dUYH6mskFHNsN_YOZE3QzRgIYvWeYgW240fthE-_FGIgz6HQmqkCSGALRwTtDiPwARPkj-HSKJEEU_djEfJcUn2M8d3pO9F9pWH9av53BVfxwyF_JNCB8uqaBp4un-pt15F8NMH1HwDTCwnhg0h9-E5EQ_EH8znP2anbo9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddbc5efdc9.mp4?token=ZA9ajhrEox7bZEb4rCnp2cM0YeT73gKspDq9nfmhNZt98g7lYMOTpID30gbEnvtrNjDgwayPz7CmaQI9DI-8YYZwuOpdqDLfsRbTHNbisQuh2v2S2K9QHRPTNYmPRnBo6upVI9o7wWLrVz0ABbp4tIvxy1rbFgvyXLgNOH8BA-Ij9_6dUYH6mskFHNsN_YOZE3QzRgIYvWeYgW240fthE-_FGIgz6HQmqkCSGALRwTtDiPwARPkj-HSKJEEU_djEfJcUn2M8d3pO9F9pWH9av53BVfxwyF_JNCB8uqaBp4un-pt15F8NMH1HwDTCwnhg0h9-E5EQ_EH8znP2anbo9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ورود وحیدی‌ با موتور
😂
@withyashar</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/16547" target="_blank">📅 11:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16546">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">الاخبار لبنان: یمن در حال بررسی بستن تنگه باب‌المندب به روی کشتی‌های سعودی جهت فشار به این کشور است
@withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/16546" target="_blank">📅 10:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16545">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugdjepxMUa5v2BdW8Q9CA4OUqr4gawMHTRulA_e2UdlK1bL6FL4xRq9tSpC3a3jHVSCi2ZjQ14K-BCLlL2H5rOewhGu3t5pNIQMSVikvJUzFlqQ15GjIPpTy1WwogfbeNTgXGXWfhf0Fea-RaAA0hai92_VyHR4GuDsuOQaD5A4luQSnOaPY3kOCoNvLQNxBwY8D2gWpDEl_1hW2xBy9w4UFN-yfLnTSgLdiM8YZMn_pw3gpx8AQc_wfcjmREFP3R5R7k3cMbhodke9vCKt_-EzkyEuaJizVa9I1v0e2QZPxilbi5ptcD-NJAf_XjSEFi4mEgGD1abFy0hDiQJ8D1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از انتشار گزارش‌هایی مبنی بر اینکه اسرائیل و آمریکا قصد داشتند او را در طول جنگ، به قدرت اول ایران برسانند : محمود احمدی‌نژاد، رئیس‌جمهور سابق ایران، در مراسم تشییع جنازه علی خامنه‌ای شرکت کرد.
@withyashar</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/16545" target="_blank">📅 10:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16543">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZbRt2l4wrv16uBvYpA7lsz-yhU4k36b7GfIacvb52HuDQZmTQ-2qudGtIpjoumLkTrtG5m3BWo0G5Vxy792Oa_Kkb1W0zzw0KhfmYbIvURHgL5o-FZWIT0GN32GVjd4cYkMdvvd2lJ-Ys3IoVcW4vra3NI2x6_G8Zyp17ajUodix_j0tNdPzBN7D54gdIE97FWJ80qKQQ0wkUSQkXNpHh3-eXcqB5sSS8bWdnz44ugje_sIFWO40Q-ejtZRbh3eK4w0m9TovG9ZQbAshOATF5WLuW_XB8bUNd3ooYhyyZ3Y83tO8nH406gPRuQyGiXxrnKrbzzxv0G5UAIpnPEwpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BqhQu3CUW8C0iUQLu-skWjyLHdNKg7coRdwpl9aRyA13pXhOcbabp9aUkGBOSZJoZak07JX2tun10LTYHx1XT38O1dwupS5NvUClimDZEm4RiFdRZfhnvczJN2s-dBMPiJNY5v3VZRmflCHFNC0_FcE8P5qsNEboPA_5XgrE9cRW81bNsiEx46xHhgCijCZ2csXc94v3ZoOiAEGoPCNix0fd3LVrUpYcfi3hOinUIHYNzp5krympWnUBjbVOGgbEvMlzSa2WupYq6c1MgChjYK5wheV9b1vCG9qAE0yY3R_VtOkMWO1aKj1Dju0HBUrclSGBEDePFR_U9UFQgNHlqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نمایش قدرت در برابر اردوغان: ارتش اسرائیل در تمرین مشترک با ارتش یونان.
در طول این تمرین، هواپیمای تانکر اسرائیلی در حال سوخت‌رسانی به هواپیمای F16 یونانی بر فراز دریای اژه فیلم‌برداری شد. ارتش اسرائیل گفت : "این همکاری بخشی از یک برنامه استراتژیک گسترده است، در دوره‌ای که ترکیه تلاش می‌کند قدرت بازدارندگی خود را تقویت کند."
@withyashar</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/16543" target="_blank">📅 10:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16542">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">این آخرین تلاشمه …
@withyashar
⚠️
یاشار : عرزشی ها اومدن ریکشن فیک زدن رو این پست ، اتفاقاً این کار ارزش این ویدیو رو بیشتر می‌کنه و نشون میده چقدر سوختن</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/withyashar/16542" target="_blank">📅 02:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16541">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKCZdXKK69EmQGq2B9kqLfpsX5pPrxG8Up3r3SnX8f1BWxU1R2egLiOjsrVEcTmSCwfdcvSxmMTcAH6lCsO8-_sq1AfKa0p4RFLKWrcliNPu9sqT6AmxSsUXVPeGlHnaesbHCxHlifY-VpjGap1IjUXYFytLFVkcq2u50Kgr8yd5iciALslvR5gpfvfR62tXu9XlTSVshUOJmYCKsX4PmPf9Y6qDctWWl02KZVNRaylM2QGN_LaSVtVLzmxO1k7G792s1b3fmzW0maL5rhPxMUzS2ccmWegh774yCULQ-EZEg_E71LlIZfQnFVfHqlOop86_nDuIdcogxNeiJyznMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوگواری شبانه روزی نیرو هوایی آمریکا در‌ تکیه تنگه هرمز در غم عظما
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16541" target="_blank">📅 01:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16540">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaFu5C42_B9MGfAs_47l5rWPjkRStRrPaVWbs7gPM_H4t0k003d4bplV4D7nHCpFMIFDv_zF4ykpqBE7mx54NGdCwb361L2432nqzgxGOVs3B6hNNF-xLPNZcwbrdfRN-Go2mztaFaWcPWw2e_BQeM5RMSRx8zl92WmHpo2pCdQ66_1LuLugrunlLQnZ3MY-a-Yc0r-ypsz0zLYnl640Utt3GM19_tl6gyyk5J3MR3xBKOWVOYxuMBgVP-6raKKf_Ick2tn02OIdlMa-q0ePVe-DzWsb4JTRw3cnn4pU6Jg5wlY_2dPOMDQQtjhIjoxRUB5Gd7IksExNfdcT0EvKvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قفلی جدید
😁
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16540" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16538">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گزارش ها از آغاز درگیری شدید میان حوثی ها و ارتش یمن تحت حمایت عربستان در جنوب یمن،ده ها کشته از هر دو طرف تا کنون مخابره شده است.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16538" target="_blank">📅 01:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16537">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOhtU5sWRW9JcUp7tMVrnfpfTtI2Svs6X5wpN1QwY5PNCBCBtSFnbllBOBP7KnjBkN0DUO7UeORKXMczZm3on_wmU5kNGqO9KjOPyiYkaA5BYjkASIJcFXPth0m1YUtOm2naM9vGzrN75JLJOcN693Syx1r-Vp4qN1cdlBQ3PkKEm1YV-kDVdqOBvXNsgnUK3mjDGY3ZWfTH3M1BEhROk8Wh9Ed2jmy3FtZDetKopv_eEZcqxzy0693leBdy38vbuMIr8d0sl6U-24jXXK8K6xoFZizeFmTcwQJsX4MjQjmIy_xHkUJPRB1NZkFAa-yIFPrHlTNt1mxkNFRoMEkvXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ پستی از خانواده خودش در سال ۱۹۱۵ (۱۲۹۴) منتشر کرد و نوشت : پدرم، پدربزرگ و مادربزرگم، عمو و عمه‌ام!
@withyashar
یاشار : میخواد بگه ما از قدیم پولدار و با اصل و نسب هستیم</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/16537" target="_blank">📅 00:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16536">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtMouxZW4_XryvRKM8cCrqQ4nUgT6WR9wrtLeTkm_HIukSJuqQjC3OMOKFpfLm5vcvto2yHibpwYSWEvc50EatLFNWTx9KTuKTzp4OS-7LMI7N0YL7VNL4v_OAL7selkPSBF9z3baJLJpjsFVyXsAqz7wm3S2Dz-ye0aORFSITFnGsiP-yF2IwMDHkdKVam0YynYec31aeX6xzJLfU4-JqNig6LTBEGFLJkc4tnHTJBKTkIgQtRCV4nPlYiU7ZesRisl-bn7oyP2RQvlw6u7kGPrFUd2FTZZjuLybzlUSh6UQBpMpQqj05XLUDq5RWs4uH_QtjnIIEPnA4K1F80tMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهیه غذای «هانی» اسپانسر تشیع موشلی , دسر هم حتما با «میهن» بوده!
@withyashar</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/16536" target="_blank">📅 00:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16535">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDuE6yuIcPG2P1WvtrzrkoCzvaIihNwYPvs34cMuvz3iFHzkIvkH_o9k6LHB1YB80199kKk3GfZFSYiNftqNP3VlJYLKHYx8NJkapIKMPUqpBKBt7rNsv5evLGWQPs4D2dj5bf1j6t1fIKBDzl5g78piRBpBzKTRVsacpD0C_GFfDJyaLOHgJxVVT5RXpRcOHXvW2PW-6o6jp2TsMRYtgFKMKRowPyOaSB2r2t_acPzXDFhYNyr2Ft8v6FBHyD9vUlIwAzepvjjXexxUz1rV1LCdtx3zbLeyAxr53sKES0DN6pGOaplDeb9pWx01h36wN63FuewNVUUqCCTTWvC-Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پستانداران انقلاب اسلامی
وضعیت بدنی نیروهای محافظتی امروز در مصلای تهران
@withyashar</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/16535" target="_blank">📅 00:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16534">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">در پی گزارش‌های منتشر شده از عربستان سعودی، منابعی در نوار غزه که از جزئیات ماجرا اطلاع دارند، به کانال۱۲ تأیید می‌کنند: حماس احتمالاً فردا اعلام خواهد کرد که کمیته‌های اضطراری دولتی منحل شده و یک جانشین برای مدیریت این کمیته منصوب خواهد شد. این موضوع تا زمانی که کمیته متخصصان وارد نوار غزه شود و اختیارات مربوط به اداره ادارات دولتی را به دست گیرد، ادامه خواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/16534" target="_blank">📅 00:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16533">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خاستگاری‌جنجالی نوک برج امپایر استیت دو شهروند روس پس از بالا رفتن از نوک آسمان‌خراش «امپایر استیت» در نیویورک، در همان محل مراسم خواستگاری برگزار کردند، اما پس از پایین آمدن از ساختمان توسط پلیس دستگیر شدند @withyashar</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/16533" target="_blank">📅 00:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16532">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnwA0ECGVZlYnejbhNlQj3wWVPIs13RgkBCX-dTmoDBHhd1aF79r0Gef_pqV9d5M3t6CrCFJzD_RcWU89mfo2v3cAwDYFEjvgkHqws78EAez9-281hW8x3yO0sY9ZMBPicwLAmYvSms-lWxVlF0YvfDxCkliMAU7AuDzaLgleXadOZ818M0XWvJjK-x916Bi0LL1swy_7X6a2tJ5m0p6b22mZJ_TEM10qJcgP76a6LSJ6GN8KycOvPKU-h5LGBVXR5GMe_kqGVJPXDh4pHTkqMbM9OEyW2IgSo-ACvhGqbQOOtvmOUw4OdIIpf5GFhxMs5nbBKD40XoTN7HcTl_7uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از حدود ۲۴ تا ۳۳ هزار سال از انقراض آخرین نئاندرتال‌‌هایی که در منطقهٔ جبل الطارق دوام آوردند ، امروز یک نمونه در
تشیع جنازهٔ آقای موش علی دیده شد.
@withyashar</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/16532" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16531">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_ZmnPWvxwcOYlbXRmZ_YfU8_mGFPdMeUwddu3SEAbCKVEljCBrhyh9OobzcU3-TmqfGBWEmu09bkV-VHv5vM8tE76ykBN4lewBpmLBzByj0QZT-Yt6k-fg1zKFDqmdObye9a-hr0Gwpp9Yj4KQotEAnzP-Pnu7yfB5eT5j92PBXg2AYcxk0_24esr2X8lA3mRWxLyrks8O9PgX33HYdwY-NaM9vlfp4GZjqCEmU7uU2y0eSg0eevzBb-VbyD1YD5roqh5ellXHx09dQGh-zLDYY80HlnlhNA6Lc8GzLICxBaqgrKaueTHfLJsssi2PWsdpK5pOKHrfYY-ibWKywPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/16531" target="_blank">📅 23:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16529">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzabuuEVWXZImUx3IF-DNGaNmv-efZWfdPSokIC-bGh7v3QJp4HAJO3geqgHHzLGDYLcJUPpMvPhVt_ipkrgCNJa0u_h5l414wgyq2q-4TJR65ETOoHJ8cmFlFJU-q3k-Kd5GFzfV-6asMm0UMNEQo1C5JXO7Hwqyab4NSKjGsEFlR6Ps0asLNANUyWst_vKfmt2Ym3gBpb7daCxrAjATzfKNYFuQU8vGX9PMG4YuCifm7SsYNx2zAmDX2buH-daMQY8V2bHTrjzrbgR2TZDpVE3dGfGF-pBDsOjY231N0W1kUfzrs6Hc2umnjfwkTM-VLQDh38U-EwrM3mFY16AeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏شرکت هواپیمایی سعودی اعلام کرد که هواپیماهای بوئینگ 777-200ER از رده خارج شده خود را مستقیماً به ایران نفروخته است.
‏این شرکت در بیانیه‌ای توضیح داده که این هواپیماها در تاریخ ٧ ژوئن ٢٠٢٣ به شرکتی واسطه خارج از عربستان سعودی فروخته شده‌اند. پس از اتمام این معامله این شرکت دیگر هیچ ارتباط عملیاتی یا تجاری با این هواپیماها ندارد و برایشان اهمیتی هم ندارد آن واسطه این هواپیماهارا به که فروخته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/16529" target="_blank">📅 23:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16528">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5TNvuBsErjIeQfLW1CtIJI861lyzk7OWCaWxk6yVWSRS-215wUkPOATBYNI3fRumx1psGuUPZvs0LgmANRx4QXJFEZ6klRQe2OSCxXWZLYKLafPlUEN2rNLZP9jwsaA3N5lPh4NASQoEL50o8XDK6myigEvv5l18NvbjuitxLYkQK2_Ga4CzJZAFQ9A8TjQh2OggdNtMHC_d6On_YojY1OIaWvbNIjpvzZ53heQI55OEUY90B39muG_rMYAhmI6k8JfWix1CmD62vtZx9SZGGp82qEYs1bB5S8OUZuRZ_QE3lN4H851_GS5QerKyknreT3-dPMWHK_YI7NAXB_vsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ته مانده جمهوری اسلامی …
🗑️
@withyashar</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/16528" target="_blank">📅 23:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16527">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">صابرین نیوز: محمود احمدی‌نژاد، حسن روحانی، محمد خاتمی، محمدجواد ظریف و اسحاق جهانگیری در مراسم وداع رهبر شهید انقلاب شرکت نکردن
@withyashar</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/16527" target="_blank">📅 23:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16526">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کریستیانو رونالدو به گمانه‌زنی‌ها پیرامون آینده‌اش با تیم ملی پرتغال پایان داد و به طور واضح اعلام کرد که جام جهانی ۲۰۲۶ آخرین جام جهانی او خواهد بود. این بازیکن ۴۱ ساله فوتبال در کنفرانس مطبوعاتی پیش از این مسابقات گفت که قصد شرکت در جام جهانی بعدی را ندارد، اما تأکید کرد که هنوز قصد بازنشستگی از فوتبال را ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/16526" target="_blank">📅 22:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16525">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یک مقام ارشد کاخ سفید گفت که دونالد ترامپ، رئیس جمهور آمریکا، در دیدارهای خود با رهبران در اجلاس ناتو در ترکیه، موضوع حفاظت از ترافیک دریایی در تنگه هرمز را مطرح خواهد کرد و خاطرنشان کرد که متحدان پیش از این تمایل خود را برای شرکت در این تلاش ابراز کرده‌اند. با این حال، وی گفت که بسیاری از آنها کشتی‌ها یا منابع لازم برای مشارکت در یک تلاش دریایی قابل توجه را ندارند. وی افزود که واشنگتن همچنان به متحدان خود فشار می‌آورد تا قابلیت‌های خود را تقویت کرده و در دفاع از خود سرمایه‌گذاری بیشتری کنند.
@withyashar</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/16525" target="_blank">📅 22:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16524">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⚠️
ادمین کانال تلگرامی به نام کیان ملی در تاریخ ۵ خرداد(۲۶ می) دستگیر شد و  از تاریخ ۱۷ خرداد(۷ ژوئن) این چنل توسط افراد اطلاعات سپاه کنترل میشود و مطالبی ضد انقلاب شیر و خورشید منتشر میکند. به هیچ وجه به این چنل دایرکتی نفرستید و از آن خارج شوید.
⚠️
@withyashar</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/16524" target="_blank">📅 21:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16523">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62ca634efc.mp4?token=asA9Hcjv1bqTn2O5efAim9nUAz69Nnh--TVwc_3mrRTFio-TMx16qwerfXIYuG1j77JnoD-lg5VsZImARTjl4WtLUQTXcWvm5CftycRebSP0qKo0LtjMZq-kiPDfn5PP6WiiL5HvtcfObpn8MIMgPoPOa-Fr3v5VndHjHVanuBspmpR3MEQFw_ZfZeniku6wFEi3gbLdACLy3wNOJgjouauRALrCHezDw1fEHg9WGroJKoNGVKBIoB_dnLYnR8Pu76fjS5nxNS6RFTPb0QrxXiQXbFB4Y0g2kHBTMX56sBN2HnmM7pIomEYJWrYwVxwjqOfl9T5LZ088ByI9EN3uJihIS4P4UYcmi_Yh5V8YAQFy_jQVMld0_ZpU3fIlweRvvc87NwG6HwN2LkSbTYJmHEkH5glCMDNhybmwMySA0q9g8i5ipo6oV2oOoaAvRqj51jLgaT4aHiJ9b2LhWkQDpbtU6fpqrygYs5yzptlEY_T-aeunv5F3_au7uxQKcxerNKK_om3dczFZL3qQqiBlqntKT54y01HVWqWrq0Gd-DltFG3lvm7ENtUMstz9xQcfPBcsCArSb7c-latVWPWGeS-imY-ccJOmJp2LGOOTl0yzftY3CSexvbUZDyTSyRVwuowLLhT55QFOe0T-KvHln_ntnWuXdEYpMa35OIcfkmI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62ca634efc.mp4?token=asA9Hcjv1bqTn2O5efAim9nUAz69Nnh--TVwc_3mrRTFio-TMx16qwerfXIYuG1j77JnoD-lg5VsZImARTjl4WtLUQTXcWvm5CftycRebSP0qKo0LtjMZq-kiPDfn5PP6WiiL5HvtcfObpn8MIMgPoPOa-Fr3v5VndHjHVanuBspmpR3MEQFw_ZfZeniku6wFEi3gbLdACLy3wNOJgjouauRALrCHezDw1fEHg9WGroJKoNGVKBIoB_dnLYnR8Pu76fjS5nxNS6RFTPb0QrxXiQXbFB4Y0g2kHBTMX56sBN2HnmM7pIomEYJWrYwVxwjqOfl9T5LZ088ByI9EN3uJihIS4P4UYcmi_Yh5V8YAQFy_jQVMld0_ZpU3fIlweRvvc87NwG6HwN2LkSbTYJmHEkH5glCMDNhybmwMySA0q9g8i5ipo6oV2oOoaAvRqj51jLgaT4aHiJ9b2LhWkQDpbtU6fpqrygYs5yzptlEY_T-aeunv5F3_au7uxQKcxerNKK_om3dczFZL3qQqiBlqntKT54y01HVWqWrq0Gd-DltFG3lvm7ENtUMstz9xQcfPBcsCArSb7c-latVWPWGeS-imY-ccJOmJp2LGOOTl0yzftY3CSexvbUZDyTSyRVwuowLLhT55QFOe0T-KvHln_ntnWuXdEYpMa35OIcfkmI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما : انتقام رهبر شهیدمون رو توی بازی ماینکرفت از آمریکا و اسرائیل بگیرین و فیلم و عکساشو برامون بفرستین @withyashar
😂</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/16523" target="_blank">📅 21:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16521">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⚠️
ادمین کانال تلگرامی به نام
کیان ملی
در تاریخ ۵ خرداد(۲۶ می) دستگیر شد و  از تاریخ ۱۷ خرداد(۷ ژوئن) این چنل توسط افراد اطلاعات سپاه کنترل میشود و مطالبی ضد انقلاب شیر و خورشید منتشر میکند. به هیچ وجه به این چنل دایرکتی نفرستید و از آن خارج شوید.
⚠️
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16521" target="_blank">📅 21:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16520">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ در تروث : از فیفا به خاطر انجام کار درست و لغو یک بی‌عدالتی بزرگ متشکرم! @withyadhar</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/16520" target="_blank">📅 20:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16519">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1NF1A9Gs84UU2kPXwyeqkBRXOFWL0fAi_Z53TMkk0F-bqWz3grAQ4pJ5XVzuOVCzSt1I_XT9FhhR8pk-Ckv3jPHxphCy2AfUu1uoGfX6_JNvaWAOU1yObFxqMhVxv-EukLaBQmsljiGHNrL_T5BA1YH5tlTuKH34VPFsq5bRRkfkBrXqv7JDlBCqXf2ntiibta_qkZlW6vdSuD-w0pgcSrx50XAR8nC51iSy81lSbCS4U8ex_HCCC094Q_J0YMzMVO5DZa2LmJFjCZZ90D-Yq4VDdbczF7S62vBSsaUTjS2_sqWDmePkCoYG9IWsWdx84DoWcDHQVVj8uaA5nvA2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : از فیفا به خاطر انجام کار درست و لغو یک بی‌عدالتی بزرگ متشکرم!
@withyadhar</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/16519" target="_blank">📅 20:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16518">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">کاخ سفید : ترامپ قراره تو اجلاس ناتو با جولانی دیداری داشته باشه
@withyashar</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/16518" target="_blank">📅 20:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16517">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گزارشهایی از مشاهده یک شیع‌ ناشناس  نورانی با سرعت بالا در‌ آسمان تهران
@withyashar</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/16517" target="_blank">📅 20:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16516">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-Yasir6WHezhsekYlK_xZb4fSN3fkgYmF_ytB4MC4DewtKOih61anahFhMoiVGLfk5U9Bd0kKB7spMSrEMm6LwNumXDwKEHHxagAhe_i5JKImkvfRcajdc6PT1mfTcytj--d1O20zDZdOhn16uOS2RrWTR6OQZ3J1YdZzVl-4ZuP5Ue3j4HtQl0hXMplIrgSI0fbm6gg4NL1yrxpkT6MFbf4IuWmqpdPgw8YnIcVlwltK0n4v-sJ0UmRg5xaEytm1aIvGquzSwH4WzrWTJO2J7vBnkfZNO6P0eRxWuUqS3UVx3iOrMH9l0WpLIR01tK0iZkyhO1FzxXvfhXFigCOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیما : انتقام رهبر شهیدمون رو
توی بازی ماینکرفت
از آمریکا و اسرائیل بگیرین و فیلم و عکساشو برامون بفرستین
@withyashar
😂</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16516" target="_blank">📅 20:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16515">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">تنگه دعوا شد
🚨
🚨
🚨
🚨
🚨
گزارش انفجار سیریک
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/16515" target="_blank">📅 19:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16514">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">هرجاى اين كشور بگى نور به قبرش بباره همه ميفهمن كيو ميگى؛ هرجا هم بگى ريدم به قبرش، باز همه ميفهمن کيو ميگى.
@withyashar</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/16514" target="_blank">📅 19:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16513">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifQW94dhOUIQersshHj43VupEn1EQMBtQC3bqSMWuDSJgpffRcGLpcnJsyX_snlDcABF9BQr4EfEP8xvgVCZnNkbE6QqvW-4IlcF0FoBxqRUMqZIQyI_OhJD2wveVQTekQn2auDQ6XNbpxahe9R0o7L9oUi1Thm6EZbvgoPx9_R-QWAvahnnMmyGIhvFQDBUQx-ikYZahh4ZGKOifk0YWTbvQU8EhCYF1pFlYd9DnRDlkyWNjEwFfjBSOcHss-AR5KVGtLgM37tkxJVQXMVmgF7ctPSupOwES9V3MJNeDzrLulT_nuiRGF1rP50evsqVvqNUhMvAE0MEiUvdBDqeqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن امير اصلانى سال ٩٣بخاطر اين نقاشى و توهين به حضرت يونس اعدام شد.
@withyashar</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/16513" target="_blank">📅 19:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16512">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHmt_jFhy3ab36wsGIb5cafR6Hu6wvYKZYUrmy0JTQVtc9k7ovr3hVirTczpvZOtRYy3tWZeM17Ic0O5_tMT4i4yARwH2fibe3J5rxEVLB5HYNIanFBBJlDb1pmKQpMmcY587L84ndSPFtcIEOYQmmCyWj2_ymV5y02PEGZhh1KGwYadEjdVKJQ0JzI20SceKT8FbpP1wd0ap42O2KYXOPExAwXlvAuzxxnYJUORsWfulS8JmueqW0_DWfshYs5mtqTKYQHnyH395skYXGdAJdxA0A435Ryz1xD6fKr--iTEJ2xubAj0xDUL3UAHBTWzYJQH50wmWnrtDIXMwYju_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک حادثه در فاصله ۳۰ مایل دریایی جنوب غربی الحدیده، یمن. یک کشتی باری، درخواست کمک ارسال کرد و اعلام کرد که مورد حمله مهاجمان مسلح ناشناس قرار گرفته است. @withyashar</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/16512" target="_blank">📅 19:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16511">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwTqQdhqnSIUbnTnYczuRolOj9S9kExrsCknZvC2Ny2h5xeYUWA2OtqQq0IrVNOdrqs8doSzzygnqWIgMnhnsljOCbQezYNZjLX1GEzcDCzSYkMs0BSdOV-UylkVc2s-Um4bonhwO_YRMDEo8BYpymTEa1zgpHFgGxXvT2-8gYDIzTa9OixEuRnNV12DsYtPjcnbINWkRBSBq4WLnOv4ZGCAms44N0EkMixLS3MX0_64p397QPzSwCtA4H9BuqjsF907I7el_GgiRpW5NxQVDgs4WA-xrCJLR6i579eeZxZP7W193rYBuNCfMnGVNAU0cLxx92yaUYPkyR-S3DCG-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی با صدور حکمی، غلامحسین محسنی اژه‌ای را بار دیگر به عنوان رئیس قوه قضائیه منصوب کرد.
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/16511" target="_blank">📅 19:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16510">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نیروی دریایی آمریکا: عملیات جستجو برای یافتن سرنشین مفقودشده در پی سقوط بالگرد در دریای عرب در یکم ژوئیه متوقف شد.
@withyashar
یاشار : خبر‌ سقوط بالگرد دوم الان فیک نیوز است</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/16510" target="_blank">📅 18:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16509">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نتانیاهو به شبکه خبری فاکس نیوز:
ایران، چه با توافق و چه بدون آن، هرگز به سلاح هسته‌ای دست نخواهد یافت.
@withyashar</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/16509" target="_blank">📅 18:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16508">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASbltLdG4l_XlFrtvi6aPISy_utEm1TI6fM5Zp0LxnMGLRW2ArAI3bWbyPBsh0wYPWl8oT0gvRWb6irfyVazUw_XwH-aq1sEmMY1IOyWswXp9-CrFYmLFHw1iNdJuC7VLCVPi2Bb1hG0y6nDVhScvlQp5qgX4XbiZBdDQ1v7eQ4ajsfe0cEqBBKsoCQNZKR_w3ynDQciu4d17Gjh5EBFp8_viHjHmuUoCWrRkmllCUaJyyP9nr79WvuoqHyi0bAvVMsGRdHG9TLuOOCfu4MgoiufGygMaP8tHmyDnTYDtJzHNaDLYM_4YdqFTa9_WxeM53jP4iWhbn6nQ9CtXS2j0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو هواپیمابر آبراهام لینکولن امروز مشاهده شد  به‌همراه یک نفت‌کش پشتیبانی (که در تصویر دیده نمی‌شود) و یک ناوشکن، در مختصات:
22.2521, 60.8321
حدود ۱۰۰ کیلومتر دورتر از سواحل عمان ، در دریای عرب؛ که احتمالاً نشان می‌دهد توافق برای کاهش تنش در عبور از تنگه هرمز با ایران  همچنان پابرجاست.
@withyashar</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/16508" target="_blank">📅 17:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16507">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">خبرگزاری های اسرائیل :امروز ثابت شد که این فرد به اسم ابراهیم ذوالفقاری وجود خارجی نداره و با هوش مصنوعی ساخته شده. چون حتی احمد وحیدی فرمانده سپاه هم توی مراسم حضور داشت ولی خبری از این نبود
@withyashar</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/16507" target="_blank">📅 17:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16506">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اتاق جنگ با شما : یاشار جان سلام
امروز تو مصلی بعد از پایان نماز ، بلندگو ورود مجتبی رو اعلام کرد اما بلافاصله هم صدای مجری قطع شد و بلافاصله آنتن ها برای مدتی قطع شد...
@withyashar</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/16506" target="_blank">📅 17:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16505">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کانال ۱۴ اسرائیل : اطلاعات جدید نشان می‌دهد که نیروی قدس ایران واحد جدیدی به نام «
مختار
» تشکیل داده است که با کارتل‌های مکزیکی و ایرانیان خارج از کشور برای توطئه ترور رئیس جمهور ترامپ و دیگر مقامات آمریکایی همکاری می‌کند.
@withyashar
🚨
😂</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/16505" target="_blank">📅 16:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16504">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فرودگاه بین‌المللی بندرعباس عصر امروز با فرود نخستین پرواز مسافری از مبدأ مشهد، پس از چهار ماه وقفه، رسماً فعالیت دوباره خود را آغاز کرد.
@withyashar</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/16504" target="_blank">📅 16:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16503">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d4a6d9f34.mp4?token=C9xwyye5fOzTxAKIMcvbQpoNNXTR7_yCXUSKC37At7YPgLehyCeEe2x808uuETdLwpZeS_I8-fDKnc0Avn1r3l1AI_5efbtg_826klS4ahwzC9AEHJd8eLv_OuLu4vLavwa4facS6QNzgvGpBmNvsU0jz_6GanXJS0LJVcltATc4VpNhPGAjcFks-0TLVrtk5d9YGydBB4bVV_59ofpxP2MuBwA-ZS8XD6wRASqkl9Q0krRp5WTPPepm21ykZ9soxaFv_IQLbHoTaDJgTIvh7Ava1-X63YIJuZGk31zFSTIBNU7BhXXRey6SDl2ySO0o0VzZi0GzHGZ9RfJdCNJTtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d4a6d9f34.mp4?token=C9xwyye5fOzTxAKIMcvbQpoNNXTR7_yCXUSKC37At7YPgLehyCeEe2x808uuETdLwpZeS_I8-fDKnc0Avn1r3l1AI_5efbtg_826klS4ahwzC9AEHJd8eLv_OuLu4vLavwa4facS6QNzgvGpBmNvsU0jz_6GanXJS0LJVcltATc4VpNhPGAjcFks-0TLVrtk5d9YGydBB4bVV_59ofpxP2MuBwA-ZS8XD6wRASqkl9Q0krRp5WTPPepm21ykZ9soxaFv_IQLbHoTaDJgTIvh7Ava1-X63YIJuZGk31zFSTIBNU7BhXXRey6SDl2ySO0o0VzZi0GzHGZ9RfJdCNJTtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همچنان حملات سنگین اسرائیل در جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/16503" target="_blank">📅 16:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16502">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f20cf4d81.mp4?token=SK8bDutQvUNviTzNZCkMpUN-3BcS_tHsrT_ci24MrqTgZTXEiT9Ln1MLyxqWSAQZ7URT1xDQ4De-nkO0U0QzuSOldkXurmn-NWq9OAtBfGu7PRQKzBRx-ArKc5MnuNMp1xeUcQw-nuilXaMS5NdQfMBs3yOmRJ5zzuwC0uaGug8gyKnsSBi8Re5RE-ZVtCz_kwM5PfS_gjfIoKuSEynIAbyx5kUdYe54Q8INvMRhb7pdZk-z5fJb1sXkhjUxu7wWxWYR9pI3ZXqh4hAXRq7IHvTHk0vIgTM5tEGElc1DioGnfNDfaIHbayh17U9-6YzGAR1o-tnRcqNMHuFreYGimg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f20cf4d81.mp4?token=SK8bDutQvUNviTzNZCkMpUN-3BcS_tHsrT_ci24MrqTgZTXEiT9Ln1MLyxqWSAQZ7URT1xDQ4De-nkO0U0QzuSOldkXurmn-NWq9OAtBfGu7PRQKzBRx-ArKc5MnuNMp1xeUcQw-nuilXaMS5NdQfMBs3yOmRJ5zzuwC0uaGug8gyKnsSBi8Re5RE-ZVtCz_kwM5PfS_gjfIoKuSEynIAbyx5kUdYe54Q8INvMRhb7pdZk-z5fJb1sXkhjUxu7wWxWYR9pI3ZXqh4hAXRq7IHvTHk0vIgTM5tEGElc1DioGnfNDfaIHbayh17U9-6YzGAR1o-tnRcqNMHuFreYGimg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/16502" target="_blank">📅 15:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16501">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsKde8Z3U_qsmsdNHB2pBlMTsm_aUpi7sYYOMO0MyvSP5JkOfNyN8eztQ4Nb-0p6hDtXXxbvLGXqmciwKDp11R7WcbiK42vzrRMhgWHLpwXe9kUiUYupk5U7rE0aKnlxxz5TFXgVzYrKe9FobvU73bDn4eyCEEK1uHhZJOH5Sr1BVehP6h7J62B0Mbd93cMKbaJjI85N2UPzbgGfmJ4MmmqBhfEbklq4zS1K2Heb1qyBJSMYhTwSwN993qHKRhTB7YbGiI2ohrRiax7fPzIAq50M4y1Z4lIBPdLwpuNJlBwd25GVT9IU_tvdYNdzDyTclNT4J9H2h-93prquVRhOrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست وزارت خارجه اسرائیل به مراسم تشییع علی‌ خامنه‌ای
@withyashar</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/16501" target="_blank">📅 15:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16500">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkMVIG3xb_bs5jxtBpNMVf3fv7iwGRKIlR1SkSEPjmJr-phgN-gZi7N916JNjecHxVigxrCDHU7pbCNo_J5vM0d9ehRtNDrDGf2maKHWEBJmXUq2NlXwYpXxuyrBEOt0Ops8Gpi99LuVha1-TsCshei1hWZirpk4Zo25LdVrII1-IQxj5lKCm_c6G0D6oWgOyvhTDzLAMqeL-v3NTF6QMhxkQcMyu6sh4ZfLkcNLlJET2WKAfCcTixSu8vOUpakvIqDkKSPYy0ADM4aVGfEQXQrGLCY8fPF3EbJmeIxwgk20bW3VZoyCRMUb2ddXqJnTXso0ZfZ3QFWzGIpG-_MNZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : از زمان آغاز جنگ در ایران، بیش از 273 آمریکایی در شیکاگو هدف گلوله قرار گرفته‌اند
😳
@withyashar</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/16500" target="_blank">📅 15:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16499">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b892031853.mp4?token=GL6G570syvHLASKpzKIfuNEvuJUIwqFwEP8n4U2mpbjaOaKEzQw6leHbcyFPEitCpxw_pUY7OiLaTkdZFEfKjdFHk1LJtWQygnaC64WxdoBtu8uSleMaxDohOs6XYJaLcPmt18C9MZQPmjXRK3GmqeBgMNMDM25-uW3hPNbC8R8uBprpk7rgw3Lf5CoLeBsmdJIYovTGlhY8Dtv3boOQt_ikloAda3rtATIdsOlYYfh0_6jvrBC4KRfED5uY8DACXa4Dvte-ThNjliD_xAbjI13rIkadkS9WXE2QbgMIhgoIoIWCzKHJbW420Njwia6V-6XkFsufv0cFa1Aja8IG0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b892031853.mp4?token=GL6G570syvHLASKpzKIfuNEvuJUIwqFwEP8n4U2mpbjaOaKEzQw6leHbcyFPEitCpxw_pUY7OiLaTkdZFEfKjdFHk1LJtWQygnaC64WxdoBtu8uSleMaxDohOs6XYJaLcPmt18C9MZQPmjXRK3GmqeBgMNMDM25-uW3hPNbC8R8uBprpk7rgw3Lf5CoLeBsmdJIYovTGlhY8Dtv3boOQt_ikloAda3rtATIdsOlYYfh0_6jvrBC4KRfED5uY8DACXa4Dvte-ThNjliD_xAbjI13rIkadkS9WXE2QbgMIhgoIoIWCzKHJbW420Njwia6V-6XkFsufv0cFa1Aja8IG0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خنده های زننده و گرم گرفتن ملعون وحید خزائی با یکی از عوامل مهم کشته شدن ۴۲،۰۰۰ جاوید نام ،  فرمانده کل انتظامی جمهوری اسلامی احمدرضا رادان
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/16499" target="_blank">📅 15:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16498">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نتانیاهو : حرف‌هایی که درباره درخواست ترامپ برای حمله نکردن به تونل‌های لبنان پخش شده
کاملاً دروغه، ترامپ اصلاً چیزی رو به من نگفته
منم چنین درخواستی ازش نکردم و ما تصمیم‌هامون رو بر اساس ملاحظات خودمون می‌گیریم
@withyashar</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/16498" target="_blank">📅 14:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16497">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHsj2scGhx7WqJdjyztkFFG8--jbFpxcb46ttjlMRQ0hIA2qMpUaKyBb397rJ8mxqzEZqa9a1p8xZXi8xCKB6mnT5OG0J1-7Y1-74UWAxxPCRKl6c3uVWrBJLGyOohOmWbTwEnYoPNYIhK_n-bmI84Fc58-aEoRY7wjydBlS_1ffnPewvi4ehcvpYukVgGybojUccdwVVgCS9wRmhYWkuAwhY5PPAAVbiLKDJT2ucT8SKsFuex_r5Hh8PSfTh_C56QIowsTMpWMotRuUcLE65NPqKPFFyK48tEUcdr5shGzE0IrLst8B75Rl1sGCdI7a5nWHxvANGNKAB50yErQ3bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک جت دولتی ایران از مسکو برگشت و هم اکنون بر روی باند فرودگاه مهر آباد تهران به زمین نشست
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/16497" target="_blank">📅 14:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16496">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asXHov4oxdpT0ZuGcTSr06YGbyogNwMG2ligUjr3TJDMTIDUamRNK5L1CJgTKXBe3Gh7lIkq6Cw0VptT4UXl0R2DwpKvp8u9sxatHw3O5j0ww_1doFfC6K3ScsyrYl_Q1BMgsTyoJYFkB8qrmPvSAhTiObcsX-bcDidfhSbJFw2D-gxL0YktsybVFqoIfrD7_DO6VMSd-JHZHR5ZDuYAMDldKeai9SMA88mkkJLyKth81GKgOFyUxNMRgDP-6Wsh-D9mpqKxKP6hY-dNFMMVHpngxPGgNYZUrMG58kM1GPgC6gjN-Uc0Va1tqXS6-b-KLD96RhZVefCvde9xgB9Ppw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که در ویس دیشب اشاره کردم که منارههای مصلی یکسان نیستند، در این تصویر هوایی هم کاملا مشخص است که ایده طراحی این بنا کاملا از سنگ توالت برداشت شده.
@withyashar</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/16496" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16495">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کانال ۱۴ اسرائیل : احمد وحیدی، فرمانده کل سپاه پاسداران، که تحت تعقیب اینترپل، تحریم‌شده توسط ایالات متحده و در فهرست اهداف اسرائیل است، دوباره در روز دوم تشییع جنازه خامنه‌ای دیده شد.
@withyashar
اتاق جنگ با یاشار : موساد این روزا حسابی سرش شلوغه و لیست جدید ترور‌ رو داره آماده میکنه تا هفته دیگه بی بی برای تایید پیش ترامپ ببره</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/16495" target="_blank">📅 14:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16494">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">شاهزاده رضا پهلوی : ‏تلویزیون بی‌بی‌سی فارسی در صفحات رسمی خود، با انتشار بخش‌هایی تقطیع‌شده از گفت‌وگوی هایم، تصویری نادرست و گمراه‌کننده ارائه کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/16494" target="_blank">📅 14:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16493">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">کان نیوز : در اسرائیل معتقدند وقوع یک درگیری نظامی مجدد با ایران در آینده نزدیک وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/16493" target="_blank">📅 13:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16492">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uxxuyvap4XXH3GKFZ8F0ZcoHeBHSRc5bA9pP1QXHdP9xhVxFOvvI6-E1J6_mOKo6uIVwsap9JlPW1RVY_OrWpH1aHFfjztiIlvtTAQaospU66L7eJ-3ZhNwL1l1B5wgDw_G-xtsErh9vkARLTjv3hmq9WNncm9ZHAs6pmdBwy1UO8St31eDMLyzUGnPWZnz38wM5wzo-VrWVoC57mVCczH3Day_6LhpJBS4U4pCsw29uDx1aiQ_EtaYp6m5ZwwDtZmoP0b3Xjf8K192ukhia-e7z2-0CwbBRPS0vktwTtZKT2AsRip1ZeucxQV3zmsL03gzdDABwCrjIdgsTyLDe3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشت هواپیمای تهاجمی A-10C Thunderbolt II که در خدمت وینگ ۲۳ ارتش آمریکا هستند، از پایگاه هوایی RAF Lakenheath به پایگاه هوایی موفق سلتی در اردن اعزام شده‌اند @withyashar</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/16492" target="_blank">📅 13:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16491">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ارتش اسرائیل : دو فرمانده حماس در حملات  هوایی به غزه کشته شدن   ارتش اسرائیل به عملیات خود برای رفع هرگونه تهدید فوری ادامه خواهد داد @withyashar</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/16491" target="_blank">📅 12:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16490">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrJypPp75aF6MKFy2Cd3juntpQqugSBUUHVMrjeAowq1iccfZjNmIvdLwmhWg1Sht36_FvKUSNWtoBVveGzvvJ1G26NDlTQ7x3C3MFZZ37DpwIVBwnrBNFrNQCAI0-naD15QUDwdQVfxToQj_k_T1_BOuxRlCIGPeAFlM1aWaotCZHT-puPKePYqs12YEVvwaeG3a6bfTaWejyUUPFczAuHqWWnFOG5fACPzewi9ZQWMFTPhTcCBUh5XDGkrcFWA0DCOT1ZLRIcvKKPHJP70uahHWYypUmnd0ByMxYVg13NRS9TJZef73Lwco-nkGNYbSNI99NMtf8D5Y0I6cyWqPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک حادثه در فاصله ۳۰ مایل دریایی جنوب غربی الحدیده، یمن. یک کشتی باری، درخواست کمک ارسال کرد و اعلام کرد که مورد حمله مهاجمان مسلح ناشناس قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/16490" target="_blank">📅 12:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16489">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کانال 15 اسرائیلی: جلسه فوق‌العاده کابینه سیاسی-امنیتی به روز سه‌شنبه موکول شد. انتظار می‌رود جلسه کوچکتر کابینه امشب برگزار شود.
@withyashar</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/16489" target="_blank">📅 12:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16488">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92ffd63b9.mp4?token=LUK18YmRTOhR_N7dO4UP00nC1KpEJkZJsCR2xAfMriUCTPXVstTClnd_fBcyuFSVBPy2RvDQ3hJJCmGfsOSyEYMVI1QPDW0n6ANQirukLajewxzXs-SdX9uWlFuHuo-xm5b7HA8CNhyqaM-bMFHsnL6-mjNaamdD1_cD6JfLAGQUJtLdgau0XQbMnEyKaOTy5v2hmSIrwEcZyi_Z2g-2XUC9MMR8-Z14naHi5_5u6SqqWFlF5HNkcOKvlRxcHbfi8iBPrPRfL1QNbnvZ7J4u6QIaBi1ziUrHM3h57k9C-hWIjBztaJbZTrTsVcPO3FfdrgkTjKh37kXrvjgh3TTFNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92ffd63b9.mp4?token=LUK18YmRTOhR_N7dO4UP00nC1KpEJkZJsCR2xAfMriUCTPXVstTClnd_fBcyuFSVBPy2RvDQ3hJJCmGfsOSyEYMVI1QPDW0n6ANQirukLajewxzXs-SdX9uWlFuHuo-xm5b7HA8CNhyqaM-bMFHsnL6-mjNaamdD1_cD6JfLAGQUJtLdgau0XQbMnEyKaOTy5v2hmSIrwEcZyi_Z2g-2XUC9MMR8-Z14naHi5_5u6SqqWFlF5HNkcOKvlRxcHbfi8iBPrPRfL1QNbnvZ7J4u6QIaBi1ziUrHM3h57k9C-hWIjBztaJbZTrTsVcPO3FfdrgkTjKh37kXrvjgh3TTFNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه های رژیم ویدیویی از حضور احمد وحیدی در تشییع جنازه نشان دادن. به نظر میرسد در صحنه ای که کات میخورد بر‌اثر هجوم و درگیری‌ بادیگارد ها  کلاهش می افتد.
@withyashar</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/16488" target="_blank">📅 12:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16487">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گزارشی درباره یک حادثه تیراندازی در آمریکا
: طبق گزارش شبکه خبری ABC، حداقل هشت نفر، از جمله چهار کودک، در کونی آیلند، ایالت نیویورک، در جریان جشن‌های روز استقلال آمریکا مورد اصابت گلوله قرار گرفتند.
@withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/16487" target="_blank">📅 12:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16486">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">زمین لرزه شدیدی شهرستان بستک در غرب هرمزگان را لرزاند
@withyashar</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/16486" target="_blank">📅 11:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16485">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37255614f1.mp4?token=nmxc37YaNQ5PI_tGJgl-he1YNluFCj788azBw4r7jryTiuHjzrVisbco9muKa9ZJWGxo9JxkM6X90FbKeJnauR9-FrwMDEE0jNWCLjguxl1Njw4a9ONUswvJBXwT2OPhzo2bXuqd8BxWKf_ljyg1JXW0Kl5xMKsC8LJEPu6bGlccjKrg9h7l524IV-qKYKPWy4Yr9Cs-PtQBkpgdSEZWnjyIrjrACM2KDL-mODUSC5EmYWJ39VtavmWn5tI2Zvs9O7X4r6D0uYOoFLnzPgAl9Td7s4-QcX_8KDV3LdrzBaqsHr9cdI-i8N_kMWzVK0kmretl0giMY5EYqrbU30Tf8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37255614f1.mp4?token=nmxc37YaNQ5PI_tGJgl-he1YNluFCj788azBw4r7jryTiuHjzrVisbco9muKa9ZJWGxo9JxkM6X90FbKeJnauR9-FrwMDEE0jNWCLjguxl1Njw4a9ONUswvJBXwT2OPhzo2bXuqd8BxWKf_ljyg1JXW0Kl5xMKsC8LJEPu6bGlccjKrg9h7l524IV-qKYKPWy4Yr9Cs-PtQBkpgdSEZWnjyIrjrACM2KDL-mODUSC5EmYWJ39VtavmWn5tI2Zvs9O7X4r6D0uYOoFLnzPgAl9Td7s4-QcX_8KDV3LdrzBaqsHr9cdI-i8N_kMWzVK0kmretl0giMY5EYqrbU30Tf8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل : دو فرمانده حماس در حملات  هوایی به غزه کشته شدن
ارتش اسرائیل به عملیات خود برای رفع هرگونه تهدید فوری ادامه خواهد داد
@withyashar</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/16485" target="_blank">📅 11:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16484">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBU4YiZiJO5sfX67sEFsnBIk5caqB52E0Y7jON3c1Z9bDmvss4d6chAOQBl3HsWMdffhsL3p1olA6x5rZc90pgSQ2nYnt3kgiICm_pBK3aaeHlgeSNgeiBiXfZ32MIobrfHccwOCtw2T5mzGk6CQWnGUzchq9TxpIXHKm0K_ITYIfjvvwYPRui4eBT3fmU_l8VgvybAVFNTLEJy2ldocpYhcwev84F_fkog2EIA39sDRiBkwgNTzegwYSmS7AtoDhv65UYqkFzPVF60dKbizLM2g8Crvo_BNjSUAwZdc9UhtJ0bIffUwg_IAzwO9Afboft5uOzW6qUSs5A0bpbtaHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌اکنون با پوشش هوایی و اسکورت سنگین، ارتش ایالات متحده یک کشتی باری (با AIS روشن) را از مسیر عمانی عبور می‌دهد!
این اولین عبور امروز خواهد بود اگر موفقیت آمیز باشد.
@withyashar</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/16484" target="_blank">📅 11:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16483">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">قایق‌های تندرو سپاه، مسیر عمانی را بستند
هرمزلتر: نیروی دریایی سپاه با استفاده از قایق‌های تندرو، کریدور مورد حمایت آمریکا در تنگه هرمز را به طور کامل متوقف کرده و در نیم روز هیچ شناوری از این مسیر عبور نکرده.
سپاه صبح امروز از طریق بی‌سیم به تمامی کشتی‌ها هشدار داد و همزمان قایق‌های گشتی نیروهای ویژه را برای اعمال کنترل ایران بر تنگه هرمز مستقر کرد.
@withyashar</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/16483" target="_blank">📅 11:33 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
