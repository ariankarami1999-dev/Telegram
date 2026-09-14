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
<img src="https://cdn4.telesco.pe/file/WygcAuCcEozahrsNiYhKU9OCl5yh_ztITpu-NnznMYi2Oc9ZKIgyMazgJ3MHYtOJdbtXRymoKLCh2NZvrFtyf3WItFSA2MgsaKuUSf0iU8oRnIyPH_C8iofPItrGh3E7wtKpN1Q4Qc4Q-lcvqPadrwNe0m7Fv6QNx-9l0LQ7F_ZPsj0WylvwmIM-4-F1TkiyJ6Z2zC-2-7YY_TXLHP1jTd1UtUHbwwVCuO9n4OIwBA83TSPuoPX7aB3ygnQmtPBdIrDEh2CIrcBlCL2FZoC7TNcEoi-_YM-uqCEnHa_b_z-V6x5K0JWqrc7juPdwMYAwpho4lNhJJRIy0Mj-rO03_Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 108K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 11:50:28</div>
<hr>

<div class="tg-post" id="msg-71607">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f19ca22a78.mp4?token=JEOdp7KbZeSxgr9CyYfqh9KclQkLdwwJPxNX5-QMDtAT6Of8RC3v7dBfwklNblYPDY6COCUhNyqhOEAsVYIWN1VT-9HXXshaFs0bfyHMV9KJ1nsJsw3t_SsjF64pMarJjHj686k7VMck6VMWH0cpOnHVYP6_T7cEjF4yBd4OxHrTQRSM4OSnsSX1h0efWH5_WTBlSHrjPrc21JL8uZMhbznryJFQq7MfL5ilLxes5uCmqcziIGlptN6vYJAk5lEiRlGLUVmubMiR9NguQgpMdoBe1bTT_9rW_o2K7Cqf59RVtBhZrDMvZ9m_gcExAAP2nWIvoWocbyW3vbHSesFf6x_MJL0HN2OzVoEV_4z0Re1RUQN_fvy4ylxuBd85ite-5wghZM5LMnaxfRd4OtwncKnKP34DJsX1Nk5dGbVADIJL3-kh__SUlTFia_30HtkAIt4e1ksg1lKJtIoESCU2rjFobxl7SSYv6DHlTcv6rrsihc_APPVxqJbOVDW-cgawFjhQDVZl3JUWV6QbYBzuVeZ-UfSNPGwjIynXOjpoL2l8YVEXTaJdN4nvhZvt07oI6eLb4EC7W4dWKelmBBDEIbWLOnUO9s0tw3IZNG-klTu26p2J9HYAvp4Rlm_Ys9YG35ahdu2EuUu-nKpt_Fz5alBVBO_BW7FJ4ce7qo4Hoxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f19ca22a78.mp4?token=JEOdp7KbZeSxgr9CyYfqh9KclQkLdwwJPxNX5-QMDtAT6Of8RC3v7dBfwklNblYPDY6COCUhNyqhOEAsVYIWN1VT-9HXXshaFs0bfyHMV9KJ1nsJsw3t_SsjF64pMarJjHj686k7VMck6VMWH0cpOnHVYP6_T7cEjF4yBd4OxHrTQRSM4OSnsSX1h0efWH5_WTBlSHrjPrc21JL8uZMhbznryJFQq7MfL5ilLxes5uCmqcziIGlptN6vYJAk5lEiRlGLUVmubMiR9NguQgpMdoBe1bTT_9rW_o2K7Cqf59RVtBhZrDMvZ9m_gcExAAP2nWIvoWocbyW3vbHSesFf6x_MJL0HN2OzVoEV_4z0Re1RUQN_fvy4ylxuBd85ite-5wghZM5LMnaxfRd4OtwncKnKP34DJsX1Nk5dGbVADIJL3-kh__SUlTFia_30HtkAIt4e1ksg1lKJtIoESCU2rjFobxl7SSYv6DHlTcv6rrsihc_APPVxqJbOVDW-cgawFjhQDVZl3JUWV6QbYBzuVeZ-UfSNPGwjIynXOjpoL2l8YVEXTaJdN4nvhZvt07oI6eLb4EC7W4dWKelmBBDEIbWLOnUO9s0tw3IZNG-klTu26p2J9HYAvp4Rlm_Ys9YG35ahdu2EuUu-nKpt_Fz5alBVBO_BW7FJ4ce7qo4Hoxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ℹ️
باز و بسته کردن (مونتاژ و دمونتاژ) کلاشنیکف AK-74 توسط این بانوی روس
@News_Hut</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/news_hut/71607" target="_blank">📅 11:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71606">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‼️
اگه نیسان کشنده ندیده بودی
این ویدیو رو ببین تا ببینی همچی توی ایران ممکنه
😟
@News_Hut</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/news_hut/71606" target="_blank">📅 10:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71605">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ed023bda.mp4?token=XAE2eDy4YtBoutO6XweTpgHQTdMTJwkxGlOFQGzibltbi8RcGAxBvTny--20-r1snjEin9AFKOXBiWeD9SHwW2f2rLBAMSD2ZyjPCcOmUZQFjRrxnpvJBpadcTwvjwR-g7O2YETwu-FpnTB7leNSI86zV_KNfI4JERY6xqAZppnfBh9rVI1bN_E8mbA70ccRYXr450tsQYiegOzNXrZZ-GIR5nGV5PwZVD6nCz0M1GvbN9y4Hdevs03dypg7DkLF-kz6mfjy959rcxSWhhhzd9Dn6Cso-FkEYYqJlVDfsxnwo0AR9fVABSxCQDtk2Xy8g_Tg2Jr5VVq63HLVlglfhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ed023bda.mp4?token=XAE2eDy4YtBoutO6XweTpgHQTdMTJwkxGlOFQGzibltbi8RcGAxBvTny--20-r1snjEin9AFKOXBiWeD9SHwW2f2rLBAMSD2ZyjPCcOmUZQFjRrxnpvJBpadcTwvjwR-g7O2YETwu-FpnTB7leNSI86zV_KNfI4JERY6xqAZppnfBh9rVI1bN_E8mbA70ccRYXr450tsQYiegOzNXrZZ-GIR5nGV5PwZVD6nCz0M1GvbN9y4Hdevs03dypg7DkLF-kz6mfjy959rcxSWhhhzd9Dn6Cso-FkEYYqJlVDfsxnwo0AR9fVABSxCQDtk2Xy8g_Tg2Jr5VVq63HLVlglfhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تست سلاح جنگی بر روی شتر توسط یک عرب
😳
@News_Hut</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/news_hut/71605" target="_blank">📅 10:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71604">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69e312dde1.mp4?token=rzYgSS67SuHatGv6nG-BVSKBt6LPq6zhWCBYZIFlLpRl7MwM8YB-fnxsnlJZJL-vrQExRmuHAYBPqn6jtvwJ2mNDB7WWnBQepoqTpc3n4ZzawbvAwXPPhMFo3yjq6D6o1aVI2sRex2_4zcUTdbca9Rmo79K2oMRCH-YFt4c_4gDZvj10JEEjCwEHsVETBGABNUhbXAzxYHIqiRZJcDD0prdJys3G7gIclNLxxDw402Yt2kT0t8KWJpG5s-0BKHP5D07-d5BYq5tr_XQA2LtsgLP8DVj7CU0tNWfPrFM5bwVgO2VDObWf0pfmLbTpSsB2yn5PD9S5wIT3iC1a_uoviQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69e312dde1.mp4?token=rzYgSS67SuHatGv6nG-BVSKBt6LPq6zhWCBYZIFlLpRl7MwM8YB-fnxsnlJZJL-vrQExRmuHAYBPqn6jtvwJ2mNDB7WWnBQepoqTpc3n4ZzawbvAwXPPhMFo3yjq6D6o1aVI2sRex2_4zcUTdbca9Rmo79K2oMRCH-YFt4c_4gDZvj10JEEjCwEHsVETBGABNUhbXAzxYHIqiRZJcDD0prdJys3G7gIclNLxxDw402Yt2kT0t8KWJpG5s-0BKHP5D07-d5BYq5tr_XQA2LtsgLP8DVj7CU0tNWfPrFM5bwVgO2VDObWf0pfmLbTpSsB2yn5PD9S5wIT3iC1a_uoviQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
زنده یاد مانوک خدابخشیان:
تنها برگ برنده دونالد ترامپ این است که پرونده رژیم جمهوری اسلامی بسته شود. این بزرگترین پیروزی است، درست مثل فروپاشی شوروی؛ این را فراموش نکنید.
چرا او باید وارد جنگی شود که سال‌ها طول بکشد و دوباره در باتلاق خاورمیانه بماند؟
هدف این است که از خاورمیانه بیرون بیاید.
شما به اصطلاح آن دکه جمهوری اسلامی را ببندید، همان‌طوری که دکه کمونیسم بسته شد و همه فرو ریختند، تمام این‌ها هم فرو خواهند ریخت.
@News_Hut</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/news_hut/71604" target="_blank">📅 10:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71603">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران:
لحظاتی قبل یک فروند پهپاد پیشرفته MQ۱ توسط سامانه نوین پدافند پیشرفته هوافضای سپاه و تحت کنترل شبکه یکپارچه پدافند هوایی کشور بر فراز آسمان تنگه هرمز رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/news_hut/71603" target="_blank">📅 09:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71602">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‼️
یه ایرانی رفته توی تجمعات حامیان فلسطین توی خارج و بهشون میگه <<کص ننت فلسطین>> یعنی فلسطین رو دوس دارم
😂
اونا هم بدون اینکه معنیشو بدونن دارن تکرار میکنن
در ادامه میگه فلسطین رو از حماس آزاد کنید
در آخرم شعار جاویدشاه رو سر میده
👑
@News_Hut</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/news_hut/71602" target="_blank">📅 09:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71601">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🇺🇸
❌
🇮🇷
مصاحبه کامل و ترجمه شده افسر تسلیحات نجات یافته ملقب به "براوو Bravo" با برنامه Minutes 60 پیرامون عملیات CSAR که در ماه آوریل در عمق خاک ایران انجام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/71601" target="_blank">📅 09:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71600">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🇺🇸
❌
🇮🇷
⭕️
تصاویر تازه‌منتشرشده‌ای که توسط برنامه «۶۰ دقیقه» (60 Minutes) پخش شد، عملیات نجات دو افسر نیروی هوایی ایالات متحده را نشان می‌دهد؛ افسرانی که با نام‌های عملیاتی «آلفا» و «براوو» شناخته می‌شوند و جت جنگنده F-15E آن‌ها در ماه آوریل بر فراز ایران سرنگون شده بود.
این دو نفر در حالی که نیروهای ایرانی در جستجوی آن‌ها بودند، در منطقه‌ای کوهستانی در جنوب اصفهان و با فاصله‌ای حدود پنج مایل از یکدیگر فرود آمدند. در این گزارش همچنین تصاویری از حمله به نیروهای ایرانی به نمایش درآمد.
آلفا» هشت ساعت پس از خروج اضطراری (اجکت) از هواپیما، طی یک عملیات پرخطر در روز که با مشارکت ۲۱ فروند هواپیمای آمریکایی انجام شد، نجات یافت.
«براوو» حدود دو روز در پشت خطوط دشمن باقی ماند. او با وجود شکستگی کمر و سایر جراحات ناشی از فرود سخت (به‌دلیل نقص در چتر نجات)، از یک خط‌الرأس کوهستانی به ارتفاع ۷۰۰۰ پا بالا رفت تا اینکه دو تن از نیروهای ویژه امداد و نجات نیروی هوایی به او رسیدند و وی را به بالگرد آمریکایی منتقل کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/71600" target="_blank">📅 07:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71599">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71599" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/71599" target="_blank">📅 01:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71598">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eX_l-ZFPkxBrv2OLqHAprvfHK9A785xpTTaLiGHVkjae6cWjelgE_NkYeuzGBKLE4R2zwc63293XfoLAlZrRfaW1YpaEBiFS6vEnKYtKpXEL8J7G75Q_7CvK0viMFoS2eeuU3ewPYGwgog4b0XOhBTMMfwfPfKE60xdRmAPR0F5tXnUOexSSIlgjCAMtRcbSyFoso4HY7eY_wLcH3Cii4pZxczPL0skIL5WCzkCKg7JIsMDhtvg_AtiXchyK-qWLkWYz4f1uagVZA93alxD75kLO4Oua9NSewjDO6yzrYUBzRUKfNFMDDTyHsT8di6GEdvgPtTGJvnNVqMAPOKpTUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/71598" target="_blank">📅 01:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71597">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b94dc744f.mp4?token=kJpw0uwLlgTVoS9kTNrVRFQlLp_j5osdICSWtBFRdm5vLIF65Wr-p8Co64Q8tVpe41AsCzQrvV5lm06jJbeDlxWVN0S81_r1IUU-vE-qwMjXpCfILkfpTglprcQpmAWcHSb-F0UUN7hKLX6XQ_mrZ57TcUziM9HpkH9Oj1gomnVkXQSIk2LJSVjBTCInpKoT1Ex9MisBXAjxlhrXp29Q4mtvoKdnfGm2zuBogJ1Toprsw6KaJGl4DGSHJ0p4k3JMvxkXtT3DVcz1ynPM3KNXaNfFyL7AVL1rCts5xn2JA_x-a692V_fGraG3LPqGIYqGbID8PPGaA5lEfutr4OTlKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b94dc744f.mp4?token=kJpw0uwLlgTVoS9kTNrVRFQlLp_j5osdICSWtBFRdm5vLIF65Wr-p8Co64Q8tVpe41AsCzQrvV5lm06jJbeDlxWVN0S81_r1IUU-vE-qwMjXpCfILkfpTglprcQpmAWcHSb-F0UUN7hKLX6XQ_mrZ57TcUziM9HpkH9Oj1gomnVkXQSIk2LJSVjBTCInpKoT1Ex9MisBXAjxlhrXp29Q4mtvoKdnfGm2zuBogJ1Toprsw6KaJGl4DGSHJ0p4k3JMvxkXtT3DVcz1ynPM3KNXaNfFyL7AVL1rCts5xn2JA_x-a692V_fGraG3LPqGIYqGbID8PPGaA5lEfutr4OTlKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
سپاه به طرف تنگه هرمز موشک شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/71597" target="_blank">📅 01:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71596">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZisGzl6WolWFcsoCmKj-CkyjfABzleqXUFjmg6wXkIPxWAWkUcglpRLB8F3mU03YohXseR3GSZXOpLJnNiWoe0nVMhhqpCOxrLZzmDaOi2iLhvzpJ78ONRSymGttF-EOa0TyfQ8oHfLwio-zWcPJuSqMDmQ85onYwIlIaVQYsPH3XpfYh4MaG-TnK1f0ZoYbRVpIi3GfW0ZalQRVscZQgbDnQdC1Y5Rf2uyEev-A1AiAkxU5N1Hk7WqAhuE36PLFKOjC-m-RtUvdt9yxrHiwgQc_wc_DJIAxkiIirtMFyaztKpinS6EDBSPnuHhp82Peg4xCnsx6w2y0hyodKOOFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
❌
🇮🇷
🇴🇲
باراک راوید:
یک مقام حوزه خلیج فارس به من گفت که عربستان سعودی اصلاحاتی را در طرح پیشنهادی عمان و ایران در خصوص تنگه هرمز ارائه کرده است؛
زیرا نگران بود که عبارات پیشنهادی عملاً منجر به ایجاد وضعیت موجود جدیدی در این تنگه شود که برای این کشور یا سایر کشورهای عضو شورای همکاری خلیج فارس قابل قبول نباشد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/71596" target="_blank">📅 01:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71595">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c7311729.mp4?token=uO0fDWWirbbLOObcygoMgMmjiLIGM2UvfPIc6tQSBhu5rijtYzYGQbmwqY9qx8_b6HH69wAmpka1-0ub0tF9NSsR6UUBhxoxfHvGVSWqX0EHTld-r92EkkTxvrzP5DQwPhEtwMmaj2rRrM-DzzpQbWxxJ1EBW9GNZ9oJ2atFLrFOTk9SJEskjSFWRFCj7YCmYfRXZq0sTIc4WBU05gSEl6CsThx8D-mLkzB_0e-YyXdqfvcfWo4ug2hlO9vBhbuKWiuoqsX7FJeMdlv-qVCgxNmRppGGh4YjApqa4_Pc6KqQ7RVvQpUhYlJfbVWdCKOBBTakMqNcuIJtM_mX__P-9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c7311729.mp4?token=uO0fDWWirbbLOObcygoMgMmjiLIGM2UvfPIc6tQSBhu5rijtYzYGQbmwqY9qx8_b6HH69wAmpka1-0ub0tF9NSsR6UUBhxoxfHvGVSWqX0EHTld-r92EkkTxvrzP5DQwPhEtwMmaj2rRrM-DzzpQbWxxJ1EBW9GNZ9oJ2atFLrFOTk9SJEskjSFWRFCj7YCmYfRXZq0sTIc4WBU05gSEl6CsThx8D-mLkzB_0e-YyXdqfvcfWo4ug2hlO9vBhbuKWiuoqsX7FJeMdlv-qVCgxNmRppGGh4YjApqa4_Pc6KqQ7RVvQpUhYlJfbVWdCKOBBTakMqNcuIJtM_mX__P-9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
ایران می‌گوید دیشب به یکی از شناورهایش حمله شده است. آیا کار آمریکا بود؟
🇺🇸
ترامپ:
نمی‌خواهم بگویم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/71595" target="_blank">📅 00:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71594">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjXNAsNK9kIPlaPl3gUBcmD_mVLPQ7oM2Mf9TK_Yzf2kfLu18bIHZlOv4WEfq_ulZyTFzKmYvtsHcNMonpafmbowGfEkHIX85qmheh9LIhWqne0ndKI3EqTlxQl1ZtOtuEkjVXeVpZu5cGbNK5SMAWFzabaOjO4li_NBQ_jlJm5WhzD3c7iIi5tysF1Vi0IiddsDyR-vLE225njU1JE7fL_KuKjWiIjhtFythdlyC0iM-oSB66S-Q38ZOBHPYu0Yf7ArLXYJK6a0-H88O9VFkmrEbXYHi-fZcczxvGE3ToUXA_iWqtYUa4-7tbksiuFikGtKwomrHAg7rxJP9ZE-KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇴🇲
بدر‌البوسعیدی وزیر خارجه عمان:
در راستای دستیابی به اجماع، نشست منطقه‌ای که قرار بود فردا در صلاله برگزار شود، به تعویق افتاد.
ما همچنان به ترویج گفت‌وگویی که حامی ثبات و همکاری پایدار در منطقه ما باشد، متعهد هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71594" target="_blank">📅 00:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71593">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
⭕️
نشستی که قرار بود فردا در عمان میان ایران و کشورهای حوزه خلیج فارس درباره تنگه هرمز برگزار شود، به تعویق افتاده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71593" target="_blank">📅 00:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71592">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNApwZOTfbbDc3PjGlVJjwwx0uZ0W02zSihDmF9muLlJLjTE5as5cmjF0PsSBljHF25fggq6k2VrdfqD8zKQ0_5N9OiqWtRH-5_Xi_9k9n6AL41ePm7i8ETKvVPEXHzVKvzezI8LKJxHAR7VgRW4A-kocdRKpmHx95KVmtZyPXIVsKby7nN5zuSJPFEWV0iHkeVKgmqgOizZ3yjT9wzxJcfiXWIk3CbiusZMwbFWHbG2EWJXO_FCQkGhtsjcFqnBO28sNVHrrJzvQYaaYg_kmh9QNSfzIYjgQywNv3vqh_wh7_UvsuT8MnK_yvkajkhoRDX9cDQi2N_aV4OwRDpR3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحبت های عجیب پوریا بختیاری کارشناس اقتصادی در مصاحبه با علی ضیا درباره ابراهیم رئیسی:</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71592" target="_blank">📅 00:20 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71591">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec76e7285d.mp4?token=cjiExMHjTu9v_Ow4uuD-wseKljyxaOc3-QQFpmxijo-XijzLnhJ8XZnwkCt6vwaF3a2012FledA1aCvUV4ebeedMx9s6pFe4rZTXA4eI_ujKEy_bLI6t6UE03o155Bd5xu2iAXtma7kyxtESjhKeP_LxjNGoOcJCTxvDAEJ6CWH3WRWg-w1VXXYA6P9Ndluh3fdxiRVMpoZ2213QJ91NPIeYVeIw3E5l-uVVD3g_aRUek2zHJGaxX7eLAnUe-cTGeXHRqOz4dNNVCpZzqxASJImT7jQZDXZeNBkzD6HCmbBEEL0H_CXc2-ZVg5QCspDOpRXr1G-A4WRIPVCiN6I7ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec76e7285d.mp4?token=cjiExMHjTu9v_Ow4uuD-wseKljyxaOc3-QQFpmxijo-XijzLnhJ8XZnwkCt6vwaF3a2012FledA1aCvUV4ebeedMx9s6pFe4rZTXA4eI_ujKEy_bLI6t6UE03o155Bd5xu2iAXtma7kyxtESjhKeP_LxjNGoOcJCTxvDAEJ6CWH3WRWg-w1VXXYA6P9Ndluh3fdxiRVMpoZ2213QJ91NPIeYVeIw3E5l-uVVD3g_aRUek2zHJGaxX7eLAnUe-cTGeXHRqOz4dNNVCpZzqxASJImT7jQZDXZeNBkzD6HCmbBEEL0H_CXc2-ZVg5QCspDOpRXr1G-A4WRIPVCiN6I7ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیو تبلیغاتی بانو سیدنی سویینی برای novig
😟
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71591" target="_blank">📅 23:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71590">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1NIjOfYv9lsbi0I8685bK4-Mut3c9MtH5HiwSEpeD4WFHWzKujfHMuheYx7DLI_g_Q6_vcMoM_YgOSLG4vasFaJgRVazLezrtLdzB0A70pKJZIfG_ucI3Yb1ZDN-UCUwnfzcyi9NTodwnL9XPCo7B4LWRWDos1v0m_eqv7qcoDTHxD-9YUVP4M_T3r_MIfx8djRMmRM0yJvfMOBOwTuTxOkeodNNEodcY24CtWHbtocOa0YUFQnS-ibKsYrmZmMawDXUux1pLGnau-HlsyfSdVfalZI1r0qO0ZG8VA_4d4zDRm9dDU7IqHsvjZGOxKm5PxI3hYFgXgQGh_hmH64-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
🇺🇸
نیویورک‌تایمز:
مقامات ایرانی می‌گویند که رهبری این کشور طی هفته‌های اخیر بر سر دو راهبرد برای شکستن بن‌بست با ایالات متحده دچار اختلاف نظر بوده است: بازگشت به مذاکرات یا تشدید درگیری‌ها.
بر اساس طرح تشدید تنش، ایران حملات خود به اهداف آمریکایی - از جمله شناورهای نیروی دریایی و نیروهای نظامی ایالات متحده - را افزایش می‌دهد و هم‌زمان تلاش می‌کند با بالا بردن قیمت جهانی نفت، طرف مقابل را وادار به پایان دادن به محاصره دریایی کند؛ محاصره‌ای که تجارت ایران را فلج کرده و صادرات نفت این کشور را به صفر رسانده است.
ژنرال‌های تندرو، از جمله سرتیپ سید مجید موسوی (فرمانده نیروی هوافضای سپاه پاسداران)، طرح جنگی مفصلی را به شورای عالی امنیت ملی ارائه کردند. این طرح خواستار آن بود که ایران و گروه‌های هم‌پیمانش - به‌ویژه حوثی‌ها (انصارالله) در یمن و شبه‌نظامیان شیعه در عراق - دامنه حملات خود علیه نیروهای آمریکایی و زیرساخت‌های نفتی منطقه را گسترش دهند.
مسعود پزشکیان، رئیس‌جمهور، و محمدباقر قالیباف، رئیس مجلس، با این طرح مخالفت کردند و هشدار دادند که اجرای آن می‌تواند ایران را به جنگی بسیار گسترده‌تر بکشاند، موجب حملات هوایی سنگین‌تر آمریکا شود و بحران اقتصادی کشور را عمیق‌تر سازد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71590" target="_blank">📅 23:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71589">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f02f69702f.mp4?token=jDfEKh9m9HTRYoF2BDxKJtMB54ibPocYUkmDlHr1NDTk3ZI4LFz7BR9TBMR-ytSREo8l1kLADsOwWO3X8R2cHEVo4hulKjlvhlBQmuLk3rRcNOtT-A12IfbgJfm5eM17HAF3KM8Yj5UeD2fcznqbOVN7qBhTHUfXa_XimdLrssN4bDDm5HxD83sCGb6jKXa94I_qt0D8rEQXMi_ireJdWQTTZParcVlmfSExhc8Xzxar_CCA8Qd81EeXzzqAr4zJdsdyyZtyVz0Qy87n_7LL5o3kisAIJuEbo6BR28Nlnt0QvK-lAPga1zbNDuxknBStDOZeteFCrng6DNXDXEJzTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f02f69702f.mp4?token=jDfEKh9m9HTRYoF2BDxKJtMB54ibPocYUkmDlHr1NDTk3ZI4LFz7BR9TBMR-ytSREo8l1kLADsOwWO3X8R2cHEVo4hulKjlvhlBQmuLk3rRcNOtT-A12IfbgJfm5eM17HAF3KM8Yj5UeD2fcznqbOVN7qBhTHUfXa_XimdLrssN4bDDm5HxD83sCGb6jKXa94I_qt0D8rEQXMi_ireJdWQTTZParcVlmfSExhc8Xzxar_CCA8Qd81EeXzzqAr4zJdsdyyZtyVz0Qy87n_7LL5o3kisAIJuEbo6BR28Nlnt0QvK-lAPga1zbNDuxknBStDOZeteFCrng6DNXDXEJzTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کشتی که امروز صبح در نزدیکی جزیره قشم در جنوب ایران مورد حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71589" target="_blank">📅 22:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71588">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18ae06116.mp4?token=ZJwog6IGxBtm_RmYqlyRAUQnPvOYb6VOSJ8VZAVFb8TC86wQ39esuVJehKspzki2q34ol5Txu93Do2ERa1lnp5cAGetKlz8wGW3P5Q_mYpw1fx-xQxIKCLNFs6DEzqfnL1uCgADFGtZnAdf3uw8QECVH9AKQ2zNb5BjeM7xz1GdZmQkT-ZEz8Plz2etyBuPTEQb5XGIACo7FUElu7-TtM5JXR-65smtQAmp0IOs0fud-SNZXrxa_dP15WxnmyACQ3yvDkT7Zb-kCCzZoxL0aUajF8wY7AaCnpLJLD1qn-eaivmS--A3KFq3Z0CGle9ddTN9EnN5gb-7NQgFJzIB4rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18ae06116.mp4?token=ZJwog6IGxBtm_RmYqlyRAUQnPvOYb6VOSJ8VZAVFb8TC86wQ39esuVJehKspzki2q34ol5Txu93Do2ERa1lnp5cAGetKlz8wGW3P5Q_mYpw1fx-xQxIKCLNFs6DEzqfnL1uCgADFGtZnAdf3uw8QECVH9AKQ2zNb5BjeM7xz1GdZmQkT-ZEz8Plz2etyBuPTEQb5XGIACo7FUElu7-TtM5JXR-65smtQAmp0IOs0fud-SNZXrxa_dP15WxnmyACQ3yvDkT7Zb-kCCzZoxL0aUajF8wY7AaCnpLJLD1qn-eaivmS--A3KFq3Z0CGle9ddTN9EnN5gb-7NQgFJzIB4rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
زهران ممدانی شهردار نیویورک :
قربانی اصلی حمله ۱۱ سپتامبر عمه‌ی من بود که بعد از اون اتفاق نمی‌تونست با امنیت از مترو استفاده کنه چون حجاب داشت
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71588" target="_blank">📅 21:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71587">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oU33dNlGbP51v2miujiTF48-CM1Jr9PCDavI1H-ol7rm-CGzQbzCLIncqrM1uCMyauEStvSv8d0hPfga_iA8306NxN8l3DGShGZvpDwWXWOsz-jlLHKG1Rh3MeGCYLO5u5ugiK2TgnesZc1V9V9uYg0s7vMTNEYPyQgdUziK5R8YphsNcxzCE-vuILKX4SwBlZ6eRJ8hALnQmHeTp0CF5Dly2GZOQC2dP35CtKDpwt-I2NwB3QKmGJzV01OFcW45CrFnIFBWxz5Ln7BYKZqOwZQmQrPfMBVquVaPfCiS3WoQ2Z7-xMJObo4WGAGVrnpiZp2J7TXQqvinhzkXfhMnlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧩
🎮
کنسول بازی ps5 pro به قیمت تقریبا ۳۰۰ میلیون تومان رسیده!
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71587" target="_blank">📅 21:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71586">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/643027f01a.mp4?token=PS5J1tYfKZFUDK6TOpPGi6ygaTvrbYDzWYDSwbdbidl2tZ3xJ0ZhsBRbFnvU6fvAihvtVhDO0XpMagclES3Q0_U_tHL_D-nt9xqNO6QehtkRQkFiEXN_j93LZVM28ZlHnScxecZSa8LGTAmxMfCRsBUq1ziaCNzHt1DERCIvSOc6K_hlejmQyi371GFAA_mQN7SHeeLdvoY40oZ1WsuX0tdf05EHy2G3uh8eQMN6P8HXXIuy38o-8W7aCfRJ1ZS75EmHNFzqGPxcxyve4vJpx4wRytxsAUsAbOA0RQNID0v8Jv-i4o1S4ZqZBauVAbHHi0tL0s02RKvxbWu4kGlGpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/643027f01a.mp4?token=PS5J1tYfKZFUDK6TOpPGi6ygaTvrbYDzWYDSwbdbidl2tZ3xJ0ZhsBRbFnvU6fvAihvtVhDO0XpMagclES3Q0_U_tHL_D-nt9xqNO6QehtkRQkFiEXN_j93LZVM28ZlHnScxecZSa8LGTAmxMfCRsBUq1ziaCNzHt1DERCIvSOc6K_hlejmQyi371GFAA_mQN7SHeeLdvoY40oZ1WsuX0tdf05EHy2G3uh8eQMN6P8HXXIuy38o-8W7aCfRJ1ZS75EmHNFzqGPxcxyve4vJpx4wRytxsAUsAbOA0RQNID0v8Jv-i4o1S4ZqZBauVAbHHi0tL0s02RKvxbWu4kGlGpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
مدیر سامانۀ هوشمند سوخت:
خودروهای نوشمارۀ بالای یک میلیارد تومان سهمیۀ ۱۵۰۰ و ۳۰۰۰ تومانی بنزین نمی‌گیرند!
این خودروها ماهانه ۱۱۰ لیتر بنزین ۱۰ هزار تومانی می‌گیرند
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71586" target="_blank">📅 20:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71585">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇷
اطلاعیه قرارگاه جانفدا:
از سه شنبه 24 شهریور ماه قراره هزار گردان مقاومت ملی تشکیل بدیم که شامل کسایی هست که جانفدا ثبت‌نام کردن.
قراره به این افراد آموزش نظامی و امدادی بدن تا اگه جنگ شد، فورا اعزام بشن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71585" target="_blank">📅 20:22 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71584">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c23e20e2.mp4?token=H2olKdCe_2KQ4-AZHoLMfQIXRfmbIM-7dU2tzN_8_kH_qWPcaqh_WTuCtKBu5diO2_wu1d_rZjHRriCh1pk2qtEHC1Bz-Uqss0SuZjuZRx3VIrXZe3-Wr-mB500qjMoCxJS_I3yPW3xksXy8Tf96zbR-C1SZBii1iucTvDfQIkSxe-TGkB6JaQU764ty5uxIol5SHhRCOBLhIWawDIw_9exruSUbKuLmc9eRVRdCPWYArKYjX5ZSIl6uhaqZWpQ_wYZBEwnwex8dhvtahQHA025QBg9nZKNug7nYwROl9-E7bRiAEDp_iNCrFDt0NWea-5zQcl2eVqmIpRLOWpkdJlmaJCtqTvC0Z_qxYfeLTt0kc8grmR_byiq-H568NrCBQcalyEwX1lI39j5EjcR5Qw1gcmfBGkOuDaO_gg2pJIVTol01wkSP2jLgbVv2a5YBUndbfUO3xsqsjpEBkHKMm2uC6V5a_gGljKiQkyb6AIX8yPA4pfbV4nui08x0gZz7fVXyzvGO0mXQeZ-VigAY8qS-rUgOJIgc_LQqVWmJzcdnP-mpYFV3--une1mSUxixscrAepXvzMOYY2JAXMF0S5kRK_Nll5dNK6FMCEtQ1KOQBE4HRDo5QOrZPcVQuPeKdewgn-ajhoWh-IrN9_4FCc-10C6XpZvh_yXWQLXWDWY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c23e20e2.mp4?token=H2olKdCe_2KQ4-AZHoLMfQIXRfmbIM-7dU2tzN_8_kH_qWPcaqh_WTuCtKBu5diO2_wu1d_rZjHRriCh1pk2qtEHC1Bz-Uqss0SuZjuZRx3VIrXZe3-Wr-mB500qjMoCxJS_I3yPW3xksXy8Tf96zbR-C1SZBii1iucTvDfQIkSxe-TGkB6JaQU764ty5uxIol5SHhRCOBLhIWawDIw_9exruSUbKuLmc9eRVRdCPWYArKYjX5ZSIl6uhaqZWpQ_wYZBEwnwex8dhvtahQHA025QBg9nZKNug7nYwROl9-E7bRiAEDp_iNCrFDt0NWea-5zQcl2eVqmIpRLOWpkdJlmaJCtqTvC0Z_qxYfeLTt0kc8grmR_byiq-H568NrCBQcalyEwX1lI39j5EjcR5Qw1gcmfBGkOuDaO_gg2pJIVTol01wkSP2jLgbVv2a5YBUndbfUO3xsqsjpEBkHKMm2uC6V5a_gGljKiQkyb6AIX8yPA4pfbV4nui08x0gZz7fVXyzvGO0mXQeZ-VigAY8qS-rUgOJIgc_LQqVWmJzcdnP-mpYFV3--une1mSUxixscrAepXvzMOYY2JAXMF0S5kRK_Nll5dNK6FMCEtQ1KOQBE4HRDo5QOrZPcVQuPeKdewgn-ajhoWh-IrN9_4FCc-10C6XpZvh_yXWQLXWDWY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی آموزشی برای دخترای موتور‌سوار چنل که قطعا بکارشون میاد
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71584" target="_blank">📅 19:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71582">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eC_YffYl7YpxqZumEU9JBiTNc0E6dAouzUDnHUC5zh4idOK7fpz8GgKRtoQJ0L1vzDD8BiziGOgm2T49YYwpTpENEZ_VowimJMawoE25nJYIn0exN1OG6eKML-vDIe1-7QYruM3IJWalHwDzGN5ioOfTJJubXUUPB6JKNbOjaCzg8LVBaaoIsRIWcsCpNNAiq5OWo1jL_RNVzJSMP4cWb-U_FcthYRBapUJrcKcZAwf1Pf37Haeop7lajdsobv5e1KwKV1Q7gqbnFCBL575DDz5oqDKeqsuULVTnzcMP7Y6LyY9EsuLuBz5vqCYp4svMDOZOkLh7M1yj40-QEcn_gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UElo5nWDxaMxr72-Ren3ZlHGIHJuxl6u8eQMhcNhT6mRFj1Flrw3f-tToZ4YGSL7Em8etwzD0fOue3bezXLte7Ayffx-T-YKhxKj7HpmNxLfjs5m9VlPoszJMBjTLh6viMkq16YhqhyJUkqNewnv6QfT_uiKwu4jd4ztsEebsFdBF6jwSyqtD-5mNruMOkKZcu9uqcR0OkK6eVuM9l7-rkRQ4_bX8YyAKQ9o16jCjAX7VnsD8JhRWTLRynhOyYgFGLCxPRgW-ITa7REl4QCiAbBSiJZ9IipAMZy-9F1KiO7VN_6howQHr6aw4k2vG3TdxiDYN1DOKwnov604TplAlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👑
دفتر شاهزاده رضا پهلوی:دستگاه کشتار و سرکوب جمهوری اسلامی بار دیگر قصد جان یک زن جوان را کرده است. سودا (مرضیه) ابراهیمی شمس‌آبادی، بلاگر ۳۳ ساله اهل بندرعباس، پس از ماه‌ها بازداشت و تحمل شکنجه، تنها به دلیل فعالیت رسانه‌ای، در بی‌دادگاه رژیم با مجازات اعدام روبه‌رو شده است.
صدای سودا باشیم و از همه ظرفیت‌ها برای فشار بین‌المللی جهت توقف ماشین کشتار رژیم استفاده کنیم.
سودا ۳۳سال دارد و ساکن بندرعباس است.
او در تاریخ ۹فروردین بازداشت و اکنون با اتهاماتی چون "عکسبرداری از فاصله دور محل اصابت یک موشک و ارسال این تصویر برای یک رسانه فارسی خارج از کشور" به اعدام محکوم شده است.
او حدود شش سال است که به بیماری ام‌اس مبتلاست و علاوه بر آن از بیماری‌های پسوریازیس، نارکولپسی و کولیک معده نیز رنج می‌برد و نمیتواند در زندان بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71582" target="_blank">📅 18:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71581">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBTcxO30-jySps5clEbAU_TuvgZk_PhtkNBRW1YBSRi8ZyCWAcmO87mAWSGyRIqR5WzATOsLwJ0Ux75RdXfqYKBNJoVXxY-o6HEjz_uUt4dJceB-3s_EsvabO7spgDqPeDsO-iRxBEHWJdcy4WR4ISwq0Z2ANJ6Ic36TMSw1DthnqbRI_PW4edlsGqjSTUn_wGNoHYjVJfk6iQ_4T9o0M5V-yslYhsc7mIpqDdx1ni06UBzvuQGyRiAa5pVykVzoi0J33S27q64hl3d7VVmESyLHQOft7yAsNoa6wa8VHYN8wzgp75ctohSNGK8Mqkdsllb-X9r8tK-CDM89GmnVFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇺🇸
نیویورک تایمز:به گفته مقامات ایرانی، تندروهای ایران با صدور دستور حمله به سه کشتی تجاری در تنگه هرمز در تاریخ ۷ ژوئیه، مخفیانه توافق صلح با ایالات متحده را که اوایل همان ماه حاصل شده بود، مختل کردند.
گزارش‌ها حاکی از آن است که مسعود پزشکیان، رئیس‌جمهور، احمد وحیدی و بخش عمده‌ای از رهبری ایران از این عملیات بی‌اطلاع بودند.
بازرسان رد این تصمیم را به جناحی مرتبط با حسین طائب — روحانی بانفوذ و رئیس پیشین اطلاعات سپاه که از همان ابتدا با این توافق مخالف بود — رساندند.
حملات ۷ ژوئیه منجر به حملات متقابل ایالات متحده در روز بعد و همچنین یک کشمکش قدرت بزرگ در داخل ایران شد.
تا ماه سپتامبر، ژنرال‌های تندرو دست بالا را پیدا کردند و به جای بازگشت به میز مذاکره، راهبرد تشدید حملات علیه نیروهای آمریکایی و زیرساخت‌های نفتی منطقه را پیش گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71581" target="_blank">📅 18:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71580">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71580" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71580" target="_blank">📅 18:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71579">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpBsSZYGgB3XpIO_fvdHreTNYig7Y5MOBfmJ3mfKC55nyXDHDu9_pcWI0ht1B-1Q7aBjzUzhV3XAE_LBEUsHQIhnxfFEMVXepZ9xC180I8BI-iVosUc4nrqlclO_7eACFpamHDEx3VUFrmXm0G5OOgaVFsVJefMfmS9CFJoNSM54icmvseLCWaX8VtgY2HhwLhIlsM1Iil28h6gOAc4-lkYoYZq6EyEs3_mIs3HHa3aDrOH_UYeALtICHDNrPGkfH6TrGUr-fa_5C4JWO-Rx_u2o0rhO2nKdslg8rOvXJR3c45dHc9-qY79rnFWNPcw2GnVaxhgKtoWvoJttgjl95Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71579" target="_blank">📅 18:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71578">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfc5dc935e.mp4?token=pfXj8uA0IHH08RC-QaOj_EePZBAfz2rcAulnjhJc2KYJ6u-uMW3oiuBZCqZ39x02bhdQlYk6WWNDMEA3mJO08vZRpvmf9Sg00qePXkuWHTvsA-43WDTeoHX2Pgp2v24gvkeNcj3AhsepxZqClun0Vm_VHfmLb6XQMrUzXQfldIUWZtSkIYG-NTc6afIufXQgDDgy77Wf5IrKAU0bBochQaeo-D9nYHNNIm0CHIUPomLIAATD5WW3K7CzH0Nq563mxoNcjEWp5i7cRzxXHPh8BUrfc8yNnfLhgeuF2eYiwpCuUE-n8A2-WJqARx5SrHcVj9DvdEqr4yMI0jwcmZA1yUr6C4KCEBGpS3DnWUayAXQgjASD5TsDy5GuHPTjofeSprF570KTQXpjiiqNS3_9wqVJ0A18BqTel0IND5J-PkZnNzS_OhKd5MAtzqYJhTIyrNJY8Gw-5Ph86zEizuuZB8vJ8UTBZU-0P3zu0K4PlVSF4kF6ZkM78JTIpF2XGHg-_z7iCW_YokcinZdnDBBBkGQV1qbVVewIwKtWaT_tvnNkPsCaugxGH-ItcTojfQ4R_rTLyLzAK8Dxq70pTYgLnlER5WmcAh4Pzq_h-jJwevIbHNniYls4qG3TiIzKf4U9JohMWxrQOCiw5xTrv0fxXs4VbbqaGoGD6u4j15cbIpk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfc5dc935e.mp4?token=pfXj8uA0IHH08RC-QaOj_EePZBAfz2rcAulnjhJc2KYJ6u-uMW3oiuBZCqZ39x02bhdQlYk6WWNDMEA3mJO08vZRpvmf9Sg00qePXkuWHTvsA-43WDTeoHX2Pgp2v24gvkeNcj3AhsepxZqClun0Vm_VHfmLb6XQMrUzXQfldIUWZtSkIYG-NTc6afIufXQgDDgy77Wf5IrKAU0bBochQaeo-D9nYHNNIm0CHIUPomLIAATD5WW3K7CzH0Nq563mxoNcjEWp5i7cRzxXHPh8BUrfc8yNnfLhgeuF2eYiwpCuUE-n8A2-WJqARx5SrHcVj9DvdEqr4yMI0jwcmZA1yUr6C4KCEBGpS3DnWUayAXQgjASD5TsDy5GuHPTjofeSprF570KTQXpjiiqNS3_9wqVJ0A18BqTel0IND5J-PkZnNzS_OhKd5MAtzqYJhTIyrNJY8Gw-5Ph86zEizuuZB8vJ8UTBZU-0P3zu0K4PlVSF4kF6ZkM78JTIpF2XGHg-_z7iCW_YokcinZdnDBBBkGQV1qbVVewIwKtWaT_tvnNkPsCaugxGH-ItcTojfQ4R_rTLyLzAK8Dxq70pTYgLnlER5WmcAh4Pzq_h-jJwevIbHNniYls4qG3TiIzKf4U9JohMWxrQOCiw5xTrv0fxXs4VbbqaGoGD6u4j15cbIpk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ایران به‌شدت خواهان توافق است.
آن‌ها مدام تماس می‌گیرند. می‌خواهند توافق کنند. اما باید توافق درستی باشد؛
من تن به توافقی که خوب نباشد، نخواهم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71578" target="_blank">📅 17:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71577">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f46b70464e.mp4?token=SeALfdY0WLwvRu5QZsvo-nM_eqMLLCWPbBPVgSf8Fr5mZ2gICZBmx0LED-LBfw9CdETZth2lK2bINai04aQghd366G7dwL_e2-jYjztxXsM3UgO3suFO_C-Zyh_WfptOegYk_FGNZO131WnCyhyFgCpqnCVNNAy2gf8iAT2zeLNOjYcyIwCU_fCnqOoF6grRcR4MIwf0s4npFSTAeaped3Y3wKf1FfRxJO1g8LZH_aYnLs9dTy2tI_woW2y1BHnJxq3qX36cZFWpXLWJzKVO4LN-40UpoIiM5m1dClPg_VD9DKyKjE37_T9bEYHKcYI3Ey6yVvCXfsnNgqHhkdKIuFJLSqIAqR35p5OKOOiFNMvyzwmv2PepDAf1JXfmnaK_M2aMuHsF4wqu16AKzxaj8FXbGTj0WtbpqUCQEG9Xi7upUPbE5Fl9_vRLecyI6X2Zcp_OhkPCfWh6CKQSUquT9w82qK9cQQN3nWG1MVrnBn1Zn99xUNxQHFzKGfp65UJvSuUwteDrjQmho3T5bKzSnQrfqMHY_Skwk04q5Xua4kQay6v4W0H_HIhXDYASMHKeoz8Tnpy7nfLF4ABUfeQjLtEj6odPwrNL8tfrrk2cf_-2mlWXBrRb8cDwTjMveVAD84Cb050Us8r8Nr7ZNaVri9I3r96M7uBNgeHrtxAS83U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f46b70464e.mp4?token=SeALfdY0WLwvRu5QZsvo-nM_eqMLLCWPbBPVgSf8Fr5mZ2gICZBmx0LED-LBfw9CdETZth2lK2bINai04aQghd366G7dwL_e2-jYjztxXsM3UgO3suFO_C-Zyh_WfptOegYk_FGNZO131WnCyhyFgCpqnCVNNAy2gf8iAT2zeLNOjYcyIwCU_fCnqOoF6grRcR4MIwf0s4npFSTAeaped3Y3wKf1FfRxJO1g8LZH_aYnLs9dTy2tI_woW2y1BHnJxq3qX36cZFWpXLWJzKVO4LN-40UpoIiM5m1dClPg_VD9DKyKjE37_T9bEYHKcYI3Ey6yVvCXfsnNgqHhkdKIuFJLSqIAqR35p5OKOOiFNMvyzwmv2PepDAf1JXfmnaK_M2aMuHsF4wqu16AKzxaj8FXbGTj0WtbpqUCQEG9Xi7upUPbE5Fl9_vRLecyI6X2Zcp_OhkPCfWh6CKQSUquT9w82qK9cQQN3nWG1MVrnBn1Zn99xUNxQHFzKGfp65UJvSuUwteDrjQmho3T5bKzSnQrfqMHY_Skwk04q5Xua4kQay6v4W0H_HIhXDYASMHKeoz8Tnpy7nfLF4ABUfeQjLtEj6odPwrNL8tfrrk2cf_-2mlWXBrRb8cDwTjMveVAD84Cb050Us8r8Nr7ZNaVri9I3r96M7uBNgeHrtxAS83U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ماجرای ایران درست بعد از انتخابات میان‌دوره‌ای تمام می‌شود؛ شاید هم قبل از آن، اما قطعاً بلافاصله پس از انتخابات میان‌دوره‌ای پایان می‌یابد.
قیمت بنزین به‌شدت سقوط خواهد کرد،خب، من می‌دانستم چه کار می‌کنم و باید آن کار را انجام می‌دادم.
ایران نباید به سلاح هسته‌ای دست پیدا کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71577" target="_blank">📅 17:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71576">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a78bb4d113.mp4?token=pyt6aAvfXKlP9U2vTLnCPl5uvPKeSWGKgQAcO2sTAUSseQ3AMqIFii449FGIWcJj33w4_zns0nrDpo1gAyOWrDKmXpOswJeLvCufXAwkCPKpYiyxeWPYlm1HUI3s-T9CAK5uzZ2wX7n1gG1bf_Y7c2Amswg_YniTLvKaFoOARIFmHFM6DiT8Jdd_IsqESqCz8N0iAnmgtoSDSne-gMq5QUIL_EYEOmiNPlEFdBDZEQsQ9xMOnMH7h9z0oIjA07zJcReyZdLfCDppBAsvSlqraZvuVz266ymO_7fudEJlwksPW6N310V-jaMli69SCXSswRD-X36ixX80PHW-N-gBNDXPHnGZV4HldoQ42YL5qxv_9Etk23UTpaV-J_jzBH4uIgSYPf_GaFrA1SLdMHJ4rUjYsZny6yIHnB7Z4JWmfBU3zHR35vQNm5mJBO2YTFUAOtEE-rtEUfxDgrCt90o7ignmuQZj2ps4QewNQpTBYM0sVn81ifdcPn95FjxgZV7hbvumpv8vyDpQ0OewP3KDCQv9yvM8en7j3hlUY774axoC2fsa-C6w-zvgy2tbVccnR2Px9N0mecEwUopVqpUOT4DSPQM36nmr_P2bv_kcVaFJ5dBSt7LprHP0zLR3t9ClJel2C6WsUkKMirt-27LkBs37XD4uIDNTRIjzFaOIdjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a78bb4d113.mp4?token=pyt6aAvfXKlP9U2vTLnCPl5uvPKeSWGKgQAcO2sTAUSseQ3AMqIFii449FGIWcJj33w4_zns0nrDpo1gAyOWrDKmXpOswJeLvCufXAwkCPKpYiyxeWPYlm1HUI3s-T9CAK5uzZ2wX7n1gG1bf_Y7c2Amswg_YniTLvKaFoOARIFmHFM6DiT8Jdd_IsqESqCz8N0iAnmgtoSDSne-gMq5QUIL_EYEOmiNPlEFdBDZEQsQ9xMOnMH7h9z0oIjA07zJcReyZdLfCDppBAsvSlqraZvuVz266ymO_7fudEJlwksPW6N310V-jaMli69SCXSswRD-X36ixX80PHW-N-gBNDXPHnGZV4HldoQ42YL5qxv_9Etk23UTpaV-J_jzBH4uIgSYPf_GaFrA1SLdMHJ4rUjYsZny6yIHnB7Z4JWmfBU3zHR35vQNm5mJBO2YTFUAOtEE-rtEUfxDgrCt90o7ignmuQZj2ps4QewNQpTBYM0sVn81ifdcPn95FjxgZV7hbvumpv8vyDpQ0OewP3KDCQv9yvM8en7j3hlUY774axoC2fsa-C6w-zvgy2tbVccnR2Px9N0mecEwUopVqpUOT4DSPQM36nmr_P2bv_kcVaFJ5dBSt7LprHP0zLR3t9ClJel2C6WsUkKMirt-27LkBs37XD4uIDNTRIjzFaOIdjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آقای رئیس‌جمهور، آیا فکر می‌کنید کنگره باید آن ۵۰۰۰ دلار را تصویب کند؟
🇺🇸
ترامپ:
همان‌طور که گفتم، نمی‌دانم اگر جمهوری‌خواهان پیروز شوند، انجام این کار چقدر آسان خواهد بود.
صحبت از ۵۰۰۰ دلار برای تمام بزرگسالان کشور است و ما به‌راحتی از پسِ آن برمی‌آییم، چون درآمدهای کلانی داریم؛
وضعیت ما هرگز تا این حد عالی نبوده است. دموکرات‌ها نمی‌توانند چنین وعده‌ای بدهند، چون در آن صورت اوضاع بلافاصله به هم می‌ریزد و نابود می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71576" target="_blank">📅 17:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71575">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2f2319501.mp4?token=b1WnO7FW_LxLArs-4VRZ0WoDXVj4QzOdQa4iJvFQBHEsgtAftkhuojjCV9Fc66bygnJW1juPHQMuPCfIo8QaRQJBpAtfTBOXzS5NQzOaA-jnlaHVIwwAmErZm7zixVTOBGJLmAY8fcgTWfwa_7GLN6IHV68J7iUSJlaukSabe6RLHIwbunMQQ25ZQ5P2iTJnNQvC9maRjU_83w1MaTMbAwoqHZIagqOlylUbCP2NOHfruKaWggq0RBwXJKLJ19n9RJ3kgFkV_iS7_7_EBWkOSeD_EzNij_1kv7EG2iSH_1WEopOQdmATl16igHca7aATlExXLbplBFvgUD4QQ1Na5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2f2319501.mp4?token=b1WnO7FW_LxLArs-4VRZ0WoDXVj4QzOdQa4iJvFQBHEsgtAftkhuojjCV9Fc66bygnJW1juPHQMuPCfIo8QaRQJBpAtfTBOXzS5NQzOaA-jnlaHVIwwAmErZm7zixVTOBGJLmAY8fcgTWfwa_7GLN6IHV68J7iUSJlaukSabe6RLHIwbunMQQ25ZQ5P2iTJnNQvC9maRjU_83w1MaTMbAwoqHZIagqOlylUbCP2NOHfruKaWggq0RBwXJKLJ19n9RJ3kgFkV_iS7_7_EBWkOSeD_EzNij_1kv7EG2iSH_1WEopOQdmATl16igHca7aATlExXLbplBFvgUD4QQ1Na5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
نظر شما درباره دیدار کشورهای حوزه خلیج فارس با ایران چیست؟
🇺🇸
ترامپ:
برایم اهمیتی ندارد. این به خودشان مربوط است. اشکالی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71575" target="_blank">📅 17:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71574">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e5ba3545.mp4?token=kX-C7NkAMrocq_KexHQc9lLvPPGTwWneUxXs6AIGVxt1TDZkTNzLKt8jrS44bme6XDQPgIQ17xLl_izX8S3S2nI_WeMsmqddXor_VGx6yO9cELBuzR9EjOEf7IzG0IWxjJ_083hoRwdn2mdCSPOOvf1bST3bui-BNjdGSUBXvaGdNKI4Z0AbTHT90k_6gg0-wnfNOMO_F9-a4079qX4DZv9XyqOq_dt1NwLYiJRbE-cmeAlK9_-TZo_2B4RlvbENniX8HqPe3Q35A-0E-Iz8Qgvwq_-LL393BTsds2T12lkX_fg4pqp-iaadZg62GBg77lv-zc15MbJGBHdmkmkFWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e5ba3545.mp4?token=kX-C7NkAMrocq_KexHQc9lLvPPGTwWneUxXs6AIGVxt1TDZkTNzLKt8jrS44bme6XDQPgIQ17xLl_izX8S3S2nI_WeMsmqddXor_VGx6yO9cELBuzR9EjOEf7IzG0IWxjJ_083hoRwdn2mdCSPOOvf1bST3bui-BNjdGSUBXvaGdNKI4Z0AbTHT90k_6gg0-wnfNOMO_F9-a4079qX4DZv9XyqOq_dt1NwLYiJRbE-cmeAlK9_-TZo_2B4RlvbENniX8HqPe3Q35A-0E-Iz8Qgvwq_-LL393BTsds2T12lkX_fg4pqp-iaadZg62GBg77lv-zc15MbJGBHdmkmkFWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
در نهایت ما آنجا را ترک خواهیم کرد، مگر اینکه تصمیم بگیریم بمانیم و نفت را برای خود نگه داریم؛ درست مثل ونزوئلا.
دیگر درباره ونزوئلا حرفی نمی‌زنید، مگر نه؟ خوب به این موضوع فکر کنید: میلیاردها و میلیاردها و میلیاردها دلار.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71574" target="_blank">📅 17:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71573">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇾🇪
حوثی‌های یمن تصاویر مفصلی از عملیات نظامی جدید خود با عنوان «و خداوند از نظر قدرت و کیفر، سخت‌گیرتر است» منتشر کردند؛ ویدئویی که صحنه‌های نبرد در جریان تهاجم اخیر آن‌ها در ساحل غربی را به تصویر می‌کشد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71573" target="_blank">📅 17:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71572">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9fa2fdcc9.mp4?token=Cb0SvG0p46YvokreNG8a57p6LnQDo7fMsHqOEH5k-85NLTb0sYn40_rIJxHRtaLsCIXpStBqpE447ouNKPEGGnSuSUGnwYZamFAV3YnR4DRGATDuXvMlGN5hkj4MMfXvjHMnr0fN6w5wACvRiZ_7HomfrvjdLrCLJZXXpBxzrgR0Yn0sZuAITXjoXNEOacYzKAUpqlVI5GsSfMr5Oyb6qxgZyVQR7AEdaUKmxl2ZFiKORJ5OJQrpxHqfsLiv9CfHhZQ9JyzWO6jc8PpB3d_iXjXAYFu7vQLAj817hb5IogL9aUTUxRtyT1EShaVrRMNkZK7LTeZ1Agsy7tMc92Wuww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9fa2fdcc9.mp4?token=Cb0SvG0p46YvokreNG8a57p6LnQDo7fMsHqOEH5k-85NLTb0sYn40_rIJxHRtaLsCIXpStBqpE447ouNKPEGGnSuSUGnwYZamFAV3YnR4DRGATDuXvMlGN5hkj4MMfXvjHMnr0fN6w5wACvRiZ_7HomfrvjdLrCLJZXXpBxzrgR0Yn0sZuAITXjoXNEOacYzKAUpqlVI5GsSfMr5Oyb6qxgZyVQR7AEdaUKmxl2ZFiKORJ5OJQrpxHqfsLiv9CfHhZQ9JyzWO6jc8PpB3d_iXjXAYFu7vQLAj817hb5IogL9aUTUxRtyT1EShaVrRMNkZK7LTeZ1Agsy7tMc92Wuww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی مملکت یه سری کارگاه آموزشی گذاشتن و به افراد بالای 60 سال آموزش میدن که چطوری اسنپ بگیرن.
هزینه شرکت تو این کارگاه بین ۱ـ۲ میلیونه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71572" target="_blank">📅 16:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71571">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cc03db8a0.mp4?token=a8AB7E8K5HM-KZbCWlkiK-T-VEKFOhVjVnVfy-vyN3Z_5cdqw7PoUuzhgAL_jBul5iqbX6CgDn40m_P9_oIZVQ9kyN0uoCntPdJ0v3WQ7VQ8XzTHHtLXx3lP_jye1uWim5y7X5AMEEN4Go7mbuPuXu1kH3gOf5ng0A-CPGrU_ec-mueSvtKSjdTKMKyoKqioH2iTvG-dzBEkldx1PUp2G9zJ0mv6DAbxFBH5PjXQgEGmVX1iE7rvngkM8gq-UtXWK9942L8iOpOhqFmtyXGy8IT5hj3zfMhB-fUFpT7MdOwsEaNygQuaZ3ER_qwPiwAAjQuEkPmh8BMO36lydaA8QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cc03db8a0.mp4?token=a8AB7E8K5HM-KZbCWlkiK-T-VEKFOhVjVnVfy-vyN3Z_5cdqw7PoUuzhgAL_jBul5iqbX6CgDn40m_P9_oIZVQ9kyN0uoCntPdJ0v3WQ7VQ8XzTHHtLXx3lP_jye1uWim5y7X5AMEEN4Go7mbuPuXu1kH3gOf5ng0A-CPGrU_ec-mueSvtKSjdTKMKyoKqioH2iTvG-dzBEkldx1PUp2G9zJ0mv6DAbxFBH5PjXQgEGmVX1iE7rvngkM8gq-UtXWK9942L8iOpOhqFmtyXGy8IT5hj3zfMhB-fUFpT7MdOwsEaNygQuaZ3ER_qwPiwAAjQuEkPmh8BMO36lydaA8QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
ویدیویی جالب از یک پهپاد اوکراینی که به سمت یک کشتی روسی در حال حرکته و یه بالگرد روسی تلاش می‌کنه اونو بزنه ولی، این پهباد در نهایت خودشو به کشتی میرسونه و منفجرش میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71571" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71570">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31fa8bd2c9.mp4?token=dO6z-tE9xhCp5OGePrI0RLOFQgjCHUGRdmB6vUYlOohjdqDxbU88aBlru01toNithPLjFbgavXSL19hpSs28TYjFv_pGwHrcGD5GxVXV1yNSi3iV32Yc-EP2P67wUXvXIPjzd4JOTPZQZA_R9p-OL58-6RRL41NkNct_wTiyJR-1Zsj2UWWffzzCCqp8LEvTN-67fCRi4HoB8_PyhTOnx48k1G1NjsoF2rO5oI96t3DNwe-njOjZCBzNRBRC647u8_1Dp79ox40_zm2x5GiPaxQG1oXfvaPAb8Ph9EcrLQjWuJQS98Sa2SFTKKzlqSgAb8DNZpCsyJXeDX28upGpgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31fa8bd2c9.mp4?token=dO6z-tE9xhCp5OGePrI0RLOFQgjCHUGRdmB6vUYlOohjdqDxbU88aBlru01toNithPLjFbgavXSL19hpSs28TYjFv_pGwHrcGD5GxVXV1yNSi3iV32Yc-EP2P67wUXvXIPjzd4JOTPZQZA_R9p-OL58-6RRL41NkNct_wTiyJR-1Zsj2UWWffzzCCqp8LEvTN-67fCRi4HoB8_PyhTOnx48k1G1NjsoF2rO5oI96t3DNwe-njOjZCBzNRBRC647u8_1Dp79ox40_zm2x5GiPaxQG1oXfvaPAb8Ph9EcrLQjWuJQS98Sa2SFTKKzlqSgAb8DNZpCsyJXeDX28upGpgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری صداوسیما:
از جنگ تحمیلی دوم حدود ۱۵ ماه اینا هست میگذره دیگه
مقامات صهیونیستی و امریکایی پر تکرار گفته ان که با حمله به ایران ظهور مهدی موعود رو به عقب انداختیم
دلیل اصلی بمباران تاسیسات هسته‌ای ایران به عقب انداختن ظهور بود
اونا نگاهشون آخرالزمانی هستش
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71570" target="_blank">📅 15:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71569">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d522fc2430.mp4?token=cAAEdZTFPJ4vICtfg278BLKLUEiA2UKp8i6XH491KBwFqdz4ZYiTge7qcqHxqFKDMnDi3w96Mw_w1GN7n-I2FjDvzaQpZsz3Ur9gpM336yd-cNU8uwl1gLBWjqZBeBkaYCLtDZ7v7kv7Hj98bmMHznvyt4G6w20WjhDRmFzuSJe6dpjXicMq_0OA56-EgpSuEjAXvx0D2pHvHLn9hWoWnKeyFVFRs-DG7Slv0lsA08LnrrxiDAKgdhrj0qGXPVgHkAJQG-t2VLccUuD6HnNfQDMLnb33yYCXoszAnjeO0bZT8lrSS0fg4oX0vYLcDaXBscDls0oQeRHtK0Bmm0D4RzSDinXB2rXae08HrWUoHH4Un70GtuSWwd5rla5yd6O1sQ_Q2vBzzr-bour1jJ-yI8GSpLxQwByB9H0f4YiLVDW77SHYeUknAlS_8eHkqAA6IixrOJVMyPhRyI-AkXEksbY4_mxp-DRzSfEyYaFtYLCwZFDvojlmlMXUydijlwzV9O8JnvK650wtCpiR1_zBZB3-n-JGbqczhDp-ZKVCodqAJ9NiivironV9cIPtrjNTxY7JOM2-h8cHhUTP5dJL_iE_Q8O0EO7wGfT7m4Qg2bIFhxl-8Tu9HarM32-Nbh_6lXyw_GaJnViNA-pLDz-SDRAdT4Q2ZXkbiVxfbCDR1og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d522fc2430.mp4?token=cAAEdZTFPJ4vICtfg278BLKLUEiA2UKp8i6XH491KBwFqdz4ZYiTge7qcqHxqFKDMnDi3w96Mw_w1GN7n-I2FjDvzaQpZsz3Ur9gpM336yd-cNU8uwl1gLBWjqZBeBkaYCLtDZ7v7kv7Hj98bmMHznvyt4G6w20WjhDRmFzuSJe6dpjXicMq_0OA56-EgpSuEjAXvx0D2pHvHLn9hWoWnKeyFVFRs-DG7Slv0lsA08LnrrxiDAKgdhrj0qGXPVgHkAJQG-t2VLccUuD6HnNfQDMLnb33yYCXoszAnjeO0bZT8lrSS0fg4oX0vYLcDaXBscDls0oQeRHtK0Bmm0D4RzSDinXB2rXae08HrWUoHH4Un70GtuSWwd5rla5yd6O1sQ_Q2vBzzr-bour1jJ-yI8GSpLxQwByB9H0f4YiLVDW77SHYeUknAlS_8eHkqAA6IixrOJVMyPhRyI-AkXEksbY4_mxp-DRzSfEyYaFtYLCwZFDvojlmlMXUydijlwzV9O8JnvK650wtCpiR1_zBZB3-n-JGbqczhDp-ZKVCodqAJ9NiivironV9cIPtrjNTxY7JOM2-h8cHhUTP5dJL_iE_Q8O0EO7wGfT7m4Qg2bIFhxl-8Tu9HarM32-Nbh_6lXyw_GaJnViNA-pLDz-SDRAdT4Q2ZXkbiVxfbCDR1og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇾🇪
تصاویر بسیج قبایل حوثی، ستون‌های طویلی از خودروهای تویوتا (تکنیکال) مجهز به سلاح را در بیابان به نمایش می‌گذارد؛ تصویری که نماد کلاسیک جنگ یمن است.
قبایل «بنی‌حشیش» برای پیشروی به سوی «مأرب» — آخرین پایگاه عمده دولت در شمال — اعلام آمادگی کرده‌اند.
وانت‌های تویوتا مجهز به سلاح، همچنان ستون فقرات نیروی زمینی حوثی‌ها را تشکیل می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71569" target="_blank">📅 14:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71568">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRCZJIJuQWtzaUxPAoL_6TT8UqFzw9B-EEvM19uEXfeEDkWc6E2ty_joRTlcX2YYNYsVAoMfZuLedG3BIRLFKphQlfjx9NjmwgAGIgNT5jjesjmFBVZnQ4aCX79YODsjO2BJd0Yw1goqYiofoK_WwUmVSp-Bog_OEIMHe83XbiZSnmMKqcTHywa3SjF53gozJGVONOc4oV3yde9C7GnzDY77cSWCK-tz1jb0qgdid638H5xRTMRJDdDsoCJeXGkao-ds2Q_E4jp1twGEGzsB0lawMSjxMUd6cGEf-CguQ98yCHQWkKpcJoXPX_P1dSXu4OCQr-VoU4kGALpMHa1HrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
📰
اکسیوس: محمد بن سلمان، ولیعهد عربستان سعودی، روز پنج‌شنبه دو بار با دونالد ترامپ، رئیس‌جمهور آمریکا، تماس گرفت و از ایالات متحده خواست تا هم‌زمان با پیشروی حوثی‌ها به سوی یک نقطه راهبردی و حیاتی در دریای سرخ، به آن‌ها حمله کند.
ترامپ این درخواست را نپذیرفت و مقامات آمریکایی اعلام کردند که در حال حاضر هیچ برنامه‌ای برای مداخله مستقیم علیه حوثی‌ها وجود ندارد.
دریاسالار کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده (سنتکام)، نیز روز پنج‌شنبه برای هماهنگی‌های اضطراری به ریاض سفر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71568" target="_blank">📅 14:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71567">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/363bcb9915.mp4?token=eHcCaHwzZNauaXrVghd8dA7RhBYdmqssfex8Z6vYxWQkwsw3B-yLcFNNYR6K4w5U2ImFxMir8I8VqrFdkvkD-p3sh7h1V2Pnhp1H0iFGvC50GRJY-mEEhbrib_e_VqSN3xyX6APmvpPNzhq7MFXPAqIrQ12oomnPTNgO3hgw1R974Z9Ap8XkJecp87hlEkjgdEXIY4MUkxGtMkVoEzcEaqB9N6YzCLIDUKLPr6pRAAZo1IDscceyBWFQ2tOnDazFtBDR1OJ0xztumBb2d9uIM5VTts_nF7tIpXPFAbJnjmoEVxQQv2Sm98__F-l8Rhxxd1c2yt7TWjNp_E4pz8mWoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/363bcb9915.mp4?token=eHcCaHwzZNauaXrVghd8dA7RhBYdmqssfex8Z6vYxWQkwsw3B-yLcFNNYR6K4w5U2ImFxMir8I8VqrFdkvkD-p3sh7h1V2Pnhp1H0iFGvC50GRJY-mEEhbrib_e_VqSN3xyX6APmvpPNzhq7MFXPAqIrQ12oomnPTNgO3hgw1R974Z9Ap8XkJecp87hlEkjgdEXIY4MUkxGtMkVoEzcEaqB9N6YzCLIDUKLPr6pRAAZo1IDscceyBWFQ2tOnDazFtBDR1OJ0xztumBb2d9uIM5VTts_nF7tIpXPFAbJnjmoEVxQQv2Sm98__F-l8Rhxxd1c2yt7TWjNp_E4pz8mWoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
کنعانی مقدم:
اگر رهبری اجازه دهند، ظرف ۲۴ ساعت از سلاح هسته‌ای استفاده خواهیم کرد
خرید فیوز هسته‌ای از کره شمالی، کار خیلی ساده‌ای است و ۵۰ تا فیوز می‌توانیم بخریم
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71567" target="_blank">📅 13:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71566">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f67e4c7321.mp4?token=G2RUTzMQte1H-6i5vUc93VXrTGDMw7zcemCGYdg7lrBoK7pFLZIX1OS8dseMTNonlsJUo-C1WPYROC0dm0qoUe3qVob9MITpm0HK2nR5D2YMNxLcMevnk_GCIMJdN23QuZ_8eygbRXOOwIHa7SJmCIT9yos-IrTk17o1r83tcz0q9P-c9lTxHKG9ntpOZv_4Lh23Qs7yiF21_-a2Pkz1-EgtcTkGEn9kgAAL-6YKmO453BtcG7cT6taP5NkmGzIYzj0ZBAnPPK5jluZ-FGPk3YMBwNMkRfrtxfONH8EzCs2uC_AivejI5AKHEfik3H_GXS9tu2T-Pewweh87tO00-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f67e4c7321.mp4?token=G2RUTzMQte1H-6i5vUc93VXrTGDMw7zcemCGYdg7lrBoK7pFLZIX1OS8dseMTNonlsJUo-C1WPYROC0dm0qoUe3qVob9MITpm0HK2nR5D2YMNxLcMevnk_GCIMJdN23QuZ_8eygbRXOOwIHa7SJmCIT9yos-IrTk17o1r83tcz0q9P-c9lTxHKG9ntpOZv_4Lh23Qs7yiF21_-a2Pkz1-EgtcTkGEn9kgAAL-6YKmO453BtcG7cT6taP5NkmGzIYzj0ZBAnPPK5jluZ-FGPk3YMBwNMkRfrtxfONH8EzCs2uC_AivejI5AKHEfik3H_GXS9tu2T-Pewweh87tO00-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎯
ویدیویی از هدف قرار گرفتن نیروهای انصارالله توسط نیروی اسنایپر مورد حمایت عربستان سعودی
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71566" target="_blank">📅 13:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71565">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0000373bd7.mp4?token=qO9w4Sx9jOS3RX0YUP5PHdwQdYD7jfrRLHhn5AQPz2gxh9SnDHDospYyIfxev_lX0CbbWOcKIdIlUKs-Avb13Qhj78Eo6oHWIr8SB6Z_Ap1N_bmtkjnT0T-ubMPjqhXmi3E_xv3AUAZ61OZBqmMK4yWbXP73dadRIdR_QsDqHqMWU71adJNU61FpbLPKpoD7lF4pk6LGBKDAtmMKpTM5Tf_TuGSJ1CE_BqKIfpofJ6gPDn3ImbCLogUYivdcXIdNicmudfwnQg9dKahxEt4ipfxqStoIlnBXIsT7ucZHxN6c4ofH7Y6t91mUw4GiNFYwHBoYX9efJbSgLuySqZ8KoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0000373bd7.mp4?token=qO9w4Sx9jOS3RX0YUP5PHdwQdYD7jfrRLHhn5AQPz2gxh9SnDHDospYyIfxev_lX0CbbWOcKIdIlUKs-Avb13Qhj78Eo6oHWIr8SB6Z_Ap1N_bmtkjnT0T-ubMPjqhXmi3E_xv3AUAZ61OZBqmMK4yWbXP73dadRIdR_QsDqHqMWU71adJNU61FpbLPKpoD7lF4pk6LGBKDAtmMKpTM5Tf_TuGSJ1CE_BqKIfpofJ6gPDn3ImbCLogUYivdcXIdNicmudfwnQg9dKahxEt4ipfxqStoIlnBXIsT7ucZHxN6c4ofH7Y6t91mUw4GiNFYwHBoYX9efJbSgLuySqZ8KoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
این رهبران جدید و رهبران واقعی که رئیس‌جمهور ترامپ از آن‌ها صحبت می‌کند، چه کسانی هستند؟
🇮🇷
پزشکیان:
به گمانم باید این را از خود او پرسید، چرا که هر روز حرف متفاوتی می‌زند.
یک روز می‌خواهد ایران را نابود کند و روز دیگر می‌گوید ما دوست ایران هستیم؛ یک روز می‌گوید ما را به رسمیت می‌شناسد و روز دیگر می‌گوید ما را قبول ندارد.
بنابراین، ما مطمئن نیستیم که باید کدام اظهارنظر را بپذیریم و بر اساس کدام‌یک عمل کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71565" target="_blank">📅 12:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71564">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71564" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71564" target="_blank">📅 12:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71563">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXT2ssQdi5CQmEqAv9GCteTNyV1iqTtUUO9Ds5nkIoA3txWlYJwuZXJvuZSdHykzdEmzpOcqpltjHunIaYT4CMHENq5b7MtxOyAC9AOQ77ikFTdSkfjSg_y-O05s8IPcnqUmPTQ3fO7sPD9ETkFSaFFv07PDFw8SLGxp9EWsNjp88hwIKa4nGj0oaOqaJTb512OsX3bfjOPZjGPyjwtfBc6IXQvK9gni34AFrdRuxP3ZtShBv9nFMzm_SsmVldx3BwPdZI8P9APRCnoCDTZZyFO31WAdhFlvYLEbC-wjMTKaqCHSjpHgvR484RN_ovxFdohXiHXqhQ4V73A6IsnOHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد بزرگ منچستر در راه است!
نبرد هیجان انگیز
⚽️
منچستریونایتد
🆚
منچسترسیتی
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ دربی اخیر منچستر:
⚽️
منچستریونایتد: ۲ برد، ۲ تساوی، ۱ شکست و ۵ گل زده
⚽️
منچسترسیتی: ۱ برد، ۲ تساوی، ۲ شکست و ۵ گل زده
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71563" target="_blank">📅 12:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71562">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Stlu8cRJyH4D6bLCfkk4pQ63Ws8sI-hAxBMqXS8QF9tblzOTT2NZtviRqzKWyiZBYaDynKml6nV0IKgME63iaWROXOe6c21hWxWrLK2SWxm8kSNKbcUaHbbqgD-qLd1PIWRKjvpcqpTyfQ33gIqY9tmPc6ywGsY-bCZwdWbhn1znm5ipal86SJrAe8NadHSjGu5m38cpkL-j8xr3Dvdc0MrWH_asWhd-9d_XRjPVJybdfHGoyOVE3nS8COGpN7Mj6wnRuiLzl7y48f420oFq5i8m9LMqWls0NjsDJCyBf2dPcxPgQX2uVIZNNHp9r9Ol2Jh2zd0gqZZgqOAxeUraAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
روز یکشنبه در گزارشی اعلام کرد که بر اثر اصابت یک پرتابه ناشناس به شناوری در حال عبور از تنگه هرمز، در آن کشتی آتش‌سوزی رخ داده است.
این سازمان اعلام کرد که مقامات محلی در حال کمک به تخلیه خدمه کشتی هستند. در این گزارش، نام شناور یا اطلاعاتی درباره تلفات، خسارات و یا پیامدهای احتمالی زیست‌محیطی آن ذکر نشده است
.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71562" target="_blank">📅 11:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71561">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇷
🇯🇴
ویدئویی از پرتاب انبوه موشک‌های رهگیر «پاتریوت PAC-3» از پایگاه هوایی «موفق سلطی» در اردن در سه روز گذشته، برای مقابله با موشک‌های بالستیک ورودی ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71561" target="_blank">📅 11:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71560">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c7237eb3.mp4?token=dGG8p-YHNrDtU3i7Th_CRjJmvvoGc2OSEtmq9w__v-RLFWOJ1-BbLN0YPMoaiiptA5ngMlkV9rZkfAhKhNsK2EFnslkmwJzoaaawyvid2SZYJKmImET8LlykWU_Nx1-X85rpF-xSeEr66jlMdtcjdgqs9oeaugN7sf7CHODF3xiAc2nOqFoOcJwuXibhF3ZqmU1HcJBD4eteE6Y3Mql64SwvsmZpvVVftjzyLkd6xTh1-J8PEw3Od3srb9WzPvCVnWuw9SaXP6QucPy-f8cfZYr1SMX9GotMP3VXS6lm-kmo3ZTGlfzfB4PFNR2QaKAGXj-7tmFVyYO30l846fKZ0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c7237eb3.mp4?token=dGG8p-YHNrDtU3i7Th_CRjJmvvoGc2OSEtmq9w__v-RLFWOJ1-BbLN0YPMoaiiptA5ngMlkV9rZkfAhKhNsK2EFnslkmwJzoaaawyvid2SZYJKmImET8LlykWU_Nx1-X85rpF-xSeEr66jlMdtcjdgqs9oeaugN7sf7CHODF3xiAc2nOqFoOcJwuXibhF3ZqmU1HcJBD4eteE6Y3Mql64SwvsmZpvVVftjzyLkd6xTh1-J8PEw3Od3srb9WzPvCVnWuw9SaXP6QucPy-f8cfZYr1SMX9GotMP3VXS6lm-kmo3ZTGlfzfB4PFNR2QaKAGXj-7tmFVyYO30l846fKZ0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
نظرات متناقض هادی چوپان درباره هانی رامبد:
بعد از قهرمانی
بعد از جدایی
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71560" target="_blank">📅 11:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71559">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097559287c.mp4?token=ncmj1F_Z4NfHhCFvAXRZscapT9A5WWsgy15iufFwKpghNJ_rey18SSG9xX762PX5e59isIe2Qph6OdsvUcAWx2wlAoxfGDygO82TUFLrX7Fc4NJLH-gkgJliydEMMIynOOVXYzlBFURTWt39FmOavszr9v7olCP10CDfXs44M7ajgN7iaYG3Flbtutvk9v-LEoAc4MhipOKDijwGur72XYWyt33YnoWJrLc6ig_np7c_LkituH5hj1tQT4cXskn7sjqQECbToXzVQvT6QZRwambOMeUCr1ZaCflGUdkcHI6IhPnoPlCoZR20ijTEDonI_WWH50F5h4z2rtZ8GdSyxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097559287c.mp4?token=ncmj1F_Z4NfHhCFvAXRZscapT9A5WWsgy15iufFwKpghNJ_rey18SSG9xX762PX5e59isIe2Qph6OdsvUcAWx2wlAoxfGDygO82TUFLrX7Fc4NJLH-gkgJliydEMMIynOOVXYzlBFURTWt39FmOavszr9v7olCP10CDfXs44M7ajgN7iaYG3Flbtutvk9v-LEoAc4MhipOKDijwGur72XYWyt33YnoWJrLc6ig_np7c_LkituH5hj1tQT4cXskn7sjqQECbToXzVQvT6QZRwambOMeUCr1ZaCflGUdkcHI6IhPnoPlCoZR20ijTEDonI_WWH50F5h4z2rtZ8GdSyxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
تلاش ابی برای بوسیدن دست یکی از بازیگران برنامه عشق ابدی که ویدئوش به شدت در حال وایرال شدنه!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71559" target="_blank">📅 10:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71558">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427cd49fec.mp4?token=hYPBafyd6MAgrBtpBeTCg263Cc-5OJD4t5ooo0Qgrc9dqwougkD_KcU6-Q0GcgvEWfqnhxLPDngntRHQfaCD6chkk7TPRMHou6wuz7TzMmS2lMCSLOA3pZ7fPN_dFa5kIaiZKVvDW5xPjQakFKjUmcAXHO9LdI6cmrPLJHSEp0ltj20uaaL9UStgjmrDMJgXwPLvTngfoB80axNePehqLAY13cQ7pq_4rDzX824lArN6l6sUjzRTGWbCHV4HwDAJi1Y4htc-lgZHrWQUlt_qPBj9ko_nko6lj4Cl6wQmy5HEtE3IInuxqkVmWtIXFU2RWQD2MVjCOY_eqYBzqpkEqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427cd49fec.mp4?token=hYPBafyd6MAgrBtpBeTCg263Cc-5OJD4t5ooo0Qgrc9dqwougkD_KcU6-Q0GcgvEWfqnhxLPDngntRHQfaCD6chkk7TPRMHou6wuz7TzMmS2lMCSLOA3pZ7fPN_dFa5kIaiZKVvDW5xPjQakFKjUmcAXHO9LdI6cmrPLJHSEp0ltj20uaaL9UStgjmrDMJgXwPLvTngfoB80axNePehqLAY13cQ7pq_4rDzX824lArN6l6sUjzRTGWbCHV4HwDAJi1Y4htc-lgZHrWQUlt_qPBj9ko_nko6lj4Cl6wQmy5HEtE3IInuxqkVmWtIXFU2RWQD2MVjCOY_eqYBzqpkEqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئو وایرال شده از 9 اسفند - روز شروع جنگ و بمباران تهران و واکنش  دانش‌آموزانی که خرکیف شدن
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71558" target="_blank">📅 09:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71557">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🇮🇷
امیر تیموری فرماندار شهرستان قشم:
یک کشتی تجاری حدود ساعت ۵ صبح امروز در محدوده جزیره هنگام و ساحل شیب دراز جزیره قشم مورد اصابت قرار گرفته است.
در این حادثه  یک نفر شهید  و سه نفر مجروح شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71557" target="_blank">📅 09:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71556">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyngvsEzPasDHbyrLqBFjmJCvmZU-zVnSUCOMgbOqadhks-jHtK5xqnlqlLHqnvdQkLKIPHH1IcSc-wW_m0GPa96weMjEeS-XK-MiQ5F0QBBpk_nxbERfSLHhspfPUvR9Zwu2ApzpclpP23fBxqI3QUcjNm15obl6sx47HM0JUbv5_6HzsNd-XvhCCqVabHxj8ng5z5UOJtQo6LRr_0JzYoA7N0LkD9Qli53gbmL_OpqU36mRqMqMpOFA5Js_99vZ3Yvjjyu1WWndW8Ih86oM6s0EgN0iIldncYlOnHqJVSqthxjH47yVHpm-PYqo2EZ2CTvKrsQokDAckopZQx1_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇳
🇮🇷
📰
وال استریت ژورنال:
مقامات آمریکایی می‌گویند ایران پیش از حمله موشکی بالستیک ۱۷ ژوئیه به پایگاه هوایی «موفق سلطی» در اردن — که منجر به کشته شدن سه سرباز آمریکایی و زخمی شدن چهار تن دیگر شد — تصاویر ماهواره‌ای با وضوح بالا از نهادهای چینی دریافت کرده بود.
این مقامات معتقدند که تصاویر مذکور با این حمله مرتبط بوده و احتمالاً به ایران در شناسایی دقیق‌تر اهداف ارزشمند کمک کرده است.
آن‌ها دولت چین را به مشارکت مستقیم در این حمله متهم نکرده‌اند و هویت نهادهای چینیِ دخیل در این ماجرا نیز مشخص نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71556" target="_blank">📅 09:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71555">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🦖
2 چالش، 2 کد مخفی، 2 جایزه 1$ در سایت بین‌المللی TREXBET !   فردا در دو زمان مشخص، عکس‌های چالشی داخل استوری کانال منتشر میشه؛ اما کدها همین‌طوری به دستت نمی‌رسن…
👀
🔎
باید با دقت بگردی، Promo Code یک‌دلاری رو پیدا کنی و قبل از بقیه داخل سایت ثبتش کنی! …</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71555" target="_blank">📅 01:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71554">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOe2ZyJuUtHmCJF3NvzmW0lzkb7qYatnMURNTTMlcAwF6ZvYCmYzwocxGu7E3Qx83oh3cis69ptD15FENQwsx1-7Nmu3td7vhh4l8kk0rO800qrtlDtmtEJlMZs9KgwkEN7hlfcrENdmZffPy1ydMX3o4mghRzlG0nDMut9lfaho0vyyBhHweOK11cwaswzsYY9VsLfY99KTuB36n1dGtGcuuzUbvBsBU-smmQAUr9cbOohF-sYdTe8oOzKfTQqSVpM7Yrvoz8PPOuF0Ya6xbyDnlb9ElgLZRf2nHYHzypFT-V15Ul5F6ns7_4q8PPDHEra_lzEhKuFtk6IMrJQkQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
2 چالش، 2 کد مخفی، 2 جایزه 1$ در سایت بین‌المللی
TREXBET
!
فردا در دو زمان مشخص، عکس‌های چالشی داخل استوری کانال منتشر میشه؛
اما کدها همین‌طوری به دستت نمی‌رسن…
👀
🔎
باید با دقت بگردی،
Promo Code یک‌دلاری
رو پیدا کنی و قبل از بقیه داخل سایت ثبتش کنی!
⏰
چالش اول → 18:30
⏰
چالش دوم → 20:00
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71554" target="_blank">📅 01:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71553">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad61e1e00.mp4?token=ppyOpKWsQS_llenVVtfvTTrpoUJc9y1qwr-Bhj94t_3-vrNhtZypMQurnLnm91FKLtgiVJvN6BkumEPTDdt2UZOYWlYYPRnSRa17h_GmhiaC5NG5CuzUzk_G_4LVzPn15lM7Ccv7-c4CMlCxDmr7h1peP6at3jmaBylIefzab1n_VCM4QucLLQncJ4u5VuTnRARuKoDvylAF118Dj37vZFySboZRwuLvNuQ_ey5eo0-gOfMC66_ha7nqb2n8ANb4D_ZLhI9FLz00ZgkNiHKaBiaZslDL9n7vdWiH0amq_yrkiKPfrzdkjbMMeRkn5aBaCBmc_mVmZbQYYn20q7xvSXQbyIXN1TgGbTCRJQtXz1nCZUlmmtQ6M4R8rIw-BOr8h1X9U3X79z_JerHwWMI0g7IF71UDXNZ5q05iD3LFiBgOH9p7kdqIhQnC-ZvMLW0iP363576oAxjROcuwIVZfmQ9VerZjMTqt7dRmJgu2NaUT2mVez-XVkhF19pzQOHRy4eiI-cL01X45bYoP_bcfu1OdE8Q4OuWW5CeZ5HvDvGXDZ6q8Grts1L6eKWpk5nfKfizjnilIPoD32z1ANJqSPlI49ir6N-CxZMnEc-Be4tmtIwb8Vrs9sPFJtghKCIoC817G6CCBVUUitvbxkgBUAcN1pxU1UNyBYynBP1oCIvc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad61e1e00.mp4?token=ppyOpKWsQS_llenVVtfvTTrpoUJc9y1qwr-Bhj94t_3-vrNhtZypMQurnLnm91FKLtgiVJvN6BkumEPTDdt2UZOYWlYYPRnSRa17h_GmhiaC5NG5CuzUzk_G_4LVzPn15lM7Ccv7-c4CMlCxDmr7h1peP6at3jmaBylIefzab1n_VCM4QucLLQncJ4u5VuTnRARuKoDvylAF118Dj37vZFySboZRwuLvNuQ_ey5eo0-gOfMC66_ha7nqb2n8ANb4D_ZLhI9FLz00ZgkNiHKaBiaZslDL9n7vdWiH0amq_yrkiKPfrzdkjbMMeRkn5aBaCBmc_mVmZbQYYn20q7xvSXQbyIXN1TgGbTCRJQtXz1nCZUlmmtQ6M4R8rIw-BOr8h1X9U3X79z_JerHwWMI0g7IF71UDXNZ5q05iD3LFiBgOH9p7kdqIhQnC-ZvMLW0iP363576oAxjROcuwIVZfmQ9VerZjMTqt7dRmJgu2NaUT2mVez-XVkhF19pzQOHRy4eiI-cL01X45bYoP_bcfu1OdE8Q4OuWW5CeZ5HvDvGXDZ6q8Grts1L6eKWpk5nfKfizjnilIPoD32z1ANJqSPlI49ir6N-CxZMnEc-Be4tmtIwb8Vrs9sPFJtghKCIoC817G6CCBVUUitvbxkgBUAcN1pxU1UNyBYynBP1oCIvc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🟥
گزارش فاکس‌نیوز:
جنگنده‌ها از ناو «یو‌اس‌اس جورج واشنگتن» (USS George Washington) در حال برخاستن هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71553" target="_blank">📅 01:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71552">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uk413CSOc2vo0lh_YQIDEJXh6M8OGLZQ2xreHjDmFkpz1kCQnx3r1KqXs3TRbYowfATWfoi8rXNr9E7lrSQbMi9i4T3JISdd_mkbJ5dajdGgPaKbukFWMAgtOJ9VOstZo5rTz-M7xFd4gOriN453NCf50HydtPoao255Wdyb-Agk1B8QpZec2RtA8e4IvhfhCBMvGbeAdnYrG-zTf8qyVEDpP2Eh0Hh7oq5ekPuAdNKaSdhscoEIulGIv60QHuo55pehFDliUlEwPqMgA21x8clWrZJ8bSAA1IflfxRx5MckTtWw5Rx4HnYBWEVKivh39XOx9zah2VnGKrzH9M_4Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
#فوری
؛کانال۱۴ اسرائیل:ایران برای خروج از پیمان منع گسترش سلاح‌های هسته‌ای (NPT) و آزمایش بمب هسته‌ای آماده می‌شود.
حاجی‌دلیگانی، نماینده مجلس، از آماده بودن طرحی با قید سه فوریت خبر داد و افزود: «باید هرچه سریع‌تر آزمایش‌های لازم برای سلاح هسته‌ای را انجام دهیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/71552" target="_blank">📅 00:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71549">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGh1mDIqabvUSlYolq0r2nFCiQeR2OTtpMwWvuA4jcbCNKnlJiSfh5h2GE1AAdtudTuHvUMXpwE-_m563-B2_dMgv26DqYnbn28DI6LwI2UppjFZYVyfKjJKDEgsivqXLRYkNBYHkaFPhY-FJuylmUQR7AyPtKWwvmcRxR8lsiRp3fBk0MIwJByupNUQSAE62JHnpzFyMvJsGCEn-SEM_DlmxGPOmEGqa1QO8oHQ1Nq3uG-mxbka_9f1DmjJfoZIBfLJPOFSreJCclppl4_9WHe1I6bPkdmlYbztUZSqjJwNTHChIOVNlz4PxVsCivtFc3RAtFmbNHhbDQVvQlnzMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ddef7d0b.mp4?token=XpAOcZLdjNdw_bCDxoL9EHzDZeOJ2KYrdu16KCVbVA_RGcZiH34XCa3b-fMeMUZX8ZOLmwHWAAs8wvXJtHsg037IVKWn2PIcLVRwoIMI17vI2X0TQiba8FfAAbeQzUqswIr29P0-0geo8JbKzYzT1DVgI9kY70J3CABS7rRrZqUjFkMVAJn5iPru2Xp-M6RB4esiBqgP20PAOBCCJGP-MsYvchTFHDXv-pOpxgTCjq1fxRM32BBqPIhRohDdqHhB-92V3-ExZMPsrJip4Fc-66SOgPpBzazZVgVGngjvToFNm83CdfOgvAA2p8Eisz-XOjOnj_9QP7o5K5V51TVDUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ddef7d0b.mp4?token=XpAOcZLdjNdw_bCDxoL9EHzDZeOJ2KYrdu16KCVbVA_RGcZiH34XCa3b-fMeMUZX8ZOLmwHWAAs8wvXJtHsg037IVKWn2PIcLVRwoIMI17vI2X0TQiba8FfAAbeQzUqswIr29P0-0geo8JbKzYzT1DVgI9kY70J3CABS7rRrZqUjFkMVAJn5iPru2Xp-M6RB4esiBqgP20PAOBCCJGP-MsYvchTFHDXv-pOpxgTCjq1fxRM32BBqPIhRohDdqHhB-92V3-ExZMPsrJip4Fc-66SOgPpBzazZVgVGngjvToFNm83CdfOgvAA2p8Eisz-XOjOnj_9QP7o5K5V51TVDUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
درحالی‌که شرکت اپل ایران رو تحریم کرده، قمی‌ها طی یه حرکت عجیب، همزمان با مراسم معرفی محصولات جدید اپل، خودشون هم به‌صورت جداگانه یه ایونت برگزار کردن و از آیفون‌های جدید این شرکت رونمایی کردن
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/71549" target="_blank">📅 23:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71548">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac8d39358d.mp4?token=CaRFIlC9cLmYk8VZWoPAsgUjJ34rB1brPfQ1hKsAtvs9KQk-j0z8FvbryVFW9TgDZf0FZy6xjQ-vqNIy7ToSy2UMnpsLJXE7FKcMnaWa_YqCeZl0SjjVzGUvI_hz1ZWn8f6a-LIIZ7PFVU8L29aKtYDHQ_V2Q8Q1euU9L7e0vhT0cMKpNDvdiYO03uvGQwU0B8svk6UyT--89Em5PlY2qigO0sBdWzueITxYR9L4g95OJPSRNObI70Zbe95_JbUxdT7y7Pq0oDboDBs7L_8LOXmVyDQRtDuSWS3kVID1iTDoS17NdKFSjw0XySbPklYGxkt5E5wXQcrVO5KkTJ6o6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac8d39358d.mp4?token=CaRFIlC9cLmYk8VZWoPAsgUjJ34rB1brPfQ1hKsAtvs9KQk-j0z8FvbryVFW9TgDZf0FZy6xjQ-vqNIy7ToSy2UMnpsLJXE7FKcMnaWa_YqCeZl0SjjVzGUvI_hz1ZWn8f6a-LIIZ7PFVU8L29aKtYDHQ_V2Q8Q1euU9L7e0vhT0cMKpNDvdiYO03uvGQwU0B8svk6UyT--89Em5PlY2qigO0sBdWzueITxYR9L4g95OJPSRNObI70Zbe95_JbUxdT7y7Pq0oDboDBs7L_8LOXmVyDQRtDuSWS3kVID1iTDoS17NdKFSjw0XySbPklYGxkt5E5wXQcrVO5KkTJ6o6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
لحظه‌ای که جورج دبلیو بوش خبر حمله به برج‌های دوقلو را دریافت می‌کند
جورج دبلیو بوش آن صبح در مدرسه ابتدایی Emma E. Booker در ساراسوتای فلوریدا بود و برای دانش‌آموزان کلاس دوم در یک برنامه کتاب‌خوانی حضور داشت.
نکته جالب این است که بلافاصله از جا بلند نشد و کلاس را ترک نکرد. چند لحظه در همان صندلی ماند و سعی کرد آرامش خود را حفظ کند تا دانش‌آموزان وحشت نکنند.
چهره‌اش به‌وضوح تغییر کرد و حالت شوک و نگرانی در آن دیده می‌شود. دانش‌آموزانی که آنجا بودند بعدها گفتند تغییر حالت چهره او را به‌خوبی به یاد دارند.
جالب‌تر اینکه او حدود هفت دقیقه دیگر در کلاس ماند و بعد از پایان بخش کوتاه کتاب‌خوانی، از کلاس خارج شد و در همان مدرسه برای خبرنگاران صحبت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/71548" target="_blank">📅 23:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71547">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e621bd826.mp4?token=gnZjI7cPaxqnv4Dm2rBRWxF4psgUPkBSFnUDiRl_JFzr8PSiBuVqXthAZD1rEmw3lH_drcieUEuyFvLmjdyQ5UArr_zc3uLdULgw6xoEC8ypWD4y6K7O0TE0x3Nj_Cy0klcux1BaVfI8CHVCCKNCF2iP060YvyaASiTua1L1Lj7UNSEk70gX6nVTD2KWC7N-rJUPkx84I_PBNH3flKpX7tComzlcAMPtkoSWvddp6sFocZX2dK6NQemWJClXer7WSM-B1EQv5kAuFQXUrbmIdVQ2yBzUnOJULox6S40_ubCGxQ1ceKXvogtFUMZ0Tg3MPxUzmytpDPE1NpVTxHgCEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e621bd826.mp4?token=gnZjI7cPaxqnv4Dm2rBRWxF4psgUPkBSFnUDiRl_JFzr8PSiBuVqXthAZD1rEmw3lH_drcieUEuyFvLmjdyQ5UArr_zc3uLdULgw6xoEC8ypWD4y6K7O0TE0x3Nj_Cy0klcux1BaVfI8CHVCCKNCF2iP060YvyaASiTua1L1Lj7UNSEk70gX6nVTD2KWC7N-rJUPkx84I_PBNH3flKpX7tComzlcAMPtkoSWvddp6sFocZX2dK6NQemWJClXer7WSM-B1EQv5kAuFQXUrbmIdVQ2yBzUnOJULox6S40_ubCGxQ1ceKXvogtFUMZ0Tg3MPxUzmytpDPE1NpVTxHgCEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو مشهد اردهالِ کاشان، از " نمادِ مشت گره کرده‌ی علی خامنه‌ای " رونمایی کردن ولی انقد بد ساخته بودنش که صدای طرفدارهای حکومت رو هم دراوردن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/71547" target="_blank">📅 22:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71544">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QqM6tW4M8tuBc2wYYM7Knu1z4Lco43dhXw-J1mkZjfV5p5HmjJ867sVYPA_2se5qt5tbKIWec18FLrNWCze1WWZ4BbjVnKpxYCdTQU8CpxLpNersaRRjh3FKfjdiXcgdeDC-78CpBxdjklpt9OcENXu1i_hiXw6OLZxHduRwNiNJX6s05QPQKNbUH9eTBMHFufAeBdKeiE1eMSCu-blmIqA0u2uA4Xm-_VajBZvSgPKN-XJBxHLZQpadoEjYCjHc-vLEjQx4LPJ-Bzzkm1GMIRe4tcvkc54wP1MQbvyFXZ9tFPHe5uP8A35FZIHLz8aqkmfnmRYWXh3H1pLhF2nP8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q-aQdG31pG182K42-R6VX2WdjCLhF1_owOIxZ3WYXkolMLbTKNwziNelRiSD3oAnlrCypciwzgg2DXVw21-EBMIUeUKvkjW7th4JRDZKyuSUUkFYLDQ4tjJGJf2ESpaauy4tUKMv_8HRoxZJznRm-uWMyF2gynIeQILFYyy7SJlTB7Fkfdb5XmwK_AQAwGluZXgxyVSm31d-6jBQyOzbR_QTzgCGVieZtV7DsrSbBgCTTPecOG3ctw5tiaqyqgztsZ5fh9LOjWzFs5ms9uU8NuY3lRX0ibvV7dWo7Dt3eH2KYrkj08A48lirDbQcuWp-oULJGCQaITI2AGJnoIfV-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jdUQyYXfBarGNZlH1p01N6CT3_LCcN4_AoHMgNoa7v596YeZ9KBmaBww1aeQkyaVYgLmac1HzKS4Wfoy9hIIlRZ0wmNB9TF3SXgLp5MzCeXsOOn6A7KcWDlAOR4L78cb2AbTIvMoC6mRcdAABz3TSTN4AAWzlGvG64z3GiiAKkTQK6LuPMopc_rBpsj1E-BeOIIIqrfrLXukf3pDIRLnjSJSrPO-3DNtcgg8Bi8kdtdkMALcJcvtpKgf6Wm_iZ4JZp-i1ykJj6tiaramEKE9igWSnoTvfiQacaaS79lVrSVnPQeQNprD-US1aCQ479u7q1Xc7YvY-HDk0pxuKYs0LQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚠️
کشتی‌ها و نفتکش‌های آسیب‌دیده ایرانی در خلیج فارس.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/71544" target="_blank">📅 21:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71543">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
شلیک یک موشک/پهباد به سمت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71543" target="_blank">📅 21:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71542">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQiVciFAWI1j4OWT-lQ3fRcaXz661EV4b2QWwQVawmoOzudH8AKocqFlaorK9ZI3e-bp0SE_PSn2LobZ7mTPl8PWnFHKtbwsovU8M0bqLcUzrUqMEKy6VPQP9sTBiYB2PyFnqjmGrWOy49xFV1A5orAishS7AENqGIl_qqPnlPAThQ-ab1lwhCdSH5FUR313nCvnfh4HIxjtkXSRFFj63ZtzPuBUdu-pBGdq6OBPLuarq6m-Pa-RfVGVQet6Z2MACjTfsw8x2rNnnK4-V9gMuBAjFMyDGMlp_vJQUUB0e6uN5E3XmdY84lp1Y4Qg7lxcXUXtdM4JJuXfvs6MUWVGdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
شعار جدید عرزشی‌ها برای حسن روحانی
😂
نهپاد: نفوذی هدایت پذیر از راه دور
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/71542" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71540">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a60a908ab2.mp4?token=tACvksFVoWkUOxmlpbY41RvSivdN1eEdr9On7qrPFSeH53fdfJg95F3MdEA3k1qyVtAe7swfuLemcVsWdxYECvzialFHnM5KGYEY2JV1EwCXNNDcMcxKqaZxuMYnzAyb90-VH8zsoU4rpLY7V5nymQ18CegAgSUNkYrQuG77Q4gbsg3gFYEuAp8gX-REUgW5wBiQZfDCg-tdEHnlSThd68R4a0o3kh5Nu-o8C4Xgbl3XdXUJV4hYuYLWEXhVoOAdRe0JLLoyM7-J8h7KvYUwblauEuNEmtxcCL7HL7rF3KtldbafOUGoLT_rAJcI4DpYvoyo-D0QImeRCRfH3lIBWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a60a908ab2.mp4?token=tACvksFVoWkUOxmlpbY41RvSivdN1eEdr9On7qrPFSeH53fdfJg95F3MdEA3k1qyVtAe7swfuLemcVsWdxYECvzialFHnM5KGYEY2JV1EwCXNNDcMcxKqaZxuMYnzAyb90-VH8zsoU4rpLY7V5nymQ18CegAgSUNkYrQuG77Q4gbsg3gFYEuAp8gX-REUgW5wBiQZfDCg-tdEHnlSThd68R4a0o3kh5Nu-o8C4Xgbl3XdXUJV4hYuYLWEXhVoOAdRe0JLLoyM7-J8h7KvYUwblauEuNEmtxcCL7HL7rF3KtldbafOUGoLT_rAJcI4DpYvoyo-D0QImeRCRfH3lIBWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
❌
🇾🇪
حملات هوایی جنگنده‌های عربستان سعودی به استان البیضاء یمن
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/71540" target="_blank">📅 20:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71539">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvNzPdlG8pEO495pcukn1UEk2lYcB_MJPLk8_JXHwkQsjFcQRaggV38qTbIu7GWYQmcAIJmxxt0NZm65VjuOXd_M3RpFek6_up3YQxJt77qiYLMdrCCYisgC-tedC6paH0t_i0iQrCrqhVCcuTc4Mu3Y2d9zXd4p3mW9nm7WbBnjKJvFU4T8_ee_zZeOohnwcJbT9yvOL6maWoH6Nevp2bQaUNR4epmKeOsU174m_vR7lWP9M1a3nxG33mZHu-G4xVFJnuvXd1f55m3ZpaDdJZxIAVz6h27wKA0paOwbY-HjB_ChOvk8DroQUzyhDq_3ODS4-ePPGbVebJdsUAbUYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
علی قلهکی:
مذاکره متوقف شده است چیزی وجود ندارد که میانجیگر داشته باشد.
عاصم منیر هم جمع بندی ندارد که اگر وارد جنگ یمن شد، بتواند پیروز شود و پرتابه‌ای سمت تاسیسات حیاتی پاکستان نرود
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71539" target="_blank">📅 19:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71538">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5OlGuWrNrLSNuyCU0ZxGj_1ewTzdhYu-bxnUIctOi8VWHe736jf9gbZhj2XtrbE2EBpseTM1dslEAXeSynILoon3fSuNmtLYQWMpHE-GDHWwvLHvf61MK6XG7mIWXS-mq7xuoFmYGnWwAnWJlSe2C5ZgiIlrBOYpnv2Yt2TXcRM2g-xKo92I3ivCqS1ctxgSS9JW9zbTNirEUDaNUQgmUtRMAJ_mqIRpcdCcF8Uve8m0fSIYBrFjkG82ShVX3fGA78qdPqWCRC8SKPPc_04rhYDBjSw0Ln-TqGQlMaz7SZvBboHJ3qmtxG1wQkduJn2F-qK7qUHh_K_ue5KHb-yAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
فرماندهی مرکزی ایالات متحده:
از زمان ازسرگیری محاصره موسوم به «دیوار فولادی» علیه ایران توسط آمریکا در ۶۰ روز گذشته، نیروهای سنتکام مسیر ۱۰۰ کشتی تجاری را تغییر داده‌اند.
حتی یک کشتی هم بدون مجوز نیروهای آمریکایی از این محاصره عبور نکرده است و نظامیان آمریکایی همچنان با تمرکز کامل بر این مأموریت متمرکز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71538" target="_blank">📅 19:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71537">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇧🇭
❌
🇮🇷
بحرین اعلام کرد تا زمانی که روابط دیپلماتیک با ایران از سر گرفته نشود، در هیچ‌گونه نشستی با این کشور شرکت نخواهد کرد و بدین ترتیب پیشنهاد عمان برای برگزاری نشست وزرای کشورهای حوزه خلیج فارس و ایران پیرامون مسئله هرمز را رد کرد.
🗣️
بحرین چهار شرط تعیین کرد:
توقف حملات
پرداخت غرامت
احترام به حاکمیت
حل‌وفصل اختلافات از مجاری قانونی.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71537" target="_blank">📅 19:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71533">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b779ef03e.mp4?token=AT5qb12Mvf02raUCpd5bMPxD-6QeJHPtR3KqGPuaTfxUafx6kydSSy4WtDzvvC-A01FbODbtpLyuTBQtl018XNk39IRJl40F_14waBktKErSY07Q36JyecV6rTzQ5FTt8sVwa7-K5uAE7FayTpO8C9v367lfVUJh81w-Xe0nzJmQdSDyvNZBPbe1bb-F2Bkv8OhkyuzsU7gqKnAPsSJzdAyVYNMNnlgQbMuyAdnyBGEnWYNDdCOnVNmBsTxK7Gzvz0kqlNLTuSdUHIFHEjp5ivVV7CWGld6K1QONAY7e7VPVahWW-5KRcMTLxzX-oLEEVlb9QK8BYG2gwryxqLS9Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b779ef03e.mp4?token=AT5qb12Mvf02raUCpd5bMPxD-6QeJHPtR3KqGPuaTfxUafx6kydSSy4WtDzvvC-A01FbODbtpLyuTBQtl018XNk39IRJl40F_14waBktKErSY07Q36JyecV6rTzQ5FTt8sVwa7-K5uAE7FayTpO8C9v367lfVUJh81w-Xe0nzJmQdSDyvNZBPbe1bb-F2Bkv8OhkyuzsU7gqKnAPsSJzdAyVYNMNnlgQbMuyAdnyBGEnWYNDdCOnVNmBsTxK7Gzvz0kqlNLTuSdUHIFHEjp5ivVV7CWGld6K1QONAY7e7VPVahWW-5KRcMTLxzX-oLEEVlb9QK8BYG2gwryxqLS9Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین  به اهدافی در چهار منطقه روسیه حمله کرد که حملات ساراتوف تایید شده‌ترین و چشمگیرترین آنها بود.
مرکز لجستیک عظیم اوزون در ساراتوف (با بیش از ۱۰۰۰۰۰ متر مربع مساحت، بیش از ۳۰ میلیون قلم کالا ذخیره شده، تا ۹۰۰ هزار سفارش در روز).
طبق گزارش‌ها، پالایشگاه نفت ساراتوف (روس‌نفت، که قبلاً بارها هدف قرار گرفته بود) نیز آتش گرفت.
در ولگوگراد، فرماندار تایید کرد که آوار به یک مرکز صنعتی و یک ساختمان آپارتمانی برخورد کرده است.
منابع اوکراینی می‌گویند که هدف صنعتی، پالایشگاه ولگوگراد لوک‌اویل بوده است.
برخی ادعا می‌کنند که از موشک‌های کروز در کنار پهپادها استفاده شده است.
انفجارهایی در انگلس (محل پایگاه بمب‌افکن‌های استراتژیک روسیه) گزارش شده است، اما هنوز هیچ اصابت تایید شده‌ای به فرودگاه وجود ندارد.
بنا به گزارش‌ها، منطقه بندری کاسپیسک/داغستان نیز هدف قرار گرفته است - پس از حمله تایید شده شب گذشته به بندر ماخاچکالا.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71533" target="_blank">📅 18:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71532">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71532" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71532" target="_blank">📅 18:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71531">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZus5qbaREFKNp7MQWLboNY2fyMdjB-PjgZmCPVQvkyn2o1CYE_X__2gDPBaKEBd_g_W0VwQeE6-Hn59gb3EmoXVW8Yu8WCB7Btuc9dKErv-rnzBcTMXOc94YEEsudum4D6hNpIt23UrYZyY6Y_76TC1sl5LxkMXRBYIzsmgt-Tzd-xUPGyite5HZuXMa694hGU3upnHIT4S8fPLlInQ0wtpxi4z5Fsk0La-qeaIMLQSsMfmh4OYUnkwCPo91gFqu7bwPYd5dMHUf--CUxJbgTebnlMIgSRgmVAioXbvCExlwvT6iOyU-5PA_PkwH23R5Q3XAaISExOpAfNU8_k6Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
میلان
🆚
لاتزیو
⚽️
را در
TrexBet
پیش‌بینی کنید.
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
میلان: ۳ برد، ۱ تساوی و ۱ شکست و ۹ گل زده
⚽️
لاتزیو: ۴ برد، ۱ شکست و ۶ گل زده
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71531" target="_blank">📅 18:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71530">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/554b629d89.mp4?token=b6_QjqkjjwalXBRCEKzoQk3VAkkwlpnkQBxNBY-YD-bJCuC7u3Bj0c4qpDl_vk5SBdEdm11X9O2efZvbnDY2OYKBa3bvng8xt-_Xdw_COqH-uLLLMWJ-0wkOCfpRPy2Ycnx1okxT6884JHc9vUcyvv51RJqW4jnHq6FitGOjw4nMZVDXaqN1bJmeYUnQXm9l15Nn-m7JDxaU3Byh7FCG_nL-edWYZnUvEWXz22ecrimYm_bgmzrwv2zzchrq_OgJbtNRZQ5e2-S_9LO8t2XsUSsRgiWPjQhaAOQL8XYwi2BW0VI9G3qywQGYLBbdN5oQx2o5lji9iwESxAU9c5QwWpUyXcJpjsolo5n3MbJ7gQaeMXamhWlskILInvPIsHKMkC8ik8h1bV2H5AsGiYY_8qP44NaqyZOvkD5QPVzdmx5dlWLvyrOGtvU8Z_CF-68tXHDf7dUzDAMmskpnMYdj7Y9ypXzJs6bKftMal2PJROSFOJZoTTM425NcC5DRTSjHppmuXt57itAWWPMUAz3BX8VXrm9GiY6bKW8wm2Eo69IyLKCcyrD2vUazJTytRuJGUfNcqnxXhHTpxXtN3leD64C0LPYVAOuNzVn1S5b0nzCeEqdSFubft4sl4y_zShCW2Zr6zLPw0o1BzEQ3yF_iFD187i_XjgncbRySGqP5BlI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/554b629d89.mp4?token=b6_QjqkjjwalXBRCEKzoQk3VAkkwlpnkQBxNBY-YD-bJCuC7u3Bj0c4qpDl_vk5SBdEdm11X9O2efZvbnDY2OYKBa3bvng8xt-_Xdw_COqH-uLLLMWJ-0wkOCfpRPy2Ycnx1okxT6884JHc9vUcyvv51RJqW4jnHq6FitGOjw4nMZVDXaqN1bJmeYUnQXm9l15Nn-m7JDxaU3Byh7FCG_nL-edWYZnUvEWXz22ecrimYm_bgmzrwv2zzchrq_OgJbtNRZQ5e2-S_9LO8t2XsUSsRgiWPjQhaAOQL8XYwi2BW0VI9G3qywQGYLBbdN5oQx2o5lji9iwESxAU9c5QwWpUyXcJpjsolo5n3MbJ7gQaeMXamhWlskILInvPIsHKMkC8ik8h1bV2H5AsGiYY_8qP44NaqyZOvkD5QPVzdmx5dlWLvyrOGtvU8Z_CF-68tXHDf7dUzDAMmskpnMYdj7Y9ypXzJs6bKftMal2PJROSFOJZoTTM425NcC5DRTSjHppmuXt57itAWWPMUAz3BX8VXrm9GiY6bKW8wm2Eo69IyLKCcyrD2vUazJTytRuJGUfNcqnxXhHTpxXtN3leD64C0LPYVAOuNzVn1S5b0nzCeEqdSFubft4sl4y_zShCW2Zr6zLPw0o1BzEQ3yF_iFD187i_XjgncbRySGqP5BlI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
پست جدید هیچکس (سروش لشگری ) توی اینستاگرام که وایرال شده؛
«هنو به یادتم»
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71530" target="_blank">📅 18:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71528">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4b43f033.mp4?token=PB2iq3doryRTTaiBiQwNcGF_MHYQWki_o8xXGAaRhVtZcYGAo78YgtphJEXZN__d_s2R_W1wDyFGiCfu4AQ3OxuoCAtHPfzIAeKiA3haa2BuXtTLaAX7KabVCckKXC4DG08WPlmqT1CjJWXJg16ADJYWI5Eu88lb5vfpTHvYgJu65Bb-VS_fQ7YyTi4lHTFNDxjAZGiZJV9KvfMnj-oqgQpb_-s7z3U1Xt9u_45hU9TlPtXPQ4yv_iauVSa-4diWwjb1M_rtJLqy4K8oIxDIuMyYZ-QBw05oKv4t0vzreDrwKY-0ASQ5nz79ICbSb-msuvh1n5-Yw_SmG8OuQQseBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4b43f033.mp4?token=PB2iq3doryRTTaiBiQwNcGF_MHYQWki_o8xXGAaRhVtZcYGAo78YgtphJEXZN__d_s2R_W1wDyFGiCfu4AQ3OxuoCAtHPfzIAeKiA3haa2BuXtTLaAX7KabVCckKXC4DG08WPlmqT1CjJWXJg16ADJYWI5Eu88lb5vfpTHvYgJu65Bb-VS_fQ7YyTi4lHTFNDxjAZGiZJV9KvfMnj-oqgQpb_-s7z3U1Xt9u_45hU9TlPtXPQ4yv_iauVSa-4diWwjb1M_rtJLqy4K8oIxDIuMyYZ-QBw05oKv4t0vzreDrwKY-0ASQ5nz79ICbSb-msuvh1n5-Yw_SmG8OuQQseBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
شعار «مرگ بر روحانی» در تجمع شبانه عرزشی‌ها
:
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71528" target="_blank">📅 17:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71527">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e506b56e1e.mp4?token=ko1ON5rhYHYzDyAkwYFOXDWC8U1WZ4qwzn9juYQMn7OBxOVvxKmz0ClwaZnnhm-JTe0NWrUTKj0aJj5MU5Fs3zRAoXLaFXWSUsNlR-YwbSwkzY6qqZCaeSjjNafxgyfhwA4oCI0rzKfTOI7On8KksYYzLvkUtejlGI6Vw7oB7oU0Q_Uv_AC9VULPazD0E0qDXKedkrAWt6sjVXfsaBCZ3j_yNhh5f1VpzBgUBUVftPuj1Iaq2V8vBH8Q9JdV2g8-C-DrwLLn94lv7U3j0Jp0ARglpivM7spAagAP6dJqa8P8YNspznmudU3XxZ9rb-bQ7v4gDRpOC44xJtvLUrvNVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e506b56e1e.mp4?token=ko1ON5rhYHYzDyAkwYFOXDWC8U1WZ4qwzn9juYQMn7OBxOVvxKmz0ClwaZnnhm-JTe0NWrUTKj0aJj5MU5Fs3zRAoXLaFXWSUsNlR-YwbSwkzY6qqZCaeSjjNafxgyfhwA4oCI0rzKfTOI7On8KksYYzLvkUtejlGI6Vw7oB7oU0Q_Uv_AC9VULPazD0E0qDXKedkrAWt6sjVXfsaBCZ3j_yNhh5f1VpzBgUBUVftPuj1Iaq2V8vBH8Q9JdV2g8-C-DrwLLn94lv7U3j0Jp0ARglpivM7spAagAP6dJqa8P8YNspznmudU3XxZ9rb-bQ7v4gDRpOC44xJtvLUrvNVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
یک شهروند ایرانی با انتشار ویدیویی اعلام کرد ترکیه مرزش رو به روی ایرانیا بسته و اجازه عبور و مرور رو نمیده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71527" target="_blank">📅 17:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71526">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89e47bf456.mp4?token=l_QDfSXT5RuXP_ixy20lXoA9kcuAhqthLTb2it0ozuw4tf1TW2JsG-z365zX9u5C13vYZmM31JSr8JCC_PYTEIXTOfiwl_JacbPaUazong8ava8OjLW6avzdvU6m-Qf_hBp841iBo_sMeNnTs46HofDi-1Y-Bcqk__sLMdUCnp4cg5Ere3j45JaNAYhK6jh1bA5pUctHe7QfTCTPn3NOJYgtBS4LbCn0IWaWUD3Seenwb5H-EVVjLHsmaeTcC6lQ7H32hmwFHl1tkGMRDINuZNImnHrzFHFEW9JVe6LRSu0GMlJ8FHgvhZIpEcISLrXaCAhF0OgYqa_ibgw9ei-F5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89e47bf456.mp4?token=l_QDfSXT5RuXP_ixy20lXoA9kcuAhqthLTb2it0ozuw4tf1TW2JsG-z365zX9u5C13vYZmM31JSr8JCC_PYTEIXTOfiwl_JacbPaUazong8ava8OjLW6avzdvU6m-Qf_hBp841iBo_sMeNnTs46HofDi-1Y-Bcqk__sLMdUCnp4cg5Ere3j45JaNAYhK6jh1bA5pUctHe7QfTCTPn3NOJYgtBS4LbCn0IWaWUD3Seenwb5H-EVVjLHsmaeTcC6lQ7H32hmwFHl1tkGMRDINuZNImnHrzFHFEW9JVe6LRSu0GMlJ8FHgvhZIpEcISLrXaCAhF0OgYqa_ibgw9ei-F5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو از عشق و ابراز علاقه زیبای یه پیرمرد و پیرزن ایرانی توی پارک خیلی وایرال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71526" target="_blank">📅 16:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71525">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/401752fb0e.mp4?token=f-Rgwl4hl6y7mJX3J4dZpLMor_2TQOG7wb2yrLhixyBO87ZDAFTnNOigK51sdHacp4HtKSC6YPUJuppJco_Z_qsSQVFEIp9C_3mPUY7NeiZvW3HQ9fuCIbq4tIVhwblDimu2zcZLYUiJBgGDTfeDGU78xSLF4WUXiH1novHC8QoKDyftlwMFMm2_DqyPILqu9yLrbQJ6oJdx2qnB2BCgk13Bor94I-q0Eu-ANNdbH-zqzDLFIQ3yoPDBl6owR3FpyvuHT4cEPmpaIx8aXLVJJxq1UATJZgpiEJ62pvjtwOS-5i_76ym_Hl8JZ-Bqu_u0hI39a-LpqQ0uv6AYs6zEKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/401752fb0e.mp4?token=f-Rgwl4hl6y7mJX3J4dZpLMor_2TQOG7wb2yrLhixyBO87ZDAFTnNOigK51sdHacp4HtKSC6YPUJuppJco_Z_qsSQVFEIp9C_3mPUY7NeiZvW3HQ9fuCIbq4tIVhwblDimu2zcZLYUiJBgGDTfeDGU78xSLF4WUXiH1novHC8QoKDyftlwMFMm2_DqyPILqu9yLrbQJ6oJdx2qnB2BCgk13Bor94I-q0Eu-ANNdbH-zqzDLFIQ3yoPDBl6owR3FpyvuHT4cEPmpaIx8aXLVJJxq1UATJZgpiEJ62pvjtwOS-5i_76ym_Hl8JZ-Bqu_u0hI39a-LpqQ0uv6AYs6zEKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه دختر حامی حکومت:
چرا پزشکیان ۱۷ شهریور که تولد مجتبی خامنه‌ای هست بنزین رو گرون کرد؟ چرا روز تولد خودش گرون نکرد؟
میخواین همه تقصیرات رو بندازین گردن امامِ ما یعنی مجتبی؟ کور خوندین!
ما دیگه فریب بازی‌هاتون رو نمی‌خوریم که میخواین علیه رهبرمون کودتا کنین.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71525" target="_blank">📅 16:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71523">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e93a51beb4.mp4?token=Sx7PcaJ33Nd365hrTDB7TJcUtI8BBCbKAXYw19j4Rh9U_utGYSS4aeK5vmZYzGlpDHFLJwQ2-CWsXaaspAoozKtmOGpueru9E5GIitPnHmAKyeAQU5-nwARI-oxeoQOukIzKkrg7cPwgo5lw98a65xCd_o-vW6TeXgS_mxmN8q4o8IOa6XNTf2cpuxgITSY2IfXMfq_tIqhnGJmXosUFLRpcmbEqGkV1HQpr6zbjBj6m7H0BKIfLcRB9MlcloL-8BUDFtvH80HrKHcmKAga9CysVEw9sh8X46pU5fI3mhmBxfM8etTa1W8Zl1nBc_9uekLVMUwxuH-8NJNYuMckiH5sFTqiTNunBzEaBaWpKzbo6ZDjCn5iV9qxEMHRVHXxw4Hs7XJI7HZqtPQTCJrk2f6B757yixIvt9n2xIAHxs13hrgTMpgjrzUPGMfnNKhjX-pUL39ET8Uk5ahdE8M8MxsfEbkr3b0xk5OQgrjdWdchbuaUUJ5Jqi06A4K8xFbXmSaH0pI870bgsW8lv7yJrIvbsO-_c7L0Grn0JNTcVJ9YtGaYisEdsXmBkJVgb38bwmCYHsJVrdvBy_evPHKE_nZrFuN_G2aL5iahw5W_qmYuo6tK5_61YNU45GBSxePkIdO-nEpZGsQpA0syorxlY0RUVLmuiPQCyuehpGkWzWPM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e93a51beb4.mp4?token=Sx7PcaJ33Nd365hrTDB7TJcUtI8BBCbKAXYw19j4Rh9U_utGYSS4aeK5vmZYzGlpDHFLJwQ2-CWsXaaspAoozKtmOGpueru9E5GIitPnHmAKyeAQU5-nwARI-oxeoQOukIzKkrg7cPwgo5lw98a65xCd_o-vW6TeXgS_mxmN8q4o8IOa6XNTf2cpuxgITSY2IfXMfq_tIqhnGJmXosUFLRpcmbEqGkV1HQpr6zbjBj6m7H0BKIfLcRB9MlcloL-8BUDFtvH80HrKHcmKAga9CysVEw9sh8X46pU5fI3mhmBxfM8etTa1W8Zl1nBc_9uekLVMUwxuH-8NJNYuMckiH5sFTqiTNunBzEaBaWpKzbo6ZDjCn5iV9qxEMHRVHXxw4Hs7XJI7HZqtPQTCJrk2f6B757yixIvt9n2xIAHxs13hrgTMpgjrzUPGMfnNKhjX-pUL39ET8Uk5ahdE8M8MxsfEbkr3b0xk5OQgrjdWdchbuaUUJ5Jqi06A4K8xFbXmSaH0pI870bgsW8lv7yJrIvbsO-_c7L0Grn0JNTcVJ9YtGaYisEdsXmBkJVgb38bwmCYHsJVrdvBy_evPHKE_nZrFuN_G2aL5iahw5W_qmYuo6tK5_61YNU45GBSxePkIdO-nEpZGsQpA0syorxlY0RUVLmuiPQCyuehpGkWzWPM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ درباره ایران:
«ما کنترل تنگه هرمز را به دست گرفتیم. تمام مین‌ها را پاکسازی کردیم.
من گفتم: «خب، پس چرا آنها مین‌روب‌های ما را هدف قرار نمی‌دهند؟»
گفتند: «قربان، این مین‌روب‌ها زیر آب هستند. آنها همیشه در زیر آب فعالیت می‌کنند.»
گفتم: «چرا این کار را می‌کنید؟»
گفتند: «خب، به‌طور کلی، وقتی مین وجود دارد، بیرون از آن منطقه هم خصومت و درگیری زیادی وجود دارد.»
یعنی اگر در یک آبراه مین وجود داشته باشد، معمولاً افرادی هم هستند که به سمت شما تیراندازی می‌کنند. بنابراین اگر زیر آب باشید، آنها نمی‌دانند شما آنجا هستید.
حالا دیگر هیچ مینی آنجا نیست، هیچ چیز دیگری هم نیست. و اگر ببینیم آنها [دوباره مین‌گذاری می‌کنند/اقدام به این کار می‌کنند]، آن‌وقت می‌بینید چه اتفاقی می‌افتد.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71523" target="_blank">📅 15:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71522">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffb4e73a23.mp4?token=BnJ0_dOK_F5F9a9RXaqiFDglAg_IAj60dpoHP9UMt6mZ9SaJGCCDY5oSqtbS6EEIG2nracyr72JbZfAdFQzLRiaMPQO9xGAArNZ78AFkSZCmyEgWvkxIvkshE4kp1VfBBrFiCWlOrZZ3edUjRGotKsgaPR4EZhb0aj4nAmXun2bYa8ImHlDfKBWxglrKmPSg9nFJxRlboujLVRu77epFlW77b40l_KoTyhAtEwOaI74LYF8F6RL6TN8J5F6ZAZMf3pKwXw83Gu3-4gj-qd45cPgX-ABtI0EXhywWkFdU2SocS0asp1ohZ6vQjlhqYQUX1ARGcp8RwDEamzt_ICcnuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffb4e73a23.mp4?token=BnJ0_dOK_F5F9a9RXaqiFDglAg_IAj60dpoHP9UMt6mZ9SaJGCCDY5oSqtbS6EEIG2nracyr72JbZfAdFQzLRiaMPQO9xGAArNZ78AFkSZCmyEgWvkxIvkshE4kp1VfBBrFiCWlOrZZ3edUjRGotKsgaPR4EZhb0aj4nAmXun2bYa8ImHlDfKBWxglrKmPSg9nFJxRlboujLVRu77epFlW77b40l_KoTyhAtEwOaI74LYF8F6RL6TN8J5F6ZAZMf3pKwXw83Gu3-4gj-qd45cPgX-ABtI0EXhywWkFdU2SocS0asp1ohZ6vQjlhqYQUX1ARGcp8RwDEamzt_ICcnuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
هادی چوپان :
هانی رامبد از پشت بهم خنجر زد.
گفت پشت جمهوری اسلامی نباید باشی ولی من قبول نکردم و اونم همکاریشو کامل باهام قطع کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71522" target="_blank">📅 15:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71521">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpGPPo78xkXfrVvia6MOOgxV3hkwIl8iMZ2AqsmKqCp6zSfiybq9oycopNZo4I3nx_pOscAD3KdzFJYib5XYBTRbCYevN_osxLzWwH85Ei28sIzf9mEYngFiQcOEd-Va7-UbRxjV6tEyI4z8-wbj95edJ6XxwtvgzDMhBF3Jd5LEV02UumfajkL1I1yRTTCHiY4m6s21uZGniFH62LrxzTvMrsLTdRhDxJpZnQcssRbGAk93yre_J7TTXpov7zGB6Q1htbNduJYfliy92O2geN76OvMPW7VV1pgUg2bi81x-05yoh9fPQ2JYpRhKhGnEeDNmfSkMQTMYB40JpplCGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇦🇪
پزشکیان در جریان حضور در اجلاس سران بریکس با محمد بن زاید آل نهیان رئیس امارات متحده عربی دیدار کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71521" target="_blank">📅 14:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71520">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64984e2da7.mp4?token=eE_XBkDqaeaHGwsPDdJCR1DfcQrPM9tVTRulddLzrEHn56LaQzkE9GqDeO6YUqxmauCnnrH4DqmO1Pq_b1DYwxZVq0q5LbvMzXqiI_aFiB26CAs-Pe66Sy84SlN9wDboyAwxiYCbz-NunjvOnmOvL2fi0wEa_bhH5BA74pzlN98qGlEhpPys8iqBZPugwhTHf4RLJtpf7d1_UsPVgSLq61BeKhYPEMjebsrhb5Zq_czXQ7r426JHj0duEtzHBAagl7toUvih22D_EoZPZ8TgJG_3j1myeo5ue00rrI_41xh4FTEFvAylsIuDFLu8WP8PT16ppccpik2bXhkjGLl_FCi-Nd_9ku6zGOi7putchyR2puiLaqfiQZnwUA7BgO9C8yoKl2XEoaXXLj_c__-F0ysO1Wo3MCSgA_-bMJ11eV9Iy0KpGJ92Lq5rXjK37nH79USOWpeKg0VtECloX9yGkqEBr03uBLALTbz8g20K14SHcL03uej1rWiykHjrpIk_pevrrlpW7TVPJXpce3df3vs41j5J4I75UbcSV_55RZ_AfHSiGdl7wMPL1HIAdzu2hx4OF_RCNQ4Era09aJZ3rqK7oY_UUESoFxz74q-20gdUh8Jcv-pi4vWEW8VWIjmwoD6cotLaG_y0mvvuLeoUVbby2NgZUe4xPQ7ALYq3xDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64984e2da7.mp4?token=eE_XBkDqaeaHGwsPDdJCR1DfcQrPM9tVTRulddLzrEHn56LaQzkE9GqDeO6YUqxmauCnnrH4DqmO1Pq_b1DYwxZVq0q5LbvMzXqiI_aFiB26CAs-Pe66Sy84SlN9wDboyAwxiYCbz-NunjvOnmOvL2fi0wEa_bhH5BA74pzlN98qGlEhpPys8iqBZPugwhTHf4RLJtpf7d1_UsPVgSLq61BeKhYPEMjebsrhb5Zq_czXQ7r426JHj0duEtzHBAagl7toUvih22D_EoZPZ8TgJG_3j1myeo5ue00rrI_41xh4FTEFvAylsIuDFLu8WP8PT16ppccpik2bXhkjGLl_FCi-Nd_9ku6zGOi7putchyR2puiLaqfiQZnwUA7BgO9C8yoKl2XEoaXXLj_c__-F0ysO1Wo3MCSgA_-bMJ11eV9Iy0KpGJ92Lq5rXjK37nH79USOWpeKg0VtECloX9yGkqEBr03uBLALTbz8g20K14SHcL03uej1rWiykHjrpIk_pevrrlpW7TVPJXpce3df3vs41j5J4I75UbcSV_55RZ_AfHSiGdl7wMPL1HIAdzu2hx4OF_RCNQ4Era09aJZ3rqK7oY_UUESoFxz74q-20gdUh8Jcv-pi4vWEW8VWIjmwoD6cotLaG_y0mvvuLeoUVbby2NgZUe4xPQ7ALYq3xDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ:
ببینید، ما کار فوق‌العاده‌ای انجام دادیم. می‌دانید، ما آنجا را تحت کنترل گرفتیم. ما واقعاً با اقتدار کامل بر «تنگه هرمز» مسلط شدیم و هیچ‌کس متوجه این ماجرا نشد.
ما کنترل بسیار قدرتمندی بر آن داشتیم.
ما یک محاصره دریایی اعمال کردیم که واقعاً بی‌نظیر بود.
ما تعداد زیادی از شناورها را بیرون می‌کشیم؛ به‌طور میانگین روزی ۲۵ شناور را خارج می‌کنیم که بیشترشان در شب انجام می‌شود.
اما به‌طور متوسط، هر روز حدود ۲۵ شناور را از کار می‌اندازیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71520" target="_blank">📅 13:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71519">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🎙
خبرنگار:
آقای رئیس‌جمهور، جنگ در ایران چه زمانی پایان می‌یابد؟
🇺🇸
ترامپ:
فکر می‌کنم خیلی زود. گمان می‌کنم احتمالاً درست پس از پایان دوره [فعلی انتخابات] باشد. آن‌ها سعی دارند تا جای ممکن مقاومت کنند تا وضعیت انتخابات را پیچیده سازند. اما فکر می‌کنم مردم متوجه ماجرا هستند، چرا که ایران نمی‌تواند سلاح هسته‌ای داشته باشد. موضوع بسیار ساده‌ای است؛ مسئله خیلی ساده‌ای است. ایران نباید چنین سلاحی داشته باشد. آن‌ها تنها دو هفته با دستیابی به سلاح هسته‌ای فاصله داشتند.
اگر این کار را نکرده بودند [و جلوی آن‌ها گرفته نمی‌شد]، اسرائیل را نابود می‌کردند، خاورمیانه را به آتش می‌کشیدند و به برخی شهرهای اروپا — و حتی فراتر از شهرها — حمله می‌کردند. و احتمالاً پیش از آنکه ما بتوانیم آتش را خاموش کنیم، به خود ما هم حمله می‌کردند. اما آن‌ها نباید سلاح هسته‌ای داشته باشند. با این حال، می‌گویم که [این اتفاق] به‌زودی رخ خواهد داد و قیمت نفت به‌شدت سقوط خواهد کرد. وقتی آن اتفاق بیفتد، قیمت نفت به‌شدت پایین خواهد آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71519" target="_blank">📅 13:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71518">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">⏺
🇮🇷
قرارگاه قدس نیروی زمینی سپاه:
درپی انهدام یک تیم تروریستی حرفه‌ای که قصد اجرای عملیات ترور در سراوان را داشت، ۴ نفر از این تروریست‌ها به هلاکت رسیدند؛ همچنین تعدادی سلاح و مقادیری مهمات و مواد انفجاری از مخفیگاه این تیم کشف گردید.
در این عملیات که تا پیش از ظهر امروز ادامه داشت ۳ نفر از پاسداران گمنام امام زمان(عج) نیز به شهادت رسیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71518" target="_blank">📅 13:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71517">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea8136d3aa.mp4?token=k-pl0jKSRWsUch9jhLn15cMggOVgmG4Ly2qCPmgHBE8cfFvN4I095SJYw4hH83iWQHof07I17HzSscmQHjTfj7Y0nn2lvrhw9ri2tLypivt6y_dXyr9ABT9d-jbsKkkzz2sNt6LpZMyjWHvR3bnshxadQblyUgGFfzT7-CsC5teRCmFTYI9yF8aGS5dtEh7tUD3tcsLig6dfRIS3FI0KgTCMLZ8Oc3xK9ddIEDv_OjzWzzxIGPQBvT1TGeKph7VNgDhIL-CGQRxRRZWcNNruAKxtb2A-zYCS8cBK0rTCc0_ZiQc-A1UtmQbDEBLEpPAkUe_eFrvRMGgQPzDm1Ony7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea8136d3aa.mp4?token=k-pl0jKSRWsUch9jhLn15cMggOVgmG4Ly2qCPmgHBE8cfFvN4I095SJYw4hH83iWQHof07I17HzSscmQHjTfj7Y0nn2lvrhw9ri2tLypivt6y_dXyr9ABT9d-jbsKkkzz2sNt6LpZMyjWHvR3bnshxadQblyUgGFfzT7-CsC5teRCmFTYI9yF8aGS5dtEh7tUD3tcsLig6dfRIS3FI0KgTCMLZ8Oc3xK9ddIEDv_OjzWzzxIGPQBvT1TGeKph7VNgDhIL-CGQRxRRZWcNNruAKxtb2A-zYCS8cBK0rTCc0_ZiQc-A1UtmQbDEBLEpPAkUe_eFrvRMGgQPzDm1Ony7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا ایران مسئول حمله به خط لوله «شرق-غرب» است؟
و به نظر شما عربستان سعودی چه کاری می‌تواند انجام دهد؟
🇺🇸
ترامپ:
خب، فکر می‌کنم همین‌طور است. احتمالاً همین‌طور است.
آن‌ها در حال حاضر در وضعیت آماده‌باش و هوشیاری کامل هستند، اما فکر می‌کنم مسئول آن هستند.
آن‌ها مدتی است که کنترل آن را در دست دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71517" target="_blank">📅 13:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71516">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9946b1f32a.mp4?token=Sw6hLsaAGSq9BUZ4FO38ATxqp0KBcKxycK7NoONdnpFpNF6xR8ssDdygCeKSVy6JmrkQoBL1RhPjR9aj3HgONgHx6I1EW7ALSj2qvoNAG4DpUZ6bvrbUnYSpPuTF2OrKTqwNedPXU9rWGU8UMQYkIjrEJLTfCQY-vHr6fV8sZ9EtXZRTSMM3Z48NR6VbFB8hZ4sT7GUguc9fLbEskYn8CwALTJ36sTXjTjhHqHD7TrwdvxOh5sXGAYm2Y_SWz77A0-iuN9grt0f8PRgYLSmCT4XxfjXwSZ6wn8woMAKs-ifdPZ522_sx-15EbyMo2M3ULAjEkA5Rd8QISl9ZjHF6rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9946b1f32a.mp4?token=Sw6hLsaAGSq9BUZ4FO38ATxqp0KBcKxycK7NoONdnpFpNF6xR8ssDdygCeKSVy6JmrkQoBL1RhPjR9aj3HgONgHx6I1EW7ALSj2qvoNAG4DpUZ6bvrbUnYSpPuTF2OrKTqwNedPXU9rWGU8UMQYkIjrEJLTfCQY-vHr6fV8sZ9EtXZRTSMM3Z48NR6VbFB8hZ4sT7GUguc9fLbEskYn8CwALTJ36sTXjTjhHqHD7TrwdvxOh5sXGAYm2Y_SWz77A0-iuN9grt0f8PRgYLSmCT4XxfjXwSZ6wn8woMAKs-ifdPZ522_sx-15EbyMo2M3ULAjEkA5Rd8QISl9ZjHF6rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
این رستوران توی تهرانه
نوشته : هیچی کتلت بی بی نمیشه:)))
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71516" target="_blank">📅 13:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71515">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db0f6d97e2.mp4?token=Mqbq7br6ypvE9gmvCNGQzPfZlsROdkbjQoN5-c0RsH2LM7PJ7gARcQd0Rm9ThJy6CWJ1CZFtiYoYiuFKaYQOO3v_7zrnUGdcaPohypOonyNoNog1Upn0Rak6IHd3zBhAW0dIBbOJwo2z40XUjffq80D905sG12xEDgD-hMTWgTn0cdGz9SqSEH_tgtuMm72X29x0G7Xpt3F-Itt6jZkNfLcTEvaGpI0rOjaOKAGsWCiR7cOwxFz-pntNpR6Grwwpat3Zc4wsNI27y6IdK5hT-5P0yofzcPN65nSUKdmeyKkHvGC0XKFZCE-XKChiRNprOrh9EgwuPC9FL3lffnZFwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db0f6d97e2.mp4?token=Mqbq7br6ypvE9gmvCNGQzPfZlsROdkbjQoN5-c0RsH2LM7PJ7gARcQd0Rm9ThJy6CWJ1CZFtiYoYiuFKaYQOO3v_7zrnUGdcaPohypOonyNoNog1Upn0Rak6IHd3zBhAW0dIBbOJwo2z40XUjffq80D905sG12xEDgD-hMTWgTn0cdGz9SqSEH_tgtuMm72X29x0G7Xpt3F-Itt6jZkNfLcTEvaGpI0rOjaOKAGsWCiR7cOwxFz-pntNpR6Grwwpat3Zc4wsNI27y6IdK5hT-5P0yofzcPN65nSUKdmeyKkHvGC0XKFZCE-XKChiRNprOrh9EgwuPC9FL3lffnZFwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
🇺🇸
پست جدید دونالد ترامپ در تروث سوشال:
با این رئیس جمهور بازی نکنید، زیرا نتیجه خوبی نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71515" target="_blank">📅 12:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71514">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1pMwAJZQyuaikr-5JrxH6AVoZRnV762IeM8j6qQzYfKZemKPj5SGDD0BbqdDAVT-PJTKwRhvoDpa96Ukfj2IUOtHXxL51FYz9SVVr5wrzxS2Q3VD1VblUoiH9kEJ3SjQ_5gMnDMFZPuj0Xt0RsNB4hvcWn2SUkJ2gqFaJ8Pu_ubznptmbUAmPJpE2y9jchZdmV6IfPoj1xVa_SLxnMme1Ae98zwRkaeRuqy2GHzfqOgxDJpudEZQG_yAFxFrVNgxv0EJj8n5xgTvlHLrG3nzbxG8mugw1r6jwvq8YZggUE7rsGM3v5O5DPQLd_Q1PCmq0LqlpRItwkZHVbwAF2swA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
طبق پیش‌بینی‌ها، یکی از پربارش‌ترین پاییزها تو راهه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71514" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71513">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71513" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71513" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71512">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLbWzoiAL4w7S3bFJCJTdlMlcgHJwLjBjQDLpibGJnPjsO4H5wSKmHXWG4Fr01db4vGO4pLZoRFiMdt0Gwq-CW52SxWDRxXiYnggmGaY_tcMXnFW54NVDghTMP5IyqKl_qTO5Le4ZgqM-x4NcLoMI5JnBODNy8sj-DXCRAvRSFFECi7-OLs4OGBJK6swRUDc46faAXxRc1BhEZ7Si0X2z6tAlOG9WKOXger4A_tHxDpF-uNiGZjx7suIyF8a9LLmR_1SrqBOc_5Hv2WHVhd0lAyWKkK5u_CbKIAjqCszDpCfYyIS9ToJl9wW8LSZNCiIWa9A_KsIjLy5ywVQUuWanA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت‌بین‌المللی
TrexBet
پیش ‌بینی کنید.
چلسی
🆚
لیدز یونایتد
فولام
🆚
لیورپول
اورتون
🆚
تاتنهام
ساندرلند
🆚
آرسنال
رایو وایکانو
🆚
رئال مادرید
میلان
🆚
لاتزیو
کالیاری
🆚
آتالانتا
پادربورن
🆚
دورتموند
🦖
🦖
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب برای بازی‌های امروز
🦖
واریز آسان و امن از طریق کارت به کارت و ارز های دیجیتال
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71512" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71511">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🇮🇷
معاون امنیتی و انتظامی استاندار سیستان‌وبلوچستان: محل تجمع اعضای «گروهک‌های معاند و تروریستی» شناسایی شده و نیروهای امنیتی در یک عملیات غافلگیرانه به آن ضربه زده‌اند.
در گزارش‌های اولیه، نام جیش‌العدل/جیش‌الظلم به‌عنوان عامل درگیری امروز به کار برده شده که هنوز به صورت رسمی تایید نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71511" target="_blank">📅 12:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71504">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d436ab6a3.mp4?token=CJp1aXqozNK2DIfMR-RugZwVHBSq-qOToTB-OLfVz90op8pOEw7Lxx31YImc46RSX9TRnRrrJLXoCqtxtFh0QEjLzmv8NsA3LHTfVk6yh5PBAmftit5z22Qky6UZQXly0Y9UX0bG49jE_x2ZNAD7EIpzgBNSCuEx-YogmRqLCAdTLh5eUj5XzKPb3yvBkzEU4FNLtQkvyE0iBDuEp_FiC2nSMuaXlVsU8qwfRlDyWc57Y3hWs0VB8Tr1m3rjoOhNJME2WzccLp1tlq5r7DYkZtBGpFLYvEuz63mxMhdRqd8Ce2Sj5tWMDESECzGF4kGc80t5YUMvnrszV8ivT9Av9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d436ab6a3.mp4?token=CJp1aXqozNK2DIfMR-RugZwVHBSq-qOToTB-OLfVz90op8pOEw7Lxx31YImc46RSX9TRnRrrJLXoCqtxtFh0QEjLzmv8NsA3LHTfVk6yh5PBAmftit5z22Qky6UZQXly0Y9UX0bG49jE_x2ZNAD7EIpzgBNSCuEx-YogmRqLCAdTLh5eUj5XzKPb3yvBkzEU4FNLtQkvyE0iBDuEp_FiC2nSMuaXlVsU8qwfRlDyWc57Y3hWs0VB8Tr1m3rjoOhNJME2WzccLp1tlq5r7DYkZtBGpFLYvEuz63mxMhdRqd8Ce2Sj5tWMDESECzGF4kGc80t5YUMvnrszV8ivT9Av9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
درگیری های بی سابقه نیروهای جمهوری اسلامی و نیروهای مسلح در سراوان سیستان بلوچستان
ویدیو ها مربوط به چند ساعت پیش
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71504" target="_blank">📅 11:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71503">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🇮🇷
🇮🇶
رسانه عراقی نایا به نقل از یک منبع:  دستور فوری و جدیدی از سوی فرماندهی کل نیروهای مسلح به بصره ابلاغ شده است که بر اساس آن، گذرگاه مرزی شلمچه با ایران از همین لحظه و تا اطلاع ثانوی به‌طور کامل بسته می‌شود. این تصمیم شامل تردد مسافران و همچنین جابه‌جایی…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71503" target="_blank">📅 11:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71498">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba81cb21e1.mp4?token=qQMtfbLaYh33bVsPGlVCE_3IxVqdRGKGdakfa_7Tw4gtGLTqIHeXO4YmMAmYRo3Z2oYGXzJypJnU44RFyNGXhYsNfe_bZhY4xRurT9oi3E1YLK5vc2M6Kg9KZvaV1LtHr-Aot_vSCdT13j6m4tOdvKCrE1P8StAZq0PVRlgSOUOvyv5m9Qna9FmAnFrOfFZxlzELrf-ZsZTVCF-NKGb42isR9iTWmmb8qTHVT4mSO7QeiB9qOVIvC_BV1L_eIvKhdulYAMkaaCkzp_0GssLMt4_RYabbruWcSEWibwADoKW3mba2Cx7DmeckLch4H8cKbVTY0MyTOpGnvzydne-Rgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba81cb21e1.mp4?token=qQMtfbLaYh33bVsPGlVCE_3IxVqdRGKGdakfa_7Tw4gtGLTqIHeXO4YmMAmYRo3Z2oYGXzJypJnU44RFyNGXhYsNfe_bZhY4xRurT9oi3E1YLK5vc2M6Kg9KZvaV1LtHr-Aot_vSCdT13j6m4tOdvKCrE1P8StAZq0PVRlgSOUOvyv5m9Qna9FmAnFrOfFZxlzELrf-ZsZTVCF-NKGb42isR9iTWmmb8qTHVT4mSO7QeiB9qOVIvC_BV1L_eIvKhdulYAMkaaCkzp_0GssLMt4_RYabbruWcSEWibwADoKW3mba2Cx7DmeckLch4H8cKbVTY0MyTOpGnvzydne-Rgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پسر تهرانی بعد از اینکه با دوس دخترش کات کرد، رفته تمام اکسای دختره رو جمع کرده، واسش دسته جمعی آهنگ خوندن تا قشنگ دختره رو بسوزونه و عقده هاش رو خالی کنه...
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71498" target="_blank">📅 11:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71497">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aa7081550.mp4?token=sXudduic9S66cqA3vQBFkJqwFOnWWPEgIWkWGbDxVqVJmE2ZsuCY-1XerUCwcqHPXdf6kss21TqkmViUeyG7tZcZFu0ZO61E3FlnscID07F0fgDMOl2h66OEfHvxhv0M43IeW33zqkYUpzYQgUtl3gUj_ANPswV2KiztfL0EEOPiTZGV_YOUckQ_gWWJxG_n4aSqthdldtCge2HSeZyZK6yGh5ML__ERIZwWMVbVVgMXKTGnv6PpvihDncKqwStPtXKozmNMYj7eGHXbSD2Wr0XqSz7RLTvg5tHcpS0bxv9xcL3tB6L1dpXOWe0BJTuviiE9r8Nm2-E3wT2oOjapU4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aa7081550.mp4?token=sXudduic9S66cqA3vQBFkJqwFOnWWPEgIWkWGbDxVqVJmE2ZsuCY-1XerUCwcqHPXdf6kss21TqkmViUeyG7tZcZFu0ZO61E3FlnscID07F0fgDMOl2h66OEfHvxhv0M43IeW33zqkYUpzYQgUtl3gUj_ANPswV2KiztfL0EEOPiTZGV_YOUckQ_gWWJxG_n4aSqthdldtCge2HSeZyZK6yGh5ML__ERIZwWMVbVVgMXKTGnv6PpvihDncKqwStPtXKozmNMYj7eGHXbSD2Wr0XqSz7RLTvg5tHcpS0bxv9xcL3tB6L1dpXOWe0BJTuviiE9r8Nm2-E3wT2oOjapU4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇹🇷
یه گزارشگر تو شهر وان ترکیه طی یه گزارشِ خیابونی، نظر مردم این شهر رو درباره گردشگران ایرانی پرسیده که حسابی وایرال شده؛
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71497" target="_blank">📅 10:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71495">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faeed5163b.mp4?token=N3g7vOp2t8_Su4mLLiQj2qDcRtJGxPVrD5yLoD2LuG4x52we33IogBjKf_Nw_y84g7zr8M7ThGLm_MC6SMVzjB5-EQSxH3nqHG47A9YTNu-qf5UQ9DbPm_mYbY0so105miV2XuhhuwwM6DHtZfwFJoUPD-I1J33M-wbTRIYFDJ2prYxH4vL4lYYO3n1BXI4Yf_y7BBrMjYnU922yS_1VhWEKrGBUftuKv5diFRkSWPTY7px9PLk23V8ur1jL0ElH-6366dnnPadZIaBccKPoZKSY54OO8-CFjR2mX00CMAttRhBmuNinteOzyz3ZW9f_sclxQGsGSL8nTYCYGzucbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faeed5163b.mp4?token=N3g7vOp2t8_Su4mLLiQj2qDcRtJGxPVrD5yLoD2LuG4x52we33IogBjKf_Nw_y84g7zr8M7ThGLm_MC6SMVzjB5-EQSxH3nqHG47A9YTNu-qf5UQ9DbPm_mYbY0so105miV2XuhhuwwM6DHtZfwFJoUPD-I1J33M-wbTRIYFDJ2prYxH4vL4lYYO3n1BXI4Yf_y7BBrMjYnU922yS_1VhWEKrGBUftuKv5diFRkSWPTY7px9PLk23V8ur1jL0ElH-6366dnnPadZIaBccKPoZKSY54OO8-CFjR2mX00CMAttRhBmuNinteOzyz3ZW9f_sclxQGsGSL8nTYCYGzucbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئو وایرال شده و پشم ریزون از کنسرت تیلور سوییفت؛
خودتون ببینید به چه دلیل وایرال شده
😏
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71495" target="_blank">📅 10:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71494">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‼️
خورلسوخ، رئیس‌جمهور ۵۸ ساله مغولستان، هنگام بازدید از یک یگان نظامی، حرکت پرس سینه را با وزنه ۱۰۰ کیلوگرمی در ۲۰ تکرار انجام داد.
او که پیش‌تر افسر ارتش بوده، نامش در لغت به معنای «تبر برنزی» است، باشگاه هارلی-دیویدسون مغولستان را تأسیس کرده و در یک گروه موسیقی گیتار می‌نوازد؛ او همچنین جانشین «باتولگا» شده است که خود قهرمان جهان در رشته سامبو بود.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71494" target="_blank">📅 09:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71493">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a695c5e874.mp4?token=s1JDuZMCKWEowZJ7IBJTueMVgUS3xD9RtrNHx3VW_67hzCuToYHfaYtm9h6EdpfQr1eOYOTRfqOJ8oHYrTSCkEqIYOWChPP1Sk2DGmWxfgiZmQCD6JAdhSHJCccplLwCIzT0LIevga5suWABsGa5Qe1whLkJiWKSqwhpGPntG4lVGeaNBvsWg0KOmWq5QHEAB---Mj123M2vlixulu3iWgqPyNEeY5vaN-SwhKZ0r6M-hux2ILD20TkiugW3R2ElXVDBV05xwCwRlWxuXEU5wlmtsz7XoJynNXbEcwLS4cn5SqKaB4zIFEO-n1IuRkIiykrkCv5RUP1Zw89WVayVYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a695c5e874.mp4?token=s1JDuZMCKWEowZJ7IBJTueMVgUS3xD9RtrNHx3VW_67hzCuToYHfaYtm9h6EdpfQr1eOYOTRfqOJ8oHYrTSCkEqIYOWChPP1Sk2DGmWxfgiZmQCD6JAdhSHJCccplLwCIzT0LIevga5suWABsGa5Qe1whLkJiWKSqwhpGPntG4lVGeaNBvsWg0KOmWq5QHEAB---Mj123M2vlixulu3iWgqPyNEeY5vaN-SwhKZ0r6M-hux2ILD20TkiugW3R2ElXVDBV05xwCwRlWxuXEU5wlmtsz7XoJynNXbEcwLS4cn5SqKaB4zIFEO-n1IuRkIiykrkCv5RUP1Zw89WVayVYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حسن روحانی خطاب به ارزشی ها : انتقام خامنه‌ای رو امام زمان که ظهور کنه میگیره
وسط مذاکره برای اینکه راهی پیدا کنیم که جنگ زورتر تموم شه یه عده میگن باید انتقام بگیریم خب چجوری ؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71493" target="_blank">📅 09:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71492">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🇮🇷
🇮🇶
رسانه عراقی نایا به نقل از یک منبع:
دستور فوری و جدیدی از سوی فرماندهی کل نیروهای مسلح به بصره ابلاغ شده است که بر اساس آن، گذرگاه مرزی شلمچه با ایران از همین لحظه و تا اطلاع ثانوی به‌طور کامل بسته می‌شود.
این تصمیم شامل تردد مسافران و همچنین جابه‌جایی کالاها می‌گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/71492" target="_blank">📅 07:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71491">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/71491" target="_blank">📅 01:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71490">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pdv0O1qmnvGwWNPGeQOR3QSxDFOmzlgnfRMmD9vI0787fJO8wrqBAuK8zUkBR35KUM5x-UuV8xkVi2MnZQIeeVKmxlqDsOwqCcMn22ueaHz0w6rCHNMXysU9WmlRUCUxnLxRDnaOOQKZ4NWduxo1ZxMYyWuThtZpDsQ2wRikp9puKjHAyAZ-sKaROFVoAk4AyMEElJfDp1fKcJSGG2iAn5CMT5kT7zGyr63VwKZrVUYh_5RaxW8Cyijt8v7_r1BmwPX3Jx4OlsnCDwp6atD5OrgzrqCt8sKZQKjNExbcOWEzaTDd5H-CHJd9Rid36gB7fgGeBcBkiaJ0c1Nse63glg.jpg" alt="photo" loading="lazy"/></div>
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
دو زمان، دو کد، دو فرصت شکار 1 دلاری.
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/71490" target="_blank">📅 01:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71489">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c20cfcda3a.mp4?token=Q6qHvZUlCJk51Bc1yU412HFt0z_aDp35S6tSwvLUCCqkyX5oGhFQdMU3HTyWDcEfwe3sa9nFTj4mEy-QCeafkwccrqYu7dObA4ZXtfVVUzQEu02Z7awnqcpRtmrJtmsWvqZ6zjq7UmI26MJ2OXWM04zLOr9NGKu-Kpy5mIMbDMQMoa1yXMWx0wMy9Y9MvMoz2bLyHDbYjzTXh1S3zbhQRG1cCg-5xINN4gDikqAsCAN3WEr7KYWxvPkNm8UFaQ36olC2McCDV1wqNaaEYTopHwZhb0A2JWRIoeoz0LO9dX9mOsT85fHtSFhbKjhAPm2H9CrIlFM7ruUkOTkbrQ9VpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c20cfcda3a.mp4?token=Q6qHvZUlCJk51Bc1yU412HFt0z_aDp35S6tSwvLUCCqkyX5oGhFQdMU3HTyWDcEfwe3sa9nFTj4mEy-QCeafkwccrqYu7dObA4ZXtfVVUzQEu02Z7awnqcpRtmrJtmsWvqZ6zjq7UmI26MJ2OXWM04zLOr9NGKu-Kpy5mIMbDMQMoa1yXMWx0wMy9Y9MvMoz2bLyHDbYjzTXh1S3zbhQRG1cCg-5xINN4gDikqAsCAN3WEr7KYWxvPkNm8UFaQ36olC2McCDV1wqNaaEYTopHwZhb0A2JWRIoeoz0LO9dX9mOsT85fHtSFhbKjhAPm2H9CrIlFM7ruUkOTkbrQ9VpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
❌
🇾🇪
تصاویری از حملات هوایی نیروی هوایی سلطنتی عربستان سعودی به بندر «مخا» در جنوب غربی یمن که تحت کنترل انصارالله قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/71489" target="_blank">📅 00:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71488">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgS_QQmGGAPcVfDhRJKj1BfjgnrAvCJmZ25f1e6mAAYAWd3Vn7Z4c6Vra7Mu0qme9zS2xPD0PD3PdmjKXSQZU8retPk4pALVst6siMHJ-aOlcAvw_j9Z0ELsLtLQUyq9f5JmxKA3mlGu0Y3dh-VMGge5VWIqvAcBkOFBqmimdDplOz4m1llSyWYRIQoFns9iat6fivtzuy51PM58q0D749xZnHYeujOqmMTepiUHIyZdRhT39nXISRWG3_IzQWkkaxQmj6G4fpM1kBZZGH86w0ttd4wErXpxlI-rfXxiL1nrec9c-pW5z2sCBncQL161s8SUu-r63mGss6Bec18iOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با پول ۲۰۷ در ایران تو کشورهای مختلف چه ماشینی میشه خرید؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/71488" target="_blank">📅 23:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71487">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2da32c63e2.mp4?token=vgDaH3RyPImyEsZ8s8QHmgFsKgz-uN0_o0eAXeR6yVRelPKiAeyPfqXnnNzdrqAJfSSCbkdxFSBQvcIA21kGeskKDqUjEF6vPhPFB3A_0LAmml5_vrVttlr8AcJ0k3J_t_87mzmlcXAOtIdTeFplzLGkoyyNahtVXSy8dGUMB0OGTS-5nqYA8vDOjfenX25GW-q6NkD__TWXFcTlfBVk5bjecyCEfNWXYZkV8lGQdpM_AZGhXk7LXSMvPM-NjPZe3qmnwEzACF7c47FNgeRhUnVPZzTPZx1QdR4G0TLw_4_7UEzEXXiQYFbfjCbXZkXfDnDcVvNP4vMJp7E1bjc4Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2da32c63e2.mp4?token=vgDaH3RyPImyEsZ8s8QHmgFsKgz-uN0_o0eAXeR6yVRelPKiAeyPfqXnnNzdrqAJfSSCbkdxFSBQvcIA21kGeskKDqUjEF6vPhPFB3A_0LAmml5_vrVttlr8AcJ0k3J_t_87mzmlcXAOtIdTeFplzLGkoyyNahtVXSy8dGUMB0OGTS-5nqYA8vDOjfenX25GW-q6NkD__TWXFcTlfBVk5bjecyCEfNWXYZkV8lGQdpM_AZGhXk7LXSMvPM-NjPZe3qmnwEzACF7c47FNgeRhUnVPZzTPZx1QdR4G0TLw_4_7UEzEXXiQYFbfjCbXZkXfDnDcVvNP4vMJp7E1bjc4Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇱🇧
🇱🇧
رسانه های نزدیک به حزب‌الله لبنان وویس هایی رو از اعضای حزب‌الله منتشر کردن که در زیر ارتفاعات علی‌الطاهر در تونل ها گیر افتاده بودن و درخواست کمک میکردن.
همه این افراد بعد از حملات ارتش اسرائیل و نابودی تاسیسات زیرزمینی کوه علی‌الطاهر کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/71487" target="_blank">📅 23:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71486">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68083de4e6.mp4?token=MYqEV_P9w-nBrfzW81glVz50Rnv1Zh3TNb1t2aLNgjVm0ErHJsIX_sYdgZGunfT-a6-azumvw1UF-mWxVqMzr8Nn7WAFSf24nXzutwf8UHp6Li8SBHHnaa1iCSdYjhG2Tgqq9f5gx8zVSbvOIImwJKcVjC5RJvpXBp-gNnqZS3Fi8PoQ4NOV6eha0RZCW9rGqqcZpCHs8fn54dLzWu8QIIAPFmiFEsrsJcYClpoAL4fa1jSswNeBZU-vMvtFmkWUUzBEb7Gxcpm-cicwdElzoeUQV01L6kRV4N5bUTj-ec45cPO4RnQePlbJk5zrXYz7R5yZHWVtLcyfA9hLYf_kWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68083de4e6.mp4?token=MYqEV_P9w-nBrfzW81glVz50Rnv1Zh3TNb1t2aLNgjVm0ErHJsIX_sYdgZGunfT-a6-azumvw1UF-mWxVqMzr8Nn7WAFSf24nXzutwf8UHp6Li8SBHHnaa1iCSdYjhG2Tgqq9f5gx8zVSbvOIImwJKcVjC5RJvpXBp-gNnqZS3Fi8PoQ4NOV6eha0RZCW9rGqqcZpCHs8fn54dLzWu8QIIAPFmiFEsrsJcYClpoAL4fa1jSswNeBZU-vMvtFmkWUUzBEb7Gxcpm-cicwdElzoeUQV01L6kRV4N5bUTj-ec45cPO4RnQePlbJk5zrXYz7R5yZHWVtLcyfA9hLYf_kWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از یه دختره که پارتنرش یه ترنسه
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/71486" target="_blank">📅 22:15 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
