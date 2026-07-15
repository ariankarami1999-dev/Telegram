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
<img src="https://cdn4.telesco.pe/file/XEPx3HeecqAQ_V7GpJs6yHCUO5awMV3VnjdAmJPAP8r-7xFT1PY8uZpXj-PRXM6luH5xsWcJjbx5VbnVyorpEuxOfIvVhqO0kMn-36PLab4aD51J10PVdUECAvneSpsKNCZM7FeRwx3rW7Btg0R5lIZCqXR2vmPnwS0Vo0zjI6HG6Nq0Gn3QkSFCOQv6d6fxXoXw_hN-tgqM3Col7eldz8Bsr0hkT2WOU8jdCqh8I2R3axJvirZRsRLvVnslLAZ9_sZSwLTX2sfZSdG4WzPiwxdsJnCP5JdBGOg8rFpo-as7YIepG66xiEp6S0EPpOhiIRpxqyb7QVZMr_Q8KGjYvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 393K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 23:34:48</div>
<hr>

<div class="tg-post" id="msg-18287">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گزارش انفجار کنارکککک
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/withyashar/18287" target="_blank">📅 23:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18286">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دقایقی پیش ترامپ: به این نتیجه رسیده ام که نمیتوان با سپاه پاسداران انقلاب اسلامی مذاکره کرد. خبرنگار: آیا یعنی ممکن است همانطور که با داعش کردی، آنها را از بین ببری؟ ترامپ: "بله، درست است. خواهیم دید چه میشود @WarRoom</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/withyashar/18286" target="_blank">📅 23:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18285">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دقایقی پیش ترامپ: به این نتیجه رسیده ام که نمیتوان با سپاه پاسداران انقلاب اسلامی مذاکره کرد.
خبرنگار: آیا یعنی ممکن است همانطور که با داعش کردی، آنها را از بین ببری؟
ترامپ: "بله، درست است. خواهیم دید چه میشود
@WarRoom</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/withyashar/18285" target="_blank">📅 23:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18284">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">انتشار این پست و معرفی من در گروه ها و تمام دوستاتون تنها کمک شماست
🙌🏾
🌐
instagram.com/Yashar
🌐
t.me/WarRoom</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/withyashar/18284" target="_blank">📅 23:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18283">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گزارش انفجار بوشهر
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/withyashar/18283" target="_blank">📅 23:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18282">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">️تسنیم:
پرواز جنگنده‌های آمریکایی بر فراز سواحل جنوبی سیستان‌و‌بلوچستان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/withyashar/18282" target="_blank">📅 23:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18281">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اهوازی های عزیز ماشین بازن ، به چیزای خوب فکر کنید بعد آزادی،  پیست میبینمتون
❤️‍🩹
قویییی‌ باشین
🦾</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/18281" target="_blank">📅 23:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18280">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اهواز سفتتتتتتت زددددد اینبار
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/18280" target="_blank">📅 23:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18279">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">هم اکنون پایگاه شیخ عیسی بحرین هدف موشک های ایرانی
@WarRoom
هدف نه اصابت</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/18279" target="_blank">📅 23:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18278">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اهواز بازم زدن
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/18278" target="_blank">📅 23:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18277">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🤯</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/18277" target="_blank">📅 23:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18276">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b902c0e83.mp4?token=bD7PP93Cg1za-mlG3Zxc6MY3V2JXKFoeslrKmgxJlvU9C2U4m4-Wbyn8046YzId1jqzkie6Lhb5kIpBGX7DA9N8MqVjI9NwWSkLJ-vWc8f8uSv0Y6DuFlmwl_L0tBMRcMtQojtCcOVKPvLzYNCzFUDnmDCOMhKEAgpiBTU6Y87v_o0E2igZzpC6QzJm4LDT48V8PF7mDPQwnTJpgi_UGEN-wJbXhKXMNZ8hafvqK38rBO9Iz6Eb_gbKpsIfDt20Y6-WZZYn7VYXQIXBoiU860Z6klkYHCuSBtfEvmcX0BZ3VpFJYwAyYhyAawC2z_ezNLE5s98AZ8Ah6HoClE9W0_IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b902c0e83.mp4?token=bD7PP93Cg1za-mlG3Zxc6MY3V2JXKFoeslrKmgxJlvU9C2U4m4-Wbyn8046YzId1jqzkie6Lhb5kIpBGX7DA9N8MqVjI9NwWSkLJ-vWc8f8uSv0Y6DuFlmwl_L0tBMRcMtQojtCcOVKPvLzYNCzFUDnmDCOMhKEAgpiBTU6Y87v_o0E2igZzpC6QzJm4LDT48V8PF7mDPQwnTJpgi_UGEN-wJbXhKXMNZ8hafvqK38rBO9Iz6Eb_gbKpsIfDt20Y6-WZZYn7VYXQIXBoiU860Z6klkYHCuSBtfEvmcX0BZ3VpFJYwAyYhyAawC2z_ezNLE5s98AZ8Ah6HoClE9W0_IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین الان پاسگاه احمدریزه چابهار
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/18276" target="_blank">📅 23:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18275">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اهواز قیامته دیگه نگمممممم</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/18275" target="_blank">📅 23:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18274">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvZWTm51n3QpPGE-YEZhwJ6ANvDF4EksLpAz7j4sSVDcvixZpNuMq2mENbg_hjWNHtSOICiDUH-MTMkw7faV97gbYB2kCYhbcATkOxJbWswhEtVLnJHyecSffHy5lreLBrkcT8X_23swiSoz4gN6M-osG3vrYQoThFJU495XDHwLq64tzgtzEl7-7IOWeMXs83vl8I73RgMSlq3yHcW1nPFe6S1zYyqfSpkhBIpw0UJT6pyJCGp6ur8_H-CuvVbKyJQsLgsFHkbkWZsInrHQnuFptu_2jN4JOu3LVAUBFwn4DY_KcmgcPFarcWw3eF_QvCDDpl-N3HpxWmPD-1SCgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راسک سیستان بلوچستان زدن
@WarRoom</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/18274" target="_blank">📅 23:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18273">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/294a418fbc.mp4?token=ki1PHAYuqyInm0BRDoht24tcRK-DC73uQ9nXJ4XzS5tCgYWmD_swyKynGHcDPoDvYqGIuz0JD9Ikb0aj7oi3tczMY107kXWjl3Z8A6uHcARbpEDM3N4kb5fOX9KUHEbTeCA0QouucETmLnrJzzlsVBXGv0qXmqBk2UjY-oMJ_lC6Ocd2aY5pfM33hZyYK219h8pS5FwMzr9O-rm06xEG1Mt1-pL3HcJUMtm7hdPp-8eDuawbHXlytDIFyTx71_1vuiyzV4kW2wV6Eu35lsGPOrx9O9y0W9dzgHgX_bvub3kziECkPx9lsG4k3rS-XJQ3ICN3IDnogHAsEoHWxBSU2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/294a418fbc.mp4?token=ki1PHAYuqyInm0BRDoht24tcRK-DC73uQ9nXJ4XzS5tCgYWmD_swyKynGHcDPoDvYqGIuz0JD9Ikb0aj7oi3tczMY107kXWjl3Z8A6uHcARbpEDM3N4kb5fOX9KUHEbTeCA0QouucETmLnrJzzlsVBXGv0qXmqBk2UjY-oMJ_lC6Ocd2aY5pfM33hZyYK219h8pS5FwMzr9O-rm06xEG1Mt1-pL3HcJUMtm7hdPp-8eDuawbHXlytDIFyTx71_1vuiyzV4kW2wV6Eu35lsGPOrx9O9y0W9dzgHgX_bvub3kziECkPx9lsG4k3rS-XJQ3ICN3IDnogHAsEoHWxBSU2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اهواز الان
@WarRoom</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/18273" target="_blank">📅 23:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18272">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اهواز رو همینجور میزنه کلا
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/18272" target="_blank">📅 22:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18271">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گزارش انفجار سنگین بندر عباس
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/18271" target="_blank">📅 22:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18270">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سنتکام : در ساعت
۳:۰۰ بعدازظهر به وقت شرق آمریکا (ET)
(۲۲:۳۰ به وقت تهران)
، نیروهای ایالات متحده عملیات
دومین موج حملات
امروز علیه ایران را آغاز کردند.
این حملات توانمندی‌های نظامی ایران را هدف قرار داده است؛ توانمندی‌هایی که به گفته آمریکا برای تهدید کشتی‌هایی که به‌طور آزاد از
تنگه هرمز
، آبراهی بین‌المللی و حیاتی برای تجارت جهانی، عبور می‌کنند، مورد استفاده قرار می‌گیرند.
ارتش ایالات متحده اعلام کرده است که
به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، ایران را در قبال این اقدامات پاسخگو می‌داند
@WarRoom
یاشار : دقیق نیم ساعت بعد که گفتم شد
💥</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/18270" target="_blank">📅 22:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18269">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سنتکام : شروع کردیم
@WarRoom</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/18269" target="_blank">📅 22:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18268">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">انفجار سنگین در اهواز حتی از قبلی ها هم سنگین تر
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/18268" target="_blank">📅 22:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18267">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دوباره چابهار رو زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/18267" target="_blank">📅 22:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18266">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxxYR_zCbq76yxQ8yF9yE39uyxWaBB0Fq6-_NfdYVGd2-Q9GVU0GWXDrAgeI3coET2fFj3FMcS7oJWMge_9QOqiF7h_Lw_zUlyw3cidaTfT0zMHMWn-hmHmyJTNq6KwAuBeC9BD8OkuhdpVyKjQlWYqE0biaDCcJAztYv0jkoIV47ik0BAFmn0QcYQG9v5GjNG_hlPPV4keQgOHZ4JO_CEU4twwWvsv_NitJyndfCh36llVJfQJAfWtY6sgY2nq4QFiymBACkHYKCMXqtSIx8HJmMkUExS-Zj6LcmV4VDYarUkqG0SPBOFPUWG_tUOEDjLHxrLVzg9jvj3g5dnps2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منوجان در کرمان  پایگاه سپاه رو زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/18266" target="_blank">📅 22:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18265">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">انفجار سنگین منوجان در استان کرمان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/18265" target="_blank">📅 22:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18264">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">در مجموع ۸ انفجار شدید در اهواز گزارش شده
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/18264" target="_blank">📅 22:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18263">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">۵ تا دیگه اهواز رو زد شهر تکون خورد
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/18263" target="_blank">📅 22:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18262">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">۲ انفجار شدید چابهار
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/18262" target="_blank">📅 22:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18261">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گزارش انفجار چابهار
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/18261" target="_blank">📅 22:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18260">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یاشار دوتا دیگه زدن اهواز خونه داره می لرزه صداش ۲ برابر دیشب
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/18260" target="_blank">📅 22:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18259">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یه نیم ساعت دیگه سنتکام بیانیه میده شروع کردیم موج ۴رم
😂</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/18259" target="_blank">📅 22:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18257">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">۳ تا سنگین زد اهواز و انگار زلزله اومد
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/18257" target="_blank">📅 22:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18256">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انفجار‌ اهواززززززز
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/18256" target="_blank">📅 22:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18255">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ :  من از تعیین ضرب‌الاجل خوشم نمی‌آید.
@WarRoom
یاشار : نیست خیلی هم رأس پایان عمل میکنی و۴۷ بار‌تمدیدش نمیکنی.
🤒</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/18255" target="_blank">📅 22:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18254">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گزارش دو انفجار در کنسولگری آمریکا در اربیل
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/18254" target="_blank">📅 22:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18253">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گزارش صدای انفجار اهواز
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/18253" target="_blank">📅 22:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18252">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/18252" target="_blank">📅 22:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18251">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0279bf2042.mp4?token=BCZEHc0BW2DkfTm401G4XxcS5tnys-lkr2xM6QyIm-NnLPZbi8CJGV3v16WrjauqiLey6cQBEnMmxMgz4XfoMuqWiATd08wqckXYXtF8Ta2zrnmbAyuRLEJ8HuNhPZCIagfsa7VuqzyzPOb_9KPo4Gdun2fI1icVdhPPdCL6EWrR49hQBSaE4HxYhgGf7DJqZBvpXoK_WhVM6BF33jmX-uaRh1OfBsWePvgmSGLMhTECbVuDuBolpD2PMN0TF_lTjC4WKV1n3dgxHdo0XhCjwPMhcu0-xsi-6OHQpA1csod2y5HWO6Qjal7SAPo0FjBu3Do3_9QQ5E1zhnp7q_sEtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0279bf2042.mp4?token=BCZEHc0BW2DkfTm401G4XxcS5tnys-lkr2xM6QyIm-NnLPZbi8CJGV3v16WrjauqiLey6cQBEnMmxMgz4XfoMuqWiATd08wqckXYXtF8Ta2zrnmbAyuRLEJ8HuNhPZCIagfsa7VuqzyzPOb_9KPo4Gdun2fI1icVdhPPdCL6EWrR49hQBSaE4HxYhgGf7DJqZBvpXoK_WhVM6BF33jmX-uaRh1OfBsWePvgmSGLMhTECbVuDuBolpD2PMN0TF_lTjC4WKV1n3dgxHdo0XhCjwPMhcu0-xsi-6OHQpA1csod2y5HWO6Qjal7SAPo0FjBu3Do3_9QQ5E1zhnp7q_sEtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ  : همین الان اربیل عراق ، درگیری پدافند آمریکا با حملات ۳پا
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/18251" target="_blank">📅 21:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18250">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1SNLvFXz37CKUY5gc6-y1KFMdP03o0miNgS2rA7Az6sUSRWm8FMH5vuqBYfRX-L0NM37UsivJCxZ32XI6FQwFn1AOs7aKdy2kAqgXKmw1p-jRIKYeewgSIrL4E_NyMSrpvM9gANiOlGcNx7Rgbj2VBrATHuxTE02chU2Q67YCY-UUqckZLUjdfAKuWQWADlL8euI-Qv9UBNiHt_qfaBu0IdxPpNb9TCK0MgjeN3czgzPgnPqDGbsXBMVEZuo7ol8AH1jKoIqvgqtp-nL8p5u2WpIVDZ5tVodLix7guc_yEoTmV8ufP6g7BKU6CrbHkt-5BcBviOHWXR_mexrLVWlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا اعتراضات و اعتصاب از پاساژ چارسو و علادین شروع شده و حسابی شلوغ شدن @WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/18250" target="_blank">📅 21:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18249">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گزارش انفجار بندر عباس
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/18249" target="_blank">📅 21:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18248">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سپاه پاسداران ایران در حال حاضر سامانه‌های پدافند هوایی SAM ساخت داخل، S-400 روسی و HQ-9 چینی را در نزدیکی خلیج فارس، مرز عراق و تنگه هرمز مستقر کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/18248" target="_blank">📅 21:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18247">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ بار دیگر تهدید کرد: هفته آینده بدترین هفته برای ایران خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/18247" target="_blank">📅 21:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18246">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">قالیباف : انتقام عمام را میگیریم
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/18246" target="_blank">📅 21:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18245">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">قالیباف:
تفاهم‌نامه زمانی معنا دارد که بندهای آن معتبر و درحال اجرا باشد
، در غیر این‌صورت
اگر قرار باشد جمهوری اسلامی ایران از این متن انتفاع نبرد ما نیز براساس سیاست چشم دربرابر چشم که قبلا گفته ام، دلیلی برای پایبندی به چنین تفاهمی نداریم
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/18245" target="_blank">📅 21:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18244">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وزارت خارجه آمریکا:
از تمام شهروندان خود می‌خواهیم فوراً ایران، عراق، لبنان و یمن را ترک کنند
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/18244" target="_blank">📅 21:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18243">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یک مقام ایرانی به المیادین: تهران پیامی خصوصی برای جی دی ونس، معاون رئیس جمهور ایالات متحده، ارسال کرده و در آن جارد کوشنر و استیو ویتکاف، فرستادگان ویژه، را به سوءاستفاده از اطلاعات محرمانه مذاکرات ایالات متحده و ایران برای منافع مالی و افشای اطلاعات حساس متهم کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/18243" target="_blank">📅 20:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18242">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خبرگزاری آکسیوس گزارش داد: به گفته یک مسئول کاخ سفید، سفر نتانیاهو به دیدار رئیس‌جمهور ترامپ در هفته آینده در برنامه کاری او قرار ندارد و باید منتظر باشیم و ببینیم چه اتفاقی می‌افتد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18242" target="_blank">📅 20:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18241">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18241" target="_blank">📅 20:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18240">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEXN_qFiPlmiKdS3bSUgvgQJmOOthtKpEvWTL3niSDU9EmsPasm5w7XttTIgHp9qtok6Gb-CMx_shWAXGTOySUXfKXtPQEA55bwwSa_vppOoFSNnHfnlQSe6tZMGFwzqSu0_2ll1ULIB_xMGshe0Se23ECPtQAl2e8xKbwKF4mMlC3WBPyaigIYnrmvprS8IkPgSco1NjQzk9qnBzJUEiz58QuCBy4b7WDwnFDHL5_RuVtVllOxG0NzpRdmrJqDWSmoO8ukiYFcZkHQE1wYEAboNAxOqZqcvEfUvz5TgX1-teFs9v7K_2fvfRwedvSasLTQIhqk4cmepVKDEdcrtgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ۷ تن از سربازان ارتش ایران که در جریان حمله نظامی آمریکا به منطقه بمپور در جنوب شرقی ایران شهید شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18240" target="_blank">📅 20:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18239">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حمله ۳پا به کویت : انفجارهایی اردوگاه پیونگ متعلق به ارتش آمریکا در کویت را لرزاند. @WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/18239" target="_blank">📅 19:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18238">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حمله ۳پا به کویت : انفجارهایی اردوگاه پیونگ متعلق به ارتش آمریکا در کویت را لرزاند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18238" target="_blank">📅 19:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18237">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRZhkGYWisppIFRJrgUlM7cCIATrNGA8t1Nd-grHjQFEwueTVnsLgu56oYq81RNtWhrJmjqyT6MGus_AEBbjdwjWY18K5wmPhn5XDs_2Yxl_bXxWOxDRXVhOhur3Ri-KYQ5ly4_4jbZnpOJOA_ZQ5ZX-4ANXKBYE7N6Iw_eDV2D-oyRfHgHoA28jAeUDv3UmYG4ID166AopVG89H34Flj8gXWj80OhxI48oyQdSGEla-b_QIkRnCFwHMhTulum5lizU-inZmMUqp6kDHk8qdspKmhzDW9ozhwiHDh2wD_M3tU_5BrgII4lHAEoRcPh1Ike5x85q8ajzlJQ7FswgIPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حقیقت یابی سنتکام :
ادعا:
رسانه‌های حکومتی ایران مدعی شده‌اند که نیروهای ایالات متحده در ۱۴ ژوئیه یک سیلوی ذخیره گندم غیرنظامی در هویزه را هدف قرار داده‌اند. این ادعا
نادرست
است.
واقعیت:
در ۱۴ ژوئیه، نیروهای ایالات متحده مواضع نظامی ایران را در
بندرعباس، خورموج، اهواز، قشم، تنب، بوشهر و کوه استک
هدف قرار دادند تا توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را کاهش دهند. در مقابل، ایران غیرنظامیانی را که در حال عبور از تنگه هرمز و همچنین در کشورهای همسایه حوزه خلیج فارس بودند، هدف قرار داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18237" target="_blank">📅 19:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18236">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اسرائیل با بمباران هوایی، جنوب لبنان را مورد حمله قرار داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/18236" target="_blank">📅 19:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18235">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وزارت بهداشت ایران: از آغاز حملات آمریکا به جنوب کشور، ۳۵ نفر کشته و ۳۰۰ نفر مجروح شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18235" target="_blank">📅 19:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18234">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ به فاکس نیوز: خوب خواهد بود اگر اسرائیل در لبنان حضور نظامی خود را کاهش دهد تا بر مسئله مهم‌تر یعنی ایران تمرکز کند.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18234" target="_blank">📅 19:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18233">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گزارش از اختلال شدید اینترنت
🚨
😔
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18233" target="_blank">📅 19:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18232">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اوفک، چهار فرد و سه نهاد را به فهرست افراد و نهادهای تحریم‌شده اضافه کرده است. بهروز نمازی، شهروند ایرانی، به دلیل ارتباط با سپاه پاسداران , دونیا اتایب، شهروند ایتالیا، ماریا سلینا و وادیم دروژبین، دو شهروند روسیه، نیز به این فهرست افزوده شدند.
از جمله نهادهای تحریم‌شده، شرکت ایرانی نیکا جت، شرکت روسی آوراتک و شرکت ونگارد تاکتیکال ساپلای مستقر در نیجریه هستند. وزارت خزانه‌داری آمریکا اعلام کرد این نهادها با بهروز نمازی ارتباط دارند و مشمول تحریم‌های ثانویه شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18232" target="_blank">📅 19:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18231">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">انفجار جزیره هنگام
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18231" target="_blank">📅 18:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18230">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گزارش از اختلال شدید اینترنت
🚨
😔
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18230" target="_blank">📅 18:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18229">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دور مذاکرات بین اسرائیل و لبنان در رم، ایتالیا، به پایان رسید. مقام اسرائیلی گفت که مذاکرات خوب بود و قبل از شروع مراحل اولیه مناطق آزمایشی، به مقدمات و توافقات بیشتری نیاز است. او ادعا می‌کند که این امر در روزهای آینده محقق خواهد شد. در همین حال، یک منبع…</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18229" target="_blank">📅 18:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18228">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">امیرحسین ثابتی
: نقشه قطعی دشمن ترور رهبر جدید ایران است
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18228" target="_blank">📅 18:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18227">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59153729d1.mp4?token=EOHGYl2DRPwTQfluKuyntKoAW3u_4k4Gs0LKPU1IEC2Y2UeKN7CbKv5YOOWT8o6kaCdRIImcNglXmNGd9aXBhcwrTkk6xLiyfalKpWHjmS7Ex82sD5W0zHgI428QynfHZBt6u_uDoYPI_PMuowlH2hkgj7Ozy0XhKHPtIRdIiqTVT0KBVep5s85MdcLI_qKl8zMseZ6hYqRW2DUYkl42kmW0DXJ30cUO25aMZP66c0pXD8vWDAIPpa9lee8ej6pR8ckS2JjF8QdfJMexhng-8Ai6peXZVcmiQhE0Im_qMH4PXQYn4Z8mwCiesrsa6kok98qK1y_IliH6bVr_oaYI0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59153729d1.mp4?token=EOHGYl2DRPwTQfluKuyntKoAW3u_4k4Gs0LKPU1IEC2Y2UeKN7CbKv5YOOWT8o6kaCdRIImcNglXmNGd9aXBhcwrTkk6xLiyfalKpWHjmS7Ex82sD5W0zHgI428QynfHZBt6u_uDoYPI_PMuowlH2hkgj7Ozy0XhKHPtIRdIiqTVT0KBVep5s85MdcLI_qKl8zMseZ6hYqRW2DUYkl42kmW0DXJ30cUO25aMZP66c0pXD8vWDAIPpa9lee8ej6pR8ckS2JjF8QdfJMexhng-8Ai6peXZVcmiQhE0Im_qMH4PXQYn4Z8mwCiesrsa6kok98qK1y_IliH6bVr_oaYI0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: جولانی وارد عمل خواهد شد و کار حزب‌الله را یکسره خواهد کرد
او این کار را به شیوه متفاوتی انجام خواهد داد. فکر می‌کنم جولانی دقیق‌تر از اسرائیل عمل خواهد کرد. او ساختمان‌ها را تخریب نخواهد کرد.
جولانی خودش مایل به انجام این کار است و من دارم به چراغ‌ سبز نشان‌دادن به او فکر می‌کنم.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18227" target="_blank">📅 18:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18226">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تا ساعتی دیگر ممباقر قالیباف درباره جنگ و تحولات کشور یک بیانیه مهم می‌دهد
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/18226" target="_blank">📅 18:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18225">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">انفجار جزیره هنگام
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18225" target="_blank">📅 18:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18224">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ: ممکن است تصاویر مدرسه میناب با هوش مصنوعی تولید شده باشد!   فکر نمی‌کنم هیچ‌کس هیچ‌وقت بتواند بفهمد آنجا چه اتفاقی افتاده. همچنین ممکن است آن تصاویری که در اختیار دارید، با هوش مصنوعی ساخته شده باشند. به نظرم هیچ گزارش قطعی‌ای درباره این موضوع نمی‌…</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18224" target="_blank">📅 18:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18223">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f54be6fd8.mp4?token=mTaR9xkWAHMkS2FIN3ScxElojKsXQDetFTFHtO10G48zeTTrHJtPGXSO6NiJ6BsKyL2JkF7USZDCDTOgzKelWKudJThS3JME4SmVN3w0sLN2quOiYpYICrUPnRvTIVv2zu6zJcWMzlr1oGA_h_Jy7vTVU_IWRmKiXT0VddzsdWwtVCQS7JA6NyAzGFPboveA1SCJJX2sGEmZWKRItk88lK9z34Z7JJrNUST6MawhIjlcG64ENnfLpK6nBwxCBvsSzv27wiTuAvUcr_bwbwtUyOQ9-t_oELVwbSA6lc8VqIqDPBrGlPw0RUU04vWqDpjVQFCBcMaOy3CIvSoVGV0uRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f54be6fd8.mp4?token=mTaR9xkWAHMkS2FIN3ScxElojKsXQDetFTFHtO10G48zeTTrHJtPGXSO6NiJ6BsKyL2JkF7USZDCDTOgzKelWKudJThS3JME4SmVN3w0sLN2quOiYpYICrUPnRvTIVv2zu6zJcWMzlr1oGA_h_Jy7vTVU_IWRmKiXT0VddzsdWwtVCQS7JA6NyAzGFPboveA1SCJJX2sGEmZWKRItk88lK9z34Z7JJrNUST6MawhIjlcG64ENnfLpK6nBwxCBvsSzv27wiTuAvUcr_bwbwtUyOQ9-t_oELVwbSA6lc8VqIqDPBrGlPw0RUU04vWqDpjVQFCBcMaOy3CIvSoVGV0uRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوه قضاییه با استناد به این ویدیو : محمدامین دهاقانی رو  به جرم آتیش زدن فرمانداری و تخریب اموال عمومی و فیلمبرداری برای رسانه های موساد؛ صبح امروز اعدام کرد
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/18223" target="_blank">📅 18:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18222">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95c80c5db7.mp4?token=jYEUVbN7KFPkl49rgV75FYo6B59z_dhrXCapk2JvlF5XRysJMKg3EiJFm7OWtYimb1a6haXIb5dXFwYcz-Mo8FOD2Rww242_9FEcrh0rrwWs3jKVqBNbHeALh_79oq0U0GOsgkiKd296IfBa2rlahLmBqPI0oSwBhHQnP-DuhSmdMsmgbeMk_xCcRCMca2sq7aSGaWbt7ykbeAbsVyWUQM1J3M4ktEHfVksiTf1FUxPigT2fZBeDp7wsjsl_yyD7fkPi-p6p2kocMKvaAa_NcU-_qNEaSnanu7eVrRJ6mIpsAxEgtTPS2rROex7SZKXhOpyDtWbzKRsJ3c8-oeY_Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95c80c5db7.mp4?token=jYEUVbN7KFPkl49rgV75FYo6B59z_dhrXCapk2JvlF5XRysJMKg3EiJFm7OWtYimb1a6haXIb5dXFwYcz-Mo8FOD2Rww242_9FEcrh0rrwWs3jKVqBNbHeALh_79oq0U0GOsgkiKd296IfBa2rlahLmBqPI0oSwBhHQnP-DuhSmdMsmgbeMk_xCcRCMca2sq7aSGaWbt7ykbeAbsVyWUQM1J3M4ktEHfVksiTf1FUxPigT2fZBeDp7wsjsl_yyD7fkPi-p6p2kocMKvaAa_NcU-_qNEaSnanu7eVrRJ6mIpsAxEgtTPS2rROex7SZKXhOpyDtWbzKRsJ3c8-oeY_Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ: وقتی عملیات خشم حماسی رو آغاز کردیم، فکر می‌کردم تغییر رژیم در ایران ممکن باشه.
اما هرگز تصور نمی‌کردم حکومت ایران حاضر باشه برای حفظ قدرت، 52 هزار نفر یا حتی یک نفر رو قربانی کنه.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/18222" target="_blank">📅 18:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18221">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ: ممکن است تصاویر مدرسه میناب با هوش مصنوعی تولید شده باشد!   فکر نمی‌کنم هیچ‌کس هیچ‌وقت بتواند بفهمد آنجا چه اتفاقی افتاده. همچنین ممکن است آن تصاویری که در اختیار دارید، با هوش مصنوعی ساخته شده باشند. به نظرم هیچ گزارش قطعی‌ای درباره این موضوع نمی‌…</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/18221" target="_blank">📅 17:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18220">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe78e56925.mp4?token=Z5n321mm4Bhjz7KudfvchmDjyA_pl2HL2TAGukJTHjtK8jOjFBUY1kjD7rp61p0uhCBAZx9zuf50ZgiI3xJ05vRFL0t8iSbnPSTukkR-vyt_yUGXACcg50Q3ZDosMMN7UloVRvO1K7lmi48eDD4Qac0mk0T4snUmwl00qKrjTsuWciz-WIrN06Lrrx8SENoCL3cgXOi5mtv0eziJwD3dloCAJZj_Cy-q6QbyYNvIGrHdkrBjkfS5MHkrhEX6YcxoqdqNW6ff2mjol25-5eULdxRKMxSQBggDSaXFgJSag6AguWSg5cWBp4pFVH5AoVYhDf4auwZP-ExSFGqADiwv9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe78e56925.mp4?token=Z5n321mm4Bhjz7KudfvchmDjyA_pl2HL2TAGukJTHjtK8jOjFBUY1kjD7rp61p0uhCBAZx9zuf50ZgiI3xJ05vRFL0t8iSbnPSTukkR-vyt_yUGXACcg50Q3ZDosMMN7UloVRvO1K7lmi48eDD4Qac0mk0T4snUmwl00qKrjTsuWciz-WIrN06Lrrx8SENoCL3cgXOi5mtv0eziJwD3dloCAJZj_Cy-q6QbyYNvIGrHdkrBjkfS5MHkrhEX6YcxoqdqNW6ff2mjol25-5eULdxRKMxSQBggDSaXFgJSag6AguWSg5cWBp4pFVH5AoVYhDf4auwZP-ExSFGqADiwv9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ممکن است تصاویر مدرسه میناب با هوش مصنوعی تولید شده باشد!
فکر نمی‌کنم هیچ‌کس هیچ‌وقت بتواند بفهمد آنجا چه اتفاقی افتاده. همچنین ممکن است آن تصاویری که در اختیار دارید، با هوش مصنوعی ساخته شده باشند. به نظرم هیچ گزارش قطعی‌ای درباره این موضوع نمی‌ شود داد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/18220" target="_blank">📅 17:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18219">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : صحبتهای ترامپ که الان پخش میکنند قدیمیه</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/18219" target="_blank">📅 17:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18218">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">زلزله گرگان
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18218" target="_blank">📅 17:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18217">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">رویترز: عربستان سعودی به ایالات متحده اجازه داده است از یک پایگاه هوایی در فاصله حدود ۷۰ کیلومتری مکه مکرمه در جنگ علیه ایران استفاده کند ، بدین ترتیب این شهر مقدس به سپر حفاظتی برای نیروهای آمریکایی تبدیل شده است @WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18217" target="_blank">📅 17:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18216">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">صداوسیما: دلیل حملات آمریکا، پنهان کردن شکست و ناتوانی خود بوده که با پاسخ قاطع و قوی‌تر نیروهای مسلح مواجه شد.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18216" target="_blank">📅 17:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18215">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ایلان ماسک می‌گوید
ایکس (X) پس از تکمیل بررسی امنیتی، کل کد منبع خود را متن‌باز خواهد کرد
و از
بررسی‌کنندگان مستقل دعوت خواهد کرد تا تأیید کنند سیستم فعال و در حال اجرا، با کدی که منتشر شده مطابقت دارد
.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18215" target="_blank">📅 17:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18214">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گزارش صدای انفجار اهواز
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18214" target="_blank">📅 16:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18213">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سنتکام : از زمان آغاز مجدد محاصره دریایی بنادر ایران در ۱۷ ساعت پیش، نیروهای آمریکایی مسیر دو کشتی تجاری را که سعی در عبور از این محاصره داشتند، تغییر داده‌اند. ارتش ایالات متحده همچنان هوشیار و آماده است تا از رعایت کامل این مقررات اطمینان حاصل کند.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18213" target="_blank">📅 16:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18212">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">زمین‌لرزه‌ به بزرگی 3.2 ریشتر خرمشهر رو لرزوند
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18212" target="_blank">📅 16:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18211">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دور مذاکرات بین اسرائیل و لبنان در رم، ایتالیا، به پایان رسید. مقام اسرائیلی گفت که مذاکرات خوب بود و قبل از شروع مراحل اولیه مناطق آزمایشی، به مقدمات و توافقات بیشتری نیاز است. او ادعا می‌کند که این امر در روزهای آینده محقق خواهد شد. در همین حال، یک منبع لبنانی به تلویزیون قطری "الجزیره" گفت که "این جلسه با توافق بر سر دو منطقه آزمایشی، یکی اشغال شده توسط اسرائیل و دیگری در مجاورت مواضع آن، به پایان رسید. جلسه بعدی هیئت‌های نظامی لبنان و اسرائیل را گرد هم خواهد آورد. تاریخ و مکان هنوز مشخص نشده است."
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18211" target="_blank">📅 16:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18210">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">به علت پیام و سوالات شما لازم به ذکر است بررسی ها نشان میدهد هنوز هیچ رسانه یا شخص معتبری برکناری «علی جوادمردی» از بخش فارسی صدای آمریکای را تأیید نکرده. همچنین پیج اینستاگرام این شبکه همچنان او را فالو دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/18210" target="_blank">📅 16:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18209">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3meE42_-2DeRVu1YB92tuopgc8lhFNfsKaKcUEjF6TQCAYFPvQjdUUl_vvBfn-dzqHbnanoB7SNlERRq2hq281dRgFYuulAjydrZSDt29a5WXqYb14p3Krzr5yG7to__HLjuchEDWf-jrppvdY-gALSrTexffnSrkLbpvOQTI01vT6rAOaKqx_GEY2qyhLcsML7ADx9hWnqKRYKm-jA_hD_bKO6OmXvlrQciu83U_7e_hkbMUNXAZcHrVOwZ2PIaDrGl4cPpBhtYMHBupr5z6kKIPwBGKTmNjswTea45SfmyOGfZCoOApkD6tMhK66RsbyEPYfSXgLrqNXPScmiVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک سند در حال انتشار از وزارت امور خارجه عراق، که محتوای آن، طبق دستور وزارت خزانه‌داری آمریکا، حزب الله لبنان را به عنوان یک سازمان تروریستی طبقه‌بندی می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18209" target="_blank">📅 16:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18208">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رمضان رحیمی عضو کمیسیون آموزش: کنکور سراسری در صورت ادامه‌دار شدن تنش‌ها، به تعویق خواهد افتاد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18208" target="_blank">📅 16:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18207">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAUlKQrFZVl20zyYbLyxZ1E9UJT-SbXNCIUpuW4ZLiPR3Br2M9ZJzAgvv_exE0BnHtgXYREad4TfYsZ61deVGfGnWJtjzS8SzLjqj91hJ34rRI4v7LdIW0ad66XbB7rnRE9bQ95RbZxTwnIrTfdRYLVV--ajSRSgBueJeCLNHGLq03iM4afgiNxuUVJLeEzOxYCaKRIw0rkm4SboyEQTXYx0d-LM2W8ZCaknyN_50HPy5mIkA3KzCUQwsksZf0_72OAHRSslYd5KWj9HYkMnnDAZ0B35oS7d2DH4vuPY3awP7NDSLagfM_sDvCeZtU4pfpV6pp7ZCn6LJrIpCIP4uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور محمود احمدی نژاد در سفارت قطر برای عرض تسلیت
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18207" target="_blank">📅 16:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18206">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnjTuVvJ8PIbV4bk6qgs85xQzRJ_SXQJdnrxXq6Y9Y0VB801oWsIgWHCABDIn-sKeSYleT8v0vXDGHtHOKwI3njZPhzz6oJ_rkx9k7HewhSjVMD6c3F6bULWHDGYMkChJKS8imJ62RUG7xz4FTxBNjwHUgUW_0tuR4jr4KDIrZsHQ3O5wbMQmzmP3cVAhP7p8oHpK3ajPecaMLbBVnUBXprw0OQLqs4hwqu7IcKexqNy_G4xVv25YbX0eRfeFadm1Y_2iMBppLLT3Kmp4dGovdlOyHjpT_2QxBFyO3UhqoxTT-5Yj4NNBvKVR5xQLvvY812IXgS-lJY0m5ZtMm9shw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز معاونت آماد و پشتیبانی مرزبانی بوشهر و زدن
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18206" target="_blank">📅 16:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18205">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">فاکس نیوز: ایالات متحده صبح امروز به جزیره تنب بزرگ در خارج از تنگه هرمز حمله کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/18205" target="_blank">📅 16:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18204">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بر اساس گزارش رسانه i24NEWS، انتظار می‌رود دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز دوشنبه در واشنگتن دیدار کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18204" target="_blank">📅 15:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18203">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f16969a88.mp4?token=Dj-0rLIt4omNdovl5UOZdUyhRgj9BREWbvQZq_7-88VpBQwuAM9vWT_tIYWihsQ4Idrz2enoV7XZ94z32aO0xliqSvGvcZOMB2QCuuGFRTRtCT-MBgcAmYhvCOJfD82CtByqX3pXnbBdykvX9_1GHu7bLgagZvuYcCwOFdSdWeS6MdEUIk6JzHGJz6w9QoM4D27feJkQPgqpMwAyH7Ond_VVbR2WkDALFsGBuMtYhE4x3TkzjmNLAI2_PuJUAk_qewftRwVrDTxPmNZdimrwhAlwJgGhE2efz78oWXZrOXc_0Z2gdpQDdviZLQlHi1e51MRxgoWPVPBGNkF1XMQELQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f16969a88.mp4?token=Dj-0rLIt4omNdovl5UOZdUyhRgj9BREWbvQZq_7-88VpBQwuAM9vWT_tIYWihsQ4Idrz2enoV7XZ94z32aO0xliqSvGvcZOMB2QCuuGFRTRtCT-MBgcAmYhvCOJfD82CtByqX3pXnbBdykvX9_1GHu7bLgagZvuYcCwOFdSdWeS6MdEUIk6JzHGJz6w9QoM4D27feJkQPgqpMwAyH7Ond_VVbR2WkDALFsGBuMtYhE4x3TkzjmNLAI2_PuJUAk_qewftRwVrDTxPmNZdimrwhAlwJgGhE2efz78oWXZrOXc_0Z2gdpQDdviZLQlHi1e51MRxgoWPVPBGNkF1XMQELQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : سنتکام در طول موج ۹۰ دقیقه‌ای، مهمات دقیقی را علیه سیستم‌های دفاعی ساحلی و انبارها و محل‌های پرتاب موشک‌های کروز در جزیره تنب بزرگ شلیک کرد. این حملات، توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش کاهش داد.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18203" target="_blank">📅 15:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18202">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سنتکام: دور جدید حملات خود علیه ایران که از صبح چهارشنبه آغاز شد را تکمیل کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18202" target="_blank">📅 15:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18201">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ایسنا: سفر همزمان پزشکیان و عراقچی به قطر
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18201" target="_blank">📅 15:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18200">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رویترز: عربستان سعودی به ایالات متحده اجازه داده است از یک پایگاه هوایی در فاصله حدود ۷۰ کیلومتری مکه مکرمه در جنگ علیه ایران استفاده کند ، بدین ترتیب این شهر مقدس به سپر حفاظتی برای نیروهای آمریکایی تبدیل شده است
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18200" target="_blank">📅 15:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18199">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اتاق جنگ با یاشار  خبرنگار i24news:  به احتمال زیاد، این شخص که به عمان میرود وزیر امور خارجه ایران، عراقچی، است. @WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18199" target="_blank">📅 15:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18198">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fe4f78461.mp4?token=GmzEt_of0NTcDm7y2DGX4qkbK8U5mRtR-6fgNeJSSvQWoGnx3PKck4Y8glvm3eTunLA2EapOZScAW_Pq-98uajLQuXaXQcPsDTw8lk8e0ebHkxCyK_IKGrggeHdEUQfroke6j9kiWVvpb31p54YNA-8QA96c284jXPUbOqLaDUjo9ZDYCKnvoD4pHCpv2j6h77FQPJb8nNG8XHzqnec7aJ-0Kips837kMJKbAH52fPa5vy2wconBacO-2xmQtrfBmUTAa-QLrWL5aoW-8GpWZma2iRKB3AoI3Duj5-OBMveVXACN2F_c9Q3fGmi7W_4qpDdwN0uSPynFDSDgrGEs7Ge95OM61Cd66Qfpctkyt3wxWcaNUDQH7JrFDIYEl19PptKWTqSlacqpPqTvk90d2nZLKN4g-mFkrqwnCMohUrGR8fmF4ckHqUqWAkMm757A5IUtSHXz1AOhq9IIMy2xBDQG73kld5gGEXnD-VwFilyqPuJu2MUleXOptq851mx4NuVD4LwQ-N3iVXC0dwQtFCYpYC02NXwciZqeY7ZzQ7HK2GFW06jLN0WIlvHVVLJLmZDppMcMG6caZyQ_pGifqqe6p2iAwthULXqmCQ21CL0RQ3YCFlKXl0bSx9teqjZXjcvC1wHj4fl4-xrsbntF6Tt0f87vyl46q24Ht4EsCqk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fe4f78461.mp4?token=GmzEt_of0NTcDm7y2DGX4qkbK8U5mRtR-6fgNeJSSvQWoGnx3PKck4Y8glvm3eTunLA2EapOZScAW_Pq-98uajLQuXaXQcPsDTw8lk8e0ebHkxCyK_IKGrggeHdEUQfroke6j9kiWVvpb31p54YNA-8QA96c284jXPUbOqLaDUjo9ZDYCKnvoD4pHCpv2j6h77FQPJb8nNG8XHzqnec7aJ-0Kips837kMJKbAH52fPa5vy2wconBacO-2xmQtrfBmUTAa-QLrWL5aoW-8GpWZma2iRKB3AoI3Duj5-OBMveVXACN2F_c9Q3fGmi7W_4qpDdwN0uSPynFDSDgrGEs7Ge95OM61Cd66Qfpctkyt3wxWcaNUDQH7JrFDIYEl19PptKWTqSlacqpPqTvk90d2nZLKN4g-mFkrqwnCMohUrGR8fmF4ckHqUqWAkMm757A5IUtSHXz1AOhq9IIMy2xBDQG73kld5gGEXnD-VwFilyqPuJu2MUleXOptq851mx4NuVD4LwQ-N3iVXC0dwQtFCYpYC02NXwciZqeY7ZzQ7HK2GFW06jLN0WIlvHVVLJLmZDppMcMG6caZyQ_pGifqqe6p2iAwthULXqmCQ21CL0RQ3YCFlKXl0bSx9teqjZXjcvC1wHj4fl4-xrsbntF6Tt0f87vyl46q24Ht4EsCqk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار
خبرنگار i24news:
به احتمال زیاد، این شخص که به عمان میرود وزیر امور خارجه ایران، عراقچی، است.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18198" target="_blank">📅 15:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18197">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">کانال ۱۴ اسرائیل: منابع آمریکایی از تشدید جدی تنش‌ها در منازعه با ایران خبر می‌دهند.
دونالد ترامپ، جلسه فوق‌العاده‌ای با حضور مقامات ارشد برگزار کرد. محور این گفتگوها، عملیات گسترده‌ای بود که هدف آن، پایگاه‌هایی در تهران و سایر شهرهای بزرگ ایران است.عملیات‌های نظامی قبلی، به طور خاص، بنادر جنوبی ایران را هدف قرار داده بودند.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18197" target="_blank">📅 15:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18196">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18196" target="_blank">📅 14:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18195">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qjv-aYztWIyF9MFLz625_wMSe4GauR80ePlYZIOUbrsJNx07Z3VRvdWmt1Gg8i1PJj6OQYk1LXuTD5AAt1z4JC48NLUNSttNSnKMvIt4RZJvtwIBvO3MnqNkg_T-OxFw0FpGYcnaosIxovm7hM8vOOqEbwBYyhV3wF6X7nm735VYrdV9_dNYDXA_9imkI4sWTkWF0Yjm1iEn9HsAAdpNHLbpwTldY_gUKlWoPn0qh718HE3djL7uQuwyneeJ9ZpUCGXbpw_6Hu259FMB9yc6RbpvCpvAdsaVD6IZPNAuDzpEPtBKax0IN9BMlepnoVrDKCUOYB2O_vD6WyVGFrv7Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنوب ایران دوباره باید تصویر بالا بشه و تا آخرین لحظه میجنگم براش هر حرفی‌هم که بخورم
🫱🏼‍🫲🏽
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18195" target="_blank">📅 14:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18194">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18194" target="_blank">📅 14:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18193">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U77xgDbuWVFsCviUEIxcBkjM36FxAfajzawcglz6MsDDxFDKCHSu8Mt9e_SXyQgqB_O_WNV74LABHXkej-RCO8kaMM0H96bAHiUoJcKSPniXOvFLEEA06VGUTlh8GyugG_edb4r8ZC3_tjH2S7dWZms1v_6bN6wl0qEtLxFW77T3Kh6Wb3KclGi7SyKtmnRrBxJZFyvxNQ0viA1I8O0vdX8GcAqqhtOvdDZLAS13PK96TVHghlo5wD-rOTozbDFtrK9ObWFgn1p7yy--T_gMsNducGPWjDW6x_AbwAI_Cs2tT_7oA9yd1MyAUA0iH82_tiKCsPyZ_tII3qo0W3AZ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعاتی قبل، دارلین گراهام، خواهر لیندسی گراهام به عنوان سناتور کارولینای جنوبی ادای سوگند کرد.
@WarRoom
اتاق جنگ با یاشار : دست خدا عیان شد , لیندسی گراهام جوان شد.</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18193" target="_blank">📅 14:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18192">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پایگاه هوای بندر عباس ۷ انفجارررررر
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18192" target="_blank">📅 14:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18191">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">انفجار مجدد شیراز ، سیمانش حرف نداره شرکت چیه حالا اسمش بخریم ازش
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18191" target="_blank">📅 14:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18190">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f48130660b.mp4?token=Osa72NoxBjvLwrrhUuVSdKkUeAU-F6eRFiERwCVrf9abSAJ8VNHRYIOFleKxpD7igVN8b0b1dtRpxYGTg9El1MFEiqpd-ogad49AHKiSwRyEu7ddELo6iI71pQVX25OTlYnmAg0UTjAUyihVrCCgYr197VW1vcWWtc8ZsAEjQLfnPD3OnDAoP-TSD0dklOjzuNVo4is5-VD4aigpKb-oFr9CjkOdlNuwoT7jWLPyPEa_NToZ__oQ8dEmeBRs4K7gveRFtgX6UMo7n6KP_kwk1VNSm8Yp-jAYy-4Wq0PuNbJH4J378zRFFH8NpcrA8Ecy4yd7_Z2bb-Wdt5UsbTjB1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f48130660b.mp4?token=Osa72NoxBjvLwrrhUuVSdKkUeAU-F6eRFiERwCVrf9abSAJ8VNHRYIOFleKxpD7igVN8b0b1dtRpxYGTg9El1MFEiqpd-ogad49AHKiSwRyEu7ddELo6iI71pQVX25OTlYnmAg0UTjAUyihVrCCgYr197VW1vcWWtc8ZsAEjQLfnPD3OnDAoP-TSD0dklOjzuNVo4is5-VD4aigpKb-oFr9CjkOdlNuwoT7jWLPyPEa_NToZ__oQ8dEmeBRs4K7gveRFtgX6UMo7n6KP_kwk1VNSm8Yp-jAYy-4Wq0PuNbJH4J378zRFFH8NpcrA8Ecy4yd7_Z2bb-Wdt5UsbTjB1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@WarRoom
😾</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18190" target="_blank">📅 14:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18189">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIKERDg1Q9BExuM8_ICV0G-UeQj74Qkvxasjgq4Cbca9fS8Mvf9AtJpX_0hzXkfru-lTXpQ6OKfAOiJ6ydJm3do1dRbK79dSVROjPOBq7jhrfeKYdNlrv7BaAp8dwUyyahyXAtUtmuxViSpLBX3bjuTfcem-HM09Xr_UwU8d-TlDPTiSdS4kUq_-BQ3_R4uwEka5Fuo-in3xj4TFtiZb0_NRcP7QjFByZBI5Y1PbQMzCXJ40UolKMF7t7ErDEzlR3WW9zuYKf941KOvHpKlC1WzA6HCJDW75Eq3JqehuXJIiAzo_w7UZB07RyEKK7e5PBI2MR87Pxn6xPYF0ZwIM3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه‌داری آمریکا از ضرب سکه طلایی جدید یک دلاری با تصویر ترامپ خبر داد
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18189" target="_blank">📅 14:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18188">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18188" target="_blank">📅 14:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18187">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تعویق ۲ امتحان نهایی پایۀ دوازدهم در ۴ استان
صداوسیما: وزارت آموزش‌وپرورش اعلام کرد امتحانات نهایی تمامی رشته‌های تحصیلی پایه دوازدهم در استان‌های هرمزگان، بوشهر، خوزستان و سیستان‌وبلوچستان در روزهای پنجشنبه ۲۵ تیر و شنبه ۲۷ تیر برگزار نخواهد شد.
زمان جدید برگزاری این آزمون‌ها در این ۴ استان متعاقباً اطلاع‌رسانی خواهد شد.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18187" target="_blank">📅 14:11 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
