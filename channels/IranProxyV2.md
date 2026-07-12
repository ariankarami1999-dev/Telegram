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
<img src="https://cdn4.telesco.pe/file/Oobok2Jr9jk0fkdzO_6NxJieFxFwCSQ0-zFw-m9SDCs9FDt-ErQcajtBhl0mdNg2uhb_ImZWej4aZ3vrGj8b0jBES8h7ZQegoMP3FKOA0wFEMatWH2GOtdbouGsslMxfIS5FCktyxmmXa_uJMWDuWwX_rBrVe7TDTGSkdB3xSzmp_BZFu_zLw8mHztmDD7HLCcXZVBf_XaBuBd_cJqFSOQ63CbJtwT54e7X_B8bi7h6FrSKIT9SYXCylEpwuNxy941fXEq2egQ7IiYq5OjNLXUujEBRz8Rlc31aeOOn7RmQP-9NP9q_1btgr1tf2HNnA8dGtm7XK7eOkpdtyijq-rA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی</h1>
<p>@IranProxyV2 • 👥 1.38K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 21:22:18</div>
<hr>

<div class="tg-post" id="msg-58">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کیفیتم خیلی خوب بود اما امتحانش نکردی...
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 39 · <a href="https://t.me/IranProxyV2/58" target="_blank">📅 18:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-57">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">+ خوبی؟
- آره بابا، یه چایی بخورم اوکی میشم.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 65 · <a href="https://t.me/IranProxyV2/57" target="_blank">📅 17:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-56">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">واقعا قدیما بدون گوشی چیکار میکردید ؟!
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 94 · <a href="https://t.me/IranProxyV2/56" target="_blank">📅 15:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-55">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WB6S5YmatJSz3xnNTw2V-JzvhZSS5uHujITkwZw8QLRTEqGo75sgH2hnnn3oO8oiSASphpewMk8cMRsdGJB-Fm4KHjRDPFfO32f9zcahvDD4vb2Nbf_mICh8TplLiJO9nOxKsXnM03UU-4ENSwfJpQen7uOXNXsQzOxaKcaYJfae_cgLjrkrirN6aDmqEY02ASrnnWeRx7lddG-82qkqGqdREI-LT7PNZeNTr_SiWvrL4yb6wYI_W3GYOS8o3zM1F7Xi213v-ODQacOE8TUpsFjh4Uspw_-quYUrxpxrfFrj8UxjhEEVSNsZO7ev3h3SlceaCQaMl2yDdUuIJ_D8Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداقت اگه عکس بود :
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 153 · <a href="https://t.me/IranProxyV2/55" target="_blank">📅 14:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-54">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔹
لیندزی گراهام، سناتور جمهوری‌خواه آمریکا، درگذشت.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 125 · <a href="https://t.me/IranProxyV2/54" target="_blank">📅 12:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-53">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isIhg825NIxu13msKlmHqlmYDEZoBVIA1KfYrHPlvzVW-A44QEksEBwI8xzYx09auReE1-auEJfAxHxc2_Un4xGhEYiwVsEyP-N7WPnE7uG7PDpdZS_aJzzHKnkZUeWEd59eSCOXPfON0q4ea7zEzJ_52rNo-CoO_f1oqI8tliqELGjlPaLby71QBNPbHOldoAFyTBcYyf15rZxcX_pWXrfmiCUuaOQ6_fXhzmDNl8vUa4VvQTe1bFag4-DNHPuJofcGLsh-y44EYH58Ie7UC630Oy4CfzRvWi3C4czKU886V_sdQh4PmwLakWX9t-PDx63kgWwdyppeHiaU7uBzmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شخصی که قرار بود انگلیس رو از جام حذف کنه:
پروکسی‌
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 154 · <a href="https://t.me/IranProxyV2/53" target="_blank">📅 11:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-52">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">امیدوارم امروز مثل روزای دیگه تکراری نباشه
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 146 · <a href="https://t.me/IranProxyV2/52" target="_blank">📅 08:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-51">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">۲۰ دقیقه ای که بین دو تا پارت درس خوندن چرت می‌زنی، بهترین ۲ ساعت دنیاست. اون ۴ ساعت رو از خودت دریغ نکن.
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 164 · <a href="https://t.me/IranProxyV2/51" target="_blank">📅 22:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-50">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYkoryx8kZRqvMT3cSqWYs0QWw13KM3DfzLdwoFT98ZixQwCXhKYfRGFyDPg7aDZ3o04wwuAeFi8Hx6XAjQzGRXbVqEonKUATuSj-7VPMluH3B_QMakCd1Bo7P1Xb6lo37N2ZNH1SEZ6YWIgXpxnQFdxMOboamOITGBc7OnRYEuf25imzigGdySeMeDRTzE0Az4vpjnH2wA-Qgj9wlR8WUWQWRjdmh72tgPpTLuI9DMtuO6XyFk6C8zJt26WOhl1tdDsqkZONufHTxc5SGR77cgjzZiiUjECGqS3oETnC3pBWPnJhPeelDe7_P5uqm_Hcks9LqmbDuu8CK7vHRIPhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه شترها وقتی میشینن، پاهاشون شبیه چرخ میشه.
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 166 · <a href="https://t.me/IranProxyV2/50" target="_blank">📅 21:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-49">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-hOyTg5UgyNlvKivTfMSDoBXIiLqAaIu5ALsa9CuB7Ua2oLMWxUIXOcv7uyUPCOdcwnWChrP7lNurlzSQlUDMtQjEKCriviqn_ssZb-1yZKf24fHqJyWfDrQhhbdd13hYcMQvJky379hhUrb4O9XQ6-ePVMXH5i4lhnWwpD4Hni0HIsZ2l9g0BCS1ZghMSbN60YXO24r2ijCjKpVA9rL07IVMEt_HQlaNieQMS4derZIUy2ORQm5LxNI-vCX70691_sse8JgkbC93cdqQ870Zz4X7chfUOTfOlDgqpBgIEqOiq0bzImehXO3BaZ2RCMt6ntuIRp1Qd0piFg-WkJQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی وسط درس نخوندنام به خودم
استراحت میدم :
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 147 · <a href="https://t.me/IranProxyV2/49" target="_blank">📅 20:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-48">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ipc8cIkUFK_EmY_-eeqKPxalRf72qi9pFZBHOo5MYH7vMS6L2e0j923Us4iMOVEyZtaotX5gqCXQ6DZjUDJS5JXnbtr6V8dfefj5hbjhjAi3iOG9Pmffc6oA1NNTbDy4369bjSdIlq15O_gbF6KfZG6fottx6erN0zHeYHSgXkfWJEg7FEAbK3TOUjbfWG8-mid-mwnqn8IOZtjD1rRfG-KC5nFLxRo0dJidSopTzLdwtsdxzVD_5dnqsXqmakhhcRNeEZCtGf6VpoMCv1FYdE_e-AfljBUFCwd1zTRJ1rG44MoSd_PtzJAISSu9ACoGeQdAGwKXUFKl16azB6wB8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلم واسه حس گناه بعد از با دست هُل دادن تو
تنگ شده :))
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 161 · <a href="https://t.me/IranProxyV2/48" target="_blank">📅 18:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-47">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bx_V7gWVqM_pxBSEmE_AwYIigTT1zKTjN-0T9LXSMUGR3O50vEd7YMOz_HEH2NDm_KFfAF-QEHnXth5fYd-BsxcZ_jCD_66eZAkA1BvF3GTILW3G6a6NXX-A5UbBI73PWEa9BNEY0mdWLMrxOkTw6QL5gQTFxQUmjfSTVG5hqDz1pAyIqsdUsOxK3jYyO0AzKk8z-DKkga6SBVdEbhmZJT4ZNRvnrrboRJNKOM3QaAYQZum8A50XeJD-nVL_-IgI6NjqGgsmBfcO9O-EN-dvjKSfGMuhWrAnBBtmxwqXcinPnVbXGlo_-5ftIvFFOACb43X6-ggvSQiabBQZwbvQ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♾
اتصال مطمئن، تجربه‌ای روان با Lost vpn
اگر به‌دنبال یک سرویس باکیفیت برای استفاده روزمره هستی، اینجا جای درستی است.
📣
ویژگی‌های سرویس:
🔗
اتصال پایدار
🌎
سرورهای بروز
📶
سازگار با اپراتورها و دستگاه‌های مختلف
🖱
مناسب برای وب‌گردی، استریم و استفاده روزمره
🔴
تمدید آسان
💬
پشتیبانی پاسخگو
@LOST_VPNBOT
@LOST_VPNBOT</div>
<div class="tg-footer">👁️ 173 · <a href="https://t.me/IranProxyV2/47" target="_blank">📅 17:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-46">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نمیفهمم واقعا چجوری غذای دریایی میخورید خود باب اسفنجی زیر آب همبرگر میخورد
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 186 · <a href="https://t.me/IranProxyV2/46" target="_blank">📅 16:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-45">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">امروز گرم‌ترین روز تابستون امساله این پست رو تا پایان تابستون میتونی هر روز بخونی.
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 207 · <a href="https://t.me/IranProxyV2/45" target="_blank">📅 15:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-44">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
زیرنویس شبکه خبر ساعت ۱۲:۵۱ امروز ظهر :
با اعلام وزارت آموزش و پرورش، امتحانات نهایی از فردا و بر اساس برنامه اعلام شده، آغاز میشه
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 264 · <a href="https://t.me/IranProxyV2/44" target="_blank">📅 14:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-43">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
طبق تحقیقات جدید، کسایی که دل خانمارو میشکونن، زودتر کچل میشن
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 308 · <a href="https://t.me/IranProxyV2/43" target="_blank">📅 12:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-42">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">يك بار برای همیشه غرورم را برای يك نفر کنار گذاشتم او هم نشان داد چرا نباید هرگز این کار را میکردم
پروکسی
پروکسی
پروکسی
پروکسی</div>
<div class="tg-footer">👁️ 337 · <a href="https://t.me/IranProxyV2/42" target="_blank">📅 11:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-41">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بنظرم هیچ حسی قشنگ تر از اینکه مطمئن باشی یکی دوستت داره و برات تلاش میکنه...
پروکسی
پروکسی
پروکسی</div>
<div class="tg-footer">👁️ 367 · <a href="https://t.me/IranProxyV2/41" target="_blank">📅 10:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-38">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">Channel name was changed to «
پروکسی
»</div>
<div class="tg-footer"><a href="https://t.me/IranProxyV2/38" target="_blank">📅 11:10 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-1">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">Channel created</div>
<div class="tg-footer"><a href="https://t.me/IranProxyV2/1" target="_blank">📅 03:18 · 06 Ordibehesht 1404</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
