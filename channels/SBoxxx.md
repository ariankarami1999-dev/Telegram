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
<img src="https://cdn4.telesco.pe/file/C7lThbsenk-A65iE9hy_oz97jZFpsoIAICZC1UX1oXnaGizaJFzmrJI7EXgIhNDC_QUMtQ3JRHtxUodXRpu9TaH0Ifjcpfc0q6mESPPTtd5U-UHb7XsZwwDTUDMLhNWtwL7rjqGX-fWz4s1xiwtw5-7PlbsqVZpKFutpB9-POOipGUkR5dC4D9yUKUnM_lqn3kAZb-IHX4jWeLYEX8UoV9av7VchIHrQIuHRSqLLaGY3yEIZsGeAxrToQepRkRmEyU-zJoHj8V1gr8Sf3ihMZiA5izlcUHK5rPNra3oQ1_ELx2lTmgdxNe_6GUE_-gyUzPOg_p-1nYrrJ9ke0G977A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.5K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 19:05:58</div>
<hr>

<div class="tg-post" id="msg-19284">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hE-gvdWCTfjgzO4m5h6xEZyIlU2U4jz-2KwqT8tWpAPdYYvS702piJmcrDChmgLqq4TlDCuqRzDhlLasaMO9Q22KxRbpPozloThGcAeqiwWkoHaTn_WE9CmtW6Emx5WI0cDzLKSrEBEIkCN_-BP9HS4z3pIwyiHC9iFINf724w_9h2XaTk6w5ibIJ9svXeSruHnX2OXkX6vs5aTVEMUSCHrXiUCTaSomth1RE52h38CO3sWLt-ZUWdWdpZ6hh5PzTPoY_ZlJuWsNodGRn5N7LVoV1T0dD66NxqWc9f5LvLD0JqiJK5TK28WodpGUaneNvluwvOROYSbTJ2uQAImJ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استالین و بریا!
بریا رییس سازمان اطلاعاتی شوروی در حین جنگ جهانی دوم بود که هم حمله هیتلر را به درستی خبر داد و هم با سرقت علمی از آمریکایی ها، برنامه تسلیحات هسته ای روسها را به نتیجه رساند.
جالب اینکه او پس از مرگ استالین در سال 1953 اعدام شد!
#تاریخ</div>
<div class="tg-footer">👁️ 312 · <a href="https://t.me/SBoxxx/19284" target="_blank">📅 19:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19282">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نتانیاهو به فاکس‌نیوز:
جنگ زمانی پایان می‌یابد که نظام ایران سقوط کند یا چنان تضعیف شود که ضرورت پایان دادن به برنامه هسته‌ای خود را درک کند.</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SBoxxx/19282" target="_blank">📅 18:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19281">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95d5b002cb.mp4?token=uYh4yezWmwZmZLp0WQOUg7CaUpmCPrYVpfgiH4qaUzZf_0tVkXxdtbB3_yVBLAi-mXDOYGCYab748uoQvYdvRCj6hEzwU38iVtEsCO9lTvC1ekflbdFF5Y8aG1amduVkWE3W3tmrhHk3uwuFp6Be10kCn7_xq21vkUxczqMj7CL-1BC6D1EtITPjkuFumaefBNyrcp-_RAtfH8fs4D162kxp4Dufn8GQYhcPlq-YwE0HWtSx8s7fnda3XUjQfjaa2Ys2yX2lFx_OQr4KLLK0euwnPk5Yox0n-KmYlAshvNVeYZDkqnkF3-Nr2YVhJQ4EVW3PMUcWdnqy_SsX5JhkbBJ5tl9gDMpPdEMH6cCA5wrJQMbadqi4iPQD7VPhLWQ0RdoqkaHuV6cXDX0kcvsSbtKJnFvoY34htgSxbByoerKXtNAEH88mc5C80UY_s8wTo9fa9BvpApBzXgQ8GWgQt8vxrdq_szT_xJhCvInn0vyP5tF-IcM1DDke4I3PYI9TMVuv4AOQ0gU3iyUim1EGNMnXT0vC8HdwqHZ5J0tPx0_42xmeknySXNmaOWwmwI2ViBe0lnlEVlTlBo5TCRvCggqPyhX4ifo6ronZHhAxzwZG7VSFH5xkQCyPFjLWWmWL1QURxp0dgAeNY7S-mZEqDyIVfg_9CGZY8q-NynBx3RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95d5b002cb.mp4?token=uYh4yezWmwZmZLp0WQOUg7CaUpmCPrYVpfgiH4qaUzZf_0tVkXxdtbB3_yVBLAi-mXDOYGCYab748uoQvYdvRCj6hEzwU38iVtEsCO9lTvC1ekflbdFF5Y8aG1amduVkWE3W3tmrhHk3uwuFp6Be10kCn7_xq21vkUxczqMj7CL-1BC6D1EtITPjkuFumaefBNyrcp-_RAtfH8fs4D162kxp4Dufn8GQYhcPlq-YwE0HWtSx8s7fnda3XUjQfjaa2Ys2yX2lFx_OQr4KLLK0euwnPk5Yox0n-KmYlAshvNVeYZDkqnkF3-Nr2YVhJQ4EVW3PMUcWdnqy_SsX5JhkbBJ5tl9gDMpPdEMH6cCA5wrJQMbadqi4iPQD7VPhLWQ0RdoqkaHuV6cXDX0kcvsSbtKJnFvoY34htgSxbByoerKXtNAEH88mc5C80UY_s8wTo9fa9BvpApBzXgQ8GWgQt8vxrdq_szT_xJhCvInn0vyP5tF-IcM1DDke4I3PYI9TMVuv4AOQ0gU3iyUim1EGNMnXT0vC8HdwqHZ5J0tPx0_42xmeknySXNmaOWwmwI2ViBe0lnlEVlTlBo5TCRvCggqPyhX4ifo6ronZHhAxzwZG7VSFH5xkQCyPFjLWWmWL1QURxp0dgAeNY7S-mZEqDyIVfg_9CGZY8q-NynBx3RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی جالب است؛  از 6 کشوری که شدیدترین بحران های انرژی را تجربه می کنند، 4 کشور در منطقه ددخیز خواهرمیانه هستند و 3 تایشان (سودان، سوریه و یمن) در ژنده پارچه ای که به عنوان پرچم رسمی معرفی کرده اند، رنگ های نجس و نحس پان عربیسم (سیاه، سفید و سرخ) دارند</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/19281" target="_blank">📅 16:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19280">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بیانیه وزارت خارجه در محکومیت حمله اوکراین به شناور ایرانی در دریای کاسپین!</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SBoxxx/19280" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19279">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">با این وضعیت می‌شود فهمید چرا ناگهانی تصمیم به دوبل کردن قیمت بنزین گرفته اند.  وقتی عرضه سقوط کند، کاهش تقاضا با جهش قیمت یک گزینه است.</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SBoxxx/19279" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19278">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQxLxCn28CglUl5Bx30sT2Qp4Sz9mZ57cY8Y-82e1ZCh2HFvGMV-aB3CnSGs2MpmlT2XkVa0PJAnEFsO-a0Lyv3Gc8ChPC1_1svr-DHJjj33yRRtJgO-0sh4kZumBJvVsSWVLlgZ29zlWqaZVGWBwkKvJajyK78c_6SfPbGt8aGBhbAD1y2wKgYAMNXPRbYonr4QChzAzk6zNvUOIaSm08JvhwcJkJhaoxOQEKLFPfLhEamzoUMkUz8L70Rp_d4bTLHjyApyRPiGG37Z8LJqF6FoxP20vvsDgoYekXNghKuRXTzYIFGD_u6M6L4d8smpr25ULhOokdoXVVRuDFi6rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روس‌ها نوعا عادت دارند انتقامهایشان بی رحمانه ، مبهم، نامتقارن و شکنجه مانند باشد.</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SBoxxx/19278" target="_blank">📅 14:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19277">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">روس‌ها نوعا عادت دارند انتقامهایشان بی رحمانه ، مبهم، نامتقارن و شکنجه مانند باشد.</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SBoxxx/19277" target="_blank">📅 14:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19276">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وقوع دومین حادثه دریایی در دریای سرخ
سازمان عملیات تجارت دریایی انگلیس از دریافت گزارش حمله به یک نفتکش در آب‌های نزدیک سواحل یمن خبر داد.</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SBoxxx/19276" target="_blank">📅 14:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19275">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">برای نخستین بار در جهان!  کشف قله تنگه هرمز توسط اژدهای بندر</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SBoxxx/19275" target="_blank">📅 14:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19274">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/312e3c4284.mp4?token=g2iu6wKDWGO4fbdQGVDBCrq_d152mMtRAaASvvF0Hlbc57jIUPalE4OmlmGz-4i4nnSFQTaUfH-2mqEiRbsXSi3gx45R0fIsorjWQIrX-XuiXJmh_vf6ggeJ5pah8mJAvEQvvatXmKCNjtVz0B98j6Et7etxqsPax8FqDPWmgBdlHMQn6QxwXrliQkVKJFMpAx6E_oa3oLLvHRmLhwjbZDEqOl5rpFRMOyeeOJcBXOYbciuARrongON8-Nqu1ksBaZkoJLPhPugFKRwkb5H0BwgX0tJklO6Nti9iYyWtX02p9G-FzOj7TRE1ZrSFXKyl4QR00xdBumSMBewxpHeYXJkoby5lGVesOzJZKTMSOFfG9RJTCdt60AX0wrKzwrwDDaDsXvjbLRDNWhqWOsKDgTNjQ0OB6T7-4eTTQpp-FKplFmlWY_8ibhE8X15GkcL41QM4YBvMvpLGDL_9Hpnbu3rgz1ZAT0vCvmk9c9VUrqxOQIzq_p2b3rQuUpQNrsn73jEnrYRFU72nV0eoarbVvNUdYW9EnVq-mExxxdV95nxxIcR1oIXO5E4tFE5BCpqKcDdXphHR16nHF8Uwtm9TnF0AXeBh9yj9X-8sk1_4P-OdKimoZxqN4HvuYRqaqhrTkjd-eLIByCi_xw62mCSfx75nuVF_7gK-c1h45xox460" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/312e3c4284.mp4?token=g2iu6wKDWGO4fbdQGVDBCrq_d152mMtRAaASvvF0Hlbc57jIUPalE4OmlmGz-4i4nnSFQTaUfH-2mqEiRbsXSi3gx45R0fIsorjWQIrX-XuiXJmh_vf6ggeJ5pah8mJAvEQvvatXmKCNjtVz0B98j6Et7etxqsPax8FqDPWmgBdlHMQn6QxwXrliQkVKJFMpAx6E_oa3oLLvHRmLhwjbZDEqOl5rpFRMOyeeOJcBXOYbciuARrongON8-Nqu1ksBaZkoJLPhPugFKRwkb5H0BwgX0tJklO6Nti9iYyWtX02p9G-FzOj7TRE1ZrSFXKyl4QR00xdBumSMBewxpHeYXJkoby5lGVesOzJZKTMSOFfG9RJTCdt60AX0wrKzwrwDDaDsXvjbLRDNWhqWOsKDgTNjQ0OB6T7-4eTTQpp-FKplFmlWY_8ibhE8X15GkcL41QM4YBvMvpLGDL_9Hpnbu3rgz1ZAT0vCvmk9c9VUrqxOQIzq_p2b3rQuUpQNrsn73jEnrYRFU72nV0eoarbVvNUdYW9EnVq-mExxxdV95nxxIcR1oIXO5E4tFE5BCpqKcDdXphHR16nHF8Uwtm9TnF0AXeBh9yj9X-8sk1_4P-OdKimoZxqN4HvuYRqaqhrTkjd-eLIByCi_xw62mCSfx75nuVF_7gK-c1h45xox460" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای نخستین بار در جهان!
کشف قله تنگه هرمز توسط اژدهای بندر</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/19274" target="_blank">📅 13:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19273">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">در حالی که اساساً مزیت پهپادها در کوچکی و سطح  مقطع کم راداری آن است، ترکها رفته اند یک پهپاد غول پیکر (همین آکینچی) ساخته اند که ابعادش دو برابر یک فیل است!  طولش 20 متر و عرضش 12.3 متر و 5.5 تن هم وزن دارد!  قیمت آن هم بسیار گزاف بوده و بین 5 تا 6 میلیون…</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/19273" target="_blank">📅 13:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19272">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEZWklkfg_pXgvDbic8NOLHmyalzsqxA3gdqPNXukHTSMV80EsEfGLWZZ1LMILpERPCKEi4fmckemxbGoc4diNSLvZO1lYLk7k-q-aYHsJxO0bNtLucFes6TkYTgCUGw9N_MhXUBY36TU58G0rPf898-Gf_ZUcOy97hNQctjEEY0uhEj608VKk6jAQWHJ9UqTJUB0N4-dtz3_W9vrkPDxrcOn8QfvgaqubFcV3zGTJ6bTj2C3cQpSgUfIevzmT8mm29mujOIw39nJVJ2Jc0_12epc54pwukXC2LFQIs2EmaMgSzVuUVPH3bEJt5WaHA00xV-3sOWZ8TUhFze9dj-mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میزان بالای مهمات پدافند موشکی آمریکایی ها در جنگ با ایران</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/19272" target="_blank">📅 13:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19271">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6066f7963b.mp4?token=sCy0Dr3GwaUXKDTsnsD-if9Y5udAnbkRf6o3cwTAnYyuBP26xwTYIXFkSGf6YxyO0dgEAU3DU_-wwr_frowr6I-lS2JkpcAjAq02tvYeCIanGK6rd-shfElM94TO5IzVExc0_z7MSjolWLXFLw8nIc6_3VXiyM_ovwyIlIci8mUwtTSqgDxuRGUMoHR1DW-f97HKGSYNsZbCM_RY9uAr_t-tuKDAzlr0iCsP030tYyoNc_Ulo0hcNFlpW9Sfg74LuJFm9NUyKTCaWdEF6o4r514P8Yxx7Wrw0kefAXSxSlSqz5qmoA9lO_0Hb_tWIkrpnMdPfd2w09Z8FctGzc4dKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6066f7963b.mp4?token=sCy0Dr3GwaUXKDTsnsD-if9Y5udAnbkRf6o3cwTAnYyuBP26xwTYIXFkSGf6YxyO0dgEAU3DU_-wwr_frowr6I-lS2JkpcAjAq02tvYeCIanGK6rd-shfElM94TO5IzVExc0_z7MSjolWLXFLw8nIc6_3VXiyM_ovwyIlIci8mUwtTSqgDxuRGUMoHR1DW-f97HKGSYNsZbCM_RY9uAr_t-tuKDAzlr0iCsP030tYyoNc_Ulo0hcNFlpW9Sfg74LuJFm9NUyKTCaWdEF6o4r514P8Yxx7Wrw0kefAXSxSlSqz5qmoA9lO_0Hb_tWIkrpnMdPfd2w09Z8FctGzc4dKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران هر روز برایتان یک سورپرایز دارد!
توحش و بربریت یک مشت گوساله در مراسم رونمایی یک یوتوبر ریقو گه دیروز در ایرانمال برگزار شده و ۵۰ هزار نفر در آن شرکت کردند!
حالا بماند که گوشی عستاد را زده اند و دست و پای ش هم شکسته!</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/19271" target="_blank">📅 12:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19270">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGJnVczVbienoLuZmqcZ6iBfFoE26JNJSvZTpQwfLnN1qoQMbbcfNVcQRmnd_8tXybiBREbJU4Sj8ajharhqGH0vPTwIvA7L8Wqu94CEXSp9DNvXVKXbWck2uLYxJQdalLpF6F2aTTZfyapaHgJkUiGrLRpg3-quJMalTolQSeSLJKnI03vxAR0C6Z1OxtqsRojvCwcCfOlHXZZvuNExnPUCVRsSNqzi2ICN8kYaAY-NzbsYrzm8v1_MR0P2c28_QWKveGFGpipF4aETT03gkMOy7AHiqNC0RapeQwYzdPsIKMvA0rO9LBHkdP_AxGJ8ASdlTzbglO6zkRGaQg82EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این منطقه سبز بالای مرزهای کنونی یمن که جیزان نیز در آن قرار دارد، تا سال 1934 متعلق به یمن بود که در پی جنگ آن سال به چنگ سعودی ها افتاد.   هنوز هم برخی ملی گرایان یمنی نسبت به جیزان، عسیر و نجران ادعاهای ارضی دارند و آن سرزمین ها را مال یمن می دانند.  #تاریخ</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/19270" target="_blank">📅 11:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19269">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gksHVEaWdorGcNhz_0pLALq6OJSCaYOQ_dXbwOl--n0AhEfhSj-RmJobm3c0E7cb6YkzE7maF3hl9nat7TW0huOFwVnrD2ynh0-Nd72CO8F8evQqU4qiBAxhkibgutvly0YxjrCBGVrJ3iqR1x9KTrSiDVXb-YxghC0JGQ9dEYEUTIkRXcg-tooxrwvaiJRvIvH4eHv-9ZH5KXuVafk5M-DjDbQk6S6XcCB1XkOOkWAs9kH0fQ6ompZNtv8svNUJYPajHNiGE-kXsaccoZkK6zILSWylpu9JlK0xGP4xQxPatFWHiorQ-P7frMdIfN5wpXomXWh2PkX0s5N_mJcTHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زد و خوردهای 2 روز گذشته حوثی ها و سعودی ها به روایت تصویر</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/19269" target="_blank">📅 11:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19268">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxkzP6wcT5g5Jdnt0eS-sFqZZQPmRhd2IeGLE4SMgbfF5zz2CfUY_qntge07FXder4tPQQrHQ59sGbOLaKPLAdTM_hO1c-Pz22shdlfclf_b7Cz0rusIC30JUrIpvHojaHWVH6425O_9tbIYutdppCo-SfVRNETN1Yd1gwQdsSa78KZrSCZhZOixJTBphxr4o04ev8CvAgp54Sof9ELZVi13Qp1KblLsRI5fdVfzrM7oKNuuFINPEN1Mi34xbnWUxColggrxVp0y3Wgl-27ttKjWxpPRJ9Wjqs6BiAaWtgF0PtNfk4yScSE2m55XS1sCRkV5yLD1swdEPUeicWYYMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زد و خوردهای 2 روز گذشته حوثی ها و سعودی ها به روایت تصویر</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/19268" target="_blank">📅 11:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19267">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بقایی پس از مذاکرات دو روزه ایران و عمان:
مفید بود اما تغییری در وضعیت تنگه هرمز ایجاد نشد</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/19267" target="_blank">📅 11:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19266">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c9dbca0a.mp4?token=g9tfyKWLW1FHOwH3tjQ9vRHYAuMjkRrN85bJJqMhBO3qNpvrsNhPpIKzSE-v_0JTO-nmmqz3ZuAfSnyQ6M_I30-N4jz1hpI0W1a0oEU0UMlFBV6QXEnZTjZtzVhx1_lJ7XrAnUR0NujrKJ9gNiQqnvo3EJ8M-CsOToYClzpd0zW9t9nSqMO2FszMp7rEQwiNYhgpCetUTTCOaAm8fUW_ZEgh65ZnmHV0fZqlmaTvaSwHrSmmaBDYU2mg9eHi6aU4Et3QDLy0isiQAYr0SnyhEPmcOxWOI77htIKDqedEU14dLjKUpFmC6J0BQ3cX8h-Ei6oZ5uu5DM7pF_lt6cNcPQXmcJZqQvJrptrs-NRrGbST3Fwp02r5W0WVqpLlF_xQRoiZgYu7jHy3kNiPPYBCFzoggA1oDasrr4unDDwvSj92fe81iY-9Ln9HCPQsP2CaooO0GWVLrpLqAuXdWpNYYEZg4dEK67EG7_abPwfWpzWpubWOaHeIgK2uk8Gd6UZ1czBfspPW7mwb2HPlTh9GniUaKsUoDTQR_LQ1qv6IEaXX0duXnztSvFTmZgzZOCXTHSK5dtvb-cJrIfaNABdoQUTCibu3PDhk2KXROJp3ttx_FqqCUG4mduvfgDPROLE8ruXFMU7JWay-9NkKpTGrgT6zvhXXsLGHNzB5R9_hRmU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c9dbca0a.mp4?token=g9tfyKWLW1FHOwH3tjQ9vRHYAuMjkRrN85bJJqMhBO3qNpvrsNhPpIKzSE-v_0JTO-nmmqz3ZuAfSnyQ6M_I30-N4jz1hpI0W1a0oEU0UMlFBV6QXEnZTjZtzVhx1_lJ7XrAnUR0NujrKJ9gNiQqnvo3EJ8M-CsOToYClzpd0zW9t9nSqMO2FszMp7rEQwiNYhgpCetUTTCOaAm8fUW_ZEgh65ZnmHV0fZqlmaTvaSwHrSmmaBDYU2mg9eHi6aU4Et3QDLy0isiQAYr0SnyhEPmcOxWOI77htIKDqedEU14dLjKUpFmC6J0BQ3cX8h-Ei6oZ5uu5DM7pF_lt6cNcPQXmcJZqQvJrptrs-NRrGbST3Fwp02r5W0WVqpLlF_xQRoiZgYu7jHy3kNiPPYBCFzoggA1oDasrr4unDDwvSj92fe81iY-9Ln9HCPQsP2CaooO0GWVLrpLqAuXdWpNYYEZg4dEK67EG7_abPwfWpzWpubWOaHeIgK2uk8Gd6UZ1czBfspPW7mwb2HPlTh9GniUaKsUoDTQR_LQ1qv6IEaXX0duXnztSvFTmZgzZOCXTHSK5dtvb-cJrIfaNABdoQUTCibu3PDhk2KXROJp3ttx_FqqCUG4mduvfgDPROLE8ruXFMU7JWay-9NkKpTGrgT6zvhXXsLGHNzB5R9_hRmU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عمومی بودن اطلاعات برخی نقاط حساس نظامی - امنیتی در ایران</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/19266" target="_blank">📅 10:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19265">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پدافند غیرعامل به زبان ساده</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/19265" target="_blank">📅 09:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19264">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFOXeelBIJsQ548jMERltEhOqwbnVA_xJtpcBOTDez15jlR0XQXgu-kcn9hrZwrwU-o5ICtTFJ--qVemWrgTVZVOHQNZUC4xUOLeLGuGYtZm8zk_OBDm3cJtaEdwtlQeFTusbYTNpFqstyREea_EH1NBip7YKvrRjnM0d58fxn37wZau95W8Pv2WXbXfOyja_wiA2OcGmyauNj0wiFZNwyCAcEugqCEmgTmi1YhF1BcBbRjjLerhS1MpehW2hUOuiYYR9vdECnp_OobhVtJZ-gm90hXHRVrMH0xVBw6Re0HpyNnMiWvmX5D3iQ0gbhPLDT0y2BqI90t0r6doVL67Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19264" target="_blank">📅 09:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19263">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نیویورک تایمز:
ترامپ، حداقل فعلاً، برنامه‌هایش برای تشدید قابل توجه تهاجم نظامی آمریکا علیه ایران را به تعویق انداخته است که دلیلش نگرانی‌های ویژه ای است مبنی بر اینکه تشدید درگیری می‌تواند ذخایر رو به کاهش سیستم‌های ضد موشکی پاتریوت و سایر مهمات دفاع هوایی پنتاگون در خاورمیانه را به شدت کاهش دهد.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19263" target="_blank">📅 02:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19262">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">انتشار برخی اخبار تاییدنشده از شنیده شدن صدای انفجاری در بندرعباس</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19262" target="_blank">📅 00:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19261">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">آشنایی با پهپاد کشنده اوکراین  پهپاد FP-1 (Fire Point-1) یکی از جدیدترین دستاوردهای صنعت پهپادی اوکراین به شمار می‌رود که در سال‌های اخیر به یکی از ابزارهای اصلی کی‌یف برای اجرای حملات راهبردی در عمق خاک روسیه تبدیل شده است. این پهپاد انتحاری دوربرد با هدف…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19261" target="_blank">📅 00:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19260">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی حملات هوایی را در منطقه دمط که تحت کنترل حوثی‌هاست، انجام داد.  این منطقه یک خط مقدم فعال بین نیروهای حوثی و نیروهای دولت یمنی که از سوی عربستان حمایت می‌شود، است.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/19260" target="_blank">📅 00:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19259">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اگر تُن ندارید دستکم آماده باشید!</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19259" target="_blank">📅 00:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19258">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">به نظرم یک مقدار لیست اهداف مشروع ما دارد خیلی بزرگ می‌شود که ولی خب</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/19258" target="_blank">📅 23:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19257">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بیانیه وزارت خارجه در محکومیت حمله اوکراین به شناور ایرانی در دریای کاسپین!</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19257" target="_blank">📅 23:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19256">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzCsprKMhiNtqVjLLWwzVJ9cn9Pw52ro9uMXstB3PsIRT8yNtRWSKfgUYjJRRAXuHHuhjy-NHWgN2Sxd2ynnpvwGnpyy9tVo1hJLAZNirDY1CetXqn7wCip6B2djisYkQfcG3BpBGi5cIIxyaXZvvG09I7lhQ4RKJnOjgHipi7E7kx9rLxCG2WbH39ly5iULcjiCuOHrQ5ZgTJgNAYoOgf1RLZ1MPl2FrUINds7u12kO4qlQP3BaDeMo4tcmt7pISjcjseUV0A8w14D7kPkX9XS7uH3GNIavChKvDbBN-uhXLTtVfYL1fGdl3H8UHF7_GJKWqPK-_hf57ukx_zXJgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید هم زلنسکی دارد جمهوری اسلامی را تحریک به پاسخگویی نظامی به اوکراین می کند تا رسماً پروژه تسلیح گروه های مخالف ایرانی به پهپادها و ریزپهپادهای اوکراینی را استارت بزند.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/19256" target="_blank">📅 23:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19255">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سپاه پاسداران:  «هر کشوری، چه بریتانیا باشد و چه دیگری، اگر از آمریکا در جنگ حمایت کند، برای ما هدفی مشروع خواهد بود.»</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/19255" target="_blank">📅 23:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19254">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">در عملیات 2 شب پیش دو فروند بمب‌افکن B-1B لنسر نیروی هوایی آمریکا از پایگاه RAF Fairford در بریتانیا به پرواز درآمدند و در بمباران جنوب کشور (استان خوزستان) نقش داشتند.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/19254" target="_blank">📅 23:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19253">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbBS1NeTe3dI0nlfNeobEcV18HnSdEsQ2HVpl0yonkV9ugb1NsDH93_l8TD9ssfZ4BkIl6bF6qtsDJDO1FI9bJxhbLg2pI73bPYcxiyaulzocbjfsORyNclv4mTYVu3JKudgsDL9Xz7Fn7R5zTHhm7HcxSoS6OlE-rE81F7qdHP6NIZQ3ImBG3t3R1E9SkhH8kntPq7XaZlEaVI86vMOzMzuKUhhpCvOg7zzbGCMlsVG8No-wqHaB58Jq-1zRk0_4MBhvyJCBe00V_Ymr25SGq80WlvFO5CqLzcpFrVxd-WYR-Bwm1Ma_XE1QGRvSsmcd9nHbrgDO3rfiSKj1Gf5Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عملیات 2 شب پیش دو فروند بمب‌افکن B-1B لنسر نیروی هوایی آمریکا از پایگاه RAF Fairford در بریتانیا به پرواز درآمدند و در بمباران جنوب کشور (استان خوزستان) نقش داشتند.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/19253" target="_blank">📅 23:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19252">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نیویورک پست :  «دقت وحشتناک موشک‌های ایران» این هراس را دامن زده که دشمنان آمریکا در حال کمک به ایران برای هدف قرار دادن نیروهای ارتش آمریکا و CIA هستند!</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19252" target="_blank">📅 23:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19251">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ درباره ایران:
اگر ۱۰۰٪ آنچه از ایران می‌خواهیم را به دست نیاوریم، قطعاً از سرگیری جنگ تمام‌عیار را در نظر خواهیم گرفت.
منبع: LCI</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19251" target="_blank">📅 23:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19250">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی حملات هوایی را در منطقه دمط که تحت کنترل حوثی‌هاست، انجام داد.
این منطقه یک خط مقدم فعال بین نیروهای حوثی و نیروهای دولت یمنی که از سوی عربستان حمایت می‌شود، است.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19250" target="_blank">📅 23:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19249">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">شین بت از خنثی کردن یک ترور دیگر ضد بن گویر خبر داد.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19249" target="_blank">📅 23:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19248">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رسانه‌های آمریکایی: به احتمال زیاد، مسقط و تهران امشب یا فردا به توافقی در مورد تنگه هرمز خواهند رسید.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19248" target="_blank">📅 21:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19247">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">این هم موج شماری
😂</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/19247" target="_blank">📅 21:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19246">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmDbdZ0eWoDeDDRwMeco5yPwGpcENP7J55CeV7njQy9YCwtqaWBwKXwVxIETh6foQGMUSjKXj2EFY59BhxZ_NaL10vijs-_y79FjOb1nTVm99rgSh8QepPxxz-b5Jg-UscFCPjcwn5pLL-xXu7mUC9Ozoo7PE9IL_KJUElI0yf42cKRtdd-EvFbScqkHST0bNyw9bjOpr01Utbd4zM7OvxLAzUe8ylhKsWfAl3Cnuw34eAkdpb6SX5_2L9n8eTpLLgfjltInw0dO3_ppyUtONcChrgFBYxGS_AbgKPU8wmrtVv263fvH5nF-urL4w7HcLRe5Nrubr4vodZyBXVU4PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم موج شماری
😂</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19246" target="_blank">📅 21:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19245">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sh4DZFfaZSkszDPp0VtN4fEogB-7um7Hozi7DL-vADpGjghbvoF471LGpFKP2Oio4MDX6T4lMfngpVXtBUX4SC482yAoqPqVvok_DwCsiCHRHc_ibs7neDV2wY7uhMwQ3HQ3d7EEIu5-AqMnES9fP8R8A9vCx8-4hgqFR5VQJaUj0-PhlrEDVxlJhb59B0UAkqwYhhxvgVWWF24T1bpGGvnQOgeDYS2CcALsMpRyCOPE_0tWXo41rS7F2Z-AnPOJtMaAADoayNIjwQizh5JS4T0ZoAX9HDNqrhhPK5Ke0GivdvutuZiiIP3vZkIgn6zTVFxbm7d0_eVYUry6ENeJxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر داریم وارد موج 2 از 5 می شویم و موج 1 از 5 تمام شده است.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19245" target="_blank">📅 21:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19244">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">وزیر امور مالی اسرائیل، سموتریچ، درباره ایران:
ما باید به یاد داشته باشیم که هدف نهایی ما در این کمپین—و این لزوماً با مواضع ایالات متحده همسو نیست—این است که رژیم ایران را تضعیف کنیم تا به نقطه‌ای برسد که فرو بپاشد.
ما نمی‌توانیم با وجود رژیمی زندگی کنیم که به صراحت برای نابودی دولت اسرائیل تلاش می‌کند، این را علنی اعلام می‌کند و گام‌های عملی برای دستیابی به آن برمی‌دارد.
در حال حاضر، بهترین راه برای فروپاشی این رژیم، استفاده از ابزارهای اقتصادی است—یعنی به طور کامل آن را از نظر اقتصادی فلج کنیم.
به این معنا، این کمپین و فشار مجدد رئیس جمهور ترامپ بر تنگه هرمز، به همین هدف خدمت می‌کنند.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19244" target="_blank">📅 21:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19243">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b9e36a3a8.mp4?token=DlADMmneksAI4FVPI2Dm0vnF-oJuTFh95j9HgFdlTwboTgV4patnHeyU56saAFEdfYEfL8f5HVkuzYMTFYSio3sBddOS3Rb4QYT8tjkOZxksS-qJ9lFYCZJAY0b5MloWecENkpkqvYt1Z9pTLE6vltxiRjXgt8u0S-m_swo43fikIa5QrXPelLBhoDqimz733ipmiNY7kGqJJaVLcnsDxZsfBUGP6SwPeE-qWKijz61SeKlwumyafiDJh-79AuIODdNZ4buQHq4x7APsc_NW4VEdUwHv7MTnZHZKmPBEzjI3e9cC0WpuyGGR3Aq9wzJDbHe4qBNgIerTQVeGu5aDVwDMjL3x7YMNaUZgSACg5guPQ3T-YBhXokXLeTjbDwb4kXlwMtaalebj2mQXqaOUq6SGjAGajtPuyQD2HOje8GynzQhO9QMbVh9RvkMzX_S274k0ELQXF58WBpGzlWztZXbqL45pOt_JAT4rbra7wb7j8om7VtuhaBPnxrQ1bJEgKhTDSlLOEcobxBnQ_xnJL2zTzfysyUoBt7-EjKVd63ljyc-QtYwCeWI_oaoqG5gHLdDZUhhSxEytRZT2MzHMBF_-c-V-0xD6TbGxbjaG6LYIXehwNMbKeCCiJJJxD3WT1eHUPrySGDmxYOK9UI1EzIJQnvZ5bEubUH-k9ZnXxTM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b9e36a3a8.mp4?token=DlADMmneksAI4FVPI2Dm0vnF-oJuTFh95j9HgFdlTwboTgV4patnHeyU56saAFEdfYEfL8f5HVkuzYMTFYSio3sBddOS3Rb4QYT8tjkOZxksS-qJ9lFYCZJAY0b5MloWecENkpkqvYt1Z9pTLE6vltxiRjXgt8u0S-m_swo43fikIa5QrXPelLBhoDqimz733ipmiNY7kGqJJaVLcnsDxZsfBUGP6SwPeE-qWKijz61SeKlwumyafiDJh-79AuIODdNZ4buQHq4x7APsc_NW4VEdUwHv7MTnZHZKmPBEzjI3e9cC0WpuyGGR3Aq9wzJDbHe4qBNgIerTQVeGu5aDVwDMjL3x7YMNaUZgSACg5guPQ3T-YBhXokXLeTjbDwb4kXlwMtaalebj2mQXqaOUq6SGjAGajtPuyQD2HOje8GynzQhO9QMbVh9RvkMzX_S274k0ELQXF58WBpGzlWztZXbqL45pOt_JAT4rbra7wb7j8om7VtuhaBPnxrQ1bJEgKhTDSlLOEcobxBnQ_xnJL2zTzfysyUoBt7-EjKVd63ljyc-QtYwCeWI_oaoqG5gHLdDZUhhSxEytRZT2MzHMBF_-c-V-0xD6TbGxbjaG6LYIXehwNMbKeCCiJJJxD3WT1eHUPrySGDmxYOK9UI1EzIJQnvZ5bEubUH-k9ZnXxTM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
نمونه دیگری از گاف اطلاعاتی - امنیتی صداوسیما از یک محل استقرار راداری</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/19243" target="_blank">📅 21:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19242">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فراغتی ست برای خرید تن ماهی و لذت بردن از دلار زیر 200 تومان</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19242" target="_blank">📅 20:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19241">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رسانه‌های آمریکایی: به احتمال زیاد، مسقط و تهران امشب یا فردا به توافقی در مورد تنگه هرمز خواهند رسید.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19241" target="_blank">📅 20:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19240">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">رسانه‌های آمریکایی:
به احتمال زیاد، مسقط و تهران امشب یا فردا به توافقی در مورد تنگه هرمز خواهند رسید.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/19240" target="_blank">📅 20:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19239">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بر اساس گزارش‌های منابع متعدد منطقه‌ای، 8 فروند هواپیمای بدون سرنشین MQ-9 Reaper نیروی هوایی ایالات متحده که به تازگی تولید و مونتاژ نشده بودند، در جریان حمله موشکی ایران به پایگاه هوایی ملک فیصل در اردن منهدم شدند.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19239" target="_blank">📅 20:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19238">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حمله دوباره حوثی ها به یک کشتی دیگر عربستانی</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19238" target="_blank">📅 20:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19237">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSviytM8shdgxqCRWEkBOJ6-d_lwtjJKQetL7fWnm2hzVyhbMcyx-E3re3vHvsbSa-qsRss7IMsBRu1aq3gRl8pJ52m6OaLYCK95aYEc3KWJZQyxpuD5dRwi8-w19FqLSmmCXmpa81SJJxMOv3qPUIoYElfkvcvO7rARqQQjxovMpxmtHEkR58xGjkYwdx53zk2yC62NOs_32R6DjS5wPw348j-aISGHi8AUXUFf_t4ApPqIvDo2xCiNtUoRRIFb7xPFYh3iFbRtMsRg9A8qJwZPGmChX9DKbcpRcVhlxIKpB1Ru7_JUnFd5Id9BQmh_fvOHdfJ0wcYleEEpG1pjgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی:  نتایج بسیار خوبی از حملات دوربرد در آب‌های دریای کاسپین به دست آمده است.  پهپادها به کشتی‌هایی حمله کردند که برای انتقال محموله‌های نظامی از ایران استفاده می‌شدند.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/19237" target="_blank">📅 19:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19236">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">روابط عمومی سپاه انصارالمهدی زنجان :
روز یکشنبه ۴ مرداد، از ساعت ۹ تا ۱۲، احتمال شنیدن صدای انفجار کنترل‌شده در منطقه غرب زنجان وجود دارد</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19236" target="_blank">📅 17:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19235">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHHxHK8ZGw19I2TtsDjx18RdSYmeKJJ-AFFdh-IQthO60Iu5HbA0La6woV0Jw_e5XY882GFyC0sRiIUFHlaEFVg7RYt7iax-7VEORCCn2wdQo8BC80mWYqaB4jkt-8kfmF7OmDQoHfL1QKn0rLExbWKwSVFtHzaOo6PhPVNBL-emyqoRwCcisKbEgVc1JT1cgzZFQsSo6imipAmX9AmOPvb1erqkeqJWPuSzcPIugJPtlXT0PcKWiUGebq8IEQTvV3Xgm0CWnuQz4WmB4KQx4kSN-SZR7SQINTSmpWiBvEl4-TIyqLqme278goldT2JdG_GhxpGojxSU1U6Wp9QW8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به طور فزاینده‌ای از موشک بالستیک خیبر شکن خود در حملات هماهنگ استفاده می‌کند و مسیرهای پروازی، سرعت‌ها و پهپادهای مختلف را برای پیچیده‌سازی دفاع هوایی ایالات متحده ترکیب می‌کند.
مسئولان آمریکایی می‌گویند اکثر آن‌ها رهگیری شده‌اند، اما برخی از دفاع عبور کرده‌اند که اثربخشی رو به رشد موشک و تاکتیک‌های در حال تحول ایران را برجسته می‌کند.
منبع: WSJ</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19235" target="_blank">📅 17:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19234">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">به نظر می‌رسد ایران عوامل مخفی مشکوکی را از طریق کانال انگلیسی به بریتانیا اعزام می‌کند.  افرادی که ارتباطی با سازمان‌های اطلاعاتی ایران دارند، توسط مقامات بریتانیایی در حین تلاش برای ورود به این کشور با استفاده از قایق‌های کوچک، دستگیر شده‌اند.  — نشریه تلگراف</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/19234" target="_blank">📅 17:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19233">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">زلنسکی:  نتایج بسیار خوبی از حملات دوربرد در آب‌های دریای کاسپین به دست آمده است.  پهپادها به کشتی‌هایی حمله کردند که برای انتقال محموله‌های نظامی از ایران استفاده می‌شدند.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19233" target="_blank">📅 14:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19232">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دولت بریتانیا سپاه پاسداران انقلاب اسلامی را در فهرست سازمان‌های تروریستی قرار داد که بر اساس آن، عضویت در این نهاد، شرکت در نشست‌های آن و حمل نماد آن در انظار عمومی جرم کیفری خواهد بود.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/19232" target="_blank">📅 14:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19231">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">#WHEAT  بروزرسانی نمودار گندم!  یادداشت امروز را هم بخوانید.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/19231" target="_blank">📅 13:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19230">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">📌
هرمز؛ گلوگاهی که می‌تواند قیمت گندم را منفجر کند  تنش یا اختلال در تنگه هرمز تنها بازار نفت را تهدید نمی‌کند؛ این آبراه مسیر حیاتی انتقال کودهای شیمیایی است و اختلال در آن می‌تواند هزینه تولید محصولات کشاورزی، به‌ویژه گندم، را به‌سرعت افزایش دهد.  از آنجا…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/19230" target="_blank">📅 13:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19229">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">زلنسکی:  نتایج بسیار خوبی از حملات دوربرد در آب‌های دریای کاسپین به دست آمده است.  پهپادها به کشتی‌هایی حمله کردند که برای انتقال محموله‌های نظامی از ایران استفاده می‌شدند.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19229" target="_blank">📅 13:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19228">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">حمله پریشب به انزلی به نظرم بیش از آنکه یک محموله نظامی از روسیه را هدف گرفته باشد، از جنس حمله به تاسیسات راه آهن در استانهای خراسان رضوی و گلستان بوده و پیام تشدید محاصره و کور کردن بقیه کریدورهای حیاتی کشور را داشته است.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/19228" target="_blank">📅 13:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19227">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اوکراین پالایشگاه نفت "تیومن" در روسیه را مورد حمله قرار داد. این پالایشگاه بیش از 2000 کیلومتر از مرز فاصله دارد.
استاندار این منطقه تأیید کرد که یک پهپاد به این تاسیسات اصابت کرده و باعث ایجاد آتش‌سوزی شده است.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19227" target="_blank">📅 13:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19226">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">هدف قرار گرفتن یک کشتی در سواحل عمان</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/19226" target="_blank">📅 12:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19225">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNh-r0qvnzycuX1JLGuTfyeodGyryDHg9gS4c0K1B5LBkUOkZ4iyvFJdPu-CJ39xf-or1v4pE01mp05863QTJ5M0lwvodSquglzglF2pW0UfbCMGvQKcWQGQ1R40ZRldE4nZkV5UF9xoDKBWaiR3hwrj0XQTeQmNLwD49wN_Nnd3S265Qc9Lq9jaH7-kq0OUxXxlPn-T8WFBCs0Gt2phu4bMiLokRX-DqC0Cxta0efgy-SYB9fmPsoCqSJ23okpNIVftFnjru7Axd16UoPLS81vtynNdyr8Ki6RLe-dMYt4eF1d94b1kQESVJSxQWISxb8FO5HjF2PSAudxDtabc9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهان سوم جایی است که در آن برای یک سری بوزینه دستمال کش بی عرضه برای راه یافتن به جام جهانی که 48 تیم دنیا در آن حضور داشته اند جایزه 350 میلیارد تومانی می دهند اما برای نخبگان علمی اش هیچ!</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SBoxxx/19225" target="_blank">📅 12:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19224">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">جولانی اماده حمله به حزب الله می شود  شبکه کان اسرائیل به نقل از یک مسئول سوری گزارش داد دمشق آماده اجرای عملیات نظامی علیه حزب‌الله لبنان می‌شود.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19224" target="_blank">📅 11:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19223">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب و غرب اصفهان  مدیرکل مدیریت بحران استانداری اصفهان:  از ساعت ۹:۳۰ صبح امروز عملیات کنترل‌شده معدوم‌سازی مهمات عمل‌نکرده متعلق به جنگ رمضان توسط تیم‌های فنی و تخصصی ذی‌ربط آغاز شده است.  محدوده اجرای این انهدام کنترل‌شده، مناطق…</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19223" target="_blank">📅 10:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19222">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">برای نخستین بار پس از ۱۳ شب متوالی، ارتش آمریکا دیشب هیچ حمله‌ای به صورت رسمی به ایران انجام نداده است</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/19222" target="_blank">📅 10:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19221">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">منابع اسراییلی:   بازگشایی درب‌های پناهگاهای زیرزمینی نشان دهنده نزدیک بودن وارد شدن اسرائیل به جنگ با ایران است.  تل‌آویو در صورت مشارکت ایران در جنگ قصد دارد اهدافی را در ایران مورد حمله قرار دهد که تاکنون هدف قرار نگرفته‌اند</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/19221" target="_blank">📅 10:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19220">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اگر این خبر درست باشد و اهداف نظامی ایران توسط کویت و بحرین که ضعیفترین ارتشهای عربی منطقه هستند هدف قرار گرفته باشند، یعنی اینکه عربهای جنوب خلیج فارس با راحتی بیشتری می‌توانند تاسیسات زیربنایی و غیرنظامی ایران را نابود کنند و اگر تا کنون چنین نکرده اند ناشی…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19220" target="_blank">📅 10:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19219">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">استانداری گیلان اعلام کرد   صبح امروز نقطه‌ای در بندرانزلی مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/19219" target="_blank">📅 10:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19218">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بحرین و کویت با حمایت امارات به ایران حمله کرده اند  به گزارش وال استریت ژورنال در ۲۴ ژوئیه با استناد به افراد آگاه، بحرین و کویت اوایل این ماه به صورت پنهانی جنگنده‌های خود را برای حمله به اهدافی در داخل ایران به کار گرفتند که نخستین پاسخ نظامی مستقیم شناخته…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/19218" target="_blank">📅 09:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19217">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یکی از تأسیسات حیاتی عربستان در جیزان مورد حملۀ موشکی یمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/19217" target="_blank">📅 09:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19216">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">یکی از تأسیسات حیاتی عربستان در جیزان مورد حملۀ موشکی یمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19216" target="_blank">📅 09:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19215">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">برای نخستین بار پس از ۱۳ شب متوالی، ارتش آمریکا دیشب هیچ حمله‌ای به صورت رسمی به ایران انجام نداده است</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/19215" target="_blank">📅 09:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19214">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فرماندهی سنتکام ایالات متحده اعلام کرد که یک کشتی تجاری دیگر را که بارها تلاش کرده بود از محاصره بنادر ایران عبور کند، غیرفعال کرده است. این دومین کشتی تجاری است که از زمان بازگشت مجدد محاصره، متوقف شده است.
منبع: خبرگزاری آسوشیتدپرس (AP)</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/19214" target="_blank">📅 01:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19213">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">این یادداشت را دوباره بخوانید.  یک روند ضدتورمی عجیبی در حال شکل گیری است که طلا، بیتکوین، سهام، مسکن و ... را همه با هم نابود خواهدکرد. به نظرم اساساً پول عوض خواهدشد و آنچه بستر ارزش خواهدبود توان «جلب توجه» و تاثیرگذاری بر اذهان خواهدبود.  همان که آخوندها…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/19213" target="_blank">📅 01:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19212">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXrReZzArMltW0fpOOUaXslOmMu754hp70f1RkQVM0rrP4Jtb-mCmiQ8sRN9Ou_hia27vCobipB3MIpj5XDnNw93eEEE1GxStbNLTZAishOnn6kXw7AP9FpC8DNiH5HlxaK13arjL2dTvdYALEsWS45yND7tqpEzMatxeHK6KU34QK0ayXoS_02fBR_ZhqNwNPTeh9hoME4ey-1BPrhlLqSq1hyE8-j-N9Q-AFc_zDat4abXvt76GD9KxSfqNLkNvVlf5q7JbEpHVPVTo0epLi4mGYXSRi3UVcd0fg097rMzk7qwcjhfjpGl3iLMR5zQQaph4xeFWDZhkdDLVLTPeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز در سطح میانه ای قرار دارد و پیش بینی حرکات رفت و برگشتی و رنج همراه با نوسان برای طلا می رود.  محتملا بین رنج ۴۰۶۰ تا ۴۰۳۰</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/19212" target="_blank">📅 01:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19211">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‌
یمن (منظور یمن تحت کنترل حوثی ها): حماقت عربستان تاوان سنگینی خواهد داشت
وزارت امور خارجۀ یمن: ما رژیم عربستان سعودی را مسئول تمام پیامدها و تحولات ناشی از این اقدام جنایت‌کارانه می‌دانیم.
رژیم سعودی به‌جای تسلیم در برابر مطالبۀ حق و عادلانه برای رفع محاصرۀ یمن، مرتکب حماقت بزرگی شد که هزینۀ زیادی برای آن درپی خواهد داشت.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/19211" target="_blank">📅 01:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19210">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/19210" target="_blank">📅 01:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19209">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcbgLknm-5n0vy0P075f4pEnqfxq9KY8ZdUVJ_bQZZvtJrnBbnH9ao0690CZlPs2-2OEqZZ6OvAjVMbXg0VWbLx8u1U_2uNeHshLegM8lGQwtpGJ62QHMYKkD-H9PAP5AK5ngkSblXsuR1gmmq-SOb5YcVC4paBcjJ0PneM0FC8k8hDrg09sVOqNyBqBuThhMR4OXn5ZRAXwhNR0QM2HLocDM7S8cG4TBSigMGoSx2llO5J_lr7-scOHqj9LCw8-0P-35u67Dt6ipl9MAKGU9xcGvoUTaCR1bBoMagGdjlxz4AxVwkHUqeagaZ-ctgl578wq2Ude_27F1j8RAwFZZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان آتش‌بس ایران؛ ضربه‌ای مهلک به سرمایه سیاسی جی‌دی ونس   تا پیش از فروپاشی آتش‌بس میان ایران و آمریکا، جی‌دی ونس یکی از مهم‌ترین برگ‌های برنده خود برای رقابت‌های درون‌حزبی جمهوری‌خواهان در سال ۲۰۲۸ را در اختیار داشت؛ این ادعا که توانسته است در کنار دونالد…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/19209" target="_blank">📅 00:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19208">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">308 KB</div>
</div>
<a href="https://t.me/SBoxxx/19208" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 12</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/19208" target="_blank">📅 00:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19207">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حمله عربستان به شهر الحدیده یمن</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/19207" target="_blank">📅 23:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19206">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گزارشگر: می‌گویید که با ایران در حال گفتگو هستید. چه کسانی درگیر هستند؟ ویتکوف؟
ترامپ: تقریباً همه. جی‌دی، مارکو - افراد زیادی در حال گفتگو هستند. این یک مسئله بزرگ است.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/19206" target="_blank">📅 23:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19205">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بحرین و کویت با حمایت امارات به ایران حمله کرده اند
به گزارش وال استریت ژورنال در ۲۴ ژوئیه با استناد به افراد آگاه، بحرین و کویت اوایل این ماه به صورت پنهانی جنگنده‌های خود را برای حمله به اهدافی در داخل ایران به کار گرفتند که نخستین پاسخ نظامی مستقیم شناخته شده آن‌ها علیه جمهوری اسلامی بود.
بر اساس این گزارش، حملات به تأسیساتی که برای ذخیره پهپادها و موشک‌ها استفاده می‌شدند و همچنین سایر تأسیسات نظامی متمرکز بودند.
امارات متحده عربی که پیش از این در مراحل اولیه درگیری چندین حمله به ایران انجام داده بود، به گفته ژورنال، اطلاعاتی درباره اهداف بالقوه ارائه کرد و پشتیبانی هوایی دفاعی فراهم نمود؛ این گزارش تأکید می‌کند که این اقدام نشان‌دهنده هماهنگی فزاینده میان کشورهای عربی علیه جمهوری اسلامی است.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SBoxxx/19205" target="_blank">📅 22:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19204">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نیویورک تایمز:
بر اساس ارزیابی نهادهای اطلاعاتی آمریکا، (آیت الله) مجتبی خامنه‌ای، رهبر جدید ایران، برخلاف پدر علاقه و تمایل بسیار بیشتری به دنبال کردن دستیابی به سلاح هسته‌ای دارد.
این موضوع را مقام‌های آگاه از این ارزیابی‌ها به نیویورک تایمز اعلام کرده‌اند</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/19204" target="_blank">📅 22:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19203">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ در 'حالت انتقام' و خسته از جنگ با ایران
به گفته یک مقام آمریکایی ، رئیس‌جمهور ایالات متحده تلاش‌های دیپلماتیک برای حل درگیری پنج‌ماهه در ایران را کنار گذاشته و طبق گفته مقامات، وارد «حالت انتقام» علیه تهران شده است.</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/19203" target="_blank">📅 18:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19202">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">به گفته سه منبع پاکستانی، پاکستان در پی تلاش چین، در حال بررسی از سرگیری مذاکرات متوقف شده آمریکا و ایران برای پایان دادن به جنگ تقریباً پنج ماهه خود است.  به گفته منابع، مذاکرات مقدماتی در جریان سفر این هفته اسکندر مومنی، وزیر کشور ایران، به اسلام آباد، که…</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/19202" target="_blank">📅 18:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19201">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">به گفته سه منبع پاکستانی، پاکستان در پی تلاش چین، در حال بررسی از سرگیری مذاکرات متوقف شده آمریکا و ایران برای پایان دادن به جنگ تقریباً پنج ماهه خود است.
به گفته منابع، مذاکرات مقدماتی در جریان سفر این هفته اسکندر مومنی، وزیر کشور ایران، به اسلام آباد، که دومین سفر او در ده روز گذشته است، انجام شد.</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SBoxxx/19201" target="_blank">📅 18:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19200">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ: چین و پوتین گفتند که سلاح به ایران نمی‌فروشند</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/19200" target="_blank">📅 18:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19199">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وزارت امور خارجه آمریکا: وظایف مرزی و گمرکی درمسیر TRIPP  تحت کنترل ارمنستان باقی خواهد ماند.   وزارت امور خارجه ایالات متحده در مورد مقررات اتحادیه اقتصادی اوراسیا در مسیر TRIPP اعلام کرد، تمام وظایف امنیتی مرزی و گمرکی تحت کنترل ارمنستان باقی خواهد ماند.…</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/19199" target="_blank">📅 18:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19198">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بنیامین نتانیاهو روز سه‌شنبه با رئیس‌جمهور ترامپ برای ارائه لیست خواسته‌ها و انتظارات خود از آمریکا دیدار خواهد کرد.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/19198" target="_blank">📅 17:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19197">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بنیامین نتانیاهو روز سه‌شنبه با رئیس‌جمهور ترامپ برای ارائه لیست خواسته‌ها و انتظارات خود از آمریکا دیدار خواهد کرد.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/19197" target="_blank">📅 17:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19196">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:  «ما به عموم مردم کشورهایی که پرسنل نظامی ایالات متحده در آنها مستقر هستند هشدار می‌دهیم که فوراً از مناطقی که در شعاع ۵۰۰ متری از مکان‌هایی که پرسنل نظامی ایالات متحده، چه به صورت آشکار و چه به صورت پنهان، مستقر هستند، قرار دارند،…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/19196" target="_blank">📅 15:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19195">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:
«ما به عموم مردم کشورهایی که پرسنل نظامی ایالات متحده در آنها مستقر هستند هشدار می‌دهیم که فوراً از مناطقی که در شعاع ۵۰۰ متری از مکان‌هایی که پرسنل نظامی ایالات متحده، چه به صورت آشکار و چه به صورت پنهان، مستقر هستند، قرار دارند، دور شوند تا امنیت خود را تضمین کنند.»</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/19195" target="_blank">📅 15:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19194">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 12</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19194" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 12
جمعه 24 جولای 2026</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/19194" target="_blank">📅 13:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19193">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwkN8OjOvNhU7jaBCQ301AR_Rjc48du-FdGv2jkvBf0xEXcQKv2kz_m5FzoZDb9Gl5118BWBcjI-VvjFWYYx-Vd-TgBqyPhqQ4gJsqSGAyfB3ExxAimMHEG50FRCtcG7jxcWuQzP02pZ0D5zj_YRtO5029SaRcItZtyCQDKZr35824j4-Rvb6jv8VdEjxVlTZ-hQK28C3hSQDt-95f4fXwuWb-ohmWILLUgWn8J-jwuYNDZTvDuMRtfoxlcyfd_0Vouq6toKHLWJ8rq7YvQZoJAwrZGwYs7pFhLDDinelnQ5C6BxTNVdR6cRFmRqHHBfokxzlRItDT8iYIfuhQXPqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز در سطح میانه ای قرار دارد و پیش بینی حرکات رفت و برگشتی و رنج همراه با نوسان برای طلا می رود.
محتملا بین رنج ۴۰۶۰ تا ۴۰۳۰</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/19193" target="_blank">📅 12:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19192">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وزارت امور خارجه آمریکا اعلام کرد که تحویل جنگنده‌های اف-35 به ترکیه انجام نخواهد شد، زیرا شرایط مربوط به سیستم دفاع هوایی اس-400 برآورده نشده است.</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/19192" target="_blank">📅 11:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19191">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اگر شانتاژ اسراییلی ها برای بر هم زدن ماه عسل ترامپ با اردوغان نباشد، معنی اش این است که ترک‌ها حاضر هستند از اف-۳۵ چشم بپوشند اما شاهد سرنگونی جمهوری اسلامی نباشند.  به نظر در این صورت، تنش‌هایی در دریای اژه خواهیم داشت.  #ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SBoxxx/19191" target="_blank">📅 11:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19190">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بوی آغاز حملات اسراییل می آید.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/19190" target="_blank">📅 11:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19189">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">استانداری گیلان اعلام کرد
صبح امروز نقطه‌ای در بندرانزلی مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/19189" target="_blank">📅 11:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19188">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">حملهٔ هوایی به پیرانشهر  مدیریت بحران آذربایجان‌غربی: حوالی ساعت ۹ صبح امروز یک نقطه در پیرانشهر مورد حملهٔ هوایی دشمن امریکایی قرار گرفت.  در این حمله چندین خودرو نیز آسیب دید؛ هنوز آمار احتمالی از تعداد شهدا و مجروحین این حملهٔ جنایت‌کارانه دشمن در دست نیست.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/19188" target="_blank">📅 11:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19187">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">حملهٔ هوایی به پیرانشهر
مدیریت بحران آذربایجان‌غربی: حوالی ساعت ۹ صبح امروز یک نقطه در پیرانشهر مورد حملهٔ هوایی دشمن امریکایی قرار گرفت.
در این حمله چندین خودرو نیز آسیب دید؛ هنوز آمار احتمالی از تعداد شهدا و مجروحین این حملهٔ جنایت‌کارانه دشمن در دست نیست.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/19187" target="_blank">📅 11:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19186">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umC9JrVObhMx7E4IQjYEhipk5DVj74NkIqKySF8LzjR5YaZkMm12BPUGipsgaAkjy9GcI6BTxY5aJ6cEAb-ErMkIea3YlLs4jhyrqO6Nilm_38VXWpoXyK_YWNiKzy1fJ_GOQE0y_AKhxcePazT48GhgOFLE2KGen3QHn5mIfPCZJGy5kqear-KzuVQOfQO3DLpXhKJrptma_sAuTwCzoKxuhvACXk2YaJ9O8GZV89aeXMcRHBtBL60PhiCQUzt0Zncb8P5rXLWeO2czCt6f1ff4W2H4ojG1YXl_-4LHyL-CJhbtoRGJ9treas9S4hvoy6uxUAOsiPKjKxxw9_FD5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز کماکان بالا است اما از دیروز خیلی پایین تر آمده.  به نظر می رسد طلا یک اصلاح صعودی رو به بالا داشته باشد (بعد از ریزش 700 پیپی از سقف دیروز)</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/19186" target="_blank">📅 10:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19185">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bc2d5ac32.mp4?token=mDYAkmmZH6pFFPIvibkCmE4-osiUES6g-2D4tLmhZ4TVLoHljbhhpnM1q-aMXQRYL-qG-3dOHNR05GwAAkFSwiW2nKIH81AZcG5BUalOlzcgJfOdZL_p80it-lD5W3f3oZP0_7uB81RClCHciRDltSM3DxoQKOrQLusTPSr6BfXJwtU4MuIv5BgekkYSFvuR-5cGwcgYaQTM7tvxNztQjRMEP9T9xkj-b8ylBQgsDSgizcWdnQ8X726Wdm-WS10FD-l73lfDnwbONzyGvRTvs_HhidpxrKRoZvsrl23eIqbK67n6dAbtV9HDGEOPG1mX_0mbsRZgfzgSPbxlBjZ2Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bc2d5ac32.mp4?token=mDYAkmmZH6pFFPIvibkCmE4-osiUES6g-2D4tLmhZ4TVLoHljbhhpnM1q-aMXQRYL-qG-3dOHNR05GwAAkFSwiW2nKIH81AZcG5BUalOlzcgJfOdZL_p80it-lD5W3f3oZP0_7uB81RClCHciRDltSM3DxoQKOrQLusTPSr6BfXJwtU4MuIv5BgekkYSFvuR-5cGwcgYaQTM7tvxNztQjRMEP9T9xkj-b8ylBQgsDSgizcWdnQ8X726Wdm-WS10FD-l73lfDnwbONzyGvRTvs_HhidpxrKRoZvsrl23eIqbK67n6dAbtV9HDGEOPG1mX_0mbsRZgfzgSPbxlBjZ2Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک کویتی میگوید از بس صدای آژیر خطر به صدا درآمده، پرنده اش مداوماً این صدا را تقلید می کند!
سبحان الله!</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19185" target="_blank">📅 10:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19184">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ادامه حملات ایران به بحرین و اردن</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/19184" target="_blank">📅 09:53 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
