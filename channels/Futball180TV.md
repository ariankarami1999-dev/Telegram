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
<img src="https://cdn5.telesco.pe/file/C4yyA_OGXzxTMD1TbEaZwocKFwSyDm-JML8txVZlMWwPQx41CX0TvJCWT1QAafIgJWrG-bUTKgRTaPFat7Ulkam3wnCWNuOC3CuSivyRS85_AqxCmWZ5XTXNsmNk2zhxnhGa4cf7LRRkNPSt7mAmodJQfhouFU6o0d9QTbW8xGJyPKrz6FPykaVfzb5-U2wPWWml-xTfwquAun_X4CtsrDguOmtf58u18XzULFi9WTEMDjZSQx_6ehwLLSwy5yfU4iWw0NW2KOi0Nvt05bItTFxSZK4PU-_-x9a8Dqghx_McmOQ_ts4QHQNOsNipWxlaG62xpdI3aPBRWM32AJBbnA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 451K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-31 06:42:39</div>
<hr>

<div class="tg-post" id="msg-104341">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fb4qOLl0Z2pc08g0_JjGp2nnB5-cFWsm7rOvY_Z7jQCXBKqEEIPem2CZI3lHAo90ZF7jSjFx8WMn0wQNM-mDs6AzNuLjfc3GdAcK2XAQc4gKQm6TQ2ZnTtJDf6MyC-QgJAYGrZru4i0aLnAEzGaro_GMFfLCj3n-G2VpdUzHTehNTuTUtgrJzmslRjbk935kPHsnlJalv2EOuvh0I9VylWB_fb-7XCRNOR1pLdH_waA590p1IRPYVmoQy1EKzF7Zk9QgpGJATtLPSyntBTCf8TC4jKs39thzFIScMtTGk7elpQrsEcpPvU7yS1MKxXO1XR7h0GQ1U58ZDbIukjNI0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
🇪🇸
استوری هیدالگو، مدیر برنامه آلوارز  «هرگز از یک دروغگو نپرسید که چرا دروغ گفته است چون برای این‌که دلیلش را توضیح دهد، مجبور است دوباره دروغ بگوید.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/Futball180TV/104341" target="_blank">📅 02:53 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104340">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
🇪🇸
استوری هیدالگو، مدیر برنامه آلوارز  «هرگز از یک دروغگو نپرسید که چرا دروغ گفته است چون برای این‌که دلیلش را توضیح دهد، مجبور است دوباره دروغ بگوید.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/104340" target="_blank">📅 01:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104339">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tE8QQP1R3FyjsrmktKuICsEh6F2-CyJPhGkd7O49l7sLv66V_bREm7X9DMg7JBniYjyD7MK91Pc0P3eRdfdUpXmUgK_5PdezkfaM_Vvh09NzJqnRJFiCD5TWakMvEEwy2zi4Qk_SAgFzlSUgfqO3CWAcTOW1rYCCop8XAz1nhISjsIlox1MeqP8N3jkzUVEEwVcDoWZER4-J2oQJgg9_BmVDQxAS_kpVrQYT0OO4-LHsJ341pGx03F-pG0C3ErH42RCtjnxS_JMrWX-IkhYNtPkRrUkTcBhetUrAq7Y39e7SE1WyLo6VUsf6nGtYcdyvVdF0-E6uZsWkz8ECUlqqGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
🇪🇸
استوری هیدالگو، مدیر برنامه آلوارز
«هرگز از یک دروغگو نپرسید که چرا دروغ گفته است چون برای این‌که دلیلش را توضیح دهد، مجبور است دوباره دروغ بگوید.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/104339" target="_blank">📅 01:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104338">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZwuwrzQvDuF1YqaJH-UmUN8z8wAbejOe33OpWMYx4hC3g2sSfW7jEj7V0AmOC1IlB0By0lGtsm8UpLdoWHdV5yYFe0SNTUIgCTBVF2ppYaUwaP2ziNoG8o9V_WhrLUsJE48OwPjXtOGmgIx3Vl3eocwPhIgO41bWSxTiZplQfPDMMxEcvAA4LnDmppflKDGLYPcheEL1YVu8NjuqjDFBfIwYo4A-VR1yagUf2aQfYGm_8R5laXkwE-rsbbSz_S2mRiBGdjajm4HjC8cTaDV4WT3Gq0pTENeZyJuand2AjPwjMYGKIkg7yoSJfJC_cDVlqA1tAVohM4V2pRx4Laoeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
پس از پیروزی آرسنال مقابل کاونتری سیتی، میکل آرتتا به پیروزی شماره [150] خود به عنوان مربی توپچی‌ها در [249] مسابقه در لیگ برتر دست یافت.
🔥
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/104338" target="_blank">📅 00:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104337">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!  ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/104337" target="_blank">📅 00:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104336">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=KVi-Zojk-8apO_EN_q-qVcPk0Fj3OwRGMYecFdtezJ_IwUYv30d0nU1XdMX5xutQmGnLzq7etZdl7s0JV_YnW61QLLSlLLz7JsIPdp58JeRMaeZLVfXmqplr-TLUP_mJgVP3jVaqKeeDOLtFYW9oinyLp7fA5iYJpy1MZ1jIWm8PWf5Xk_PbEfqd5Acv_SyKvbYC21tzlzokMipZ5NcwPCC0mMZrxnL9GktqOKmcINrBTwOaqXtlDRqyJq2gDnJ14AkffxiXkks7LOSYq24rWir4gYNaajUtlJA5e1FF5n6NQa0HX9gqsVdsklcs_wvSTEIXg66DhrGRfZexOWjnJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=KVi-Zojk-8apO_EN_q-qVcPk0Fj3OwRGMYecFdtezJ_IwUYv30d0nU1XdMX5xutQmGnLzq7etZdl7s0JV_YnW61QLLSlLLz7JsIPdp58JeRMaeZLVfXmqplr-TLUP_mJgVP3jVaqKeeDOLtFYW9oinyLp7fA5iYJpy1MZ1jIWm8PWf5Xk_PbEfqd5Acv_SyKvbYC21tzlzokMipZ5NcwPCC0mMZrxnL9GktqOKmcINrBTwOaqXtlDRqyJq2gDnJ14AkffxiXkks7LOSYq24rWir4gYNaajUtlJA5e1FF5n6NQa0HX9gqsVdsklcs_wvSTEIXg66DhrGRfZexOWjnJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!
ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی تخصصی بازی‌های دوستانه باشگاهی و تورنمنت‌های معتبر
➕
فرم‌های گلزنی (بله/خیر) و گل بالا/پایین با تحلیل آماری
اگر می‌خوای از روز اول چالش همراه ما باشی، همین الان وارد شو:
🔗
https://t.me/+UfR2NG4GjAMwNTQ0</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/104336" target="_blank">📅 00:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104335">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e4cd1601ff.mp4?token=HbHZQyhRMpuW5bhgZ2ca6DPZrbjUDJyfHrgHm8Iw2iH0XAetWrYkOEP1wocBSYpRnJAHLOKbo4Mc6PWGWRAzvLGxJ4KuM36CA77_nubcgGfzGgq39mpS9u_EyMjZFgJrNfIYTwpJKczaSZ9_cmvvo9H9vY7bISU-8JJlHEj1YTzqphvaiOaf9XJbZj_b-RRlvDbFcObiR3uC-U3TssYXHL6bF0huDAhPT2HasVz3eBUQZuqwE3_PzRPaM2X7QnHCVn5A6_DqKCYb7LlW8L67VQn1yEPAT7nNFPusDt4EQ6XgYuiA83zH8QlHHwYYTAvh89_PY3Od4nQk7InOGEc3BJ-3RlWm8xCie134OHjc0bEFKsncQ0ZXXDWj3UXJrx593x0a-lrGy8snUvrDbQ4BkXq0wumOiO0MHNHod3N-kI7652RVTlNBN1pqLQXi38TeAJH8d8HBxQBIwGoXD4xCZ6degy0K62BLx4_OgGLYlqYl7lehhzSZSYYSNouVgX2saYS5zxt7PXLNnPGjNpRIXtfifFzU7l-nneFHKL3y1pmvgYrgToy8mPzo3NGOaqXOWsrb5uKw9C4A8t7PpZZar9LPsM7XIqPWYXSo6u06CsAhQj_YLGeLq2EVMAro-zj_viv9PJwWg7X5tMzjEPcK7nY2_wUM60DNK4dfk6gsjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e4cd1601ff.mp4?token=HbHZQyhRMpuW5bhgZ2ca6DPZrbjUDJyfHrgHm8Iw2iH0XAetWrYkOEP1wocBSYpRnJAHLOKbo4Mc6PWGWRAzvLGxJ4KuM36CA77_nubcgGfzGgq39mpS9u_EyMjZFgJrNfIYTwpJKczaSZ9_cmvvo9H9vY7bISU-8JJlHEj1YTzqphvaiOaf9XJbZj_b-RRlvDbFcObiR3uC-U3TssYXHL6bF0huDAhPT2HasVz3eBUQZuqwE3_PzRPaM2X7QnHCVn5A6_DqKCYb7LlW8L67VQn1yEPAT7nNFPusDt4EQ6XgYuiA83zH8QlHHwYYTAvh89_PY3Od4nQk7InOGEc3BJ-3RlWm8xCie134OHjc0bEFKsncQ0ZXXDWj3UXJrx593x0a-lrGy8snUvrDbQ4BkXq0wumOiO0MHNHod3N-kI7652RVTlNBN1pqLQXi38TeAJH8d8HBxQBIwGoXD4xCZ6degy0K62BLx4_OgGLYlqYl7lehhzSZSYYSNouVgX2saYS5zxt7PXLNnPGjNpRIXtfifFzU7l-nneFHKL3y1pmvgYrgToy8mPzo3NGOaqXOWsrb5uKw9C4A8t7PpZZar9LPsM7XIqPWYXSo6u06CsAhQj_YLGeLq2EVMAro-zj_viv9PJwWg7X5tMzjEPcK7nY2_wUM60DNK4dfk6gsjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌سوم آرسنال توسط اودگارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/104335" target="_blank">📅 23:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104334">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ecf24c9409.mp4?token=A1PaCy21dWDV_wTc81bKQfdFcj4qZr6fPdUI7B_NCEZfXkeKhkbSKzludvqM2IsugG7ItIlAf90dLNRZU3wb37gyiQdLQKhTRrNyyYLO55FO1DbEaabLBdiFSIzOIlCFrWeXfN04fmXVXhPlrBF1XemaE9JyLJSa73TkjGDX2Zsw1DRwjq0nglbzMT6KZTzt7Pu9Y-VWzYWO1YglNbaHzMGfwgfSNTSTWw5rUUo2zbb_6wfJSfZyeGHwQ7VVFlAtMXddFM2nG5c9uJEUyWKnvvkEOTwySUNs7t9OW3jb6ZsMiW64s7h1p6GCUznukEpWdqSdxMKy9IC1MnMUC_CSWLBSKsXimAlUjUVcKu1Foyy_oEBNfQb6BX7vgx3Ddy3drSK_Mc1VaSkoEF-gfJnXI3nJL8w903EQFdM5ZHBDGSmFMOEZZl0dnMUMs8ahiIiTfeKguQkbDJ5rj-jGzUTy5xXQZzequvkFMt5JiDm2Dil65Ng5LCD2n_wgHjljc5SVgEQ_Iw2twqeBceTI3z4G5rbNp4HhSZpsJw0Qn-c3jtB7wDHI_UrtzEAP7VzBeupdNT26NOqVsRgKXl1VS-qYmdMKoeYQ2GaonlIvGAIcikA2wZXPqLVpCuosHuggD1yEOd9EBTvZ8QeZfk57S8MMJPOQBo28zouiNN3QK2nmycU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ecf24c9409.mp4?token=A1PaCy21dWDV_wTc81bKQfdFcj4qZr6fPdUI7B_NCEZfXkeKhkbSKzludvqM2IsugG7ItIlAf90dLNRZU3wb37gyiQdLQKhTRrNyyYLO55FO1DbEaabLBdiFSIzOIlCFrWeXfN04fmXVXhPlrBF1XemaE9JyLJSa73TkjGDX2Zsw1DRwjq0nglbzMT6KZTzt7Pu9Y-VWzYWO1YglNbaHzMGfwgfSNTSTWw5rUUo2zbb_6wfJSfZyeGHwQ7VVFlAtMXddFM2nG5c9uJEUyWKnvvkEOTwySUNs7t9OW3jb6ZsMiW64s7h1p6GCUznukEpWdqSdxMKy9IC1MnMUC_CSWLBSKsXimAlUjUVcKu1Foyy_oEBNfQb6BX7vgx3Ddy3drSK_Mc1VaSkoEF-gfJnXI3nJL8w903EQFdM5ZHBDGSmFMOEZZl0dnMUMs8ahiIiTfeKguQkbDJ5rj-jGzUTy5xXQZzequvkFMt5JiDm2Dil65Ng5LCD2n_wgHjljc5SVgEQ_Iw2twqeBceTI3z4G5rbNp4HhSZpsJw0Qn-c3jtB7wDHI_UrtzEAP7VzBeupdNT26NOqVsRgKXl1VS-qYmdMKoeYQ2GaonlIvGAIcikA2wZXPqLVpCuosHuggD1yEOd9EBTvZ8QeZfk57S8MMJPOQBo28zouiNN3QK2nmycU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم آرسنال توسط بوکایو ساکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/104334" target="_blank">📅 23:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104333">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/889cf6b1f7.mp4?token=jBi3B7bJqjjPEfoFx9xQrog0uUGKV_9szuOnxwdNMExzPgbnC9Dp-6dLLZ_qJARpELvIfejIzpCQRKP12IBftDn1H3OINfHzeyki0DR_hTEloExPWfyrY4zFduBx7Ikpzkt08uXdpH_1bL_JpNDCfwZFVbXbeyL1G_3leFwZK3Oww_t5QqECebwh-xJbIM3FwIdwUFGMYZCTdMbq_wso1mfE1r6LR12ZIXOL61dbw5xksHzZlWpWRcnu2GVR10Dz1_y1cKr4OARRQbmv1RBBwUM8epH6h_x1hyd4qjpYVWzu7SDruBWwPqh4UIaiUezB6itQJP3-FmPPvmdsl8EaZmfzkN0q6Q3BTiQIWyCeEE6MRCAhLNQx4zo7aGZ0ZTTd8grxLSbTiN9bQEuKLK1WbrUdr0HGOusKOsqsshwCcVTVGya17LhtSPVNBDqt8_TQ5N-G9AmnljjBc-xUJ4Qw7Gt0Cx-Lk0f2Wz8FTDQFYbwpDpOqVFmfyPy_FpiURIhP2FqedXJ2Rlz4PyRXdAoaVLzprK2UVD72GyLc0WrjjxtDqcjJAo6mCnLLhcF9ZbUfwUuXh-Spzh2-VfWUZhWGDUBUxFEZsUXAzhSrkadV4UIN5t5LszNBWDByx_pKLr98jKQ1gRwJhgm5R6Umgfk2hX8QAmo04HnGjYPGodtyLT4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/889cf6b1f7.mp4?token=jBi3B7bJqjjPEfoFx9xQrog0uUGKV_9szuOnxwdNMExzPgbnC9Dp-6dLLZ_qJARpELvIfejIzpCQRKP12IBftDn1H3OINfHzeyki0DR_hTEloExPWfyrY4zFduBx7Ikpzkt08uXdpH_1bL_JpNDCfwZFVbXbeyL1G_3leFwZK3Oww_t5QqECebwh-xJbIM3FwIdwUFGMYZCTdMbq_wso1mfE1r6LR12ZIXOL61dbw5xksHzZlWpWRcnu2GVR10Dz1_y1cKr4OARRQbmv1RBBwUM8epH6h_x1hyd4qjpYVWzu7SDruBWwPqh4UIaiUezB6itQJP3-FmPPvmdsl8EaZmfzkN0q6Q3BTiQIWyCeEE6MRCAhLNQx4zo7aGZ0ZTTd8grxLSbTiN9bQEuKLK1WbrUdr0HGOusKOsqsshwCcVTVGya17LhtSPVNBDqt8_TQ5N-G9AmnljjBc-xUJ4Qw7Gt0Cx-Lk0f2Wz8FTDQFYbwpDpOqVFmfyPy_FpiURIhP2FqedXJ2Rlz4PyRXdAoaVLzprK2UVD72GyLc0WrjjxtDqcjJAo6mCnLLhcF9ZbUfwUuXh-Spzh2-VfWUZhWGDUBUxFEZsUXAzhSrkadV4UIN5t5LszNBWDByx_pKLr98jKQ1gRwJhgm5R6Umgfk2hX8QAmo04HnGjYPGodtyLT4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول آرسنال توسط کای‌هاورتز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/104333" target="_blank">📅 22:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104332">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو و متئو مورتو:
🇮🇹
برای مالکان و همه افراد حاضر در اینتر، لائوتارو مارتینز فقط کاپیتان نیست؛ او نماد باشگاه است.
❌
هر پیشنهادی که ممکن است برسد، بررسی نخواهد شد. موضع مالکان کاملاً قاطع است.
✔️
با ایجنت او تماس گرفته شده است؛ با این حال، تاکنون هیچ تماسی بین بارسلونا و اینتر وجود نداشته است.
🚫
اینتر قاطعانه ایستاده و پیام‌های بسیار واضح و مستقیمی ارسال می‌کند مبنی بر اینکه لائوتارو غیرقابل فروش است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/104332" target="_blank">📅 22:39 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104331">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPYRR1XffU4KhE-aRSxs-K5jbqEHdGIFpAY_U52lG37q8zvR5PsH92BkW4CSxkntsib3Bjefkb8L3J0Fylp2lIJNCUkwJN0idCGQqBQ7SGmRuXpwdZSNQUhV_QNQ-LNZ9SW8WD_xR_tX7OHC-qspXqO64MsUB9S0qyoWN5k1JCB3mnl-7DlRDAQl3AmuZTYPYObtwi7Pkp7YlDvlIaRb900ziyb8nbZRh3YcHom6l9fuCwqTA2Lg223kXupK-i_ZglNY45_LEId4Cq91iMSfRRpHxNkv8LKyVa5mqfsyQB651BtXoasSYDK0XYwykyqhkmXS3rtp6K1tKfD9EBpy-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🔵
#رسمیییییی
؛ مالکوم از الهلال جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/104331" target="_blank">📅 22:09 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104330">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsWr_rQPDmX6Fa-Q16zPEatbkzf2fQ9o2TzA-qO_F8RMhorU3AasnQOG8_6vAkHdAVPTij2ix6zB8vV6inbkZ2GnyflX5N7P1KqHe3bY7cclk2v7QcUTCkXIUmCN1M6-l0Av7-5gYK1LSCnFhmuC0dnhEHp6v7z9bJL3IFVw3UH-8YgImkiY0ym_GOBi4eWxIRQWfh5MgySOZynJJhCqu-UqTr5ny10cp8an5dpKN19IQXbbWPsaEuo6WYYNdiQN4Y43GQEcB9gLcwiJc7JJJi8IM_Am9sWJ_pQzIPztT-P89u5R22gqFHgM1eynDyZsCDQMGn7DGmFI6M6NEgNUnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووری
از متئو مورتو: بارسلونا از انتقال خولیان آلوارز دست کشیده و این بازیکن رسما از برنامه‌های فلیک خارج شده
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/104330" target="_blank">📅 22:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104329">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f670f0bd57.mp4?token=ADzc6T2pqefEuYjzYD3-o0w69dl_o-swUN8P0wyxqTwLH_-QdORoeP--LjT3qosVbTC4If_P-8xoqxkooWpz5GtsT1CrXMIn6RFKLJN01Kuc0LRRGlrgwnGBavbb3eW9fg81tNsiia-IKltLtPIYsnq7IFpwhegeME2nXsdL12FDGyQcX64nYDyb9UG1eom0Cl607kpR7aZ_42EUmXjQrCRxlCK9NXWCApABA7x5uz5PEgHimyd6hCrZX3gYpVfOy2zeGtQR_Az4yG_PHhw1kOkUpsuTfqTnRydpsUnL8DfRJAd9n2HVr21fWddbv4barDvT8sbzAv9CeaezZOVdyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f670f0bd57.mp4?token=ADzc6T2pqefEuYjzYD3-o0w69dl_o-swUN8P0wyxqTwLH_-QdORoeP--LjT3qosVbTC4If_P-8xoqxkooWpz5GtsT1CrXMIn6RFKLJN01Kuc0LRRGlrgwnGBavbb3eW9fg81tNsiia-IKltLtPIYsnq7IFpwhegeME2nXsdL12FDGyQcX64nYDyb9UG1eom0Cl607kpR7aZ_42EUmXjQrCRxlCK9NXWCApABA7x5uz5PEgHimyd6hCrZX3gYpVfOy2zeGtQR_Az4yG_PHhw1kOkUpsuTfqTnRydpsUnL8DfRJAd9n2HVr21fWddbv4barDvT8sbzAv9CeaezZOVdyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
حس و‌ حال مردم وقتی مسئولین درباره افزایش قیمت بنزین صحبت میکنن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/104329" target="_blank">📅 22:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104328">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKOe0HiO3DxP5e7HLuQbHa1p3Hj192rlnNlySOTjxa9zq_-DLgaB6FjnA86-eVtFQm4mhcWRW1DccecB4_RodQp31fxXLav0ODpKoHnriSR7JHwPn30YV907cVhkvV7hXFCint60yAlY-XyO1_jaOfDZLwg5LXBZD81gN9PhJOBOCzPHuGY_-AzlaNKs9I7dIGQjI9aNn7cVlgLyc_flXS4sv4ZN7upWqIQxeHwWDlITpMo9T4JlT8NkQTbsiwnmLR7nnMHrAfCrnhdjEA_1KKc3klDGFd1D8LWcUZ8Fe86zZ5baFUkw3pdTNNsfTA1LuK0qQDN9Zq-JsQvIsDM2Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
#رسمیییییی
؛ کورتیس جونز بازیکن لیورپول با عقد قراردادی راهی اینتر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/104328" target="_blank">📅 21:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104327">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtcMgm_riC2ATCEykw898VQj894armpHR54iO6-WRdVIKaNY6zb3PooeHxu9aQBTsHbGUwOh4V0PfHYVktwc0IIThiDfDnn1SXBHKZi8uqT9KCzU42R0dX9SGro4nEbiOLWtuHuKSW2AZxNcJNuDRHK2vrM4XYLB7zRjtTEtN08T9SPxDf76O0hPZ0vChgJFsOryJ6dAU96lrR6VY6lVZo2ARn9a3C0T4jmsYxmbSuGVvQVm1kyifw7WxErkOQE0kkieMOyXMgwj5Pyg-a_DR1A3emfVe952EJRnEfjqBc4HXjaPKqk8lHRpD9R5I4_-TvO0yTRmkW9omvdA-aKolg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گلزنی رونالدو در شب پیروزی 4-0 النصر مقابل الریاض
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/104327" target="_blank">📅 21:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104326">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91919c1481.mp4?token=NfJJhKykmS8UpzzxrkvVd4AK1g-76HMiWTgwsAtxdvK8bKBNOGv7H8ujJ1uHbaVlaR8KLzHu1yOFF2cCdbYS70NcocxlHQ7y8wPElF22kCGyYjYAEJK1CounSPXWFpKqZdJ-RwSWHs4fX3ZZM8yw-jDDD3j5x4w2qkF13BBxhp_t5cAznW7xX_0h-cSZdNo6zmER1Axa-IWBI8Lxqv1CxCtvrScDYcXDlGd9k40blDCnW9DiSPPZG24Kla1s75SJ-OhUoEUSCuowcmIepfTt1voou5B_ZMHQNXRAbHeIHn_QESK8CLBqkMqiujDLwDngKUP4xx5GFhxaXZUZygBTqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91919c1481.mp4?token=NfJJhKykmS8UpzzxrkvVd4AK1g-76HMiWTgwsAtxdvK8bKBNOGv7H8ujJ1uHbaVlaR8KLzHu1yOFF2cCdbYS70NcocxlHQ7y8wPElF22kCGyYjYAEJK1CounSPXWFpKqZdJ-RwSWHs4fX3ZZM8yw-jDDD3j5x4w2qkF13BBxhp_t5cAznW7xX_0h-cSZdNo6zmER1Axa-IWBI8Lxqv1CxCtvrScDYcXDlGd9k40blDCnW9DiSPPZG24Kla1s75SJ-OhUoEUSCuowcmIepfTt1voou5B_ZMHQNXRAbHeIHn_QESK8CLBqkMqiujDLwDngKUP4xx5GFhxaXZUZygBTqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گلزنی رونالدو در شب پیروزی 4-0 النصر مقابل الریاض
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/104326" target="_blank">📅 21:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104325">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e061ffb68.mp4?token=Ax9DnHnXnyBZFbb5RNTu5JlSgER7xmR2oWAvXELqOT7XO9nPJyh3kL-xiz0vqRM605imbgsR2iFxfaYKzQWVddWgzfwd5MWeU4rLhTU-eLnlUtH7BjUFwJEUQH6YG01Wq_VNp5jKVPsxpUG5AFF74Bh_RWulmSHhDRiflnbSPEOEKQHJ41zh5vNHH1nzE8k22fumnr5vm-SqMvNBHGqAVAodiUjrSwP_Ca-l8dfohzb0lNVABQqT3sPL8Xzb-QhBo2NwH96aezSy8-zHtKord7UMpd44YI3Y_9j7lB6__F9HPjTyQkCU7EtOZKqaYE2LIvQOQ426Qi-Thyf0Z3p6yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e061ffb68.mp4?token=Ax9DnHnXnyBZFbb5RNTu5JlSgER7xmR2oWAvXELqOT7XO9nPJyh3kL-xiz0vqRM605imbgsR2iFxfaYKzQWVddWgzfwd5MWeU4rLhTU-eLnlUtH7BjUFwJEUQH6YG01Wq_VNp5jKVPsxpUG5AFF74Bh_RWulmSHhDRiflnbSPEOEKQHJ41zh5vNHH1nzE8k22fumnr5vm-SqMvNBHGqAVAodiUjrSwP_Ca-l8dfohzb0lNVABQqT3sPL8Xzb-QhBo2NwH96aezSy8-zHtKord7UMpd44YI3Y_9j7lB6__F9HPjTyQkCU7EtOZKqaYE2LIvQOQ426Qi-Thyf0Z3p6yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
واکنش دیدنی و واکاشیزومایی گلر الریاض روی موقعیت تک به تک کریستیانو رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/104325" target="_blank">📅 21:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104324">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdplxfF9K5FO49cessI156WUJ2kN2U5Fmib-nDmDYj5ePYOn1u1FDXsmbFl_R9IMD2wakw2WqaBb-_gIaVHqM-wKAYcQFjXz_sA5E300JGWgKV3fKeBfnfO39vHWSKbTjrqk0-GAK2N0NzgYVNduWe-o6AuWjsmAFZgKrao3cnm6ajFPOUFPEe3Kc3Dep1JAmrt5tg5LQ8bCmHB3X7FePcMRE3IrCX61dhqHxZ-VXvrPP_lU1VOuVHhNlGjXgusZNyObEOjTG6rUcvEqi8erBK_9AdWltew1huIf7WyDwypx_Wo9UvsWVjKywHJBOzATaWXzs7PC4sV68MGvybquBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیبببب آرسنال مقابل کاونتری‌؛ ساعت ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/104324" target="_blank">📅 21:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104323">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9ah3wiv_eNQYzvh8G8aE3mVn7CbaFuJ1XZp6F9M3lPPp3nGOMWyR97pZZTj2CsXDovaD0bwOI3RFsq7BpUoNRDZlB44OulculkuCtkoBEAf2yyf1Zlq2MR3RUxqlzTbsKTBWi0j4GIXeRjVdr0LUKzlNvLWOtRfRT7zhvK9JRo4hGZNmzwDWIOpRx92V8N-qGgOUB--QYIuPHPmgP8BbvLyvo-r4QIPqoSY7EHSOuk4Rxa2g5AE1AKDyrQq3-3vIvqaqbp0jIVzQU2-a5WZBnutS84LSs9JeFzIU3KlhEMD454NRz4WZS-ChN3gRXTbTGazM7HnLvKwIsNzh6JUag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته اول لیگ انگلیس
🏴
آرسنال
🆚
کاونتری
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗓
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی در بتگرام
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/104323" target="_blank">📅 21:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104321">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5c212597e.mp4?token=HswiXbvaOWhSpFJQsgsd86MsZni1zjqg8gvo78l6nTvAxkWlY1zpIGDRs95HAWhH-MHzO2tCMvrqHbRC6Cv_Wa0Q3EaCYQZg2KcoOok58BsYoB2Ddach4EZ0Yw7d2VO6EO-JjXaz_i2gQhRFESVnH_aWEPkfA3X5v1V4wAI6poc9fD3w3AdfyyhPfqUrNrF31wydokWcea31KfIaaIharfeAzZiMCw2g3qQ-L34P1bIj8h798iRacXf0VDUhd0fXvm2WQjt194Y8Y62bdoMSqk3ADesOVuDTpxY6yJlkVvGK1QvyuoZ8q-qtECQEn_ZXK2tY3676A50CSt-NQoi5_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5c212597e.mp4?token=HswiXbvaOWhSpFJQsgsd86MsZni1zjqg8gvo78l6nTvAxkWlY1zpIGDRs95HAWhH-MHzO2tCMvrqHbRC6Cv_Wa0Q3EaCYQZg2KcoOok58BsYoB2Ddach4EZ0Yw7d2VO6EO-JjXaz_i2gQhRFESVnH_aWEPkfA3X5v1V4wAI6poc9fD3w3AdfyyhPfqUrNrF31wydokWcea31KfIaaIharfeAzZiMCw2g3qQ-L34P1bIj8h798iRacXf0VDUhd0fXvm2WQjt194Y8Y62bdoMSqk3ADesOVuDTpxY6yJlkVvGK1QvyuoZ8q-qtECQEn_ZXK2tY3676A50CSt-NQoi5_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
‼️
تاجرنیا با کنایه به پرسپولیس:
🔺
اگر استقلال قهرمان اعلام نشود از طریق فیفا و AFC اقدام می‌کنیم اما مثل دیگران با لابی های سیاسی پیگیری نمی‌کنیم، این تبعیض باید تمام شود، آفسایدی که قهرمانی را از استقلال گرفت از ذهن هواداران پاک نخواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104321" target="_blank">📅 21:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104320">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9ApoSs23lv32_q0bzZNxDyf_NAUpwhHRloK_9tyZPcUku5Zm1PJY76Bqh180U1cw_BBn4AOXeW7miiOBbNiz8MVM0ibk9qGs0486P_IPlrjcMWK3fe7zLhYiQuuNd-jqCBxOQn4B3ioyxNcOzUrnB0RdvALTBCKpSr8hPnB0343re_C1qX7P4zSPTe7aPy7LILtecqYu2tYoInI37Nvl9ww2wDRUAB164kB-MHRhT1N07u_bFdQpsv2ZkPDTc96Ekjh8BcBPaOnDVvSWq3cSDz2Ts65W5Kbufchpm5OBy5bE84qdlhAVmyv2GrQ1ZQKriQIiXUosYkSilz4Eh66QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
لائوتارو دل‌کامپو (El Ninee)، استریمر آرژانتینی و فرد نزدیک به اطرافیان خولیان آلوارز
:
🔻
اگه بارسلونا مجبور بشه منتظر بمونه تا اتلتیکو اول خولیان رو به آرسنال بفروشه و بعد سراغ خریدش بره، اتلتیکو هم باید فکرِ خرید بازیکن از بارسا رو برای همیشه از سرش بیرون کنه.
🔻
یادتون باشه یکی از جاذبه‌های بزرگ اتلتیکو برای بازیکن‌های سطح بالا، موندن تو اسپانیا و مدعی بودن تو همه جام‌هاست. اون‌ها با در افتادن و جنگیدن با بارسا، دارن پل‌هایی رو خراب می‌کنن که قبلاً باهاش امثال لوئیس سوارز یا داوید ویا رو جذب کرده بودن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104320" target="_blank">📅 21:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104319">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CuSch-oc2IHkMdK5naU4TFznQTJXdLDYsjFeLjmHa8ScDcxVAXbl1X_A5UftwV9tRSbZGbgEAxwlLsdyEFDB2MkdV-YPf7Ot4MWa8ZHztyM1ONmSNxjDvtZXspbGZCdA3Qpx91AhNn5HACdWyBjwSAJE9826wy0N--acjKw9DSeQW1HfbM9fYjGetRCcLFWHLBTlSpBrmLAOxiFTm3zBubBu0VAJSE00yTn_AgczO-eYi7NqpS_CvDvJfoFPq8x4THFR5Z0AtfUqtMQTxTjX2mIT23LxqrOIwaOc3YahxDCQf-JKWCjjLIfMXpxMh4PQS3gFAX4qq_6cMvCYGKN86Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از بن‌جیکوبز: باشگاه تاتنهام بزودی قرارداد خود با عمر مرموش ستاره سیتیزن‌ها را نهایی خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/104319" target="_blank">📅 20:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104318">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrJjujChkbq62RQETSPUGhhPXVeD7vhfaScjZ5s6KlqyXVsvzuTISQSc6o8GpbGPaq5pbkkdVNe_VNn_qmBJUveXC-U4hFzjD5kpGDaeQc7ck7-e92Foavg9Y9fD57f-SQvWUYXmqUGUr5lx8DFIQ50Wkwl3rua5cHbVn66ZrRuIgwTI8oglGz_e7VpJYXeQADpyqL8gceu7Kpy-zrBqDCu4Nr-EqV23P8tlr--T4OsiSjz9cttohSapZK9hcq4TM0HO3WeOeffzdk80rzA9kIynzTN2IDAh4kDT7TNTsDrZNLBOXaJABihWx74g3NrCJqGC4p1eAne36ZWL9cee0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از بازیکنان لیگ‌فوتبال بانوان پاراگوئه
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/104318" target="_blank">📅 20:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104317">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDIke9QNectM36JYED0P5rArpdjWLtx8sMYvuKdXhRnnfxwgKT393nhsgWrEEmeWgj8rAnf5a62TLGbTEkCUx94EXV7YJCneqy8PbSJHWJ1qMXc2HkNJPfI3vJP99poJz8XwadoXsDbJHWI8wzpuW52Z9nOEN7vWvi79Yu5lthR4BDfOyZa8MksMT3QrKW0ebgbpxGH49UVoj7MBri8bHCFiemKtMRK8OrxdSCS_I5sVLhMQ5DKAuTbZ546SEh37g3OVcsQ--8ZYUY4qKlqF-h49KR0YZkivQC_rMAZ6NzwtqGzR80Z3ks3MKeb630nODYvaICagPkBURbEiRv7PnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
میگل آنخل خیل مارین:
🔻
اتلتیکو مادرید به حمایت از خولیان آلوارز و کمک به او برای ارائه بهترین عملکردش ادامه خواهد داد. این باشگاه اجازه نخواهد داد باشگاه‌های دیگر در استراتژی آن دخالت کنند یا تلاش کنند تا تیم را از هم بپاشند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/104317" target="_blank">📅 20:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104316">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c62d1ca0c.mp4?token=CTWAGEqwGZqeipkxQDaV_Wbz5n6r3HEmUn74w7A6y6MUU1BpiRXaZ5CGHF89MIZoJ1Uc5y9UVglYBbD4jFhsDimA19PssEUnaoVfbHyjZMJngm1vwyCD7Zeu57fFTdY-upbNed0hsTySTLclJMUkJr5GB7fAa-PlgZW1wWLurfCo8f1A_msMXaP_Y9VrpDx2heCZgEsiC6YT1IBw_ztmSCnQqdBCplSpxcmHHVpVxpVxEX4EJbHu9svPDbziKoT0hp3IL5ccsrBnbcqMexlI4Iq49Z5a0HgmlzirnouzXjEk-0dWypejbWPy1Dyx8YGLGcWc82QZmwD9PQlXgm8Uog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c62d1ca0c.mp4?token=CTWAGEqwGZqeipkxQDaV_Wbz5n6r3HEmUn74w7A6y6MUU1BpiRXaZ5CGHF89MIZoJ1Uc5y9UVglYBbD4jFhsDimA19PssEUnaoVfbHyjZMJngm1vwyCD7Zeu57fFTdY-upbNed0hsTySTLclJMUkJr5GB7fAa-PlgZW1wWLurfCo8f1A_msMXaP_Y9VrpDx2heCZgEsiC6YT1IBw_ztmSCnQqdBCplSpxcmHHVpVxpVxEX4EJbHu9svPDbziKoT0hp3IL5ccsrBnbcqMexlI4Iq49Z5a0HgmlzirnouzXjEk-0dWypejbWPy1Dyx8YGLGcWc82QZmwD9PQlXgm8Uog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
خاطره عجیب حنیف عمران‌زاده از شکست سنگین استقلال در دربی
:
🔺
آرش برهانی را پرویز مظلومی وینگر گذاشت تا رامین بترسه ولی رامین در محوطه جریمه ما پارک کرده بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/104316" target="_blank">📅 20:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104315">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2950ea1958.mp4?token=FWE1Y64LMnjCFlOowyet9yunmTNFoLtvHX8zASl--oeHDffWgJQ5mY-CZkT0JZOTvyR7csYU-UgY_o7NDIfcg5UL06FMgDGFMYrt1qQBE3nBe97CRgyhm87IShV0c-wgJJHiIMLpwsK82RjVK8VakRkA9bQqMhJdeA52yloK88Sn5YI1BmFN-703aRLfPyY7b3vxtiys1h_oCUYs4lb7lNQDSBf-Da60ORddZwzsognIFXahbpU13U1UivBzC8-tTc7eLibxpTm4dLR5Xbw5v9gGZjVWBrvavrs95RginxH6AWJUFsTuVwUNgU3ymANA0pIsksSWYBgjPYoRWYS-N3koHbpJymC26IrBym49OJwsgMJ0ejjGIpn5NjKBgtDryu5WDoGYA3IJAs0axlHdvv3eASmS74RTlGPoghOnify6gisHtXde_8McsK4nXyui8ZuS5CICqmBSTsUQxokdoxQIsHo1K1KxPgXrbp6wV0rBL65_0XdND-yLYeXgtDXcMKaj7k0dQMmr_4KUowM1zECMgBUgcbenjsMkyMtquaNSxL4aQfogL9br0ZGCOkCvYGgtDJP4ay69zCsejWGu4kfLmzA_ZucfPxSfcpZWhUyRhVgSpRTH4HMQ9SOcgnMwEA86NT1CVliwZ2I9fROniQFeMYs_oXpk-EjBvIqYFV4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2950ea1958.mp4?token=FWE1Y64LMnjCFlOowyet9yunmTNFoLtvHX8zASl--oeHDffWgJQ5mY-CZkT0JZOTvyR7csYU-UgY_o7NDIfcg5UL06FMgDGFMYrt1qQBE3nBe97CRgyhm87IShV0c-wgJJHiIMLpwsK82RjVK8VakRkA9bQqMhJdeA52yloK88Sn5YI1BmFN-703aRLfPyY7b3vxtiys1h_oCUYs4lb7lNQDSBf-Da60ORddZwzsognIFXahbpU13U1UivBzC8-tTc7eLibxpTm4dLR5Xbw5v9gGZjVWBrvavrs95RginxH6AWJUFsTuVwUNgU3ymANA0pIsksSWYBgjPYoRWYS-N3koHbpJymC26IrBym49OJwsgMJ0ejjGIpn5NjKBgtDryu5WDoGYA3IJAs0axlHdvv3eASmS74RTlGPoghOnify6gisHtXde_8McsK4nXyui8ZuS5CICqmBSTsUQxokdoxQIsHo1K1KxPgXrbp6wV0rBL65_0XdND-yLYeXgtDXcMKaj7k0dQMmr_4KUowM1zECMgBUgcbenjsMkyMtquaNSxL4aQfogL9br0ZGCOkCvYGgtDJP4ay69zCsejWGu4kfLmzA_ZucfPxSfcpZWhUyRhVgSpRTH4HMQ9SOcgnMwEA86NT1CVliwZ2I9fROniQFeMYs_oXpk-EjBvIqYFV4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
Premier Legaue is Back
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/104315" target="_blank">📅 19:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104312">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Koe04OvAPNN9b0xT5lmhFqxTLKaX0aeocqXYEK80c9_FFGkMS_UKB1uPDMERApOMZx4yYaM6BRWZiWkY0D_IA1ydKOchUuuB50q6acOvIkn7dcTfvTu_Xa1Fi_a_oR8fSgNjU4EXfqjZQaNalb_jcvgfcpFhrdjEQ2d6GL736WbB62wAtL9kJ5BkmwOVBK8YiX9kL_PoKKV0BnIFjE4KpZSfoGR-8PaAicujOcd0s6PXqrWajKyb2Mi1Xj3KzWcY2cGxB-1CiYfh8GWpBXQtlDh0tW2pvSNA4CllvaXJdmr50lenMjhPtgA3CG_Nx2t3HiPh-34xj4scJkXAx1w6lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#رسمیییییی
؛ قرارداد رودری ستاره جدید باشگاه بارسلونا در لالیگا ثبت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/104312" target="_blank">📅 18:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104311">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👀
🤯
یکی از سخت‌ترین مسیرهای مانع جهان ملقب به «Obstacle Course Racing» به اختصار OCR
🔻
ایدا ماتیلده، ورزشکار حرفه‌ای این رشته، وارد مسیری می‌شود که برای عبور از آن فقط قدرت بدنی کافی نیست.
🔻
بالا رفتن، پرش، آویزان ماندن، حفظ تعادل و عبور سریع از موانع مختلف؛ هر بخش، ترکیبی متفاوت از قدرت، استقامت، چابکی و کنترل بدن را به چالش می‌کشد.
🔻
مسابقات عبور از موانع، رشته‌ای است که ورزشکار باید مجموعه‌ای از موانع فیزیکی را در سریع‌ترین زمان ممکن پشت سر بگذارد.
🔻
بعضی از این مسیرها آن‌قدر دشوار طراحی می‌شوند که حتی ورزشکاران حرفه‌ای را هم به مرز توانایی‌هایشان می‌رسانند.⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/104311" target="_blank">📅 18:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104310">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">امروز تو ویپاری رو برد آرسنال
⚽️
100 دلار بزارید 245 دلار (25.000.000تومان‌بونوس میده)  سود کنید.
✅
🎁
برای مبالغ بالاتر از ده هزار دلار بیمه شرطبندی ۳۵٪ داره‌
و مبالغ بالاتر از هزار دلار بیمه ۱۵٪ داره یعنی در صورت باخت مبالغ به حسابتون‌ دوباره واریز میشه.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/104310" target="_blank">📅 18:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104309">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari (3).apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/104309" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر WEPARI
😀
😃
😄
😁
🔥
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 120% اولین واریز
‼️
🔥
بونوس برای 4 واریز اول
‼️
⚽️
بونوس ورزشی هر دوشنبه و چهار شنبه
‼️
🎁
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :
Gift
🔥
دانلود مستقیم اپلیکشن اندروید
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
📌
آموزش نصب برای IOS
g39
✔
https://t.me/WePariFarsi</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/104309" target="_blank">📅 18:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104308">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHlgM1fK7c_C_E6EqbICgZdrllfzRct5zvw9d-Ob_Ud0v32dQ2at3ywThfjE3089S0Pn3FU0ZTkPpa7rGSq7MBnUDqLsQ_wIEk5zfLBm5ZYKg-T1iFiLy4DnYGgLZhWl8WdZA0XWnUhEm_SO0_fL4EmbKwYvugkII7QbTiFdlr-pKSRAJUo7K1w4j_YZHu_rzpXM0-A-CBFrmKWhR5mjhDsybRolTCWBc7WtUsXgJnE6j_VXb4uE09gkuFIuwJ_o1kthwmcjgq_zIl_YMaC3UzF-GoMcpJSrK4Wz4bOy25L_7bcfXQF8965NiFc9bMxduMCM1yLkzzkaM6c_3tnoxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
#رسمیییییی
؛ باشگاه سپاهان اعلام کرد که سعید واسعی و امید نورافکن بدلیل مصدومیت دیدار روز یکشنبه مقابل استقلال را از دست می‌دهند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/104308" target="_blank">📅 18:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104307">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHl5FWd9A3AUHOEvdqa5ikHwrRUdrpeUlAXtRx3GNkP8RYLRhkH3kVPkSkjdNoJXftbwp-x2Zmt4IYhLz69qCzmxCUrSAmKyxGhIHrgNYcOAKRh_I8XVQ0eCZRIMbZKrtKT0dYlnMy8lLCFWqt9IZ8HO9SqE8gK-Zp7jHEAOcYjlKrfp7RNpW69WYjm42jKvPrXjaPPtCUcmSx175RpKiUcwehXZ0UGsiUb5WYoPvo7m7sgoyUCvY4lI2ADuOjAX6GrK3mOCuFVyuUwEGg2ULJNfO3VMsKuUbRgwPTKYyAxQeiRGvV_kX4COBri_Xef_nouNOimPRX5CKz5j3nid4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🇵🇹
نیمکت‌نشین رونالدو در بازی امروز النصر مقابل الریاض در هفته‌دوم لیگ‌عربستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/104307" target="_blank">📅 18:18 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104306">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z0cDz9HqXghiPMXWBrdDlz32_jE73RlsrF35k12DWeS1yO5oJIyXxdZpbU8JsKcuOKZclyKSyOCQc3tVWpKwyxR3_Cp3IGmf0_0qn2d0Xolr2uAlRxDpCicYRV8OpYJ0lmhRpX1Vcw5jgkV9gyDfl115R4bEgJAHOVAsvBWTVA_35XGYkeUh7i9VPmktV1ZJGwrmUgfMSxLbq0tVgJirnEKrf1BuDrhviRsPeDrT2IUj28Kzq0kQrjLXLRw7dCldJ1HR8Z8FLZbCvy5T5GNo29cu9bJAb9rWI1Knjm05DnH56CYdXxL0b43LTDWa2yydEPT357ApKFxTDa0LI6navA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏆
#فوووووری
؛ جرایم انضباطی فیفا پس از اتفاقات فینال جام‌جهانی فوتبال:
❌
لئاندرو پاردس: 10 مسابقه محروم شد
❌
مولینا: 7 مسابقه محروم شد
❌
گاوی و آلمادا: هر کدام 1 مسابقه محروم شدند
❌
فدراسیون فوتبال آرژانتین: ۳۲۰ هزار دلار جریمه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104306" target="_blank">📅 17:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104305">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPZMrPNm_bC9NuM-YaSnLD3KqM7zUbuDKWN7pa7jMHh4hRKuS1QufcP3uYJkyhlQThEE9y2yQrgMbkS55GgcB_NPWCIcUcLKsKnxA-vj7McgheiZMS5i10J4vU4t-N57FDLkMjHqrNd25mEclgvz3lhSMwz8k6txoczc1Ndp5AwqoGsHF4NkR_HS91oWP-tPXjoLsPn72MyOCgGyNIA9tz8RDacJMnkGDCZFrerGCca4hZOlh3_nzXHSXSBFLTFqU0rganiiB_6T8fMgbKbNjlDk_NDR4cvuvJSZzIEQVg6nChrQUWY1xBPO0PkQDo-D0FP_-9oroJPt-9cyZDr24g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
لیست تیم‌فوتبال رئال‌مادرید برای دیدار فرداشب هفته‌دوم لالیگا مقابل اسپانیول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/104305" target="_blank">📅 17:33 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104304">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOslcqUXwXuc6tASWAkncMLgwie6x_YAtefxZOFJGEjjOwu8HGS4ukZKzrtP7k9WpBq8qcrPTdI-XeMhMhxPIRlYWOqjAco9vNYhRM5cblXk_2BmjT0uZ9WJkMTdxYuxDxmGoxaDxMzzD79avj4FrSb1xfm4qnxo4Am-vFEjhkaesehdZFwgQSUqZ4bQOcd4AqqW7y4GX6flyA8Y-WOhMOMvs986KOknZtarEQ2GN-RVtEd1Bz8TDIfgN1IWvVRbwZ5IR2ywmy3h8GUSM7BBHFRQyjrn-MdImODvU0ZJVx0Z5YTQUCVhlI6E9EB01kL3wRNdps_PJ5MH5MNc2xguFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
اتمام حجت اتلتیکو با آلوارز با سه پیشنهاد:
🫱🏻‍🫲🏻
تمدید قرارداد و عذرخواهی از هواداران
😡
سکونشینی تا پایان‌فصل در اتلتیکو
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مذاکره و رفتن به تیم آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/104304" target="_blank">📅 17:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104303">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a482d69c0.mp4?token=U0VsQwOIvvq4jTJD5wVsjjqFs6kIntYl-ZEQiLI3LI9qBwRiNXaMQFc5u3cQn8xEzRy8cmWfiOTKPQgj7RI9pFb7Uw7SENmTJOr7pW3hLCbKous4n7OuR5pnLVne_7AZnXaLoAXCTwrqNc5O2bbFIJPQqYv9imyhitzSiMBNjXaMFN3TOYdjJxs7h2XpixNwRA3xqvUDIuz6MPtxgh6nm6HDn2FYibtoQ-alnqNScfJA6pW6fgd2g26JPD2l6bmItzA9_g0tJisJXg0grnWK0-ShiTNb-AuBH944EvZfFKg1wm_gdKRWiFkvDoBnNBa2_BaMnlNNDqmSHbj2ZKnLdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a482d69c0.mp4?token=U0VsQwOIvvq4jTJD5wVsjjqFs6kIntYl-ZEQiLI3LI9qBwRiNXaMQFc5u3cQn8xEzRy8cmWfiOTKPQgj7RI9pFb7Uw7SENmTJOr7pW3hLCbKous4n7OuR5pnLVne_7AZnXaLoAXCTwrqNc5O2bbFIJPQqYv9imyhitzSiMBNjXaMFN3TOYdjJxs7h2XpixNwRA3xqvUDIuz6MPtxgh6nm6HDn2FYibtoQ-alnqNScfJA6pW6fgd2g26JPD2l6bmItzA9_g0tJisJXg0grnWK0-ShiTNb-AuBH944EvZfFKg1wm_gdKRWiFkvDoBnNBa2_BaMnlNNDqmSHbj2ZKnLdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی توپ، داور را از بازی خارج کرد!
😳
🏐
🔻
در جریان یکی از مسابقات والیبال در سانتو دومینگو، توپ با شدت به صورت داور زن مسابقه برخورد کرد. ضربه به حدی بود که او دیگر قادر به ادامه داوری نبود و در ادامه، عوامل حاضر در سالن او را از زمین مسابقه خارج کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/104303" target="_blank">📅 17:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104302">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
واقعیت‌های فوتبال امروز و‌ ۱۰۰ صدسال گذشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/104302" target="_blank">📅 16:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104301">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b4df9ad5e.mp4?token=sVs0XqYAxQ0aB0YBm_cWSe0kTjDnS7Dw9wVZrvXwFIfiwQJRWKyK0MuKnhyHw2iGvBwIXWJB3fyMYhqafSTBHcbPABpPzbOjAiP4wFiW4WF6kCW8Phm7_BmNcg1mYU-kKbaq-4VkP7iWSRlTQoxHvlJx4Zltzs3TGevzGB4uNgAsacLmCRjBUcPMCyjhT8qhU9Fs3gW5QRHQTTed3dOu0ZL6WKGy_Wovf_CzV2Ck7Oekv2T9NhpgcxtZnvRsFSjdoE2ABn_gBRPtK40w5NIcF6lzeWNDYCVtza5-Ow1G4kOzdabXDgbaQoxjhaOulZ0XqrSGYcX6rYlIyg2gIlPj-gueAMiTRTdA_cj95FjmV0Ijo9dnBmHZagRzlH4xKZBxxgZ2Ywpq5zGTHmXoOoEWHNNDp_RdnbKs7deGSraum9jiJU1Q3p8rlv6hvX4L46RhAZi1FONSvrkBoURwva5Lj2g5WVWXa7jsfhZyJLz6jTvEol_ISe4zaG7IS3ERJOrH_QvnxJPTadbDScFp6lrbrQjDdkXwD6GPqDARr2JVOCASN8B9pge60Al4OQtBYhd0KZ774iyUIrDq5DzENB6mJ15KrKKQmbq-qAv2KyrjO2DB7IiEWYCLEu2m8r8tFK_sVw2leNyBXN5yIl7WcLDynb1R0Eq1UdQxkbvofdA3Pr4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b4df9ad5e.mp4?token=sVs0XqYAxQ0aB0YBm_cWSe0kTjDnS7Dw9wVZrvXwFIfiwQJRWKyK0MuKnhyHw2iGvBwIXWJB3fyMYhqafSTBHcbPABpPzbOjAiP4wFiW4WF6kCW8Phm7_BmNcg1mYU-kKbaq-4VkP7iWSRlTQoxHvlJx4Zltzs3TGevzGB4uNgAsacLmCRjBUcPMCyjhT8qhU9Fs3gW5QRHQTTed3dOu0ZL6WKGy_Wovf_CzV2Ck7Oekv2T9NhpgcxtZnvRsFSjdoE2ABn_gBRPtK40w5NIcF6lzeWNDYCVtza5-Ow1G4kOzdabXDgbaQoxjhaOulZ0XqrSGYcX6rYlIyg2gIlPj-gueAMiTRTdA_cj95FjmV0Ijo9dnBmHZagRzlH4xKZBxxgZ2Ywpq5zGTHmXoOoEWHNNDp_RdnbKs7deGSraum9jiJU1Q3p8rlv6hvX4L46RhAZi1FONSvrkBoURwva5Lj2g5WVWXa7jsfhZyJLz6jTvEol_ISe4zaG7IS3ERJOrH_QvnxJPTadbDScFp6lrbrQjDdkXwD6GPqDARr2JVOCASN8B9pge60Al4OQtBYhd0KZ774iyUIrDq5DzENB6mJ15KrKKQmbq-qAv2KyrjO2DB7IiEWYCLEu2m8r8tFK_sVw2leNyBXN5yIl7WcLDynb1R0Eq1UdQxkbvofdA3Pr4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
بعضی‌وقتا دیدن اینجور مسابقاتی‌از فوتبال دیدن پریمیرلیگ ایران جذاب‌تره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/104301" target="_blank">📅 16:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104300">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
🇪🇸
لیواکوویچ سنگربان تیم فوتبال فنرباغچه ترکیه به باشگاه بارسلونا   HERE WE GO
✅
✅
✅
✅
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/104300" target="_blank">📅 15:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104299">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEYuqkKFU1mNWEPZ0H9Q0i_T5_ANan2a7qLlI_k-HHVwO8ciBlktKvLZfIzlgr6-8uQmhWab69Z8j9orZR4ttIeMg7UPjCRdjXQC4s5Q7qkHLtvwTvdvmAiCbTtP9vAZ4z1Yq2LzZQpFZM5WiyLieFh5Xhhcabj2XlUi6fjK4IWTpoBmEpyVcTprQRz8ApvCV4K3z8oSKQM5puuo71lSh5-5fD0p5a6-Wr2Olp3LkIoMwh6RTgE9eZTI_Tyy1tZx93LtwRjN7C56Ny5cBjnPTXWeofz6E8-5ZqRJY8ygImjiWy23hYITy1YiYuvxw-ZHHv_-gzP10O1pvNu3GkE1HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇹🇷
#فوووووری از روزنامه اسپورت: بارسلونا و فنرباغچه برای انتقال لیواکوویچ به توافق رسیدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/104299" target="_blank">📅 15:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104298">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jo9IXwcWGqE1dz5IOt39BI3J3WLSboPcCOlTSWKeBpTE4KkwI8OJbod0jCnNy5CEuK79D6qxUhy5AKK7lVkcj-4reWGAivUd-sFmvy1fbrk6HWMjHvJVRppVhRxklYuDudK1oLFgPSoOTlZXgm66C7PIimyn824wULVGb9xER5w6xoHS8M9Nd31VbNsyqtyYzY8_1a-6N1STXVj6dswTLBoZZIpuUGEHoJIlZsIDNxEdYZgQ2b3kZf2-vldRt1URFtmBUHlMN9t9y6SmWkpHZqxWw3XFTYF_nvBxhP2oTnyO8OigdRaJxS0AxozYeUF5ZeUTJriFJYWZZ-jxwYom9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇹🇷
#فوووووری
از روزنامه اسپورت: بارسلونا و فنرباغچه برای انتقال لیواکوویچ به توافق رسیدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/104298" target="_blank">📅 15:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104297">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xa0_MWvx1tnGmg-OJKhmE5JzIDoy11DBPPC7CUhwJGOA2Tg96GmOzgTki642fEkSQOs5SqiF--7kpAGqGLvqFoAAWQUc7MItgFjA7QptkmNwDbdlngoXfbfroNu9APpLbXqWS2hzqo5oThezvci8k6_ZVezI5GZxvKgtFkP73IFyd4yoG8d_ZpyrM-zH1E7_SMxi9ewXTRPqX3xg8gugC5lLEnAcuvg-rdcI0mE-TZvqPglaojX0SfHEOVTvPesTaWezT7WXPesKRszsST21beMGclBQWeKWXznWX3N1IKdOnpf-an5FeM3JF4L4e4NwdkLwRjNiZXQYTYcTaxe6nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
اتمام حجت اتلتیکو با آلوارز با سه پیشنهاد
:
🫱🏻‍🫲🏻
تمدید قرارداد و عذرخواهی از هواداران
😡
سکونشینی تا پایان‌فصل در اتلتیکو
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مذاکره و رفتن به تیم آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104297" target="_blank">📅 15:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104296">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQxQFA7uAxytgp4A2dPm8ft8YxviL6Wcov3k_eunX6KIpJg3UfLqeXhrrDFRoBgz7eJTSOwEIb1ot-75D7YcTUTclMjo2Vbek8MvrU8wDkvHqxWVZcpiZNFuOXG3AL8q98X4iivAU53Gz1bCnMRpNwUZrN_iUfz8wqz-R3udrzGyR5iBx8B7YnIdpRNd4VjvwhaNfMJAT8l2QYNYQAjg1e0s84e-SezMR27a_aQsGXx1q3sf-KzmDT3qjMfYG9QwtSORRKVB6MAP1nCdMXxikJVZaNgekHh7AO1xQdQzVCzWzW7Givy1dQbzdE_NKoZz_arZd0IDnZ7v9jT0s3QE0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
میزان هزینه آرسنال برای بازیکنان خط دفاعی
🇳🇱
یورین تیمبر — 34 میلیون پوند
🇫🇷
ویلیام سالیبا — 27 میلیون پوند
🇧🇷
گابریل — 27 میلیون پوند
🇮🇹
ریکاردو کالافیوری — 34 میلیون پوند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بن وایت — 50 میلیون پوند
🇪🇸
کریستین موسکوئرا — 13 میلیون پوند
🇪🇨
پیرو هینکاپیه — 45 میلیون پوند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ازری کونسا — 51 میلیون پوند
💸
🤯
🤯
مجموعا: 281 میلیون پوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/104296" target="_blank">📅 15:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104295">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2JcnQpiGR0liBwcZvLD8DaxCP0cM88adcCo5evku5qPqkFRAm96JyQENvoDrk9SqTB1vjaDdpKpoIEDxd6mxDBOLGTaWtA8lwqH_9Pd3qM5FaowgPVLjqDGre6U7L4lH9TAszxzIrRM0anr7kcyAyBScqGRmwvsn75n6s7CO1JlxZ-SGGSKeL7Z4SsxpVoXZtPW9RQpxf7cQfTt85F52ppoTqmgmLnnHpZ7rhKFQ6S719WFASKyraaS3JZ5VVh7XFxPfxFVUw0xlGsRjzjpMszPVKSKqpUflkm7r1W8ntUSZI1QjpAJJrAh7gAUKwBnwg_pPuoBgK8-WJ2Ylntj6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ایشالا آلوارز تا ۴ سال آینده دووم بیاره
😂
🙏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/104295" target="_blank">📅 14:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104294">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b326cd073e.mp4?token=em8VlIhzZR2J0_34whmAaxALgDuXtVYBQpmCuao01499WaSpi_XOhbSI2zpqWIPCcDRg7FldlVxX3Le7KD962WLd9frKt5_fIj3X3ULsQd_iqbHQjGStCnH3fsd-hvcQ3PB5-fozVUxaW9D20X_d1RGzkMBezx_mr8Sm1YbTPb2LpH3YqZrDgxzMub4R9ZbSV932G0QaODyIn3hVjf_j91-24Sks4dQNPnsfQQ7N1YMNFsR_7_Pb9e29v8CUZgY5BrOcFhHsJ0XWTzU8ivsB3pbk-65pCDgfv-U2ZuGTzxWJD2_Zvro8duMIeLjnE590IpqKk0wtrmnv4MVW2gavYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b326cd073e.mp4?token=em8VlIhzZR2J0_34whmAaxALgDuXtVYBQpmCuao01499WaSpi_XOhbSI2zpqWIPCcDRg7FldlVxX3Le7KD962WLd9frKt5_fIj3X3ULsQd_iqbHQjGStCnH3fsd-hvcQ3PB5-fozVUxaW9D20X_d1RGzkMBezx_mr8Sm1YbTPb2LpH3YqZrDgxzMub4R9ZbSV932G0QaODyIn3hVjf_j91-24Sks4dQNPnsfQQ7N1YMNFsR_7_Pb9e29v8CUZgY5BrOcFhHsJ0XWTzU8ivsB3pbk-65pCDgfv-U2ZuGTzxWJD2_Zvro8duMIeLjnE590IpqKk0wtrmnv4MVW2gavYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
وحشی‌بازی آرائوخو تو تمرینات لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/104294" target="_blank">📅 14:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104293">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btIxnPI8Y5ld12drGPwumdWJtilUkY5pEKqcR76xhhvd0i13bpjGOlqNZfk3g0njSdMrcOwiWvr0xO1qzo4tmNO6TcGH32IqnmeCHFEbxFKW77-pTvxKosLYZa4XOEfvWsOhhlCqfwDFPzXZyZ_2tov2kX6k9Hx392Y0Q2TSd2gBmA4LYiN66Fs2dPD_HMw3i3uSHXuDWoYdnJm7R5wjCHw0nT-7-c2LMZEydV7jL6vsU7DP-KDUDYsvLNeHlvgKYO_HrfUSuiooBeDtrhIMSbCs2V7XDIZW5V3ZE_Cuv0UEw3tHc_DCgs6m_i6dCZFT-D7_uZq6CWFrjqIXDGqddw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🤯
تمام تیم‌هایی که ژائو کانسلو در اون بوده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/104293" target="_blank">📅 14:04 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104292">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7da3520408.mp4?token=GSoYYZhryGyg-r0GWgqiO14QUsrV5-819sR5xaUqoIiKcNy7CPwIvctHu2qdFGuuK256Sc8rkJAz3xCag0TxP3VMqEhqCfMxJ6LAyLEx9oTdJu84bQTR5KjO2Giir-LyHGRZhFh1DxYnNvi06dLh7FWJef7iaWJaVapgyPKQP2L62lUFHrbWCkRG8O8m3th-7QKrWkqv0mjWG4y65rVznkn0ZViCfh3nDvwYikacbosBzePVhaysJbr-xeSkWtMemPFC7JYWM0L--hDtkQsgBqzADdhGx1AsTIi-2ee_ZESOjCPIa1qad0y-lWhpWee7H6ac1B_LAFptzK-yHq4WVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7da3520408.mp4?token=GSoYYZhryGyg-r0GWgqiO14QUsrV5-819sR5xaUqoIiKcNy7CPwIvctHu2qdFGuuK256Sc8rkJAz3xCag0TxP3VMqEhqCfMxJ6LAyLEx9oTdJu84bQTR5KjO2Giir-LyHGRZhFh1DxYnNvi06dLh7FWJef7iaWJaVapgyPKQP2L62lUFHrbWCkRG8O8m3th-7QKrWkqv0mjWG4y65rVznkn0ZViCfh3nDvwYikacbosBzePVhaysJbr-xeSkWtMemPFC7JYWM0L--hDtkQsgBqzADdhGx1AsTIi-2ee_ZESOjCPIa1qad0y-lWhpWee7H6ac1B_LAFptzK-yHq4WVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
شباهت فوق‌العاده عجیب گل‌فصل‌گذشته علیپور‌ به سپاهان با گل این‌هفته حسین‌زاده به این تیم؛ فقط واکنش حسینی‌ رو ببینید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/104292" target="_blank">📅 13:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104291">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f86c9cb5.mp4?token=eN1xzDrqxme4z9JWQZqCtAisDKF52HCGIK7TXs5D6wSRyfNwENfljdcKFyeNsjlsHd5lelKeyt7oR0O2Tv6Z5-HbBSc7mVeKFNP5DbrvUaRhssoeV43xYhqWoxRssf4Rge1mmIRctyCtoHcDnNTOcrLMupckVF8Syd3fZhgwhdLnMm6W9v3Xbi2s9BMn58mSmCOWOCh8Rmkx9wJIYcrnG8InG7TlnKNtxM04hrwBQae-6OXx0Rq9WjF7Nih5YUoZFQYVu66ta6_Elf8XcIDcqHfvJQEmR_-y52rzm0fJlgCuSzD6X1iZ2JdKSzeXB489xNUD93xmSYPWxe2AlPgq7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f86c9cb5.mp4?token=eN1xzDrqxme4z9JWQZqCtAisDKF52HCGIK7TXs5D6wSRyfNwENfljdcKFyeNsjlsHd5lelKeyt7oR0O2Tv6Z5-HbBSc7mVeKFNP5DbrvUaRhssoeV43xYhqWoxRssf4Rge1mmIRctyCtoHcDnNTOcrLMupckVF8Syd3fZhgwhdLnMm6W9v3Xbi2s9BMn58mSmCOWOCh8Rmkx9wJIYcrnG8InG7TlnKNtxM04hrwBQae-6OXx0Rq9WjF7Nih5YUoZFQYVu66ta6_Elf8XcIDcqHfvJQEmR_-y52rzm0fJlgCuSzD6X1iZ2JdKSzeXB489xNUD93xmSYPWxe2AlPgq7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇪🇸
هو شدن فرنکی‌دی‌یونگ توسط هواداران بارسا حین ورود به زمین در بازی جام خوان‌گمپر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/104291" target="_blank">📅 13:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104290">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POUIRd9o5PAS4xNhdiPLforT1Vt9tTuCtEwCgTaYvhsESRwHGrcQWS1Tjd_bkY9n1arrhexMvX9i_rQROngjdEKp2lVwlgPlvf27NpOjhd4vtpkDSLMUGw-LswLUHHbAXmaRtg7MU8QfaLBSN_MlVaQ9clxSJMD39GT3AoeALk-VDhhlg-qjifCruW-JIRsAeX1W_evmtqG6y9sEZb5J6q3WmM5RB1slHuwYRYJBV39LkdYugrseZhgTTpLvqKV9gbylhSGJb5XG4hJVwem9xeD3yMXtQY6Nkw7KdYzqd-BLORWmzbns95uqf7DcJkwBKKcZNqfbqzKYoPvTBLaXyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
گستون‌ایدول خبرنگار مطرح آرژانتین: بارسلونا با اطرافیان لائوتارو صحبت کرده اما هنوز پیشنهاد رسمی نفرستاده. اینتر شدیدا برای موندن لائوتارو پافشاری میکنه چون در فاصله ۱۰ روز تا پایان نقل‌وانتقالات قرار نیست مهاجمی جذب کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/104290" target="_blank">📅 13:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104289">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kch7MkYvrZ-1Lu6CHjb4Ciue66PZGDdVkfoG-TrxYr-tTRSrNfHZAmj9qrDqW2KYOSM21S_XJdvqC95dfNoHZ0HHdz8EH2cmvoflie6qysQaHWMllXp-EIuNCqi3QO_SxAI4MR3q2FyRp36RCeBv7g4fcj2KwT2pTSKSd_1Z9IgIDvvENy81SCnO-yhE9f_pBVc37SNqUdaOd1xLTsDuqOiial3_6Mt0tC6Y9hJFM9DBZmcRxniq2_gt-hYer2Ns90SayD92X-_TU9agDTFmW6Weze5QVoy0knPJR6fIGnbZdM58C1vG10S5j9yiYG99k_7JNbShyWKkzBsP_9qwNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚑
🇮🇷
#فوووووری
؛ ابوالفضل جلالی بدلیل مصدومیت از ناحیه کشاله‌ران دو دیدار آینده پرسپولیس مقابل تراکتور و ملوان رو از دست داده و وضعیت نامشخصی برای دربی داره. پزشکان حداقل ۱۴ روز استراحت رو برای این بازیکن در نظر گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/104289" target="_blank">📅 12:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104288">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFD8sIA9iuzUuQBlRylvc4EJjlqMJoD59RE1iS1CSvFHCYlqMNyGVvb_cdTmAFHe7r1zuvME8IiYxlDn_oV9wR2OEoAePfgOXNGBpLQ_l2TPTY8bnvAuf00IwhzV46imp8q9uU0TYYOOF-nuZYYsR0YI-RxmpNLownCLIfkzwX4fFCPHBUHsMhAMNxvqZX7B_eZU6ewGbXTuGCfzniX1GRdPxUXMDgqEHJJnJyQ_iRUdSKgokJ7nyRJ_8Ga9fVW8CSi9iy_J8RP7k48c-TuE2Ky9Pfa1smdHkdQTwg9Q_UoNq-mlKgg_Vd-_qDOG2nwpQfqQg69C-SCDPdbLfczR9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
❌
👤
#فوووووری
؛ علیرضا بیرانوند در لیست تیم امید برای بازی‌های آسیایی ناگویا قرار نداره و طبق صحبت‌های سال گذشته نظام‌وظیفه، باید از روز اول مهرماه راهی سربازی بشه مگر اینکه اتفاق دیگه‌ای رخ بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/104288" target="_blank">📅 12:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104287">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c4e9318b3.mp4?token=iCKOAdSqSiJSfIy9KiGkcrSgUUszBti13Buh9eXaSe_41MjVZo92Jxnjt7k3tiuqoSUsc_ruePfLnCoySykkOiQEMEwQW2LOg1uVJEDzPACE85RgBIB-loLvS9qkPL1CpHNS2hX6io-tFPIZGUuiJrn56tGEkxMpLNYE8VfGnsP8KruXDR4F-6-QoJMnC_oFthjQVmzI1g8M6DdI2QuphUg_B8cLLaVa_SJkMfwqC8DUosMtJXXNEzWufpzajopz383mbgH4Istrw9IolgrR6yWZfFTjiUd1pATjior-mz7IxPF5Xx6pI16jOF2MDiC-31ZBhyDmn5W4WmDC7kDWTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c4e9318b3.mp4?token=iCKOAdSqSiJSfIy9KiGkcrSgUUszBti13Buh9eXaSe_41MjVZo92Jxnjt7k3tiuqoSUsc_ruePfLnCoySykkOiQEMEwQW2LOg1uVJEDzPACE85RgBIB-loLvS9qkPL1CpHNS2hX6io-tFPIZGUuiJrn56tGEkxMpLNYE8VfGnsP8KruXDR4F-6-QoJMnC_oFthjQVmzI1g8M6DdI2QuphUg_B8cLLaVa_SJkMfwqC8DUosMtJXXNEzWufpzajopz383mbgH4Istrw9IolgrR6yWZfFTjiUd1pATjior-mz7IxPF5Xx6pI16jOF2MDiC-31ZBhyDmn5W4WmDC7kDWTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
😐
شب گذشته در اقدامی عجیب، حراست سیتی سنتر خلیج فارس اهواز، با ادعای حفظ نظم، آرامش خانواده و جلوگیری از مزاحمت برای دختران، از ورود پسران مجرد به این مجموعه جلوگیری کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/104287" target="_blank">📅 12:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104285">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T9PHAs_dFukTD3UPgwSIC3yfCUEgnfl4F52gGvE8idq8Sult5vVNqKPHKfsDReMcx2WuqwlhCPNfqMRwVw6xbRTNaT_q3-L9B0LwiRzPtRHrq1QU0yFaOifL1H_SwYonaBdPE9g7DXwsB9Zk0yBt-Zqmy0-2axlAB_4xT3UW9vkQHNtrax6Z5iRc50fysGyrLFjLfTiPZCxtKZKiMTN1aAbkO-UXTyFjAYG6_-8ZeAXkqpeewGLjZJOP03JFFpARGwif2dPi71d-hzf25qMvuYfF8UcBn2gpurW7sIUEgpm2MH5xpFC7POpChRFitgTt-1ILoE5TnRKSnJ8zr0oxlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J2zPf1JI5ANy-61U3Ot7ufFX-EYy8gmrf_zZuyRmoMl6nsCO6MkY8hY0xGeTuPNV94t-Eiknvn0o5ECd1SuxmKFhbt2vldlAKBLu8I2s_4mBerKS-AUxQJaUJPohqu_j9KYoVI0Ak2e97IjclrZjtDohAfBM2Bdf7V3EHS-MoPgg3KaWR5ZAkfNaKtiSgU0pd6V0fpy3eSXAh1RxzockYJQJnCQQczQfxKQILXMapaEmIyPj9gkOYUeLHb8ZUIdYscwTzdapJAnFNwgN996LkKwrVFxBN60ZCjj1qF-66v9c5X_0auS-Wl1eF7qKlczWU1X5YVmUm2tupCGTAgUC-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
‼️
بنرهای ضد آلوارز در ورودی‌کمپ اتلتیکو:
یه دونه بنرم اون پشت زدن نوشتن: گمشو برو خولیان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/104285" target="_blank">📅 12:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104284">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baadddf33a.mp4?token=NJBvbOs6LE_XHOP02VxgQ9NCi7YswRAh2NddTX6K68vNi5DrQCJo9Qjsu9p2y-X1LWfyOSciJ7_8MzgkYl-E_SRh94uIgDT0lsHs8p1YI__VZzaztOBBY089MVtBqShljyiu32pBmu3CQwnTzGjDvnPs307hWPIaJap78u_Ca_bMfMnbgA3WByhR-C9rXc8L02aCGzk8snp4dNreBPBoEdWDVMiadQW21jBbNheGDWJcd5c71Sz8CWnDxpe6Uq_tX21RI4e9nkjNQwDMlLlAmWBwje2Kel0d7JuCiWcd8cf8ncIL7gTCpXMOcVYryYWHP3OTf_3bBCrRD3bAHmdggQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baadddf33a.mp4?token=NJBvbOs6LE_XHOP02VxgQ9NCi7YswRAh2NddTX6K68vNi5DrQCJo9Qjsu9p2y-X1LWfyOSciJ7_8MzgkYl-E_SRh94uIgDT0lsHs8p1YI__VZzaztOBBY089MVtBqShljyiu32pBmu3CQwnTzGjDvnPs307hWPIaJap78u_Ca_bMfMnbgA3WByhR-C9rXc8L02aCGzk8snp4dNreBPBoEdWDVMiadQW21jBbNheGDWJcd5c71Sz8CWnDxpe6Uq_tX21RI4e9nkjNQwDMlLlAmWBwje2Kel0d7JuCiWcd8cf8ncIL7gTCpXMOcVYryYWHP3OTf_3bBCrRD3bAHmdggQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
مهدی شریفی: بهمنی گفت تیم ها بعد از بازی با استقلال از این تیم شکایت نکنند/ از نظر سازمان لیگ یاسر آسانی برای همراهی استقلال مشکلی ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/104284" target="_blank">📅 11:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104283">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22ba668970.mp4?token=rGXxbJ-jLWa9gm-xLsCfwQK1-6JU8DfWTMi9UktPenT_uTEz9ZpONVIiHYODpnNd-rlqCu9d2_BosLNXwE23V8_OVnb8dHUhwcTriX6JvPGO8kzORDHtnFer3ZJOugPNnnK14QKVBpbmG2r_O_NR9hqYsLX5MSSGVRAojKOPkaQIZ-aLH3eXp4tNHyVA3E0clmQD8dPWzAiI5_Tm-dM5i5X7q8Wg82Mu1PR4srnP8OqmvH5BiE6TDyMnWymXauBT3Skawa96aH6re8-TTX3c6a8T3s_fwxFOM5DGTWAWi1aBWMzhjvV2FvH5NrieQ-7HjgH80FDwNAZtw3vLpo5CCxFY4hztxM_ni9XgW3lErN6U8XocHVnJQHROfQBzX5MPg4mqz4Vl5JEzZ-bxlZ_rqDgGECey7as84CEdB9UHCOvpWGMmU8wF2gBYRryzqsigJoYa19ncfvFkK3Mi9xpGq_-gd6xmtD2VL6TJxXvi9cZvWj8vqwhpuR8FomBbxZRpZNHWft6BRfRwSkSLydnCgBp-B5WbhFsfdZ0AeakIZ6USGtuODmUOpyxmPlsqmCxjAdopNR1CW-bakce_uDzlnursAMkk0BGpgOHdab-U50MujFuf9sJ44543S3oaDrm4pxqrIkbcVk1ifm80BHpplNDbdziBJFcZSBLrXUKy410" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22ba668970.mp4?token=rGXxbJ-jLWa9gm-xLsCfwQK1-6JU8DfWTMi9UktPenT_uTEz9ZpONVIiHYODpnNd-rlqCu9d2_BosLNXwE23V8_OVnb8dHUhwcTriX6JvPGO8kzORDHtnFer3ZJOugPNnnK14QKVBpbmG2r_O_NR9hqYsLX5MSSGVRAojKOPkaQIZ-aLH3eXp4tNHyVA3E0clmQD8dPWzAiI5_Tm-dM5i5X7q8Wg82Mu1PR4srnP8OqmvH5BiE6TDyMnWymXauBT3Skawa96aH6re8-TTX3c6a8T3s_fwxFOM5DGTWAWi1aBWMzhjvV2FvH5NrieQ-7HjgH80FDwNAZtw3vLpo5CCxFY4hztxM_ni9XgW3lErN6U8XocHVnJQHROfQBzX5MPg4mqz4Vl5JEzZ-bxlZ_rqDgGECey7as84CEdB9UHCOvpWGMmU8wF2gBYRryzqsigJoYa19ncfvFkK3Mi9xpGq_-gd6xmtD2VL6TJxXvi9cZvWj8vqwhpuR8FomBbxZRpZNHWft6BRfRwSkSLydnCgBp-B5WbhFsfdZ0AeakIZ6USGtuODmUOpyxmPlsqmCxjAdopNR1CW-bakce_uDzlnursAMkk0BGpgOHdab-U50MujFuf9sJ44543S3oaDrm4pxqrIkbcVk1ifm80BHpplNDbdziBJFcZSBLrXUKy410" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
حمید بلان عصبی در بازی پریشب فولاد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/104283" target="_blank">📅 11:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104282">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/Futball180TV/104282" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/104282" target="_blank">📅 11:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104281">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClB4bKMhKYudFMe7iN2ayJ8KRQCRZeaWrYBzEIDt7B9iPMh3HThJqeCV8ZBwpeRt61GIZHlqCOuujexefMp__RRRdQ20aRIS2kzsWi5sbqoANHNJlR20oI-U3-LgcB872RHXWP3CSQ_xCaeMqQ7chuUIR_SMrxmUAehztGH0qWUVPyK1j5ieYQyn2h8xzt4DOe0Raoq2EOewRQGrm4OyxjVzejo1kv_dBENzMekfqt5VNgjZDdr4BvFsHC_0uhia0quhP-HtyzDiqgw57XHtdjsKrpzlD-sDar3djmXwVih0ySCoBkYXaMnA0xSWkHhcCIXIUerm-7AfTSEXoleJhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سایت جهانی  و معتبر
#Melbet
🔴
بازی های مهم 27 مرداد
🆗
ثبت نام آسان و سریع کلیک کنید
🆗
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
پخش زنده ی تمام مسابقات
✅
درگاه اختصاصی برای کاربران
👍
پشتیبانی 24 ساعته فارسی
🎟
Promo Code: MELBET90
🇩🇪
دانلود اپلیکیشن MELBET
📱
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r30
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/104281" target="_blank">📅 11:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104280">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adf8127dc6.mp4?token=hx8aDz5pMfUkbzHXZmofqLAynI3LrM1lTbvY51a9Yx7PwzzB3eYd9wRjiNsuxSA5fO-SANJ3d5N7wBjdNVUktCAn0QDApVBUL_5yWfxla89EvGkdytVEZlAflYzMbvfgATQ5vTXv5b7uAslVAUx04c8BLMCQD-m7fzW4ZLtj5jyPpNa23lFqs4tBCKF_tBacfK9lCUd04NyaVAkHQOULQokLQwZlkzUwnbWnf4Ya7iqgPs5pmvRQzNxOOAYmQ1NgTPfpO2YAbjGC2c_6IRbDTJwVBlTdUou2U9sLr7xQvc7qdkgHw68dPpZF9TRHsT_KMDyTu9dhpXSC2o7E_Lq3rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adf8127dc6.mp4?token=hx8aDz5pMfUkbzHXZmofqLAynI3LrM1lTbvY51a9Yx7PwzzB3eYd9wRjiNsuxSA5fO-SANJ3d5N7wBjdNVUktCAn0QDApVBUL_5yWfxla89EvGkdytVEZlAflYzMbvfgATQ5vTXv5b7uAslVAUx04c8BLMCQD-m7fzW4ZLtj5jyPpNa23lFqs4tBCKF_tBacfK9lCUd04NyaVAkHQOULQokLQwZlkzUwnbWnf4Ya7iqgPs5pmvRQzNxOOAYmQ1NgTPfpO2YAbjGC2c_6IRbDTJwVBlTdUou2U9sLr7xQvc7qdkgHw68dPpZF9TRHsT_KMDyTu9dhpXSC2o7E_Lq3rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🎙
خواهر پژمان‌جمشیدی در واکنش به افشاگری شاکی پرونده برادرش: پژمان جوونی کرده و میکنه. اگر اتفاقی افتاده نوش جونش
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/104280" target="_blank">📅 11:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104279">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fb6e5fa0e.mp4?token=TxnaMdXvQvfx7RWcI-o3mcr3ubuH2O1XXXvi1EZ4Sf5FPNwez6-6O5zyo2IJvZSlMxIhA8sRoz7HLMcYg4_wgyDFmdbhbv0gYYQTrgcJJEnAZCUrZHJ6eMqLnwTmnM8YMiCD3frEmdDYtinbNp_mG5-hDyRWtDrFOYACjnn3GfROfTTOJfABtxKk9Bv-HoKMQ5OT2iwzjPC0shrGMVkTDzPSK5tKb6UEJQAi1iSDTyc_MBCXMbF9CIbgnI4CGxJKn7RkYBY3_DNMSae3Tdf5jGTG2C7CWnNZ_2RZGCrr-Tj0G2q5Xt80iUYFJM3N10tMyjeoJgbARUHlm63lY3MBpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fb6e5fa0e.mp4?token=TxnaMdXvQvfx7RWcI-o3mcr3ubuH2O1XXXvi1EZ4Sf5FPNwez6-6O5zyo2IJvZSlMxIhA8sRoz7HLMcYg4_wgyDFmdbhbv0gYYQTrgcJJEnAZCUrZHJ6eMqLnwTmnM8YMiCD3frEmdDYtinbNp_mG5-hDyRWtDrFOYACjnn3GfROfTTOJfABtxKk9Bv-HoKMQ5OT2iwzjPC0shrGMVkTDzPSK5tKb6UEJQAi1iSDTyc_MBCXMbF9CIbgnI4CGxJKn7RkYBY3_DNMSae3Tdf5jGTG2C7CWnNZ_2RZGCrr-Tj0G2q5Xt80iUYFJM3N10tMyjeoJgbARUHlm63lY3MBpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
یادی‌کنیم از مشاجره تاریخی علی‌دایی و عادل فردوسی‌پور در آنتن زنده برنامه نود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/104279" target="_blank">📅 11:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104278">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAR7CDV-DDWNlmupeWtU8EJ0xrPJToc2KlE_7rigorMuztqJK7X0Afi_i0Drp9CnvVEwOtbB6-vr74qNUT1smuf3kQvAL98qXVadAY-6XqBqzw-5PhY7a_T1QqBlP7ThVX_WUPM5M0vFXf_vRaCgKn4HLnJ50JLsa53PB9hlmp9stqtbnnzLdrDOD9So7ndZ5ykKO-9tGYkA-oVTXpdo2A0ZNE9DXTCOXhhY_6sAUJ9_3xBT-rG5wFS6Ojpu7yc9oAhrtf0TlfNkVTjbYxTA3vkPo7JY3iqrFoPo6Z4uB0pRO1xSgXvOcwJTE16nu12R5gGdgEr9fQvOojylDvybCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚨
🚨
🚨
توتواسپورت ایتالیا:
❌
فعلا هیچ پیشنهاد رسمی یا مذاکره‌ای بین بارسلونا و اینتر برای لائوتارو وجود نداره!
⚽️
بارسلونا ارزش او را حدود ۸۰ تا ۸۵ میلیون یورو می‌داند، اما اینتر لائوتارو را غیرقابل‌فروش می‌داند و حتی در صورت موافقت خود بازیکن هم حاضر به مذاکره نیست.
❗️
🇮🇹
در حال حاضر، ماندن لائوتارو در اینتر بسیار محتمله و انتقالش به بارسلونا فقط یک احتمال تئوری محسوب میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/104278" target="_blank">📅 10:37 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104277">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f89a3d29.mp4?token=vJ90pwmwjb0LLiRinDQ88v8KVP5vONBuzeYC48FIR4OwkR5iiiGd2Pgi6XO-8NEQKvCJKE3Ul3sA709CnZVflxsfU_Hl9dkKhsVKTxMb5ETtWzMMN2O9lZ8dUEIMErAzDUT46ZhCTmNyybjR0leKL_u15f_L2ew3lMHrs1J0IIo61Zfi5QOwsJjYdRKex1Et4Bt4ItAkALUrEibLMzYH9ahxq7XNZ47l1V34d2xuGqw1KV9o6DmXg-_3Tf8vcBSm0a6E8LnlDx48A-q4Z0F5hqywK2Qq1AhCuxHIDCOkuDeHdTopayerDohg3BueTZPgzohPZyYvERWfl10P9T_zUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f89a3d29.mp4?token=vJ90pwmwjb0LLiRinDQ88v8KVP5vONBuzeYC48FIR4OwkR5iiiGd2Pgi6XO-8NEQKvCJKE3Ul3sA709CnZVflxsfU_Hl9dkKhsVKTxMb5ETtWzMMN2O9lZ8dUEIMErAzDUT46ZhCTmNyybjR0leKL_u15f_L2ew3lMHrs1J0IIo61Zfi5QOwsJjYdRKex1Et4Bt4ItAkALUrEibLMzYH9ahxq7XNZ47l1V34d2xuGqw1KV9o6DmXg-_3Tf8vcBSm0a6E8LnlDx48A-q4Z0F5hqywK2Qq1AhCuxHIDCOkuDeHdTopayerDohg3BueTZPgzohPZyYvERWfl10P9T_zUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بغض و ناراحتی کوین دیبروین بعد از تصمیم عدم تمدید قرارداد با منچستر سیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/104277" target="_blank">📅 09:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104276">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b11ab942df.mp4?token=lsL7oux0IVEa1LGY-gUYP8eA51BWjfY3xsZLKhE6DOtVHnfCmo5zPSJRSUYZVkmWVXKRlmdPBqP267CElxarzc4Ji5ZrVZa33CDR2O_tsh_hWh7I5IPq_FlaqgpG4s5eN9GetKxbtGJVG6UmGTyB886-bByUJTL3m1PuJ_DKnIcTLUBr4x-x45yn9QQ1NdA2uKXpt9FQJk31chxzZdcPwbRNWPNbQqJzXK6K8GZPqtwOUgoi8beXLtzKgUqZea3V_uWOnWr1pi9v6HNTQOKImh0SJEiA31XHs-B5q80w7Zmvg0NuqcEclJwl1OSMXR1kwSpAvInS1xnPW1zlvchxRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b11ab942df.mp4?token=lsL7oux0IVEa1LGY-gUYP8eA51BWjfY3xsZLKhE6DOtVHnfCmo5zPSJRSUYZVkmWVXKRlmdPBqP267CElxarzc4Ji5ZrVZa33CDR2O_tsh_hWh7I5IPq_FlaqgpG4s5eN9GetKxbtGJVG6UmGTyB886-bByUJTL3m1PuJ_DKnIcTLUBr4x-x45yn9QQ1NdA2uKXpt9FQJk31chxzZdcPwbRNWPNbQqJzXK6K8GZPqtwOUgoi8beXLtzKgUqZea3V_uWOnWr1pi9v6HNTQOKImh0SJEiA31XHs-B5q80w7Zmvg0NuqcEclJwl1OSMXR1kwSpAvInS1xnPW1zlvchxRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ربات انسان‌نمای جدید شرکت چینی یونی‌تری روبوتیک که با نام «سوپرمن» معرفی شده، تنها چند روز پس از انتشار تصاویر توانایی‌هایش، با یک برخورد شدید در آزمایش سرعت خبرساز شده است.
یونی‌تری روز ۱۷ اوت اعلام کرد این نمونه آزمایشی که طی کمی بیش از سه ماه توسعه یافته، توانسته به سرعت ۱۲٫۶۶ متر بر ثانیه، معادل حدود ۴۵٫۶ کیلومتر در ساعت برسد؛ رقمی که اندکی بالاتر از برآورد اوج سرعت یوسین بولت در دوی ۱۰۰ متر است. این شرکت همچنین مدعی شده «سوپرمن» قادر است از حالت ایستاده تا ارتفاع دو متر بپرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/104276" target="_blank">📅 09:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104275">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0af9a107.mp4?token=DaIHoC8kyUn_vbg8ICFHpESczSTdTquud9Ckh3h_td3-H2LR2PvECkATfWQzdieGBdz7Jbjve1tSVXPdCLN5nxgd2ITIFlSeF7oohTc7_R0NjTP4VoRQIHE8yH7FcUhi5YWY031cFy1nc1d2r4rME-BPqFs9UP1DY2SbYqH8vrG_M3jcBRmkxaTJvOetqpddcgx9-Z1JmnMtFFyQKCn_ok5cdYtEHg1ulmh3xhAoFpVxi19I-48yjNSB78kAb_O0D_bd-cSBuIvAagPLtxMjmUNM9As-WHFwvsZr_50K05vuXrIUpGtHWiE-_B16xFCPnfH-M8gNflbSZdbAB63_-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0af9a107.mp4?token=DaIHoC8kyUn_vbg8ICFHpESczSTdTquud9Ckh3h_td3-H2LR2PvECkATfWQzdieGBdz7Jbjve1tSVXPdCLN5nxgd2ITIFlSeF7oohTc7_R0NjTP4VoRQIHE8yH7FcUhi5YWY031cFy1nc1d2r4rME-BPqFs9UP1DY2SbYqH8vrG_M3jcBRmkxaTJvOetqpddcgx9-Z1JmnMtFFyQKCn_ok5cdYtEHg1ulmh3xhAoFpVxi19I-48yjNSB78kAb_O0D_bd-cSBuIvAagPLtxMjmUNM9As-WHFwvsZr_50K05vuXrIUpGtHWiE-_B16xFCPnfH-M8gNflbSZdbAB63_-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادارای پرسپولیس خطاب به هوادار روشن‌دل: علی‌پروین برو دیگهههههه
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/104275" target="_blank">📅 09:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104274">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzFlBqSV24oitn0aLLRaQX22yFxeyIOL2R114A_zF-vf0wAFlyKybkExSZwOmCrYuPnBN4678bXQAtqF96THHSx1KeTyJSITPab3ZSJxDPH4NTCe-Sd2aqe_4EU_BbM3vAr3thF2IQkZvYk_XiKy5KBGSZnIOFtCI3HbF6bqVArzWeEZBSGw1dGwj6xFY4IxiCYmFP5aSBjl2h_RMW9mJqqUtgGO12aHJa4MBrpV24Uah6HpFvPI3lFxdO6WNerJKzxxsdP-5GmMMUUNWpZ_mEWSF-V-jlSEeEKL4wnimuaZA4L3Gp2eFbgaRtqLsF5bhg7HuhgrmtkX4oENA7vPdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#
فوووووری
از رومانو: ساوینیو وینگر سیتی به تاتنهام با رقم ۷۵ میلیون پوند!
HERE WE GO
✅
✅
✅
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/104274" target="_blank">📅 02:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104273">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2e63463aa.mp4?token=McXiqyziTqn9peC7jCM75RGEs2nSThlYJ9cHc5eo-5LXpwrW5vLqDAmbmBD2fv3Z8qgmFtIg49SD3YolE65DJvmfNSXVCJApVhwszzkz72BG8Tdv1LeRzLY0wYgBC1Uq2Vh4IAxlvEzyEqOpc-8TxUe2ioFPujxjbBCTbblfWAM8nv--eNWWRIDv7KxyQVXQ0KlYqT_GM6elrAlOvhJlfrTsb3g-55ElinbZZWGnvB1iO4wAFxLQjEzKjFuY6W-HWpdBnEdsSMBAmZW_n8fNixXQshcesnJReDwoS46kxIWXD7Vr4_4lTC2oC4sNMEBtNuxjrwAtbMB-F0jgQoSPIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2e63463aa.mp4?token=McXiqyziTqn9peC7jCM75RGEs2nSThlYJ9cHc5eo-5LXpwrW5vLqDAmbmBD2fv3Z8qgmFtIg49SD3YolE65DJvmfNSXVCJApVhwszzkz72BG8Tdv1LeRzLY0wYgBC1Uq2Vh4IAxlvEzyEqOpc-8TxUe2ioFPujxjbBCTbblfWAM8nv--eNWWRIDv7KxyQVXQ0KlYqT_GM6elrAlOvhJlfrTsb3g-55ElinbZZWGnvB1iO4wAFxLQjEzKjFuY6W-HWpdBnEdsSMBAmZW_n8fNixXQshcesnJReDwoS46kxIWXD7Vr4_4lTC2oC4sNMEBtNuxjrwAtbMB-F0jgQoSPIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
😳
حسن‌روشن پیشکسوت استقلال : ساپینتو آدم کصکشی بود
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/104273" target="_blank">📅 01:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104272">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22d167412a.mp4?token=G31-TuIG9xHbCuE9awQwtdH4lX2EwWyEETU5mbDknkBxC98KuEsOfHYekSOsoXqaK_7n4FrZcwd2_yLL3LBz0bRIYUkF_f2gVCjiQ5KTJ5NEwGIWZL2xqlrxvRbdWoOtiBOfyO51shOpXPnTw4LazqwKwOgalmtph5fDrXHiF4JYe0T-H3zqzAJMa8uNnlgC_F8nGmWfFIMxbQZ6WbpwEs_l-KOTxQ3IJa-JkqfJK1g-oUgQCQ8rovYhL7KKLMIOsXDWj32Ylp7UlAxzGkp9ZOLxQTuQSRP0ly-SW4PAr5gIwDLX_gHDNbGOxol4ws5PEUBauBuQys-isb9pnZE37A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22d167412a.mp4?token=G31-TuIG9xHbCuE9awQwtdH4lX2EwWyEETU5mbDknkBxC98KuEsOfHYekSOsoXqaK_7n4FrZcwd2_yLL3LBz0bRIYUkF_f2gVCjiQ5KTJ5NEwGIWZL2xqlrxvRbdWoOtiBOfyO51shOpXPnTw4LazqwKwOgalmtph5fDrXHiF4JYe0T-H3zqzAJMa8uNnlgC_F8nGmWfFIMxbQZ6WbpwEs_l-KOTxQ3IJa-JkqfJK1g-oUgQCQ8rovYhL7KKLMIOsXDWj32Ylp7UlAxzGkp9ZOLxQTuQSRP0ly-SW4PAr5gIwDLX_gHDNbGOxol4ws5PEUBauBuQys-isb9pnZE37A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
😍
🇪🇸
قشنگ مشخصه یامال دلش بچه میخواد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/104272" target="_blank">📅 01:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104271">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c7cda8f28.mp4?token=suATpfRruCDhRNvTMefX3HcU_YZf04fJiSU7Xha6RqBnuD5N5qdaBSmj3tRlYE6dzHxg8hgMqlfAMArlcy1K9e1GoReBj_hqeX0vpvhuWePz-hy6aDxB5pwJkZK80gmAYBmaa6HKR-EZzMEHdk5ToOG-naAp2YjNisGkg0oc8DWqNZCdME45onfDKS2Yuz4sXk9V47ULiXs0sPyl3hhiPV4l7pl36kSZRKHfErvUrN3jyUicI6yBNShSrBkT_SKqaCZxY_Mf5uJxpxBONEaS1iYSoGQT4pCRZ8R6E1mKnzAnBJhb4EXU7yi4ayvocxkpy1xHeJSNUE9l5lnfKmEqaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c7cda8f28.mp4?token=suATpfRruCDhRNvTMefX3HcU_YZf04fJiSU7Xha6RqBnuD5N5qdaBSmj3tRlYE6dzHxg8hgMqlfAMArlcy1K9e1GoReBj_hqeX0vpvhuWePz-hy6aDxB5pwJkZK80gmAYBmaa6HKR-EZzMEHdk5ToOG-naAp2YjNisGkg0oc8DWqNZCdME45onfDKS2Yuz4sXk9V47ULiXs0sPyl3hhiPV4l7pl36kSZRKHfErvUrN3jyUicI6yBNShSrBkT_SKqaCZxY_Mf5uJxpxBONEaS1iYSoGQT4pCRZ8R6E1mKnzAnBJhb4EXU7yi4ayvocxkpy1xHeJSNUE9l5lnfKmEqaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😳
نحوه سوپر مخ‌زدن شیرازیا وسط بازی فجر
لاشی تو ورزشگاه با گوشی قلب میفرسته واسه جایگاه بانوان از اون ورم یه دختر قلب میفرسته واسش
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/104271" target="_blank">📅 00:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104270">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">هایلایت بازی الفیحا 0-3 الهلال با گزارش شایان آقایی پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/104270" target="_blank">📅 00:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104269">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fdf2dd188.mp4?token=a3UnHMdg0Jnoo82GqX3Smko2sqlemqvWVDZZ7ruy_RJTvqm_ktsr72buYeAHtD3LDh3tKldLzFOrKzNi92e9Fl41skzBQygLmN2Z45WqnvIn31oib-cxtvJU7AzHQV9lF-bRduwWD8I9mR5fKm98R3zwuhtGo04qZ6SX21OAJHnRVQojBXl1hdaw6VZw0u0NFSw-TXhaCbJlAjbHEyFzJy8Z_tC7CnjWijuHzNms1G664BQIU0Z5MsGjXHQqt4mTmuy7fYvgV3VGrShTbGiLakYHPOZ2nUZn_XEM4vGT_7VlgU55JY1eodL_oHLYUYVEQWzclzulAJRt1ATjeGP-qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fdf2dd188.mp4?token=a3UnHMdg0Jnoo82GqX3Smko2sqlemqvWVDZZ7ruy_RJTvqm_ktsr72buYeAHtD3LDh3tKldLzFOrKzNi92e9Fl41skzBQygLmN2Z45WqnvIn31oib-cxtvJU7AzHQV9lF-bRduwWD8I9mR5fKm98R3zwuhtGo04qZ6SX21OAJHnRVQojBXl1hdaw6VZw0u0NFSw-TXhaCbJlAjbHEyFzJy8Z_tC7CnjWijuHzNms1G664BQIU0Z5MsGjXHQqt4mTmuy7fYvgV3VGrShTbGiLakYHPOZ2nUZn_XEM4vGT_7VlgU55JY1eodL_oHLYUYVEQWzclzulAJRt1ATjeGP-qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
قالیباف اوایل تیرماه: اگر به سوئیس نمی‌ رفتم، ۱۲ میلیارد دلار ایران آزاد نمی‌شد
❌
همتی، دیشب: یک دلار هم از پول‌های بلوکه‌ شده ایران آزاد نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/104269" target="_blank">📅 00:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104266">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1230d6d53d.mp4?token=LonatazTt-SO2JM_FwKCMCVs_-5YI-c14iPLf6evdccytnijNpmEiyeRsZuh-sR_iftBk_cDOZOf2glHWwYkwL6BHv-4dcrLDiuov5iQgeRwEW_Rss7XVke8ctEXiwV2HJL9R0wWJ7cmspiWoB0T4bAJBOfwNO-d_t4OErSJqYaGSPN6_mv3fUWACmhpTrfo9X8xKWrzq5idzykGklufl_2WsnG1mcOhrvTDaqBka2Yb4GRXF_SDW3nygIp667D8rkNZ_Hgkv20DEeCPxYaSO-5vPUXKiTJ-JvcWLtlP2UUdy3Q5VTNltA-F-47Z5VIP2eyegO5y23ECaLheqJflyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1230d6d53d.mp4?token=LonatazTt-SO2JM_FwKCMCVs_-5YI-c14iPLf6evdccytnijNpmEiyeRsZuh-sR_iftBk_cDOZOf2glHWwYkwL6BHv-4dcrLDiuov5iQgeRwEW_Rss7XVke8ctEXiwV2HJL9R0wWJ7cmspiWoB0T4bAJBOfwNO-d_t4OErSJqYaGSPN6_mv3fUWACmhpTrfo9X8xKWrzq5idzykGklufl_2WsnG1mcOhrvTDaqBka2Yb4GRXF_SDW3nygIp667D8rkNZ_Hgkv20DEeCPxYaSO-5vPUXKiTJ-JvcWLtlP2UUdy3Q5VTNltA-F-47Z5VIP2eyegO5y23ECaLheqJflyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
💙
نقل قول مهم میثاقی از کمیته انضباطی: دوستان اعلام کرده اند چون فسخ قرارداد یاسر آسانی در سازمان لیگ ثبت نشده است بنابر قوانین داخلی هیچ مشکلی برای بازی کردن ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/104266" target="_blank">📅 00:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104265">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoZJq_wHT9c6VdjSLst9mDFItjzOQA0oRsaKqUcCI0wNR3WVzaaRWOoaAjUA7qmLUpoju0ZlVjech5p8M5HflDQUnyz2qkOU6u_TF1jbPrkn9D57cPk0-3G3gW-UXpHP9NbeDdfbxbgSa2i2WieGzYu0yOGT2QpZ6OWCYAmGV_dBm2qXnJbm2LnNVmACACECpxQhe8TYEWK41rG0fIMyzltFdsFoPIU0k3gcijOE_Um5HffQFGqOwGLgvapy3hBWExB8ZvOz1_e5-2OkVRzsrztPcO64KgZ8JeD7xrdw8e7rspLjqYlxgiA-UYVNkplIzETF6oyGhL2nXvVTrT_Obw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
مارکا: متئو آلمانی اکنون به لندن رفته تا کارهای انتقال نیکولاس جکسون به اتلتیکو مادرید رو نهایی کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/104265" target="_blank">📅 00:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104264">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e2e98ceda.mp4?token=o9F-1_Ia1-UAHyLL91z6Eppz4r9yaQEEhRJ7i8FXnVSQPCmo9ylMVP7VtfZG6jOjEYuJ2re0xQjoUEw0dp1u2m5Vu2A-3yw_T9POKmxmVgyCcntvPU_YyJHqyfhyHpmjF9qsvQXCArFU583DdfDTnRg7Uun-F5HnY9LvL-DjcR3ikCsSbHcle8y1SYNfG48GD4xv-VV0r0yOc6LS7lIWX4n9nFTAseBDW9ob6PQLLVDy0ssDCaTXuibsA0EGWeksM2fGuqJh9UxYxdyDPjuXRl60t9ft_nswmQJUcrFLDQ-52Y1uC6kuKa8OD_kmwrfP_VRxuVDSyNMgrl8tPRYUaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e2e98ceda.mp4?token=o9F-1_Ia1-UAHyLL91z6Eppz4r9yaQEEhRJ7i8FXnVSQPCmo9ylMVP7VtfZG6jOjEYuJ2re0xQjoUEw0dp1u2m5Vu2A-3yw_T9POKmxmVgyCcntvPU_YyJHqyfhyHpmjF9qsvQXCArFU583DdfDTnRg7Uun-F5HnY9LvL-DjcR3ikCsSbHcle8y1SYNfG48GD4xv-VV0r0yOc6LS7lIWX4n9nFTAseBDW9ob6PQLLVDy0ssDCaTXuibsA0EGWeksM2fGuqJh9UxYxdyDPjuXRl60t9ft_nswmQJUcrFLDQ-52Y1uC6kuKa8OD_kmwrfP_VRxuVDSyNMgrl8tPRYUaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
حجت الله بهمنی سخنگوی سازمان لیگ: یاسر آسانی یک قرارداد 2 ساله با باشگاه استقلال دارد و در سازمان لیگ هم ثبت شده است و درحال گذراندن آن است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/104264" target="_blank">📅 00:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104262">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1449e6d243.mp4?token=Fo8KYE3uas5V2LKQNFo1bM3JbrlCxdEOWrWx9LdKFwgV2YLNOXPNzIslacKmoF31CJOCWvV3dQ7qXWVv8RQel2K0G02Q6Oc4ha0ze2Gvb3CXgvVtH24lCVL1eWDSgPkXE_IEVdAJbvr-NYIyQm3L32AduaPYLVX3oRvVLTkFHpw_1rDWLL6TQYT0o-RlamdozqWdcECcNn1UCFer3jZqhS3kqZ39tvsw8igM3xa9QcYO0zkHHk2LNudl64g5OgZcR7I2M0RM7WFeCn0pRE_3uxPx2fEG638ZCC4UQi4ApVua-prBGkkJHh9YXOgCB_33OE1knZ-9kmv8VwxkiiTbeUD-1Spg46wmpDKMBT268ycf5Tvy5PjkA2wZD_SAgrsy_PnZ07va_e850pBEzJE58IOXel_JRA-gky949pF2xOZCQiHpdMToXnn6OQYsj2GI1hG9FfesuPiDcLPmBaHiBcEeFN6mTIntLQOgr7gNV8g87KGIgupEy5KE00UnXkhXMVpJqpkwlWCZLgZIsA4UC3ecvk61fUdjKxqntwUdmFH7flin945KGAdec3WbyCOE71fIVbNZs9hAuP33eKe4V57HqgHAWHoWMY0PTlgvhpZ8JaAOTEZmYGeH2_7RDCu99kvrjQfpWubdGMOYqO65PFyUeRLAeh9V75hiisImnow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1449e6d243.mp4?token=Fo8KYE3uas5V2LKQNFo1bM3JbrlCxdEOWrWx9LdKFwgV2YLNOXPNzIslacKmoF31CJOCWvV3dQ7qXWVv8RQel2K0G02Q6Oc4ha0ze2Gvb3CXgvVtH24lCVL1eWDSgPkXE_IEVdAJbvr-NYIyQm3L32AduaPYLVX3oRvVLTkFHpw_1rDWLL6TQYT0o-RlamdozqWdcECcNn1UCFer3jZqhS3kqZ39tvsw8igM3xa9QcYO0zkHHk2LNudl64g5OgZcR7I2M0RM7WFeCn0pRE_3uxPx2fEG638ZCC4UQi4ApVua-prBGkkJHh9YXOgCB_33OE1knZ-9kmv8VwxkiiTbeUD-1Spg46wmpDKMBT268ycf5Tvy5PjkA2wZD_SAgrsy_PnZ07va_e850pBEzJE58IOXel_JRA-gky949pF2xOZCQiHpdMToXnn6OQYsj2GI1hG9FfesuPiDcLPmBaHiBcEeFN6mTIntLQOgr7gNV8g87KGIgupEy5KE00UnXkhXMVpJqpkwlWCZLgZIsA4UC3ecvk61fUdjKxqntwUdmFH7flin945KGAdec3WbyCOE71fIVbNZs9hAuP33eKe4V57HqgHAWHoWMY0PTlgvhpZ8JaAOTEZmYGeH2_7RDCu99kvrjQfpWubdGMOYqO65PFyUeRLAeh9V75hiisImnow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
بهمنی: استقلال به عنوان میزبان دربی، ۹۰ درصد گنجایش ورزشگاه را در اختیار خواهد داشت
!
استقلال میزبان است و ۹۰ درصد ورزشگاه در دربی در اختیار استقلال خواهد بود/ استقلال ۹۰ درصد گنجایش ورزشگاه را در اختیار خواهد داشت و بازی برگشت، این موضوع برعکس خواهد بود/ تمام تلاشمان را می‌کنیم تا دربی با قانون ۹۰ به ۱۰ برگزار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/104262" target="_blank">📅 00:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104261">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4bac35957.mp4?token=Gz00KqZZTnYDf63llkmUp3F_5MlXI4uMK_yYPaXI0_29SvJ5HN6i9pHMdmWmOLT8OLu7anZdOrQDuJyvwQAdVWOF0G401L9bUSntL7cPg9gw673xiC8JR_FzpGoQcTlRmEJdl7cpoC2irHMsbbeK33wFKD7HgkrOdV_n09VZb0SG_hNPhNsVA-aO6uW7SWWsrvn8WaAQgwX0J3vnZ61PG8BMfiTDRpfw_shiKeyUhjWIy811fKp1qhGLBNppm5qD_Y7V9wR_WY0rL2WgiyhHZ67nKBjed0LRr4NwFzLyMVS0YMaXGyMWVkPsINa4FtsSxAAKgXU5031GJC3yfjNdd8Ab0vJBDKm6DQY8pRrfS9l1CHXROq08iFMlFarQ5z7yeUIj04BlZxXez04f-BDU6_aSasp5N5IBUxc0vlCRwbeVKvL6l5yWXCyElrBUvy_Zn64eG2Zl1dkRL-oU574e227W_CfZxH_ULEq93JFSzHlco9MRdMBIJibaxjcRRtkEwCk3nu3f2ktv4GicbjZQNCeoDm-Ekx4hGFAceik0iT7qg2xDXmMd2FsjedaQ2CmGMJX3KSEZj2hu8TB-JvhczSrTIdl-xswnMghACpiP7FwObjQOTXznnQkxzCXqVW8dIzj6Yq201ZPbMptPZ9bfQBhcX7LPWJTAJInz4lpjE0U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4bac35957.mp4?token=Gz00KqZZTnYDf63llkmUp3F_5MlXI4uMK_yYPaXI0_29SvJ5HN6i9pHMdmWmOLT8OLu7anZdOrQDuJyvwQAdVWOF0G401L9bUSntL7cPg9gw673xiC8JR_FzpGoQcTlRmEJdl7cpoC2irHMsbbeK33wFKD7HgkrOdV_n09VZb0SG_hNPhNsVA-aO6uW7SWWsrvn8WaAQgwX0J3vnZ61PG8BMfiTDRpfw_shiKeyUhjWIy811fKp1qhGLBNppm5qD_Y7V9wR_WY0rL2WgiyhHZ67nKBjed0LRr4NwFzLyMVS0YMaXGyMWVkPsINa4FtsSxAAKgXU5031GJC3yfjNdd8Ab0vJBDKm6DQY8pRrfS9l1CHXROq08iFMlFarQ5z7yeUIj04BlZxXez04f-BDU6_aSasp5N5IBUxc0vlCRwbeVKvL6l5yWXCyElrBUvy_Zn64eG2Zl1dkRL-oU574e227W_CfZxH_ULEq93JFSzHlco9MRdMBIJibaxjcRRtkEwCk3nu3f2ktv4GicbjZQNCeoDm-Ekx4hGFAceik0iT7qg2xDXmMd2FsjedaQ2CmGMJX3KSEZj2hu8TB-JvhczSrTIdl-xswnMghACpiP7FwObjQOTXznnQkxzCXqVW8dIzj6Yq201ZPbMptPZ9bfQBhcX7LPWJTAJInz4lpjE0U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇮🇷
هواداران ملوان در بازی دیشب تیمشون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/104261" target="_blank">📅 22:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104260">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzlvmfZnWo7PVJTePOawAKP1TIRmAknLy4Jv3PbBTkr8UUpE8-gweR_kWj4uz2eYqEE9N8FYbyD26IomG8RB-Y6GpeInnR2spSTwLTGLdUog9kIaKKVweLTxjAz_THyzjOrqogdFQAzEvEqob9kVoYYkdSLVBSZZUKAdoWbF2sdFLDx3lFKYORADTMYyq-qHQFUHm4UfVEwb7Ks4HHWHjfgQtr5eWaQif2cEj-5L2P2seYL7sxsXdORwMtUUpGvhaHPT24xXq8Dd19CRm68LOxxBXAzi3xzPtO9ko33egdt7AEwCI94RMIacTY_QPNOKumNnUWGIqrHfOmq36nWkvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
نادر محمدی(منجنیق) و هوادارانش در روسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/104260" target="_blank">📅 22:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104259">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tL9HE5jInkYkhno5gAoaQn2lwH1F6pjI05cqct-i_7l0ujsI4dJEmVvFrAdF-3Nf1BKx8EBnobP5EE0EQU0lWv0N0QTbQj8c4UXdyRLChngF3P3RVp-532KkN7eTNG-PUQ5B50tCSiQajsbgJGpi44P7_Nh62NzJchnA6NFya9N7ujy6SbUTve0FaX3RHq2KDdj5TvugjdiJNjKZbJAS62MJNzKcB9_aYtpqsQfTSBXeMu2vhdDp7Abd-HIY6sZhXu3CTbNSwOiOcu951GXqDFy9fn1qxQAASjRSaDG2pJ0bKIwexNc4gnmI23pIlA_xSI-17WmgS8aTKRDL9HUGaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
خط هجوم بارسلونا بعد جذب احتمالی لائوتارو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/104259" target="_blank">📅 21:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104258">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gItvu2bThTOkHyPH4S9OH3T3-jAFNBbDuiXlmDkJcmPGsbfNBzBIE9lzK4NdkFdoYefqqfhvcilo6j8QFDoyke1vluZyM0RgH_VemR-xrqmnzfHakCeh-sdIgYcsJY4ADpHNTxGo5NRpDBq0eBCTaBnINqCxuFBJcVort9ybSM375Eg6BZ3b4h6LaFY8_P2OQUVdCdsbsOdosDykP-zX9GdCtUJcIFxreNT4DhzUCAwsUs1to9Aj5gnZg7TyTPRJmnxKruSjJjmeLYa18Rc9rxWtxzELjqSjnErWC_QdLS5H4-L1wiNkYggbYRFdY-poRwUiksa272V6-tx16haCCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
رونالدو پس از دو بازی غیبت در لیست فرداشب النصر برای بازی الریاض قرار میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/104258" target="_blank">📅 21:17 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104257">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a24abd1333.mp4?token=rY0SGkH34OqtQPqw43xK_5dWowIotX-dQUtzNCaBwOdmpcQ8zdVu7fguPD8PmoQhdDuFCgKo8zJxA1blqWHaMK88o8dn8Fvst08RE0Um_FGUAE-AjhJ57BMJhyiTjSUVtj8qHYskY0zROTzSZJIImVFMZJVdiyklR4aqcWYR_ctQAILXsSNR9R_PjVsBx-kH7FEJQ8DQu08rtwFi4O_DIc3aT2D5SsKYkwwgimEcy1wtQKl3f_4k5KcZTJQC8CHgNoS7fjsjggytgl05s4IBQDaatM_ohLSUkw_i2Eyq2Px-7iiEQOrGO_rZoxyjuII3mUIoUT7dKMd8MKO2pQR2-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a24abd1333.mp4?token=rY0SGkH34OqtQPqw43xK_5dWowIotX-dQUtzNCaBwOdmpcQ8zdVu7fguPD8PmoQhdDuFCgKo8zJxA1blqWHaMK88o8dn8Fvst08RE0Um_FGUAE-AjhJ57BMJhyiTjSUVtj8qHYskY0zROTzSZJIImVFMZJVdiyklR4aqcWYR_ctQAILXsSNR9R_PjVsBx-kH7FEJQ8DQu08rtwFi4O_DIc3aT2D5SsKYkwwgimEcy1wtQKl3f_4k5KcZTJQC8CHgNoS7fjsjggytgl05s4IBQDaatM_ohLSUkw_i2Eyq2Px-7iiEQOrGO_rZoxyjuII3mUIoUT7dKMd8MKO2pQR2-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
‼️
هیجان‌زده شدن یک نفر در خرم‌آباد از شعار بزن که خوب می‌زنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/104257" target="_blank">📅 21:11 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104256">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfUcQ_ugaDb9oKeNtmbvIdTu_Apm9QyISKAL_uFfZHYwvJJBoGZ4iRY_IOd0qZCPn5dzYXUbZZgXD661lI_73OyOuwpRnjFtQft_UQ2OgOKffADs1XHeoQf7VY6pU3wyWKluSq7ZdgiNQk51W-vajmnEmvwdzqvYLnv90cUrNG2_Up6TdEkV4EnAWUXUJgDTQbRBskjVFSfWxsdjC4rIx5QatYs9lyNheP9Bcz7IdkwpUJGrDr7dAnQUYaCCtXBMVtE5w-J9AC1M5HwyxnP9DX_Z9pReWwHBRtFGcY88FCF_St9WRnDgMn0gTWpb0N8LER8ztmzByZ--PfBgV3rY8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🏆
آخرین‌رده‌بندی توپ‌طلا تا پایان ماه آگوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/104256" target="_blank">📅 20:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104255">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLpMi7SCK7-1tzwOS2FaCF5FXbXsZFTGhNAEfviE0fCFsoPvAG0_CqnVtVg24I6z5Kel8GJK_RiJMWdbidfbM3TA0wvIg4j34XtunuqOKF3vup1N-L-5I7E2TvSNcnb5un8WcgkZIG0Tvu7goo4TEJGzXZflgKMd88XbF6BEGiN1ASgPpwYt-XOqauCQb080vynyFeyO5k8jB_pKbclfrh6qYyuI-6pXf2Pz6cXZIVIV9Vy3Of-ci7JBPdEwIz8dNGd2553chI0EiAZFulk-YVp0Kz_f2NMt5qm_uf-qSMNYzCs6AM6VBqDynmdSH1zQbPErh6InpRMkZW0EpbiFxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفته دوم لالیگا اسپانیا
🇪🇸
رایو وایکانو
🆚
آلاوز
🇪🇸
🗓
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی در بتگرام
🔼
با بالاترین ضرایب پیش‌بینی
💵
واریز و برداشت ارزی و ریالی
❗️
💰
۲۰٪ بونوس روی بالاترین واریز روزانه
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104255" target="_blank">📅 20:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104254">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815fa09b1e.mp4?token=iBQB3uNDixd_Pyzb-GPjb9wQEUMmB4VoNbz7Vd8OsCOdpwtYZeKK2b-CMmW23btisiLAVLosnwUncW-7heuL_2R1zaaUbBoL8gGFIk_01zfgoQc9cDWZiLIqRnIou-6xkPvPyzHvaxNmE9ftOdRypvfkPKGgm3Nmg95AyQ51WsuJPrSMxLLrPhArKCm_HMcwJi3jG3NKd1y2ll8cHiMf5PDAqde3Dy_8W6IWFWcgFilfH1AglSCxpb4tBsWOx-nUbs-oAZumr8UPZ8pXWG6cwS0y5PId-3T4PJR49SUL3w-yLl7MMHaBcpKzMAbxz0nHJXh2VSsJGoylIRoVe2qkxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815fa09b1e.mp4?token=iBQB3uNDixd_Pyzb-GPjb9wQEUMmB4VoNbz7Vd8OsCOdpwtYZeKK2b-CMmW23btisiLAVLosnwUncW-7heuL_2R1zaaUbBoL8gGFIk_01zfgoQc9cDWZiLIqRnIou-6xkPvPyzHvaxNmE9ftOdRypvfkPKGgm3Nmg95AyQ51WsuJPrSMxLLrPhArKCm_HMcwJi3jG3NKd1y2ll8cHiMf5PDAqde3Dy_8W6IWFWcgFilfH1AglSCxpb4tBsWOx-nUbs-oAZumr8UPZ8pXWG6cwS0y5PId-3T4PJR49SUL3w-yLl7MMHaBcpKzMAbxz0nHJXh2VSsJGoylIRoVe2qkxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
لیواکوویچ سنگربان احتمالی جدید بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104254" target="_blank">📅 20:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104253">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05150752d5.mp4?token=gmm2M3XcPIdlOgjGw21RXVdE_Nm1FgaVenbZbHBdbzbwwc3jA-g3SmrauMfe-SH3OOUF1jhRgLqGN5ieLM2jfDIbBifJ_j02NOFCAbJvG7ByMLaFv-6XWYtolHpSVv5yFo8CFoesLvJ86gYfiOQ8tCRbnv2vJx8ADfN-3shizQyoJISu4KZUKUI581_n_-zzpzKe2ta__aPL1OZL7vLqIcGBw1m7KlS0WjLdOh9BUf_IX_WR0s4X33guRRpU0frCwlb7Np8k-V7TYimyzfyaKL62VvkyMn4lfv-Df-2_OufHmVDOTzWQTuq0TvY6betLjh10epeXJCeGzv1HdeSe6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05150752d5.mp4?token=gmm2M3XcPIdlOgjGw21RXVdE_Nm1FgaVenbZbHBdbzbwwc3jA-g3SmrauMfe-SH3OOUF1jhRgLqGN5ieLM2jfDIbBifJ_j02NOFCAbJvG7ByMLaFv-6XWYtolHpSVv5yFo8CFoesLvJ86gYfiOQ8tCRbnv2vJx8ADfN-3shizQyoJISu4KZUKUI581_n_-zzpzKe2ta__aPL1OZL7vLqIcGBw1m7KlS0WjLdOh9BUf_IX_WR0s4X33guRRpU0frCwlb7Np8k-V7TYimyzfyaKL62VvkyMn4lfv-Df-2_OufHmVDOTzWQTuq0TvY6betLjh10epeXJCeGzv1HdeSe6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇹🇷
ایزاک کارنی، یک هواداری که به خاطر علاقه به محمد صلاح و باشگاه لیورپول شناخته می‌شود، اخیراً در صفحه اینستاگرام خود، پیامی برای محمد صلاح منتشر کرد و برای او آرزوی موفقیت کرد. او به شهر ترابزون سفر کرد و با محمد صلاح دیدار کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104253" target="_blank">📅 20:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104252">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/338c9ad977.mp4?token=AUSXA7Ei2dPqnfm2WqTnKohOJ0yacGrgR0UQSgZctnERym7kYJitAlKWCAFCAUltFiMElyljkQNdx68DGEL9zUcdwotW1NVjBYusz13epeJirdgE3xXSAxQCi8OgNb9FIn4YPaBsi28jhZsMs5ep-zPSJstA1thtRXW-eok5G11el11rXeu2RWGXvm7H8T5XnW0rt42OFTi1WnKUSIGotTfQqA_WaIwV0HmelMs7cGwLFVkmUAhsaxcNAkcVb1xqyn0eDEBOP0kP9zesM44lUGFEe4EQ1v6XqczH7-nMO4ficQeyjPt7aNXndJcyFZxzEytU4e-SmxmyPeTs026KLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/338c9ad977.mp4?token=AUSXA7Ei2dPqnfm2WqTnKohOJ0yacGrgR0UQSgZctnERym7kYJitAlKWCAFCAUltFiMElyljkQNdx68DGEL9zUcdwotW1NVjBYusz13epeJirdgE3xXSAxQCi8OgNb9FIn4YPaBsi28jhZsMs5ep-zPSJstA1thtRXW-eok5G11el11rXeu2RWGXvm7H8T5XnW0rt42OFTi1WnKUSIGotTfQqA_WaIwV0HmelMs7cGwLFVkmUAhsaxcNAkcVb1xqyn0eDEBOP0kP9zesM44lUGFEe4EQ1v6XqczH7-nMO4ficQeyjPt7aNXndJcyFZxzEytU4e-SmxmyPeTs026KLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از گل مرادمند به پرسپولیس در فینال جام حذفی سال ۱۴۰۲، هزاران استقلالی در ورزشگاه آزادی اشک شوق ریختن که جاویدنام مهرداد مشتاقی هم بین اونا بود. روحت شاد و تولدت در آسمان‌ها مبارک بزرگمرد ایران
💙
🖤
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/104252" target="_blank">📅 20:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104247">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j3KmTdALLF0yfkldfgnAww0QaC2PDxG5HFnD_6nO4tIjSvIge1yUF5PxDvfQQ-MFf-XtBBTockZaOiGOePPRuFPmpLabuuyvjTjV6DjqkzbEdXK3Kd7DfWXOxPtNqj7Erzl2oa3nbLELlhRppAAibaks_Fyjs2dtnhIrVo2iA1uuHcF3NgD1KOf1ThsXd0IgDAgKK7ElZlOr3jmr-IQpTT62pJD754fv4r8iyfJm5JeriCPZ8Jk5nn2f6hAO6Y0QOeG9pXdJILpaNIerQCNdIfA5k7U7PyIb5f3UWSaf4ssSFpmK9_MTk8ozXIO7Dgj8S5gzldI9ZJH-suLf5Oqn8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AyaVIsQoAanIRXNlpjrqbQB38kzzefqxvqIVYUHpfv25RlM1zdM4RuNWOlZMftjgd7jQ5rSax0YOWLvwzhPRKoSrsiNVaiHLOYrErwo-TkNCw_5VH5AQqhWNYHMeyR_ua4fGVVg725_BClxxCGGterC2SXvlBmAjCYwq6RhS32rs9lWjpazUbBKdHPyd2YqlrD44bQTwuDzkFA14VDVCVAXOhM7d1CluaPALFhJIYodt11dTmffLNifcOPsgqaDSTBfGh1PAqULBmUSXGgmW16A7uhcNCrewanr_TKOOVQLmhYdp-e6DGcrZh9KLUJP2NM1RFFgY-1TyW4-hnwa2Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Py4Xms_4fpNvmTvoa-x2jlLle0xBhj0HZ9qudmNhoXLh7ktj42a-lTpHTpVuKvy8op7RLp-lPBqaBoDTf5LpHYGY_sT4QS4uhNAUmWFF3IS35EjlNcJTjm1ai4Zj1F7-c08jqgq0-imuu-YGU-5JR4vfg0mtYy5ObEmeCUcgb0ufQF9lJii7xHqJW51ACbcKDhCqOM01Iyt9GPr7KvVueJPaVwK-yTSr_pI_eo9Uzuu_dVvY2F_b0O8jajxTRW9ASpMmgSdqusve4yDZC4fb_NvXbnsW3MBdTeTc1icHMjfik363OF9r6oWDN4RdGbLeFzh0EKPSsHkU1rEjR5h_FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JzCfTe4jDtS2q00ku4QQfKg8_5JSdVdZSAr4BO9BgAW6u8TqDKhn-WeOEGx1skuLSaYyFTbc9kgxE4d_XruWYZjljbdJEt9RFyXkeQ_jwJqZ0O12hv4NBrkj19rfBpc8_HsmzTF36MiJrUo4slzpWTQsX8uifKcHI46Ts9BZOvAuKmAm4xhvbR-FdikbqziTMLMcce1KUUjN6pdvBu0fIwbUc0HCfQcTelbmSk0Cvg4luZRVpJN5UCUEKwhHUudvzjtZQO9gW3JZCoS4CDQ8wOUgN5KwIIeFFZv1qN94rL5xKqrz_q0edmP5vj0EbNBiDGaqauOxCSClh7Cx7AVpPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vft-ynYrcCXYerkuou56zEt06ACHB9iA1bkNWIJGgicFgJUL14prvvAoCQj6p90Yz8dC7iVHcTP0JbMkxZn8eUChj3VONTULNaWDs2KAeayxg0aLTWqeiDdcqPfYRwBtHEyZEzN9e-oi-DLsKz_F4BOXiG5s7C-UDr1L3eAKqH7RbbkZNTu10D7mhvrPk-YAVob542Vgllx88DdKJUEgcZfulaNDimHwpdalQP-JIGMYc_1Vfq8sv9rcS3W75sBzX2tuh9VOwTtp4UyTYCroG8Brmj-rAgEWOEjyZ6WIP-WvgRaZpFsjOpTeJgK8nbK4QtvV7T4V4m9GV7EZB_q_bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🇮🇷
هوادار پرسپولیس در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104247" target="_blank">📅 19:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104246">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJ0dpufHrYn0d21-qXMFHx7GKtPebnu8EnAlQKUefm_oq00cTk28jgCQIPUCLqxjbqvr-YfPTCgIdfERuFU-aV8lbsU_CuUtM1h2NwByJMWGA7HeMUj7wJrEbmRgJd_Lw1NCIGWzefPuyZw2NsdK7dhsmJ3RcfiE-s2y6wRkvruglBwVaG1Yzs8qSvmWIhe_w1-Ca3uX07fw6NXPo24Oih-Nvi93vzOgNn5ecDo2P4DRGOXXGhD2ohMQyPJCAiEinEVMm-gWQIGi6o5oNxiLh-Z9SYc1zkLhaXRzc8eoNQRUDHqh5kHTp92yNol6VzP-vpT8jefl5yivxTiWxCdL6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
😍
پست
خداحافظی منیر الحدادی به هواداران استقلال
ممنونم استقلال!
💙
همیشه همه‌چیز آن‌طور که تصور می‌کنیم پیش نمی‌رود. شرایط باعث شد دوران حضورم در اینجا زودتر از چیزی که دوست داشتم به پایان برسد؛ اما با خودم خاطرات و چیزهایی می‌برم که کلمات قادر به بیانشان نیستند.
از هم‌تیمی‌هایم، کادر فنی و اجرایی و همه اعضای باشگاه که از همان روز اول کاری کردند احساس کنم در خانه خودم هستم، تشکر می‌کنم. همچنین تشکر ویژه‌ای از هواداران دارم؛ به‌خاطر تمام محبت و احترامی که همیشه به من نشان دادید.
امیدوارم روزی دوباره مسیرمان به هم برسد. با قلبی سرشار می‌روم و می‌دانم که این فصل از زندگی‌ام همیشه جایگاه ویژه‌ای در قلبم خواهد داشت.
تا دیداری دوباره
💙
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/104246" target="_blank">📅 19:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104245">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fa83936b8.mp4?token=NBdo_NdC-cCanwg4jqRS_rprcM9LvoKAePiHsq5D8PQMOaZteOrO1yG4ZRwwC1ERaT1ql12W66CFhK3HbF_PbUBzIczDbaSgDkC0hhBesSQAo1ioMRLXDs893UrugIbg7GrFH25CbXu_psno95DVo_JyJm00qkAKgbHuq8v_5knrpOK3NaHZhZNnrVksb0__HzjpeuUBOMixBkXI5beB9PfPzRVam7bMJ-sd20HGN7nZtyHCyS-GHk1BIF65DooLzxQ1A9ljXp2nrfzzmz9FKOWIK2YvAtjGmpoTT_PazWsB9H5vYkUidJJfmCBb0BOSUpaxzkLDHpZYIAKhETlR9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fa83936b8.mp4?token=NBdo_NdC-cCanwg4jqRS_rprcM9LvoKAePiHsq5D8PQMOaZteOrO1yG4ZRwwC1ERaT1ql12W66CFhK3HbF_PbUBzIczDbaSgDkC0hhBesSQAo1ioMRLXDs893UrugIbg7GrFH25CbXu_psno95DVo_JyJm00qkAKgbHuq8v_5knrpOK3NaHZhZNnrVksb0__HzjpeuUBOMixBkXI5beB9PfPzRVam7bMJ-sd20HGN7nZtyHCyS-GHk1BIF65DooLzxQ1A9ljXp2nrfzzmz9FKOWIK2YvAtjGmpoTT_PazWsB9H5vYkUidJJfmCBb0BOSUpaxzkLDHpZYIAKhETlR9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
عملکرد ریدمان لامین‌یامال در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/104245" target="_blank">📅 19:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104244">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Po-i2HLM2n9FnBgzDAGm2J-nUUXK0_I7YUcksUAo0qnvBatQ7O3iQv8GJUvUuBnmID4G1lXNVp1GqRZ9O-or7hPqugPycSwBWmVUDckQVe9cjdt2UTqX_edAQ6p-yo6PUiodO7WgKTql8YWP8RSKGuBh5JD3kFaWgW_ZEgTPRULdmm8d1Y7X9lg3xI9ve9x-PgNPDJQdCdbX35kW8kfkl4d4B35NVWpqrkdFFvFY7m1Dumxxunzrl0DarNkj8ECQWF0gZLccrVemhY5n28RQaoHOt7xCxKf8OIGSnAwjO6nUEgOLrK_iueIqsqluR-aUEJbZrnYyfEiICFaloUS-tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
#فوووووری
؛ یکی از مدیران الوحده امارات در گفتگویی با رسانه الریاضیه این کشور اعلام کرد که رقم رضایت‌نامه محمد قربانی برای فروش این بازیکن به‌ پرسپولیس و سایر تیم‌های ایرانی و خارجی رقم 1.1 میلیون دلار است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/104244" target="_blank">📅 19:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104243">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRjtDSUFDpIwhM8UT7z5AiBeD6q_laf1nqKMsK8N80rVIM6P752o9zd_71Z2Y_f14U8rjJw1cehOXo7t0a8KAwYmFqXXiQJLZPcudvtEIXwDpPorW92iZOZLiw9rUAHpjKD2h4IT0Q5DMp028DKxP09PCy_soMUGwUUPW874m3qAK-jWKRYD2L43QO53e1ouVqeGoZKDWaGd6jvY0ouh7ozRqCx6HlUiz13LzqygGrPcCxcHk-1o86uSEHDk5Cfa5lo-MmR2OnTkfQPq-q0JCmgC5OGQgMbLzkHRSWWsuvdYP_VdfqTqZ4ieSj9HBzk8G4_ox1rLJEwRgyK4KDLbjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
پرسپولیس امروز در دیداری تدارکاتی به مصاف آریو اسلامشهر رفت و با نتیجه ۴ بر ۲ به پایان رسید.
⚽️
گلزنان پرسپولیس: امیرحسین محمودی ('۳۲)، مهدی تیکدری ('۷۹ پنالتی)، پوریا شهرابادی ('۸۷)، محمدحسین صادقی ('۹۲)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/104243" target="_blank">📅 18:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104242">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hAzp9umokueALS0pZp80SCMAcOqXmFIv1yaZT6ksVgXqStrOLDFObLCVOSHjgt2p3yNamSbkWV3t4e1x41WcwiB7MF9O2eX1Lr8cxS2i-dcLKuB3SN1VZZSYKDcPzmn66bDkx5vSBdce1Ei4we14oWUy4Jm43DdIAqDZzC_GlM1mqR8dTq8lzImk5YA6WL-5Jjy62uTDOgj4F-5TlmI06UumKeIVciz1FPrUF7lDkyNi73khy0QP_rtzqWdGAVLl7hpe_gpIjXDZ2akx443_qKm7Ex0cZPecf-9RaJExvXB8dnlntE6r-d8YESVytj50SbdBNa8nIeF8pBp8xC8pcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇮🇹
رومانو: تا این‌لحظه اینتر هیچ پیشنهادی از سوی بارسلونا برای جذب لائوتارو مارتینز دریافت نکرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/104242" target="_blank">📅 18:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104241">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8c825309.mp4?token=H3AnTp3ANm5vZjwkEnzeHxIx2AyJd2CQbqr97MZkUCZ2Ukp_0IVqBoO7M0_JnEMLZbL3jUo_LQ6hS-YmuzSBLe7k3udYyaD1Saqn-rNjDiPeckXga3YH7ce5WAWkkjNkWWPuZsd4FuCr-VztyuGFVkQyovQ8UV1fG7gnUJf4MTlBkfpb1XzARYh8E_cv5Z5m_e7T6KDqPb9psaBZqD2OZ31Zv80912VwIx8oqZ-08W5GKPYNqwptporzeJnAQlNXWpYt8NLnqGJ3wd5Cqz11bnE1vK1VdqptvlC3v95xcg4KjSGewhaoR11Lm3tizVE9Z-WZjcAMvQu147SeKOaDqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8c825309.mp4?token=H3AnTp3ANm5vZjwkEnzeHxIx2AyJd2CQbqr97MZkUCZ2Ukp_0IVqBoO7M0_JnEMLZbL3jUo_LQ6hS-YmuzSBLe7k3udYyaD1Saqn-rNjDiPeckXga3YH7ce5WAWkkjNkWWPuZsd4FuCr-VztyuGFVkQyovQ8UV1fG7gnUJf4MTlBkfpb1XzARYh8E_cv5Z5m_e7T6KDqPb9psaBZqD2OZ31Zv80912VwIx8oqZ-08W5GKPYNqwptporzeJnAQlNXWpYt8NLnqGJ3wd5Cqz11bnE1vK1VdqptvlC3v95xcg4KjSGewhaoR11Lm3tizVE9Z-WZjcAMvQu147SeKOaDqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
یه پسر دانشجوی ۲۱ ساله آمریکایی، به کمک هوش مصنوعی، یه مدل اونلی فنز به اسم «مایا» درست کرده و تونسته تو یه ماه اخیر ازش ۴۳ هزار دلار(۸ میلیارد) درآمد داشته باشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/104241" target="_blank">📅 18:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104240">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59287a8b90.mp4?token=NQow1MTqDKjqmrNA1hVYrgxJur-JtDkwWsMeva_pnoZUJ6kJQo6CyN8aNL_pW-2lA4bSpKGZGPCxIadpaHDG6dKbxJcK0RkF_Ogx-QeYNnFbBFrzyv6mvVzwkOmHX5-S9rex5wvbynJgDSGeMzch5So9xF1PfX5bt12VhB4BJnYaSctEhOoBRcXdevNhK-QOS0DZTHhGdJ8LOIKfjxxH6GYAj1y_4f40QoX8tfzzYqBTOpCDdl3DwC2MmUOYT13ZmQJRuzjyOjLiODn6va3wQKYUel62cDs0kckjCknLqXEeFqEKBJTRnh3zVNRBOAuYvzQ5t7PHQHtgRbjaNjuQbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59287a8b90.mp4?token=NQow1MTqDKjqmrNA1hVYrgxJur-JtDkwWsMeva_pnoZUJ6kJQo6CyN8aNL_pW-2lA4bSpKGZGPCxIadpaHDG6dKbxJcK0RkF_Ogx-QeYNnFbBFrzyv6mvVzwkOmHX5-S9rex5wvbynJgDSGeMzch5So9xF1PfX5bt12VhB4BJnYaSctEhOoBRcXdevNhK-QOS0DZTHhGdJ8LOIKfjxxH6GYAj1y_4f40QoX8tfzzYqBTOpCDdl3DwC2MmUOYT13ZmQJRuzjyOjLiODn6va3wQKYUel62cDs0kckjCknLqXEeFqEKBJTRnh3zVNRBOAuYvzQ5t7PHQHtgRbjaNjuQbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ماشین جدید رضا گلزار، تنها رولز رویس کولینان منصوری ایران به ارزش 200 میلیارد تومن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/104240" target="_blank">📅 18:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104239">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6c9d46d94.mp4?token=b1qSizEWd35vmwACzyLCC68zU0P43aAp1d2s8F5LJCxMJkpm3sw1FpZ8kKya9BFT-xXQut9zu3s4q41LAvurNINVyTvz1b06oloQC-3B8MqJz4HfQAAXl5F1dY4_WfkT3GaNPPFOf_PmO3Ba6hbByBho5c55HFIgVtuvTFhVBNT2Y6CokO_qKCzQfU6LrOCrUWoln0YCskTTIs0qef60YtFbj841V6ZQijopUIoYm79_tpcYXmxRE3ikzIdZXz1bVRl-MwBQbjuwRTHkAVnyPW6C_7_TU7-x1bp_AUOAMtm1eWcjdPWy9nAN68B7xVFvVRWDg-b1r9zRPeGBcezNMTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6c9d46d94.mp4?token=b1qSizEWd35vmwACzyLCC68zU0P43aAp1d2s8F5LJCxMJkpm3sw1FpZ8kKya9BFT-xXQut9zu3s4q41LAvurNINVyTvz1b06oloQC-3B8MqJz4HfQAAXl5F1dY4_WfkT3GaNPPFOf_PmO3Ba6hbByBho5c55HFIgVtuvTFhVBNT2Y6CokO_qKCzQfU6LrOCrUWoln0YCskTTIs0qef60YtFbj841V6ZQijopUIoYm79_tpcYXmxRE3ikzIdZXz1bVRl-MwBQbjuwRTHkAVnyPW6C_7_TU7-x1bp_AUOAMtm1eWcjdPWy9nAN68B7xVFvVRWDg-b1r9zRPeGBcezNMTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🎙
افشاگری ملیکا پارسادوست شاکی پرونده پژمان‌جمشیدی از اتفاقاتی که در این پرونده افتاد و منجر به شکایتش از پژمان جمشیدی شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/104239" target="_blank">📅 17:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104238">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcca79f2bb.mp4?token=mAo7n__UhLz9JUhHnc4_JOjyLIMmCsoO7agwG7u9BiDCBN9Z_KGJY-fklILAvtQZqwXug6kMTnBR2JRJkc9Wav6kpVbVvIbCMxd10UgN_d-drsSnNNgHDSbUtrgGC-H00IH5TDbjtmiRXePdvI4imezCz9o4QUpwb8Qk7mQqXaEgeXTdSE0wpaQOpwrMfONJUTkcwaESRX9foSnuC_f1nnDq_ON6Q2XZ8NDSbeWKHA5onyumJJ9XTBbE6gR82dm6XbFxOusKLpvE4MKX0cRPB-L7C1e6vND_x3tM4xbneTvddsE1rCBlxT0MIL34Zpj_DKAOvgYI6XCknIUiv-R3PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcca79f2bb.mp4?token=mAo7n__UhLz9JUhHnc4_JOjyLIMmCsoO7agwG7u9BiDCBN9Z_KGJY-fklILAvtQZqwXug6kMTnBR2JRJkc9Wav6kpVbVvIbCMxd10UgN_d-drsSnNNgHDSbUtrgGC-H00IH5TDbjtmiRXePdvI4imezCz9o4QUpwb8Qk7mQqXaEgeXTdSE0wpaQOpwrMfONJUTkcwaESRX9foSnuC_f1nnDq_ON6Q2XZ8NDSbeWKHA5onyumJJ9XTBbE6gR82dm6XbFxOusKLpvE4MKX0cRPB-L7C1e6vND_x3tM4xbneTvddsE1rCBlxT0MIL34Zpj_DKAOvgYI6XCknIUiv-R3PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سمی‌ترین سرود یک‌تیم در مسابقات محلی مملکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/104238" target="_blank">📅 17:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104237">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">💎
میدونستین تو ویپاری
با شارژ بالاتر از ۱۰۰ دلار ۲۰٪ بیشتر حسابتون شارژ میشه
✅
🎁
برای مبالغ بالاتر از ده هزار دلار بیمه شرطبندی ۳۵٪ داره‌
و مبالغ بالاتر از هزار دلار بیمه ۱۵٪ داره یعنی در صورت باخت مبالغ به حسابتون‌ دوباره واریز میشه.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/104237" target="_blank">📅 17:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104236">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari (3).apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/104236" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر WEPARI
😀
😃
😄
😁
🔥
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 120% اولین واریز
‼️
🔥
بونوس برای 4 واریز اول
‼️
⚽️
بونوس ورزشی هر دوشنبه و چهار شنبه
‼️
🎁
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :
Gift
🔥
دانلود مستقیم اپلیکشن اندروید
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
📌
آموزش نصب برای IOS
g29
✔
https://t.me/WePariFarsi</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/104236" target="_blank">📅 17:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104235">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
آخرین وضعیت استادیوم آزادی: آذرماه جدیدترین تاریخ اعلامی برای بازگشایی این استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/104235" target="_blank">📅 17:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104234">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1b80d7014.mp4?token=c-MtuAvP-ss6S-ClMgM9ujC_RTnAy_SgXSjEIP4P6WQv3bJqgoSBF54HQuRLCN2eU1x_n3PySl8Id5w_p86PpdOLZJjq959sMcySue0V4ol32TDAdv7bdcA2aid_C8v1wN5inxFKPe9voCBNIiWAxFL2Kk6VVWJihG-1u_oYAQ8smb91NBDBbrhMws3n9zsZ-ltsxmMNShyVWwJRnao26StIA1G1H9xV4lPeFwtONUOFvvxtb8Hk8fvUXclfmMyzg1t3BTSJLQiqpHwAWNaBYofFaro6nhs_pcdr6PqnNZ94SLBP0GL8EsXRiC_xt2WwCPsmkCOp9A-62al81vRFmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1b80d7014.mp4?token=c-MtuAvP-ss6S-ClMgM9ujC_RTnAy_SgXSjEIP4P6WQv3bJqgoSBF54HQuRLCN2eU1x_n3PySl8Id5w_p86PpdOLZJjq959sMcySue0V4ol32TDAdv7bdcA2aid_C8v1wN5inxFKPe9voCBNIiWAxFL2Kk6VVWJihG-1u_oYAQ8smb91NBDBbrhMws3n9zsZ-ltsxmMNShyVWwJRnao26StIA1G1H9xV4lPeFwtONUOFvvxtb8Hk8fvUXclfmMyzg1t3BTSJLQiqpHwAWNaBYofFaro6nhs_pcdr6PqnNZ94SLBP0GL8EsXRiC_xt2WwCPsmkCOp9A-62al81vRFmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇸
مراسم خواستگاری دیشب کف نیوکمپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/104234" target="_blank">📅 16:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104233">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85f3ef3446.mp4?token=G08BDLftpBx7wV9BR1jaUPusnV1KmMpgbA_PnwLNUcWwcOPRM3qCViBoVtKZZS9d3h3UTH_ZdAIUpEe7KeBHhEU5oT3NPKAqs6VF9wnUOsH_ezgB43bJ9XyRmNGx33wW88TI4wFuv_V7XLwOykDwnADwI5hP6gnIIlZE1a7qAoDO9QpujiVd-s3qhur25FY4nwCTv8OBhUa0G43SUCjQmOy1RX1to45mu5dHZjLKT2k7Bu0fbQNT1xzQirf9C43B4LwUc27r5EMuD271o8zu6q527f3Cj9NSmwmyDHRKqeheow2jrDigjvvLv599aQySb_ytvaZSrc070lUNpy-9jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85f3ef3446.mp4?token=G08BDLftpBx7wV9BR1jaUPusnV1KmMpgbA_PnwLNUcWwcOPRM3qCViBoVtKZZS9d3h3UTH_ZdAIUpEe7KeBHhEU5oT3NPKAqs6VF9wnUOsH_ezgB43bJ9XyRmNGx33wW88TI4wFuv_V7XLwOykDwnADwI5hP6gnIIlZE1a7qAoDO9QpujiVd-s3qhur25FY4nwCTv8OBhUa0G43SUCjQmOy1RX1to45mu5dHZjLKT2k7Bu0fbQNT1xzQirf9C43B4LwUc27r5EMuD271o8zu6q527f3Cj9NSmwmyDHRKqeheow2jrDigjvvLv599aQySb_ytvaZSrc070lUNpy-9jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
نحوه استقبال از تیجانی‌ریندرز توسط القادسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/104233" target="_blank">📅 16:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104232">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e04b7c878.mp4?token=iSRQeQH0lbR6OCzDmTT2SdobSWkcKm19RCj7xfJf_NQebeqGKOv5ynkffaCdhTIHHREo1G88Mgws2z0R-mp8lLI0JzPl7HM_CgS3XK49xpSd97SBD8RLLk-Yrj4rCOrqjtGeB0BxkW-E82FHRXhoAxi5ux0uJmxCcY9VLEj0lsh9-vWrZ_dDwJlc2VWBO7i2GMtQv8wPeX16r3S0XayCZCZfmMSa0VBy9zazHsFsys2fKUcaCEgnilY5-xj6_Gposp-p1N_4ynSjEijPQLmBWY4zCruU-v_otwskaABp4EjexcxDAmaG_QvpkaC1Q3BVRk-Mki2o7WjoXzjBGVn8xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e04b7c878.mp4?token=iSRQeQH0lbR6OCzDmTT2SdobSWkcKm19RCj7xfJf_NQebeqGKOv5ynkffaCdhTIHHREo1G88Mgws2z0R-mp8lLI0JzPl7HM_CgS3XK49xpSd97SBD8RLLk-Yrj4rCOrqjtGeB0BxkW-E82FHRXhoAxi5ux0uJmxCcY9VLEj0lsh9-vWrZ_dDwJlc2VWBO7i2GMtQv8wPeX16r3S0XayCZCZfmMSa0VBy9zazHsFsys2fKUcaCEgnilY5-xj6_Gposp-p1N_4ynSjEijPQLmBWY4zCruU-v_otwskaABp4EjexcxDAmaG_QvpkaC1Q3BVRk-Mki2o7WjoXzjBGVn8xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
▶️
خاطره بامزه امیرحسین اصلانیان از اسطوره فوتبال ایران احمدرضا عابدزاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/104232" target="_blank">📅 16:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104231">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ea3bf7fa1.mp4?token=smhc-L0RKjvm6p0RpP02mLgVKoQ9udFFxPYZY59H-WuYaJD3POIr3SiB3T0yQ_QALPMk1uzVXqhJn2upxEUhsDwcGTUzfe76EXB2wY1hf4cUzw_1_mic5Lvrnp4s2Mlfr7aZHdMgAubCHaPPDOUkNmhwpybhj10FvSOA5MTcCtZS6kuWk_si7Z5cUjLxtgW0PTJV1Sl5z-VQzb8YI5SomkozyH75PK-sSUyP4wz64bgOPpUQP6zCZbhTrUbMw6m7fCnbHDp9NElzthltru6u4xmZYUGL8fgzpUX8sz1Kg7beUw433qOQhYdtfO1zId7cFszz92JJDPx8lmRUW-CGig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ea3bf7fa1.mp4?token=smhc-L0RKjvm6p0RpP02mLgVKoQ9udFFxPYZY59H-WuYaJD3POIr3SiB3T0yQ_QALPMk1uzVXqhJn2upxEUhsDwcGTUzfe76EXB2wY1hf4cUzw_1_mic5Lvrnp4s2Mlfr7aZHdMgAubCHaPPDOUkNmhwpybhj10FvSOA5MTcCtZS6kuWk_si7Z5cUjLxtgW0PTJV1Sl5z-VQzb8YI5SomkozyH75PK-sSUyP4wz64bgOPpUQP6zCZbhTrUbMw6m7fCnbHDp9NElzthltru6u4xmZYUGL8fgzpUX8sz1Kg7beUw433qOQhYdtfO1zId7cFszz92JJDPx8lmRUW-CGig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
وقتی میخوای بیانیه یک باشگاه را یک نفس در ۳۰ ثانیه بخونی
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/104231" target="_blank">📅 15:40 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
