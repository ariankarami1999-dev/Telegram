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
<img src="https://cdn4.telesco.pe/file/fwAIGGuUyr19DpP8ZxXKagIbAw8cWsl44E5wdiTwfIFoE6r4hXv_9ik1Jq9BOwf91U-rCdLeWxF1je8Wr1UkYJGyYPvm96ffEujg3MJtBzoHofrl6--rOeLYKzv9TWLy5pcUFaJ2h4lWC8hRMeWuZ4FNpcZrWGbwqOenSTOntuggxezyUJtdTHI4FlTiyLRMvqVYXjT9VLnTh8UsVbfvomAC2C_KFsbJT3ySamGa1fTGtSzvihm5fWD5d5n2U1MTfMLxFcfxpYCnqzNfsbQBxIsOWxxyef5XG7WdLy4aSvy5nNnpt6BJ-gyyK4QM0EAOjKNlmuCnrLaIcJRLLEpp9w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 623K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-28 21:50:23</div>
<hr>

<div class="tg-post" id="msg-28083">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lC5eskZ-B7bTx9iUbxkUOgkGC5i9pY1HdVyCe5JtWrr52WXrTsMLfZqtpyvSPzY4bCX1oE4UC9IzWQ4Be6VCVOTq41g9lva-2RwRKS8Mj112tkzAxx9i71xTPQE5qa-OEU8VP1kbVbVKGFgk3fOhO6LcKS9pnT2WKRN-ubmVlMyyxKfYeYkNfE2KaJL4eXo_ADEsPXYtxIGQwSXEUfuVxIe5WKSrxVkaqYR_PojzreuTwXHEyZwuEwvMBU_KAtfF81g78Jk-FO77BAuJU7WxNfmHxUuOR9JKFNCfiDOcF3vfB0WGi78bST3crwahoNAXsLn0VOjddOqjPvlT2HoZsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔴
🇮🇷
#تکمیلی؛درخصوص محمد قربانی تا این لحظه باشگاه‌الوحده‌راضی‌نشده رقم رضایت نامه این بازیکن رو از 1.2میلیون‌یورو کمتر کنه و همین باعث شد تا سرخ‌پوشان پیگیر جذب دهقان شوند. اگه طی ساعات آینده اتفاق خاصی رخ بده پوشش میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7 · <a href="https://t.me/persiana_Soccer/28083" target="_blank">📅 21:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28082">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6602afdddb.mp4?token=k4TJi4R0WYFkv6fX_v7Hw003xHbcTZl5_y6Zum3P1FAxdUOOHOvN9AiF6ZIqmBzVaSMmNwrerMilewd19tKRzLp8PgA9_sZ55XosrPtlVw6uC99N1rUyBKU2hVi-56JvGNPxfm3oCkWwNho72NJSCgkG_SwZODBw3O0svBrVVf9gsoQdcC6CBj-GjCYZBxUrC9vZFPw6C_Zc_Ed6CbwAbs98D61QHvD8rpdob56TDejXP-vg6ril9oIye6ZQcjP-MseCP6n4QyCRt6-sF4hDZzyhS6y4LsQTEk1Xu5mFyEOEdR_O7rQSwKPWf-RTBq-DCWr33ZlXIPN-Lp282Dya1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6602afdddb.mp4?token=k4TJi4R0WYFkv6fX_v7Hw003xHbcTZl5_y6Zum3P1FAxdUOOHOvN9AiF6ZIqmBzVaSMmNwrerMilewd19tKRzLp8PgA9_sZ55XosrPtlVw6uC99N1rUyBKU2hVi-56JvGNPxfm3oCkWwNho72NJSCgkG_SwZODBw3O0svBrVVf9gsoQdcC6CBj-GjCYZBxUrC9vZFPw6C_Zc_Ed6CbwAbs98D61QHvD8rpdob56TDejXP-vg6ril9oIye6ZQcjP-MseCP6n4QyCRt6-sF4hDZzyhS6y4LsQTEk1Xu5mFyEOEdR_O7rQSwKPWf-RTBq-DCWr33ZlXIPN-Lp282Dya1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛جدال‌پرسپولیس با آبی‌های خوزستان و مصاف‌بارسا و الاهلی در جام خوان گمپر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/persiana_Soccer/28082" target="_blank">📅 21:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28081">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRYcZc8XFYX5VX50K4988AbyFT9Kfir-_clzBZrvKE7ozi9AO2cuaUOXQHfrNs-m0Wd-rVLwb38xYpWMnIrTtgBMldOTIpwONE4f8MA32HmyrX_O_7Xf5SpAnddLOoZukPPpCd4BkjbIzlD92KjkfvmyxudvEwOPQy3H73tsek0fTBfVYMiwoh9GGwIeLBwThKAMEJr7Z9lnD80ILRfy6f4LHd2BSgKLEZbt25uxKjBZDUKM9cYncTCs1MPGdHwenF-BkdwvKtNsfOylR-5wwNzUIgAgE_ZadcB3_TPgHgooJccAwWBv5n0suU8l0EW5M70Zi4NqsVyELee0CP_3dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌برتر؛ دومین پیروزی قاطعانه سرخ پوشان در فصل جدید با درخشش علی علیپور؛ تارتار باپیروزی خانگی به استقبال جواد نکونام رفت.
🔴
پرسپولیس
4️⃣
-
1️⃣
استقلال خوزستان
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/28081" target="_blank">📅 21:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28080">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfIff1HNdW2EcMMEhN8tj4ZOgyifq_xYI6lENExOomxFvE_oyMfrHjO-sVWMdLcFF8K51adu_Gc7lRHfdJMa5n5AwIINq8oaRyOH5A-_5RHBXRxgoMwT0IACwHKR8prqlSs525M67AH3buhyMQ81WBY3Cdjp5yn3NHX8amx7i_MXZlzDJ52xbC36Dv5rfaFcXff5LaBBQO6A7czhLRxI2tZYl82EA_OeTe58z_DgXTFJ_0BhlF5aYYj8qaAXArrGBuuX39pyQ4RkYioH2lk2Tebv_ppvh2tEAjXYNQJMyBrs4xHrPv1Iz4BH6jf6QUb89-hNYilvGFBf73BFs72uuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌برتر؛ دومین پیروزی قاطعانه سرخ پوشان در فصل جدید با درخشش علی علیپور؛ تارتار باپیروزی خانگی به استقبال جواد نکونام رفت.
🔴
پرسپولیس
4️⃣
-
1️⃣
استقلال خوزستان
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/28080" target="_blank">📅 21:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28079">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhL6Y9KcnmcTyWe_5ruEIZiuefyyFR_lfcafEavYTJINRjLh4B4Qi8ja1vSU7Yje60o0TzwNsGiyjMvp6_CC8DkJ6U2zLzt4gtAAqV1Ljf6COmCBFl5IwrKICO6oD1fshpZNpJQ5XzUNzicWmmapqlklm3SBSylqQ79wT_qFSS47dK9SgrDdiXZq-gYjYQANVAdCxFlSpVnzWmau_-5OQNLJ8HTg15-0kC-HhBkQHvjbKzmQNqIRIXEVnwphOh0XrjYFS2Z3uJRzapSWduMlOVvI1juNxNeN-c1he-CnNBApK0gl_Nx_CXRRTIGoJwFv80vq_UtPJi9c5jltDaYe_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کلین شیت نیازمند در دومین بازی خراب شد! گل اول اس. خوزستان به پرسپولیس در دقیقه 64 بازی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/persiana_Soccer/28079" target="_blank">📅 21:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28078">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f0b34890.mp4?token=V3RCsok-d-PxgKIPpiBC2ixL6PT7fDzNQmX5vpKbBEkf1hIaNX8O5ZaHKJok347wq-Q6ImTuo3as_pARTZjd_2UB_j8K2iVJte70Yp0A_i6TN_CcTE3yOYLgzwNc65DyG-4dXYfemok7Bok0iRb4My4IpGw63k0qttZ3PAcl7t9njUl0XHupQSIyiBAVS1cRij8fYfVQKCg4uTeAQ9TpsfsRk-X5H4KBepuBx1ZQJPikJly2XqUWdXposNaqvOpbSnSRbfIxkMeXX3Gr_9BOmumMwmqKd2WZ5MeasFqKJzu0SG5rmSF9Y9W9DQH7MuPb5ZVCfXFxyHTRzi7PoAhsrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f0b34890.mp4?token=V3RCsok-d-PxgKIPpiBC2ixL6PT7fDzNQmX5vpKbBEkf1hIaNX8O5ZaHKJok347wq-Q6ImTuo3as_pARTZjd_2UB_j8K2iVJte70Yp0A_i6TN_CcTE3yOYLgzwNc65DyG-4dXYfemok7Bok0iRb4My4IpGw63k0qttZ3PAcl7t9njUl0XHupQSIyiBAVS1cRij8fYfVQKCg4uTeAQ9TpsfsRk-X5H4KBepuBx1ZQJPikJly2XqUWdXposNaqvOpbSnSRbfIxkMeXX3Gr_9BOmumMwmqKd2WZ5MeasFqKJzu0SG5rmSF9Y9W9DQH7MuPb5ZVCfXFxyHTRzi7PoAhsrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلین شیت نیازمند در دومین بازی خراب شد! گل اول اس. خوزستان به پرسپولیس در دقیقه 64 بازی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/28078" target="_blank">📅 21:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28077">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIuUnosxA8-ZYiRE-b-lADhWQqbT-nDJ2HV-YCCeLrQTm1bQtYRo2DGmm2SNVc0eIuGSniZFTMI6pzYelEJi4gnl4URAL0ZHBSbJ1zAK6Q_0RyDa1g3ZMFLSrb6FzBYqyexT0UfH2ZrRpeQhNcoRFLmLeY_jS12vCr7VUi0h_cgdtX7mO4mbIh_MBeEt902ZVngxeNgIxPI96QodHAtCBMHWIMKmUMVqiarITLe9mFB_H0M8N10fU1cpBNIBOUeqqUasXsYKuDEaCJvUQM3ykT2fYoqPUZtJ5bSlwHFcMUSSx-61oOiMJnl1EGauI9LXqc92pVIe8fBhQe8A_7Wksw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیویی‌ازگل‌های تماشایی رودری هرناندز ستاره جدید بارسا در دوران حضورش در منچسترسیتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/persiana_Soccer/28077" target="_blank">📅 21:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28076">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecb9a3fa5f.mp4?token=pRDqsmbZXO5feWw-cdc_5-3HMZc4axeVu7RQ0eQlhULz51KsCgIW76N010i81gio3nySuR_vfRAliYSQz02m6eDZBUuywDOUv2Ndd5lVXwf4fAgCzX7kJRtZ64-mFJxLl4zVIrx1YqxU9I-f6SF9frpMY4MEEMWPdT21dcGLvj6sVgFcgPCHkYbwXctP6prKy2QNV7EpvLtSUoAzbYnDRYL2crH1UAzdrgiPkzmejg8uYrcch7k0KDgSCV3GvJxnD3Bp-A_y7s69xacBm1e_Wf-HUsLbCxqMe_liIvtNm4Yic1BQZ1DHWfirsviFDoqKs5vhNr-3yQnphsAtdNfVwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecb9a3fa5f.mp4?token=pRDqsmbZXO5feWw-cdc_5-3HMZc4axeVu7RQ0eQlhULz51KsCgIW76N010i81gio3nySuR_vfRAliYSQz02m6eDZBUuywDOUv2Ndd5lVXwf4fAgCzX7kJRtZ64-mFJxLl4zVIrx1YqxU9I-f6SF9frpMY4MEEMWPdT21dcGLvj6sVgFcgPCHkYbwXctP6prKy2QNV7EpvLtSUoAzbYnDRYL2crH1UAzdrgiPkzmejg8uYrcch7k0KDgSCV3GvJxnD3Bp-A_y7s69xacBm1e_Wf-HUsLbCxqMe_liIvtNm4Yic1BQZ1DHWfirsviFDoqKs5vhNr-3yQnphsAtdNfVwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل سوم پرسپولیس به استقلال خوزستان توسط ایگور سرگیف '48 روی پاس هوشمندانه علی علیپور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/persiana_Soccer/28076" target="_blank">📅 21:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28075">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ef87ad1f3.mp4?token=t_sSocNT8Fpb3ouPk5XhyvjxmENr2WZ9bKxTCBERHYu1TiSLpDi4bt_eGQNcMuAIgeOA_WbT83uurfR01vnLbvgXvxnrfK562KST0y0VGSzEDmN9spwNUSS30Yc8bj2u1XopOxxbO8Ps6f9_aoguqtgChXuwOrU7h76uIXcLDeVMcLTISuP464deMkwtx15E0trG53DPTqF8MCsaN3IXI2mvpvPvEQM3wugXTdQZ0CgxQeMkdt6XnjS6bNVIZJ6mw7TgGu6bDYHqrXBb3JR7uTKclhYu9ulOfh-UT0EkVF_aesVgwywOjYpBkVMAyUdtvEI_YxWqRP3WFlXLpqOiIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ef87ad1f3.mp4?token=t_sSocNT8Fpb3ouPk5XhyvjxmENr2WZ9bKxTCBERHYu1TiSLpDi4bt_eGQNcMuAIgeOA_WbT83uurfR01vnLbvgXvxnrfK562KST0y0VGSzEDmN9spwNUSS30Yc8bj2u1XopOxxbO8Ps6f9_aoguqtgChXuwOrU7h76uIXcLDeVMcLTISuP464deMkwtx15E0trG53DPTqF8MCsaN3IXI2mvpvPvEQM3wugXTdQZ0CgxQeMkdt6XnjS6bNVIZJ6mw7TgGu6bDYHqrXBb3JR7uTKclhYu9ulOfh-UT0EkVF_aesVgwywOjYpBkVMAyUdtvEI_YxWqRP3WFlXLpqOiIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به اس. خوزستان توسط علی علیپور در دقیقه 20 روی پاس مجید عیدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/persiana_Soccer/28075" target="_blank">📅 20:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28074">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51f80a1480.mp4?token=Wta-wOvvWRHc7EcV0NqjeXMzhUJ95gCcffVa2FmGmnfWU9I8YuBnCrs9QZvr3cads2PRHVOw1z1QlqkUHpnOhAac1Ao5a7BG-NKaY9r6AakNOodmXhFtyS4RNH-uwPLRSllLFfP7K8mDgRlFRTSW109fyvHvVg75Ah1ltNjz8Esa_z84Xpvv8YRqHbDiDETkq7lmofUOPmrqFoMTwYFC8cQhBUEsrnpwhldEGZ2RXnXyL9YGcNX_IX03QwunhT5u-s779_7lETyBaHitJvozyUGMwqtcWVRnysfggQUp0ZLOTbjXQQFUbA3v_cR4kDLxn4H0EBHQDr7lGaHabzlD1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51f80a1480.mp4?token=Wta-wOvvWRHc7EcV0NqjeXMzhUJ95gCcffVa2FmGmnfWU9I8YuBnCrs9QZvr3cads2PRHVOw1z1QlqkUHpnOhAac1Ao5a7BG-NKaY9r6AakNOodmXhFtyS4RNH-uwPLRSllLFfP7K8mDgRlFRTSW109fyvHvVg75Ah1ltNjz8Esa_z84Xpvv8YRqHbDiDETkq7lmofUOPmrqFoMTwYFC8cQhBUEsrnpwhldEGZ2RXnXyL9YGcNX_IX03QwunhT5u-s779_7lETyBaHitJvozyUGMwqtcWVRnysfggQUp0ZLOTbjXQQFUbA3v_cR4kDLxn4H0EBHQDr7lGaHabzlD1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعداز منتفی‌شدن حضور مرتضی پور علی گنجی در باشگاه الطلبه عراق؛ رسانه‌های عراقی خبر از آغاز مذاکرات این باشگاه با سیاوش یزدانی مدافع میانی سابق استقلال و سپاهان میدهند. یزدانی از طرفی هم‌پیشنهاد تمدید قرارداد از گل‌گهر دریافت کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/28074" target="_blank">📅 20:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28073">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxgM-20V_PK1bbl5NftOGXgn58JAyFVmb0DoZU6Tij5uJtp-a62NUuhSxB8AsAnTrqCV45PAmx9G1F2VphD8Dm6nS7i6CQiqWYXX_olI3HiOoidcbNDXWlls4xLl-JOi8WLHZPEiGWmyR1q5hxtdofC1iCYBJkIDGunpzXfcyO0TWzWxhOglvWaWMPXxonbCdPqHdEdOCqj1oTDbnHoTvm3_0_rlHqwRIjtgt01-5E4M4O5J0PSYSA1_A7XN-4lOUdyFmRy931Jomt6Mxydqih_iowXCMUQU1kuBocOkZyimY44CU-lRy9tSPjH4W0hWZmCEC91kvhcLvIBg_4zSAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درآستانه‌دیدارحساس باتراکتور؛ ابوالفضل جلالی از ناحیه کشاله ران مصدوم شد و فردا بعد از گرفتن MRI میزان مصدومیت او مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/28073" target="_blank">📅 20:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28072">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67aba5f2ad.mp4?token=T_VytIvIkz57d7TZCDmsNGodXK18pu4dyWzJR-hEskNC-YEZ16iUU_ZQgxqDdGnsye2WoAkYyXxK_ZBiwGjkELToyEyrVdBm1ynI0R8GOayWrlDpPvIG7XTKwLuWPsytK-bvNOJQnzUt4Gxra4vdgPAYCu6aBpK49rVIgBp8Rf6PHM4uaWE7Zot9bhdkgOXc5102AIdIJO_yBxGJ0wo2mn1EOXe1FGFCbM-Gx-C2JiwhThChhGiUX8SRbqYXY9eOoG_OkSWNiLixUZzwCwpM3buHzcDy2sI7G47njF7VJU6p5FWXfg4-to1VnQx9pIZZXSoOEA6XMdIsnTfiDodg_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67aba5f2ad.mp4?token=T_VytIvIkz57d7TZCDmsNGodXK18pu4dyWzJR-hEskNC-YEZ16iUU_ZQgxqDdGnsye2WoAkYyXxK_ZBiwGjkELToyEyrVdBm1ynI0R8GOayWrlDpPvIG7XTKwLuWPsytK-bvNOJQnzUt4Gxra4vdgPAYCu6aBpK49rVIgBp8Rf6PHM4uaWE7Zot9bhdkgOXc5102AIdIJO_yBxGJ0wo2mn1EOXe1FGFCbM-Gx-C2JiwhThChhGiUX8SRbqYXY9eOoG_OkSWNiLixUZzwCwpM3buHzcDy2sI7G47njF7VJU6p5FWXfg4-to1VnQx9pIZZXSoOEA6XMdIsnTfiDodg_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
👤
رامین‌رضاییان ستاره‌فولاد بعداز پیوستن به این‌تیم با استایل بالنسیاگا کنار این تیم حاضر شد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/28072" target="_blank">📅 20:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28071">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJLA51evo3TvCkSx7FoJyMxRTaDNorJNOcRCMKXvS7up4yD7MRr5B3uoZKmtW0yaqvtXXly-wjvmDNqe_6kUx_mswhYvrlXeYXZnKzq2vJIJ_O59qgHNrMSuPsdKVXjeBXec0-2FJTbSg6WICzNDIgXdYdTerAcQfn8GGqycIvwqALPIU5d6BNTMWVq3h0-unNTUiWUn8lqR_rNrSFCGQ0NP09q2k7CGQWi3Wo-oZXIBya969-1ERS0rp-AeJbCeBE12-R9a1FwBIMj_zJU_MwKzqhlZl31i_jUy2SJ6z1pTSWIFDWWi9SFqrdf63WVnK6Zyk33nlDp5bPY3WUdowQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به اس. خوزستان توسط علی علیپور در دقیقه 20 روی پاس مجید عیدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/28071" target="_blank">📅 20:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28070">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYYWntip02tusMslyT_nD8YEM174wDez4IGhFLCSY9smpQc3WRxxmkNE3Hup8gz3vv7VNFFcg1sxUo-Bb5a6Fehbi2DGtOhDeThHEdMb2Ea3f6WcNTGKCoJl6kLQ4w30QrRi6IQC9dIjldf7aYTh03YkosCQIAObkDJX9Mes8n4Gx3-TvY-eSROUuUHVKn6nTO4JDUUmeYY9GYKCnGVzEqoPLiJZ0Bzby2_XJ8NIDdnZTQh_4cJw3_DyTr3fDBrMMnCdN2g1TLi7bCHiAbKRkmDavOJ3l8KF2MGVOwcYDmB7k8Bn2TetP4A1oGb3JR96K45lHARxAvW3-KjAsdMQ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درآستانه‌دیدارحساس باتراکتور؛ ابوالفضل جلالی از ناحیه کشاله ران مصدوم شد و فردا بعد از گرفتن MRI میزان مصدومیت او مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/28070" target="_blank">📅 20:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28069">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b5b577f54.mp4?token=A89M2doZnaNjttcaaw8tTx5FYI86ZoQ0SI9jHMEp70yRfrWPExEd6D9Mh28XnjfnAp5kyHkAxq9JCfUq2Zb_h5P9DBbo4KoQUSEJuIc0MO4hjeaYUG--zkvuFeEDC0eRUDI0rV8Lr-PrUM3-yjIPJYEIN9u2hov2IzPfIdeWtKFmnR-w3Kco6VyQOxyDNT45g3MYKpzkP3_Ba08bPsbJeowOCuNZ2ohb2rqDDOx_ktahvC8DFAvlTFYewzNJ-Uk6SwsdajPXnatlia8kUAi0Zlvl8_QJbE0nNldjYJ3Hg3WK_s2yDHerf1fRatRnt2V17POWZQpI2xl7W-6q_JHV_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b5b577f54.mp4?token=A89M2doZnaNjttcaaw8tTx5FYI86ZoQ0SI9jHMEp70yRfrWPExEd6D9Mh28XnjfnAp5kyHkAxq9JCfUq2Zb_h5P9DBbo4KoQUSEJuIc0MO4hjeaYUG--zkvuFeEDC0eRUDI0rV8Lr-PrUM3-yjIPJYEIN9u2hov2IzPfIdeWtKFmnR-w3Kco6VyQOxyDNT45g3MYKpzkP3_Ba08bPsbJeowOCuNZ2ohb2rqDDOx_ktahvC8DFAvlTFYewzNJ-Uk6SwsdajPXnatlia8kUAi0Zlvl8_QJbE0nNldjYJ3Hg3WK_s2yDHerf1fRatRnt2V17POWZQpI2xl7W-6q_JHV_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل اول پرسپولیس به اس. خوزستان توسط محمد خدابنده لو در دقیقه 6 روی پاس علی علیپور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/28069" target="_blank">📅 19:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28068">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f85915bad.mp4?token=K4JrG9q7_i7XVaIUOcZazONwrKdVctskELxqU4nUycM__hfBjsOuVY-i-8pJ7jbgz_qS0E8xOnE-R1IJZPlkspg_ZBt9v7NHcT1NOxuwQHPvbX7qSz-puc07bzsQWZLp9ba9JF-HI6PgfFIsLL80Rg2W49yqVT0HTLJUfDsGaqPRRmdndYzZ0KGUFySIx-MyX_b_Gs0p3aHPP1Ho4MkeFU1P9O5oE4OjvqjOQ4-TOxScWUnIRzyWp3l25bd-ZTQhdvGrh2mwIb-r_LLNBZNPaLvwdKpaITNd3R6hrGDR2AihLHbL1hbmPjV-h2vVMarDgE4xykzz0o8d0BfigxT8sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f85915bad.mp4?token=K4JrG9q7_i7XVaIUOcZazONwrKdVctskELxqU4nUycM__hfBjsOuVY-i-8pJ7jbgz_qS0E8xOnE-R1IJZPlkspg_ZBt9v7NHcT1NOxuwQHPvbX7qSz-puc07bzsQWZLp9ba9JF-HI6PgfFIsLL80Rg2W49yqVT0HTLJUfDsGaqPRRmdndYzZ0KGUFySIx-MyX_b_Gs0p3aHPP1Ho4MkeFU1P9O5oE4OjvqjOQ4-TOxScWUnIRzyWp3l25bd-ZTQhdvGrh2mwIb-r_LLNBZNPaLvwdKpaITNd3R6hrGDR2AihLHbL1hbmPjV-h2vVMarDgE4xykzz0o8d0BfigxT8sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
شماتیک‌ترکیب‌پرسپولیس‌برای دیدار امشب با استقلال خوزستان در هفته دوم لیگ برتر؛ تارتار کاری کرده که هرترکیبی از شب قبل منتشر میشه اشتباهه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/28068" target="_blank">📅 19:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28067">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/568f2b5232.mp4?token=H2cXRMS51iY36ekBg8m45XG-4wiHAK7HIi9_8ieUwJZ9l1MY6sjPB7WrIUp292oBRHTmPWoiWeNrklW5zvWByKqmbI6qyNjLFG1vs1vLJgehcYMC46-W-G0ieCtVLy9drE9L4ANJBZc14DGyiGhrbLhGPWN-hr7dT891_-MYgJgrYtYJi-dapnbCjl1Vy_t85eOnoqbgJoUN6gd0cWLoTAWaCElKd14ggiBU8Mk_9lyiT-hRTTIz2-bw63C-fwL4DjGXSd0pHnVBeRO9wAkVtwGRzU2G8KMGYCW0M0d8HYkr7GuFpN3WBFlmgEEf0RQrjsQGrCQ5ckLVpnKJH2hnHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/568f2b5232.mp4?token=H2cXRMS51iY36ekBg8m45XG-4wiHAK7HIi9_8ieUwJZ9l1MY6sjPB7WrIUp292oBRHTmPWoiWeNrklW5zvWByKqmbI6qyNjLFG1vs1vLJgehcYMC46-W-G0ieCtVLy9drE9L4ANJBZc14DGyiGhrbLhGPWN-hr7dT891_-MYgJgrYtYJi-dapnbCjl1Vy_t85eOnoqbgJoUN6gd0cWLoTAWaCElKd14ggiBU8Mk_9lyiT-hRTTIz2-bw63C-fwL4DjGXSd0pHnVBeRO9wAkVtwGRzU2G8KMGYCW0M0d8HYkr7GuFpN3WBFlmgEEf0RQrjsQGrCQ5ckLVpnKJH2hnHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
کریستیانو رونالدو و جورجینا رودریگز در اتاق نشیمن خانه‌شان ازدواج کردند!
🔴
هفته‌ ها بود که اینترنت پر از گمانه‌زنی بود درباره تاریخ، مکان و لیست مهمان‌ها. از جمله مهمانان مشهور شایعه‌شده از فردیناند تا ریحانا بودند. در نهایت، عروسی این زوج در یک تاریخ برگزار…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/28067" target="_blank">📅 19:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28066">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AN2soJ5ZAfQvoKZv1omLVbOc7NCUES7Ukvlzkfu_N5_b8eDetMLFb7t5qYwza1boPGEQPIDqadGjaXua_Mmi1tj3HRZ2w8c8guYPaKDXTwcFNOVPvcIQCYcWlY_rQfm-DE29WntEtUR6RDsQ7r4tMumeBfqWWPrB9Vf1JwdQok_C2-yABsA7nQQZBrDlXfppfYW-nwjfVBQtjEc7qLt2x7uDQPbxV6gvHTU8JSDdCDtvBWQxv_zwCCq4L7t4pZpoZEanq2H_N1pkJFhGApb46yFwFYhBokwK6yXEQqqYU10IpFTZLd9R6BMHj2LMZfnO7a025AjJKcgQENLqRgJReg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#اختصاصی‌پرشیانا #فوری؛ پاسخ‌ منفی ستاره سابق‌بارسا به‌تراکتور:برگردم اولویتم استقلال‌ست.
‼️
منیر الحدادی شب گذشته از طریق مدیربر نامه‌ های ایرانی خود به باشگاه‌تراکتور اعلام کرده باتوجه به‌شرایط منطقه و مخالفت همسرش فعلا برنامه ای برای بازگشت به ایران ندارد…</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/28066" target="_blank">📅 19:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28064">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oGkBhrD1FIjNDeAdHi96gT08aVc7c7YkKXNNACag6aK5Gm3VkgJyMoQh6zB1C_zc-9xeIAAyBbwND1cE2FnYEDTz7th3RTchz-5TczgJ3WqdwdAps8EIw_dsrAmXB0zHuEZanRCscLTyvAHLBWdQcps3gSH2zq9oSY9Iu7-y4OVNW3nbkBb18kgtqUWd5uMBQKwTaFotu83JanrQIQYumLai_nlvMG2c293eGOAAQiPkA1gWZxYf9L12SHpc7xjprlaz-Iuyu9NxHqAkw9jgQvKM3ZoOtZJq0Gy5MKFtbklSWtBcCIdUIDxrzMLIID_SR3vKzF3Rj3PNfcYAF2hrdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ou1tpZQak8ax2QnnGyoAlkR_D22Bns0B6J42JXGivECKYyKAMFZaBEvsbaZTruvYHnxJFrtET2tR4A576OY0dRbC6MMsSIKCBd3Fj0hN6GvQVJ7tamJQvDczuUeGHJk_2SvBDeTYotS-D7_vhA3bFVYvOjmATbBBCj-YgtMUlENEiWGGu3iIOOE8W4YiUcLnZwuDFah2rY8NoEChhc-w6gJ3-waVYwLHhrPs2siQfIBCXjaU3jk80t4MtllPZOMF0HUXF9-S8TOC-VR1BIEk-KD8UOYNUvIMzezgnsKiAAnvjeXtlrhlPXg4vrFH2jUljAomyy8MLQhMHr4hohLV_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
صحبت‌های جالب پپ گواردیولا در رختکن پس از باخت ۲-۰ به یوونتوس، دو سال پیش:
بچه‌ها، می‌خوام الان یه چیزی اعتراف کنم. من از زیباترین زن این سیاره طلاق گرفتم، همسرم، همسرسابقم! عاشقش‌بودم‌دیوانه‌وار، ولی دیگه شور و شوقمون از بین رفت. عاشقشم؟ قطعا آره. اونم عاشقمه؟ آره، ولی شور و شوقمون تموم شد. فوتبال رو چطور بازی می‌کنین؟ فقط چون بازی می‌کنین، یا یه چیزی از درونتونه؟ تو زندگی‌تون، هر کاری که می‌خواین بکنین، با شور و شوق انجامش بدین. من بازیکن خوب نمی‌خوام، بازیکن با شور و شوق می‌خوام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/28064" target="_blank">📅 19:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28063">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbUbT_UXPALoGQUxYxMKdjKipRq1yGKoxsCrh-KGyMHcA-X7lLw7_lOCKhtyxl0NXDv9iyAkC4opXoQSOxd2HAC5K2yX4zG5fUWgvDoEWY0PPiXAzEF-STmMEVa38JiUqPEerZyimRL179rgaRVLBbPkHcmCNjYMru5uvTgQS8gs-B_7DC85HAPqQJCAYpC4ZFc7H7coEQK8Ly2Vr3ccQpJ8wB9id6kLOeaUJF4hY5dodgX_3v9kujy3OttsbCyeG1Vbj6ZRmHO8-v6qO-CopouVf7l8BkNG-kzcP17OjnQcMkWxezbLAMU51IA8dHD7Buzf8V45FtWCYZ_GMqdakw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵۰۰‌هزارتومن‌تخفیف‌خرید با اسنپ‌پی در شبکه‌های اجتماعی!
دیگه با اسنپ‌پی میتونی از بیشتر از ۴هزار فروشگاه و برند محبوب‌درشبکه‌های‌اجتماعی مثل اینستاگرام، بله و تلگرام، خرید کنی
و با درگاه پرداخت امن اسنپ‌پی هزینه‌ش رو در
۴قسط، بدون سود و کارمزد
پرداخت کنی.
با وارد کردن این کد تخفیف توی درگاه اسنپ‌پی، خریدت رو نهایی کن:
✨
کد تخفیف:PAY5SCMD
از طریق لینک زیر، لیست برندها رو ببین و با تخفیف و قسطی خرید کن:
https://l.snpy.ir/br9ej
https://l.snpy.ir/br9ej
https://l.snpy.ir/br9ej</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/28063" target="_blank">📅 19:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28062">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFvvplXgb2ZrpppnrvNFcJRc1Eo1kcK0KU9jXQryOQ6DEdPRLZ5gTxBT7CMicve1oyHrdd8BdZnPUmK4mnWjeRbFKtK2W1RBWkMi3tDzjhDZcj-TlaYXSNU2Jw7xzXToBwbnGsFXQVIYVaEvL6oBI311TJ8dlUiYKDU4vxgc_6zmroJJb5qkkH-nLyQKMQOd7Epea0SgWnRk8cnaxOSbS8F4i4RExKudhqG5HSJLCTjBxrQRCFUX4AjCoyCRLh1AclgWMCU7tdToQOj0pO7A11fel-IhZDVwZq9tIYVl5B0rlGmLDPSsPkCyfb3q1rJ9-QmqURNG4lAUD5egFdykAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/28062" target="_blank">📅 19:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28061">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCxNmRxHH75XIvm2UqbCNkvmabSblnWyDlqTqVRhX_qIgZeBPCIYAgzrXTuAPXfn4FqaBz8fm_jCTJHuxUUYCrJM5KjaYz9DZkPs2BGaum9rdnyYT2BAOnkksvNSvQWWIF9KPUuqA95CdUYMZ4OhZBkjOly4jpyEZAqc-uh8Hx8RigS6tG-Fw0d2Fq4D-lG5lRn-dJYgJdbMy-Z35gFw36EAwLG8C5qKdZAGjP53N_TyRr5MEbkUz40f719afEImqC4ulTp85gL_YDIz_VOjp1zQ0lh-7-RnOLSOEIWBKEMr_wDdT9aN9VH3VqWTDeMwNJXCX6AgOyMyhf7cA1ZmKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم لیگ برتر؛ ترکیب تیم پرسپولیس برای دیدار امشب مقابل اس. خوزستان؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/28061" target="_blank">📅 18:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28060">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngwdLQmjPOTksIvgsjfnvDVU_szUYSxr64rtAbO_vZsbe0Ybh3bwFPA2oTJ9Y0fT4wcoKOU9Yw4SM1t4gijxMU0GHwZFrXkvxmdPJqIb2xl8Z6wvKbJCPJ5dV9OmaBNJqw1qmGHlO_Z_ACKbUeyeVN5nAimQTjE_939XSUSSZXsJT2gnoLkAA_5cqUuESEoYRBIjqm4yY0EAz6POJJ_wHgVkzzVVoyAuqUNaBozZnPvwHzrhnXTB5vghmCq-hdiP0TE3PqgYAJRf9h_n8uOByc87VTyZsvCMH3jagOVnqqiGaMlg4h93JPVp2OAy9MqpTbE9ZcHXPhAHeCIzD-yimw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
طبق شنیده‌های رسانه پرشیانا؛ باشگاه گل گهر سیرجان به خواست مهدی رحمتی با ارسال نامه‌ای رسمی به باشگاه پرسپولیس خواستار جذب محمدحسین صادقی وینگر جوان سرخ‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/28060" target="_blank">📅 18:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28059">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_cfmdL6kvmWf5B4l0EAFm9lRfVfyGZTwzmu4NVi_otb_SUsateMf4i5Uqg6OrZ2U1bQTbXkQTefKi2lwW2ihwP7szGy5VLjT8lUJxs1dfknACqT-2ujKLqg_9tr9h3qv53piXDUIfcZbGIiib4be71uchuYbIfnHbAv5T0eAX-ReVRB122cfZlxcChhVuU9JY_akXQMdipS2LfuNTW7-0q41Tto2u9H29I7LCEUBryY_yWVPdrJhpZf22paLnMPAoKOCJUsTxu3opV2PQwQJGbAV6RagJ1NkA-qg3bZEePtsUtUHUwNMRD8hNkOUBmInCEUCVecPu7nl2v_vOkAHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج 5 دیداراخیردوتیم پرسپولیس
🆚
استقلال خوزستان به مناسبت بازی حساس امشب دو تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/28059" target="_blank">📅 18:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28058">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41809830d6.mp4?token=Ml6zQwhbf7ynJYIPQnbc83UWPBiCiCC2teD6h54DI_VT_5aYnrWZRDSc9pVm0bgwhNf5W1nKE2gMMrZo02JWVYU_Qq5eHwlt4mpBa2mviMP4OxQaHJYjlNu-fn_e6s1QwEbLZpuhaCYCDjoBdbAQdT6946u5-1wJpeQkIBdqXyvlGQWW29xAeZJq-pRp2PFoZIhFavf9oB8kwnsqprWPMPof_RLzFdaywqxoeSfsj9yYVJOVegh6Ms2vUk6YbbXVbPmresFhB5UP0zz2v5zJkSDYgxx9syfC7GBRGVYKLe-qV0gem-nnyKhdqoC-14t92K0cOQ_6JRnUN68g84-eFQUM30pz3yQp839o5eyM4-xQ-xJyZP9qIgc18-35QReBbknzeVQDAKSUZ-j0Y35vlw2btYXjv0WE62gMfgaD-DU7R0SK6w_ZBdG9Pr0_RCILx4FnL97LhnUV4u_4dhHdJUxSWYJlEPFGwcTy30ZdMlRMAf9zKQB45r0aNjBEGgSdsdhrAvAD0m9ItRWjvZ5SqTIxOliXACtWvo2fKLwY0JLHqMin_kQzVpq23yV20eywyiSyaFQzDPd6dwNEAyj40Rm8FGF_No6MQpOZZscWvb07nqI2JH0rU1t6qH5RClHkLCKHfgzOcw5C662k9XkymPHVrWQDIg7GXxDX2YNa8I8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41809830d6.mp4?token=Ml6zQwhbf7ynJYIPQnbc83UWPBiCiCC2teD6h54DI_VT_5aYnrWZRDSc9pVm0bgwhNf5W1nKE2gMMrZo02JWVYU_Qq5eHwlt4mpBa2mviMP4OxQaHJYjlNu-fn_e6s1QwEbLZpuhaCYCDjoBdbAQdT6946u5-1wJpeQkIBdqXyvlGQWW29xAeZJq-pRp2PFoZIhFavf9oB8kwnsqprWPMPof_RLzFdaywqxoeSfsj9yYVJOVegh6Ms2vUk6YbbXVbPmresFhB5UP0zz2v5zJkSDYgxx9syfC7GBRGVYKLe-qV0gem-nnyKhdqoC-14t92K0cOQ_6JRnUN68g84-eFQUM30pz3yQp839o5eyM4-xQ-xJyZP9qIgc18-35QReBbknzeVQDAKSUZ-j0Y35vlw2btYXjv0WE62gMfgaD-DU7R0SK6w_ZBdG9Pr0_RCILx4FnL97LhnUV4u_4dhHdJUxSWYJlEPFGwcTy30ZdMlRMAf9zKQB45r0aNjBEGgSdsdhrAvAD0m9ItRWjvZ5SqTIxOliXACtWvo2fKLwY0JLHqMin_kQzVpq23yV20eywyiSyaFQzDPd6dwNEAyj40Rm8FGF_No6MQpOZZscWvb07nqI2JH0rU1t6qH5RClHkLCKHfgzOcw5C662k9XkymPHVrWQDIg7GXxDX2YNa8I8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سم‌جدیدی‌که ازطریق هوش‌مصنوعی ساخته‌اند با حضور ارلینگ هالند، کیلیان امباپه، مسی، رونالدو و حضور افتخاری رامین رضاییان ستاره فولاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/28058" target="_blank">📅 18:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28057">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWaT2zntnMbf7R1-RWBzLslbaxnfwCFgX4oJctezMYvTyr2oapP6vRgxIHzHg5z44zy3aGDEomnY3EMGiijO-pQQKPt_QTzfBm_Stz39fRl-4YDgd91drrB6DRdj_mhjoYl2FKRCWXz8Rp2FdJHFPg0tvt1cojRR9x2auJX6DTKQDdjjK8KIKXZOWWUMsz86Bp2RtnSqVxVNf7VWFtDCJkSfMF6ZVrJRU47UBY62G9UgOj0i-KroRkNY8NFvAzkWTeAfx2alz2TdRe2mOGCeD_EhGgQs9U4BUBOBeej7el285jNaZ8B7nwEc6_kuOSL4zm7VF6kS1Wb23njMvglDYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اُما مودریچ دختر خانوم لوکا مودریچ که ستاره خط میانی تیم‌بانوان آث‌میلان بود با عقد قراردادی بلند مدت به اکادمی بانوان رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/28057" target="_blank">📅 17:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28056">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keiF2mF1m9xBOQ_V3jBg2bHAegqRMoHayZYdxy7UcNzO_ZXjJUXYr2wNTI1uohXwmZH_tcyFf6VLbysPZs00PTPsmBjyXliuP2aLhYZ7p40lA_BAYGVwpjYmjLXG3D3N_itNAKw0V70EEGQbBxPx1pYjauHf7gWdiwhntBsLcAZx4irZrtVh0dSjfF4k7QXSfOR5AcxtMNWJ165EKRqEr8eRVgBaDVgs_3u1E0h91s29VxpdgbhIgaPn4Le8GheI0M0FwxW2DtkJPleyIwgd411CxC4Vxrv_K5LVVFS3fONXIHRVELMp9krd2XUd3DFIND2ffrXK0ateNPKkbOMT6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شماتیک ترکیب احتمالی پرسپولیس برای دیدار امشب مقابل اس.خوزستان در هفته دوم لیگ‌برتر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/28056" target="_blank">📅 17:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28055">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzMPSjf2kVRnyV07PnfODM-1GwI0ZD4-idq0Ah1sIVO9qyvQPhKFc5jkLKDnFyfHkfUsyl_ZLBJInw61wdT3pIirU1XDmvFxyMR2nMLMn2DtikxP0ezJ4eWUbv8Dvb45hXujIPvj3o9nwniYRf_snjOfTMoTejWQ3Agjvy97UUPljWIbyJWSRBMMtVAG0u3ytJTx8HRGUe9KC1jvr2Qr_cSl2HEBSoP6RIRIC8ds9PXKzci6_UYhY8CysvmPPd43_8uY-c4F62bCA7JCpxXapksGdFjj97jMTvIZXHXfH-dx6B5bRg4C2hvmyphkIEiv4Oum032h2FXQusCicR97AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آرسنال با پرداخت 45 میلیون یورو عرزی کونسا مدافع میانی28ساله‌آستون‌ویلا رو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/28055" target="_blank">📅 17:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28054">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-egzfWvmlx9KYD5a0MM9q4ENTiMsaqQGAbCQgFc5qfwUMwe0uIq25vZG64L5tgAtfOwtfsUrge8jZ6F9CsEGfXx8UrMxsLR0XMw5MHGMS8Eue1SmF2BXLxcrZPwAfR94Mqfe6uZAwEb_wTcp9-leeHKPZJ82ACgvOcMqUn1yAB65Vd9GnOOY1ggsJjivUOfQErsD5MfaufUMrITSgvzdSEpJ21ok8hXKRyUPqB_0pCm7VoQQ1QRdJ_y9RLak-w42r3QFeTjzQCHhOlaID5oxs0YfuIf4RR4d0NNzK-Z0c-rhjmQZvpa2DMk6Qdw_Fl1-7Nlcuk5QUb4DjYDl7PWgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
عمق اسکواد باشگاه بارسلونا در فصل جدید رقابت ها بعد از نهایی شدن ژائو کانسلو و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/28054" target="_blank">📅 17:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28053">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdbd62c202.mp4?token=gJP2nJLoi2pW9_PSnDgF8Yeb9xm7RwjM9sn-UwGHMPl9RaKHlRLcuZZK018aS8wqGjBnRqhmkSQjMlwtvFvCdnspNrn0-PI_FvouDXxtJMMZQQ-ppkv4Oj3jI3pqcHPivqQOjqIEXRuD7_0Do4CmdEd_HOlRDdQFa9ctgPXIcpHDKSxB5M9YnIBcRzvZtkWL8mTGR1zi8vA_0uENWwsWoQYpkI-0RKapQOKljVerWvs5e-tX88GW_3G0-NLWaADZ5SfD1AC8102E8xoPhIpezJt-6G97fUVQVxyeFE7JBhXl4IpYNugQo1VKxfdT_ztqaMEDzU80zfupymY7u31YnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdbd62c202.mp4?token=gJP2nJLoi2pW9_PSnDgF8Yeb9xm7RwjM9sn-UwGHMPl9RaKHlRLcuZZK018aS8wqGjBnRqhmkSQjMlwtvFvCdnspNrn0-PI_FvouDXxtJMMZQQ-ppkv4Oj3jI3pqcHPivqQOjqIEXRuD7_0Do4CmdEd_HOlRDdQFa9ctgPXIcpHDKSxB5M9YnIBcRzvZtkWL8mTGR1zi8vA_0uENWwsWoQYpkI-0RKapQOKljVerWvs5e-tX88GW_3G0-NLWaADZ5SfD1AC8102E8xoPhIpezJt-6G97fUVQVxyeFE7JBhXl4IpYNugQo1VKxfdT_ztqaMEDzU80zfupymY7u31YnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌ازگل‌های تماشایی رودری هرناندز ستاره جدید بارسا در دوران حضورش در منچسترسیتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/28053" target="_blank">📅 17:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28052">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3Ue9eI8CEX9UzoRYC2hyKXy5Cnln107CcliFmNXLa5ou5ZYjbxjqO5U3iyUlokDE_Fe8mvNnOBIQA83VZAtcMzM_dYIaUpyKVHQvIbc-PgDmZVW6VplltbGvEdf4fO1dt1R6N1epFAIwWKCBrOuKdVp9t9T4SjoKgIDOTw8lEYxFRrrdDt_tXmot7R45Upfub7CH_4nKpGIZjkbvHlU15OP9r4YstgefI7UDNStiLEtSSr6R2v_6REEjSXMEtHcWGfIpcLyfY41oDa8GkBeULae5ivanGU5bWnBOoaVwZa8nj-bNgXOe8tIua9UqS54nRKolgK4SHvH9xHfZw0A-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته دوم لیگ برتر ایران
🔴
پرسپولیس
🆚
استقلال خوزستان
🔵
🗓
ساعت ۱۹:۳۰
🔴
انواع آپشن پیش‌بینی برای این بازی در سایت بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/28052" target="_blank">📅 17:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28051">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBNCBi6rsXkolg4oqMCU6dY_ty30dl5H93TcJFmK25VK95KHHNS5YZloKqJTyNwjr0JhnEP4qwnce0wmaMmjtj4CS20MwQWahu3wAIuY44OSO-JQl5luXBFvscyOVmLTA7D30u_WlAeFSgT-AD_Lj519IPaqZljjeyJudW1_7C13La8kY1c43VTdYY53r3EIxSrkZYldcOq_9KaIiSWsE3WSqDWZMRslcwrQ1_tjfKI6pmdrct6vTid9yAv6SUUUQwBprup7byYQa33tdRBGs3JJn2GDowiazLNzdZa0Yf1B_05erLUobUWaO1wdNjR_eQnx42CYMVtz2Pwg8yrBwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/28051" target="_blank">📅 16:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28050">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfxP6sJEgyrzugX7TOxixS1N2P3vmUsISD6P89gkSoJEEcHD-zOM_-iaVVYofAqYiV9pt-4YeZjZ5EP1XNFeZgJDfbxhGwjQ1VXWWXHxtzrzSNyVSq_noUyGxdHObQRhXvN6YA22vZdRZiddzdLiIHTxJG-ZKt4AogqgUeyzhs3zWF7blcZ_FsvHqGqxmx2_Q5oPGJi17f3PbZ3xYOYWPnOBoHVxe8YWtglUnnow5h3XRKLXn09SlusnGISqHX-y2AdMSgjS9TxS7JthaM9akyfUl5_Vf19k1lqYOjaiZFsozGdmtErH-WuPy6PPb1weypqFgxtDb8-rCHl-Oh80Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
مهدی طارمی مهاجم34ساله تیم‌ملی رسما در لیست خروج‌المپیاکوس‌قرارگرفت و ظرف 72 ساعت آینده قراردادش رو با این تیم فسخ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/28050" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28049">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsG1HUgHggFkoCFt6qX_0jiS4uRKE4F66p7PvCKtAPxw-pr8f7wWve31SS_lMaKFnrS7KFH9dadqDTtOhWbeK-mAkI1lEoNGUhJsFzvnKnacAKAk_knVFOdB4F-MUDmnSYuzllkFc6rEpjUo0xYMpQag4XHX8vjR8gTIa33EhpBBwYQqNSgLFHe9sbg6k2dFjjFtdBY55wbl7GCoYQ0r_OGPf-7Dx8mLqG8nljCHlE-Mik7s3TP-A24CQcNyimwifbbzByY3I5ZSHbdFTngBqfzuPZwrIswrkd1TRvUEYVa3UlQHPFVRf_zsAxZ4BC-fkfRs32WvcI34SO9W4glE7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
استوری‌عادی وحید قلیچ پیشکسوت باشگاه پرسپولیس؛ رئیس فدراسیون روسیه به دنبال قلیچ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/28049" target="_blank">📅 15:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28048">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICAPj5lzQCjFfflD0cZQY02yVgKO8LyD08S6-Gaub3KiKR1CZOgQp_i9BdUD7XBrUXYILXfkhL8ACxfbYDUPIPEySDJqG8KsRzya-TC6XsskWKz6_bPdLvOG6q-JGb5WcUVYHixEdwXH_lO6g3w2t8O1Y-4X2gGW30p7Geq7XTOr2gyT-nrxwBm9szgDaakqiaRamEJd07yCV-GKsKxNXjXm_0SKMYni8e_Ksls8AIGPQXn7NlaBwq9b1bbbCt-6nUJQMKJ_7cSrnX-yFYhwuDCMSGPyQSF_9xU6bYGfoBP9wPQKgxRRg2NYAyfGd2tp2QVzrEACBJgbAAZUlyCBJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داروین نونیس مهاجم فصل گذشته تیم الهلال با قراردادی قرضی به الدرعیه عربستان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/28048" target="_blank">📅 15:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28047">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrJx_nkqfLomVGTPdrLSkJ_rwmE_d3fx3lMRnMmqvlKtB2IbErtgNBLqIYjdAVNVoXEd0FBLVB8lqALcvaHbcNnVYEcEzzf0fMLhX9bovuceWb6dXLEWtZ2EMo5kyz0fy37ZhaKBKPgybbGmq3iRTIr47wvCgfgU_3mheo1tle0kETqfDOoaHSg640jEMvqGJKewHi1wwg7wjHyTPZs1VdVq5iFnTGYPMq2oNvXZlloQNWtPstFpaAfMMuLPG1QH31e1JyND_RMfCT9QX-3BruaXf0-lfjXKUmLKSh3Nieujs9w8I7CX1IUBBvphO7nxVfB82jZ4Km-1RFEP6aLwPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رسمی؛ دیدار دو تیم استقلال
🆚
پرسپولیس در هفته پنجم لیگ برتر روز چهارشنبه یازدهم شهریور ماه ساعت 19:30 در ورزشگاه نقش‌جهان اصفهان به میزبانی آبی پوشان پایتخت برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/28047" target="_blank">📅 15:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28046">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5lVQdVMuPl4X4ssfCAgLPylEglETLJ0LNClY4Se6sfJgg-7nw0DQcq5PQFRC_JKhoTbcxBVl5-fx2_1ZWfFb_GBfv1SL7N-WY0LnmSheSxQ22VeKD6KBbYc7TrlmJkFTPOxptg2-lo3YN9y7aTju-MGwex8ltWhk-HicHg_V7te7sLFt-tG0Sf__C-6kI3hlTC9oE7t-wsgTOXy5FbB-EXlu90SeiVFJi-7q6FZNXIc_0duqVaQIw7iv0-nM6ZkEr0kevdFrBgUeFVyZRGbi4bwz78T8TBHfBjl61ALRfeWMGP8GwgUj1_KOEBblNT60vN-V7Kan-qs-KpBHUvp8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
جواهرات جورجینا رودریگز جون توی مراسم عروسیش دوتا تیکه لباس ساده‌ی ساتن پوشیده و جواهراتشم از برند chopard بوده که گردنبندش هم ۷۵ میلیون دلار قیمت داشته و انگشتر پروانه‌ایش ۹.۷ قیراطه. ارزش کل جواهراتش تا ۱۰۰ میلیون دلار میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/28046" target="_blank">📅 15:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28045">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fM0uPbwT8ESfUl355y1ZHa8_1CVNuA6PSDO0AFzhkVddMqDoN3oaaxN1ykCkPl8WdEU4QlJkzb9DIsXCMW7CGd0MgCmM2so_zJ7oH3gefh_F4oy7VsdRuHjkuWudpTu2tk4ebGYWpbuswb76HQEk2Lg5S8kQtbB01N4onBKIb7IL6HEIVLcAkvX-Xa3M_7MlJBrR9hTM6KtdvEDqw_gnHyBLiayUEAvSbDEihxQtGyroOOFauQjw09-r0xkmKOsF2-Op7079dBSSmt0dP74MsDvkjARMBa0adz5tSDfqEUzo5RMOCXAgcUVc2p_TUmyYQAAD5-fZ5K6UU_2uTFPxXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیو باشگاه بارسلونا از رودری ستاره اسپانیایی جدید آبی‌اناری‌ها؛ قرارداد چهار ساله امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/28045" target="_blank">📅 14:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28044">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FylhZy7FNRW7z069W331QU5asryxVNlArK5GZOUlg4TQjuJteMaxXKaGOMNOpPrA-d9EcG40wyI2NKtP2RpnPuQv7SoGaXQHzBHkXHw_DpnZdnKDFGgRFsJNJtgVedrBrGeajWZMXqSv6sBNzNe6NaHEeg6w0Z5mwQwV8SyIBEvKX2YF7NQ8NbI5PtYcM6JOEN5PLRCy5Jk9kCt_ljp9x0QEX821C7HDHAuSJiOR7TH24eNg8DSZOij6UbO6mgP8VPeKubsz6dk_g8I34OiquEocj0s35jdpEg3E8o4wzkKdzV4Z7VLKz8nZvMTRIUxYP6fIdylWQUdu1a88hrqc_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
باشگاه استقلال باارسال نامه‌ای به فدراسیون فوتبال خواسته که بازی رفت شهرآورد که آبی‌پوشان میزبانند درورزشگاه نقش جهان اصفهان برگزار شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/28044" target="_blank">📅 13:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28043">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba681cb008.mp4?token=tsKW55iuRKbFXqUg5SrGzXGiml5GvouYxaZe1nxsXSjVi4NtaIpOEbxTjlfLqG3Xt2o6Zs-cI_yJd-0VfnLaeO1YP74er9oIWHw72J-hvJxYpqddAXTd5hyNwRG5CiqQwEzBMTKMcK4Ahl1MJvGEWSCqBP_mm6jGNzLKWAMl2LSKGcPYMWEosKdJt41GOOR_YqyHACCs5zYYmLjrr7eKpX7HgvK9BLpo2rAarUaXsvOuCK402JMwhLmkWwvwoCyfPT30J2THdNUJKPvQJUBsUqCi4RSmPDfgLr-NZBhGkUkit_1mCloe0AL8XbewCVnjYQU9nWxiRM_SbSizigWZng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba681cb008.mp4?token=tsKW55iuRKbFXqUg5SrGzXGiml5GvouYxaZe1nxsXSjVi4NtaIpOEbxTjlfLqG3Xt2o6Zs-cI_yJd-0VfnLaeO1YP74er9oIWHw72J-hvJxYpqddAXTd5hyNwRG5CiqQwEzBMTKMcK4Ahl1MJvGEWSCqBP_mm6jGNzLKWAMl2LSKGcPYMWEosKdJt41GOOR_YqyHACCs5zYYmLjrr7eKpX7HgvK9BLpo2rAarUaXsvOuCK402JMwhLmkWwvwoCyfPT30J2THdNUJKPvQJUBsUqCi4RSmPDfgLr-NZBhGkUkit_1mCloe0AL8XbewCVnjYQU9nWxiRM_SbSizigWZng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر محمدی هم یه تنه تمامی قوانین فیزیک رو داره نقض می‌کنه؛ در جدیدترین اقدام این پرتاب 45 متری رو در لیگ یک روسیه انجام داده که کرک و پر تموم رسانه‌های دنیا از این پرتاباش ریخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/28043" target="_blank">📅 13:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28042">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZ0GJl2yuOyOPuI5W3Pd0Zl8mZdvbP6XV88za0qe4MjFk4f4ZDkX3yfHrMBs74qZZYyt3ZFykW18Fvvidpwt_KhWBGPJYXD2Elgk94NDUSkzwu1rgG4wIRxTTsvjsU79kZ0jIhcTAd41HAMgCcsShSy5lbsrCdmORrOiQAv-RrIJF49P06ptVPAwpzmkmPRDibGkrCeSZZg2xPF7EvPzMS4dA4WJWYOK2fzGKMi5ApgUwN7YutSkWi_sk7uRdDIoMFYIN3wrbo5uX_ehUQOb1QC4cI2qE6-DKigfYCqQdF2OBPT12czAfhO9Bja1AyEINuWqZT4VLkqYuyJ6K_3mUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای هفته‌سوم و چهار رقابت‌های لیگ برتر؛ هفته سوم دو بازی فوق العاده حساس داریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/28042" target="_blank">📅 13:24 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28041">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opTBd0AqOpJNh5t0qS1rnbGhA01ROKhDpUgz74mulweKMszmpFq6X1C4jR2E1tCVUNsaOOEmNtv0ogPhV3JaqyLA7HeJd4boHPs9wEbrPVOXrLROzL7qku94FOj1tbw4cKIU84LftqZl28HGBc4GVWr1YAF_olFlHNlyDieNrML1t6YEnLMIcfVpZeEpd5AC6xvL5JYu0Jmg8jGbo8osrSXqZ623c8NrT0I0S44vncgj27nEH7vfmmfQw_SvOezkDnBdFqa7bFxSetrpc-t07eXJjnf2Vjk-Rh8TjYN0vyaaCwvXshLqG3kCm4GAI7qrqpabz2FffRzC21PVxHLHUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام‌رومانو
؛کارلوس‌بالپاوینگر22ساله برایتون باعقدقراردادی پنج ساله به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/28041" target="_blank">📅 13:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28040">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcndOFfdmd9LTgz3jXfbs2HU4_ULrSur-zaUSmMzv5GklaIKuxbJ4p00ejfAuU4B5G1j2cXt2auxUPVNpyLof_I4Yac3zyXMTUu88sCJKqew_-dmG2X710atr8mkmWGPTg95iSXMlatSBkPbVzH4W5rQRenfEn0oppajtAiLUcGTuD54TFx3ixavvbb1dmftJRdvEHtCNZvrhw9xcmnjIEjbBTaEPlWON3DPwUVsZsyE2m9pwz7k-g-pYwiOrihbNMZqMEQWA4djtwm3OL-cXoN04cUO3xcISbrZbEDkefXWPchbUPKAtc6Zy2E_Z_6TWtBZEmxO37ACZjTiuKMv6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
پل پوگبا که پارسال بعداز 26 ماه محرومیت با موناکو به میادین بازگشت امروز تو تمرین این تیم بشدت مصدوم‌شده و رباط داخلی داده و طبق شرط تعیین شده موناکو میتونه قراردادش رو فسخ کنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/28040" target="_blank">📅 12:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28039">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i267sbFG2PXU4lYK65ITb-j5zO314E8R7JlvBHUj_ZCirEOd1Qaq942tY1ha7Wa3lkoABEspnNWVZ4c2CSGPCubqSKZ5KFmuHcNxfluzL-lvCFijToNgc8bKFvWRnCb38Jhn8ezVCN7xZJH-fW2Gus67nkvcG0XEslittr6UzFJOOHa8fYlStKaUfPYD19iDWk5iwkITqac5N91VOy-EMducdpiQ_ChoN0M2FP86YO9U3hxreAIkk-SeWQCsOFOWRDYPTJfXoHjyKq06Jbn5kW30hxEDPcQf2MYHJmX24qDjzDOnDKdJOsv11f0-xmrgmgc_nKv9F7dpcd0tsAsE2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
رضا عنایت‌زاده هافبک‌میانی جوان پرسپولیس با عقد قرار دادی قرضی تا پایان فصل به مس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28039" target="_blank">📅 12:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28038">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsAS7zKDvd8ZhoDagHCf1Klx-VKZ5ZB4dp3tAVkkjE1_eXJnFOSZYEmSnk60J7yFQ5L8SlhKIThwcvhFPau-HsKcq4tQE-3UABgUVbC-rUVHcG9KSJDMPi20pEC-0ibBF6PiwZ-_KKXN8PXT4yfc9veGiCYPp6B0SFm2rAN7zJrqkrpJaoVJuT6dD1AXoDVji8PWsLJI5JD5I8lBwkq24vFguytt8zRHeRYprp5uz0s7sVUCe4iy5x3Wpm_fbNiGGmdu9HG7M3NWI9IQ17Px-lc7MjxMzncpdxj1vqpkpLS5KVwkhb6JO3HuahjvgVKv9AkIBSTifg2rKkK_0CqONg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
فدریکو پاستورلو مدیربرنامه مهدی طارمی: جدایی‌مهدی‌طارمی‌از باشگاه المپیاکوس قطعی شده. درحال برسی پیشنهادات هستیم و به‌زودی تیم جدید طارمی رو معرفی خواهیم کرد. مهدی یک آفر از لیگ ایران نیز دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28038" target="_blank">📅 12:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28037">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btEfHQkO4O2ozTInWNzDQw3Fk2BpGxIorUPxN7Xx75kE31NZpovVinNX5EJk2EYk3I8YMnzrOsqVoYEA17kmFLQjMR-hSDfOgFTQtoJfxPG0Uw23019AWCyS3gUfkNQYlUsAxFv2rkrYx7cHcj4z7-Ar-UmHuZVrvxCcOiHTaXADk605tqha8FO7HQi4A_CeH_3aNCzEfcvehrANnQtH4zMXzG-USlZpe7EgSs1JkQRE7Kb8eI4l5fT9rN1DORFZo6MnKVQ-Ih15kUMK5kqICFHY6-updqF5xuZyMUgIx1kCkyruUe-eq1sjtXOSGWuK4trLkH0ugoiAVZhxZpkLAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
یکی‌ازمسئولان سازمان لیگ: روز شنبه هفته آینده درخصوص‌وضعیت کسری‌طاهری و یاسر آسانی جلسه برگزار خواهیم کرد و رای نهایی خود را درباره قرارداد این دو بازیکن رسما اعلام خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28037" target="_blank">📅 11:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28036">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZl4PDfdKHV0QPDMsy-cpFkT0lXxHHC_iR7SGRueinxaMervR264iFz_XlzMr8JjCX8SkMBtozXYkicglnJ7JnEiT3x_WePyFZ-TqBS3mYGHn-ZBHVkSs8EzcJ1Dksfof9FAiEH1VgjV9i9QKEhnxgjRcuvmNPkjCcNFWXDIrgRnnhOSz_RHnA9XVZmKHUtZepx6j7013Rkb3hEvhA-vNEB_Ep0Wy79pO_AFsLHQkdx6XnrglSYQxP6S4KY6T2AGUs-bFXrjKc_NOKlOl8rcy2zmgxSksRpRy6laBXW7mRXFJx2_V8mROgIoTGb8H2aPNNeOf0YGT-ArI6Wba3RTtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
دو باشگاه استقلال و سپاهان امروز تمامی مدارک‌لازم دال برقانونی‌بودن‌قرارداد آسانی و کسری طاهری رو در اختیار فدراسیون فوتبال قرار دادند و بزودی فدراسیون در این باره بیانیه خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28036" target="_blank">📅 11:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28035">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k11pFEgvxc0Xa4J9xh1H7RN-rrmhFCDz_AKRfEH6YPyu0h53MORYD1fHt9UwRdszldi7lItawOpiDiV75NDaFer5Xkt9aKGymeF8O05z0qm00ZZJFem9pA8hMoY1Ki6YuWXzgyEd29Kvatz8fe806lEICtm4HGThmVAseCVkb73PfPwSqMQ6KqFMzDrajOUpsg4dy1kt51C5ISqTLSVsgwCYR4YTwe-saEZ5Z1xX5kHKkaxmZ77W_dKlH5k-68kFMmM4HYADu9roRhMXIW3wGBK8IP9vpADXQ79D5E-vY3fPwplWhWi0oQRPLHGsyh9i5cVNn04LA_ytj9eyKGfFpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
نتایج محرم نوید کیا سرمربی سپاهان مقابل تیم های بررگ فوتبال ایران: 6 مسابقه، 6 شکست تلخ‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28035" target="_blank">📅 11:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28034">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mixY5vP7cNj8BqO5EX3ddpNCJepiubPoaHIxf2d1KUlJbbdwek9EJG663F-nVEsyhqZ1fpDJdSF6Dos-DWF1ctM3U5YWssU-9efHgWMKMzy65CrB5AlpJgUcDFZJZwfSGUQlalnskIu0OFNQb6kzzCtoPs2KAt958NqWocDRLDX_abaM9Vtx_xLst2wt8sPuDgWqMPhNmyLdXbf2kegKyYED52aEWZF2FnW7SYql-7WskVu81IzDoaIbmlmTHeELVYCMgD2wodW_2XLnPGCKKrxp9UQv2ZXbeBO7K8PLsr-5JERKpVPapcbtCLCHNaop6DTfWLLwBh1Sl8mqFcVYqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کسری طاهری: از پیوستن به سپاهان بسیار خوشحال هستم؛ باعث‌افتخارمه که کنار بزرگانی هم چون سید حسینی حسین بازی کنم! واکنش حسینی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28034" target="_blank">📅 11:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28033">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uF8ccGlaQ14a_Pjj--XS0iy0SpntYbDquG-q_WE-zZuL0Z0jEwH0hIOskpvQ2UZcHVxH9xCQ_Og4cScvTv4os-zGx8_xydUqvas0ViMAEPJAIh07mZr1IczgMqxVBOsYweMkifTJ6UrjSKAizXOMt6MO-B4jWWwEj7qDF9DYl8dvIXpq3V0uKqtUbWkzhupsXx80hnXwjfVLvHlsCalGEMSp-i0tUSjmDIU6qb7cSdy0CCX8R25ksiu6L9dgpAUVluXXZ_Zh7CpRnJiz2nX3SL494r_wyjlPqcHZ_pn9AGnb_Yq5cG0dhSDK68yAq8bLh1JFwEnlfdUfbX7KkCzZJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگار: چی‌شدکه اون گل خوردی!  حسینی: این توپ‌هاجدیده، تاجابیفته که بگیریش یکم زمان میبره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/28033" target="_blank">📅 11:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28032">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HB995LweS3JrYaumVubWS1kIDC-ICsz1iYtGKfB67jeYw3CxNsFTQH4JWNNRwrIcb7gmA3bdGXntAmhMskBIPA-M06IGxcFCasXcN_2p4LeUk7W6uGsVdKCNo8gMID1QmRH8ALd7mlK8tC-ujCGhR3pRmyuWnvWmVc9tgfaWpSNwPFzUYunHtKUQGchcM1ROIOcGODUwD7rvX0TzmT1UDKqhjFVpOB8pBAKtQFuC0xzyZE9IQx_YNPXEZXDNJgFtsduZQpt_4zyDs8HXUpWJ8hczDEmqsJkuWYt6YCYaE4gmt0aZxhFuN_HEX-2JvRvfnCguCD6OZ26BTdwKdfzJvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به‌دنیای‌پیش‌بینی‌فوتبال و کازینو با LINEBET خوش آمدید
.
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://t.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/28032" target="_blank">📅 11:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28031">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7xxjaUveuk3Lflgo-xJAc5DDYGt5gVt0O8FfgCITiwKppT8jbRZT4fli9x638rQazXkIevVi3dGYfOl9iR7V5tNtmj6g5mYR2JDhk5jjUb4aTXP2a4dOIbcvf_joZiMwYVOkKrUktr2aWosFKCvw7Fa94i1JGeeBEPe7cyxGDQXIdbcDWkWF1ocPpVs-E5l4R2OvyDmXFTZfYrmwjLKZph-yyPBpmgRaJHZqOoUDX-UycjPI8ZOkibeyACWhn6tXMkkHBGsrbRnyYOYSTS-twdsgt6v3YsBHGWcEB6uxprfzPpMH945TNTx-TfIZGVxqQ04c1aQ6tqh7Uw-MnpaTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظه‌ای که هوادار منچستر متوجه‌شد حالاحالا‌ها قرار نیست موهاشو بزنه و باید همینجوری ادامه بده   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/28031" target="_blank">📅 10:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28030">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpKyoklaZ6FVJ2VfT8SHjBR8V9gmK-QO1WTJaDOE920SoDSwDGTw7ad0avHs2erOOkqVKtjk5F49hfgU7LMBghpChIf-xosjPm-fGAdvmM6TznqMvCeroGzBURQ8GfK0kgBd6_3QdBGiI8vUjqrqmfpQAXuHlpGAKLP9qhrBm9Sxt8lwn2Eu-x87EjNjE2nPkTyw7vtyy5osnOacfeu0FeiJbInZZanMnGomPcvqsdvWNedZwP3tcB82v4XoWh1JVBAtcLpW0kNrWMjKlfQ7UoiijGQndndTxBv9jLXrXNHgCgUEo9XoB6wJDxYHFRTujzk1ehjub0fhIQhvAbTCDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارکامل‌دیدارشب‌گذشته نساجی
🆚
نساجی از نگاه‌سایت‌معتبر متریکا؛
صالح حردانی مدافع راست آبی پوشان بهترین بازیکن این مسابقه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28030" target="_blank">📅 10:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28029">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936c9a62e9.mp4?token=hIHRK_5WDxxkFab8CUyd6tAVP0D8b9i9qcfq6INV4HY3iSHO5aDWYEdN1nOf3G6BRuo62wjXOBWcm6YmByGLp-Pen8p2rweeJhgfAwFHwOuHWtgjh5dmoWTfP_uIT1wcbpDEfPRosYtKjMFG297DLF_DdiF-ujf1QQQ3b3pxew-eDqf--m1-QIZQ9EGyIXyByHwPPxwHF5RWt1zdOxxDlXgHdjNlydaykkU8X63Rwet9r9aQ9B6VlEVCW7wkAWlz6YpGcLj6lNZcXysP5mkZvmZfqLCynrGAevyWR5ivdiq5T-V0tFDei0_ttpQo7-oLuajOwXZaChdxdIkqeAWw7RES7y9_mmlqi3j3RxSuKZJuunikdLPuCaQJqRy2XeU0C98zu4sac7Mw7iNdgKcygLsyTy6LVNAnpAyfHsGNGt5EaUF7EosLOUUvLVcERy2pYq1myDMgA2xpDtxynYYn7emjPfq_zPdtGZ6300bC5_Ae4i3Xtp3I3J8XVzhRhQL3s8P75ccDrLcwLg-w3gqcmJJHnOObTbHyJnWrk5dWxfFTYP4yPM5HabYgO9Nojl4AwT1Vn30Nso2mcFm4J6REpU782YW0cqiY_fd-J9Qh0VAEGUjKddXfVSsplYIx-wHZxUE0Nl8NDj91naMqA8Imuy__a9EpTO8agbjU2dmTU_I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936c9a62e9.mp4?token=hIHRK_5WDxxkFab8CUyd6tAVP0D8b9i9qcfq6INV4HY3iSHO5aDWYEdN1nOf3G6BRuo62wjXOBWcm6YmByGLp-Pen8p2rweeJhgfAwFHwOuHWtgjh5dmoWTfP_uIT1wcbpDEfPRosYtKjMFG297DLF_DdiF-ujf1QQQ3b3pxew-eDqf--m1-QIZQ9EGyIXyByHwPPxwHF5RWt1zdOxxDlXgHdjNlydaykkU8X63Rwet9r9aQ9B6VlEVCW7wkAWlz6YpGcLj6lNZcXysP5mkZvmZfqLCynrGAevyWR5ivdiq5T-V0tFDei0_ttpQo7-oLuajOwXZaChdxdIkqeAWw7RES7y9_mmlqi3j3RxSuKZJuunikdLPuCaQJqRy2XeU0C98zu4sac7Mw7iNdgKcygLsyTy6LVNAnpAyfHsGNGt5EaUF7EosLOUUvLVcERy2pYq1myDMgA2xpDtxynYYn7emjPfq_zPdtGZ6300bC5_Ae4i3Xtp3I3J8XVzhRhQL3s8P75ccDrLcwLg-w3gqcmJJHnOObTbHyJnWrk5dWxfFTYP4yPM5HabYgO9Nojl4AwT1Vn30Nso2mcFm4J6REpU782YW0cqiY_fd-J9Qh0VAEGUjKddXfVSsplYIx-wHZxUE0Nl8NDj91naMqA8Imuy__a9EpTO8agbjU2dmTU_I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قرارداد رامین‌رضاییان‌بااستقلال برای فصل جدید که زمستون امضا شده‌ بود: 100 میلیارد تومان + 25 میلیارد آپشن که توسط‌بازیکن فسخ شد. قراردادی که هوشنگ سعادتی با فولاد برای رامین توافق کرده 65 میلیارد تومان نقد + 10 میلیارد تومان آپشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28029" target="_blank">📅 10:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28028">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djVzuGnStotbt3TLDoFtGEP8K__6oOtvuDu9Lvk9HD4IIi7IBjN8pvH0oWlScA9ZC3ZWrMjQJdeQHvLw24rPl3F2FinMWgDc5CaatMvm05f99QhA0dHE9N_J6Q9lKCRSCwmTFyQKcjLFlk7SR6Z95bK9S8CdiXS7p-u5sSPJkcMvspENSYdMAo3MVAkWYU8XdjD3Bubvofg3DAzHvkBoXHhSy5I-x6mGDYzmCs8Pui-PqzdZd0ldBI97WkrZ6Q7NT4pekFzIfpHWCu19cW-Ea3ZEz1LyAocdkHC3mR0Oanh9DlZw_T-nxFigng2GK_Wnn_a2B6n5HwONKj7K6VAo0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شماتیک ترکیب احتمالی پرسپولیس برای دیدار امشب مقابل اس.خوزستان در هفته دوم لیگ‌برتر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28028" target="_blank">📅 08:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28026">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXtE6cm8VKIoa7XqAlVjejBtS7jNredOfTLP3X3pzIFKGLER2Kph1uN-5IaqMHO8qQWQ8nrMxlwyu21ExICR6j6Yrlo_DmTtNHdUt24DP6DTXHMRarbcKGhOUdkS58HJQ3xQVrh6oo_faQR8hbHYiNYgErjw-RruhZoAKc3GTAbxd7c3gurKId9M21uMsOrbu-bKjwegFqvu1vc2rUlDle0ycdQiXchPeHlrBkqYw_iXl8Bc_HhwuaztVze--Yn_h79Ky-N2llgBDh64oHv8gGWXdJmcrQ8KMZaJG7EvHeqApKm7IESlUzXzelYb4cpDkxd0ynMnkB5snuMl9Rpl8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
جدال‌پرسپولیس با آبی‌های خوزستان و مصاف‌بارسا و الاهلی در جام خوان گمپر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/28026" target="_blank">📅 01:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28025">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENWGm08Wk_ZclpAGcqH-7uqnt5qQIAt_OSPnf4WZ_Cprq70uKgYfzxpPn-b2d-hNEdmT_nn5mWHGLUVzuVZOG-BxS0SShcvMGPS4ZkoUeWpMdnrp2rhxUWf1ZhrF4bZrZ7gm-L0a8vIH_efJBB89JpG_L0MTjDccvCzAKAEMaLZEgjTPAAl4EJu3JOLVBeXrcyku56x9vvhM6OaU9q0En7J5lKHBWtBBKGw0iRf5O5CNNZntxCylJ_cPjiIVqficZHMQysF6De9QpU_LsGvWp0wJJatBbawzI2t6iWcl41DF73aO6j6lsCTl-Dv62cxJYPixyJ8kJeEQG4Yo49zZkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
برتری‌استقلال‌برابر نساجی وشکست‌سپاهان‌مقابل‌تراکتور با درخشش حسین‌زاده
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/28025" target="_blank">📅 01:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28024">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSC5n_Hrhir6CVpogZMaVl4fiAgbapNZAytSMwqWb-pdTELw-rqTx8E9P2QVsNogabZmhiBgoQ19T2x3lShT_eiuYKbM34nDl16p1d67amA-fx_QwkVElwtggVLdJCZALOlgiL8mA6somvTduNkZW9OfwfNiqkUEX8iA3H5zICBBRMXp1rlPKjDgni7ogxjTNEQW1Hxrg1Xj_D1JfnQaSo0MCDPsPlecbl30dFZSDFTvbl031rlP9i3CK-4dA9HI_ODh-p2hqUUGkjf2sIY7v1X5N-Npg5Q1a3n5ytf8W_KsDON_XTPPeD95dFgvImlTBX7hiLM-7UhLl_90_Sonaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روبرتو کارلوس، اسطوره فوتبال برزیل و تیم رئال مادرید که اخیرا نیز مسلمان شده بود با یه دختر به اسم سهیلا 22 ساله ازدواج کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/28024" target="_blank">📅 01:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28023">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCB_y_QCROL835pjlq4INqckI2Lu4tg9fU_ghJ1tj6fVsaHSS2k_lYoCtkdo3BY2rjQ8N4_hx38imyom9nYv2ZCy48HmNX8CBb2WNoZR-Y6tiBqOQZdIb2SkpdfrsnRrEzszYTXK2AcTMryaRaBZdr4G85v8P8u1NrvJAOtMLyOc7NToGAyUdiT2aS0PBAMXz1E083GAFHRc69GO-sg9US0ECswvvoCjVv2U9TE_CZaZ8VO4_vA3fbqSGQgJhVXrt867d-VzSf6KJ8NPbqo7Fy1kAwwBndLkdQJhlPnZEWxI4jm4b3Mpt7-G9PIjnk50z-G6EvhQ7y3W0ePnqHQ2dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
داکنز نازون و آنتونیو آدان دو بازیکن خارجی استقلال تاپایان‌هفته جاری به تهران خواهند آمد و در تمرینات استقلال برای هفته سوم حاضر خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/28023" target="_blank">📅 00:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28022">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbdviWhRvhSR75mlknGNm7ZJiEm4u42TzyfrQzxZm37E0l-OLZLFUZUB12qP0vaC5QUdYrG4ujW3rnoFyrXYRch3yNU_qSZMvKr-YMPNqj9sq6UYt65peFEgJk4oBRL72DrXJoSXNuoI_dA2XJeoxyaHRiOOqyyNU9KmbXAyi3xCro6-pdn2A7my5fGgPa4jQPy4-21A9YnVJC4vM_JoaZSU22E7mohpnQhut1grKknGODerH7k9M3-yBV98oX1gbJLoJGd2nkaD4y53lxDmFyTSZEMGeTFLMlq-XLox2BGP9yhNo6aYT4nx8xWEE0m82RUZ25riF6JeCiLQvMqsSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛باشگاه‌الهلال بااولی واتکینز ستاره خط حمله تبم آستون ویلا به توافق شخصی رسیده و این بازیکن آمادگی‌خود را برای عقد قراردادی سه ساله با الهلالی‌ها اعلام کرده و  تنهاتوافق‌باآستون‌ویلا مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/28022" target="_blank">📅 00:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28021">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19d89cb00f.mp4?token=L8ZLaZ7Ba11q0tCtG6U3o2_mjJJ8UfsoOTGv4i7yIltD8yMOwYOfK56IXmBX2HOFPHS-XxHHEr9iyO-PHCt9FuFm16a3C1HT0RtT_5hPtpc25td0MFNhOsju-blpE2oSfrwQepCQXRUnFzlC31nV4vQKyUipKeYL8kRoAFo6bR9pHyhEYflFaB11sJyB0TcZjbtF7uhk7LJWyS-J26HKE5G6kognUYgBVuFWGkY1cBb5gzdrLn47h9cTCJGO0cOQqohGeSiDBo39-Li71NMQPPWmYOcqL7FOXfo91ez3M6ZTbInLh-kfMVbDH1htZJVNPPYDIYiJihvkr8xQ0P4fhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19d89cb00f.mp4?token=L8ZLaZ7Ba11q0tCtG6U3o2_mjJJ8UfsoOTGv4i7yIltD8yMOwYOfK56IXmBX2HOFPHS-XxHHEr9iyO-PHCt9FuFm16a3C1HT0RtT_5hPtpc25td0MFNhOsju-blpE2oSfrwQepCQXRUnFzlC31nV4vQKyUipKeYL8kRoAFo6bR9pHyhEYflFaB11sJyB0TcZjbtF7uhk7LJWyS-J26HKE5G6kognUYgBVuFWGkY1cBb5gzdrLn47h9cTCJGO0cOQqohGeSiDBo39-Li71NMQPPWmYOcqL7FOXfo91ez3M6ZTbInLh-kfMVbDH1htZJVNPPYDIYiJihvkr8xQ0P4fhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام‌سازمان‌لیگ؛ دوتیم استقلال و پرسپولیس فصل جدید رو هم در قلعه حسن خان شروع خواهند کرد و فعلا تا هفته ششم هیچ خبری از آزادی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/28021" target="_blank">📅 23:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28019">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GPLrAwFpJm13vDr5nqdRGgBeZTVNtY3xxNIag3kCFQqTqaHI6aKrG5NYlLSH4PDPr2ifhtFAQpPFeSBAV1lNwWiE52ZUFSY0oKewcQ4P6rxinH8fltVewPglpcV7NjN3QHtKP1DPNZrs-lol_jp-228nX_Rqu3gp-afv_Av8IYqKwab3VBmGi3g8oHa0jRyBIb3KXhz0D-HkuSHS9nErHyqjEYianqlpq87ANjJjtjSi8hUz1zEDWSUKohGrtBhYANObAU8QrPfKjxhqxhnDFcbgENT4_Op624itp8mWAWLY1VGJ8gTkqUblONRXYYq30rGhn6rZHC8NPKKT3Zkvbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gBGixwPSLnN3DIc5f99CNdSb9cJtKiBZ3LWMC4Ldbcz8XYBgkXDum21wJAInP93f_Y1SxOBAS0yP3UOXF-YaN9CyjJzWzSzPOSDrqJZBuR7wDiuiADMEVPbAr2yU_x2K-Sdjg2Dqm2uQw19SI1JK2z8NgHKoidTa9ssFlTLJWIS2MLesjKsEM27gYIbYHcewMUDSBB3FKD_yZMqn-8cfGtizsA2oW53u23W12c73WIys91AMww_DlKY7uc5jkuxTMXgN96Qma8P1ugMr4UTKYGiW2pEf6nUFgpZdmfz7vHBbl8exmOjDNNnYIC5JSQ5KQFy9br4bmCc2326YoYebTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
روبرتو کارلوس، اسطوره فوتبال برزیل و تیم رئال مادرید که اخیرا نیز مسلمان شده بود با یه دختر به اسم سهیلا 22 ساله ازدواج کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/28019" target="_blank">📅 23:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28018">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89654a5b7e.mp4?token=sHXun1WSSP6ga3nXuli36mGs05wWQguVYyDnJ3KOAjaICCM_oBd-re9Hc1ATqxMz5qlqJCv1K0730cONAR24BTrhPVhRNYWRZ31p4Xxf8E_YRRr038C1m1cOE6abSf0go0pSPRaG4d6VmoA1TkJWUd_EjFQ86p8RVp0PlADc45pyvHpxMK6a758m5TjUYuAOnPgy_cs5OMNzEh93YvenOwBfcWmhrUgHeciah-Sjet3UJqD_tsHl8OjCd1_PdMoLuraxNcGYl8ojhJq6w502QCk-W-1FUGKL6TmDfu5qP6JsgvcgAigub0L-IinBy9T8rSrYzOzTffciphbu8592Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89654a5b7e.mp4?token=sHXun1WSSP6ga3nXuli36mGs05wWQguVYyDnJ3KOAjaICCM_oBd-re9Hc1ATqxMz5qlqJCv1K0730cONAR24BTrhPVhRNYWRZ31p4Xxf8E_YRRr038C1m1cOE6abSf0go0pSPRaG4d6VmoA1TkJWUd_EjFQ86p8RVp0PlADc45pyvHpxMK6a758m5TjUYuAOnPgy_cs5OMNzEh93YvenOwBfcWmhrUgHeciah-Sjet3UJqD_tsHl8OjCd1_PdMoLuraxNcGYl8ojhJq6w502QCk-W-1FUGKL6TmDfu5qP6JsgvcgAigub0L-IinBy9T8rSrYzOzTffciphbu8592Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه جدید شجاع خلیل زاد مدافع تراکتور: فوتبال دعوا نباشد که لذت ندارد باید دعوا کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/28018" target="_blank">📅 23:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28017">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a8d45198.mp4?token=VUqYi-XayNcbCZb7UoU1VmnOdO_3qwGu23ShJm0hQ9JNAk19IcUhVh_2bWj-DmFPtn1rO0X0UOanIRfA0FcHOjVBTCm8-aouyfE7tU_x9WdueVAkC7OGf1rEmK8_w08i9ZTl2EqhyZFzLtjI0VQcg39pjx4pkfg_pA7xM-eBKc93uE1FpYy5M8JfLXv2Q_le7emBawGEbhd-nD27dY_XX_xRAyo_sTQK-B7D8SQKqxBAW5b2iO1pdtza5luw44wWV6w8xq0MkdoGroC_Z4QuW2aAn1skT22x6AXXLucoSMKqududPEoMJ7TpGROG0aRpbYrsOivkSNFL-GEPWWOS2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a8d45198.mp4?token=VUqYi-XayNcbCZb7UoU1VmnOdO_3qwGu23ShJm0hQ9JNAk19IcUhVh_2bWj-DmFPtn1rO0X0UOanIRfA0FcHOjVBTCm8-aouyfE7tU_x9WdueVAkC7OGf1rEmK8_w08i9ZTl2EqhyZFzLtjI0VQcg39pjx4pkfg_pA7xM-eBKc93uE1FpYy5M8JfLXv2Q_le7emBawGEbhd-nD27dY_XX_xRAyo_sTQK-B7D8SQKqxBAW5b2iO1pdtza5luw44wWV6w8xq0MkdoGroC_Z4QuW2aAn1skT22x6AXXLucoSMKqududPEoMJ7TpGROG0aRpbYrsOivkSNFL-GEPWWOS2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حسین‌زاده‌ستاره‌تراکتوربه‌اینشکل دروازه سپاهان رو باز کرد؛ یک شوت محکم به وسط دروازه زد که با اشتباه سید حسین حسینی توپ وارد دروازه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/28017" target="_blank">📅 23:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28016">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175de0fa0.mp4?token=WArKYCBbHqwQFlsp9fbD58ZWUEALHUlzjTKiWh9vpaJSkEUVVWRNVmT_S2xJQG4H91pRjHCai6xqIMEqUdo2fMZUHLWshrHsj8t2OzsgwASrlErnoWGu1irrPV3TYWH5pNstivXX2t2MNtgFktANEMd5tGVfYkphts4nVY1VjD9yhDvwFnLZ6hCKUV2Yk6SRncusenKG2YzPitOo47RhyQQJh85-3F3RQy5rGZw7j1aonbuIB_0y7zxqSB8wb7JdQt-jTFdqm9MpiS3DTZrxGNDFg6XNAGHIF_qPin9SvbqaeRS1iHng2CZBO7Yp4axOsSfs7Qrf0w-FNN_T5AZCFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175de0fa0.mp4?token=WArKYCBbHqwQFlsp9fbD58ZWUEALHUlzjTKiWh9vpaJSkEUVVWRNVmT_S2xJQG4H91pRjHCai6xqIMEqUdo2fMZUHLWshrHsj8t2OzsgwASrlErnoWGu1irrPV3TYWH5pNstivXX2t2MNtgFktANEMd5tGVfYkphts4nVY1VjD9yhDvwFnLZ6hCKUV2Yk6SRncusenKG2YzPitOo47RhyQQJh85-3F3RQy5rGZw7j1aonbuIB_0y7zxqSB8wb7JdQt-jTFdqm9MpiS3DTZrxGNDFg6XNAGHIF_qPin9SvbqaeRS1iHng2CZBO7Yp4axOsSfs7Qrf0w-FNN_T5AZCFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلیل‌زاده:اون‌عینک‌لعنتی‌مال حسین کنعانی بود و دادش به من‌که باعث این ماجراها شد اما من بازم میگم اون گل آفساید نبود؛ ویدیو رو حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/28016" target="_blank">📅 23:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28015">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfc13a6650.mp4?token=QpCOE20dUXPqgB8iZU9y-cvUiCyUdWr6JnWLJhZS1BN_oPyTpKtrUsQQCHMCf2l9gb1lyzrNhtPxkUSI7JzIUxt4SJZVwoSyu18ZXfOQ9s6BC-GWSX60IUDtlu8C1HK-uwfLPWcvrzQKdbs6kW4DawT0QIi_gc0JlRipr_Vr-YqZ7rdSQWzw_i7fL7wvgJ6SW6oRjZ_DsGMvOQYcB133avTcH8KKfXORGxOtfhqDqHmSx1ASOYwVE2y48yR5CbW7Jso1KaklL87RaYsTq9VSNWR8Lx0Q-lt5iK57MNZEKIPKOzS8PvzJim4OpRqtUfmnnYHFk49bGSB2Kg-JndgQ3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfc13a6650.mp4?token=QpCOE20dUXPqgB8iZU9y-cvUiCyUdWr6JnWLJhZS1BN_oPyTpKtrUsQQCHMCf2l9gb1lyzrNhtPxkUSI7JzIUxt4SJZVwoSyu18ZXfOQ9s6BC-GWSX60IUDtlu8C1HK-uwfLPWcvrzQKdbs6kW4DawT0QIi_gc0JlRipr_Vr-YqZ7rdSQWzw_i7fL7wvgJ6SW6oRjZ_DsGMvOQYcB133avTcH8KKfXORGxOtfhqDqHmSx1ASOYwVE2y48yR5CbW7Jso1KaklL87RaYsTq9VSNWR8Lx0Q-lt5iK57MNZEKIPKOzS8PvzJim4OpRqtUfmnnYHFk49bGSB2Kg-JndgQ3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رفتن با یه هوادار نساجی که لباس آبی پوشیده مصاحبه بگیره. هرثانیه‌این‌مصاحبه عجیب‌تر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/28015" target="_blank">📅 23:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28014">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igIzPBrs7vytljt1vgy44sPnjca5B8lPaR7j36Fy5M72sd7wcHx_4rCedidpuciKe7yxKbtdG5rdelJV53vg-eZVn4gQ72xBTSAq4uflkOGd3z9e2fix5O-Qs2YbKGAGLZQIpauqHpT7f9NT0vQmJDXcgcAFtzw7A2CREqOXYckWNreZOHetgMZiExMyyyS7ShxpnSdKTGcvNy-bKIQpwAEydzl3m8TXL65kyDYjloyRACobiYz9Mhjrm85EQxMqQF_5ATZXOXVxRLHgQ1-DirVWxD6c1O0_thT2Y8XHlmYHJDTktaSzi7UJE1gCsE19s-kyFfhnzFEMwo47bui14A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جمال موسیالا ستاره جوان بایرن مونیخ تو بازی امروز بایرن‌مونیخ دوباره غش کرد؛ رسانه های المانی میگن موسیالا مشکل‌قلبی‌داره و ممکنه پزشکان او رو مجبور کنن حتی از دنیای فوتبال خدافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/28014" target="_blank">📅 22:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28013">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZA19hO8xgXjTUC6tbCMd7xeoi6lxy7xleKnLb4iKLSFQ0hSVcLCp7GkOZW1YzU20cCBoj3ABhij7rcLiydfRpckq65v0qT3GzfOQ4NkntFWkNnBRkhz0fNFugHEZBYlY0O6LNHuiOc2ZYgGlAN6xaUjJbVexZkE-w1acqLTuxQL461B-m8iU6LtmaoWC3d8IbuJkzVpSspO78SADfa5Oqr9afiFb7kgtTwCEQqk0XmaFlTJvAURbLzF5txcptAfvmFD7OqvLUlTJOSyny4KUja5rsVKL7SPHhPwLNrOjZgPk9GMAlMp91XsqpKxK_LvEN6KcKYI4iPaR3OihXl6YgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای هفته‌سوم و چهار رقابت‌های لیگ برتر؛ هفته سوم دو بازی فوق العاده حساس داریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/28013" target="_blank">📅 22:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28011">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YqFcRtkCimUMDxdov6R7qzH48gtaP4SeRObGWrhfOSSuHlT1hFXkvq7WvHJN_xEXUKvFD4QROsWO6nk9Q0FG9e1hfFJ9tTAyiMXdE9aYHilt19DQAG0lkc2tDIlDhxYIE2uXweSQPd94PaVE9_JD2SBkfzPHKoDr3lQZpBOxLbppsXQyGX9jw6R7GPe0uyGEybPZRne9cnS3hvVjBHMa21dxkgQ7tuH0JKUokNo9d6RGKhcF_ep8_YYcyzRtl7xBpT53uHiU6mojX2Q78PIzo2YM2sW8gDWa4dNgQm5NTblzLnYKxCnkdqqsuhPgp91Q18Bwb6-h_SsnJwCoNvGPsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qq8EoIES_roEmqhfKc27cUaUbi0UWJCEHH4EFBh2amByVcruYFPAzO2LlIfPL9KwDO1ZiJbtUxQtyTGcUaXh22hW5i6tSTj0aLb-l4p7el4aYSmOpPI42eQA9GoL82zhgq7ZQeIhYNQ5Ocg97_re5c6rh02fvXCabQFwwDN-mkr9TttfaD98Cae376bUBMaBVPysEZz_lIQTGqqBwdWlrMUUwKyXRbEJMqrEl7ajbDyVXS1pGHTBUsSmadgHS0Ok37DsWxztvRGsQ7nfg0PMD-WDZ85av2KFGzamutBOcWyycRdhEJd8JDsbObV_LbyPo1uTGwBh7CkTA-dmoirv5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول‌ونتایج‌بازی‌های‌امروز هفته دوم؛ ادامه مسابقات حساس این هفته فردا برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/28011" target="_blank">📅 22:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28010">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/liEJHelQ_RswZaI5nrni03GXDB2vVekr4jR6wVlInShi5wLifBgeZ8ZE7ZF7UmEgmA2paZGRD9UwEbVj_5Yg7hkKE0_4BrgWlmzrrdlc9B0PQd8k7KePduMEiuQPQa7jv7_lFxZoBjvUrxfFFd86FjpCT_uHdR62WxO7lKCdDZdwaABv-aw8_MswM0T39PDoGu9PMqG2f7mgiyvugWEIDYhmrKhYLaEAawzwI7c9VzLLLVtbJ3UgxZ3_dFBJrGi5IUdw763MdscgihMMIgcwSP-j0FN1AzzoZh0fCAaSa-A0Qf4WvNRm39okHv7Zd0Vkbbwp9--JoJ-EFGMfq_epoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ضدحمله‌مرگبار تیم جوادنکونام؛ گل دوم تراکتور به سپاهان با دبل دیدنی حسین‌زاده در دقیقه 90+2
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/28010" target="_blank">📅 22:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28009">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ff906fcd0.mp4?token=OsOkaggkGwCReN0dzDRI4nTV4AIJmr5kAhPNuvaIhcWNL5u86o47eiea4Cc62RUaEu5DBZ61tztYQUg_YjWJA4ujA-z5HLKIiVGks_DQxb1BTYfN2lfM-sr3NHTdvAGxj-vkSMMkOIuqc3OF5cYuT6fsIrblWxten504wZznwWxd-ZkpALgKez6bbeZ4hP-IzNj9usgu7zeBbsHLa96V2HvXW6tkeS02qkgPDKjBnT8351AVAkjrqI5D6gQgwdZZ1RpxvmkDxWUaQ2Ujmnj_fa56LE5jlGAn0ZAG9nuPhFWNbGdLWgz-UMqH46AX1u3W_E4F2kfaX8xYuLdq4pqVxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ff906fcd0.mp4?token=OsOkaggkGwCReN0dzDRI4nTV4AIJmr5kAhPNuvaIhcWNL5u86o47eiea4Cc62RUaEu5DBZ61tztYQUg_YjWJA4ujA-z5HLKIiVGks_DQxb1BTYfN2lfM-sr3NHTdvAGxj-vkSMMkOIuqc3OF5cYuT6fsIrblWxten504wZznwWxd-ZkpALgKez6bbeZ4hP-IzNj9usgu7zeBbsHLa96V2HvXW6tkeS02qkgPDKjBnT8351AVAkjrqI5D6gQgwdZZ1RpxvmkDxWUaQ2Ujmnj_fa56LE5jlGAn0ZAG9nuPhFWNbGdLWgz-UMqH46AX1u3W_E4F2kfaX8xYuLdq4pqVxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حسین‌زاده‌ستاره‌تراکتوربه‌اینشکل دروازه سپاهان رو باز کرد؛ یک شوت محکم به وسط دروازه زد که با اشتباه سید حسین حسینی توپ وارد دروازه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/28009" target="_blank">📅 22:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28008">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e991a4e87.mp4?token=Jeh6iSlo6ofToGEb0nqnO5hHuZ86X2_JR5vCGDo3mRuhctNRUuo8n6zAg_uihBgntH9ivAv4YY0nRcPvE1wJrWGMB2k1h8aDQlaVMBUCFF1wwnHApJUgdAeesR7nD-vgAIQSO5qJvDVGqagVHUmYai0BNz2Por_c-Q_ycDZLXu2Hsf7_4d24b_n0QOnjIfZHjziEcuWZ1hNK4yyA8xa4b_GymUgbxiuBSBXtPNDPyQui84NJjiG5pAkFLD6cKCR7avwg0N1ROGR3z33LZvDsghDf71EFdUCiJHP1rz6ZjLp9oVVJYcmNuxbDpMHmO8UnHDrNvTOAROGR3ijmJgKjIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e991a4e87.mp4?token=Jeh6iSlo6ofToGEb0nqnO5hHuZ86X2_JR5vCGDo3mRuhctNRUuo8n6zAg_uihBgntH9ivAv4YY0nRcPvE1wJrWGMB2k1h8aDQlaVMBUCFF1wwnHApJUgdAeesR7nD-vgAIQSO5qJvDVGqagVHUmYai0BNz2Por_c-Q_ycDZLXu2Hsf7_4d24b_n0QOnjIfZHjziEcuWZ1hNK4yyA8xa4b_GymUgbxiuBSBXtPNDPyQui84NJjiG5pAkFLD6cKCR7avwg0N1ROGR3z33LZvDsghDf71EFdUCiJHP1rz6ZjLp9oVVJYcmNuxbDpMHmO8UnHDrNvTOAROGR3ijmJgKjIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته دوم لیگ برتر؛ ترکیب دو تیم سپاهان - تراکتور؛ ساعت 20:00 از شبکه ورزش سیما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/28008" target="_blank">📅 21:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28007">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/9321265911.mp4?token=LYb87Fjz9q1PJn8xYlX3jklTov9r6mCCB2aRhy9KawE9baL2mUay_EvOzgtc16Pc6YbO-4irEDZWNMTLXwojqePZs4YpwQdY2Gzvwvr_OnzmniXgReIaUzxOzsqhlgwdaXYaqMpHXMQj5Us0-et8p_Ky0bB_Yj-rFtFg5gZBNM6R1fCJIJt4jFQu_QntJSimqVDXFCZW2JSIeO1V1LFjCYffmLw3_kfbU4UXAhZi5ZX92tDx0OvuVo2JpeOsKz_U-2m7eXZvruLDRDffo9hrbp-i694De1Sd0aw3r_dJ095pMte87hLEPBgo91R-3rUlUpFJfcU65X43jcaxStxaiw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/9321265911.mp4?token=LYb87Fjz9q1PJn8xYlX3jklTov9r6mCCB2aRhy9KawE9baL2mUay_EvOzgtc16Pc6YbO-4irEDZWNMTLXwojqePZs4YpwQdY2Gzvwvr_OnzmniXgReIaUzxOzsqhlgwdaXYaqMpHXMQj5Us0-et8p_Ky0bB_Yj-rFtFg5gZBNM6R1fCJIJt4jFQu_QntJSimqVDXFCZW2JSIeO1V1LFjCYffmLw3_kfbU4UXAhZi5ZX92tDx0OvuVo2JpeOsKz_U-2m7eXZvruLDRDffo9hrbp-i694De1Sd0aw3r_dJ095pMte87hLEPBgo91R-3rUlUpFJfcU65X43jcaxStxaiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جمال موسیالا ستاره جوان بایرن مونیخ تو بازی امروز بایرن‌مونیخ دوباره غش کرد؛ رسانه های المانی میگن موسیالا مشکل‌قلبی‌داره و ممکنه پزشکان او رو مجبور کنن حتی از دنیای فوتبال خدافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/28007" target="_blank">📅 21:40 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28006">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkcWsYEWsI2l2uF3Ap0UMAKh3HYBTvP5Fs3NiRKBbVWxtG_dp5XikVo7qYjCV3k8jgBSLuQR4Hnf0NYk0etEYi8AQ6VaI49rvJ5cyXhkk8-FUeBuTDXA-Ea6Ll8lPXyBbgEi7raHGqN77wLTGdiQ7Zp-nbqB4ulR4nUCvJ0gRUL6V0ZubOBZYiqdgQxQivMaTQw60CXFVQuoUmm2Y2Tz3rijtFxlWNA-HcqJjyDgQ-DNP69e0g9iHHQM5UyS796--w9Q4ZSDfIu3yxLMm-5TYpi1ow6_Z9s-mZ0L0FlpL3JNWeHhp_ZAUcb6D7ZhVSopLAQY3r_kwGPUrwlzE0zJPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔴
#تکمیلی؛ طبق‌شنیده‌های‌رسانه پرشیانا؛ دو باشگاه الوحده امارات و پرسپولیس در آستانه توافق برسر رقم رضایت نامه مبین دهقان قرار گرفته اند و احتمال دارد بزودی رضایت نامه دهقات با پرداخت 500 هزار دلار از سوی اماراتی‌ها صادر شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/28006" target="_blank">📅 21:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28005">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYydiL-Oew9Jl4r9MqBfO6csplB6VCE7m9fJMGAY4MWjqH8xdRv4v_n3NKSc1Vl2LhLQjsnw8jPr5j1TJkRn6QK1IFEi3oUoUXUUct9e_MIn0qUgfPX2kY9paJz8BI_7ElZjMAZCCb2jQInqxj9C5DivzIz9ETyG_tZXLEfCIM-mXYjbDzbgJpjVnpfI6XyZyQxlm6NfHxe7O8RV3YOrsggZqU50ihjwr8tLxetd8217rADOG1EqG28gBxXm9kk2X9Ug7k6fIwY9W6KH8cPhKp9sfGeeo535lIWhSo1vfGXZdWX6FBl8ZgrTEoRyLMa5eT58UTfUS5lJdjbEj1xT5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌برتر|دومین پیروزی پیاپی شاگردان بختیاری‌زاده درفصل‌جدید بابرتری سخت و نفس گیر مقابل شاگردان حسینی در وطنی قائمشهر.
🔵
نساجی
0️⃣
-
1️⃣
استقلال
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/28005" target="_blank">📅 21:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28004">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grts5ojbttJ6sxQgBWyLqKJVlPPAsqDK0OjIaJcI5sKvwrLXpZPa3Ll0n8MqH506P1lhzOCMDICMXFJ6df--AagX4naNIrVsZSSLghiP-bbawrMG-4YNd3l5tNV4fxFtFsUpoZyDiafrPgp85dt7gfsRMShEjVdK3VFCC207J6P5BmcYs6XxXgisS_ytrr-k6CMQ9X8PStJwOI2fPHFvHTElxqDlb2NKY8sFyJaipEGhzMxeDU624wqGObVoE-C5FrL-sMgLtuHxVor6Xgc2jAS3WaA6T06vliAjux0X85iCG57-AsGIp6Qzh75L7OWe8u4B4JszpqQx4fFyGMZP2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
گل اول استقلال به نساجی مازندران توسط محمد آزادی در دقیقه 81 روی پاس خلاقانه آسانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/28004" target="_blank">📅 21:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28003">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f447a609fd.mp4?token=VxeC3c7CCrXkzg3VU3glDVhk--Nhb6xHCoB4It3E1FRehlakUORKwHkcJcufLJY3TQ8bNXWuZaOUHxbdM1aGpaDoVd130U8J-ZAgPf30OLF8-ePlHkW8W5A7ONnoGfMHSdpxX4rKhRhZ7cIdAmWIv8r_j4z40iUcsXECPC48wORqUUusuN78p-NAmJDcp6NWhnHuiis8q3bdKguFZgYNtI_LaS0focip-DSjr6tj_xI_XBLuJTgh-_Ts1oHOB4xLUOqL_si6SFpniG1IuBJgrCrwQ3519IdHJc-zgWN7a-VY121Cx7qk6j7SzSbRmXdp9w8aYbB_Co-OkJFEanFOhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f447a609fd.mp4?token=VxeC3c7CCrXkzg3VU3glDVhk--Nhb6xHCoB4It3E1FRehlakUORKwHkcJcufLJY3TQ8bNXWuZaOUHxbdM1aGpaDoVd130U8J-ZAgPf30OLF8-ePlHkW8W5A7ONnoGfMHSdpxX4rKhRhZ7cIdAmWIv8r_j4z40iUcsXECPC48wORqUUusuN78p-NAmJDcp6NWhnHuiis8q3bdKguFZgYNtI_LaS0focip-DSjr6tj_xI_XBLuJTgh-_Ts1oHOB4xLUOqL_si6SFpniG1IuBJgrCrwQ3519IdHJc-zgWN7a-VY121Cx7qk6j7SzSbRmXdp9w8aYbB_Co-OkJFEanFOhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آمارنیمه‌اول‌دیدار استقلال
🆚
نساجی؛ جعفرپور گلر نساجی با نمره 8.4 بهترین بازیکن زمین بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28003" target="_blank">📅 21:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28002">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsXE5CUFE-FSGX2KYiakFpO223WCplRa9STCguijqCbR9bw8bwD6nYYZ_5blfYxu7QGr-oogrMYjm37LsgBrA0LI_aUWBAQmm2JP1cveOJHko59ZpqZvuqV8W3oR3ltKDJxvRm4BM6cSQHygAnQXKMXzLet50eAjSSH4GYgaaOm-gM7Dl5sU7KutSEocfiXvrtL3kTYZBMxU60UJ6MBmMZtpGLhCxiEvWuZewR48jDI_Ktm5oAooqiTfDLIS2aQXPkCnKZ6vZdiyexzfKdWYqXFkIeV3-gIIlrdglUR_oVsihzm5kmnFCh2rRogZk_hGIDJmdmCsQUGIXXYWvj4I9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ به احتمال بالای 90 درصد از بین مبین دهقان و محمد قربانی دوهافبک‌جوان الوحده؛ باشگاه پرسپولیس یکی رو قطعی جذب خواهد کرد‌. اولویت سرخ‌ها قربانیه درصورتیکه الوحده تخفیف بدهد. هر زمانی اتفاق جدیدی رخ بدهد درجا در کانال میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/28002" target="_blank">📅 20:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28001">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a08f75b6c4.mp4?token=iMTT7wxitRQA5e6XH4XEsq8mpszm12IwHno4FEdXC14YWe1TxClhoVC6AAsg9PR5jngMcK5huUV9KYl22OK57VQHSrUTEa8gdaCExHSHbz8JVCopHBAWhGPajngEJSdNkvTYlBXvSFm_9NGTyxONB4dd1RheiZtnaKxZwHRc-sUxaGnvgdtQHO6shwDSR5E3IOv2gFqhfIhnJN7R-vMwDx9WXcLj1k5yeivEt1Pc2k8NFxsVCG897rjwjXZW10kaCMxRcRNMa6U5_QAEay9bLlzz8LrI9S7Spt_vuL1t_i03mMVLesWm6IViMz0DpVVN-CbVt4MFcUEkTU6tMM11Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a08f75b6c4.mp4?token=iMTT7wxitRQA5e6XH4XEsq8mpszm12IwHno4FEdXC14YWe1TxClhoVC6AAsg9PR5jngMcK5huUV9KYl22OK57VQHSrUTEa8gdaCExHSHbz8JVCopHBAWhGPajngEJSdNkvTYlBXvSFm_9NGTyxONB4dd1RheiZtnaKxZwHRc-sUxaGnvgdtQHO6shwDSR5E3IOv2gFqhfIhnJN7R-vMwDx9WXcLj1k5yeivEt1Pc2k8NFxsVCG897rjwjXZW10kaCMxRcRNMa6U5_QAEay9bLlzz8LrI9S7Spt_vuL1t_i03mMVLesWm6IViMz0DpVVN-CbVt4MFcUEkTU6tMM11Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
رودری ستاره جدید بارسلونا به طور رسمی معاینات پزشکی را با موفقیت پشت سر گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/28001" target="_blank">📅 20:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28000">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOeJI-CN3FAzUNyNAPv7RwvtlWM0FhvI9Re1F2njy5MEdo6cwa0JD5rRB5tjX3Qwua7xvWlJVdo_7eeMmBlpqXDOZcmJaQuQIX_FLq9ZrbQtI2ZGXo5tClJm8PAyv34okqtb3GJjBYWkzXsHORfXalS_UJ1GJ_vRIYXU0ppCImeECdStm4PoYRYXxgT-Tng1niKDVY3WqGiqa_1wzSHDCqeqr4AyeXI6fZKTq32uSO0qL8F6FzAov4lTxmouVwiw2Zoq5g47QEz9KsSHzo8C2cgjWIEDi5q6mrVIpIcMfep7dYufNZhBhe_UnjIdwCmjMTItYn7mn9BbZPtp1PPv5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیما امشب تسمه تایم پاره کرده و لوگو تیم‌هارو به این شکل که مبینید اشتباه درج کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/28000" target="_blank">📅 20:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27999">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktjYgK79jN8F1l9EGwGj__ndC65QHo0Zmnek2tFWgIILMhyZKUdTiAHGUdoFouMpl3gUBVdkIyhgeDcoNo3JK_Aj1U_YE8yYmpfodjybXklX3IidIR72Lv6wmilFrlFe28RWqdYxf3Gt8Ji8JY6iF-DFshc8slAvfsSNu8zavVXTsCdSMzcyumy8f_Vum0W73lO9hL9MD79X7mSzOL67xxqREzlMg3EIdVH3_ogMfZeUmZa0dSOuUG2cZacOwcN-7mRAT8WYQ0-Np_oFHICNIiwGfc7jxIslpnwVToJy-UNHc0H8C13IYQty_yeyl6rEyQEsBgsh_NWefsnSeqyQXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحالیکه فردا مسابقات فصل جدید لیگ نخبگان قرعه کشی میشه به‌دلیل‌ اینکه مدیریت استقلال نام کشور میزبان‌مدنظرخودرا به AFC اعلام‌نکرده اونام گفتن پس هر کشوری ما بگیم میرین بازی میکنید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/27999" target="_blank">📅 20:07 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27998">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaQtqgo3fAyt97HLZONmsuoG5Iy39TPyx1ws1ls_zwyWuRY_RTJc3YX6GJioHnNyhXeRwWTW_I-AtFq6GwDiEq375-8S7UJ1_REOachjIcvxuCN6lsrfMfNTVdzdxDxsfVZgnfUbdVObVpHPa7YiPgyPIp7793dnPzmZHVi47nF617D2Fz6WCO6MB_Wm1LMF5yegLXOi-IAL99diyKu_b1klmukHLjOc_7awvPAHMw_fJF0de9h7GtiGNKYWxcw6WcEy3UOpW5a-L3cBTfMfOZ9V0-nqR5dGRHwUSmyJ8-VOH0M29s7nhxreV3xhdeomazaelfZf4wnaymiCntRJOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
شماتیک‌ترکیب‌تیم استقلال برای دیدار امشب مقابل تیم نساجی مازندران در هفته دوم لیگ برتر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27998" target="_blank">📅 20:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27996">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JJoivyw4lErf7czqdap3WSIHIh-t4zmtxdVHgbKt-l38FGLV9WhParCO_UIA6gtu2PaJvcaBuDfGvWTskDgflqBEWi2seFwBZuwA3C_Og0O2wwXgkGWIraUOsgEpbMGeKUcyRs0XVOxNGQjeasj0d8j4zKNAdZcbR71FfNIsSWztkkcY8R-8zhTixdo6CJos1eP9VC1XFTmVR5Du625cHVQJVYQVEbQMnhC07j9pQmv-vrWS2VOO1O9zCrwSkts-Z2Dg-7VsldYTXGNGrP4GYYr3s-DBpgCy7Wp6TIrwcIQCG9TtdqtuAfQCdLRpIL7rITZTnDf7tH6A_ytzKE9pAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kg1F6yVyuEXIBeM-RINkAgWliii29AsEjmtX4bG7pfY-OqKRO1CtGDG-T-96tTc6NafdeOfBdjx7jnIgeyhoenz1OAJk3K4wqNDujREUSBksRXWzzYCoFQTKBb4AnTpmWWTJQS5ytNtOuPGRJCRD0qLvYk1uFrAgs5Pzh7vTj1sTEhjyeg5AxBegUnBt1Jc5242Q-u1A3fwLNAhk9DMufLh1T9irR_Aw7Gi5GwExrmCNcylw4zKADx434OiC6dvb1mz71BkZEmFXUQyzJr9DfRqxG9nOOieV_fGPkztjTygN0bTK_JJkZLL2uFbNLtNXrBx_0Mcj-8vhXq8n4m7tgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟡
👤
جواهرات جورجینا رودریگز جون توی مراسم عروسیش دوتا تیکه لباس ساده‌ی ساتن پوشیده و جواهراتشم از برند chopard بوده که گردنبندش هم ۷۵ میلیون دلار قیمت داشته و انگشتر پروانه‌ایش ۹.۷ قیراطه. ارزش کل جواهراتش تا ۱۰۰ میلیون دلار میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27996" target="_blank">📅 19:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27994">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oheHFAxWb3LeSYR7YhDnjOemk1FwpE9xgLix4aXRGGuVWU2qNELoKnduSv3CAGO-A5Dt7-4upnGvGj-96mJgHFDDQLL0A-iSFbh3mWGPro_rhHs62u2X79oJ7b5oiZITibBFHwuxOuyvXIvrSdbX9D3f1PUX7Ydmq64QfBNxdBd-TEoBYW9b1hr7a7m27QvjYi6h6QttdDc63IXj7vScI8gngbHkefBW8biTXc-T1odgtyVwxAm46B6ZHYKzKNWQIamnnhIvcb2Yxc-kV7IEp9pxe_CkWLLfYhKd6K8CVrFjNCoIwMPL2YEqMjHCeVahHHLbT1F_dB-tpaLIuuF6WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ULhvBI7Q_xelz4KMIjzkmlZQaokHnwDnaVXbo_bSJdHds2Y3H3IvhcaRPnkceM6JmMP7TePsuvxMgDwCJpqyI0EpMGVZWEzL5jbyN6hhOylcDfUuYnJ1yMIRtiAJm9k411_0mRRt1OihxaPIRxvVDOwPMcLqjFuPlz_IcB_NOAYMUDvIn5Pi2I_6jia5gjuTVez8ilKpJpwJaDN2z07c48zgTUNzQWhdKf-aeiiGd8ZvjW3V7-KpchcS81odf7lCQmxbKykbfrZdSglHLjaqlid_2o_atLrItBqoHovoxy7PBjRSkRw-m8RF5y88cdCLTQnFxZ4K7zofGpJ-WZR-HQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته دوم لیگ برتر؛
ترکیب دو تیم سپاهان - تراکتور؛ ساعت 20:00 از شبکه ورزش سیما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/27994" target="_blank">📅 19:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27993">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3z760AEeWL5rmuANbybhxAS0Rcqgqz1fzbKzsOKNuW0ryGNsAOUgX1L3qOx4VQbN6_R25ycRWMALPC2av9--ir8FIWVPLXxcY5utPu_AA1zL645BhuGpSEiyK4J3jw2l3vM23QRY9ZUYACJDcd9crWnH_WvCdAWxMl_huBE3mqYhiUVGkjd6euCUv9gBYWrVqniyBh8zsNLPirgYjYj6qMwoofAL4Ro13JbQ6MEzcj__0AV7boQL-OIEc04DlGBHljO6B_gSEjs0W1DZsphKfHH_qMePbnKfPgeFoit37RfJMsKfU8AYCEumkmwScUSHjHCWG7gHgI2RiLVQZeopg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
🇪🇸
ژائو کانسلو و رودری هرناندز رسما قرار داد 4 ساله خود را با باشگاه بارسلونا امضا کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/27993" target="_blank">📅 18:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27992">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSIDQXEBeloVgFx_dZ2dIX9x1ZFBow1ScqurzHG58DU1NbnY3bDFdatNpRTn3xppte2-_5EVN5-peVYygSwowskguIHE67GXVDY66rsw_reVGDzrx97izLnD4lSTQIvq3XxJYIyQmsx8izbbe1dkLf6LXnXndEReHqqBjy-62oDAtzXiRWzu0uCo-gD4GciOPUuishGdqui1-R0nHL0Hyk0YW2UQLZHCQj9biu0j_EpcN3Zi_ay5CYpiVVqB2O45MS5t3BSsErqIp40huWCN7ceSYeTygMqvoF2fmrLcoyMvPhQ-oWr65Pr_H1T0NVlT4g3W2Ny9sPDDaODHsoo1Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم لیگ برتر|ترکیب استقلال برای دیدار امشب مقابل نساجی؛ ساعت 19:15 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/27992" target="_blank">📅 18:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27991">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqQA55JPTFFINn9RgVCOO8pbZ9D-ieKTQH35ehJsOtukyqANl7sPvHy8O4aJuFqTwhgh5jiL_3CIAZGrhXNqjFcQGHIkIhoVZxjF41H4l9kNeKMdbynZ-j154nJariIDkAiJ5CZTgzOmHNr5VU0fHG--sQ1hTHuh-A4pOrw3eGpDTtbGssm4Yig2PECZqvZ3ntau4thnDWrrC1JeABpu0aow0MijmnTcpIurafh9yv0u36FOD7C2CYGFbXKr3ictVgWNqaDn2u83CaOYEfmU4iwowi9moPm4RgBRddIxsyrq_IYLEdApyFeMjJ7TkAnsVzT8CRTy0awgNJPU5JpTEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم لیگ برتر
|ترکیب استقلال برای دیدار امشب مقابل نساجی؛ ساعت 19:15 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/27991" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27990">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyNUXSJQtuETddPPtVvFyuVnwRuzZP2e5R22LrnT95Es3pQqB6tXLjZIJnCgpmyu2sQmAXr4d7h5RgJzLlhgbjvuzENHxiRMKGGtdfQdbtnbhUbL-aD0O9S7NtuzsYVFgPKZBcGxWbVW1-nt2X7DtKg8bc5MLT6LnCUai7kndIKvEZ4TlNGaUGLJhA79f7gKGhr-cbmxZhRfoSJ-l1EFJHMXbRFV7na7zH7KWUd6UunIs0cotyBFYRLFvWYw-Bg-1blIq0Ayk66iWljJ2EK2yUWJbOt39tXmNRpfg7V4v2r-d81HDbgpoZG9R6UNq-zWtCCKYD3ZemU1GkqY20NDaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری‌جالب از نرگس محمدی و علی اوجی در کنار پسر بچه‌ای که تازگی مسئولیت سرپرستی او رو بر عهده گرفتند. دمتونگرم چه حرکت قشنگی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/27990" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27989">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3kbmNEt1CCEflZSPhKq9wGEKARZIG8zEs-khnl_HtMjQ3BfCz-_HFf0vxqKmWNxyQLS5teN7VOz_slWDy7qAZNEDF2dT8O8lZ_Fm5sj4XD06H9N-jCo1XLw5hV5kEOkp4C7F29-YrCF1Lp_g8agGg2I4dMQNlE8pDD_Q_gXZ_ZYsAQnM6NQtzNenFdPUQZeaORNiT8i9JR9dqbWU9FOnrD1ORHCVKkIpcCAl4O_8ps21Q1faGW08cnwX0-JUPJesVKjhfJqOno98DcNhBYXBzZ0CvER1PvEziOJ3tn3ryIgtOLwM5yD827_24wABVw2XrPQmyZothsQQsNQQKHaag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته دوم لیگ برتر ایران
🟡
سپاهان
🆚
تراکتور
🔴
🗓
ساعت ۲۰:۰۰
🔴
انواع آپشن پیش‌بینی برای این بازی
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔹
http://betegram.com/affiliates?btag=3_l7
.</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/27989" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27988">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSsmwk9FFdvZazfnEXvkMxvoxNockCrNZmb2z3jLVpxadMrFxSUJXlfF9Bj8RE8SVhthsvRbZ7Ofuza7aRFba0uo5QgtobHNrq6nVguiDSuCzxV6mwK0FMcU7Tm1y19nOvtCQ0BXQ84_s3V2ZbNxlsZd8oHcGgBObME3ewV4fa8YFfm_tUjBgfaotxvszT-LM3VMs9FtGZ5raVKPtRo4WtYn5RvgKlKG7EpLYUHwLfFZ74gQ6GmiqxcE8FBtknjw-wdYbwkndxjeTkCL4cHjntyt98-FfD7u4oO9uHbPQ0HoqZPBmJ5MgtVaCpDwsa1DiKLdlRaK01YKcTGkwRycDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
مدیریت‌ باشگاه‌ لنس فرانسه بعد از پیروزی یک‌برصفر این‌تیم‌مقابل PSG در سوپرکاپ فرانسه؛ به هر بازیکن تیم مبلغ یک میلیون دلار پاداش داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/27988" target="_blank">📅 18:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27987">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFYXL1_QIwR-ydspiTLw-BRFt1ywTyi0sH1b_f4mWv3CEelfRmUVLpJ_SRgUhXONIciad5gUoZmnzVAvzbYcQBPoCrjaYsZgz2S8YSwrE6bvbzvIAECrQg451YCGPXYFx58t4QYMNNQu8xYbCv3PRH_1Q3pM-oUnWNYepMGb0T_UbgYvO8owB1Dw6_bHjC9y_dPxl-cxqg_7E3AYhad1dc15Z26iEEi7fTkTBUcVG8y91UeCE7lzkXigntbcghhOlfkqkhgnBcXQRAPJoMuwygt3sU2BvA9RX4GIGtdsN7Lps2xweE_E7vBb39OpogfSn5lDl5jJs2kV3CLiU3W-Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیکولاس زوله30ساله‌ای‌که تا همین فصل پیش تو بورسیا دورتموند بازی‌میکردالان با این شکل و شمایل داره تو لیگ های آماتور و محلی آلمان بازی می‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/27987" target="_blank">📅 18:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27986">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQKrL6_nPSrQXIkuWwpNi86qscYrC4d2Tg6LIZBRB2EaTBEsGVCot3uAyrFU58m0Rh1Ia5bIU7A0ZdIV7pep57jbkN9GK02xLYlzJSR7IcgC8zomtLPIWM0ZAi4UvvrLiDkuuyinq1IL_-ajd46iTuk170wQBYBqOEh4cllGA77_zm871nzj85wnZ7oepg6jsFKHPCWFAZP736pG3gvEBbyc_vKZkbWtNWwn3JuPLhUDU62vtbbhRyaJLyaYTFFyMVPiseR8titgCsL-xWU2cv4CTJAgx4Ks9p9l5CinpAWYGWej8XUCtX41aWHMgO1j0c0BCmTFgvvXduU_IOvJ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برخلاف شایعات مطرح شده؛ کمیته انضباطی فدراسیون‌فوتبال‌امروز اصلاجلسه برگزارنکردند که به برسی شکایت باشگاه مس از باشگاه استقلال به دلیل بازی‌کردن‌یاسرآسانی بپردازند. رئیس کمیته انضباطی هم اکنون در یک مسافرت‌کاری درشمال به‌سر میبرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27986" target="_blank">📅 17:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27985">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1E40ZbMxus45b-LdxsJz_oZBg2Di_gx51QjdNMFC07QlQy2FQEsuRb0fwPh7UycyTOKrkKeEY5RfZWgma_l5CV8SNP0HNqORA7tDx4_2dQRPXzUttN9q1TM1ZhPSMDHmgMvkry4bEfJFy2d1DbKHNRr2Qg8MfaSv9-F731QgSUwVbuU6W_y10cvyVL0Njx7epCzzYbVC91SBi8dti8t8tyYTWMFzTK8IDNw3ugh9DMZizQ56cvGy1sKAVkm8YX36Z-ScBPsUPkMUSHHgyfYW_B8gwwGD-Lhpp6jHLKhFBR8nEwaT5zL5YRrC9s_IOtbd8_LLZzsO2MRttgseMfnoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رودری ستاره جدید بارسلونا به طور رسمی معاینات پزشکی را با موفقیت پشت سر گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27985" target="_blank">📅 14:47 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27984">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxKmzguw77_CDJ3qo114xaQ4CdA0vzLoRvk7J3aCIxUexz9vIb1Y_wJ993xPzpyfvBuWEHW9lAWN9pPM8BSdgTGEAgQ0bqmtZuXR0sG0P9QEPoNC6WUsmQqEd7A5Yo38MVgNF6e6BfOyNm0KmDm48dQrHyqsLdAYMVGAgEEWWwyDUUINk4Cq7ScW-JkNENByM0dZJ9PROPEooqrHgqskQCjfo97h1mS5_wQoJO0aAKmSf-yQNfKZxaswwSVgIisP7Ooh2eWvKlJayIQ7nbpAWo4sHq9q-HofSCh5H-kGarok7NXH_hIPCFqnynLfLHHBzOWX0OT3wJIsN7u0rfkc5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی پرشیانا توسط کارشناسان حقوقی‌فوتبال: آسانی مشکلی برای‌بازی‌کردن ندارد.
🔵
هوشنگ نصیر زاده و رسول باختر دو کارشناس حقوقی فوتبال: بازی‌کردن یاسر آسانی برای استقلال کاملا قانونی است. درصورتیکه قرارداد او در فیفا و سازمان لیگ فسخ میشد و قرارداد…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27984" target="_blank">📅 14:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27983">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GREJ9PYeOANgCqY0K_QXTxyXXCZfjTUULRQjksrPSSKQcc09fB1UBfWeLT0krjXN3VQfZn-x7PUOBqiDcZNGRbHF5fYuu1cngKicEA2G1pEwV3MhdNr3NjVLaU_raXF0LSEa5lVtl7OO705O8KQbcyFtT60SfN2cccu1maDfDUExtvEwiOGwJaJBYUAFVJuxTSX0OpZ5Ldukdiz0Sl-kJ9DVgGQbRtFDVWfcktuInMleyIkM97eF5IPiDtSIMm96GaYSSOqrteDO3V-4dFq5Q4jIj8Un4A2UR6V86dKoDqzCcBwryFIG7V8pOM0YfXwalpJF0OhthzuwyIIVKm01lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حسام‌حسن سرمربی تیم‌ملی‌مصر شاهد درگیری خشونت‌آمیز دوهمسرش دریک‌هتل در ساحل شمالی مصر بود. حسام‌حسن درهمان لحظه بیهوش شد و به بیمارستان منتقل گردید در حالی که پلیس هر دو زن رو بازداشت کرد. مجبوری مگه ۲ تا زن میگیری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27983" target="_blank">📅 14:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27981">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpN-R_2YQiHnkqBaX3l_xjixTYJvpSjez83ybBkW8xK8MpaXubjAoAj-pGO5NX8D6jXXJ_D6vu4h5bFqQ6PnrrA6CwERfH7fKUd8H3r5yxBy258WkktWyCI-8vszDonql_D-2bmXXnQfu-J5A99IjUBoXXUltX_EQfIqVnkRwVKGlrz8LtwN_BZ53MUnxIK8Sg86Jyr9SxAuYUPh5GKNCWU-jfd1O2VLjhY5y0DVMyuBEmr_IG6As_8gNHTY6u91K6ua359IKvgY6K0QkXK096sPzBsFYVwfxTkJLrX8InNJ0P4KMcJdtgR43p2r74TH0KCHYBbr88pKhX9QzSdXoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رودری ستاره جدید بارسلونا به طور رسمی معاینات پزشکی را با موفقیت پشت سر گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/27981" target="_blank">📅 14:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27980">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAWlWyfSw7OEjRby8qzA7L-WTrfmec-pasqqnD2XTHevqza85BTheF8TncOPSxIl2N4ASAHQQO0YjCK_6iYpVkut-9GKNee4CY0t1YwZ4OQScWH4c-LLW0Foe8rO2oB80oH92YGu7Wc9CZjSsRUhmvjDU36FlLek41sp7MeICpMCyupwrhZG5ozjhU5GmkBAeFfGkxMveZRqJsAyHqNuJgmXDDWRmPVggrr9vO6o-UHPwxaVVIMNvOVwKcTlVg0e2xyKpBhcB7ZrUbYX9OT5xi9Ho_ifzKW5NTzCon4Yss2COms2uoBFS0Exqj-4saJmIIdIX_Uwwg_HdAgsnrzCcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ رامین رضاییان ستاره 36 ساله سابق استقلال با عقد قراردادی یک ساله به فولاد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27980" target="_blank">📅 13:47 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27979">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQ-DGhmJzEI-uIo9i8a2HFcqtlz9S1g-336SA8T-0m-Gig0In5BCprDcMQZhPgxk6A1lDhvBwVbYa4bhILDCCWF-ekg8nwZyoQ5Ix8KgEGwRjqnG99T_X8Gvaqn5FoHcky0iXUkHh52kRbmzo2A0cqeCOjhEmsYMih6Ey1c_uBzWNeoy7i4rcj9lgBWKpoFMBT9A7c-sO8VlnMP5vf2mum0uMimirxvmVLwdaYLWGWzhfXVI5KKolNF95E9eNXBIO48_gviM2KOHwS0cn7RHuvPcwSR5AD3AAK831-VZAom6oDjKG3emSkFGSURNQqKmv8GDZcR3CJP4Sljp5miTng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#فوری؛مدیربرنامه‌های رامین‌رضاییان ستاره سابق پرسپولیس، استقلال و سپاهان برای قرار دادی یک ساله با فولاد خوزستان به توافق نهایی رسیده و اگر اتفاق خاصی رخ ندهد بزودی باشگاه فولاد از او رونمایی خواهدکرد. رقم قرارداد 65 میلیارد تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27979" target="_blank">📅 13:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27978">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUPTOvvyzBvcH5EiOrnPn4FoqZff0gtxuskOhkX_1JPAOxtouNnjq9fBzDcEea3sa5dCUSkodwZ7o3jLdcVfUsHh6pjN4MgndDdtnCzIxEcKcHrqKsIjttk9jKh9igRuzBJRl14U-DyskTuqf3_w6FVrLTgbKz708-7rGFn7myLiPNVASIpvB-pKjeTs0fziXczqzWz9F3eiW5id8_OVJQBJdCYh896YRZvMnxMRHhnJjYNITnXci0K-RxHOlT5bpYHnFEYXaFEFwhvekG9uDZt6tEFY83bf506KEaUCZ3Mw5SGe9mvWVJqMhquQI6Ixn4-z2VKGy5wPY_91dPPCcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ به احتمال بالای 90 درصد از بین مبین دهقان و محمد قربانی دوهافبک‌جوان الوحده؛ باشگاه پرسپولیس یکی رو قطعی جذب خواهد کرد‌. اولویت سرخ‌ها قربانیه درصورتیکه الوحده تخفیف بدهد. هر زمانی اتفاق جدیدی رخ بدهد درجا در کانال میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27978" target="_blank">📅 12:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27977">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DX0QZPjn14V9Hq40cf0zW7q4OA9RVRkJDjpgRnQldzlNmcX07Dxc6MH1OdJy2ztKf96cwvoKKJw5-JMbF-1RFtYJ6LJbspoqyiXmC3HEA4v6oah15xTbLFCr93eNdzlw5bsewoHAkFRaAn3mWQc87Tp4aTnsrYH29bnNh-f-l49iI6lCJ5JBAWJqRoi4nA9rQrj1EeugUTWgTLcWuGyyc5g7uMJjhTV80ZThYvA4AiGl3wv_msLFoURDouK7tovwtYNfwG8m6z9GwqFFIqkvoe0xydCivWo7J8BnIK39DVrNtrG4zwNMSMtJVn3l1_ZSo9MH6zuxnvQC2vdqVHZjZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ شانس‌بزرگ برای نمایندگان ایران؛ نه استقلال نه تراکتور هیچکدوم در مرحله گروهی لیگ نخبگان به غول های فوتبال عربستان نخوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27977" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
