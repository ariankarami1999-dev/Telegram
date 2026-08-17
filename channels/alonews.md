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
<img src="https://cdn4.telesco.pe/file/MTLAxeaui2u_Zq6hgfHRnz6xUtsvPzTZOtnbY9LJpJ2D8XO6SNwxZaI9exg4rqLHDw9pWmFF4ehG2LrpgPWwgQejErWrAFDO5b1STT7CIwyk0uu1jdPM4QgM_DqnTSACtvA9J3gUSmaKBUK8XQACdC2szPWZawu3Bgu8D_q5usyXZt3wYLqq40h6vdB5nKpvNu8zA4wM8L5Fr5y60tjsSuCR41dMYAAke2KSdb-jVMfX8GkK7Cuizn4FAi6sp0Yer_iZJNf16Ak2UsI--KjpiVCpeAl7T9ciV8E8wqAnjqj1CkOnwkj5N8MWqF7Zk5wvurrEe-8A75_JuzELiavguw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 976K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 22:35:44</div>
<hr>

<div class="tg-post" id="msg-142324">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845779b633.mp4?token=k2ksbzlMVJrGvVCREfYml_ebIQdF8ct2jbltAumxb4QubSBdrABVss123wmYnox_u7TGDcNaztccvoQnnOF0qkl0M3vfS0OEGXEAh52rX6TGqRZy67mVQI8lVyyV49fz7_q6gZa0yMAkNpY3dHcusX6OoXb4QvaEFSh5aNrFAO7pqjhDKop0suZeyO_7V5VwwYu5Gf13wqZQdjF8kWYZCrxv5UicA4RFEYWHT_7HXyDLOA7o1zKZ2WbWLGUL4i_RAheK1WOBlEdtgQ12F4MXNPjGbYc8FXSJzBBBlLIAZY1uzWu7EP26kSzGpyCDhF6b4Y9BOpE9r0Hlovq8LJ3wl4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845779b633.mp4?token=k2ksbzlMVJrGvVCREfYml_ebIQdF8ct2jbltAumxb4QubSBdrABVss123wmYnox_u7TGDcNaztccvoQnnOF0qkl0M3vfS0OEGXEAh52rX6TGqRZy67mVQI8lVyyV49fz7_q6gZa0yMAkNpY3dHcusX6OoXb4QvaEFSh5aNrFAO7pqjhDKop0suZeyO_7V5VwwYu5Gf13wqZQdjF8kWYZCrxv5UicA4RFEYWHT_7HXyDLOA7o1zKZ2WbWLGUL4i_RAheK1WOBlEdtgQ12F4MXNPjGbYc8FXSJzBBBlLIAZY1uzWu7EP26kSzGpyCDhF6b4Y9BOpE9r0Hlovq8LJ3wl4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آیا بنزین گران می‌شود؟!
🔴
رضا نواز، سخنگوی صنف جایگاه داران سوخت: تا الان هیچ تغییری درباره قیمت بنزین قطعی نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/alonews/142324" target="_blank">📅 22:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142323">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hv_E8Fi6zKfQ3DwPpsy-97Nj6zW-dMCNGYVtDft2KJK86VtKXvycV4d_GR60mvW-ZStG2RRG0OtStfwRHkNe9Av71_TcfgbC7jqY0e4tDb6KgjsHi9Wx2JAvUt9IAzJOqOyosVJ61xl76WwuTnzDMRLBwR1ZTnQGmg9wJaJQXk0f4-LX0SiajLR8dd6DvJLI2xh9WAJ8IOreCBmDlm47ZtJudaG4TP6IPl8eEsFP5jcNIjypiBFd6YW-vKsFQgSpOa0L_pFuK9TUXFsngq8NJJYorzAAIexizNeBxzVBXW_I4M8lLMAdZZOJLbG8mqcmoe8YKpAGDOsK41AKcjiN2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش عراقچی به خبر امروز حمله به دفتر بارزانی در اقلیم کردستان عراق: هیچ چیزی حمله نابخردانه به دفتر نخست‌وزیر بارزانی را توجیه نمی‌کند.
🔴
دوستان کرد ما باید در برابر ترفندهای پرچم دروغین که با هدف ایجاد اختلاف میان همسایگان طراحی می‌شوند، هوشیار باشند.
🔴
ما در برابر صدام و داعش از دوستان کرد خود حمایت کردیم و از امنیتی که آنها در مرز ما فراهم می‌کنند، سپاسگزاریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/142323" target="_blank">📅 22:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142322">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vI1xWU1jEcNpnaA0cH2a_2fUCveDEhAk2RGCgVxjm73x0JtCDJPc5AiS5LXa4kFVUW8WGBOPe8Xhhaj1BWG_Lqoyyx_uXKe5z8wH7-iRuuCy5b5Bx2uk3-j0sJ8HDvk2b1a_vMAqErrSCn4Ofmd7HEL6XzYulnL1t14zuWYfl8hU_0PjjPVGYMeYPGYEbqjfeIMHAfC_8CkR17HjyyrSA_OYDIN4smGLt6_3QK3ib75QeklwaFzcoph27BBigiUsTb8p9Nmpg9Mw0xDyJZFSbvw7GrM5K4Ot6dv_NBec_taBxffNGbuUGdS2N5LCkVPW6Maag9Vv1WtgBtSR5R8SEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت با افزایش ۲.۵ درصدی از ۹۱ دلار عبور کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/142322" target="_blank">📅 22:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142321">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
وزیر نیرو: با درایت مسئولین، قطعی برق امسال بسیار کمتر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/142321" target="_blank">📅 22:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142320">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
تحولات به شدت داره خبر از جنگ مجدد میده
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/142320" target="_blank">📅 22:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142319">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
کان: احتمال شروع مجدد جنگ بسیار بالاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/142319" target="_blank">📅 22:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142318">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
فوری/قدم بعدی ترامپ مشخص شد
‼️
👇
👇
👇
👇
https://t.me/+S8mMBRHkHmFiMTFk
https://t.me/+S8mMBRHkHmFiMTFk</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/142318" target="_blank">📅 21:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142317">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f5f083dc2.mp4?token=f8VJir6Rb2TKvFQGVIJxnfQkitTLDlh_2F1_hqOtS8AFfq0Z-cmut9Yr_TuYGjqICwogeCfRbJN50w5ROHeI27xv6CldlKPCb6QqjbZ6O10YNkfwfjND-ukou4O9ByEs8_WBcjyJ7UgVn_1sPqFPfi2EytoAlOJ4RL3rjR4S3OWhJs8S5Ta-NaUicjJIXI18m14cBEErYmgmKznY5K5i3MYrS2Btnar1yrvpNE1WteVd8x8t-9rfiPwehmvvYbTuf5tZHzhSwrmmU6njianhn-Z4eTTpQ9tyEumUPb8UapjadeZzt0OyN0faTt4kHPPI7Kt86ea9OLYNCIwcXLw8yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f5f083dc2.mp4?token=f8VJir6Rb2TKvFQGVIJxnfQkitTLDlh_2F1_hqOtS8AFfq0Z-cmut9Yr_TuYGjqICwogeCfRbJN50w5ROHeI27xv6CldlKPCb6QqjbZ6O10YNkfwfjND-ukou4O9ByEs8_WBcjyJ7UgVn_1sPqFPfi2EytoAlOJ4RL3rjR4S3OWhJs8S5Ta-NaUicjJIXI18m14cBEErYmgmKznY5K5i3MYrS2Btnar1yrvpNE1WteVd8x8t-9rfiPwehmvvYbTuf5tZHzhSwrmmU6njianhn-Z4eTTpQ9tyEumUPb8UapjadeZzt0OyN0faTt4kHPPI7Kt86ea9OLYNCIwcXLw8yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: «ایران با مشکلات بزرگی روبه‌روست و وضعیت این کشور آشفته است.
🔴
نیروهای نظامی ایران کاملاً شکست خورده‌اند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/142317" target="_blank">📅 21:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142316">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فوری/دونالد ترامپ: به دنبال تمدید یادداشت تفاهم با ایران نیستیم‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/142316" target="_blank">📅 21:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142315">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85f96aa426.mp4?token=WuPcIjFRHDvOMNjTCVZAN5MvTNNrGfKNJy5IYXKq4wihWkqYAeFihDE1aj4Y6NsJyz-GtY1XHsUCnyBytTDJCk7H8taX0MQ-tnV6vANjG7xjK7r2wyMQH1UpTnn1pngS4m3ahkjxBE_ifKzADO7ms-Fg4gIJx-SI1WM8mgxdikZtzXMd4tVEKlSUluctzVeStDczFXNeT8-BI0dX3gi2g_fJFeawa4yNbH5I496j3RgegpwH-GMr4686r37sNdcZcIi0D6imy9yZO_2Puk4KTLPJOptc8Ly4x-jJhis89q9LpFsdH97G1ERre-OixxxtkzUDHq33ahOdwQPnv-yoJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85f96aa426.mp4?token=WuPcIjFRHDvOMNjTCVZAN5MvTNNrGfKNJy5IYXKq4wihWkqYAeFihDE1aj4Y6NsJyz-GtY1XHsUCnyBytTDJCk7H8taX0MQ-tnV6vANjG7xjK7r2wyMQH1UpTnn1pngS4m3ahkjxBE_ifKzADO7ms-Fg4gIJx-SI1WM8mgxdikZtzXMd4tVEKlSUluctzVeStDczFXNeT8-BI0dX3gi2g_fJFeawa4yNbH5I496j3RgegpwH-GMr4686r37sNdcZcIi0D6imy9yZO_2Puk4KTLPJOptc8Ly4x-jJhis89q9LpFsdH97G1ERre-OixxxtkzUDHq33ahOdwQPnv-yoJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: «ما هر هفته میلیون‌ها بشکه نفت خارج می‌کنیم؛ شاید این روند متوقف شود یا حتی بیشتر گسترش پیدا کند.
🔴
تنگه هرمز باز است و قیمت نفت در حال کاهش است و این کاهش ادامه خواهد داشت؛ مگر اینکه تصمیم بگیریم اقدامی بسیار شدیدتر از آنچه اکنون انجام می‌دهیم، انجام دهیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/142315" target="_blank">📅 21:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142314">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/434bd2f553.mp4?token=FNL5Q3UhtiVKpb0IoBaR95yT5dgj_44xaQezo5bK4CAQAMpTSKQr1jFC6tBT3tSqeWqN8AjE03nFq048SKdBCF2vWQJm_da9wbuPkkBdYXHhD_5YTL4LShm9UZfw0Ri-m5XzAYrLYoM3ZOYPgGnKW-hIRWMTMaJEh9U2nBgMPIjy0nDA0YV-qw6x8f998J30m3uFHcUeIiDoKR_veVEj94pjQOpMlGuoZoFxT5YkECGtC4ckbK2zpAz-o4d-RPmUQBxoTlSqnTntNDc7CqG6YyARRIcJAe0S0Tr5Zlo5n1FKS5QicEe2OnHQ3dSGOL8Nu6O29rIHZIUtyJ0n06rdiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/434bd2f553.mp4?token=FNL5Q3UhtiVKpb0IoBaR95yT5dgj_44xaQezo5bK4CAQAMpTSKQr1jFC6tBT3tSqeWqN8AjE03nFq048SKdBCF2vWQJm_da9wbuPkkBdYXHhD_5YTL4LShm9UZfw0Ri-m5XzAYrLYoM3ZOYPgGnKW-hIRWMTMaJEh9U2nBgMPIjy0nDA0YV-qw6x8f998J30m3uFHcUeIiDoKR_veVEj94pjQOpMlGuoZoFxT5YkECGtC4ckbK2zpAz-o4d-RPmUQBxoTlSqnTntNDc7CqG6YyARRIcJAe0S0Tr5Zlo5n1FKS5QicEe2OnHQ3dSGOL8Nu6O29rIHZIUtyJ0n06rdiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: «از ایده اعلام تنگه هرمز به‌عنوان قلمرو ایالات متحده خوشم می‌آید.
🔴
ما کنترل کامل تنگه هرمز را در اختیار داریم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/142314" target="_blank">📅 21:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142313">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abc9ea29b6.mp4?token=rcGrqMvROb3hWnnKKfFT7_beIuc5DSUIPZsiCJxQMVi9LI8mFwg1oiidpmrXRsLHiaoqgIh6ejr2khJ5KDv938i6pEINiY6P5vjSVnIMwI1i3WTS4vyXfQUl1SLf02BDDHvIfQeYyjSXVi_PQWFBzb_m4_U35Qemed8f_VZt97xr2FniYzLaRMvs-5XrSinDsEJxzbqb8uWFziTtQptIjTy7l74dwmw2Y90MtsPneUzOf9cHGn3LVjZLqtjyF5FZCRo4v9JNhMGd3N79G9qFc6-j7c3I6IGqxelqcesX2TuVV2baYtIn8-d1aPTWwM4H5y3MF1dIcgbktfx3b-CbIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abc9ea29b6.mp4?token=rcGrqMvROb3hWnnKKfFT7_beIuc5DSUIPZsiCJxQMVi9LI8mFwg1oiidpmrXRsLHiaoqgIh6ejr2khJ5KDv938i6pEINiY6P5vjSVnIMwI1i3WTS4vyXfQUl1SLf02BDDHvIfQeYyjSXVi_PQWFBzb_m4_U35Qemed8f_VZt97xr2FniYzLaRMvs-5XrSinDsEJxzbqb8uWFziTtQptIjTy7l74dwmw2Y90MtsPneUzOf9cHGn3LVjZLqtjyF5FZCRo4v9JNhMGd3N79G9qFc6-j7c3I6IGqxelqcesX2TuVV2baYtIn8-d1aPTWwM4H5y3MF1dIcgbktfx3b-CbIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: «کسانی که با ساخت سالن رقص مخالفت می‌کنند، به نظر من افرادی هستند که به کشورمان وفادار نیستند؛ بسیار، بسیار بی‌وفا به کشورمان.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/142313" target="_blank">📅 21:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142312">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c26719b14.mp4?token=CRePsSQOgi2cKAl7ezmwsoCUvKE62pcC0Yrtb4u86orbyN-3T45jshnq_ZZZEWiMLmFtYAQwpkPwcBYhOFSDZYYSpeRh6Wg7MUm28A4HGmgFdIaKcsjd6Cwd4p9OsI6zpleTZAquzyOmwV-8YwmIvrezG65OsNVn5YVvYKQWLuj5Ol3IXA9328WkLZ7bnKs9asF7chgIqSBgWebSe1rt2dhSx9yQVbDxNoJHzRCsBwptqzpFvcwcB6XWGtLActdXbpwk3tzuJ6Urh9k1q_x7gbGmJXFZ-Vw40LK1sZtfUznUsg2aDbLbWM7fkfmaFHipQlEjann2gahX8F-hs_4v0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c26719b14.mp4?token=CRePsSQOgi2cKAl7ezmwsoCUvKE62pcC0Yrtb4u86orbyN-3T45jshnq_ZZZEWiMLmFtYAQwpkPwcBYhOFSDZYYSpeRh6Wg7MUm28A4HGmgFdIaKcsjd6Cwd4p9OsI6zpleTZAquzyOmwV-8YwmIvrezG65OsNVn5YVvYKQWLuj5Ol3IXA9328WkLZ7bnKs9asF7chgIqSBgWebSe1rt2dhSx9yQVbDxNoJHzRCsBwptqzpFvcwcB6XWGtLActdXbpwk3tzuJ6Urh9k1q_x7gbGmJXFZ-Vw40LK1sZtfUznUsg2aDbLbWM7fkfmaFHipQlEjann2gahX8F-hs_4v0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آیا در ناو هواپیمابر آبراهام لینکلن غذای کافی وجود دارد؟
🔴
ترامپ: «بله، وجود دارد. گزارش سی‌ان‌ان درباره این موضوع جعلی بود.
🔴
در سال‌های گذشته، ناوهای ما مدت‌های بسیار طولانی‌تری در دریا حضور داشته‌اند.
🔴
یکی از دریاسالاران به من گفت: قربان، من مدت بسیار بیشتری از این روی کشتی‌ها بوده‌ام. نیروهای حاضر در لینکلن هم می‌گویند که به‌خوبی از آن‌ها رسیدگی می‌شود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/142312" target="_blank">📅 21:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142311">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dbd66f94a.mp4?token=nsERUzlHRSOs48P8LElSC1L31ApSodTcOLXOsUmSOXvQqtjT__-7IuXKHVnI0vTviLN3x9hi7ZQ4jwEOmsD65D7cPa3rwxapdbmLsfwmaU-NrLBOnKQi6u8pmFSOycZJti1pjVH9Vkyz4rPf9KEeisMIJBr9t11yilJ31R3MLLYsnXzJBGlsRw6-8utUoaWf3wdaHoNYbaeV2yW5L3UMU23hUWkHDkRBhRAE4I2_9bJyvCXS9ngb6DFta02PBdYQYpVCqO4S9aKbrT5mZMrGlZbnqfJQcjt0eB_5GOWZiLcuWopr8XToF0F-gjZTEnSWEfv_rDwUPNhBwX2b68AEfYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dbd66f94a.mp4?token=nsERUzlHRSOs48P8LElSC1L31ApSodTcOLXOsUmSOXvQqtjT__-7IuXKHVnI0vTviLN3x9hi7ZQ4jwEOmsD65D7cPa3rwxapdbmLsfwmaU-NrLBOnKQi6u8pmFSOycZJti1pjVH9Vkyz4rPf9KEeisMIJBr9t11yilJ31R3MLLYsnXzJBGlsRw6-8utUoaWf3wdaHoNYbaeV2yW5L3UMU23hUWkHDkRBhRAE4I2_9bJyvCXS9ngb6DFta02PBdYQYpVCqO4S9aKbrT5mZMrGlZbnqfJQcjt0eB_5GOWZiLcuWopr8XToF0F-gjZTEnSWEfv_rDwUPNhBwX2b68AEfYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ساکت، ساکت، ساکت. شما بسیار بی‌احترامی می‌کنید. ساکت باشید. شما با چه کسی هستید؟
🔴
خبرنگار: من از شبکه CNN هستم.
🔴
ترامپ: شما اخبار دروغین را پخش می‌کنید. ساکت باشید، ساکت باشید، ساکت باشید. شما یک خبرنگار دروغگو هستید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/142311" target="_blank">📅 21:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142310">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ce69956d0.mp4?token=KXtkHN3ezFJXfIla7e6pfBlWVNCMEGGKwUvwLo29-tjSVxTK1nWLewWzKaBHk0Gtfod_e6zIJWMty5ZqTTcbAuC6r1b08NQJiAmKqchu7CZcUIxGyRJ_6yHf0mAiaVWQqHKQwKpCOCKrWf5bTL2hkO8zXJoiw5g8-a5lUdvzJ2fhW-VCNK1gqzKGIZmYW1rUBVcXFor8pta0wGsszYACtZCJm3Ozpx96sihzahHLQZouQ5GQvO00YHzn2YOuBkpLrxZai2iAPbqPyW__Hsoxs4G2ZscAeB5b91cotTytQ3tk9Q_wWVrENva7swYRfD95t8XuVoIr3KnAzzjj2qBkVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ce69956d0.mp4?token=KXtkHN3ezFJXfIla7e6pfBlWVNCMEGGKwUvwLo29-tjSVxTK1nWLewWzKaBHk0Gtfod_e6zIJWMty5ZqTTcbAuC6r1b08NQJiAmKqchu7CZcUIxGyRJ_6yHf0mAiaVWQqHKQwKpCOCKrWf5bTL2hkO8zXJoiw5g8-a5lUdvzJ2fhW-VCNK1gqzKGIZmYW1rUBVcXFor8pta0wGsszYACtZCJm3Ozpx96sihzahHLQZouQ5GQvO00YHzn2YOuBkpLrxZai2iAPbqPyW__Hsoxs4G2ZscAeB5b91cotTytQ3tk9Q_wWVrENva7swYRfD95t8XuVoIr3KnAzzjj2qBkVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کیم جونگ اون: «کیم جونگ اون همیشه با احترام زیادی با من رفتار کرده است.
🔴
ما مدتی را با هم گذرانده‌ایم؛ من او را درک می‌کنم و او هم من را درک می‌کند
🔴
او تقریباً از هیچ‌کس خوشش نمی‌آمد، اما من رابطه بسیار خوبی با او دارم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/142310" target="_blank">📅 21:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142309">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/623c03350d.mp4?token=CnjUhhNda0CZ0kOVvMoyUmgk1sliGWZ7Y-mUcLOVtW2RR3uBozi2YMDhtIg5IT1Tp4PJRnPGCUlAi6nJA0e3lUXFctTNm4NTwl7GkPpdE9HSYb18Sz4WM8zspLzYmyj2VSmDmh3jVNpKUhm9NgncmuXkBnCBGD9RdIu5UUMyUCdVm-t7mIz78_AF_vIk9_HWublS0KbBbvnbEsKDEmTp-cOjI9rtE_HwVZ2LMSsNmt7C6wgTGtanXmsc86S2h4TAcPEyDJTJ3UsJYkrhNtcQ-7kdF7R_fxgAL5Vz5LHFffZs7v0K72XmK-yhRlEcAeKbqbcph_3i2Fi6bbVJpYKYgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/623c03350d.mp4?token=CnjUhhNda0CZ0kOVvMoyUmgk1sliGWZ7Y-mUcLOVtW2RR3uBozi2YMDhtIg5IT1Tp4PJRnPGCUlAi6nJA0e3lUXFctTNm4NTwl7GkPpdE9HSYb18Sz4WM8zspLzYmyj2VSmDmh3jVNpKUhm9NgncmuXkBnCBGD9RdIu5UUMyUCdVm-t7mIz78_AF_vIk9_HWublS0KbBbvnbEsKDEmTp-cOjI9rtE_HwVZ2LMSsNmt7C6wgTGtanXmsc86S2h4TAcPEyDJTJ3UsJYkrhNtcQ-7kdF7R_fxgAL5Vz5LHFffZs7v0K72XmK-yhRlEcAeKbqbcph_3i2Fi6bbVJpYKYgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: «آن‌ها خواهان توافق هستند، اما حاضر نیستند توافقی را بپذیرند که من آن را ضروری می‌دانم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/142309" target="_blank">📅 21:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142308">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf45ba5f07.mp4?token=a907t6YRo-g0-3JwIT5N8gKH1EOOERwII_HKCvfXT2JAOgzkUTQByXs-nhktlVh3cQBjI_ZHteADQQRMuTLjcXN2_XX6Z3To00_b5EVVmRoAF6TP-6gIIyeDZPHwhq2A5EHEHZlUoIqE6IOxb793LKSu-yVZ4RmRMAdIGlLC85wjBeV_Wq9ycxcB4ig1UzrFpO6Wrue2XZk7ZVKHSKBsdWNzbs3c63-wUnCoTMEjd7ydDk9T-eeF_jr4rRFtOYPVjmsIXKAX68CMNGyBm57VIjt6m2oMe6naJ06CWD9arFQ_kirLges_xdpeSsb1leY7Jwpi8dkX_4hVwHk5yRxqMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf45ba5f07.mp4?token=a907t6YRo-g0-3JwIT5N8gKH1EOOERwII_HKCvfXT2JAOgzkUTQByXs-nhktlVh3cQBjI_ZHteADQQRMuTLjcXN2_XX6Z3To00_b5EVVmRoAF6TP-6gIIyeDZPHwhq2A5EHEHZlUoIqE6IOxb793LKSu-yVZ4RmRMAdIGlLC85wjBeV_Wq9ycxcB4ig1UzrFpO6Wrue2XZk7ZVKHSKBsdWNzbs3c63-wUnCoTMEjd7ydDk9T-eeF_jr4rRFtOYPVjmsIXKAX68CMNGyBm57VIjt6m2oMe6naJ06CWD9arFQ_kirLges_xdpeSsb1leY7Jwpi8dkX_4hVwHk5yRxqMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
«ما نمی‌توانیم مدام از همه این کشورها محافظت کنیم؛ به‌خصوص وقتی که آن‌ها حاضر نیستند در زمان نیاز به ما کمک کنند.».
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/142308" target="_blank">📅 21:38 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142307">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d292649909.mp4?token=qMtN8Hni4pgvpyK_80Ta2mU4RyjXhwAtub_m2HruAqvozIKpW06-4juFaMFaaqqvMzdVvLhN5PspnLusYgy0peTIMlJU_7Om36wJo5shQjgFNeIgtGk1beqWfTBRDIwmAhzrTpSd5biNXIRZ_84pSPqGkDqPEYBDNddQ8kK5gJ31tTBBZGgzwlrlokMdBtovonqB7eyOBwcU1zh3YyLHZhv9NqsN26SMPeho9mf6j8XjCc2LhCSqCOSRnMp74_CgSW9T0nct5yJaX6KsjpkK8yLJiUPJGSiRREyteiPi3cdvWW7GVkq_SB4Xaaz2yVDf90Khm2YZSglaLR9zmP-ouA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d292649909.mp4?token=qMtN8Hni4pgvpyK_80Ta2mU4RyjXhwAtub_m2HruAqvozIKpW06-4juFaMFaaqqvMzdVvLhN5PspnLusYgy0peTIMlJU_7Om36wJo5shQjgFNeIgtGk1beqWfTBRDIwmAhzrTpSd5biNXIRZ_84pSPqGkDqPEYBDNddQ8kK5gJ31tTBBZGgzwlrlokMdBtovonqB7eyOBwcU1zh3YyLHZhv9NqsN26SMPeho9mf6j8XjCc2LhCSqCOSRnMp74_CgSW9T0nct5yJaX6KsjpkK8yLJiUPJGSiRREyteiPi3cdvWW7GVkq_SB4Xaaz2yVDf90Khm2YZSglaLR9zmP-ouA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
: «با رئیس‌جمهور کره جنوبی تماس گرفتم و گفتم: آیا برای موضوع ایران به ما کمک می‌کنید؟ البته اگر بخواهید؛ ما نیازی به کمک نداریم. او گفت: نه، ممنون.»
🔴
«گفتم منظورتان چیست؟ ما ۳۹ هزار سرباز آنجا داریم که از شما در برابر کیم جونگ اون محافظت می‌کنند، اما شما حاضر نیستید درباره ایران به ما کمک کنید؟ عجیب است.»
🔴
«پس چرا ما باید به شما کمک کنیم؟ حفاظت از کره جنوبی میلیاردها دلار برای ما هزینه دارد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/142307" target="_blank">📅 21:38 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142306">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ترامپ: ایران می‌خواهد به توافق برسد و ما به یک دلیل آنجا هستیم و آن جلوگیری از دستیابی آن‌ها به سلاح هسته‌ای است
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/142306" target="_blank">📅 21:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142305">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
خبرنگار: شما گفته بودید اگر عمان در مسیر بازگشایی تنگه هرمز مانع‌تراشی کند، «حسابی آنجا را بمباران خواهید کرد». آیا می‌گویید دیگر صبرتان در قبال عمان، که یک شریک راهبردی است، به پایان رسیده است؟
🔴
ترامپ: فکر نمی‌کنم آنها رفتار خیلی خوبی کرده باشند، اما ما به‌راحتی از پس آنها برمی‌آمدیم؛ درست همان‌طور که با مسائل دیگر برخورد می‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/142305" target="_blank">📅 21:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142304">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0da1c4c2eb.mp4?token=HZbyd6pJWSfNJ0ygswx9pqI8zaGI4rkt6wITO9GjqpoVjkg_LZBr_Yj_RCVoa4TmzNt-cdTUoTMOy0tFX8WVpLIUMOUJT1gIPiVRDHBMnvgcEyiBPsHjq6YKNkm6WxO71wgC9iiO5XnotatPK6bWyS6zXlaLidkvqzASiSdM3Pw6wCqi8arFsfjJoOv9OF9CBGgKWugZoPq9qk6DvrKEYmjTdA-ye4GiJYbvP4Rzj9JhxdBXtm1ESe7w_B7OOHnYqybryRUBbxlrNcSNgGQpvxCEBgpjPfmdWcImXUAj1vvxP8Bap1CU5ELrrTtnIvxk2H9h2F8ddUmHsT2Ft-pnnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0da1c4c2eb.mp4?token=HZbyd6pJWSfNJ0ygswx9pqI8zaGI4rkt6wITO9GjqpoVjkg_LZBr_Yj_RCVoa4TmzNt-cdTUoTMOy0tFX8WVpLIUMOUJT1gIPiVRDHBMnvgcEyiBPsHjq6YKNkm6WxO71wgC9iiO5XnotatPK6bWyS6zXlaLidkvqzASiSdM3Pw6wCqi8arFsfjJoOv9OF9CBGgKWugZoPq9qk6DvrKEYmjTdA-ye4GiJYbvP4Rzj9JhxdBXtm1ESe7w_B7OOHnYqybryRUBbxlrNcSNgGQpvxCEBgpjPfmdWcImXUAj1vvxP8Bap1CU5ELrrTtnIvxk2H9h2F8ddUmHsT2Ft-pnnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: چرا کیم جونگ اون به درخواست شما برای گفت‌وگو پاسخ نداده است؟
🔴
ترامپ:
«شما از کجا می‌دانید؟»
🔴
خبرنگار:
یعنی پاسخ داده است؟
🔴
ترامپ:
«اِم... بله، بله.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/142304" target="_blank">📅 21:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142303">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fdab4a5a7.mp4?token=MX9DiQ_MLrbJmhyGIZNufr2qDFpLBRtDYVGgpEYufZV8B0bGDuRW_N74D74amxMWifVE8yX6Ona922XnhEa8GmeakafCyU-V2UZYxIPxulsBqQT_r5kbhjz5I_OxtlOsJuAb6IOsfKqO4F6TqYSTnmeBd3OKe_M1f8xkvo_ZLsgK9tamWxB6_AlG5N7iGXRlddKGnQrmpWjJExMRqVEaITT12v3hSIX7RDoFAhXiFLXl1u6KU8gy0fdhMMklk8lZBceASDa2-TAFKgTfFzF1ouDdET-ya3lgZDpwE-wb9GIg_6j1y2zSnd2z0lm3bFpjJ9UZwd86pHIMeHfxN5Po1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fdab4a5a7.mp4?token=MX9DiQ_MLrbJmhyGIZNufr2qDFpLBRtDYVGgpEYufZV8B0bGDuRW_N74D74amxMWifVE8yX6Ona922XnhEa8GmeakafCyU-V2UZYxIPxulsBqQT_r5kbhjz5I_OxtlOsJuAb6IOsfKqO4F6TqYSTnmeBd3OKe_M1f8xkvo_ZLsgK9tamWxB6_AlG5N7iGXRlddKGnQrmpWjJExMRqVEaITT12v3hSIX7RDoFAhXiFLXl1u6KU8gy0fdhMMklk8lZBceASDa2-TAFKgTfFzF1ouDdET-ya3lgZDpwE-wb9GIg_6j1y2zSnd2z0lm3bFpjJ9UZwd86pHIMeHfxN5Po1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آیا به دستیابی به توافق نهایی درباره ایران نزدیک‌تر شده‌اید؟
🔴
ترامپ: «اجازه دهید ابتدا صحبت‌هایمان با رایدر را تمام کنیم؛ بعد از آن به چند مورد از این سؤال‌ها پاسخ خواهیم داد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/142303" target="_blank">📅 21:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142301">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gB4jSovTJvmqFqlWDHqZqgWIuSMStEp554CECMvYcZkgytCs6p6k5BincSr_HWLZM_t_lampMQI8hrgWThMPpQewEMHNFRRCxJzl6fYRwOlbGIuv-5LpGB0Kpsuh0fb_6y8iWLrX0pwcEi7MRwRU_OLaEJUf1KybvzzJoBKj2M0eeLHuz60fqhDmyw45qbiJquf9h4YejDK1ZhdlyZgrNrzSv1ldB0p_w7wdaHB_5_TDLlEoMpYk1sYsqC6LTDY8vqlN5EzeWoEYkqdlsJ57kCOeXq3W5MrUd8vBqkkiPVfuRMkaERxDAk6-wlILCMBvZW0eR3z2_qOfELJx-keMzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S4QKJNLGi2Ua1hHe9ifcgtTSeJZPd3A6_668AkoLdFTTel15d6pd4vk4V-9c-TM-zpgmPcpTOqsrNJvpUax5L6srRxHKgqx7E_qrlr2EhpzjSGPdqglzYwKRqFCJhSffWLu6T8SDPIAyM1L1G4Gwx5rRQLQIrvyb4lPJELrOEsBREyeR0t8kSRKoGQTO3tGDpDr8r_nAfqSvWsRgyUNOeFGITE3H2rqfyGNIz1OaariWHDdbHwWM7g3M5zKdWva0_pr0DIaDPeLK7DmAUGVCwzqm2pIoqJrtkEZoPlikQ1U63_dPzpdylsha7uiQ5YGKKsPrZH10CE9NiwwoG_bBrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک فروند هواپیمای ترابری از نوع C-17A اماراتی دقایقی پیش در تل‌آویو فرود آمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/142301" target="_blank">📅 21:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142300">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhXTEyp7i5HgwkNQAcYE98n_iT7LiV4ozA6VReUsCQMoMYfrfqowmD4T9s2m1cTENGZpKpO1WppR_olkuw04gOSwZfm6f5skB2erg2izR8wrYC6cNkx6GJjd_W2Jv55njKrKgnOePGEyXTeoGwhQ4t2b82pRkoEzcWQzIYzoRuCbc61pBGv0WwIDuygic3aZ1ndM68BD6eUv5Ww2YnkZWI9uE_OE70x3my9hIMSKPnyxML23ix9sbeBtDRYYLMfNAb6n1ULrxm0v4rf_RyRz7NHGwesv5eAeo0p5Y-eOW4Ex6L-Vg4xH0KExTUqzGFKPLbaixlVS8kqHidyUmMMLDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / تلگراف: "ترامپ" در حال بررسی امکان حمله هسته‌ای به ایران با پایان مهلت توافق صلح است
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/142300" target="_blank">📅 21:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142299">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: هدف، خفه‌کردن اقتصاد ایران است
🔴
وزیر انرژی آمریکا مدعی شده ایران در حال حاضر قادر به صادرات هیچ نفتی نیست و واشنگتن همزمان تلاش می‌کند جریان نفت و گاز از تنگه هرمز ادامه پیدا کند.
🔴
او گفت روز شنبه بیش از ۳۰ کشتی از هرمز عبور کرده‌اند و صریحاً اعلام کرد راهبرد آمریکا «اعمال یک محاصره اقتصادی خفه‌کننده» علیه ایران است.
🔴
پیام واشنگتن روشن است؛ حفظ جریان انرژی برای بازار، همزمان با بستن مسیر درآمدهای نفتی ایران.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/142299" target="_blank">📅 21:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142298">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/690d167119.mp4?token=o0-2Wepk6TgsGfp9jGbxmruIKCcdKZTvgRVdao7KNnkGStuCfu20harpNfEXTqm7bGm95xO6I9RCeiXmLE3Zos7SzJd2r984C02suhLJeKmxlz4lp__OhkYzZCQJW1y2PSjHOKgoM1oO0bnp3JJZlAfQ6JrZqKK4bzrrW4-1avkGrd7xeUU51Vh0WI0bK0afnWpYs3HxT-Pn6sBBTZ0i7REcgHuLKTAC-1eWcnM7qS-pIFNOnzzma6EN_irFZEZFhUvuSy8DBR2HjPS1QDuCkwTYr92BhYYGiLLFyLfiFZug3Q1GfaI0h4E-5BIJoQrdlS73A7RX3AOJr3HVj4-T-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/690d167119.mp4?token=o0-2Wepk6TgsGfp9jGbxmruIKCcdKZTvgRVdao7KNnkGStuCfu20harpNfEXTqm7bGm95xO6I9RCeiXmLE3Zos7SzJd2r984C02suhLJeKmxlz4lp__OhkYzZCQJW1y2PSjHOKgoM1oO0bnp3JJZlAfQ6JrZqKK4bzrrW4-1avkGrd7xeUU51Vh0WI0bK0afnWpYs3HxT-Pn6sBBTZ0i7REcgHuLKTAC-1eWcnM7qS-pIFNOnzzma6EN_irFZEZFhUvuSy8DBR2HjPS1QDuCkwTYr92BhYYGiLLFyLfiFZug3Q1GfaI0h4E-5BIJoQrdlS73A7RX3AOJr3HVj4-T-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وحشت مردمِ «گالراس» از «ابرهای خونین» در آسمان
🔴
‏ ساکنان شهر گالراسِ کلمبیا چند روز پس از وقوع زلزله‌ای قدرتمند در غرب این کشور، تصاویر غیرمعمول از آسمان شهر که با ابرهای سرخ تیره پوشیده شده را در رسانه‌های اجتماعی منتشر کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/142298" target="_blank">📅 21:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142297">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yzvbv7BGBRip-hsFkJ6eWTaRCfZCAgjKcOuvhqt8o0vN37Lf_qpPHhzG-2CzL572eMVArcqu7UhND2XOuDkHY1SVtHFOpa7fs5GLpcT-Kj2J6el0u6rmMj1WqAJoNgb-r4HpYwjYGiJ-QYO4IGjy8rL3stdjdC4JfmA_LdbFefgZpWS8hV9r3kNWicr4sqMDXCequkTuLkUxT-ekQMD72Z4FT5K3qSR3h8n3aG4SQU3Xd7WIXsEbmqEhAtPGiKsObQjryqxwqB7y2mjG_VPDJti268fP94LUyuwp1oQdVBx2YuGj9jIUFMcRKX76KFIWM29rL4FZ-rcBY76u-z7Ung.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
گزارش عجیب رکنا از دعوای دختر و پسر تهرانی: دختر گوش دوست پسرش را گاز می گیرد و بخشی از آن را جدا می کند سپس وی را به بیمارستان می رساند
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/142297" target="_blank">📅 21:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142296">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0b06591ce.mp4?token=Sv18o77O73hzrJcppKMtRSoUT_-H-b_sgTyoLq-QHJmNFKyPoo70fRbOO__h5jORB5rw3n1sXdgs1Je-DkPpSQ-fOR7v26JVJjJoJhb4zVv_8ueZjPFTvrYywEYXbMei7i73zNqGg9fs1Kx_zXktZ0r5dZt15PdQP--pwdf2gY2xVmUmgbHfscwwJs1WApfzqtn6EE3ob6PWqmteSInA1OkugWcAX32mfn17fmKTLnv64nsmy29E-mMjsDOztitCFW-Uy6cVjnD96DvhTrcz7b2XmOkEy_72Y3fSHSMGEkhIlZOJYJfVxI1EpBQfYg00XjCEyMIdFEujqHEfnibwuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0b06591ce.mp4?token=Sv18o77O73hzrJcppKMtRSoUT_-H-b_sgTyoLq-QHJmNFKyPoo70fRbOO__h5jORB5rw3n1sXdgs1Je-DkPpSQ-fOR7v26JVJjJoJhb4zVv_8ueZjPFTvrYywEYXbMei7i73zNqGg9fs1Kx_zXktZ0r5dZt15PdQP--pwdf2gY2xVmUmgbHfscwwJs1WApfzqtn6EE3ob6PWqmteSInA1OkugWcAX32mfn17fmKTLnv64nsmy29E-mMjsDOztitCFW-Uy6cVjnD96DvhTrcz7b2XmOkEy_72Y3fSHSMGEkhIlZOJYJfVxI1EpBQfYg00XjCEyMIdFEujqHEfnibwuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سی‌ان‌ان تصاویری از یک سامانه پاتریوت اوکراینی در نزدیکی کی‌یف منتشر کرده که فاقد موشک رهگیر است.
🔴
خدمه این سامانه می‌گویند کمبود مهمات باعث شده حدود ۱۰ هفته نتوانند هیچ هدفی را درگیر کنند؛ تصویری روشن از فشاری که کاهش ذخایر موشکی بر پدافند هوایی اوکراین وارد کرده است.
🔴
سامانه هست، خدمه هست؛ اما بدون موشک، پدافند فقط یک سکوی خالی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/142296" target="_blank">📅 21:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142295">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ستاد فرماندهی مرکزی ایالات متحده (سنتکام) : از زمان از سرگیری محاصره دریایی ایران، ۶۴ کشتی تجاری را منحرف و ۳ کشتی را از کار انداخته‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/142295" target="_blank">📅 21:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142294">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TE2gDa5qK9quXD-M5Lnx8HbNwYcazRjJISn0jnCnIx2hPQnH_aIe1DZ1OoCkyRj9heyfTeWg0VSj-mGbdj_bjR7VzySa8-GqgiSGM6FaevxOAa2Dy-zmVYQoAviKB44Zo8DSH8A7F6ggyne5_McVPS-exdV7VZkLuu2O1Z7ei_EcjlfoXrrNpeSgC4p0OOh-xbDEjBRYIXZTdNviZFd-uA4-UTCBnvrtxZI5J_0B0uWHwMuwWijeWP2Se_-IWjx8Gv8P5F7Mb0rj0MI1D9gc1L_898K1-sGEt8tpBzspit9dj8d483tD9mLS4l9_34dgDl3zJzmewuh8fBIAJaQHpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
نفت برنت ۹۰ دلاری شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/142294" target="_blank">📅 21:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142293">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSwuRg9wE1bxDWq4B1foOyjWNbLTBF-lCCmv8b8Lss1QGBelxRkGbXF39DbRxcbYmfeIyKoiyktc45xxElUz3G2GTWIH3SEhg9a9m7khhPgfkCAf_3iCx7L8bhwiB3YmXujfUE6teXBpUc3jUFcJwqDvuzQn1g4skj-SQH-gX-DXRmB4KM2PC0lKeKflnwpd5dN3IG8Pmf6U2yZEJvEqK73c6m7AktIGdj_cSBZnoX9b0w79uVgE0JPFhJwyz2pmJVKcAPJJDOZzfkkDdE0ufTdlySZLCsXwsMnDTIGuITp5vM0R9s_WtjxmbEV_zx1_Sc8VhuKrNa5ZPj4T5AG7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار عبدالناصر همتی، رئیس کل بانک مرکزی با علی الزیدی، نخست‌وزیر عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/142293" target="_blank">📅 20:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142292">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
سی‌بی‌اس: کاهش تردد کشتی‌ها در تنگه هرمز؛ ناامنی همچنان ادامه دارد
🔴
بر اساس داده‌های ترافیک دریایی، تعداد عبور کشتی‌ها از این آبراه راهبردی ۱۹.۵ درصد کاهش یافته و از اوج ۱۹ مورد در ۱۱ اوت به تنها ۳ مورد در ۱۶ اوت رسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/142292" target="_blank">📅 20:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142291">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
فایننشال تایمز به نقل از یک مقام اسرائیلی: اختلافاتی بین اسرائیل و آمریکا در مورد احتمال خلع سلاح حماس وجود دارد.
🔴
اسرائیل شک دارد که حماس سلاح‌های خود را تحویل دهد، در حالی که آمریکایی‌ها معتقدند این امر امکان‌پذیر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/142291" target="_blank">📅 20:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142290">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ddb0267e.mp4?token=HlopafOqoTsRrFrPUhJyeY1v60dgpAs_W7pAE2BbdhgTeZ9WZQUJfxWDfEfEvmFwsOBrzVN9x7ZG8OAnOXq6QlY174dRCtFi6dWIb1Z2fjLQBDomfxppcv3Gnhlo8unbzl3IIDHAwPKuURR1g-riSFTeGwMlMg6VdpKnOPU9EYrnFqJjPx-x00vdYS1kV9Xs9BE4vHvCQ0AlJXcZPCl6n0GrRVs0DjC-wE0337J5rtAlxSc9qwNf_77oCgPTbfB6E_fODSgOAemUH3dpmVqVEgULhSwRCrdlhyuG_07vGSk0fVCOV7qPJ7MnjH2EIvoxxuDzsdZyF_4QYKNQO3MVQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ddb0267e.mp4?token=HlopafOqoTsRrFrPUhJyeY1v60dgpAs_W7pAE2BbdhgTeZ9WZQUJfxWDfEfEvmFwsOBrzVN9x7ZG8OAnOXq6QlY174dRCtFi6dWIb1Z2fjLQBDomfxppcv3Gnhlo8unbzl3IIDHAwPKuURR1g-riSFTeGwMlMg6VdpKnOPU9EYrnFqJjPx-x00vdYS1kV9Xs9BE4vHvCQ0AlJXcZPCl6n0GrRVs0DjC-wE0337J5rtAlxSc9qwNf_77oCgPTbfB6E_fODSgOAemUH3dpmVqVEgULhSwRCrdlhyuG_07vGSk0fVCOV7qPJ7MnjH2EIvoxxuDzsdZyF_4QYKNQO3MVQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتیش سوزی شدید، میدان شهرداری گرگان، تا کنون بیش از ۱۰ مغازه در آتش سوخته اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/142290" target="_blank">📅 20:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142289">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBXxcnjbPoJWrQluGiE9lzx5fyp4XKQCs5FqtOva5Wdiwq1vDYRwimkeszK1_B1-YaeFsvMRtziKsoTvYwcRR0NeWUDuO7kpt5uHu64FNG_I3dqasdSkmG-qG7hxeCAMI9lhgG5XBkYRmHAv2ocWgsFZPeDeC5C4uZwl9dxFQbXmWvfoNhDWz-oL1IuW2RE9wdHpewDfCs8tqGrVku6MxFng4fM104dh_4RgMRlIqxjxqp6l6nt7Qc-gr1yH_tO64QdoUwmSDi3_mMim1fmYh4cmcp8qgp7XPqL-oiY8bkBGwafBYJSyRhm4LqM8HxkjFtR2zroZkaO8WXxRVNIoTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یاشار سلطانی: ‏هشدار می‌دهم ‏نفتی را که قرار بود بر سر سفره مردم باشد، وارد بازی کثیف چند دلال⁩ دزد و چند جوجه اطلاعاتی⁩ نکنید و الا همه چیز رو افشا میکنم تا مردم بدونن چجوری دارید بیت المال رو غارت میکنید
🔴
دوران پنهان‌شدن پشت عنوان‌های امنیتی و محرمانه‌سازی فساد باید تمام شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/142289" target="_blank">📅 20:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142288">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ذخیره نفت استراتژیک آمریکا طی هفته گذشته ۵.۳ میلیون بشکه کاهش پیدا کرده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/142288" target="_blank">📅 20:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142286">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
پزشکیان: اینکه کنار گود باشیم و فقط درباره مسائل حرف بزنیم، کافی نیست
🔴
ایران برای تمام مردم ایران است و به گروه یا جناح خاصی تعلق ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/142286" target="_blank">📅 20:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142285">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
الجزیره: رفت‌وآمد کشتی‌ها از تنگه هرمز برای سومین روز متوالی به پایین‌ترین سطح خود کاهش یافته
🔴
روز شنبه تنها ۳ کشتی، روز یکشنبه ۲ کشتی و امروز دوشنبه ۱۷ اوت نیز ۴ کشتی از تنگه عبور کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/142285" target="_blank">📅 20:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142284">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f4b01950.mp4?token=ScGeHhgb19vejyJn69e-irh5_9sJhkBGe2ioknp86urNbT-XSvdJg9q2uAFou3cmsv8I_65IHPJOjEM30Rzs7zzzJbYW1DD36m1gezxjKsYjTs9r3mlbyVxHUi2u2QbUSzDgeleLaxVCGpNkPxzukG-X9exIotGK9aVcRIoqLiGJYU8oRMNCuetZW9I4a4F7u3hmY7XBHEeV6ayMd-pvD5RJk9xbeOnmnR1MCCnWQ6SzbhsXJt7MXgNKtZsEPKcB79bB7FdnEwuaJxee_FxpgIr2IhbHYoJxi_Vd60kY0lKNJL46ojeC2vNdtXAXqiMLYQcys8rUlQaGayeIbIGhIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f4b01950.mp4?token=ScGeHhgb19vejyJn69e-irh5_9sJhkBGe2ioknp86urNbT-XSvdJg9q2uAFou3cmsv8I_65IHPJOjEM30Rzs7zzzJbYW1DD36m1gezxjKsYjTs9r3mlbyVxHUi2u2QbUSzDgeleLaxVCGpNkPxzukG-X9exIotGK9aVcRIoqLiGJYU8oRMNCuetZW9I4a4F7u3hmY7XBHEeV6ayMd-pvD5RJk9xbeOnmnR1MCCnWQ6SzbhsXJt7MXgNKtZsEPKcB79bB7FdnEwuaJxee_FxpgIr2IhbHYoJxi_Vd60kY0lKNJL46ojeC2vNdtXAXqiMLYQcys8rUlQaGayeIbIGhIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دفاع سابق اوکراین فدرورف:
مرحله بعدی این جنگ، ربات‌ها و پهپادهایی خواهد بود که با ربات‌ها و پهپادهای خودمختار دیگر می‌جنگند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/142284" target="_blank">📅 20:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142283">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
روزنامه دیلی میل به نقل از منابعی نوشت بانوی اول آمریکا نگران است که ایران، رئیس‌جمهور ایالات متحده را ترور کند و این مسئله موجب ترس همسر رئیس‌جمهور شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/142283" target="_blank">📅 20:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142282">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXFfku5bJTGhmzs7FVvvB_h3cMlxwhfTC6kcVDsZLU6RnAbG9iVSEI-QyPS5vzijuKAOBVWLZPUa7KXKdOCU9vXStsmYozXi0eXM3V0E3G44PlWytI_3dpQ0FxIcRFy_z4ixFyGfXXXsHPiTFnvF9kygJ5rul8ixzrZZyY0PsjbWzu-AJNBkUXoTaaerKCiRvdv5nLhjs7408Wc79ltN-in53dtW-6VgMu7nU2hX0p3GcyvUs7cyGCxmaBtM7yb9Cs67XBbBsEwuvHvly2-gan9raxLVrnsU-DrH9b8KKvyAQBY3eILhMRVO1PO7DcJU2wvZ84wL4RG6vkt6UYmcdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تلگراف: روسیه دست‌کم ۱۰ پایگاه پهپادی با ۵۹ ریل پرتاب  نزدیک بخش شرقی ناتو ساخته یا گسترش داده است.
🔴
سرویس اطلاعاتی آمریکا ارزیابی کرده است که روسیه ممکن است با یک حمله محدود، این ائتلاف را آزمایش کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/142282" target="_blank">📅 20:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142281">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
یدیعوت آحارانوت به نقل از یک مقام اسرائیلی: ما در دیدار با کوشنر تأکید کردیم که هیچ چیزی را که زمینه ساز تأسیس کشور فلسطین باشد، ارائه نخواهیم داد.
🔴
نتانیاهو از دیدار کوشنر با رهبری حماس انتقاد کرد زیرا آنها معمار هفتم اکتبر بودند و کوشنر پاسخی نداد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/142281" target="_blank">📅 20:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142280">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c492661c3.mp4?token=vOQ9Va1Hc7ktXsI3-FD022bikj894XEM6ILsMjs08BZhJWr-3icE8x-StgveepSYcUHez4DbtJqSUS8vMdY3OV7L6YcooAncUci8LYEEb5zK6WRSWwSLpwmQmkPOUnoLME4rCSf1xxD1EhVEc3uupBd-TUbE31TKb84eQNjnY8FcTUT_zXYcsB5Dfb3dPkqHchHg8xu1G0-5GlWzn7J73F9Xwk8lBnsBIDlyto9Qb5ADnK3bUuZrPrerz3WBiOtX2rXgzlWD0MCwXmoimE1qFiXeHbqFqsTp1uRRc36yjGzt2PKUX4mtg5AC2iiffk65ep4sKnv2-r1wMrmO4SO5t4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c492661c3.mp4?token=vOQ9Va1Hc7ktXsI3-FD022bikj894XEM6ILsMjs08BZhJWr-3icE8x-StgveepSYcUHez4DbtJqSUS8vMdY3OV7L6YcooAncUci8LYEEb5zK6WRSWwSLpwmQmkPOUnoLME4rCSf1xxD1EhVEc3uupBd-TUbE31TKb84eQNjnY8FcTUT_zXYcsB5Dfb3dPkqHchHg8xu1G0-5GlWzn7J73F9Xwk8lBnsBIDlyto9Qb5ADnK3bUuZrPrerz3WBiOtX2rXgzlWD0MCwXmoimE1qFiXeHbqFqsTp1uRRc36yjGzt2PKUX4mtg5AC2iiffk65ep4sKnv2-r1wMrmO4SO5t4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو نخست وزیر اسرائیل: به رای دادن در انتخابات مقدماتی لیکود بروید و تیمی پیروز انتخاب کنید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/142280" target="_blank">📅 19:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142276">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X882H5LGzRq5IG-SiVnxvTj0vtibRNQjqOLWwYiAK9hVV1mXyD-b9llo8g0kV31P71_oyYAklVgZSaFP6XNivraQ5ar82gnMeoxnWHnEvDXNvRxGn11b-b3vvN2A6eRzcCS2oXmaCXE41tXz7eH8Gs2xtM6ypcKIZzUjxQAoejL8EvsaN1nHOW_dA6ls0q1ooq5VgGG8CvmjaGoZj1Wb8y7EeEYEdSjeeN6iFTjPuRPQxLZpmslNiUk7aup5Ja3ZNymDJDaOIyK4IglT6pa41ELCuBUkd5G_xMobsBBdmHLsDEOsxDfyLGQ8CFDAxPidzUVoOayu4xgiJ9T9i1kjHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nQF7-2OlEJa-JCuOHYgV53aZ8SO9JeEA1ALO7BgcZgUzrA77r7fUcVzK8AtwPuVc2-YPWCnJa2faWjTEnVu24rl8fOPlYX3I3YP6Ol90PNuSjCaw4Ura4qHOap1vGqSSieKaE3kC7zgzOM7wAsiY2qMevyiTiwaM1GuzDY6RooHa9LAkiIrXPbBZCDJalwSODqpsybr2AnQ5a898cNembzFgEvIUyYJnjgONwXfA6Vu51xSIDMFM1fUnBqERmMbwVp3mG_6gfl5Tsiu70iGG5MFlStrRMQQ83nZGK5-DSI0b-43vLTa7HkTlG_jgdCK2YoejXr02GsrZDuPX0e0xog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G7piSbMCUsUc9p8Dvi7g5zzvmmPRzLG3Vcebr4492M8OyhRHpq_aGSGEipP9nvz2qiIcllrT87mSHLYIbIOD3dl9T2Chtiy-Mqv4JocNkkTSdXJcm4rkoOo9RzGbvoydcocMfTCQVUR_S0oB0Ai0CIR2P_mTewWTDAHLwLRi_icacgVv5J-RswpLz8GfTnoZhHYWvimDuAyXdgXwg9BBdqzVav57Vfwg3XyWJzaeJpmmANTvVYWbZBG3TXgcOL-6197SI4cE0EYhoKlt_vHlW2dwPzgK4d4GrZkuM0otHv-H2MsPQLu0BmAfkV1v5iAKW-9MDtWYd8ruT3I2hVKB_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IlXj6ECpN2x1RunH2RzmntEWgO-YNY5FygQNdDTmeq1l4klAaDX6v29nOPg4HYTQGLeqf4y9l3Y0GWL_u2kFZVY-MUAXzgoQq49gZZSLP3eFWRLIe75dq3AXCCr7UPBSfiAJj_87uipgoSZk_sTNmN6jnOJTQZ5K621pypeAY_enfI7PkjZP-qCw3CNTGgTi0WlZSn31jcnwJZIN3RUgsguhavS2XInqPGqFWyegMOR52KFBmMXjDlqI0LhT_dxr1JTCyAnqke6cZpAp8FgkrVxOb1Le9zNh4skbcDilZMLIf55zy5VvEOy8byE_OdGfFOmsoDwVDnIQYiy3no6Kcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ساعاتی پیش، جنگنده‌های نیروی هوایی اسرائیل به المنصوری در جنوب لبنان حمله کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/142276" target="_blank">📅 19:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142275">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCkSVpdR_yQp0_Cys46LFrmdxPVnhY6S7M7FjrQRgDIYYfg6sNzvyanqdyYzDQPQTfsjn1URK_b8cDza62S9zTzx25ADsZTfv0To8KrcWWCySNi1q1Py3m0LqegFm5jdLk_DV1eR8GP1Pjxz4Ti5BW4fUEicMaLyzJhYnDzMpIQ4jZAxUsC4_jTVCk6Qv3N32oXQyMqmrTOEnaoeVJwNc58FEDzQ-E_mrFD1ChJEOy1znwXsJeAiWN9x-kIW22gQ8_W-qlXf0S2REreb_BOGxEyLV42vWbyr1NVxxsFGyIhwlng-qcGYeo3PpJPgJOMZ3rrMwtm4PVIVSlBMBACafQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابراهیم رضایی، عضو کمیسیون امنیت ملی مجلس: ترامپ باز هم حرف از تسلیم ایران زده است. ایران بزرگ تسلیم‌شدنی نیست، کسی باید تسلیم شود که با ماشین غذا و با خفت و خواری فرار می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/142275" target="_blank">📅 19:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142274">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72764905ee.mp4?token=IgVBlkWCWmEXgDN4dCALjXxyif7Mq-7d6X7xpo2Z9ly4jfpAvwuHG6IIN2lL0g7Cab0x486PAxbw6xvcjAGxyysy2QoHRcNARMmZihoscWiLVyn44miJE1v5F_wjHTVEHlHgQSDj4TERvs074DCpbe4K9uR01cSrcdKKiNY-P9GQ368zxwDGuyYpH1w2qYPvhuc341Wz_RGWRYDjSt4JrgPE4qgMI1H1vZF3sNIWM7O5O2oDyesNCnwBb8q_uT5eJ5ot5VqzqtQSpamXNEumMWwkGQ2prqUNOEdbFjXRuh_bCWauWCb6B5Hk0WZUZly7d5FjY6hwrbwTL0A1iPL-cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72764905ee.mp4?token=IgVBlkWCWmEXgDN4dCALjXxyif7Mq-7d6X7xpo2Z9ly4jfpAvwuHG6IIN2lL0g7Cab0x486PAxbw6xvcjAGxyysy2QoHRcNARMmZihoscWiLVyn44miJE1v5F_wjHTVEHlHgQSDj4TERvs074DCpbe4K9uR01cSrcdKKiNY-P9GQ368zxwDGuyYpH1w2qYPvhuc341Wz_RGWRYDjSt4JrgPE4qgMI1H1vZF3sNIWM7O5O2oDyesNCnwBb8q_uT5eJ5ot5VqzqtQSpamXNEumMWwkGQ2prqUNOEdbFjXRuh_bCWauWCb6B5Hk0WZUZly7d5FjY6hwrbwTL0A1iPL-cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بالن جاسوسی آمریکا مجدد در آسمان استان اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/142274" target="_blank">📅 19:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142273">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
داده‌های ناوبری دریایی نشان می‌دهد که یک نفتکش متعلق به یک شرکت اماراتی هنگام عبور از تنگه هرمز، متوقف شده است.
🔴
طبق ترتیبات ایران برای عبور امن از تنگۀ هرمز، مسیر ایرانی یکی از شروط است و پرداخت‌بهای خدمات و اجازۀ ایران از دیگر شروطی است که نفتکش‌ها باید رعایت کنند.
🔴
نفتکش امارات در نزدیکی قشم متوقف شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/142273" target="_blank">📅 19:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142272">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
بن گویر، وزیر امنیت داخلی اسرائیل: ما هر شب باید حداقل ۳۰-۴۰ تا ترور هدفمند در غزه انجام دهیم. نه فقط اونایی که برای ما خطر دارند، بلکه اونایی که ارزش زندگی کردن رو ندارند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/142272" target="_blank">📅 19:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142271">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foCQp7RMbgoWdlcr2JyLvyXcYN1K0ViqtChNfUmFUzhkx6i0rIeRw8q2n1fqvMFxt7unLaRPWfjctOdMFgBvyW8XdBT197gqIYqu4-ZWG8-TWjHUIr8enP6f9ILzKGUD-XP9OYHbXcmMHEQ7NX0_KHx1ct0hWn4AScbCgMQAmnoPTA6Mpk0jiK8tUrzI1gXEVvQAJCehgNGyZ-ItnJspuTkMFRxXulasDN7OPVSOjinAvd9C-RiT5pHSe3PkxXoEIABtZd_Wx_0K4In9csmEHc073Tm0X3BXgdm_bn4mifAW3-CxfyOHGUXSMhrMd7Ckc8OeoGIlzznAn9BAMNL-2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بن گویر، وزیر امنیت داخلی اسرائیل: ما هر شب باید حداقل ۳۰-۴۰ تا ترور هدفمند در غزه انجام دهیم. نه فقط اونایی که برای ما خطر دارند، بلکه اونایی که ارزش زندگی کردن رو ندارند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/142271" target="_blank">📅 19:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142270">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
سی‌ان‌ان: کوشنر بیش از چهار ساعت نتانیاهو را تحت فشار قرار داد تا طرح آتش‌بس ترامپ برای غزه را پیش ببرد
🔴
نتانیاهو در برابر این فشار مقاومت کرد و با اشاره به انتخابات اکتبر، تأکید کرد که پیش از هرگونه عقب‌نشینی اسرائیل، حماس باید به‌طور کامل خلع سلاح شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/142270" target="_blank">📅 19:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142269">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c96f732b1.mp4?token=tE0pcG2EhK-pyWQu1cRN7H9yjaLRfqYZPjpMyZKf8pqr2VUS8T1I5vQFq8NYSjqcQ6-cwTtYykRZc43HNUP2IJUwyvsUAyJSPpNCuHtEGE4Nz32_L58cAQ8EqqypkIOqAUpWdWUMAA3GDKyzBS0fvbrALLUy66yas0KS51cEq1AB1EJF0_Y9pMAyUv01Qr5aYTs1xed0xzca_Wcke-21fAUmrf7m9QsVnfvUFUKxMXnE2GAVIiNrNKBo4OWkSXKk_K2sFkV2Yp1mXTdt1bWyQt3c0poagpP7wjgVoi6Mk_cUun4jvzUjIAPbr9BsXx-gZSrF5ESHe9Nt4uhfCD_kVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c96f732b1.mp4?token=tE0pcG2EhK-pyWQu1cRN7H9yjaLRfqYZPjpMyZKf8pqr2VUS8T1I5vQFq8NYSjqcQ6-cwTtYykRZc43HNUP2IJUwyvsUAyJSPpNCuHtEGE4Nz32_L58cAQ8EqqypkIOqAUpWdWUMAA3GDKyzBS0fvbrALLUy66yas0KS51cEq1AB1EJF0_Y9pMAyUv01Qr5aYTs1xed0xzca_Wcke-21fAUmrf7m9QsVnfvUFUKxMXnE2GAVIiNrNKBo4OWkSXKk_K2sFkV2Yp1mXTdt1bWyQt3c0poagpP7wjgVoi6Mk_cUun4jvzUjIAPbr9BsXx-gZSrF5ESHe9Nt4uhfCD_kVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مقام‌های محلی در ایالت اوکلاهمای آمریکا پس از وقوع آتش‌سوزی گسترده در یک مخزن گاز طبیعی، دستور تخلیه ساکنان اطراف محل حادثه در شهر گلن‌پول را صادر کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/142269" target="_blank">📅 19:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142268">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
وزارت نیروی: 4200 مگاوات برق را در نتیجه جنگ از دست دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/142268" target="_blank">📅 19:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142267">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
المیادین به نقل از یک منبع بلندپایه ایرانی: حادثه‌ای که امروز در اربیل، در اقلیم کردستان عراق، رخ داد، نمونه دیگری از عملیات «پرچم دروغین» است.
🔴
ایران هیچ ارتباطی با حادثه‌ای که در اربیل رخ داد ندارد و عملیات‌های ایران به‌طور رسمی و صریح اعلام می‌شوند.
🔴
هرکس به حاکمیت ایران احترام بگذارد، از احترام ایران نیز برخوردار خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/142267" target="_blank">📅 19:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142266">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک مقام اسرائیلی:
نتانیاهو و کوشنر توافق کردند که یک ژنرال آمریکایی بر روند خلع سلاح حماس نظارت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/142266" target="_blank">📅 19:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142265">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
یک مقام دولتی پاکستان در اظهاراتی به «ام‌اس ناو» مدعی شد که مذاکرات برای بازگشایی تنگه هرمز و پایان مسالمت‌آمیز جنگ ایران و آمریکا همچنان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/142265" target="_blank">📅 19:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142264">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0512c8ba1b.mp4?token=g1rOb43XcgdH9XDY2fxc1hd-_rAUrINnD96GA6Iokp41SVLfbu9HpsvIhv7LIgN5bVmQfXaFxNTjKZ2u_y3oaJYHS0BB3Hgev1DY7V_vuTVxQOOCCt_r_NCb0hrMZmYJu_qAyzP0s-S3vwjK_4NXf4QsppliLYPbFo0gYQnUZFZ-7dA8uyxVz_0vsbSv0ohuDYEZr3qzoXGzIZgSxY5qbGPP3yrNu5rC3eKziiqVb_CkBpvG8njh54J1Md-NsfJ5fxnpkprlr8A-2kUOrQm8c8I_RVtwhGvBX4OSJabGZM7AazItdkkVM8pkxSc9GBDL9TjLvC-l-KuVWnE-zwsW_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0512c8ba1b.mp4?token=g1rOb43XcgdH9XDY2fxc1hd-_rAUrINnD96GA6Iokp41SVLfbu9HpsvIhv7LIgN5bVmQfXaFxNTjKZ2u_y3oaJYHS0BB3Hgev1DY7V_vuTVxQOOCCt_r_NCb0hrMZmYJu_qAyzP0s-S3vwjK_4NXf4QsppliLYPbFo0gYQnUZFZ-7dA8uyxVz_0vsbSv0ohuDYEZr3qzoXGzIZgSxY5qbGPP3yrNu5rC3eKziiqVb_CkBpvG8njh54J1Md-NsfJ5fxnpkprlr8A-2kUOrQm8c8I_RVtwhGvBX4OSJabGZM7AazItdkkVM8pkxSc9GBDL9TjLvC-l-KuVWnE-zwsW_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری صدا و سیما فاش کرد: قطعا ۴ اسیر هم در کویت داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/142264" target="_blank">📅 18:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142263">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
یک حمله بمبی به یک مدرسه خصوصی در کابل انجام شد که منجر به تلفات ناشناخته‌ای در میان دانش‌آموزان شد.
🔴
مدرسه مورد هدف در منطقه‌ای واقع شده که عمدتاً توسط جامعه هزاره، که عمدتاً شیعه مسلمان هستند، مسکونی است.
🔴
هیچ گروهی مسئولیت این حمله را بر عهده نگرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/142263" target="_blank">📅 18:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142262">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
داده‌های شرکت ردیابی نفتکش‌های «کپلر» نشان داد که عربستان سعودی در پی افزایش ناامنی‌ها، ارسال محموله‌های نفتی خود از مسیر تنگه استراتژیک باب‌المندب را موقتاً متوقف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/142262" target="_blank">📅 18:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142261">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
یکی از ممبرا پیام داده گفته پارسال به بچم گفتم پول چیپس‌هات رو بریز قلک سال بعد پول زیادی جمع کنی اونم پول ۵۰تا چیپس رو ریخت تو قلک و دیشب باز کرد و الان پول ۵تا چیپس داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/142261" target="_blank">📅 18:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142260">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVDepP_lsYawjZYKagTJ1dgTCJA1oxO6ufKi7xRg_OMZGvKUz79l021P08SQ_NQhjcTKTfDZTL49T4H3bOr_twsnk8LIMfrQz6EsCmUAK51RicJaX_h4z9E4M7PFSuddr_tp65TKMFVTzh0snAMgiFusQMfvFf6b0CobtEpSW9b_3arOv-kQZ8B8gMpeDxtOK4JGX2H2JYhXWP-5CyIuPJypXeEZiAWYI55I4hI2RFps_1_7ywWttl5qMfB3R73jk2Ch3YHP8kpPiD9LzBsfSlFaB2LvLKDpOLw4zCqVu-di6MEwMyrz48TnnVW_tD5mR710sZbImOFj3846HNKgeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دفتر نخست‌وزیر اسرائیل: نخست‌وزیر و هیئت صلح گفت‌وگوهای عمیق و سازنده‌ای داشتند.
🔴
توافق شد که دو گروه کاری تشکیل شود؛ یکی در زمینه خلع سلاح و غیرنظامی‌سازی غزه که هم اسرائیل و هم هیئت صلح مصمم هستند این کار سریع انجام شود و پیش از هرگونه بازسازی در غزه به پایان برسد.
🔴
گروه کاری دوم بر بهداشت، آب سالم و سایر مسائل بهداشت عمومی برای مردم غزه تمرکز خواهد کرد که این مسائل همچنین بر مردم اسرائیل نیز تأثیر می‌گذارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/142260" target="_blank">📅 18:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142259">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhUa1x1FQhEYxfdeTCBI17AzEQtw9tgjs2KHxap5yjiy5s1gJX9qOrZ2V07w7nFQc3oWf_Kdpl87q9wrjtayozScTW9nuoCAmhmqkauFoAlcU_pnxAMK2DbUsgzuvUIPExMF_FZCeRONNpw7SuaUUEg5Kj87JkNX8141mgk64c0D1p6a1HaCEN6UVOyja1vj01WKzlFi7a9ZtXdQsIzFv8VVU1gJpCUHfVCU26bWW3N0yLALBk9Htt7GfaClpRObBbMVq0JxH0A4-GvAVYa1c2Q_MPbVCAOTQIitTY5obHqKspgfpJ8Z8Jwl6fkEyF5fi5QvvqDbb-Yekozgwt9YRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
د
رخواست صلح از طرف پاپ!
🔴
‌بار دیگر درخواست خود را برای پایان دادن به خشونت‌های جاری علیه غیرنظامیان فلسطینی در کرانه باختری تکرار می‌کنم و فوراً از جامعه جهانی می‌خواهم برای پیشبرد راه‌حل دو کشوری و دستیابی به صلحی عادلانه و پایدار تلاش کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/142259" target="_blank">📅 18:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142258">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhFpWBcX5-gSyUhPZ9ToclqFrrL0Su7v7OC4wgpZb7joeqBYof5zW86IKCHVI28uUNve2YvSpU5Wv7i-E1FGDEvsYU2M7OToGQjFdB_hMGlWhvYhcCLfL62Vm47R89ziuxspf-qQ2OR3gioEuMmG9xcIyK0xWFzwtFc2OgyYBoKcYuuPU-ezr3a0MRLGvIuzkurnakXBgnXTmEHfpj1K-eYebz9-K1tKSkCGtzCAuvbPBeXgF0O7kowoKuN4aOD5YJoUBBM3MiF_wnY2Qv4CKT5RYZpS7mzItrtqB0YCUgk6bMC6VPvU4IjKm79lkogUXYtEPAaXFIc2clfzGWdRrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شرکت ریتئون از گروه RTX قراردادی به ارزش ۲۲.۹ میلیارد دلار و به مدت هفت سال با نیروی دریایی ایالات متحده برای افزایش تولید موشک‌های کروز تامهاوک به بیش از ۱۰۰۰ موشک در سال به دست آورده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/142258" target="_blank">📅 18:38 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142257">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
رئیس جمهوری لبنان: از برقراری روابط با ایران بر اساس «کشور با کشور» حمایت می‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/142257" target="_blank">📅 18:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142256">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffb511082b.mp4?token=YIpnaAe79r8BZAbgbNwYNw6L7ms1cB78rMmr0Z6-vK-Ko0W-iNKeaLXUH0zznkHR_FmWk8H8OJV1xz3CcNXl566xpVSVFNF_KBnitwZ6F4iE93NqDIdmCdt_4sGuW2Wv8NNrsVFTuK4hA-9v3kFETb4-BdNdv2ylhnuHqLuWZ8q0p3YKsJkr1ngf2-6FvvKDs9NK2dCp0t8dL-ogP7t0CCunjiqZp7Hrj6cgSFuQb6X1Mo6rX9LGro6IR49u7LgVP0BR9nRCv3S-Uo4njVl3SajrA9MjQVg2mcTbS_fF--gAgS9AlqF6Cc1-ol_4AG-Fb9ZfiqEm-RqGEpp150BmXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffb511082b.mp4?token=YIpnaAe79r8BZAbgbNwYNw6L7ms1cB78rMmr0Z6-vK-Ko0W-iNKeaLXUH0zznkHR_FmWk8H8OJV1xz3CcNXl566xpVSVFNF_KBnitwZ6F4iE93NqDIdmCdt_4sGuW2Wv8NNrsVFTuK4hA-9v3kFETb4-BdNdv2ylhnuHqLuWZ8q0p3YKsJkr1ngf2-6FvvKDs9NK2dCp0t8dL-ogP7t0CCunjiqZp7Hrj6cgSFuQb6X1Mo6rX9LGro6IR49u7LgVP0BR9nRCv3S-Uo4njVl3SajrA9MjQVg2mcTbS_fF--gAgS9AlqF6Cc1-ol_4AG-Fb9ZfiqEm-RqGEpp150BmXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری مشهور آمریکایی و از افراد نزدیک به ترامپ، صحبت از به کارگیری بمب اتم علیه ایران می‌کند
🔴
مارک لوین ایران را با امپراتوری ژاپن مقایسه می‌کند:
"رژیم ایران تسلیم نخواهد شد.
🔴
می‌دانید، ما قبلاً در جنگ‌هایی بوده‌ایم که با دشمنانی جنگیدیم که آنها هم تسلیم نمی‌شدند...
🔴
ژاپن را یادتان هست؟
متاسفانه، ما مجبور شدیم دو بمب اتمی بیندازیم تا آنها تسلیم شوند."
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142256" target="_blank">📅 18:27 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142255">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLtDOsQjBp-fYHYOmpVvSRNPIS1gTliWAcJ9TrBVXw_XqCHGyunbOlzOdXema3dtLytfMK2qgs5WjFLsGMti478tBt3mK-6K4ATVQMv3nk8m27Ph0ChmyRYXR2ny1_22VzypfEmM89URgXs4t3mMyZAjNUjXgbfmLy82mSK3YGsWk26P2OtZ3laD9LxsEyXITAv7W39C5IjYTscSF0gNYCYqP7oZbo-LiCoqw9UNaXROiiswolok0x5gGM3E34y-Wv4C_kwlzes3Oj7II1SetUe4QPbmp8VvJ8188z8jMh_uMugILGG76dAr_GueozQt-Vgzw7fyWcoDNcbdP0RMsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
۲۰۰ میلیارد دلار زیان در بازار سهام امریکا در معاملات ابتدای هفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/142255" target="_blank">📅 18:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142254">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره :
@khabar
◀️</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/142254" target="_blank">📅 18:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142253">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a545b29a7a.mp4?token=eO1-lwbdS6pzzbcW01NIdX9vseR6wE7RmnZp8nTJhhySD6ykzpDL0PuF4QDROh7DY1hvnOPCHL9SmwJ6yXuDVaF-ChmygRvo9awtGULkSn2Aj7qvEm3VjtkFrXgi9BP8tbQm9Sx4Roo53L1BT5uhyT4NXWctqA03nEqmav73KN0QOkKs72zVGkTzlY_mH3FkH5INqaSTJCx7A3PkY9OxqmTl7CZYEo0YtCp0qkN5LVpuowqM-3pnAW3Gr7QgOEMU8VzGemABXOvU7BjtETsAPgLqNb389lXyTZWvYV-MFtvJ6yP5yT78QlJ2r_7GIPxQcbR7rCLOJHmKH465X_JtuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a545b29a7a.mp4?token=eO1-lwbdS6pzzbcW01NIdX9vseR6wE7RmnZp8nTJhhySD6ykzpDL0PuF4QDROh7DY1hvnOPCHL9SmwJ6yXuDVaF-ChmygRvo9awtGULkSn2Aj7qvEm3VjtkFrXgi9BP8tbQm9Sx4Roo53L1BT5uhyT4NXWctqA03nEqmav73KN0QOkKs72zVGkTzlY_mH3FkH5INqaSTJCx7A3PkY9OxqmTl7CZYEo0YtCp0qkN5LVpuowqM-3pnAW3Gr7QgOEMU8VzGemABXOvU7BjtETsAPgLqNb389lXyTZWvYV-MFtvJ6yP5yT78QlJ2r_7GIPxQcbR7rCLOJHmKH465X_JtuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رسایی
: «۹۰ میلیون ایرانی متهمند، مگر اینکه خلافش ثابت شود»
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142253" target="_blank">📅 18:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142252">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
اطلاعیه رادر کلودفلر:
ترافیک اینترنت بین الملل ایران از ۹۰ درصد به ۵۹ درصد رسیده ،وضعیت الان اینترنت ایران دقیقا مثل روزای قبل از قطعی ۸۸ روزه ی اینترنته و با اختلالات بسیار سنگین همراه شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142252" target="_blank">📅 18:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142251">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
طی اتفاقی عجیب شهرداری الیگودرز لرستان، کف رودخونه رو آسفالت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142251" target="_blank">📅 17:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142250">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0T5lQWekK2BR9Ogb0VXRrqF-u5e3nt2Qt46Sm0qM2HBg707DkNXe4NPH0zEl1lTh2yLmhBeGxxh3e8uY_tlOnOng6S_9ds4QL-s6ZRDaJ9L6hEfZpIXVs5JVsmtX583aalIcqqyGkvKmlvgX6VH_O3kK_H7ULITI7Gmp68ZSvzuVdQ4vxFvY_yQW61gRLgtn5B8aAbZJKn6zIz0o9jEw_PwloZQp15TfpBxMakzBsIbYuNizezdneTvgUlejOV_OzSlb0krJ7wylBde7iyu15n0GYZOy1on5YJTFgA413LJYjIIMhZqsfGB50EYWw9gTUVHN2ehpBZ9aTUZiY531A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد رائفی پور:به ترامپ مشکوک هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/142250" target="_blank">📅 17:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142249">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
مقامات پاکستانی: مذاکرات با هدف بازگشایی تنگه هرمز و پایان دادن به جنگ همچنان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142249" target="_blank">📅 17:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142248">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ME-ovMUrlvmfVSxZNrsL_1j5kyNcGaiebZShnyGVnAjM4_j7uhqViTQClFwowLDa_CpFkV7rl6xtEDEEpBGFFyA5yHZdjVcJX63njUifo1lmIcjFnjyIxAMTLKlnaKDgWBp08-ab5cExHiAdlmFKLyhCciHNxENKYTCHf1j9xDINQ7nGnF0aL6W-6j6J3NOCW3gbSCM8u7C-R8xR_KfjePaOyGy5fGblViJFiGYTDhxYt-EhfBTnQe5m6LYyUj4fZNhD6d7KRm5u568-sb7osnSF3-unFNGzqjFKZIeoPwiP9cJN1qM-_-ZxYdYk1syfJwr6-VY5cGLWv1ugcsx2uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ظریف: قرار بود بعد رفتن آمریکا از افغانستان، نظام شاهنشاهی اونجا مجدد برگرده اما ما نزاشتیم و کمک کردیم طالبان قدرت بگیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/142248" target="_blank">📅 17:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142247">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358b452f1a.mp4?token=KgsTpyBtSnOgcxFThacvSYcic67ppwnYCACqH_1iP8I1YV8m84Q-ADmkei72BjlLOTiZFoPJ6X07iBnsxOKPDa8CGzDNnAeOyiWENLBxkPvXrL9U8fSK5GGLA_zlU6u0RL1vHlV4oCgfacJ_uZDPytKnE6jV_wgutzGg6u3w9lu08GgOi3HlANzPzxYkwbGAQu58ncUc6PtGh8WbwYtsGPrG_xuNAM4tTciATDxZGulbRC-AFAFvK1TNFnlNWeYjM54ZfG6FYpCwNODWeNGbUd0sy03Br7hURoEqllY6SXgB4brOdne57-KiFIzlMZzxYCWg9MrjCjNDJLFtfgddYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358b452f1a.mp4?token=KgsTpyBtSnOgcxFThacvSYcic67ppwnYCACqH_1iP8I1YV8m84Q-ADmkei72BjlLOTiZFoPJ6X07iBnsxOKPDa8CGzDNnAeOyiWENLBxkPvXrL9U8fSK5GGLA_zlU6u0RL1vHlV4oCgfacJ_uZDPytKnE6jV_wgutzGg6u3w9lu08GgOi3HlANzPzxYkwbGAQu58ncUc6PtGh8WbwYtsGPrG_xuNAM4tTciATDxZGulbRC-AFAFvK1TNFnlNWeYjM54ZfG6FYpCwNODWeNGbUd0sy03Br7hURoEqllY6SXgB4brOdne57-KiFIzlMZzxYCWg9MrjCjNDJLFtfgddYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
خداداد عزیزی: دخترهامو زور نکردم روسری سرشون کنن. برام مهم نیست چی دربارم میگن، حکومتی بودم که بیکار نبودم
@AloSport</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/142247" target="_blank">📅 17:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142246">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrH6QXjN_NNm2w2aRq0EANfbt9YLmefeGRjQ11pih7iezNraRQYJ7if34PYMup_SvMoUb1U4Bm6KxEGILfPAGh1e_qJLcWorlhqqD0P3i-c2oQjzmK6lvKxXseQJQW7Vr7g5UxuKdg54aHjbyPNg8AtkrjdyC73ws6BHgF07g-8lXGtRNS-tnXP99Ho-zqBH9ZWfgeJiuTFzuFJ6V-9MszvrlMS15MGQfAm3z-Zpl8wjez2ElKmnXnlENA-MyKwjNKXiAnifnrgC_BpTxkYgRwRBaZ6E2DbjxIWlILCRWbSRA7I9CG16Z7kGX-Mwdn44tLVKlMHIquRETTF6F1p8uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
مصطفی ایزدی، جانشین فرمانده کل سپاه پاسداران:
🔴
دنیای غرب تشنه معارف انقلاب اسلامی ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142246" target="_blank">📅 17:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142245">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHxMp_YqgwKhz3vna8cIRVt1g7_r7sn7G-x20WbTfxJFsow-1qNp3Byv1gdnkfY0UXd8gOZjssCe8Nd6wzFzNb8dUZ5zC-RvqbH12vkxbs_3uAe8ZXiKAJN16JgfYUHXX9mIxIlD8kcgmhRprRIGEAbANMDXpt-tMO6_fv8qW8dCx94noKR_C3sgDmWrbKLRWykQLEDMLB7RSz86Sbh1tSLA6gcjHLGm9EMVuIu-MnVBcP4sdo6LiWXjOVyEBT2KHcrhpD1TJmU8VhCrr5nBWI7BrF5hIkTvXA6mRgeRVhvJYmPp07C9iUBFC1-V7SaKkr3D_Q4ICu34olLaZQOnkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
متاسفانه قطعی برق ۴ هزار ماهی آب‌بندان در بابل را تلف کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142245" target="_blank">📅 17:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142244">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
حماس: از درخواست ترامپ برای توقف حملات به غزه استقبال می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142244" target="_blank">📅 16:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142243">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlg9MxzmrTUgypnbLtlqIzIO8M5ESIiEBqA-E7tmSC_ST8uzVreTWydwi-yepI63GmwED4GLalHkZhr-cG6xtJvVVYGhe4eISwELdu8xJnej_r60UI05zgirCmyuDNK4S6dOL71qfE77YTXJqDIBFbXR6o7Xl50l82e_pmVxCNMIzQA9zE53Rq7fEDFrd3G-HUqCZQpw6DBzCZGsD4lXxVsop0fWxbmboJ863H4brr7j6jo4zpJrwCNfJtVOi1KrVzp_qJP8iRrr46gbIxbeFKsLLnw6Be8gNL5jtNuwzXjNoixNA4U4vE02gVCqGJN4XB1elvQY4JnUJUPGUJKViA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش سی‌ان‌ان،
ناوشکن نیروی دریایی ایالات متحده،
یو‌اس‌اس بنفولد،
ماه گذشته در جریان عملیات در
دریای چین جنوبی
دچار قطعی برق شدیدی شد و خدمه تقریباً ۳۰۰ نفره آن بدون سرویس بهداشتی، تهویه مطبوع، خدمات آشپزخانه یا سیستم‌های آب آشامیدنی در گرمای شدید رها شدند.
ناوشکن کلاس آرلی برک در ۲۴ ژوئیه پس از یک نقص مهندسی مرتبط با ژنراتور، برق خود را از دست داد و به مدت چهار روز قادر به مانور با نیروی خود نبود. یک کشتی جنگی دیگر قبل از اینکه یدک‌کش‌ها بنفولد را به خلیج سوبیک در فیلیپین منتقل کنند، غذای پخته شده ارائه داد، جایی که برق شش روز پس از نقص اولیه دوباره برقرار شد. هیچ آسیبی گزارش نشده است و نیروی دریایی در حال بررسی علت آن است. این حادثه دومین قطعی برق گزارش شده برای یک ناوشکن آمریکایی در هند و اقیانوسیه در سال جاری است و در حالی رخ می‌دهد که نیروی دریایی با افزایش فشار عملیاتی ناشی از جنگ ایران و سایر تعهدات جهانی مواجه است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/142243" target="_blank">📅 16:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142242">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
عارف: سهمیه اول بنزین کاهش نمی‌یابد، اما سهمیهٔ دوم به‌تدریج و در راستای آزادسازی قیمت‌ها کاهش می‌یابد.
🔴
خلاصه: نم نم جا میکنیم درد نگیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/142242" target="_blank">📅 16:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142241">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترامپ: ما یک کانال ارتباطی مخفی با سپاه پاسداران داریم
🔴
ما مستقیماً با مقامات سپاه پاسداران در ایران در ارتباط هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/142241" target="_blank">📅 16:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142240">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
گویا اینترنت بزودی بازهم گران خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/142240" target="_blank">📅 16:19 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142239">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
مقام ایرانی به رویترز:
ایران سیاست خودشو از دفاعی به هجومی تغییر داده، واسه همین چند هفته به آمریکا ضرب‌الاجل میدیم که توافق نامه رو کامل اجرا کنه وگرنه بهش حمله میکنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/142239" target="_blank">📅 16:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142238">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
نیروی دریایی ایالات متحده قراردادی ۲۲.۹ میلیارد دلاری برای تولید موشک‌های تاماهاک به RTX اعطا کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/142238" target="_blank">📅 16:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142237">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
مدیرعامل آسیاتک: مردم بی‌رویه اینترنت مصرف می‌کنند چون قیمت هر گیگ اینترنت ناچیز است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/142237" target="_blank">📅 16:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142236">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6764e436a3.mp4?token=EHwK9VGTiR6_I4iofpqqVsZFd0nVkMxiCZ1KWeqQyRUpuznynQL10dmvNv7euld-IY1_1AEr7Qn0T2PavG3fDGPEHthVF_kSLx1qmM6cejjXI31xMxxng4Q2N_sXqG_P5mQwXM8ZVJlVlEVHSX4StyCXdfI6Wds2DJZBt8w55AVhN9XkO6CbPqLjYyE966MZCcaA5JYAfmEfNFAIm0cFJPCyySswJJxDLR9s6zvwkgRnbeZ9J-VCc5NU12vRmA5kNbLuCUbFwt4ahwUfgfXUyH2H_F3i452gx8b35LBWsR-dTOZBu27gzSmLBXqmdUkbyVn9l60SgE16hW_vUL1VCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6764e436a3.mp4?token=EHwK9VGTiR6_I4iofpqqVsZFd0nVkMxiCZ1KWeqQyRUpuznynQL10dmvNv7euld-IY1_1AEr7Qn0T2PavG3fDGPEHthVF_kSLx1qmM6cejjXI31xMxxng4Q2N_sXqG_P5mQwXM8ZVJlVlEVHSX4StyCXdfI6Wds2DJZBt8w55AVhN9XkO6CbPqLjYyE966MZCcaA5JYAfmEfNFAIm0cFJPCyySswJJxDLR9s6zvwkgRnbeZ9J-VCc5NU12vRmA5kNbLuCUbFwt4ahwUfgfXUyH2H_F3i452gx8b35LBWsR-dTOZBu27gzSmLBXqmdUkbyVn9l60SgE16hW_vUL1VCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با حرفاش موافقید؟
👍
👎
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/142236" target="_blank">📅 15:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142235">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ترامپ: محاصره دریایی آمریکا به اعمال فشارهای اقتصادی جدید بر حکومت ایران ادامه می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/142235" target="_blank">📅 15:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142234">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
رویترز: قیمت نفت بدون تغییر و در سطح ۸۸.۵۵ دلار در هر بشکه باقی ماند
🔴
قراردادهای آتی نفت برنت تا ساعت ۰۱:۲۸ به وقت گرینویچ بدون تغییر در سطح ۸۸.۵۵ دلار در هر بشکه باقی ماند، در حالی که قیمت نفت وست تگزاس اینترمدیت (WTI) در همان زمان با ۱۴ سنت کاهش به ۸۲.۲۶ دلار در هر بشکه رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/142234" target="_blank">📅 15:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142233">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فووری/خبر مهم درباره ابر تورم
👇
https://t.me/+S8mMBRHkHmFiMTFk
https://t.me/+S8mMBRHkHmFiMTFk</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/142233" target="_blank">📅 15:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142232">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
علی قلهکی: تغییرات مهمی در قوه قضاییه در راه است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/142232" target="_blank">📅 15:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142231">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ترامپ: انتخابات میان دوره‌ای آمریکا کوچکترین اثری در مورد دیدگاه و نظر من در مورد ایران ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/142231" target="_blank">📅 15:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142230">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjZEnbPm7mxL_KHKc1xUpuxkgyQpFq5SPblkgjXToGnL_dOprtDLWQAj2qmmkueNnsjgbqrclAooP6qDCcbjgoj3ifAwg7g8QPgmiWPAqlQqqXU9MOO2wOBJjijw-WTi195e-4XyIIxvF6Q0IT_1ax4Sd_ERbmxdme-HywJg2QJIEyGlU_qi5vTO0mtlY8mTp8-vXu0sWDC9YaOw98f8dMqJ0yv1qKhL1iUlJ4lDJvPNsgxQSVaI1Xj0J7pkjGwAjnYZRojf8kYzaqjMGpBeICNfeSChkNWnZuZDw_al2DsCoMVXP--B5b9gubvu3yn-wH3cVWh-2OhVEq84U0VCMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از یک کشتی عربستانی که ساعاتی قبل، توسط حوثی های یمنی در تنگه باب‌المندب هدف قرار گرفت!
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/142230" target="_blank">📅 15:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142229">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
کلش ریپورت: رهبران حماس در دیدار مستقیم با جرد کوشنر، فرستاده آمریکا در مصر، تعهد خود را برای خلع سلاح کامل و غیرنظامی‌سازی نوار غزه مجدداً تأیید کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/142229" target="_blank">📅 15:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142228">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f72ceb115.mp4?token=ufso8jh92W77f1ouv96_S2dt25sKy-1_qMf32ZYgFP0Jn_8EoyDVDno8CiwiEHoefxEyIrfEOrZt3nyhiSfsv_1IfMt1YWUveppXua-zmaJmwuy_z5dWsW0WK-bMDb24bwd00rvrxjKIIBsA_lkflRPBmecCev3h41GHO4KqmOw1WsrchpWidhds_Z2wZS64scYC8rrs7B4dIe7-XV4NTDB05FlMsFM2JGBUuUBKr4gNoim947iHmgYrvEjVjygGit9LUVHn8bmfYpvD4v_4zDYFSkUDAlEAerhVmPtxecgMDS6m-86gPZagdfn2hTe_ebkQSOPQxKcNoaHH4Mlz4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f72ceb115.mp4?token=ufso8jh92W77f1ouv96_S2dt25sKy-1_qMf32ZYgFP0Jn_8EoyDVDno8CiwiEHoefxEyIrfEOrZt3nyhiSfsv_1IfMt1YWUveppXua-zmaJmwuy_z5dWsW0WK-bMDb24bwd00rvrxjKIIBsA_lkflRPBmecCev3h41GHO4KqmOw1WsrchpWidhds_Z2wZS64scYC8rrs7B4dIe7-XV4NTDB05FlMsFM2JGBUuUBKr4gNoim947iHmgYrvEjVjygGit9LUVHn8bmfYpvD4v_4zDYFSkUDAlEAerhVmPtxecgMDS6m-86gPZagdfn2hTe_ebkQSOPQxKcNoaHH4Mlz4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: به نظر من، مناسب‌ترین کار این است که من از دخالت در انتخابات اسرائیل خودداری کنم، اما ممکن است از یکی از نامزدها حمایت کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/142228" target="_blank">📅 14:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142227">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aea77c36c6.mp4?token=QOVDUkr9wVUubsEwvJgKBR1EzjR6owDRUn8UbvjD1ONWOYgwG9rD8GwMJ9JxhZWt7LKZ7ZryrBvrSNEEUjfBjiPiRliUSRLCbOM3mqG0BTLdrSC4UvS2rXsIdRkPBS3Wo58ajhGB3Fwe2_5Zz8-cPNjWDl9h4eE23FFAWWYzYrF-McBuDmtmfylg0VED9FGqG38AG7xWPMljiwABX2-rv-gny90SjMWTPD5RJaXZo_54Q4edPdMkGA_UbFAG02AhZ9bdtxLrpU0kFnT-uIzr-l8UkPHuItMU9NkXnMsvgrnQ_NuMbCY--LZKowoa3X-xjJqcMFPFcikXMWE-HDcv3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aea77c36c6.mp4?token=QOVDUkr9wVUubsEwvJgKBR1EzjR6owDRUn8UbvjD1ONWOYgwG9rD8GwMJ9JxhZWt7LKZ7ZryrBvrSNEEUjfBjiPiRliUSRLCbOM3mqG0BTLdrSC4UvS2rXsIdRkPBS3Wo58ajhGB3Fwe2_5Zz8-cPNjWDl9h4eE23FFAWWYzYrF-McBuDmtmfylg0VED9FGqG38AG7xWPMljiwABX2-rv-gny90SjMWTPD5RJaXZo_54Q4edPdMkGA_UbFAG02AhZ9bdtxLrpU0kFnT-uIzr-l8UkPHuItMU9NkXnMsvgrnQ_NuMbCY--LZKowoa3X-xjJqcMFPFcikXMWE-HDcv3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد حماس: ما یک کانال ارتباطی متفاوت با حماس داریم و در نهایت آن‌ها سلاح‌های خود را زمین می‌گذارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/142227" target="_blank">📅 14:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142226">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ترامپ : اسرائیلی‌ها نباید در غزه حمله کنند، زیرا حماس موافقت کرده است که سلاح‌های خود را زمین بگذارد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/142226" target="_blank">📅 14:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142225">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af9189453b.mp4?token=gRWY6Z_K1ddPuR6GcxcOsbeinuWmoaWkOAzmujK1IRtlxVsooGky4kIgAQDSMHwrrhFM3JAWitHF8hwjdpjz_1SMnEJflyC7z5MpctvbjO4r35ZoBLrdHlDECnHmg30r665U4ZjdNMGxYrZva9rkYRssMJ0gYyt2r0-eY7XltVDGII8DrYiJ-wI1tBeLY7EBb6N69Q1HBcfBIvxePZU-46dTzO5ByMY-sRPpXd5vMjfBhTX8miPKQ9gYAitc4P9KdwkGbrrvCHYqrFBpWwCGw1SwBvta9tuWmI668K4V2l5Gc4JDDBr6Ouxq4x7F99QhWdtQ-aqcuqX2kZcURllJsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af9189453b.mp4?token=gRWY6Z_K1ddPuR6GcxcOsbeinuWmoaWkOAzmujK1IRtlxVsooGky4kIgAQDSMHwrrhFM3JAWitHF8hwjdpjz_1SMnEJflyC7z5MpctvbjO4r35ZoBLrdHlDECnHmg30r665U4ZjdNMGxYrZva9rkYRssMJ0gYyt2r0-eY7XltVDGII8DrYiJ-wI1tBeLY7EBb6N69Q1HBcfBIvxePZU-46dTzO5ByMY-sRPpXd5vMjfBhTX8miPKQ9gYAitc4P9KdwkGbrrvCHYqrFBpWwCGw1SwBvta9tuWmI668K4V2l5Gc4JDDBr6Ouxq4x7F99QhWdtQ-aqcuqX2kZcURllJsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما یک کانال ارتباطی مخفی با سپاه پاسداران داریم
🔴
ما مستقیماً با مقامات سپاه پاسداران در ایران در ارتباط هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/142225" target="_blank">📅 14:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142224">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ: ایران باید پرچم سفید تسلیم را بالا ببرد
🔴
آنها در بازی پوکر خوب هستند، اما در حال نابودی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/142224" target="_blank">📅 14:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142223">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95373bc7de.mp4?token=MKZ1NF4prJhJESCfVzgY8mEEcVq4LFJImLqZ1vFNoPpJW86z31F8pVxcywD8EyfMVD6vlQCCxvnct4hLC9b3gAC-k5JqULOxpOvNOLo3cq1_YBjCqYL8Hok09rdo_XxYzpwB5v3_NEBPsCgoO0ZTT0qrEuUcX99fgvZdbTf8eX-bZ8gKHGEF882kmmPHUpwKYcDNy3HVBUb-ed66dSen3MbYEaBt_bikvsT0hBGgjZ8XOc7j7N9zj94CbkpcOWh_WIoFd8B-mhqVzCvb_p3R4erkqcS5dBqn-LTX_L8xRgJ8av_hwwF5KaSbHbfE-w51ZBPrNzMd5Gh6r28U2pEh5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95373bc7de.mp4?token=MKZ1NF4prJhJESCfVzgY8mEEcVq4LFJImLqZ1vFNoPpJW86z31F8pVxcywD8EyfMVD6vlQCCxvnct4hLC9b3gAC-k5JqULOxpOvNOLo3cq1_YBjCqYL8Hok09rdo_XxYzpwB5v3_NEBPsCgoO0ZTT0qrEuUcX99fgvZdbTf8eX-bZ8gKHGEF882kmmPHUpwKYcDNy3HVBUb-ed66dSen3MbYEaBt_bikvsT0hBGgjZ8XOc7j7N9zj94CbkpcOWh_WIoFd8B-mhqVzCvb_p3R4erkqcS5dBqn-LTX_L8xRgJ8av_hwwF5KaSbHbfE-w51ZBPrNzMd5Gh6r28U2pEh5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: آنچه تاکنون از آن (مهمات) استفاده کرده‌ایم، در مقایسه با کل ظرفیت، بسیار ناچیز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/142223" target="_blank">📅 14:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142222">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فوری / ترامپ: اگر عمان سر راه ما قرار بگیرد، آن‌ها را حسابی بمباران خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/142222" target="_blank">📅 14:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142221">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
الحدث» به نقل از منابع آگاه: گزارش‌هایی درباره موافقت با تمدید مهلت ۶۰ روزه آتش‌بس میان ایران و آمریکا وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/142221" target="_blank">📅 14:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142220">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abT_h91lcY9v7c4gzY48Lxyn8ORn9iNkLT1Yi_thkcWjPPNr693LO6MoQX87uhk0bRnFQ4nRRWlshdW1NcBGIiM0MiKp44g2m0Pw1ubF6qzhhT8ThdAAH8OUW4owXaqpQv3tUBym1IkgXIcsS7UFAbvON9P06_LiKALhB929EmOBm6L_8w7JmreP39nE9c6cGo3PdZexNzbtWWe6q5upCI6SJ0wg9v5mubrHXaUW9xNK7lwN2trY8qZjzRID_AhU4M0_s-VFoyxa92GAtOTzuWrnaOAZXct2FSJtydMZD6k-7jSr68j4dn2ljsR4WZygTYZ8iET1fUe9twaYs_32lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دبیرکل انجمن کشتیرانی و خدمات وابسته به ایران: منشا آلودگی نفتی سواحل جزیره قشم برای ما مشخص نیست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/142220" target="_blank">📅 14:36 · 26 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
