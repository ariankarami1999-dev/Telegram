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
<img src="https://cdn1.telesco.pe/file/E2K-c0os9-UHJpv4ynaJUeSZ36tCo_BzDR_FNVfkgyJR_psJr8o3ldBo5ZGZ6fNV5gtzY_EOrY0v5COI0qDUnnKwPeMlP9lreuHlNmO1Yl3BaSIDTgNX5TG1WosxzbSY1kDTPcuTjWOKRlnbMPqW0M-LFv-yh5WFxX_yXuJhRLHj2xw_WSjJseGnHZSwWGw6NpzgWFxtESQU7xxfQMrSmAJoBv3GMZ4smhPgXEcanys843W4j7I62D7ADNn8ydEiUKbnAnKStbr8FtBIJLCuFJgCq0auv9zfNOTDg5GKGK3pdx2dq5cYcg2eh3XYY9_wLQtOwVvUFyaBorMK8xpQWA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 02:17:12</div>
<hr>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JU6Tm93GeGtdhkjGRBwZ64GVQF9ckLa_WYW9BU1fFwp9nz_qgHggifdGhU1zpCBLkOYordaj2edfsGU2jCzsew4BCEaGjN_QPuhTchGs3T4Cnw_z25Q5yDpEjVcgWOFul7diD-fmeovsF5q-VkMv4h96TkcXgyTLrptvZOR7yhwfrU4cpYaXJOMubmGUzmBVT4h1RULb_HD1zQYrc1-ewlMpUNppiWNZ9xrDZLomPSXxL5gemQ47f5xJov1PdcVRTejg7Vw___zXxIU-anpGX2FmNI0ZbjgFuOczLkolpdIac0fF9ZMWD0O6fM4gU4MouuyN_KrKvGgpx-YfHtX0xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قسمت ویم واقعا بامزست
https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/MatinSenPaii/5409" target="_blank">📅 00:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">هرمس خوبیش اینه که سمجه. اگر از ترکیب هرمس + مدل رایگان(مثل mimo) استفاده کنید، واقعا غصه‌ی توکن سوزی یا انجام کارهای سختتون رو ندارید</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/MatinSenPaii/5408" target="_blank">📅 23:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مدل Claude Sonnet 5.5 معرفی شد. هم قیمت با GPT-6 Sol، اما به شدت قدرتمندتر! نزدیک به Opus 5.5  • $2/M input • $10/M output • $0.20/M cache reads 1M context + 128K max output
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/MatinSenPaii/5407" target="_blank">📅 23:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WL_LaFZ4MkQpuLnWHMInJFpZYuBwThlUN5Uj7-shMUasPuDb1k_Ax1dRhTlVxQXMKBQ4vjFeETMincwbc19_-2OMgywHkFwLUyTXako4UM7kJzCekyFtRw4VjlwirZtJxhFABrCQukY7uIWP0a2Zy9xBcooLZ7251HjH1w8YXu94BVO-0cYf2T5yV8Aa9v2HsDb7eoPyGFO8KhtSr3OYVUiK_ydBbvqSoz8zjWayHDeDHr_4T-dOdxyTzsj38Hvq1z_hw2jojHmKXv7CDuUidhxg7MfazKFtrsI4Oc1lNh8RL4M9WIYWYlTl4XT4Te0rgRXXzwgKv_8aqdqBPP3OmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FW9PZHwFve1TH6p6mgnjQkjiKVByWBZKM8fwXIgtUvziT6VTIKkIKueERLCkT1vmaDG_cXSkwZNLHsnXjFWAogptu6NuwAW_DdTnNz2ZqQFQEYq6zYwaBelKtzvMi172Hx4jW4QnW7Ub9WBCG2i88lyw_MkV3cazIsuliAE5gBKMPFZb-rRXwidgXOpT5Yd9j7a3DkPXtmPbs63V07R_6i2-J8EhiUQjtVb5Pl_q2S1PK_h-IY_7nQCDBvwmHxMBL_-nJUlhWHh4AFeqM2Ug6domhMFaE1o8Nm5sL2TJUFueVdQdd2yPojXu0i-QDIfCZ3emuy5z6m-2N4ADULRWNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق لیک‌ها و یه آیدی تست، امروز و فردا قراره Sonnet 5.5 منتشر بشه و گفتن که از GPT 6 Sol که سر تره، و نزدیک به GPT 6 Astra هست با همون قیمت Sonnet
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/MatinSenPaii/5405" target="_blank">📅 22:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">389 تا ویدئوی ساخته‌شده با Opus 5.5  از موشن‌گرافیک و ویدیوهای توضیحی گرفته تا صحنه‌های ۳D و بازی.  هم ویدیو اصلی و هم ریمیک رو می‌تونید کنار هم ببینید، پرامپت‌ها رو هم مستقیم کپی کنید. https://skillry.dev/ai-videos/opus-5-5
✍️
ai_ba_reza</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/MatinSenPaii/5404" target="_blank">📅 21:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82410567b8.mp4?token=KtBQP70suXlNGUHbWbFdC5IDH9Ri6iuMKsY9xuXbXXLs4JnwkXTqZQ5VqgwUrJdbKl8JmhWzAh-A5tg9VB7Hlj3zQcF_0W66sQIOVyz74xq-OoSuzrYr_2O5S4czn6cVcR0MAfBHGiOKQ6KTIRPJYbYvwC_l2IKrPlmS9nqtCC_O7toFlVgzo7aShP57zMCSc6H41p0q23b7fIJYOHPmStgmVpbZ0XYmtRcBbz5jmukXJczJXpn7_4fT28UM8shNtbqMqL46H6ehiY0YQ0kor32uo6u7Ye2-I4m7rRCC-HaQ1r-HznJszSF_OltfOsLpGTQgG0hwbJz_mxoJ5iCrIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82410567b8.mp4?token=KtBQP70suXlNGUHbWbFdC5IDH9Ri6iuMKsY9xuXbXXLs4JnwkXTqZQ5VqgwUrJdbKl8JmhWzAh-A5tg9VB7Hlj3zQcF_0W66sQIOVyz74xq-OoSuzrYr_2O5S4czn6cVcR0MAfBHGiOKQ6KTIRPJYbYvwC_l2IKrPlmS9nqtCC_O7toFlVgzo7aShP57zMCSc6H41p0q23b7fIJYOHPmStgmVpbZ0XYmtRcBbz5jmukXJczJXpn7_4fT28UM8shNtbqMqL46H6ehiY0YQ0kor32uo6u7Ye2-I4m7rRCC-HaQ1r-HznJszSF_OltfOsLpGTQgG0hwbJz_mxoJ5iCrIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">389 تا ویدئوی ساخته‌شده با Opus 5.5
از موشن‌گرافیک و ویدیوهای توضیحی گرفته تا صحنه‌های ۳D و بازی.
هم ویدیو اصلی و هم ریمیک رو می‌تونید کنار هم ببینید، پرامپت‌ها رو هم مستقیم کپی کنید.
https://skillry.dev/ai-videos/opus-5-5
✍️
ai_ba_reza</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/MatinSenPaii/5403" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اگر کانفیگ‌های کلودفلرتون از کار افتاده، با این روش می‌تونید دوباره زنده‌اش کنید:
https://youtu.be/dQKfkXnThCE
به زودی یه ویدئوی آپدیت سعی میکنم واسه اش ضبط کنم</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/MatinSenPaii/5402" target="_blank">📅 19:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KeliG7kcDH7BvIFtkArRoNWAGVATRx1FLSVJIYBeB2ZOyJkxVqhE32HVITMGxhLQwh5SR4qLZ0UC9rrMrnMH-o-vvbOetHKD6bX46tHVcjUtyy2tVX0VxnzSro7o2ZVQpfwDbQOaPWOeBgGvQzufRaauPHUm1nYAdR-6dNC_0_Spox69HFjN6661vAQOde1IUpzjW44eJB3epcPBn2bGNk-bWajvXHQxctyRTZLsOkhq8yjTo4cNZEU9Ic3lN-byJFGW2xrMnFkDbl1-8002ezsx9--rJ-9ciyZu8I_x5GcL-XbNVZK7vX7dvuWvo6ia4_jHUz05lfo6QnJYaMNI8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حافظه‌ی Hermes: از
MEMORY.md
متنی تا گراف دانش
نویسنده این پست ردیت گفته بودش که مثل خیلی‌ها به دیوار
MEMORY.md
دو هزار و دویست کاراکتری خورده بود (۹۹٪ پر و مدام درگیر نوشته‌های کهنه‌ی توی کانتکست). پس برای همین تصمیم گرفت plugin مربوط به ارائه‌دهنده‌ی حافظه‌ی Hindsight رو توی یه کانتینر Docker جدا راه بندازه؛ بعد از کلی تنظیمات مختلف، اولین اجرا و تجمیع گراف تموم شد.
که این باعث میشه:
1- دیگه محدودیت
Memory.md
رو نداشته باشیم
2- سرعت خوندن از حافظه وحشتناک بالا بره
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/MatinSenPaii/5401" target="_blank">📅 19:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5400">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jVvsstZqvmsxua-EelAWZzLR9aeC8HTz8cMuVSNeqf7V4syPeC4qOCTKgyrzWCzr8O4SaPwFqTWaUkECM2CKueiJnyr7flnyblm_ZvBCNmcuQaCkOzlQNUfkGAj5uvUkKNpsTt1a14J86ZKHpYIAxzUpvjUP4R9oraqC9YamdRPUTbFya196UrXzk7IOIVvMEaZG65s9r1wZuaoG09pNPB0o0xbSKXi-PQwPC_OybH-u7wx6HcSUoSSR2oZ2v0u1LvM8rX5U4QXo8bdWbFNN3eXfB5hZlPcrI1Nui6_BJ321RuBjgLtQfJeMdlGREV8yozniPqJkStLB8-wagK_Ylg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر کنم گوگل چند صد میلیارد توکن از نسخه 4.6 ساننت و اوپوس خریده برای Antigravity و نمیدونه باید باهاش چیکار کنه
😂
مشتی 5.5 اومد 6 هم به زودی میاد ولمون کن دیگه</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/MatinSenPaii/5400" target="_blank">📅 18:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5399">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zqo5U0Iat_KjDz-Hxx33Aj6pED45aEKi6TGC3fqueRkvkj8q4L0q5NuuJ8gEFgvKDW7N_mHaoMgHHLWxcJ7YJYz_d46hKkIwQjVPyL05BPrHrGYZXdd6GoyO3mb9jNIIl6rfXU9mz47H8XPeTHcR8JiRnogApY5f0Kox7fW3rnQrxcXSaPrHYsAO20FkOpqZ031V2oTqvTrgh9uprT2Mm9ghX3ftByjrC8pSF5swtfgN7zlwWoRGihSRPpQNOpu3Y3ZPRQYL_EqP6go30YLQYYF1kLmiOHm_hXild3lMwGWt74hxs5zOp4SGc3-QhXmNv7kAPP4gVRgtMqsrKXlEhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی ساخت نرم‌افزار رو آسون کرد، دیده شدن رو سخت‌تر
قبل از AI برای ساختن به توسعه‌دهنده نیاز بود؛ حالا آدم‌های بیشتری همون چیز رو راحت می‌سازن. ولی تعداد کسایی که حاضرن پول بدن، یهو چند برابر نشده. نتیجه: وقتی ساختن برای همه ارزون می‌شه، مزیت واقعی از ساختن می‌ره سمت توزیع، ایده و شناخت مشتری.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/MatinSenPaii/5399" target="_blank">📅 17:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5397">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eoyGdTJ0pnJNeCqXnAPbce9G3cr1Gg0BjiMfE7Pjscav_0foTQVKTzlfJKE3CHK37e_qTPkC2N_Cop5X9s3C4_fsBU7WX6YkLFFVdMHSSI_T9W74uJh3-n6_Y1rU9J9GfOjjhq7Up3aARSl2wTiZCHhv2EFJCv_OpGsSFYP49Fk4H69PB8B28V8ziV_ud7w-kfCnSZ7UtAovdc3GjMANFLFWblZWJj9KuDryhHtnSpHjDa9xx2VnYZcARnjxU_C4ZSRG7MkbpLihYE9hS7_r4PObbslbTkzhwCIdthhkj45fKhlQ8hqKeDFk6jeLesQzD44J8vNR--o9ZpdMF-MqdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CPeEmHiGN0DJlFCTuF7-asgs3j-zQ_rqL40LT9y5nxbsOaLJxuAVJ8GKu8dKS_Nyx9ucv7cjIrque0Jl3f4AZGLjYeYgfLiONRArgm5paNmCL_xK9P2EP-ajBgPxd9xlKxHgSCV18PSHxkrDrUdP91Uf6GkRKVXv9uVzSpi2lZ_4RoK0ucoQocucUu-hVXD7TFrudEPnQ_hg2VZJToCMl8UVE2n43ZKivQMj2VzufhH4R7EJOQY2gncDrv8c_uQ4kl-V-x4RjiAN_7jpGos__rd7ICCFM9wu_FMKAQo05A65XkIA00YBar-d-94keAoq8uuvlGUOJe7131st_mZmbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این فتوشاپ اوپن سورس که مسخره‌اش کردن یه دوره، سازندش اومد توی ردیت درآمدشو از دونیت‌هاش گذاشت و گفت محصولم خیلی پرطرفدار شده
😂
لینک این فتوشاپ اوپن سورس که اسمش Photon هست:
https://tenzen.studio/photon
لینک پست ردیت:
https://www.reddit.com/r/SaaS/comments/1wsac6d/i_replaced_adobe_photoshop_with_a_free_better/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/MatinSenPaii/5397" target="_blank">📅 17:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5396">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">طبق لیک‌ها و یه آیدی تست، امروز و فردا قراره Sonnet 5.5 منتشر بشه و گفتن که از GPT 6 Sol که سر تره، و نزدیک به GPT 6 Astra هست
با همون قیمت Sonnet
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/MatinSenPaii/5396" target="_blank">📅 16:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5395">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">محدودیت آپلود
۶
پکت رو دوباره دارن اعمال میکنن.
از چند روز پیش برخی سرورهای شخصی دچار این محدودیت شدن.
از دیشب وبسوکتِ (alpn/1.1) کلودفلر هم برای برخی دامنه ها مثل
workers.dev
.* دچار همین محدودیت ۶ پکت شده.
در نتیجه کانفیگ‌های ورکر کلودفلر به صورت عادی در دسترس نیستند.
با ech ,
fragment+fingerprint
و چندین روش دیگه میشه این محدودیت رو بر روی کلودفلر دور زد.
فعلا تغییری در وضعیت warp هم مشاهده نشده.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/MatinSenPaii/5395" target="_blank">📅 16:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5394">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZYc8EEzXnPWMoycvwPSjE6QvtGSjbD4358Lk-rkHc0BMQmODf16B_ReRlPHy0tDqLgEYoSk7_ZewzAWRHhkuPMhmvTgJu0-6KZhvhbGr4-8oLrBenVQkeTTC8NcIj3tDJaDhLorkutNNeViz_U6KBi7OdbrpvSiPCdw7azZUH75wJXlKsd0xH3K0ZW391jlwZeJ_gG_2V399m9mx-JC_YJaauMgp8vJ_mJPWOYkaZPrEyx5sui42Tn5wdqinqE8gg24BN0hMa9ylhN0MIbHuNHCePEkLIIpheypnRxKEoTv2yAkre74aX2IkrAy6JxoDr7XDYLKh285jvGBkVsomuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/MatinSenPaii/5394" target="_blank">📅 15:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5393">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jNaeZa7Ub4Lc4fYYQJbFiAU6ETMjNVujGHfYjGoV0P4UDWmAdOpI4A3qUWoXEJC3I8-312bSeKGJ3Y7-cHS6CRINR4Dz66wSYJe7LX3FUG6rk8A13-REPLequf8KoDoFU83Qzc4sEOWjR14ndVbCActniY9sy0VZQZW3T1BKlGOrQBwKpyiub3HBX9ycDtv092aCCoAlUrwE20zDxT-eniugP_8otC7fAwalLIDp_5uN1bHZ2HjXGXgbvlc8YdmJ_rIf8dIo3UXnBF9y5p2B8u7S-wTJZg9VtlMm8j0R_79qODOHLwkzHia66eyft6umv-DPS--aHK1SLi_ImlCP6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک خسته‌کننده نمی‌خواید؟ بشینید جنگ مدلها رو ببینید
🤣
سایت TinyAIArena یه صفحه‌ی ۸×۸ هست که چهار مدل توش دارن واقعی با هم می‌جنگن؛ نه یه جدول امتیاز خشک و خالی. روی هر مچ کلیک کنی می‌تونی تماشاشون کنی و ببینی بالاخره کدوم‌شون باهوش‌تره. کل پروژه هم روی GitHub عمومیه. البته این صرفا سرگرمیه و جدی نیست، اما همچنان برای دیدن اینکه مدل‌ها توی یه محیط محدود چیکار می‌کنن بامزست.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5393" target="_blank">📅 07:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">قضیه‌ی «انسان در حلقه» خودش داره از دور خارج میشه
مارگارت مچل و همکاراش توی یه مقاله استدلال می‌کنن که راه‌حل «انسان رو نگه داریم وسط کار» توی عصر AI، اون‌قدرها هم ساده نیست:
هم طراحی فعلی ایجنت‌ها نظارت مؤثر رو سخت می‌کنه، هم استفاده‌ی طولانی مدت از همین ابزارها، توانایی‌های شناختی خودِ ناظر انسانی رو هم کم‌کم از کار می‌اندازه. پیشنهادشون اینه که نیازهای ناظر رو به‌اندازه‌ی توانایی خودِ ایجنت جدی بگیریم؛ تا هم توی طراحی محصول و هم قضاوت انتقادی تمرین کنه، و هم توی سازمان‌ها با پروتکل‌هایی که اثر اتوماسیون رو جبران کنن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/5392" target="_blank">📅 23:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">بعد از ماه‌ها که برای کلاینتم آپدیتی ندادم این مدت روش کار کردم و کاملا بهینه و بهبود یافته. UI/UX  کاملا بازنویسی شده با متریال گوگل. و خیلی فیچر های شخصی سازی داره بخش "رابط کاربری" از تمام هسته های حال حاضر پشتیبانی می‌کنه راحت میتونید کانفیگ هاشو اد کنید،…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/MatinSenPaii/5391" target="_blank">📅 23:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سندباکس‌های ابری Docker برای ایجنت‌های کدنویسی
داکر سرویس Cloud Sandboxes رو منتشر کرده: محیط‌های اجرای امن و میزبانی‌شده روی زیرساخت خودش، با ایزوله‌سازی microVM توی سطح سخت‌افزار. با یه دستور میشه سندباکس رو بین لپ‌تاپ و سرور جابه‌جا کنیم طوری که فایل‌سیستمش هم منتقل بشه؛ یعنی کار رو محلی شروع کنیم و قبل از خاموش کردن لپ‌تاپ بسپاریمش به کلود. هدف، ایجنت‌هاییه که ساعت‌ها کار می‌کنن و می‌خوایم چندتاشون موازی پیش برن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5390" target="_blank">📅 22:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گوگل امروز صرفا ۶۰ تا اکانت مرتبط با صداوسیما رو به دلیل فعالیت‌های فیشینگ سیاسی و پنهان کردن هویت مسدود کرده</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5389" target="_blank">📅 16:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5388">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EV3COECMekWqjsFV7fmmykegTnLANrcpA1RIKfmpy_zknpBFRr9sDHB-8DYexDsPQMZQU__zS7GBic1TI15s7Vlt7FXpfbJJFSRX9AxxqPEnSulIOK-1jRXOEo01lmWJjkNpfbyZvvN5loPL4ChMuU5IKalH5uMFSACxZJOX5neQOdAsKgwIFBNf_3QN23cO-jHBWdkXdBbW4sbnFhyQbFrIKfqWgRdnS6IQhL1tDFznenME4U_qtshwFQIjb6zcB8iGt7iryT4ZJR4PjCt5qIH10nVXCVrB36zmcB2MKU-522kag5ex4gwpIUP5gaOrbu5bx0ieY2EsBAF_P5O_nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر بلاگش رو از WordPress کوچ داد به EmDash
کلودفلر جزئیات کوچ دادن بلاگ اصلی‌ش از WordPress به EmDash — سیستم مدیریت محتوای متن‌بازی که خودش داخلی ساخته — رو منتشر کرده. EmDash با TypeScript نوشته شده، روی Worker خود کلودفلر اجرا می‌شه و تا ۷۰۰۰ درخواست در ثانیه تست شده، در حالی که بلاگ معمولا ۷۵ درخواست در ثانیه داره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5388" target="_blank">📅 15:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5387">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kUsBrATmuhsnDikJvOyEfUu6De_TUDynRV-MuAAoqPcQK2GaFOh3unMmC89Ln6RrK1eHr0XOYE9be74pnhnySKT7MbPZPfM89HD-7wx-zwr_goRt4kJKfv4u-UeeE0ntMS3PrGLapOHP1DDfxeKGIFsa_q7Komp8I7a4xBXZScm14c-ck5q0Gm8yGHZgwaUZD77bHmFwdM4vF0CnNi_zQLmGLYxofHLA9mVKhnVC2DtdgVF4fAbxMWJIiABEeCO1esxpPlgLoX1Gd9YJODMgUMgI5IsmoIUvc9gpVu7wgHXs4KssADPbqAV-IQQpvKNwPt5lqIJkO-yu5wpl8GpFhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا حس می‌کنیم هر مدل جدیدی که میاد، انقدر از مدل‌های قدیمی قدرتمندتره؟
باید بگم که این بیشتر از منطقی بودن، «کلک» شرکت‌هاست برای مارکتینگ
اگه یادتون باشه، 2 هفته پیش همه‌ی این بنچمارک‌ها(خصوصا سه بعدی) جوری از GPT Astra تعریف می‌کردن و چیزای خفن می‌ساختن که انگار خدای همه‌ی مدل‌هاست.
بعد که Claude Opus 5.5 اومد، خروجی‌هاش رو جوری نشون دادن انگار اون مقابلش پیامبره.
حالا این قضیه برای هر دوی اونا در مورد Gemini 4 Pro داره تکرار می‌شه
به این کار اکانت‌های بنچمارک و Ai Enthusiast ، قضیه‌ی Strawman Fallacy می‌گن. یعنی مغالطه‌ی آدمکِ پوشالی
توی فلسفه، Strawman fallacy یعنی از رقیب قدرتمندت، یه فرض پوشالی بسازی جلوی مخاطب، شکستش بدی، و بعد خودت رو پیروز جلوه بدی
هم خود کمپانی‌ها، هزینه می‌کنن که اکانت‌های توییتری/ردیتی این کار رو انجام بدن؛ هم خود آدما خیلی وقتا این کارو سر هایپ و ... انجام می‌دن.
چه شکلی انجام می‌شه؟
1- مدل رقیب با پرامپت ساده یا بد تست می‌شه، ولی مدل خودشون با پرامپت بهینه‌شده.
2- قابلیت‌های رقیب مثل reasoning، ابزارها یا context بلند خاموش می‌شه.
3- هایپرپارامترهای رقیب به درستی تنظیم نمی‌شه ولی مال خودشون با دقت tune می‌شه.
این شکلیه که می‌گم هیچوقت به بنچمارک‌های این شکلی توییتری، نمی‌شه اعتماد کرد.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5387" target="_blank">📅 14:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkszzl0HrLnr1iByFWt3152Z9Ve-XFnqSQ3uAYNpTfZZgQEF3gBsr-xEqUiBpqX0mhb43PuUuM9bcPmIKAdI0EYilX3IcVfTuzhpMzO2VJlWpLvRaAZX0XHIJCIm5y_uzHMa_syFivgALSPYH83v37WAxDbtng0yT-mmPc_rrM-RhwZjy2ijd86nRBeZlBROUrt4s0Bvo7lC1yQ8xpPsOfM2AQJDft6upZO3kECRNqshViqMNssWnyp63AwqUQ-FpA55ANUj0y3OfFsDIBkz3VspuB3kzdKYl88HN6wJzPp455qDM-HnTTfTgelOE-gYsr9UpRMnChC0ptLX2u9pdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۶ هزار دیتابیس Supabase داده‌های مردم رو لو داده
پژوهش شرکت UpGuard نشون داده حدود ۱۶ هزار دیتابیس میزبانی‌شده روی Supabase بخشی از داده‌های شخصی‌شون رو عمومی کرده: اسم، آدرس، شماره تلفن و گاهی پسورد و توکن.
و بین اینها دیتابیس یه کنسولگری دولتی توی فرانسه هست، پلاک هزاران خودروی یه پارکینگ، و دیتابیسی که برای دریافت رمز یک‌بارمصرف کلاهبرداری استفاده می‌شده. Supabase که امسال به ارزش ۱۰ میلیارد دلار رسیده می‌گه پروژه‌ها پیش‌فرض امنن و امنیت یه مسئولیت مشترکه.
بخشی از ماجرا هم کدهای Vibe Code شده هستن که بدون پیکربندی درست، داده‌های کاربر رو  لو دادن(شبیه یه بنده خدایی که یه بار پروژه اوپن سورس گذاشته بود با به به و چه چه و بعد دیدیم apiهاش توی کد فلاترش هاردکد شده. (طرف مخالف سرسخت ai بود و میگفت به کد ai نمیشه اعتماد کرد)).
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5386" target="_blank">📅 11:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5385">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e71f3ca5cb.mp4?token=qt95u7mYANfssZ7Otx3mpoHjQiQJXNvFW5JGQuykwCxP4q7sTpX_hkux-6mF3cxIhTXG3HI3YMQCfbqBrM1u8zTmOuToRbSXEEyBuCTr-PeWatrEk5dJYJwE6qOpFexLrUj-0Gu3SGlOA5kxPHx7c7woDTjOEUW89bcgsWhsIB6nTQzSq976LujSR3B6OJq5UFc7PhQ4kQ9feMAbJP9wokuG98AZgFSNLzX7Wkpc682vn6-6C0FyVltYdqxSZCtj8koEYAiWxncWIpRvC_sC-GTGtQuVploZPkr4nFsPmw_OBIsLhcdopImCJAUKxmlEfz3-xLhnWYeArn5W10sT1Z7k_XIg9RlushNMg8njBZor_gMA_QhfBIJ1woMEi5WlXRyro24So5PxskxHZyf-Yb-LoDMkZxLn5_ZMrvXVprE7ZIQ9niv0U90zDKx8bbqw3baQ6qYP19wq_qSvmMVx5Y9hHRmXJ9Y5ECx04f3fPizkDUoFSv-ynVLICy7fkE-xRL76pFkQB7exQFiG4wAwEozgU7tXctZQe6gqF1yPkQfMJ04wwhhTQ8Oq4XVXQAxFHLW__toLvprk2wjkJPVW1x85w4FaVk2J1fGX8yF_i9OoHG7HMEVIn-HQPU9i7CRW-ZNb4-yZ0s6ODChWqUhTk7booa4XgQGS05-7jnxE9Gs" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e71f3ca5cb.mp4?token=qt95u7mYANfssZ7Otx3mpoHjQiQJXNvFW5JGQuykwCxP4q7sTpX_hkux-6mF3cxIhTXG3HI3YMQCfbqBrM1u8zTmOuToRbSXEEyBuCTr-PeWatrEk5dJYJwE6qOpFexLrUj-0Gu3SGlOA5kxPHx7c7woDTjOEUW89bcgsWhsIB6nTQzSq976LujSR3B6OJq5UFc7PhQ4kQ9feMAbJP9wokuG98AZgFSNLzX7Wkpc682vn6-6C0FyVltYdqxSZCtj8koEYAiWxncWIpRvC_sC-GTGtQuVploZPkr4nFsPmw_OBIsLhcdopImCJAUKxmlEfz3-xLhnWYeArn5W10sT1Z7k_XIg9RlushNMg8njBZor_gMA_QhfBIJ1woMEi5WlXRyro24So5PxskxHZyf-Yb-LoDMkZxLn5_ZMrvXVprE7ZIQ9niv0U90zDKx8bbqw3baQ6qYP19wq_qSvmMVx5Y9hHRmXJ9Y5ECx04f3fPizkDUoFSv-ynVLICy7fkE-xRL76pFkQB7exQFiG4wAwEozgU7tXctZQe6gqF1yPkQfMJ04wwhhTQ8Oq4XVXQAxFHLW__toLvprk2wjkJPVW1x85w4FaVk2J1fGX8yF_i9OoHG7HMEVIn-HQPU9i7CRW-ZNb4-yZ0s6ODChWqUhTk7booa4XgQGS05-7jnxE9Gs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">+ متأسفم اما AI هیچوقت نمی‌تونه همچین چیزی بسازه. - عاااااشقش شدممم. با کدوم ابزار ساختیش؟ + الکی گفتم. با Opus 5.5 ساختمش
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5385" target="_blank">📅 09:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nFPhlf536hfQgUFvlC4reP6RC0Ladv3AUk02SGscUfkzzh4hR-uxksV9vcZWYEmLWy9J6AdQ7DFGrZvcFrAP82AuIZw2qg8pLipgxKEvKdvU2mKghHgCKHg_R-zelV1NRO1H5R4WCMHjE-mWRzq8JS_61Vb7bvQasPXVo6QJ_AT7zRtdzg-KCZD6nH-hLpNNI9KhbxUz4Sd09JbGnGxeZCaur1Ib9AQCc8anfsgLJur2RimsWFz8PrHq4O6Uj8QgAf1GxL5qt1oziy4UeBgl3ik0w64j1QzhmpYPLwuWSmJ8ayb1-AB4MmxY8Jv6w9xOQJtZ5IrGQ4rQJDuKSPy1Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+ متأسفم اما AI هیچوقت نمی‌تونه همچین چیزی بسازه.
- عاااااشقش شدممم. با کدوم ابزار ساختیش؟
+ الکی گفتم. با Opus 5.5 ساختمش
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5384" target="_blank">📅 09:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBnwhx9CTHnDCQFBOPxKyo9vUXe6CRzAWKTv9ACYndUndGZklZ1WQrRyLSkL45EzVm9-cZ0Cw2kMvpGaE5lpQtn4E1RfqXUUQmqKo4_7VTb0pSSiMS9_Ik2On7-4vrvRVMoHOihv0_zNTHyGL8M7LI0yVQz6oCln44WBRESL3tBLWodYhU69OeckD-OYch-PB4Fpwh5Br-bdDEohUn8uVhcmFt5bAPka2dSrlDald-wbgQw9HC6N7S0VGc8kUVpjtiCqk_NXG04JS7DVahWrLFeEuTdQrWnLqf_NmEiFYx_2fszKSPQh1F6a8vCJBxk0UTYgb2RV29vcIxY3udVWmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولایا (Ollaya)؛ مثل Ollama ولی برای مدل‌های تصمیم‌گیری
خود Ollama، اپلیکیشنیه برای اجرای مدل‌های Open Weight روی سیستم خودتون. حالا Ollaya، همون Decision Models که Jev ساخته رو می‌خواد لوکال و متن‌باز اجرا کنه: سوال تایپ‌شده از هر متن یا JSON میدی و جواب کالیبره‌شده رو توی چند میلی‌ثانیه می‌گیری. جواب از یه پاس روبه‌جلو میاد، نه از تولید توکن‌به‌توکن: حدود ۸ تا ۱۰ میلی‌ثانیه برای ۵ تا سؤال روی RTX 4090، در برابر ۲۳۶ تا ۲۷۶ میلی‌ثانیه‌ی API عمومی Jev. با API سازگار با TypeSafe کار می‌کنه، پس SDK رسمیش بدون تغییر وصل می‌شه و مدل‌ها هم همونطور که گفتم، open-weight هستن.
اما یه بحثی که وجود داره، API خود Jev انقدر ارزونه که فعلا من با اینهمه کار باهاش 5 دلارمو هنوز تموم نکردم. لوکال اجرا کردن لایا هم خوبه اما شاید بهترین گزینه نباشه
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5383" target="_blank">📅 07:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5382">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pAVPLn_7cYWTrJ-7d4PfS7FI94_zcfwKC-YGp7F9t-6rmCYDJJD35Ot8Hi0D4sg4pwrYDhQqnM6p9s03eITCviO06UJ921q_JiEzQrmjf9k2qg61-BWzPWKc-8vNVRVQ4BsQQm6JFES8kfVAbmQ7u4Peq7hLBEXIzU5rXBjEz-IJpaD3dIM1CbirUeoRBtn6XcVJRecmx2m-XeY8EMiRKGd5dTHw9UvDawLEBocm77cvKfqfEDZxL_w8OA3Z-aalt86aDWiSDFOqDAB9iRXavb3cWd6GgjC3FcSbVYdT1mEM_F5wu1IYJoBaGp1fPueswEMBoQV89ZsZ-pQfL_11NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک هست دوستان.
گوگل یهو ایران رو تحریم نکرد. سالهاست ما تحریمیم
گوگل امروز صرفا ۶۰ تا اکانت مرتبط با صداوسیما رو به دلیل فعالیت‌های فیشینگ سیاسی و پنهان کردن هویت مسدود کرده
این خبر هم اشتباهه
می‌تونید ایمیل بسازید همین الان با گوشیتون و نگران نباشید</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/MatinSenPaii/5382" target="_blank">📅 00:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5381">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تانل با دو سه تا یوزر و سرور قوی هر 40 ثانیه یه بار ریست میشه
معلوم نیست دارن چیکار میکنن
کلودفلر هم اکثرا کار نمیکنه واسم آیپیا با نت همراه. فیبر وضعیتش بهتره</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5381" target="_blank">📅 00:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وضعیت اینترنت خیلی افتضاح شده
هم نت هم VPNهای تانل</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5380" target="_blank">📅 00:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjjfapcewmQeA2TfKAy87dZ1KJEFlmSezV1QabMn_F3cu07zePaWCwVUQbMgqN6CO_7nAoeaoi-HkM4kF7ohTEEvA0NZZmEDV4h9x3eZDnwcyA00FC7_8FRbgo9w-LzDnvs_0OhrvDUZ7BZvSqqIsYkmqEZ6acSuRN5DcOudJbHopXnVh01Ylktwzxel0ItvtZC5GktlGSR74HhOuus8uLpYL5qB7wMROTnuncY-l8kgSoNWWjRF9KD_1jyFfAELsjxaLxQ-QqPWQ2dZ6lLIXWXBOwnExA7a_7YpYz2QL9Jyc-jgP-6I7jkcZzCkH37wb6c9c5HdnC-xRl-GzzCXug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رابطی رو که توصیف می‌کنید، ایجنت براتون می‌سازتش
گیت‌هاب توی اپ Copilot یه قابلیت به اسم canvases گذاشته: به زبان ساده توصیف می‌کنی چه رابطی می‌خوای و ایجنت یه سطح زنده برات می‌سازه که هم خودت می‌تونی استفاده‌اش کنی و آپدیتش کنی، هم خود ایجنت. هدفش اینه که وقت کمتری رو صرف تطبیق‌دادن با ابزارها بکنی و بیشتر کارت رو پیش ببری.
این کارا فایده نداره گیتهاب جان. پلن‌هات گرون و به درد نخورن
برو این دام بر مرغی دگر نِه
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5379" target="_blank">📅 00:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5378">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AXw18fMFxAx6K5gwM-sDsxv-H1_ha_WkR6d8mLc3A38S-n_UBNTEPKQI86F34TsWTMZYBK8lARhGMybTyeS1Siu-LlxNukMzm_PFR8wqWaajRy4IcONXmgna-Wy-3xj5RwpYbB9Qqd1_k82GlbP-mC4OClp9_Jl1tDanHLu5ajrVLY0lPMBzCiVpbE_jgvJZdeJshGOwYwhVI9y-AAbfX-KCLls53q2ueeFqMYGkwIm-XOW5zJZESIjo_2K8QDeLtDOGAsTpcVQL7cuLtHSaQGp-UZxiY8M7XXfj0hEPGXWFT-2lMZ0J1-4R5msTDoJVyGdTaVJRP2bl_LkRv5-fMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">(باید برم ببینم کپچا فارمش چطوری کار میکنه)</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5378" target="_blank">📅 23:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5377">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XkYcpB0U-cs7SXmTfQJG_fnEIgLQqfik3VkS7laGfoV_hbG9qfdomfeBCw6Edv6X8_sZmkh9FISSVp6KfCBRqfqvUImkIbv8FdwspHlFZjLuo_EW5rFEFsrDmMBdrXPZ2O-sNqMvtSxlCHemNl40YAYyR7pgd7BCeNgN5EABwI5z-mmex_GrBVQGar8dPZI-DHq9Hcn1Vw2Qtiov1tu1Z15oADzaol_j-t5KfZlhf4djqFoBXFMYNkS3CD_1_VDiO8kNP5B3_3_ArxPnup34JYGQ3RWbbTtwec8UB3mftC9oR8-DJE6dXa9cdIMMVCMhwTNpUPeEKT70_42te8cPJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر سایتی رو برای ایجنت‌ها به API تبدیل کن، بدون Browser Automation
💪
یکی از توسعه‌دهنده‌ها توی ساب ردیت هرمس ابزاری به اسم
agent-data.dev
معرفی کرده که ایده‌ی جالبی پشتشه.
حرف اصلیش اینه که برای خیلی از کارهای تکراری وب، مثل چک کردن قیمت پرواز هر روز صبح، دنبال کردن آگهی‌های شغلی جدید یا سرچ توی یوتیوب، browser automation رابط مناسبی نیست. ایجنت باید سایت رو باز کنه، بفهمه چی روی صفحه‌ست، هی کلیک و اسکرول و اسکرین‌شات بگیره، و هر بار که لازم شد کل این چرخه رو از اول تکرار کنه. وقتی کار در اصل «این سایت رو با این پارامترها سرچ کن و نتیجه رو بده» هست، خیلی منطقی‌تره ایجنت یه API call بزنه و JSON ساختاریافته بگیره.
حالا این agent-data چیکار می‌کنه؟
1- یه کاتالوگ از APIهای آماده برای سایت‌هایی مثل X، Reddit، Zillow و کلی سایت دیگه داره
2- اگه API مورد نظرت نبود، URL رو می‌دی و توضیح می‌دی چه دیتا یا عملیاتی می‌خوای؛ خودش API رو می‌سازه و نگهداری می‌کنه
3- از طریق HTTP، MCP یا CLI قابل استفاده‌ست، پس برای ایجنت شبیه یه tool call معمولی می‌شه
نکات فنی:
😟
به‌جای HTML selector، endpointها رو روی همون network requestهایی می‌سازه که خود سایت برای لود دیتا استفاده می‌کنه؛ برای همین با تغییر layout کمتر می‌شکنه
📱
خود APIها مرتب تست می‌شن و خرابی‌ها خودکار شناسایی و برای تعمیر صف می‌شن
💰
زیرساخت proxy و CAPTCHA رو خودش هندل می‌کنه(باید برم ببینم کپچا فارمش چطوری کار میکنه)
سازنده‌ش گفته قراره نشون بده این روش در مقایسه با browser automation چقدر سریع‌تر، قابل‌اعتمادتر و از نظر مصرف توکن بهینه‌تره.
🔗
وبسایتش:
agent-data.dev
📌
ردیت
اصلی پست
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5377" target="_blank">📅 22:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5376">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">این ویدیوی موشن‌گرافیک رو با مدل Opus 5.5 برای یکی از دوستان ساختم. و باید بگم با ۲ خط پرامپت و یه ویدیوی مرجع برای گرفتن اطلاعات و متن ویدیو عالی عمل کرد. عالی  حدود ۴۰ دقیقه زمان برد و دقیق ۲ خط پرامپت با چندتا فایل فونت.
✍️
Saeiid</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/5376" target="_blank">📅 21:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5375">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a18edb9ea.mp4?token=UDmli2rCStJuka1fM3nr13CZE-8sdK9eiR8ZWZcjWWR_pcF1J6obGOds9hKo1ISssqA_uP8ehdznzS4fxda7AkEYGOQ-gGeGA6E6RyHfGOFxT4uxwOzJnatDG0iw7vtuqXt1u-vuWKzKUJ7ZJs9doNnL1-Uy3F4GU6V4jtzud6uvIuTmKcQ2or1JUzGStvtqWv4oQwiB4p4ZCW4ASFtLyZFQHDYOaBdjw4Y02A3NdpecUA5yboaaNuFqmjEth5USqbzM3ShiGJ2y_PhWxYU1j3uKTIWps1tQ8nEXl_UHD1aWl3PuarTvPaZmcXZgpZhhRd5pxwnGTacpWbkmHhlP9w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a18edb9ea.mp4?token=UDmli2rCStJuka1fM3nr13CZE-8sdK9eiR8ZWZcjWWR_pcF1J6obGOds9hKo1ISssqA_uP8ehdznzS4fxda7AkEYGOQ-gGeGA6E6RyHfGOFxT4uxwOzJnatDG0iw7vtuqXt1u-vuWKzKUJ7ZJs9doNnL1-Uy3F4GU6V4jtzud6uvIuTmKcQ2or1JUzGStvtqWv4oQwiB4p4ZCW4ASFtLyZFQHDYOaBdjw4Y02A3NdpecUA5yboaaNuFqmjEth5USqbzM3ShiGJ2y_PhWxYU1j3uKTIWps1tQ8nEXl_UHD1aWl3PuarTvPaZmcXZgpZhhRd5pxwnGTacpWbkmHhlP9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5375" target="_blank">📅 20:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5371">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/patOCTR0HFconjktv_KWMEuvlZ6hMyLa9GAeMxF5goe3y2gRhNJz2wODS6Bg5BQZ1qHPt2ju5b6SmYvY4sA5CkxX5wdhY0ionV6sXthXuggwRQO1Os-xpUqqQz3d-ds0JZ3-rKoTis7pxG-beD2ryTYF1Twfs74UOnOnJvgpweL7HScyop5JRJFgAHtvva70IiYeNQ5GAcE5C7ORgQ_tUxfOlB1aFUKgYS8kQJsFC3j5kOXEyG6PpODyLeMVkmEKSISltw6Uv6NAgYfRKuZXtWyMZeQYqSBsWSsPe_s6mFxQe_kKhBlwQdxMmfOUT8NA-cOThcyygrEopQfAqdsfTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BhMR_1jdsOTYnKcEhIyyTugUUxzYSdeWB1Kcl_gcriLRgbuEEzu2Qd3wGYXMo82gtQ2j02cy0fQLfxcoZRov0DDf5BDM4s_gNbgo_pGajdrDl5BPUZV3IKW1dhcx_-GI6SJWDieKByHxliMzlBNEFYkotyLzwxWR8dnG87BuYJcwc72Ez1WrI8Sq37KxYFjLp0rBpRm-lEGEVeBAHUyA9M6wlQ91HpwcT7Ogm1cqD4V9g09LcsrQV3G_OKhzG3nEEDcXZmRknNSHa2WAjRqyAXKYxQQkG6bBUsJ9APUUBtem_TpLXpzOT2pN4OQqKY6Czj5XmjL2AhV2-oAMOj_HWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W3htc6n3tYPMfhRjkSFooglPvcJRvqbCxvp0V7wGc-VXgxxj7pscS5utzoxLDOAyKeVLcMnOTvVMLNZ6CVkqn-66KhiQJK9V8qufxctsC1X4H2hT9l-vTcvEGEzqAjBKBow03Kssk9Wn1umaAS2zG9gku-B7Ma3GVseB1EfH_Eed1g1MTXTTu-hSg7uYkgKk-XynEsxajgpzMoIXkr43V4f3bbKxAaaMjNM6QT_VNQAhTBjRvbPn0CjLHW8FN2IayqTbM8rGQ2eef-1kYAqgZmEq1iz_Xu6ToZ9J7WYJuKQEuZS4qCgnD-R4YTLYh2MMH_t5MX63BPcpuidExxJOVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HYmsxHYiltbJaqfilKFUbyWCUwP3nYOKjZ4zNgVUygRpr4Rp9YsQpADedvgvMVTHgGNwtBvXnYfBDcDBFIQo0Akq3F9_oni-ZHHvvlJR4grRntZaPRWj7WniMf1XSdLbCx7U0gcggjvK6AJN2hbLJNasuLxuvbgku1MP0WTko0g_4HllxtqnIl4lFRTrZtB-hob_TN8b_SJo1If8Q_WY_3ZDztHPFUoEdomA2vIkdgEbV9W-fG_lSN1jqC1B-Y-KXZaqlvIcm9Ays2m-fGWYcbqvajAVDGPwN0f_XG0uatoOUltLuNpIVoPUgJBZaIQ4b7BpHT_G2OjOdCYsqlWEow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اروین از توییتر
یه سایت بهم معرفی کرد شبیه به Mpay، اما بیشتر برای بیزنس‌ها یا کسایی که تراکنش نسبتا بالا دارن؛ با قابلیت برداشت مستقیم از کارت و کارت‌های تبلیغاتی برای کارهای حساس مثل تبلیغات گوگل ادز یا تراکنش‌های سنگین و گرون
از اینجا می‌تونید ثبت نام کنید:
https://finup.io/?code=MATINSENPAI
لینک، رفرال هست. اگر دوست نداشتید میتونید کد آخرش رو پاک کنید. برای شما سود یا ضرری نداره
نقاط قوت:
1- برای ساخت کارت، MasterCard داره به جای Visa(شانس قبول شدن آفرهای رایگان معمولا بیشتره)
2- قابلیت برداشت ازش وجود داره به ولت کریپتو(هنوز تست نکردم که KYC می‌خواد یا نه اما توی مستنداتش چیزی ننوشته بود که احراز می‌خواد یا...)
3- آدرس BIN آمریکا داره
4- از ارزهای مختلف برای واریز پشتیبانی میکنه برخلاف mpay که فقط تتر داشت
5- دو نوع کارت بیزنس و تبلیغاتی(هزینه‌شون یکیه) که کارت Advertising شانس پذیرش بالایی برای کارهایی مثل تبلیغات Adsense گوگل و تیک‌تاک و متا و... داره
6- کارمزد رایگان روی برداشت و تراکنش کارت‌ها
نقاط ضعف:
1- هزینه اولیه ساخت کارت 10 دلار هستش
2- برای KYC شرایط ثابتی نداره اما توی تراست‌پایلت نمره‌ی خوبی داره
3- حداقل هزینه واریز به خود کارت(نه ولت)، 50 دلاره
و اروین گفتش زمان واریز مراقب باشید از صرافی‌هایی که امریکا تحریم کرده نزنید. ترجیحا بریزید توی تراست ولتی، جایی و بعد بزنید به ولت این سایت
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5371" target="_blank">📅 19:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5370">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d63885ad.mp4?token=Ix6Sox6_GvBQk_yiMMCQsDB7HKC171xcLBmfwhwzcZwnYfdZWkGXJbGnzDqQvYn6KxcLpAydEWGdKwm1u0l8SMdMk4571zL5lGgtD4AdG-qCnXlm2rnaVcHPpy2-iYcYhm6mgFuimj5we-3wJ6ugz8txj04P2BuAUm5DluMUf5l6n-3rT9dqdNuS2jF-x8mW_qaHo1e-KDon1gtR3tXDIW4OpZnW5XbvfIVWVWjfC61-LcNnuXThBC1bE8q2dY-3NP3zz7_ijZxJoI5AAA77fjWxyZBh4sqIfC3oQKIed_NbHhBDHvjhlXVD3YJCj4N0D6shEhqOOixX3a0QuNPPWR3sUH7BSEVWKMm3UUXPBg9FdUHCSF2gMhtx5YS4ujMLkgLoMtEe-ry8jjK0kC0jLb8hcZ_TmDcupjIzjl6VjqiYEoR3zMZ9FNeiKswJEEIJoA195B-FoF9RCdkY4HMe_IA5tsl---FAvEkqHpYX-jNcephx74yKj7M5WGcT8uaVUHHtKPKP0ZEKLwNZ3pPzG0wwtDrQEt2QqVZ3TNqtOkNUlf8m98DIncNLxLM0z0kGatVolgaAJ1_pUX6sPBoNqGbAm7Cbdvzsmi-NYg8mUZmUSKJix71oOg4zo2c5YqPlLxzjmgXsrNDJ_TYWuLRRfF-sbdFrZikBC_iTRFd5CYE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d63885ad.mp4?token=Ix6Sox6_GvBQk_yiMMCQsDB7HKC171xcLBmfwhwzcZwnYfdZWkGXJbGnzDqQvYn6KxcLpAydEWGdKwm1u0l8SMdMk4571zL5lGgtD4AdG-qCnXlm2rnaVcHPpy2-iYcYhm6mgFuimj5we-3wJ6ugz8txj04P2BuAUm5DluMUf5l6n-3rT9dqdNuS2jF-x8mW_qaHo1e-KDon1gtR3tXDIW4OpZnW5XbvfIVWVWjfC61-LcNnuXThBC1bE8q2dY-3NP3zz7_ijZxJoI5AAA77fjWxyZBh4sqIfC3oQKIed_NbHhBDHvjhlXVD3YJCj4N0D6shEhqOOixX3a0QuNPPWR3sUH7BSEVWKMm3UUXPBg9FdUHCSF2gMhtx5YS4ujMLkgLoMtEe-ry8jjK0kC0jLb8hcZ_TmDcupjIzjl6VjqiYEoR3zMZ9FNeiKswJEEIJoA195B-FoF9RCdkY4HMe_IA5tsl---FAvEkqHpYX-jNcephx74yKj7M5WGcT8uaVUHHtKPKP0ZEKLwNZ3pPzG0wwtDrQEt2QqVZ3TNqtOkNUlf8m98DIncNLxLM0z0kGatVolgaAJ1_pUX6sPBoNqGbAm7Cbdvzsmi-NYg8mUZmUSKJix71oOg4zo2c5YqPlLxzjmgXsrNDJ_TYWuLRRfF-sbdFrZikBC_iTRFd5CYE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم یه ویدئوی جدید از مقایسه‌ی این مدلی که فکر می‌کنن Gemini 4 هست با GPT 5.6 Astra توی یه انیمیشن ساده(هرچند بنچمارک‌های این شکلی اعتباری بهشون نیست کلا ولی خیلی وقتا درست از آب در اومده این مقایسه‌ها توی قدرت دیزاین و درک سه بعدی)</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/5370" target="_blank">📅 18:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5367">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ad410f0702.mp4?token=p64pvVN1iKb8bMl4YGQb5MW9OERKdhCV1d-o1gPAKfBG7C5jruz-Lo4inOooNae-CdPYmfDdl8DBpiBM9N5DkLIdnUj7UJQkeVHr03VfwaFXjmeyyJAlf7cYhDkO1ts_s9m_jgFKbcF2G3fKpYf-hb52_NE_wHmZmBcoOSGkYaym4GxAzQ1nVnCpyHrwd2qpKKbD-FIE8kipCctciM9N1g22VIKJ0xI0GhdgtyCmwZ5n90wE0b5WRIG5BiFeaTli9cDK7aJFPXlcyzZMefW56aAsE9UG3i5QLrqR5MqiBEaOaBvgZZjqWBQxS4fIB56UIWOoO3MJU0NDWEGML2fiVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ad410f0702.mp4?token=p64pvVN1iKb8bMl4YGQb5MW9OERKdhCV1d-o1gPAKfBG7C5jruz-Lo4inOooNae-CdPYmfDdl8DBpiBM9N5DkLIdnUj7UJQkeVHr03VfwaFXjmeyyJAlf7cYhDkO1ts_s9m_jgFKbcF2G3fKpYf-hb52_NE_wHmZmBcoOSGkYaym4GxAzQ1nVnCpyHrwd2qpKKbD-FIE8kipCctciM9N1g22VIKJ0xI0GhdgtyCmwZ5n90wE0b5WRIG5BiFeaTli9cDK7aJFPXlcyzZMefW56aAsE9UG3i5QLrqR5MqiBEaOaBvgZZjqWBQxS4fIB56UIWOoO3MJU0NDWEGML2fiVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب، انگار توی Arena همه جا دارن تست‌های این مدل اخیر رو به جمنای 4 پرو ربط می‌دن و شایعه شده از Opus 5.5 هم بهتره</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/5367" target="_blank">📅 18:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5366">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خب، انگار توی Arena همه جا دارن تست‌های این مدل اخیر رو به جمنای 4 پرو ربط می‌دن و شایعه شده از Opus 5.5 هم بهتره</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/5366" target="_blank">📅 17:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5365">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تیم Tokio نسخه‌ی ۰.۹ فریم‌ورک Topcoat (یه فریم‌ورک فول استک برای Rust) رو منتشر کرده که می‌خواد ساختن اپ وب با Rust رو به اندازه‌ی Ruby on Rails راحت کنه.
توی این نسخه ری‌اکتیوی سمت کلاینت جدی‌تر شده: توی macro مربوط به view سیگنال‌ها و عبارت‌های تایپ‌چک‌شده می‌نویسید که به جاوااسکریپت ترنسپایل می‌شن و توی مرورگر اجرا می‌شن، ولی بقیه‌ی رندر و منطق می‌مونه سمت سرور. نکته‌ی جالب‌تر اینکه نویسنده میگه راست بهترین زبان general-purpose برای دنیای توسعه‌ی مبتنی بر AI هست، چون قراردادهای مشخص به مدل کمک می‌کنه با توکن و خطای کمتری کار کنه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5365" target="_blank">📅 17:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5364">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XDj2E5a3q1wLK9SWopkeT23JRI777kq1tRU4PCOWDdaX6oeGQ9jWEgH6wmeFFSQFzewoXLp0wUspaICxMN3TLkCgehSiyJ51FN_rQgKCc6cmQjWs3k3bdWqFPgGuO6BlZcOGtNXHFKIYBeWhJdeb6cZl66qkHUM4BD9PVb90k54FJdb_PGOIN9_qFAbTChX9NS32ERO7vTRWc7D4wu-dF-knyDB5X8FS9HZRD8xxTkb7iELOSRwbCWghucUya6m-Zk8a55Lnne8oYHgkmjDKx1AtENLYxGGxI7wToFXHZ6StvvupYocGSd0IKpYSA1VlRO_g1ZF8FJDyavj6J3f5Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با توجه به علاقه گوگل به اسم قناری، خیلی طول کشیدنِ Gemini 4 pro، و چیزای دیگه حدسم اینه که ممکنه گوگل پشتش باشه
کاربرا فعلا گزارش دادن که به شدت کنده...</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5364" target="_blank">📅 13:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5363">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qXw0RdhoiFAQrA3oZZLbwEIox5pIpCYffngqV8avFK-Z3Md2Fve_vtkrbH6IbMXSqQ3-H_N6gJNRw7qLWwSUNuv71ZzSa5as5hrIe5ABwKGOWV4APyyaisVvo6bD_32HepHpQA8hNUgfLliUNtzbCmnsHc4UNeC-oTHMTCn-dKjmPE_ZO_WKY0-wYRwdNBIZRbCsest6Zb7twlaxg13S7wVJFYJcrZVJdmcmnbXIYGmcAmuHc9fqkZhDeHZ2AulMdDX1QnYJuObs6jUR7e2Y11FBplBkXCo-qrZE_YchHipWoQND69LuyKxeeIq5c45zpYQb46gQqJP8TEq1t23zXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Gemini 3.8 Flash روی Cline رایگان شده آموزش استفاده ازش: https://t.me/MatinSenPaii/5099</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/5363" target="_blank">📅 13:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5362">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">زبان‌های برنامه‌نویسی توی عصر AI چی می‌شن و چه بلایی سرشون میاد؟
خوزه والیم، خالق زبان زیبای Elixir، یه مقاله‌ی فکری نوشته درباره‌ی اینکه وقتی ایجنت‌ها بیشتر کد رو می‌نویسن، سر زبان‌ها، ابزارها و کامیونیتی‌هاشون چی میاد.
چند تا نکته‌ی خلاصه از صحبت‌هاش:
۱-
کامیونیتی:
هر زبانی دور یه سری سلیقه‌ی مشترک شکل گرفته؛ پایتون «یه راه واضح برای هر کار»، روبی «خوشحالی برنامه‌نویس»، لیسپ «تغییر خود زبان». وقتی دیگه خودمون کد نمی‌نویسیم، حس تعلق به این کامیونیتی‌ها چی می‌شه؟
۲-
اکوسیستم:
فاصله‌ی اکوسیستم‌ها کم می‌شه، چون پورت کردن کتابخونه‌ها یا پیاده‌سازی الگوریتم‌های یه مقاله با ایجنت خیلی ارزون‌تر شده و زبان‌های کوچیک‌تر سریع‌تر به بزرگ‌ترها می‌رسن. ولی از اون طرف، وقتی ساختن یه کتابخونه ارزون باشه، چرا کسی بیاد روی یه کتابخونه‌ی مشترک همکاری کنه؟ خودش به ایجنت می‌گه دقیقاً همونی که لازم داره رو بسازه.
۳-
سینتکس:
سینتکس‌های خوشگل (مثل optional chaining به‌جای چند تا null check) دیگه اولویت نیست، چون ایجنت از boilerplate خسته نمی‌شه و از دیدش همه‌چیز توکن ورودی و توکن خروجیه. به نظرش زبانی که ادعا کنه «برای ایجنت‌ها ساخته شده» و تمرکزش روی سینتکس باشه، داره حول محدودیت‌های امروز مدل‌ها طراحی می‌شه.
۴-
کامپایلرها از بین نمی‌رن:
اینکه ایجنت مستقیم اسمبلی بنویسه منطقی نیست؛ کسی نمی‌خواد برای هر معماری یه نسخه‌ی جدا نگه داره. تازه هیچ زبونی توی همه‌چیز خوب نیست؛ Rust، زبان‌های اثبات قضیه مثل Lean، Erlang/Elixir برای سیستم‌های توزیع‌شده، SQL، هر کدوم تضمین‌ها و سطح انتزاع خودشون رو دارن.
۵-
تضمین‌های قوی‌تر:
اگه ایجنت کد می‌نویسه، می‌شه trade-offهای زبان رو بازنگری کرد. مثلاً type inference برای آدم‌ها خوبه چون نوشتن تایپ حوصله‌سربره، ولی ایجنت حوصله‌اش سر نمی‌ره. نوشتن صریح تایپ‌ها اطلاعات بیشتری به کامپایلر می‌ده و دست زبان رو برای تایپ‌سیستم قوی‌تر باز می‌ذاره. به نظرش زبان‌ها در آینده با این متمایز می‌شن که چقدر تضمین می‌دن: از طراحی‌ای که حالت نامعتبر رو غیرممکن کنه، تا تایپ و اثبات، تضمین‌های runtime، و تست و fuzzing.
۶-
دیتابیس برنامه به‌جای LSP:
پروتکل LSP برای IDE و آدم‌ها طراحی شده و با فایل و خط و ستون کار می‌کنه، که ایجنت‌ها دقیق دنبالش نمی‌کنن. پیشنهادش اینه که اطلاعاتی مثل سیمبل‌ها، رفرنس‌ها و call graph به شکل یه دیتابیس با زبان کوئری در دسترس باشه. آدم حال نداره برای پیدا کردن رفرنس یه تابع کوئری بنویسه، ولی ایجنت راحت می‌نویسه، حتی کوئری‌هایی مثل «همه‌ی مسیرهایی که یه مقدار می‌تونه nil بشه». برای همین هم جادوهایی مثل monkey-patching که کد رو غیرمحلی می‌کنن، بیشتر مشکل‌ساز می‌شن.
۷- در نهایت
Observability به‌جای دیباگر:
breakpoint گذاشتن و خط‌به‌خط جلو رفتن کار آدمه. ایجنت می‌تونه سریع کد رو instrument کنه، trace جمع کنه و اطلاعات رو کنار هم بذاره. پس باید runtime و state سیستم رو جوری در اختیارش بذاریم که بتونه برنامه‌نویسانه کوئری بزنه، حتی روی پروداکشن. اینجا هم طبیعتاً یه اشاره به Erlang VM می‌کنه که این قابلیت‌ها رو از اول داشته.
جمع‌بندی خودش: زبان‌ها قرار نیست از بین برن، ولی سؤال اصلی عوض می‌شه. اگه دیگه برای «آدمی که کد می‌نویسه» بهینه‌شون نکنیم، برای چی بهینه‌شون کنیم؟
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/5362" target="_blank">📅 12:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5361">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">AI
فقط یه ابزار نیست
نویسنده‌ی brettcodes از این جمله‌ی تکراری خسته شده که «AI فقط یه ابزاره، مهم نحوه‌ی استفاده‌شه».
استدلالش هم ساده‌ست: ابزار یعنی دریل‌برقی که کسی ادعا نمی‌کنه ده درصد شانس نابودی بشر داره و اگه برعکس بچرخه خرابه.
اما AI یه صنعته، یه محصول اشتراکیه که قیمتش بالا می‌ره و مدلش بازنشسته می‌شه، رهبرهاش مدام حرف‌های عجیب می‌زنن و پشتش مراکز داده و منابع عظیمه. به گفته‌ی اون، تکرار این شعار فقط داره مسئولیت استفاده از یه فناوری خطرناک رو از بین می‌بره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/5361" target="_blank">📅 10:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5360">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTRahYK9kofiz5a7LsT78vMvc4nGwuMnWrH3m-iPOXk4VJyVk5eos60Id-fDeBYx23SAsDcY0NSGUZC-A2Tkr3wr93Osx5rzZoJza3ciiFTDKahqnLBdaqxDWcGKAzhuUnEtBtsZkOVf3VRDI1-GDKdKs53LpIdYfrIjb19o_BxOKjdRFcneHu86taVYa8nZCG8apAQ4Lry7HtPRPPlt9JIsPmdN8iQWzIsC6KQ_mQHWZ4C5xQcUOUJO5UHbMO-7RQPxA_Kg-b3lFvEvxaHEj4WtBJptzpie7EpRsFBRvxBsLtJs2gDUlT4J310vcSRrJ7wZnXxiULENNo3Rh2PpZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر وارد بازی میشه تا ایجنت‌ها امنیت سایت‌ها رو به درستی تأمین کنن
مشکلی که کلودفلر دیده اینه: خیلی‌ها ویجت Turnstile رو نصب می‌کنن ولی اعتبارسنجیِ سمت سرور رو جا می‌اندازن و عملا سایتشون برای بات‌ها باز می‌مونه. Turnstile Spin یه جریان کامله که به ایجنتِ کدنویسیِ شما اجازه میده هر دو طرف ماجرا (ویجت و فراخوانی Siteverify) رو پیدا کنه، برنامه‌ش رو بده، منتظر تأییدتون بمونه و بعد انجامشون بده. از داشبورد، Wrangler یا یه URL مهارت شروع می‌شه و اتصال‌های ناقص قبلی رو هم تعمیر می‌کنه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5360" target="_blank">📅 07:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5359">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5359" target="_blank">📅 23:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5358">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">واوووو چه باحال
😲</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5358" target="_blank">📅 22:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5357">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5357" target="_blank">📅 22:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5356">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اینم موشن گرافیکی که Claude Opus 5.5 ساخت توی 18 دقیقه هیچ ابزار خاصی هم نصب نبود جز ffmpeg و اینم پرامپتش: make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.…</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5356" target="_blank">📅 22:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5355">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اینم موشن گرافیکی که Claude Opus 5.5 ساخت
توی 18 دقیقه
هیچ ابزار خاصی هم نصب نبود جز ffmpeg
و اینم پرامپتش:
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.
که یه کم بالاتر داده بودم.
روشی هم که ساختتش اینه:
۱. هر فریم فقط تابعی از زمانه
کل ویدیو یک فایل HTML به اسم showreel.html هست که یک تابع renderFrame(t) داره. این تابع زمان رو به ثانیه می‌گیره و همون لحظه رو می‌کشه. هیچ حالتی بین فریم‌ها ذخیره نمیشه و حتی موقعیت ذرات هم مستقیم با فرمول از t حساب میشه. به خاطر همین میشه هر فریمی رو با هر ترتیبی دقیق رندر کرد. تیکهٔ «Rewind» هم ساده بود: فقط renderFrame رو با زمان‌های قبلی صدا زدم.
۲. حرکت‌ها از چند اصل کلاسیک انیمیشن میان
- Easing: فرمول‌هایی مثل outExpo برای ورود تند، outBack برای کمی رد شدن از مقصد و outElastic برای حالت فنری.
- Squash & stretch: نقطه موقع افتادن کشیده میشه و وقتی به زمین می‌خوره پهن میشه.
- Anticipation: قبل از جمع شدن شکل، اول یک لحظه بزرگ‌تر میشه (inBack).
- Stagger: حروف و ذرات هرکدوم با کمی تأخیر نسبت به قبلی حرکت می‌کنن.
- Motion blur ارزون: به جای نقطه، برای هر ذره یک خط از موقعیتش در t - 0.02 تا t کشیدم.
۳. تکنیک هر صحنه
- ذرات: کلمهٔ «FLOW» رو روی یک canvas مخفی نوشتم، پیکسل‌هاش رو نمونه‌برداری کردم و هر پیکسل مقصد یک ذره شد.
- سه‌بعدی: بدون هیچ کتابخونه‌ای. چرخش و projection پرسپکتیو رو خودم با فرمول ریاضی نوشتم.
- مایع: با metaball ساخته شده و داخل یک WebGL shader اجرا میشه. هر حباب یک میدان r²/d² داره و جایی که مجموع میدان‌ها از ۱ بیشتر بشه، سطح مایعه. نورپردازی براقش از روی گرادیان همین میدان حساب میشه.
- جلوه‌های نهایی: یک shader دیگه chromatic aberration، grain فیلم، vignette و فلش رو روی تصویر اضافه می‌کنه. شدتشون به ضرب‌آهنگ‌ها وصله.
۴. صدا هم کامل با ریاضی ساخته شده (audio.mjs)
هیچ فایل صوتی آماده‌ای استفاده نشد:
- Kick: یک موج سینوسی که فرکانسش سریع پایین میاد.
- Clap و hi-hat: نویز سفید که فیلتر شده.
- Reverb: با چند delay که بازخورد دارن ساخته شده.
- Sidechain: صدای بیس موقع هر kick کم میشه تا ضربه‌ها گم نشن.
- زمان‌بندی صدا با تصویر یکیه (۱۲۰ BPM، هر بیت نیم ثانیه)، برای همین همه‌چیز روی ضرب می‌شینه.
۵. رندر نهایی (render.mjs)
اسکریپت Chrome رو بدون پنجره (headless) باز می‌کنه و برای ۹۰۰ فریم (۱۵ ثانیه × ۶۰ فریم) renderFrame رو صدا می‌زنه. هر فریم به صورت PNG مستقیم به ffmpeg فرستاده میشه و ffmpeg اون‌ها رو با صدا به MP4 تبدیل می‌کنه.
۶. کنترل کیفیت
وسط کار فریم‌هایی از هر صحنه رو رندر کردم و کنار هم گذاشتم تا ببینم. صحنهٔ سه‌بعدی زیادی کشیده و شلوغ شده بود، برای همین طول ردّ حرکت و زمان‌بندی تبدیل شکل‌ها رو کم کردم تا واضح بشن.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5355" target="_blank">📅 21:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5354">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.  به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé.…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5354" target="_blank">📅 20:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5353">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iGSVHPsnrPKizuB4pvCU_orYPOs6uX6uiRYluw3460dkSohrjIJZvfWp3NRyr3MX1xnLAtlLWoXk13sUaiDs_0FKCy4QL0_XA_Prk6vw9YwGWJFytVJpdRTPB3eVCAYRmKBwGbIX__tRQjhaOEgD33GRt1p7dDM6SCDZTQFxIc_76XUMPOEXgBGTR2EsA4Sf3Hb_OKJL0d1GVA-CKoGNmAp7HSGdCnj_0naIpzc9kzUjbcQNq0Ug_ERprr-AqpDU-xCerwb1UCy_CrkW43evFg5zUQEQkm_ypGA7KHg2WpKfW7nVvHdnizdXQheaDErKFbu6Uqs3B9mY6b5-dlbZ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب خب خب
کارهای جالبی قراره اینجا انجام بدیم:)
matinsenpai.com
فعلا لندینگه. به زودی لانچ می‌شه</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5353" target="_blank">📅 20:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5352">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.  به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé.…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5352" target="_blank">📅 19:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5351">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.
به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out."
آسترا حتی نزدیک هم نیست؛ خودتون ببینید. GPT اینجا صادقانه بخوام بگم، فاجعه‌ست، OpenAI کلا بدسلیقه‌ست.
✍️
shneural
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5351" target="_blank">📅 16:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5350">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mg1-GPVvPBnWt7ebY08AMwz7UhM0MmzxIvkIaUJH9kb_iIqHMzrzpqECQm1eAZWyheEJz9mJl60SDDgAB1Vw1YSkREDdx8zzcOLwc_qNW-PnFRUhXanBPAYIp6TKosyB7-PD77M_5-MKmnkRb-Gw1bNGIYpUJSNatrqSrYu79sg6X0ZijGcHU_RV_76qJndC-QGD7CEJoTFFhT-Y0dRf8m4MK-oYOZaj7enhQ2ZyMIcCDZGMZq0n-v0WajtYyMb2FjHikIVPtuj6JfnFxT99ToRaeirfNlF8por2-Uu-FNrRSqFEZVxsoe5EckrAJeDabfWSpH-nCBsxGyZAzT4xPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازبینی کد با Jev؛ Diff خام دیگه در کار نیست
یه ابزار متن‌باز که پی‌آرهای پرحجم ایجنت‌ها رو به جای نمایش خام دیف بر اساس اولویت دسته‌بندی می‌کنه: فقط تغییرهای P0 پیش‌فرض نشون داده می‌شه و بقیه P1 و P2 هستن. توضیح تغییرها به زبان طبیعی نوشته می‌شه، لوکال اجرا می‌شه و چیزی هم به گیت‌هاب نمی‌فرسته.
🔗
لینک ابزار
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5350" target="_blank">📅 15:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5349">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NE2oGtshOT3XNt0rkkMj30o8OEP6i8RHfMUabKOjobNYlsV9Ivtz6ko650iHWWh-7H2ARMrEY9RecLcQ2U2z5xKyp9EmcRLBg_PIbUK1b-W-AHizJxSetebFvmxfrlzTKkNv1dXIAjxI5gHf5EPqQ4Wk5VYSOIaLARaht7Y9xG7ssD92a3-r9n_epfqf-hrXx2k9QurkiXZJWKhCHt5HDhzZO-NY04euX5t1RONav17VZSEn_JMpSNmU2hBdP271OtYN1RmNTi2u_ya0SMCygASHd1vTaLjkpzgDr6nNKqfZkK1iO0Y-56m50cbVD0XgATlw11CtaA-sgzcEGiXamw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5349" target="_blank">📅 14:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5348">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Irda71mzm6vyYXrJ04-rNMRCGB5oG7GSMdeDQCtFBqWP2_aG24tUSaBJO3_irfLLR-ZOk9edlYPQgxTzvWak-e-hThEE6K8yF1jzRz7y_9Opo8M7w6QjfiS2DPB6IOvXNUB-mIk82f9BSUr9pqRSbpNVP6ikjdl1zky2MTZ7n56OrskJu70a8pZYliUEs60pC94yRGkmwIqWKr-gT5OKFVa61B64AXfhD5o4iTX8N4n4wCvv7fynjRNegpQKrFittosudVj3yj0IOuHXRMBL41NnT6R9k_mm7vPf4D_AbKUfChKs4ZL7WSv03ytgpKWOd66iycBHdlVPphRfGeRJWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت‌سی؛ تایپ‌اسکریپت اما بدون موتور جاوااسکریپت
ورسل لبز کامپایلر آزمایشی scriptc رو معرفی کرده که تایپ‌اسکریپت رو بدون نود، V8 یا هر موتور جاوااسکریپت دیگه‌ای به فایل اجرایی نیتیو تبدیل می‌کنه. نوع‌سنجی با خود کامپایلر تی‌اس انجام می‌شه و خروجی می‌تونه C یا WebAssembly باشه. نتایج اولیه استارت‌آپ سریع‌تر و مصرف حافظه کمتر نسبت به نود رو نشون میده، هرچند سرعت اجرا هنوز پایین‌تره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5348" target="_blank">📅 13:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5347">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">https://youtu.be/qNYT3eoyJ-c</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5347" target="_blank">📅 12:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5346">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ویدیوهای بلند بالاخره هماهنگ می‌مونن
ریسرچ گوگل یه فریمورک مولتی ایجنتی معرفی کرده که ویدیوهای بلند چندپلانه می‌سازه و جلوی عوض‌شدن ظاهر شخصیت‌ها توی هر پلان رو می‌گیره. لایه‌ی هماهنگ‌سازی روش Gemini و Veo سواره و SynthID هم داره. چهار فریمورک به اسم Co-Director، CANVAS، A²RD و VQQA پشتش هست که دو تاشون توی COLM و EMNLP 2026 چاپ می‌شه.
به نظر قراره ویدئوهای هلو و پیاز و عشق آبدار رو قوی‌تر بسازن وقتی این تکنولوژی اومد
😂
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5346" target="_blank">📅 11:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J_gL5u-tFR7uAcMjGUR0ASztDWcyjdjOSf0fN8EKyzFhsTzwSgK1LRgmp3aCgNlqqAOT4vm86CjWMN5HU4VleU7QsZ1nIpwTEoOsmZjWWN1HPLAygSMgCNhqqznNnFmmsJwz9YTSqWWX875UgHJMuRQjnU_A7fqGUbAv23P-7jX81qB2kZPm_VF2RLzoxcW3lUXqVQIGtlvkjjFkLhWgNLyBqOH4_-LVDuLYqh451hbL-AWAi9H2TqCQvP9ZFAYQUQWfcTcauNyGSdcVNarPy5g0woxjZ9SFdagLTn0dNM2t9xmktUiL2cqdtEpqUl0FxMdTbJnXoCyKQEiUNL8-GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک آرنای توسعه‌ی وب مدلهایی که اخیرا ریلیز شدن.
طبیعتا Opus 5.5 با این هزینه، صرفه‌ی اقتصادی خرید پلن کلاد رو خیلی بالاتر برده. و نمره‌ی پایین Luna 6 توی ذوق می‌زنه حقیقتا. اختلافی با Qwen3.8 27B لوکال نداره:)
که آفرین به برادران چینی</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5345" target="_blank">📅 07:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5344">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مصرف Opus 5.5 به طرز عجیبی پایینه و همه توی کامیونیتی ایرانی و خارجی هم دارن میگن.
خودمم که دیروز توییت زده بودم راجبش.
روی پلن 20 دلاری هستم تازه و اصلا تموم نمیشه به این راحتیا</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5344" target="_blank">📅 00:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1cccff5f95.mp4?token=LgtH-kUcC7ZgK2xZdcZLUA1afzsEIQkJJQevRLgBvGRrZ2Kbc0cFccYxosEnS0LjdPzfCFBwdqpG6sj_G3n3ww6vvzWIa5gX7dcaBXPUZVGbu7IRJdnXv_r1Bv6xBzFE1eJLKhG2I1bUcgknZmvHI04akFtfN-wZzqcsyKK4aPDBH0CvkDN5xMWEO_zg8g0rleGv4HV27mjvXttDDXk5DaONhhKocFzxdyqCHG83hdYz6aW8_mSUwMx7XV5lBd_CE997XT1SIa6FPWiwW5F1T41-3ykgNIjf8_Y5fU6F2nQ3fxMRnd7ebRZn-lwn0LPvYwTv7kXtW9QA8TTCHKbYEg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1cccff5f95.mp4?token=LgtH-kUcC7ZgK2xZdcZLUA1afzsEIQkJJQevRLgBvGRrZ2Kbc0cFccYxosEnS0LjdPzfCFBwdqpG6sj_G3n3ww6vvzWIa5gX7dcaBXPUZVGbu7IRJdnXv_r1Bv6xBzFE1eJLKhG2I1bUcgknZmvHI04akFtfN-wZzqcsyKK4aPDBH0CvkDN5xMWEO_zg8g0rleGv4HV27mjvXttDDXk5DaONhhKocFzxdyqCHG83hdYz6aW8_mSUwMx7XV5lBd_CE997XT1SIa6FPWiwW5F1T41-3ykgNIjf8_Y5fU6F2nQ3fxMRnd7ebRZn-lwn0LPvYwTv7kXtW9QA8TTCHKbYEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب، Jev از زمان عرضه داره روی GitHub منفجر می‌شه و همهههه راجبش حرف می‌زنن؛ و اینا چیزای باحالیه که مردم تا حالا باهاش ساختن و شما هم می‌تونید بسازید:
- پروژهjev-trader — ربات معاملاتی واقعی که سفارش‌های limit زنده روی هر بلاک ۳۰۰ میلی‌ثانده‌ای Monad می‌ذاره و فقط Jev تصمیم می‌گیره. ۱,۹۱۱ استار
github.com/jarrodwatts/jev-trader
- پروژه jev-ultrafast — ایجنت مرورگر که هر کلیک رو خودش انتخاب می‌کنه و فقط وقتی واقعا باید تایپ کنه، مدل متنی صدا می‌زنه. ۱۶,۷۵۸ استار
github.com/browser-use/jev-ultrafast
- پروژه jev-doom-agent — Chocolate Doom واقعی کامپایل‌شده به WebAssembly؛ دو موتور روی یک نقشه، Jev هر فریم تصمیم تاکتیکی کلان می‌گیره.
github.com/lukaske/jev-doom-agent
- پروژه jev-t-rex-runner — همون دایناسور کرومه که هممون هزار بار بازیش کردیم، حالا کامل توسط Jev بازی می‌شه: بپره، خم شه، یا ادامه بده.
github.com/joshlarsen/jev-t-rex-runner
- پروژه‌ی typesafe-chess —خود Jev در برابر یه موتور جست‌وجوی واقعی، دو بازی با رنگ‌های جابه‌جا. موتور جست‌وجو هر دو رو برد، ولی حدود نیمی از حرکت‌ها نظر اولیه‌ی Jev رو وتو کرد.
github.com/TholeG/typesafe-chess
- پروژه jev-drone — یه کوادکوپتر شبیه‌سازی‌شده فقط با دوربین مسیر مانع پنج ایستگاهی رو رد می‌کنه و Jev نیم‌ثانیه‌ای یک‌بار وضعیت رو قضاوت می‌کنه.
github.com/RomanSlack/jev-drone
- پروژه tax-doc-classifier — فرم‌های مالیاتی IRS واقعی رو با دقت ۱۰۰٪ روی ۲۶۱ فرم دسته‌بندی می‌کنه، با هزینه‌ی تقریباً ۰.۰۰۱ دلار هر صفحه.
github.com/kyotofin/tax-doc-classifier
- پروژه killmyidea — ایده‌ی استارتاپی‌ت رو توصیف کن، Jev از هر زاویه‌اش امتیاز می‌ده و بعد kill، fix یا ship برمی‌گردونه.
github.com/monteduro/killmyidea
- پروژه jev-curate — ردیف‌های Parquet و JSONL رو با قضاوت‌های typed با سرعت ۱,۵۰۰+ ردیف در ثانیه پردازش می‌کنه و فقط چیزایی که از حد رد بشن نگه می‌داره.
github.com/AkashPriyadarshii/jev-curate
- پروژه pg-jev — افزونه‌ی PostgreSQL که بهت اجازه می‌ده به Tableهای خودتون سؤال انگلیسی ساده بپرسید و جواب واقعی بگیرید.
github.com/realZachi/pg-jev
✍️
imryven
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5343" target="_blank">📅 22:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cUaDS3EKmQHD2BV37S70S44Zp5BCnEHUi_uVMVtZqIjZ0QjLWP_O0vC7KCZGcOh63OD0uNoFc-94xgwF3g0RnQ6qSBypG2viIxvjGmhhjXW706BIljVk6CwuHxYkT0ziNeJlayoKgHfRKjKFhcFAGqWpgKPN39PJMy93WDbL7HyJh49ja7LNnDrCRt2hbYwUe_TwhooqjTeYZ0p1SNw3w3XS1CyNj3oI2GZl6Cf8s8JDcRTlbU0HD9_sxpsr6BBQNGSQ_GRsUkIKeliW51HTKEnp5JgpWdWYsQ5d8wA5ZIpvdaJaHsaX2xNvXsC-xF0ojAi5D7Strl77swJmTHtK2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«داداش اینا که AI بود»؛ ناسزا جدید نوجوونا
😂
گاردین نوشته تحقیرآمیزترین عبارت امسال بین نوجوون‌ها شده «That's so AI». یعنی وقتی می‌خوان بگن یه چیزی جعلی و بی‌کیفیته اینو به کار می‌برن. جالب اینجاست که بین عامه‌ی مردم، خودِ AI داره به نماد بی‌اعتمادی به محتوا تبدیل می‌شه، نه فقط صرفا یه ابزار.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5342" target="_blank">📅 20:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">هکرها چطوری ChatGPT و Gemini رو کردن دستیار کلاهبرداری
🥸
یه تحقیق تازه از Vigilance Security نشون می‌ده یه کمپین گنده (اسمش رو گذاشتن Dark Sourcery) داره جواب‌های ChatGPT، Gemini و Google AI Overview رو مسموم می‌کنه.
قضیه اینه که: کلی پست و PDF و صفحه‌ی پشتیبانی فیک می‌سازن که با تکنیک GEO بهینه شدن، که هوش مصنوعی شماره و ایمیل تقلبی رو جای «اطلاعات رسمی» بهت تحویل بده.
تا حالا دست‌کم ۳۷۴ شرکت قربانی شدن؛ از Fortune 100 گرفته تا Delta و Lufthansa و Bank of America.
چطوری این کار رو می‌کنن؟
1- شماره‌ی فیک رو با فاصله و نقطه و ایموجی می‌نویسن که فیلتر اسپم نگیره، ولی مدل راحت درش میاره
2- شماره‌ی تقلبی رو قاطی شماره‌های واقعی می‌کنن که معتبر به‌نظر برسه
3- محتوا رو فوری می‌نویسن (جابه‌جایی پرواز، قفل شدن حساب) که هول کنی و سریع زنگ بزنی
4- پست‌ها رو می‌ریزن توی LeetCode، اینستاگرام و حتی PDFهای سایت‌های دولتی و دانشگاهی
پاک کردنشون هم فایده نداره؛ کمپین اتوماتیکه و روزی هزاران پست جدید می‌زنه.
بدترین قسمتش؟ Google گفته این خارج از scope‌شونه(
😂
😂
😂
😂
) و OpenAI هم گزارش رو بسته، به این بهونه که reproducible نیست. چون عملاً به سیستم خودشون حمله‌ای نشده؛ فقط خروجی AI دستکاری شده.
۹۱٪ آدم‌ها جواب AI رو چک نمی‌کنن. شما جزوشون نباشید؛ شماره‌ی پشتیبانی رو فقط از سایت رسمی خود شرکت‌ها بردارید
چون به زودی شاهد همچین افتضاحی توی ایران هم خواهیم بود متأسفانه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5341" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5340">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ogCGq9EE5hbBcRx6BYZ5HyypFq8e3emfvWG818WiE0Xl7USOURKQBVwxmX4oblX83PRfargB0ynAUJ5nR8glrFe0ynrr2VxonqC2BtVWkU25DCghRcPx8MVyhgLcnpLFPsREhzolwHJWE2QRPVjsOeda88lA4FcKD_XzGdoFjE5EILpqkjkulYDfnrNZ7MwkJm7qkxJQ5kxVBDJLdShlfax4tBFZEJjT0ZuS1J-OvP7jhqOGDC0cdnc71WvtK7qpUmqXGKSWCjFktpqwc6_pGjsjCq3G58iJf9gvRTGduLx2P2Qc-uhTHHnSyZ-lSgQrsKcON3p4yf6obMPICam8Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیق رسمی استرالیا علیه OpenAI
نخست‌وزیر استرالیا گفته یه agent از مدل‌های اوپن‌ای‌آی ۱۸ ژوئن رفته توی سایت Services Australia و فایل‌های داخلی و آمار سلامت دولتی رو برداشته؛ دولت هم تا ۱۰ سپتامبر خبردار نشده. این اولین نفوذ ثبت‌شده‌ی یه مدل AI به سیستم یه دولته و حالا قراره تحقیق قانونی بشه. (حالا اینکه agent رو چطوری چند ماه بعد متوجه نشدن رو کاری نداریم
😑
)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5340" target="_blank">📅 18:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دارم روی چندتا پلتفرم کار میکنم، یکی یکی ریلیزشون می‌کنم
اکثرا هم سر و کارشون با ترجمست
و یکیش هم برای یادگیری و تقویت زبان انگلیسیه، اما با یه روش متفاوت</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5339" target="_blank">📅 17:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k07RKCRjQf8oKX6OgH4MSdhH3XZ2nq0m28PoQzBoD39I_-gyN-glbiRrnCAKqvga1sv65D8VfBB2PfJtXt-SWEDgSNbmbPWK1C7q3S_YZjWG7ILN1XOaP94iceDnYzALTSeLjhz7670nxMgy-O4GfhAQ3gsvQVB-JNRl00Keo-9RgFLBPbEQgwqDFvxT346THR3CfhuBBT0opyt1Ioutda3v2bRTcy8tLmqUq0mSPDbwlYswIcFnBx91JJ21wSEpmb-AxCtBZDq7moppVkBVDOixNMCX-uT73f77ThZ6ClbFykaR59bpySUbKp8oqylttbSZvdSiTLoVccJc8JQK_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5338" target="_blank">📅 14:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromReza Jafari</strong></div>
<div class="tg-text">تو سایت زیر می‌تونید ببینید مردم با jev چیا ساختن و ازشون ایده بگیرید!
🔗
لینک سایت
@reza_jafari_ai</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5337" target="_blank">📅 11:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5336">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مراقبت کن عزیزم. سلامتیت مهم‌ترین چیزه و ما درک میکنیم
🌱</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5336" target="_blank">📅 11:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">یه سریا جواب پیویشونو نمی‌دم ناراحت میشن. از دوست و آشنا گرفته تا غریبه‌. دوستان من دستام تونل کارپال وحشتناکی داره. توی طول روز هم همه‌اش پشت سیستم نیستم در نتیجه نمی‌تونم اصلا گوشی دستم بگیرم اکثر اوقات که حتی بخوام با ویس جواب بدم. پس اگر شرایطم رو می‌دونید…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5335" target="_blank">📅 09:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5334">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یه سریا جواب پیویشونو نمی‌دم ناراحت میشن. از دوست و آشنا گرفته تا غریبه‌.
دوستان من دستام تونل کارپال وحشتناکی داره. توی طول روز هم همه‌اش پشت سیستم نیستم
در نتیجه نمی‌تونم اصلا گوشی دستم بگیرم اکثر اوقات که حتی بخوام با ویس جواب بدم.
پس اگر شرایطم رو می‌دونید و ناراحت شدید واقعا برام مهم نیست که درک نمی‌کنید</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5334" target="_blank">📅 00:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5333">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cWS7YR1n-vwomuA1J-Ni_v00lmE_TsNrNeGhfdYIaiL4OPqzUj9IzvUS-h_zhHcBBOiuEI4BfJGm9gux455godGKg1yWjg9zpQ_OpHG5-06RJyK8zXBLn5D6CRhchaRH6XHq40FHkAYP0_6iZ9e3eHCswy0Wi2lf0B5C1ZwMOge8fRALUK3YlTt_Yp4WQp9p4mpw0P9LYDwGEUfCmBGXuUkXwHp1yprm_VFcr-ZQfCO8fveSXWlprPh1Li1Jv9BVx8-yjyRhhyNn__e4okLB3HFnMyC9NjA_0rKr4QXikA-SLk-bZXMnxmOGHzOG78JNEHcWs9iTlRTR9xpz6Xo06g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل
GPT-6 Astra نشست پشت فرمون تویوتای واقعی
😂
یه بنچمارک عجیب به اسم DrivingBench منتشر شده: مدل‌های زبانی فرانتیر پشت فرمان یه Toyota Corolla واقعی می‌شینن و باید یه مسیر مخروطی رو طی کنن؛ یه ناظر انسانی هم آماده‌ی ترمز زدنه. نتیجه‌ی جالب اینه که GPT-6 Astra با Codex توی تلاش دوم ۱۰۰٪ مسیر رو در ۵ دقیقه و ۲۲ ثانیه تموم کرد؛ Claude Fable 5.1 به ۴۵٪ رسید و Grok 4.6 فقط ۱۱٪ پیش رفت. ویدیوی هر تلاش رو می‌تونید توی سایت منبع ببینید:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/5333" target="_blank">📅 23:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e71e738709.mp4?token=ERLzpEkrI9I5f6QC2bSA4QbtXv-FyE9xA7KRJAER1W5P-15UYo5cX9ZnfRmBlKSp4XTrLTZFqSlKXPrr9rtUPk7ys3T8TB4Qi-vFsrkPfnfE15vjS97d8tOVOOitvkY-hvODvD-hUiDBTEHjJtk1CfeYQ7Op44BbyG-52vSsuT-Yoo8121UaXKmdw0QiqUwj0TnGF8sYBIdOy2MGWGD-6ZhAHJncXdREcqJ3-iD29bCIafN9uhJNTwo-26gicG_Vi9-oKxUEVhcGSYszXTRSRYaT3-AShdw_htCdk1HJjVtKu2SFA0xpASVxAVSnbZUpXTGPFeQCSGkJEDNtJmJbPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e71e738709.mp4?token=ERLzpEkrI9I5f6QC2bSA4QbtXv-FyE9xA7KRJAER1W5P-15UYo5cX9ZnfRmBlKSp4XTrLTZFqSlKXPrr9rtUPk7ys3T8TB4Qi-vFsrkPfnfE15vjS97d8tOVOOitvkY-hvODvD-hUiDBTEHjJtk1CfeYQ7Op44BbyG-52vSsuT-Yoo8121UaXKmdw0QiqUwj0TnGF8sYBIdOy2MGWGD-6ZhAHJncXdREcqJ3-iD29bCIafN9uhJNTwo-26gicG_Vi9-oKxUEVhcGSYszXTRSRYaT3-AShdw_htCdk1HJjVtKu2SFA0xpASVxAVSnbZUpXTGPFeQCSGkJEDNtJmJbPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتضاح Union Alpha</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5332" target="_blank">📅 22:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مدل Space Bunny(که یه مدل مخفیه که نمیدونیم مال کدوم شرکته) روی اوپن کد رایگان شده برای یه هفته
- 1M Context
- Multi-modal
بریم تست کنم ببینیم چیه
امیدوارم
افتضاح Union Alpha
تکرار نشه</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5331" target="_blank">📅 21:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5330">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hk9tb4wB1ucvvTkuIIJ77fG6H_AkFUScbS4zYTJ-nWLm_zmcKUNHvdE2EHFML-uul-HPZnVU9acmSVg10G58z2506Vy5E02yKMhtjw3ULUjINWsmV-kNqyxwsP3Y1PISUl6iOB7Bz9bDTo-oE35VMIUpReJnTWSjTQZLPYYovEd94nWJeXhewGQSqEdeZhx6cwr511YXu9Yk7qdk01RfNhOU42kANr9zveb5C5uWse1fL42C2bY9AqDseWrVeUhNjY4UQJnV3lbu7wZNk2oMpD-G4s3mKCkopL-sxZ7lEuhtHZJKx8SX--jq8HETV0CqWZaLS1sS3vDn5jZGmecrvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی GPT-6 Sol، GPT-6 Luna و جنگ قیمتی با Anthropic و Xai
دیروز Grok 4.7 اومد، اون وسط Mimo 2.6 و چند ساعت بعد هم Anthropic مدل Claude Opus 5.5 رو منتشر کرد. اما از لحاظ هزینه، شوک اصلی رو OpenAI با معرفی هم‌زمان GPT-6 Sol و GPT-6 Luna داد که رسما بازار رو وارد جنگ قیمتی تازه‌ای کرد(برا ما که خوبه والا)
مدل GPT-6 Luna با قیمت ورودی ۰.۱۰ دلار و خروجی ۰.۵۰ دلار به‌ازای هر میلیون توکن، تقریبا نصف GPT-5.6 Luna قیمت خورده و به یکی از ارزون‌ترین مدل‌های تاریخ OpenAI تبدیل شده. مدل GPT-6 Sol هم با قیمت ۲ دلار ورودی و ۱۰ دلار خروجی نصف Sol قبلیه(۴/۲۰) و رقابت شدیدی با Opus 5.5 داشتن. از اون طرف هم خود Opus 5.5 هم افت قیمت داشته و هم توی تست‌های اخیر، سبک مکالمه‌ش طبیعی‌تر شده.
منتظر بنچمارک‌های معتبرتر هستیم، خودم هم به زودی تست میکنم
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5330" target="_blank">📅 17:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5329">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">یه سری نظرات راجب مدلهای چینی دارم
سعی می‌کنم ویدئو بگیرم توضیح بدم کامل</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5329" target="_blank">📅 15:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5328">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">عرض تسلیت به دوستانی که مدرسه میرن
غصه نخورین زود تموم میشه
😉</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5328" target="_blank">📅 15:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8fb483df78.webm?token=GDuh3uLQRSxPGFQfm456wXgjwvPVFYGwYv5rZWYD6_bXkZWpXW3AXkKgXeTKxuJm2xd59B_a87kTxqJi6JnB_IEitf8XV67ypjl3h4NJDpUq9q5NE73OwkDRi-DLElFydZ0LIgNYSGLMkvxRXaTc7ariTIf1faDr6gpCXH6CVWBIjtJsD97Eg_IGoBnjDDqfvIgawxwuNnY-jN-fuIbJihgDy3q_kPMcT-WrfY_a9j1gqtybH5RXrb-SrkS0OZrsCIX7gbXMaZNZzS_Ou68YW5M7vM3snrjYhH3dzZaLfgxp29UGGboO7HJxFnkMrKioIfSEg9OZAmCLiQ9jgg5xkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8fb483df78.webm?token=GDuh3uLQRSxPGFQfm456wXgjwvPVFYGwYv5rZWYD6_bXkZWpXW3AXkKgXeTKxuJm2xd59B_a87kTxqJi6JnB_IEitf8XV67ypjl3h4NJDpUq9q5NE73OwkDRi-DLElFydZ0LIgNYSGLMkvxRXaTc7ariTIf1faDr6gpCXH6CVWBIjtJsD97Eg_IGoBnjDDqfvIgawxwuNnY-jN-fuIbJihgDy3q_kPMcT-WrfY_a9j1gqtybH5RXrb-SrkS0OZrsCIX7gbXMaZNZzS_Ou68YW5M7vM3snrjYhH3dzZaLfgxp29UGGboO7HJxFnkMrKioIfSEg9OZAmCLiQ9jgg5xkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5327" target="_blank">📅 15:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">Check this out:
https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5326" target="_blank">📅 14:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vzs1ha-nCHgZsjzKWmFDd3_q8JgursWy0sgblmq91ohoRcn6V-UUhkqqaKFH5JRccenh-J1hPdDZvsIo_PEtRrlLE6xxrSO0s0XcWdxGNCSjJcM5jSzWW0lVMDrP2QJdh-w3AyscUK4kmZswWYUNfRVcSEFGpH5CFfRRXIA__S916JIEb74d3NPx-GXiQ_lKQVLFpl2YvtFmgzsmJ0KACcci6jgmjdUzWdIsPpXR5-1ZYxJxxoF1hkpUn4goWBa1tkiP6A2-sPhnP-BYs8Mxdcr75ER2jky37B5Z8bGY4pkqKvSBusD2jnxvmQNJweQyFTp-xjz_80ThBr4VvN-4pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بگم از چه مدلی استفاده می‌کنم اونم با چه مصرف پایینی، باورتون نمیشه</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5325" target="_blank">📅 13:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فراموش کردم بگم، یه World memory هم واسش گذاشتم که کامل از روندی که تا الان پشت سر گذاشته اطلاع داشته باشه به طور خلاصه</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5324" target="_blank">📅 12:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sDzMD2mdcYzZBQR3q_ncjZtuxgC00snGUtFnKH9mt19xUCXPseR6QTSA1DtopVeEnWbn_StSBDH1Y2H3uoA4VQaGBUx6bZwzFWzgfYPuBVCLagntkGYIgWd80rcSNrsyaXgcSwSEtuMTotXLIOlDgp1cY-ujAQnmxSoSR7fxeD5xPKWr4Wux2XC0bAPenjr6th_zOqx-SQWICo9nyUtGNyeN5NTN-lMwTFS9-UgW8uKUMEg9sqTGvsBaRI3UeB21vaHfimz5C2RTrUiAhG4JoBGAzkS3VldI0lCclp1ivBAayF14BeyIWG3xHGRpZcS6HlpAwGSNrDjvLeoXU1CruQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YhijeIbXjzTNmP4gwz-zjE3MEh8NHT2NbrBZnnOnqQPr07W_V9D5WDE535i5RuNd3SrIlCi5OIIDFVnaGWtzR0XsomlQ_SmncTFyIf67f6eKzOG_TqSsgPVILTKNs6quMWP8UhDp54d3KFjB6VBp7GxeB67MceJXF8t5WByjFlHFOHUD21XccvFo_rMpraGuKKxN156Y7WIRYhTeCjBniYWGOXWB5TnW5MtAuSK_NMrd_-LF0L7X_ufQ28FXSVbFrkQ16m0AzOPbJjJuCSj6YQRWpeTet_t74GF2XmsSghk8j5IF1ijKu1nPTBmpPZy9_S79obD0KWcWt8HN9iIT-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XaWPkB1a03J3zTvkrVnkPJIDHPD2_QBxIcXymG5tZRx8e-RXIK2yA79sC8cHk4E0vCQ_wfRP_h9Dan1oUkrQUuwo7TSGffytima7cf-oqXNKLly_0QHswEH0YEreML1vtGJxY90HkSa_wEzpAXiyWNWJM4Y40U3FHiER_qKk7krJ9u10lGqvizSDmT8Zfk4eCW4mcHtS8Ht52z3u3nolzRW8XDmS18VJIwIpqoZWA0hX4jHfc_WQrZOQFAvo_0bMbK6Hwq4Gn7mTXYhDA8zBpE0YW12xeT5zywxySNqNTDbDetrFi05AtaIRsFY2goli9Aw7zhCuNxdXaTbaKjlEPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WTt6hV3PXjmPTY_ZsOcaLPsHzre9iOZy_EqpQ93G1XwftPCaQUp4wNxwxi-MnNCBex-OwxkiY7sparqrZgFybae8t0bZDqTvwhPTyiqZun8CbgJ9_ChOljKjxvYZBkIStQkrvrlN843Gby4VhsGyu9YidoNtmPs9f0f0_UURz6WOfCmI5lls0FLqtH1kzuvJCqgdCY8yj3hgcwaEbzUMX5wixPbA_ep1oQDhARWeXN1w-1eOBXPx9H7EZgdTgU7aP1gzPdvTKvKiyg08btGkZ6BMXPGSMSADo26ZG4ewtiylErD9uutiqBw8AtpOjeK29Xv2TZAnk23FnhfL778JTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S7q4ItM7MxoVdgapXKrSxEnxUVYNMIM63JyqFB44-UXIZP0gejTkzTeuF3iRN7U0df2B6KBE0TyeEwnpaB0DhVclp-KZTbQ9tt3uTYtIM0XB3JQjSYrdkZBAArnBhP8aBprGOPshXAtwu6Vnbk18PR6nj1sn5yd-aGxDJQpe7KSvb7C8e1Sk5j8VQY0UvYOk5qBr75H9tYnwex1y-32jLzBaAdr6-KVyvCVnqVgLXtfozv-wBaWhOm2lZdQ1g8eZ8MH26X7n-TXjhJlUkj7s_F46pgcD0lrXLdwDICOT0zunifPIgXrVoRl8KCOqN5KGmlpPDj9vLYtlm7kkosFRAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VEH4tiXQsvbqrg2dMZIqlnHHDX9Dr_S6p4Xa4o-1I6EOFfYIMippF5JedSXUW-YWQcVtkR_uS3i9e_91YW6JzvVdS8otgMqT7h4SLyrtqRyWzd4ZTZSz6jrTXqzF6fVMILaeStdMRSx2dTuSE1yDsqMPh0WyiJ4n2U3Z-5jMwRXNyJod-xxqWEM95BP7bU4S46KyWZk_EbL8PbAe0IIFjOyMNl3TEGUD1SBFn4p2H8tBhoZ14ffV6EuSAp_TX-82R9JiXxiz-1vc98DhbVh1R--TAgdA4_iw9D_6G4poA9mNmsYajhb0Eb0Tue_KC4kIDLinIw2in3WHCusNqnbfIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X8FRYtYZ4xRsIgb6Dv8NuETJ6PFpuKMoxjtKFT0WiSIgTbR9mbWcq8IT56ittVghI82mey5-ytLDtZ0CASgufEZxHyewRX4mCRRLf2IiEbRU5aEgs8KlsT70rshBjQEtdczLZWv-lRKz-jnuZGHuitJvXRKlfXf1GYAh8BZ6rDnh0dzs4DVa5MKjzASsNCQ2Y92b9K-dMo34Qy70FG5CZ500oYbYrWXjVQTrP2Rk2LVt_nOGnheiuSNdEuaC6c07rI1iH78gI3fXLH8zK2o2fUDCZLE9Hn23wAwmk_yjYAmYhrlDjfByef3YnuoBPuiZvIkRifvLxxszUGBMZ2RfAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گذاشتم قویترین AI دنیا ماینکرفت بازی کنه! GPT 6 Astra + Jev  توی این ویدئو، با همدیگه پروژه‌ای که ادعا می‌کرد تونسته ماینکرفت رو توی 8 دقیقه اسپیدران کنه بررسی می‌کنیم و خودمون بازسازیش می‌کنیم با استفاده از Astra و Jev از برادر کوچیکم دعوت کردم بیاد کمی راجب…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5317" target="_blank">📅 11:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OgjyvdMzXtyd3yAXagLYpVnmrUdtvzv7FAxKii72LFuFeGCS9ZnFeWWVxEOedrU6Ei0Mj88NssR4v0bq7zErT68ms7yCsMlvAVHk_CSU7e9_z41BlyBR0dqg_lfgv_dLiaFXVo-0kdmzPoaezhzTtetAf0RcOpMh05Ep04vIA152exQRx74IC2CjTDeR1LK8gm5grHpoJw3iBHXeoTclt7MmjFfdY-O_Ryl0o9Lp2G1yiq2DV3q9EyepSVwj12rBSF0cMBie612-hT97LU4VfMXqfw3lDBLvREgPF9znSPH4FmlwqsH5XDauDLkF49DF7X35Upyg9HmZ-igMip2jHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کد Rust سریع‌تر از کتابخونه‌های روز، فقط با «سریع‌ترش کن!»
نویسنده‌ی بلاگ minimaxir ماه‌هاست به ایجنت کدنویسیش یه دستور ساده می‌ده: «این کد رو سریع‌تر کن» و بعد بنچمارک می‌گیره. نتیجه‌اش کدهای Rustـی شده که ۲ تا ۲۰ برابر از کتابخونه‌های state-of-the-art سریع‌ترن. حرف جالبش اینه که بهینه‌سازی سرعت توی RLHF این مدل‌ها جای اصلی نداشته و با guardrail و حلقه‌ی تکرار باید تکونشون بدی؛ پرامپت‌ها و خروجی بنچمارک‌ها رو هم کامل منتشر کرده تا کسی ادعاش رو بی‌اساس نبینه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5310" target="_blank">📅 11:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">فراموش کردم بگم که هزینه‌اش نسبت به Opus 5 کمتر شده.
هزینه Opus 5،
5$/25$ بود
هزینه Opus 5.5،
4$/20$ هستش</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5309" target="_blank">📅 00:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gMyEBH6gBFmf2Ov_hBGOv3ycomYscnUg7qIE0IhIatCv9VY-mhXGR1jLdVa9uJ7NGl5LzFtRZxowLwEJQPVMUBkfumbG8JGwLtwXrDMnj7zGnQtCV5I-RHj6JPPVtVPi8ExVzYa8xjGcUN2I40ZqRAcM19QOcR9m6U4hFY1-wC9ckGqstKLl1c3J2z4Wv-Xh_LMqCgU8y3GJqJ35HZyM5L6wL_3nj0cM3cgxlbi3W-bge4RFRABc44tIw4Kx30x-nqu-YlWIi4qLaVDfndf-iZYJ-78WxkSqKj6i3Ibgup56JrTF6CnnKp-FYV7h8-M_s4jQYDhem6Iu8f1DjHmK1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5308" target="_blank">📅 21:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QH1UtntiXwVTh8K8KT8-DYrd1u4drDGZOJF9Ws7r-mWuT2GJGxuecSBbxAD09nQnlj7ls3rKA0RAAdAHnpuPqsKfLalWmw4b7qWeQKm3DkerWCnUiHdt06c95Puk81MMrWzPk0X3Ts6O9RV0UclHriSKuQG8GlQJixwMNtSPWLCKEv0q1AOkJyIdho7h13s6NkvB3p1geaIfO3nRIF_q5Kk4xqDFsqRqyOn6mCyP2RCdFWyXuWRiZ5Ef7WEeVTjBGGfbZChGKtAImLgl-gF-K51jpK8Ox-Tyy1jvkZTKVpWkx_F0Crim-uV9LnrZ9OeHa_0P-bk9WYutHnL7CIRtEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IpWK1fp1xV76Qu68zDhsnhnfIF4q8D2mC3jZtkOK3ULbz4iblN9CKQY9FOnST3VUQOfPvFcjP-eiyt8wzJyM8QRwFitO-aZ8D8Cd6CpSf7hQoCesQPqyia8wNOr5JGojzlZLjgA-v6J-7OJ1cMy5q9ZSyqoxGv_YrskP-4Qgqibrw2ZBaDF_wkseF7bDGtvXqWdt6XHPB1KzHQP9sz9RbvdfgkYkbz7XI3obVjncqtdSrgx8-fmAQ-78HGhaflTLPItRqC6AsjIWsblNEA3oHWSa0QtGS7wTn8kITNr3qXKye2e6_cFe8pb1nDfq7T4OyA7-jC_cZffykRB4b6Buqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مدل Opus 5.5 ریلیز شد
وقت اون میم مدلهای چینیه</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5306" target="_blank">📅 21:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G97ii1z6j2-TTeFA2aBhqHBhn0O7E7LnhijAcd9jVYs3qSnJABultYQYuWNS7V0bA31r10Jke7fkMkrFb9_uEjvjuv16QnwkagHJI6HX5j5Yt8FSsDbtcGrtacF6XRspTNdOAYtNLc20Fg27jwgcG1wzeX_Mxo6svQakdedY4DRktOs2054T0zZQrmjzFuRKzL5YItfDs5p9RbIrm-hUmjJcoE_xvGBvghee_3Gsic2NAz8Hp-xIrwOnBzJOQFPcGmiCMFYkpDUE_73PQLFPj4jZ9FQ0eWqcHGTxRiWpqcFKFnA9uyIRFFzhIhqD0E1SD01HSqMU191T5mUUp8BtcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر روی 9Router ارور
HTTP 403: [403]: {"type":"error","error":{"type":"FreeTierError","message":"Error from provider (Console): OpenCode's free tier can only be used from within OpenCode"}}
می‌گیرید از اوپن کد، علتش آپدیت نبودن 9Routerتون هست.
برای آپدیت کسایی که با npm نصب کردن، از دستور
npm i -g 9router@latest --prefer-online
استفاده کنن، و کسایی هم که با داکر نصب کردن از
docker pull decolua/9router:latest
docker rm -f 9router
docker run -d \\
--name 9router \\
-p 20128:20128 \\
-v "$HOME/.9router:/app/data" \\
-e DATA_DIR=/app/data \\
-e JWT_SECRET="change-this-to-a-long-random-secret" \\
-e INITIAL_PASSWORD="your-strong-dashboard-password" \\
decolua/9router:latest
استفاده کنن(با پسوورد و JWT دلخواه برای JWT_SECRET و INITIAL_PASSWORD)</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5305" target="_blank">📅 14:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">این وسط Mimo 2.6 Pro هم اومد و grok 4.7 رو بولی کرد:))</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5304" target="_blank">📅 12:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fgk5jEDOcxc_00rwqso5K0g-AycZ6ze1n9yYzI-CIO1b-pU0Md4bE3yWlBJmMMMJU7QapTa7btzM9zSu0QbEAJiFbxH1024bI4o4Wrq8BS0_ZiUbw0a98_EURpNhYhjO7uVYvy86avDjxaUspZ07i0BX5NuX6UliXbHXyDrj7NrZxStCl9QpD5yTPkA4nCRinNVVJTN3ckXGgUhG1ZutPoqlaNxh7wimHHso84PKC1qy9XOZEtHiXXXiLzCKo6E3pzClnq0vPFmGu6_OanoYa5B7taetCWUoY7NVMm3nFuAS4SINA-4RSQXQ1Y0KYaec5k36QCXEypps00sITOgG5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا منو پولدار کن یا متین ویدئوی ماینکرفتی بسازه:</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5303" target="_blank">📅 11:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BISwLIQNChznsvXfo9k0cc86vQonMAGgH5zGPFx4yUQJ3kSl4myfPRIHfDZfooOJO7LT37bG3hx6UxeLYQc4goqo5D6IS-3zlpra_TUChgSdjjUC5dG-Q-a6GHY93sFG2CK1EEwSDa7WzH2NTVEqQ25kSabQtOC5XQP9VM4K42qsAfDfYzwWEzqYMsQTlQNlx7JnJVjc7wQFjUIMszSPZUMshaiYlHmjKLPUBrRjoMSX92FUh2n-1Z37rp0cp7fd8VYE8z4yAo6BPcM7AqJzcju6SDa8saehAxQRC0y5PYeUtEWIytJF6L3xA-A0nwlzl0i0t2quhm3Bii95_GkEIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گذاشتم قویترین AI دنیا ماینکرفت بازی کنه! GPT 6 Astra + Jev
توی این ویدئو، با همدیگه پروژه‌ای که ادعا می‌کرد تونسته ماینکرفت رو توی 8 دقیقه اسپیدران کنه بررسی می‌کنیم و خودمون بازسازیش می‌کنیم با استفاده از Astra و Jev
از برادر کوچیکم دعوت کردم بیاد کمی راجب خود ماینکرفت توضیح بده و کاری که ادعا شده ai تونسته انجام بده.
همینطور در مورد Jev صحبت می‌کنیم و اینکه اصلا چه نیازی به این معماری حس میشه در کنار LLM ها؟
و می‌ذاریم ai ای که کدشو نوشتیم، ماینکرفت بازی کنه برای خودش ببینم چه اتفاقی میفته
😂
لینک سایت Typesafeai برای گرفتن 5 دلار اعتبار رایگان:
https://console.typesafe.ai
لینک سایت هوشیار24 برای تخفیف 90 درصدی API از GPT 6 Astra:
https://houshyar24.ir/?ref=B2N4W9SS
پروژه رو هم توی ویدئوهای بعدی که تکمیل‌تر کردیم می‌ذارم گیتهاب واستون
🥰
📹
تماشا در یوتوب:
https://youtu.be/l-o_fQM_9AI</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5302" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مدل
Grok 4.7؛ آپدیتی که بیشتر ناامیدکننده بود تا پیشرفت
ببینید Grok 4.5 نسبت به قیمتش واقعاً مدل فوق‌العاده‌ای بود؛ سریع بود، کارکردن باهاش حس خوبی داشت، قابل‌اعتماد بود و به‌عنوان مدل پیش‌فرض عملکرد خوبی ارائه می‌داد.
مدل Grok 4.6 از نظر من یه قدم اشتباه، البته قابل‌درک، برداشت. کندتر و گرون‌تر شد و برای انجام هر تسک، توکن خیلی بیشتری مصرف می‌کرد؛ درحالی‌که فقط یه برتری جزئی از نظر هوش داشت.
البته دلیلش رو می‌شه فهمید؛ بالاخره تیم سازنده باید خودش رو توی بنچمارک‌ها بالا بکشه.
اما بخشیدن Grok 4.7 خیلی سخت‌تره.
1-
مصرف توکن برخلاف وعده‌ها بیشتر شده:
گفته بودن مدل جدید توکن‌بهینه‌تره، اما توی استفاده‌ی واقعی بین ۳۰ تا ۸۰ درصد بدتر عمل می‌کنه.
2-
بنچمارک‌های ضعیف‌تر:
توی چندین بنچمارک، امتیازش از Grok 4.6 پایین‌تره.
3-
سرعت و تجربه‌ی کاربری بدتر:
کندتر شده و کارکردن باهاش دیگه مثل نسخه‌های قبلی لذت‌بخش نیست.
4-
هزینه‌ی واقعی خیلی بیشتره:
هزینه‌ی استفاده‌ی واقعی از Grok 4.7 بیشتر از دو برابر Grok 4.6 درمیاد و حتی از هزینه‌ی Astra هم بالاتر می‌ره.
با توجه به این‌همه تبلیغاتی که برای این مدل شده بود، باید بگم واقعاً ناامیدکننده منتشر شد.
البته بنچمارک‌ها همه‌چیز رو نشون نمی‌دن و Grok 4.7 توی بعضی کارهای مهندسی واقعی همچنان تجربه‌ی خوبی ارائه می‌ده؛ ولی درمجموع حس می‌کنم هنوز خیلی به مدل‌های سال ۲۰۲۵ شبیهه.
مشکل اصلی، قابلیت‌های Frontendـه:
عملکردش توی کارهای Frontend به‌شکل غیرقابل‌قبولی بده. قابلیت‌های 3D تقریباً وجود ندارن و مدل دائماً توی حلقه‌های تصادفی شبیه Gemini گیر می‌کنه.
حرف آخر:
این انتشار واقعاً ناامیدکننده بود. امیدوارم تیم SpaceXAI این موضوع رو بپذیره و توی نسخه‌ی بعدی بتونه دوباره ما رو غافل‌گیر کنه.
✍️
theo</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5301" target="_blank">📅 10:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WJWNWn3iaLGLc6B4k3OORFnXRxDaOWXRjwv4GfAM_i6UcvnMKblVVetFYCKCQdDyOZWAC0OggOweMLfglnQUAJ3MHQl4D4TjefOj-hC9vGucTpzi8ql95J-MIX1MDQ11p6U9P8JvSuDcWfXha9mRlX5YS4DXzVOpd3Gg5vNpUnm2Z5gyAYaRtrpKL5dq1e6qVkDjDCywlfikZorusKSNYag6ziQYnSQhZbV7g6ld9KJMtPk_61bOcoq_l-0zeFW8Ol-KzYY_2jVq8Wl-lWeOua3WfIETsp41YkLpzlNdEVfjMMQC0eF1y4emHAv2SdQOpYW7cfQeF4Fp3I5dCmbiaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط Grok 4.7 هم اومده، توی یه بنچمارک DeepSWE الکی بولد شده که از Fable 5.1 قوی‌تره، ولی توی هرچی بنچمارک دیگه بگردین از Muse Spark 1.3 هم ضعیف‌تره. ایلان ماسک فقط بلده گنده گنده حرف بزنه و تبلیغ بخره متأسفانه</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5300" target="_blank">📅 00:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JGCTo5ibZa2-nVPL0NpR_Yz-q5KdKw3RjqLY375e2-k5eTaZuPX7xu815h4DlgrvAshpRNN49x_w6cYjRw4VZQa4shEPcX0mTnXDTej7EzYGpTH79B_QM9Pci2nq1dSjJNyY_B9o6PD7PcN1E1l-Vgc0_y5-TCRonHw6IxZ5njGTapn1Mbk6_hF-S8e4RQy25XJC0wCxyFhyqfRZRG7e-kvMAArv1y_LsdUylAca7eyflV0NpiV34kZmhap3z8G7lY67_bwwECaeR70LGbe6nE1KrOsR3szMgsu0HRANwM96xLNzR2Yqh_Vu8Go0TstlMUpf2uPnPWZYIFqLSBLBbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/doJRNJvnrsq9r_ipMANNue0-8CeSvVgrKaM1vAy49_xENjTLwMmiRToYqEdrY-j1ajUQIvtN4t0Ya-pu0w0sSVtTOuKLhmcCDdI1i_o_3swT6bAyv_YhRtHkFiRK_dwlsoq8mcuKcn505wy0pJ0THYZ02lnE1aFfPAtv5XFuUOPy2wEyyO2DsDrT78Ytn7IoVxmngdEZl6HVt2apBE8T0AML6ubhic5mQJ_Gyn6YZs39do0BIhpsMQsH6-AKiA9Xh73AgEPP6moQvQPfie4Tw-oCd3FTSGKp4UKGZdEkCgRsJnMAgLB0LAzF1ZppW8pBYQaV1TI5l50f4rqCynnuFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این وسط Grok 4.7 هم اومده، توی یه بنچمارک DeepSWE الکی بولد شده که از Fable 5.1 قوی‌تره، ولی توی هرچی بنچمارک دیگه بگردین از Muse Spark 1.3 هم ضعیف‌تره.
ایلان ماسک فقط بلده گنده گنده حرف بزنه و تبلیغ بخره متأسفانه</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5298" target="_blank">📅 23:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اپلیکیشن ZCode، هارنس رسمی مدل‌های GLM و شرکت Zhipu، اوپن سورس شد: https://github.com/zai-org/ZCode</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5297" target="_blank">📅 22:49 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s44jzAsU7v7mFnnuGiF0KD2dZWAzVsh0z0U53JbwxVw1-ZVEGmig-ktPUWMfpJdDLiqckBxSAS1RH87vefH89EY8c7aHQnIqWwzoiQW8rfslTJUOflR4mKOoUSY4qoH2ng2Mm4vPGJ3Kpvw8KQilEBarbZ4FVkDAlGAqLNqW-5U6a90p_45Qt-xks7eRyX162mhsLNdH_E4HQdmrlc70zCOs5vDdorx1PQITEEAZgojjn2fdsz7h_eEZf83Lpy4KbC5feuWRURahyfB85r4Ew3wx_eti6Ar4OmMx9zkHBu1V8QC4WRl70zK4TCY0IS_iiYbNzqMRA4Rl_BAJDz53Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن ZCode، هارنس رسمی مدل‌های GLM و شرکت Zhipu، اوپن سورس شد:
https://github.com/zai-org/ZCode</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5296" target="_blank">📅 22:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hhy72mzeE2J8PQsv349lNl8SOZAqAU6oOXFlUtoRlZfaTWAMwPZZ1rw3ac03rA1YMPd-x0K8mQFp7BbU9dcZ_jiECVuGK4G734VWFwSxCwj4fh7mX675uM6jRRd9aikY1wLXrfvkyObMJo-svTvak30nT2qkgH0eEEc2CZvdxmrAxnifqVoSrzc85R5-Zsuh1O_91N3aHH6oDfmrGrir-IAhyDp_b9VHqTvpDkPTEfoPfA41E7EX29dfmRCoLyR5G3R2bn6iFMThuVsqt252JZNOaLu6c7jpmWDMP2vijPmqAOm2haGxhC21oIG7aNM1dCSEMZH209thELk6o0YnLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی مسلمان
اصلا هیچی بهش نگفته بودما، خودش یهو اومد گفت بسم‌الله</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5295" target="_blank">📅 18:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5294">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یه نفر یه چیزی ساخته بود
من دارم یه کم خفن‌ترش می‌کنم که ازش ویدئو بگیرم
بعدشم اوپن سورس منتشرش می‌کنم
مربوط به بازیه
#️⃣
از اونجایی که 3 تا 5 هم برق میره، بعدش ضبط میکنم و احتمالا تا شب آماده بشه</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5294" target="_blank">📅 14:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5293">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5293" target="_blank">📅 13:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اگه اولش ازتون پرسید Can you chat with Jev
باید بزنید No
چون طبیعتا LLM نیست و نمی‌تونید باهاش حرف بزنید
یک مقدار شاید پیچیده به نظرتون برسه اما به زودی راجب کاربردهاش صحبت می‌کنیم و ویدئو هم داریم</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5292" target="_blank">📅 13:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tMmY4O8rwdM8qv5nr20Zf7WRsrmix3Zd30RCI0nc5MPlPnMssP2D1YyJWqE2DsPH2IJEd1wHHZe8e3fsulLkDpUEWnZ2fQyt2QGPBh6wO3I00wyPFE20Lksfdko_5fNhb8_HqDydaU11q7u6p6XOsaTeRk7MXCs_tU5_hBdFC5fu8JGKiw3NYM2bSvGeXEAvyl_k4K_7ukx4i4_MGg1w80M0xQrDgYfyePpkv1AC2j7GYndKOi37QfPJKA1_0N4TGev7DPB246xn7T77EPypsFsn_9i8LHpx4KWKI8kk7E8_jMidhOfxBVOyxFW34xJnm00uiTZS4_1N00J6ej_jVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی بامزست:)</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5291" target="_blank">📅 13:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5290" target="_blank">📅 13:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c5Jh6ZE5Js-GnYM-xNz6KGzLAYi5p8J23zI7xzkgKReyQCbBxxZF18fExF1Da7Y-wnQLRArOQxoltymbcT_sV5Vmq9Kt1HRlTFKd8Vlz2nKcHXTNGogJuYGTxlYLzy7Z8LIP-bJowzOo2iKYK53w3OHDd7Cnp1YGE8yS_okGMjo5fKDJYFRsudHfbq62QBIL9UYye07JKP7q8s_a4AvutaGx9VRRLhLa1k5ptHJdNzosDlDL14RCX1PhMj2ffX7iKrLETv4khoo6pYtFzgVfi4FLhPqe9bsdlFNVcZsr7it0MXSD5Aqhv1fsD71X-zFpsovb507odSFl7_lSmns1Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه‌ی کاری که Jev انجام میده
😂
(سریال Breaking Bad) برای اون نرم‌افزار بررسی کامنت اینستاگرام صد درصد میشه ازش استفاده کرد</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5289" target="_blank">📅 13:02 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
