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
<img src="https://cdn4.telesco.pe/file/Z5vcp_n5lZ7RwExGaDUUb4meZGTeh__6tifoF5qod44DicENwkVnm73wD9uFpuey7ZPFNkPQ_7P8JVUtlhCs0IIgPI9Drib2-2Rz5eYVTSytiwt-NwmmG6qmCfUZq3mjagMp0JI269gkz9TXmyCPh-Pyu17xQrjH93_vni8qmL4qa1QHcNdzHxLjEd5PDAUb2rFe-nZl8KI4gPkB1zDL6RgvFlq8zOwONNNlfJ69wUNlNwEDg1Xmd_nxhTlNAAJ5jUx0ll3n27a-gwsnn_rIuX8CwbCDBmbJICUvbWA0gzunMO_dDRw5ZsLnmGfCU1KuIT7IMjdqhmBEMsxCJIqgXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 20:39:24</div>
<hr>

<div class="tg-post" id="msg-152344">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
حملات متداوم ارتش اسرائیل (IDF) به جنوب لبنان مواضع حزب‌الله
✅
@AloNews</div>
<div class="tg-footer">👁️ 24 · <a href="https://t.me/alonews/152344" target="_blank">📅 20:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152343">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
سخنگوی شهرداری تهران: تمامی درختانی که در پارک جنگلی چیتگر قطع شدند، آفت‌زده بودند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/alonews/152343" target="_blank">📅 20:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152342">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
الهام علی‌اف رسما حجاب رو تو مدارس ممنوع اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/152342" target="_blank">📅 20:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152341">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdBNzBxKtjmmD5GnktaRB4z71_ZUmGGyO9bfEVnNi7P2crEZ0UYTsjqzdT5no3krsBMJ8DsMR4MENSDEgqtdt2QLyBJPGp__UNPUJzI1RjFIyDUqPkqHtCOZoOJ7r6SoIOZR0_6fkl9KynUjOKhUJhYoHZcXUPlHLlOtgomowMiT0RlvmPtRdS2NmW_NAVlGYeArrSj9RpLs3UQToyvsfrOWx6eDZ8hpGyFKAb1MENWWX8UKrsIKExbTVRXg9i2jb4tMQcS5A_bOZnJussCCfEoKOYImUvxWpARoK0JiVTBHY-gCHc6oKoO78qg9gwIh2r1T1rCbWwCmYifC2wdzdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر کشور با الهام علی اف دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/152341" target="_blank">📅 20:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152340">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
یائیر لاپید، رهبر اپوزیسیون اسرائیل در گفت‌وگو با یک رادیو اسرائیلی اعلام کرد که بر اساس اطلاعات در اختیارش، انتظار ندارد پیش از انتخابات اسرائیل جنگ جدیدی با ایران آغاز شود؛ بااین‌حال، وقوع چنین جنگی را کاملاً منتفی ندانست
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/152340" target="_blank">📅 19:59 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152339">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X17W4G7tgDxYmbj_54d_uh-_ALd3ygG74go4IWIXzYzXOQM0vTFIFsU5GK2wQXuY_-dbrLw9SJV4WLMfEHt4nxdNDx1PENvdEBhxB095AOoXXRJvnqzFz-L4kqHh2s4YEp8aOTSicfMkW-FczvZ4RmkKf3f4Bqniua3oz8ktg7oBAnjeRco7E5BkROofiTYKCEbWjHO7DW0V6bBSy_3EJfu31S63Tapj6sKIuaUM_FEFicL48tPHQEJfhckQADqtlbqeoEql6kP5RakUq4ne6z0zbLk4dB8Vxm-naX-deO0Nbh2XUOAKeLPiliWkHfxByruwwheNlEfBL5uF-J27Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید کاخ سفید
🔴
امریکا به سوی پیروزی می‌رود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/152339" target="_blank">📅 19:56 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152338">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ولودیمیر زلنسکی، رئیس جمهور اوکراین:
اگر ترامپ می‌خواهد  رئیس  جمهور  را در اوکراین تغییر دهد، باید بداند که فقط مردم ما می‌توانند رهبر را تغییر دهند.
🔴
من واقعاً برای انتخابات آماده‌ام. ما به دستکم۶۰ روز برای امنیت زیرساخت‌ها نیاز داریم تا انتخابات را آماده کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/152338" target="_blank">📅 19:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152337">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCyfHOfNhmECGlkmT9cL5rTKkdEQ2ISygtldNWMJx7CWn-mjv47sGfTNuAW-arS6LyY_VcUYZlSF4m11GjtjCc-TSg8yWn62A6rkIlI5rjj_tYRtMEhzkP74H39xnt6G9OQAJvQfwxQKBIAEthEIik_IbVD5HcU4Ee4oKzS1axd3Lu9akBjDlrTEFTkLVBn2jsp3A0nb8-1HECLSXZ7j2E7e72Qe5WnLnTTAE1pRpnfSbnmUOcSE41MyfCQGNPe0x9Z2B5BaEy4p5tu7lZPAoT1pTzeHn3v68Qp0uHdXLCmOpasf8GTZIci7Z5IqSu0zv3nJJnyhD-jcac_jLKIp2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تهران، خیابان ویلا، سال ۱۳۵۷...
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/152337" target="_blank">📅 19:42 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152336">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVc9b2HDwV27-mSPxZ4Q8LAG-ZcyJUYX48XucIvurKrJR8RXaAi2wd6v0KfHkomjlhFWfI__WgN3J12yE9pvTo7KlyWOudKzU9Q0e9uvfbGxsvZ5cFtrJv7aZCwIk16RJVHayAqre0RRDhbZQtGJ8Rbo5iII8EmMML-SWk6X3dgJbdIYV0ZRAYrYnTB_z3rTljghkqNd8y4JuoyXf4jjT4qLpReKlqNmzxG96enCkAzDAYW9lTMG7R_9LxIH-DuciRMSG2n8q4Ygw8RCpNDBN6fqOhmz-B-S9yuOxY_C_BhWWl3dFgv9Vc3hGd395bBfxKaUCZU9eXy6_P-fTABfzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد گزارشی با تأخیر دریافت کرده است مبنی بر اینکه یک نفتکش هنگام عبور از تنگه هرمز به سمت خارج از آن، هدف اصابت یک پرتابه قرار گرفته است.
🔴
بر اساس این گزارش، خدمه نفتکش در سلامت هستند، اما هنوز مشخص نیست که این حادثه چه پیامدهای زیست‌محیطی به دنبال داشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/152336" target="_blank">📅 19:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152335">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVoX NET | وکس نت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDllzabb775xTZBC5e9VIIvbWZDimdCBxNDg4-1wCvB7DY-h8QnabPR0rJdOMoMRjcWV3B5aYsm0yEjXxi4SY9qPHyDqxpKlcLlK8xXVfPQTAQ4widvklntYrT48ztL4PnD5jZ71HuLzBAFrW3IDCC5XKUncVDjvzZymddBam4kZ253Xoqj1IK2xg5WpBqfU_mhOWxE_qmMEb4wbWcbtFX1KdtCNwEh1XpY9i8rAcTWoA67NRGTZZcZLU5iKgrA1Tow-Ike_X4aVv-TdLSHDxhI0zFshQGUKBC2YgBiK4Xi24cEzeOFZ6vrZFj6v_yUpt_yJ0a30bVqfPO2CgLklGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پینگ کانفیگ های اقتصادی
🔥
برای خرید از بات زیر اقدام کنید
👇
☝️
@VOXNET_BOT</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/152335" target="_blank">📅 19:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152334">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
هشدار امنیتی دوباره سفارت آمریکا در ریاض
🔴
کارکنان دولت آمریکا شاغل در عربستان، برای استفاده از هر فرودگاهی در عربستان سعودی به مجوز ویژه نیاز دارند.
🔴
شهروندان آمریکا باید از احتمال لغو پروازها، بسته شدن حریم هوایی، و اختلالات سفر آگاه باشند.
🔴
توصیه می‌کنیم وضعیت خروج پرواز خود را مستقیماً با شرکت هواپیمایی و فرودگاه بررسی کنید.
🔴
لطفاً اگر تصمیم به استفاده از فرودگاه‌های عربستان سعودی گرفتید، احتیاط شدید را رعایت کنید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/152334" target="_blank">📅 19:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152333">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
گاردین: پس از دیدار مقامات آمریکایی با یمنی‌ها و اطمینان از اینکه کشتی‌های آمریکا هدف حمله قرار نمی‌گیرند، واشنگتن از حمایت نظامی از عربستان خودداری کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/152333" target="_blank">📅 19:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152332">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayAUBsaZ2G3UD_IX4QD5dxlvcPLBtdT4RrblI4_-wiZwokhjFqd7qgyEI4U2GFXkmubYPf2hN0PswgpupjIUk8XlAXOfVqrDSXLAlkMnK0YQQKcPQL0XJp_6-gTpK0_6HdNMaHthzwQ-JwewvkdFUnsa466W9QdNNzuUUNt8ufrFEk2Rm6DwPaKjJKGp7Gu4DZ4vYz5LR6LyyrEPC8E9GAvQJDHq3mM6DLUV8vFlxAgDa7o-ZZEr3cjoAK292A7v8XlY86ATcbyQCmuzEuoJnZmu3Gnwsw9lwlFs1PFbnUsr1r3fZGqMKhc5TtNmuRCAjvKpkBMcXRvZxdtORNFIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون اصل نود: زمستان سختی در پیش داریم
#کارما
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/152332" target="_blank">📅 19:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152331">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc547ce9c1.mp4?token=MavpXifFbFfGZaJ8tJdJ1sVUOMqxnDB5U8H1eO_gw4XcfksJJkbEtsHbAoWNR-3mRBPsFuf6-hA1bkVaPiBV8MMddSmTgTD3GDDXEAzTEqWoGn4l-1cU4rxByNlzNeIf-KDdxXgDQI6z5doa_yfNcqxkUdIiGy4TLkuQlbZicTrdG40pEeVCxIuSnxT7b5nLmIce-2vyMMSuVv0ooBgAr-CI8v87gVVCsYJOEhJs5LIfZUOaZtckRNQp1f8t2irAEhYY5iriciM6YmvOCYl4NKTaNHRrQ5J87LRnGDtMkp-V82nHxcNDaTdT6nzrYiJdmquTtccCrbqRrhLuLPoXrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc547ce9c1.mp4?token=MavpXifFbFfGZaJ8tJdJ1sVUOMqxnDB5U8H1eO_gw4XcfksJJkbEtsHbAoWNR-3mRBPsFuf6-hA1bkVaPiBV8MMddSmTgTD3GDDXEAzTEqWoGn4l-1cU4rxByNlzNeIf-KDdxXgDQI6z5doa_yfNcqxkUdIiGy4TLkuQlbZicTrdG40pEeVCxIuSnxT7b5nLmIce-2vyMMSuVv0ooBgAr-CI8v87gVVCsYJOEhJs5LIfZUOaZtckRNQp1f8t2irAEhYY5iriciM6YmvOCYl4NKTaNHRrQ5J87LRnGDtMkp-V82nHxcNDaTdT6nzrYiJdmquTtccCrbqRrhLuLPoXrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه هموطن سیم‌کشی ضبط ماشینش مشکل پیدا کرده و تصمیم میگیره خودش دست به کار بشه که در نهایت اختراعی ثبت می‌کنه که توی دنیا، شبیهش وجود نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/152331" target="_blank">📅 19:14 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152330">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
نخست‌وزیر بریتانیا: تلاش برای حمله به فیرفورد احتمالاً در ایران و به‌طور مستقیم از سوی سپاه پاسداران هماهنگ شده بود. پس از حادثه فیرفورد، تحریم‌های بیشتری علیه ایران اعمال می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/152330" target="_blank">📅 19:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152329">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
نخست‌وزیر بریتانیا: تلاش برای حمله به فیرفورد احتمالاً در ایران و به‌طور مستقیم از سوی سپاه پاسداران هماهنگ شده بود. پس از حادثه فیرفورد، تحریم‌های بیشتری علیه ایران اعمال می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/152329" target="_blank">📅 19:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152328">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Buir2s5gkyAq4csHGfAH8yzp7gVw14j_DaEq2wf0Q3laxaEITE51NL-HS54NRrVb2tkLD0Se14adV2DyW1MdaleY-NpGqYOoeNaRc6kDRkVZ7P7JykBrdRiGjWZ-8yC3gm1vhqDb0z-aKiSB2lnQ1V_YejbLrjM3tiTmQ3FobNkPKbKh1AgZeU-ROTJlrR3phDwbRkxw4A7BsYcK6nQ1YOKjIyVHXNBG3npZXJlhvehQbhkUn9OChVA1kVO3j0ED7q_LbDBnQsrImRHQzaLCfx037XX4K5BFcCAjtojSi8FowaZ-1eUoiTuKU9mRl_xANuF6dv8RoHh2H9e4hH1PFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الهام علی‌اف حجاب را در مدارس جمهوری آذربایجان ممنوع اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/152328" target="_blank">📅 19:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152327">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
اندی برنهام: ما در کنار عربستان سعودی در برابر حوثی ها خواهیم ایستاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/152327" target="_blank">📅 19:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152326">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
۲۹ کشور ایران را عامل حادثه پایگاه فیرفورد خواندند
🔴
۲۹ کشور از جمله آمریکا و انگلیس تو بیانیه‌ای مشترک ایران رو در حادثه پایگاه فیرفورد متهم کردن. این بیانیه بدون اشاره به جزئیات، تهران رو مسئول دونسته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/152326" target="_blank">📅 18:59 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152325">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
وضعیت اینترنت کشور ۷۰درصد افت داشته چون احتمال شروع جنگ خیلیه
‼️
🔴
اگه سرویس متصل و پایدار حتی تو قطعی میخواهید سریع تهیه کنید
👇
https://t.me/voxnet_bot
https://t.me/voxnet_bot
با پول یه پفک اینترنتت رو بیمه کن
✔️</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/152325" target="_blank">📅 18:54 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152324">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1rqZ-bds4x1Lz-5sPnjkkMQd4lVovaDlQVHEEV-B3gsVoY8zUqcFXahhI9Z4Aa4Ha2bAHXWewNJ7pCfJzBAx_zSL_g3fL4ewyb9KmhZHLpbb8d1nmjqkOtPn1iCQ12QrV8sjsWBbIVWJXK2t0xTnzYFRE9qRPiWLk-MbIjeolBe-Hqh5s9uukEWvcBcgrCew1FiMRLydTZ9bjCxqwnRNYrfedb3voZvqw1rm5fNHV4KZI0Wm1_zK-nU-vAsaRHHsJni4I6UXvDFX3v6V8nEPSpaeRtq5GGUx9PHri1UbR7QsWxiyia559Jf7lN4SKzJd6CmrQDLVGAE72YBDJzN8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آتش توپخانه ارتش اسرائیل در منطقه منصوری، جنوب لبنان، گزارش شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/152324" target="_blank">📅 18:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152323">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
رویترز: بریتانیا دو فرد ایرانی تبار وابسته به ج.ا را به فهرست تحریم های خود اضافه کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/152323" target="_blank">📅 18:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152322">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
نخست‌وزیر بریتانیا: تلاش برای حمله به فیرفورد احتمالاً در ایران و به‌طور مستقیم از سوی سپاه پاسداران هماهنگ شده بود. پس از حادثه فیرفورد، تحریم‌های بیشتری علیه ایران اعمال می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/152322" target="_blank">📅 18:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152321">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f4e0a1584.mp4?token=AW8e2y-0aeEP2fPHtVuiaEDisc_s7HYKNerhIfh70IFJWyv7KISRXAru-tkoQPCGCe162SaXRsothtREwy3UeraQjr0jOjjeMSCqOB2HxzzmBzq68ujqA9Cp8MtOkzRyRrr8EzE-ADDtOkKh-08awep3fwrysJorkmepOv-bY19lh7nSeD-xy-OyM7MQDoITzJoMcObmFpkpy4J1kfyX0vFDtGSNQJFMqXplfLoKNBWniixCU7M4sCbqBN09Qd8qIU9fhPxYgTCb9b-oHv1hLdxU80732UeK_ZMvHMaHOZ4EsPFQfvv9ocTVTWQGKhFRRBGjJFlotKjG8eI4_TPO1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f4e0a1584.mp4?token=AW8e2y-0aeEP2fPHtVuiaEDisc_s7HYKNerhIfh70IFJWyv7KISRXAru-tkoQPCGCe162SaXRsothtREwy3UeraQjr0jOjjeMSCqOB2HxzzmBzq68ujqA9Cp8MtOkzRyRrr8EzE-ADDtOkKh-08awep3fwrysJorkmepOv-bY19lh7nSeD-xy-OyM7MQDoITzJoMcObmFpkpy4J1kfyX0vFDtGSNQJFMqXplfLoKNBWniixCU7M4sCbqBN09Qd8qIU9fhPxYgTCb9b-oHv1hLdxU80732UeK_ZMvHMaHOZ4EsPFQfvv9ocTVTWQGKhFRRBGjJFlotKjG8eI4_TPO1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کوروش احمدی:
ترامپ در توافق، تحریم های اولیه و ثانویه ایران و مشخصا تحریم ها علیه نهادهای ایرانی که بعضاً نهادهای سپاه بودند را برداشت
🔴
تحریم پرداخت دلار در ازای صدور نفت از مبدا ایران را هم برداشت
🔴
شما وقتی این لغو محاصره دریایی و لغو تحریم های نفتی را ازش دیدی، باید یک مقدار به طرف مقابل فرصت بدی که ببینی آزادسازی پول های ایران را هم انجام می‌دهد یا نه
🔴
آمریکا در مورد لغو کلیه انواع تحریم ها علیه ایران متعهد به لغو شده بود؛ خب این خیلی مسئله مهمی است، همین که اصلا وارد ادبیات رسمی آمریکایی شده قبلا غیر ممکن بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/152321" target="_blank">📅 18:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152320">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
آش چه شور شده صدای خضریان هم دراومده
🔴
رييس سازمان اداري که از دوستاي رييس سازمان بورسه براي اينکه رفيقش رييس سازمان بورس بمونه الکي نامه زده که استفاده از اين پيرمرد مشکل نداره.
🔴
خضريان پایدارچی هم فهميده و ماجرا لو رفته نوشته:
سازمان اداري و استخدامي غلط کرده براي افراد مجوز صادر ميکنه/ سازمان اداري غلط کرده قانون ممنوعيت به کارگيري بازنشستگان رو دور بزنه/ مگه تو کشور جوون بدرد بخور نيست که افتاديد دنبال بازنشسته ها؟ هيچکس تو کشور مخصوصا سازمان اداري و استخدامي کشور، حق نداره ديگه با نامه اداری، برای خودش قانون بزاره
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/152320" target="_blank">📅 18:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152319">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
تتر 260هزار تومان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/152319" target="_blank">📅 18:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152318">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Djfz2pyNiOiOsYRD6ZzHOy25h36UGtGVzJZRTUEUF22n89MNIZ7UxzYjjwByWFpjMTZ0UqOROcRjFIYtdZwRvmLkvY-09ZXddI2SF-PRK6XE-iidHJ3TD9FYARtnAFfdfjPUHx5_TzakY2UHtkkaTSm_Wcapl3ic9LxwDOiKc-bJV_bjroqinKQq6joH3XtDMAuvGoFTJ8MyGercgbd8kkQsnVz1sFRn2jDqY6sHbU6DeeGLUpzkGdyFtFwEvpif8ZjDeQ3WPpIZXnq1hLdZIvKaGpympSGiy0sWk6J07NN8DpT6_0KXus5TOZLyB4CU6f8oM9_Rgl-y9IakhZAkog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ظریف:
زمین و زمان را برای خود دشمن کرده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/152318" target="_blank">📅 17:54 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152317">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏
👈
معاریو: برآورد نهادهای امنیتی نشان میدهد اگر ایران [به اسرائیل] حمله نکند رویارویی به بعد از انتخابات موکول خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/152317" target="_blank">📅 17:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152315">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GTo1NhEQcswl7nmffl-4pBOwpms9DN19CNXIetRCaS3dlC2yewelfxoNBA-S9xQU_ULMx6NX3v3K7uMPphoibqPl6ZkgTeFRO_wD7UQuiTfm2-fBsOfrmAX0s_TAbqKgzliTSbTqY2_lsFutV-cdI26m2u5tsXgP5nE9l2YN3bT6xMibrHIYZO1srHXqPdyMAlA_ip0ZmkgDai4MxbuSZep2E-puDp7TY60sRW5x9q-k7NuTkmKSNRYQUU0Xk8kaIRcHm5ObWXjk1A1rpNYLHFc710r_itQmSoi0OsUMcLHlqbOeAb8LwgLCT-Rj5t3CWT9uisZKmmSBIBv6nmVmrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oEceuaTIkIagIsUdD1FOArJE34hs_ESS7y35zBmYWvpzOFzLu5-tnWdGtZAX2f5TLNweHP0L5MlTY3Q8DB0WBuEDI2vib7rfiEGW0IZ3q31YUpGA1iomC4s1_7VMDRlnKZd9VetCJazfjcx_jj9iZcvFNxjXO-kZ_-rgHmc29t8eJIO5A_ienr4EkJIbPwc9sLHS6RtJzUnf3gvANh2zPoCKz0jF4KIEB9aSe2KGoGYQ9rs0_5dPfB-ubrAMxogc7SjWruD3Su-uhatLtybViFGZYQ8tXjFF4y5DEVO8T_1ApTlU2B_1yMDf9wJ6DeLPs4mD-vqWxa1w4zHnqwCFUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
چندین موشک بالستیک از یزد، اصفهان و کرمانشاه احتمالاً به عنوان بخشی از تمرینات بازدارندگی موشکی در حال انجام پرتاب شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/152315" target="_blank">📅 17:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152314">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99ec666f45.mp4?token=YJhUC2Lkohwi2tBVuk9M1-MCTQmMf6_jijnVbAhSOMw5JTDrgTLcx4Oytj513W6vy1N534NyNBRrRgrMdG24es8zGXd-RIpQLLyw1BIIaQJqvZ-RiEJVHoZ41zWUYGLdG0kCtTXJUno21nE7UelOxzS3Rx2UzddKtxxDhfPkSRAsdrPTYflxCLFzhSNjXWcNHJyMKCOLO3vHbMoL3XLSmlgRcZHgvR0LnyFD1LFNOCnqnIW2jPMcSKocSAUWAMjeQnM8Th8dJMuQNf177GyBZvuxi_CTfOtmb_yIVOtEi6h1XJOW2EVWPi22aQsjmqAh-byjzhwEkAOQ6Hsoi4LobA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99ec666f45.mp4?token=YJhUC2Lkohwi2tBVuk9M1-MCTQmMf6_jijnVbAhSOMw5JTDrgTLcx4Oytj513W6vy1N534NyNBRrRgrMdG24es8zGXd-RIpQLLyw1BIIaQJqvZ-RiEJVHoZ41zWUYGLdG0kCtTXJUno21nE7UelOxzS3Rx2UzddKtxxDhfPkSRAsdrPTYflxCLFzhSNjXWcNHJyMKCOLO3vHbMoL3XLSmlgRcZHgvR0LnyFD1LFNOCnqnIW2jPMcSKocSAUWAMjeQnM8Th8dJMuQNf177GyBZvuxi_CTfOtmb_yIVOtEi6h1XJOW2EVWPi22aQsjmqAh-byjzhwEkAOQ6Hsoi4LobA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شامگاه یکشنبه تو میمه اصفهان مردم برای تبدیل شهرشون به شهرستان تجمع کردن. یگان ویژه با ساچمه و سلاح جنگی معترضان رو متفرق کردن و تعداد زیادی زخمی شدن. میگن چند نفر هم کشته شدن و بعضی مجروحا رو از بیمارستان بازداشت کردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/152314" target="_blank">📅 17:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152313">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
دلار میریره یا بالا میره؟
تحلیل عجیب نخبه ایرانی
👇
https://t.me/+ViT7_yfzcKRmOTNk
https://t.me/+ViT7_yfzcKRmOTNk</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/152313" target="_blank">📅 17:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152311">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GKoVz4TruhAYGuXl54Qr347ou5DBHqxKnRG0Dg16MnigEp_AqDi-gTUWZabKQxvFqi6ReVI7poV14j-K64WOzZEXrni4OFQEf9zyU44gJLvob_W2tn2oSS6z82INKZGDZVcX2M-9nifWBQeOvsisdGiDRSnkUA8-z3_nicxYTQF8nSxxSvvEr0FVVJyccQS5IMAQDL_WmSpUWnvtuj0FKWl051v1xQP7NlnYSqcq1lmbY-PSm37zL26w8yUesCcmmzzPHYByT4uiWxQNEsOxCXNOjx2_V5CV6iOECe5A-eiMIaZARpXMzwFnn8P2FYNatwQwvQNlJFKl0vLFwr043A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XBdKB5AdkE0l_O7BQk7whHCcXgMDOKmUO8hmJWiTeoAQS635L6ap-3iAzA_-CRH6nNDBBmA5xN4cYI86ugO1kBortTSMxshfOuoP6ZSPjCXKkEx-C3Poyn5Ictv5A6jsuwUbiUBhB9A0NC7t4S4Dr-X7oXcjSi3Kg7dPohUlYiJF_efGTaby6MuUmi1U94d2TBF1OLOvZGpBQMhFMBIzHGKl3CEZvxBEAi0zUlCtceXvwyv2Qq5FOlVtlOSR3iZO-M8ePWS3A62XCdMHsxjWJ7Ncd-CHGaockKA0HdQYDcOQ5NdHD8xgEvni-sKbovVHkidfNrs2W97EHc_Ef94lTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از ازمایشات موشکی سپاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/152311" target="_blank">📅 17:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152310">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7Y0CmVqG3rsL33L6xHvKvkSEXbZjYxSwcYSKGfD8i9pCuimNEPHEfsSY5evGQ-62Xl2KdvkgGmZ-J3oROiP0xPQKF_e10EAvvrNlHuuK9eHTZ7LaqXd62cpEcMphcqRCmh7uC-AThAis0ZQxM6hllF_ssVCFEqRed_iKeM1MEncxGbQtxu-F_wUDJGI4BSl3hWjevLCEw7n5j7OOuBjiY_fecKNMJhJflmoo5uDKhTGtGFRWq97DNGZZNLDTcwonBDPwvfKW-tgYffYoFbKbDOu9MQFyWDK2AkcIUhK7AJw-DkK6dGNbC1FZ5wPYH6WCvpF70q6w1pImBiugKeo7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏هیمتی: دلار میریزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/152310" target="_blank">📅 16:59 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152309">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دوتا پست بالا از دوتا زن ایرانی با دوتا فرهنگ و محیط متفاوت
خیلی جالب اما غم انگیز</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/152309" target="_blank">📅 16:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152308">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/657dc51454.mp4?token=hlk7H1KYvRB9mIjXSugF8aC3k9Rsu8pwVghIdFcZL-5MW_3tYnoHksp8j79FF3vcu2Jh8OsOar6HnPI-NqAB3qAK-Z28UEI8ykxeKBeeGnnYa475ogUoiJWv5oVYz6Oxt55pCa2v0uO4q54ngqGlG9DV_SFIgemKDhbVnTPUTheAU5wiNu9oc2t4BsW6QxyDpVas4Z-oOfHmmzzlfDtY1FcKI6zYeg1Uhi6cWxL_gORpvhW4j3QF7UHyfZcoyfFYbMmfqf1-wkfvCzeJP3W4OdNuwUpi86qZMUOYLWGF7cIz6vo4y0nBS6-VQkWPcqwL2JcDv_ioJeXcM4C3RqlYaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/657dc51454.mp4?token=hlk7H1KYvRB9mIjXSugF8aC3k9Rsu8pwVghIdFcZL-5MW_3tYnoHksp8j79FF3vcu2Jh8OsOar6HnPI-NqAB3qAK-Z28UEI8ykxeKBeeGnnYa475ogUoiJWv5oVYz6Oxt55pCa2v0uO4q54ngqGlG9DV_SFIgemKDhbVnTPUTheAU5wiNu9oc2t4BsW6QxyDpVas4Z-oOfHmmzzlfDtY1FcKI6zYeg1Uhi6cWxL_gORpvhW4j3QF7UHyfZcoyfFYbMmfqf1-wkfvCzeJP3W4OdNuwUpi86qZMUOYLWGF7cIz6vo4y0nBS6-VQkWPcqwL2JcDv_ioJeXcM4C3RqlYaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دختر شایسته ایرانی به مرحله ۱۲ نفر پایانی رسید
🔴
حدیث ستاری، دندونپزشک و مدل ایرانی، توی مسابقات دختر شایسته 2026 تو تایلند تا مرحله ۱۲ نفر پایانی بالا اومد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/152308" target="_blank">📅 16:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152307">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4Gbjy3QI8OKB5vWN7Zc0ymujSKSU8F9Pemby5CLHPTbnigRXcv6CWz1AyNDCWXi3XwgVCNyQN-P3w-OkKFp3LKH0tJJDgIook0fS65stjb_y09bTop3NKjqhsXg29LHTfNyW5uzLkirZE5tPSR3CeV4xVhel-NHRcyItffmiLITCKHaMWXVXoZfz_IPqgdF-oCw4dgWYc8GjSFy6i6RtCx62EZ4CH-LDXuWrYy4XG_eGdoK9-JbAn4pGre-RNoFbsLIndnABaa06VS0ipqL8biapqTcBJggezpzDhcxEgWuOTZJf8-FHnHFHltQwsNYa6PVlmfoQBAMyoqqoMbDtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قتلی هولناک در قشم
‼️
🔴
مریم یارمحمدی زنی ۲۸ ساله اهل روستایی در قشم بامداد ۱۳ مهر توسط برادرش و با کمک شوهرش و «با انگیزه ناموسی» با چاقو کشته شده و اندام جنسی او بریده شده است..
🔴
شوهرش ابتدا بچه‌ها را از خانه بیرون برده و سپس برادرش شبانه به او هجوم آورده و با چاقو، پستان‌ها، واژن و گردن مریم را مورد اصابت ضربات متعدد چاقو قرار داده و به قتل رسانده است..
🔴
هر دو بعد از ارتکاب قتل بازداشت شده‌اند اما خانواده مریم گفته‌اند هیچ شکایتی ندارند و مرگ حق او بوده است..
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/152307" target="_blank">📅 16:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152306">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
فوری/بافل طالبانی رهبر اتحادیه میهنی اقلیم کردستان عراق از آغاز روند خلع سلاح و اجرای روند صلح احزاب مسلح کُرد ایرانی خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/152306" target="_blank">📅 16:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152305">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
وال‌استریت‌ژورنال: تلاش حکومت سعودی برای تبدیل‌شدن به قطب هوش مصنوعی اکنون با خطرات جدیدی روبه‌روست؛ چراکه دیتاسنترها جزو اهداف حوثی های یمن هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/152305" target="_blank">📅 16:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152304">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u8brNJwuSpPAiT2n3i1_b34B50RLIEDA48qXsqQVNo6dyEIRunmjXn2JVN8tnGvPfyYn6v3fN7EB9Q51n-f0tEmlXeZfkCeiegFtkfqSBgEx2HnL780y5LRVecWsU4zx0voQfeC89XQeacmf-F_LaGp-v4LJ44WzLFhZ5ZiY4uslkGdcBC2ZFXfVZe2nFq3Q91dSBxbgzocwLTheiRdLrxJ7fcfW6UTkm8WTX5vPO66qmRh8CmAM59vUxZ7luvpMMkGOz2PQJ4cYOJ_5r3UveEkiZVJugtIZarPq52ZRfH3RR76BGGlkmB6CMG5gHnwUomloOYQBuAua8T6Du7jFAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اینترنت ایران نسبت به هفته گذشته 70 درصد افت کیفیت داشته، کم کم به مرحله ای رسیده که فیلترشکن های رایگان و پروکسی درحال از کار افتادن.
این یه نوع پیش آمادگی برای قطع سریع اینترنت در زمان حمله و آغاز جنگ آیندست.
از دیدگاه مقامات ایران جنگ قطعیه و بین بازه ۲۰ الی ۳۰ مهر جنگ ایران و آمریکا در ابعاد بسیار گسترده تر از جنگ ۴۰ روزه آغاز میشه.
🔴
ولی این سری قطع شدن اینترنت همزمان با آغاز جنگ قطعیه.
🔗
اینترنت پایدار و متصل
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/152304" target="_blank">📅 16:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152303">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4daef3062.mp4?token=uy6PSVp8QTfoUI8GB-0Cp90bapeXuvDuKb5V-gM6odkpOVErjvYKQ77MxKuhfd3aviqFtUI4ACXMAnW85rOU7DVccJ0cU4vd6n5TmHw4t78M4kCVkg2M03qhAMFm-f-LEdGmZL8zLLeK5UB8mdZvIvS9bxzwQwy52bbZdVleFvN4BVvb4a591UgC9MJvAPb0Vi_59FomVPFhUu229MBZMHC2ifcjT15EVL6FkVd9M7m1E2C0liu9Cb2oIlSYOKyzelmwSxwEmuOLuU0fNcje6PqSo7YYlqs9JEGFHQHkGkVgx4dr_OSnxLC03uLyWmlqD-tKYQj9ZqqJ1FQ95fRnfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4daef3062.mp4?token=uy6PSVp8QTfoUI8GB-0Cp90bapeXuvDuKb5V-gM6odkpOVErjvYKQ77MxKuhfd3aviqFtUI4ACXMAnW85rOU7DVccJ0cU4vd6n5TmHw4t78M4kCVkg2M03qhAMFm-f-LEdGmZL8zLLeK5UB8mdZvIvS9bxzwQwy52bbZdVleFvN4BVvb4a591UgC9MJvAPb0Vi_59FomVPFhUu229MBZMHC2ifcjT15EVL6FkVd9M7m1E2C0liu9Cb2oIlSYOKyzelmwSxwEmuOLuU0fNcje6PqSo7YYlqs9JEGFHQHkGkVgx4dr_OSnxLC03uLyWmlqD-tKYQj9ZqqJ1FQ95fRnfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بالگرد های اسرائیلی در حال انتقال مجروحان
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/152303" target="_blank">📅 16:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152302">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل: ۲۰ مجروح در حادثه در منطقه الجلیل، حال یکی از آن‌ها وخیم و حال دو نفر دیگر خطرناک است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/152302" target="_blank">📅 16:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152301">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
سفیر پیشین ایران در بیروت: پیجر من قبل‌از انفجار نوشت یک پیام فوری دارید!
🔴
اولین‌بار بود که با چنین پیامی مواجه می‌شدم؛ روی صفحهٔ پیجر نوشته بود که «برای مشاهده پیام دکمه را فشار دهید» و به‌محض فشاردادن دکمه، پیجر منفجر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/152301" target="_blank">📅 16:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152300">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
نتانیاهو درباره ایران: کشورها، حتی آنهایی که به ما حمله می‌کنند، به آرامی و پنهانی می‌گویند که حکومت ایران باید سرنگون شوند، آنها ما را خفه می‌کنند
🔴
ما مطمئن خواهیم شد که آنها سرنگون شوند. آنها سرنگون خواهند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/152300" target="_blank">📅 16:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152299">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
عربستان سعودی به دنبال افزایش ظرفیت لوله‌های نفت به ۱۰ میلیون بشکه در روز است
🔴
عربستان سعودی در نظر دارد ظرفیت خط لوله نفت خود را به 10 میلیون بشکه در روز افزایش دهد و توانایی خود را برای انتقال نفت خام در سراسر این کشور تقویت کند
🔴
این طرح ها ظرفیت خط لوله شرق به غرب را افزایش می دهد که نفت را از تاسیسات تولید در استان شرقی به بندر ینبع دریای سرخ می رساند
🔴
گسترش این شبکه به عربستان سعودی اجازه می دهد تا نفت خام بیشتری را بدون اتکا به تنگه هرمز صادر کند، تنگه هرمز که در طول درگیری های منطقه ای با اختلالات مکرر مواجه شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/152299" target="_blank">📅 15:56 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152298">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
شبکه ۱۴ اسرائیل: ۱۲ نظامی اسرائیلی در یک حادثه در جنوب لبنان زخمی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/152298" target="_blank">📅 15:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152297">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72b594a539.mp4?token=NhkmcFAw4qX3w5e3RDjy87_ICR0GGHf8Rit8_z7OChQABi8VkBAh4QGyJHnnTbzdStPFgpSKzfB4UsT54HvFP5hA9Tq-5HHusuxCJ62VwEiUgBFov6B5q1nmBjxeOTMZVSuz8LMB91lNgukUypTQvI0ZmPX2fS-VpeGP9LmEqllWJBlHnijoEFgqZbtVSxaZys38lUW9bX4NEywDryj0XqD_sqQHtnScmkjWJjF63pMwKQve26mhr1J9jVLwmN2kfK6KK0TMM7rhQCNUfaQbT-N9yNpKCbxEVZHyBkdPC1JW14gmBhA7HME7Ak9aGHzcFKhrCOO3AzIyaRki5P9JiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72b594a539.mp4?token=NhkmcFAw4qX3w5e3RDjy87_ICR0GGHf8Rit8_z7OChQABi8VkBAh4QGyJHnnTbzdStPFgpSKzfB4UsT54HvFP5hA9Tq-5HHusuxCJ62VwEiUgBFov6B5q1nmBjxeOTMZVSuz8LMB91lNgukUypTQvI0ZmPX2fS-VpeGP9LmEqllWJBlHnijoEFgqZbtVSxaZys38lUW9bX4NEywDryj0XqD_sqQHtnScmkjWJjF63pMwKQve26mhr1J9jVLwmN2kfK6KK0TMM7rhQCNUfaQbT-N9yNpKCbxEVZHyBkdPC1JW14gmBhA7HME7Ak9aGHzcFKhrCOO3AzIyaRki5P9JiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی: آنچه در کرینکی رخ داده، نسل‌کشی است
🔴
ولودیمیر زلنسکی، رئیس‌جمهور اوکراین، گفت روسیه در منطقهٔ کرینکی مانع دسترسی کودکان و بزرگسالان به غذا می‌شود و این وضعیت را نسل‌کشی توصیف کرد، نه قحطی
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/152297" target="_blank">📅 15:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152296">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQcuGyntZMLFtWoEhncsKkOH5v1dK9dJoKIMAi6ugXkGcDZ-GbeGvrPGP8W6ZqgnSjJaSXMSiCyAhMEUqFPHVE2XtrMgYzCROzWNN4WwAcpkn8XfE_Winj3RaoTTTaRXO23QZiPIMVuf2Oj8Gzj99M2dN_c3Eq4AxGdy2K2j1bzisHZRHzso38_XoNn5NP6pDqJa3boUu9pZ1Qz4j6oCUeP3PITCB53-FqI7F97wqG-nMkluAweYfN56kDEjoytGQdoEDHUVxP9H0KRTzJmyVzzkfJwAqFtU9Y25q08bj3lEJ2LW0341rsBvJJvNrHOwurhOFOxvIBPtcuBQ6GtewA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میرسلیم:
اینکه پسرم با مجاهدین بوده به من چه؟ مهم اینه توبه کرد برای همین اعدام نشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/152296" target="_blank">📅 15:38 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152295">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره
👇
👇
https://t.me/+ViT7_yfzcKRmOTNk
https://t.me/+ViT7_yfzcKRmOTNk</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/152295" target="_blank">📅 15:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152294">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
وزیر پیشنهادی دفاع: تقویت پدافند هوایی را با جدیت دنبال می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/152294" target="_blank">📅 15:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152293">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
هواپیماهای ترابری نظامی آمریکایی به صورت پی در پی با حرکت از آلمان، لحظاتی قبل در اردن و اسرائیل فرود آمدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/152293" target="_blank">📅 15:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152292">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geJT7AHwm42NIvnWQfXDZwsJVwdO9pbWENhfEILvCu6JoVllLWzxzDkyPUHgUvjDSQ6YgrMb5GmhK7W3ahrYOTMkvfZ76eLzIkxptkjqG-6wI-L5h4Zwpcm1pfAmn_8RxHVxvglnYjTLmrGNnsbasVdUqkkMI7qYjj5Y3uMvwqehP7zLN0MQ9A0vzWJAPkzEyO5QPqLfZpAI_lc-0oe8Nk49o7reNKmeMqSCZEYXCtDR7DBh_nRdtMg_X0hZ6OQ5gdEMCwslWVxX3WIvN8dTlxvUbgRKKTjKXPqOpzAEny0skm-3jAvO4hUNaDiQ0nVYbyhdRkzdPGvn_uLz6WzRDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برندگان جایزه نوبل اقتصاد ۲۰۲۶ معرفی شدند
🔴
آکادمی سلطنتی علوم سوئد: رابرت هال و مایکل وودفورد، دو پژوهشگر دانشگاهی آمریکایی، به‌دلیل پژوهش درباره «مبانی اقتصاد خرد تثبیت اقتصاد کلان»، برنده جایزه نوبل اقتصاد ۲۰۲۶ شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/152292" target="_blank">📅 15:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152291">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56777f13a5.mp4?token=FHtUIueguYULaDxWhklX0eTHCvuw7JxqEtSWIs4kGOC0dZU3nEVHW7Sbr55QZU8hM76EbSe-3IIUQuHuk7Zye_5xpZ-cX82W5sbc8k8DK4SOre8sf6uRKLYf3tbG4I1zX0PWsUQdKanXiO_erEfirGcIa-6pcPYDnuMn-DW4avoNEe4AKlqDFHJ2vNEX57w77rCZAEB1dxR-akPI_ShM5KBP7QuWMdxR4iJekcMMtURh3CJSxd8XBczEsqwXc2mnVcjYIC51yIsCH5ov3wC8W4r7XGG0m4YmBw5s_E5aejGSVeWQDNZ_Vu0sSGfxbPB4VNnjegiH0S2eAoiKoP1JAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56777f13a5.mp4?token=FHtUIueguYULaDxWhklX0eTHCvuw7JxqEtSWIs4kGOC0dZU3nEVHW7Sbr55QZU8hM76EbSe-3IIUQuHuk7Zye_5xpZ-cX82W5sbc8k8DK4SOre8sf6uRKLYf3tbG4I1zX0PWsUQdKanXiO_erEfirGcIa-6pcPYDnuMn-DW4avoNEe4AKlqDFHJ2vNEX57w77rCZAEB1dxR-akPI_ShM5KBP7QuWMdxR4iJekcMMtURh3CJSxd8XBczEsqwXc2mnVcjYIC51yIsCH5ov3wC8W4r7XGG0m4YmBw5s_E5aejGSVeWQDNZ_Vu0sSGfxbPB4VNnjegiH0S2eAoiKoP1JAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ماهیگیران عمان موفق شدند خدمه یک نفتکش را که مورد حمله قرار گرفته بود، نجات دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/152291" target="_blank">📅 15:14 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152290">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSEooZE0hoduVNbXiFDovn_Uv2AjjF295uFDjX_Y2g6ftFe4ym5nqQgELpdezEY5T3iQrrjwAMtGlmv0fLATEfcQDZzEeyk0mk_4Bckbgt6adyOo3I3T7-vxizqN0ha9_9ykCNQRejaksW1U2qY4KYWDJh6GU-gCHn1LygPH8a3KmnG5BUPRe6EcnMGtRccauCmX7hOig_44rAZUcnLlVZR7Fgerl3hUAK9jlnDW_g_TMvO6i0suSDpaZNASA3sBGtzkUFqA0pjp12oVf-_SV_EBLwB5ddaoiJ6nkN5qfuxszeqiCQR7luvCtw-m6HvAEAhzsQZhbUJWZ7Hs1myXfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
3
هواپیمای باری نظامی آمریکایی به سمت خاورمیانه در حرکت هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/152290" target="_blank">📅 15:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152289">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
وضعیت اینترنت کشور به نسبت هفته گذشته 70 درصد افت کیفیت داشته است، کم کم به مرحله ایی رسیده است که فیلترشکن های رایگان و پروکسی درحال از کار افتادن هستند و احتمالا یک نوع پیش آمادگی برای قطع سریع اینترنت در حمله آینده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/152289" target="_blank">📅 15:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152286">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhLKpk2hYPkXg-OHWCKn9Br8QlKzHsPWt7VixrFS2_m23lZFcCsk7WLIua5qcuvQrm7VKaPHgncyMxUtUv-rOdsaHnk8MMk37Dx69dS1PMsBwj4LMtThfXuHW190ZRoi4UEKn409C7j43cHTzh30DANriXKyLqTCOMV2M_VP9gEM5LOlEiYc1EwIb9OIxf3Q1DVspoii3Kw_rCyAAkIfs5mtdgnqtf9DuE8VeOqiGdGk35D0QHQSpK18FDJKZ4KvaKpiJvCb4D9oBWXIpOCA_LpQ0cfHUIdAs09PbkmeMAY0eaP7F2Mm7FCvhV-0sY3WMGELM7BDcUBQs0aveB_M-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طهماسبی،مجری: والله قسم حاضرم برم ترامپ و نتانیاهو رو بکشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/152286" target="_blank">📅 14:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152285">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
شریعتمداری : درصورت جنگ مجدد کابل های اینترنت و فیبرنوری تو خلیج فارس رو قطع میکنیم تا علاوه بر اینترنت ایران، اینترنت کل منطقه و جهان قطع بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/152285" target="_blank">📅 14:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152284">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
رسانه عبری معاریو: برآورد نهادهای امنیتی نشان می‌دهد اگر ایران اکنون [به اسرائیل] حمله نکند، رویارویی به بعد از انتخابات موکول خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/152284" target="_blank">📅 14:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152283">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
سخنگوی کرملین گفت که اگر اوکراین واقعا خواهان برگزاری انتخابات باشد، روسیه در روز انتخابات هیچ حمله‌ای به اوکراین انجام نخواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/152283" target="_blank">📅 14:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152282">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">با پول یه پفک یه ماه vpn بگیر
/
کلیک کن
🔗</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/152282" target="_blank">📅 14:38 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152281">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
رئیس آرامکوی عربستان: ذخایر تجاری نفت جهان به کمتر از ۶ میلیارد بشکه رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/152281" target="_blank">📅 14:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152280">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZH-7ZMIUsu5o0vVHdkYYg_JNPZ5omPDcuEDJwOYaLjdYQWmh0Y7BjxgD-EJIrXZMqhaSo7uHkX0L44IumkRLayuDJEki4r2teUnb2v3tXcu8WP7QgLB3mS7IhoAvV98ZBlM_9U0uQ3f1VT092ibhzHAIUkBgkghA_5nzwy2IIiL2ocGbs4yI9H9M5AKXuVBEdVLz_ojswlbHbFkdd-6zmEV48zApLB6PRjQzWHKVBROOdWGyLIN2OIPAfLzirVUG0tgsmmgiee2oz_9D3JB1bV8Q4xG8AXniqTRys1lh00q909FcBDJcPwRUURrnwxoduDk1SjNDgbzzXBHgNOhxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر وایرال شده از یه آگهی ازدواج تو خیابون
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/152280" target="_blank">📅 14:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152279">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5938a46ea0.mp4?token=LPkVNeRjTAnTODucv1cJsXt5w4O6acTKOVhhYFkqMXFd_RakSoRuJKie74F4muMhNbzdokDqyAtbgNCnx9UxaAA01QwQpunY-O0uvN5od77ymxb4qwjVNZzk3RpzJEUZsgHj8p-WDqpYyStIrjIkfJeS6sOVV2_m1brovL-Yk0r0xp7HhAVapNwLwnDuDi7gUM9BHCjMwpa5fROlMio9cKDq3_cpgWpgDTf-L6bC5Mr4pU8268vB9foV_1dmZAvkr2Qyxqb8ly17lWSx_rL5fxHCrc_2BwcvuwbZlQrmdpOiopgvjF3mPZg-bdlxELNWMXuqBGdbSWmnZJOtjvVT-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5938a46ea0.mp4?token=LPkVNeRjTAnTODucv1cJsXt5w4O6acTKOVhhYFkqMXFd_RakSoRuJKie74F4muMhNbzdokDqyAtbgNCnx9UxaAA01QwQpunY-O0uvN5od77ymxb4qwjVNZzk3RpzJEUZsgHj8p-WDqpYyStIrjIkfJeS6sOVV2_m1brovL-Yk0r0xp7HhAVapNwLwnDuDi7gUM9BHCjMwpa5fROlMio9cKDq3_cpgWpgDTf-L6bC5Mr4pU8268vB9foV_1dmZAvkr2Qyxqb8ly17lWSx_rL5fxHCrc_2BwcvuwbZlQrmdpOiopgvjF3mPZg-bdlxELNWMXuqBGdbSWmnZJOtjvVT-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ورود حوثی ها به روستای الصراری در منطقه جبل صبر، واقع در شهر تعز
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/152279" target="_blank">📅 14:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152278">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
کانال ۱۳عبری: نتانیاهو شب گذشته در نشستی اضطراری با مقام‌های ارشد امنیتی ،حمله نظامی به ایران را بررسی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/152278" target="_blank">📅 14:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152277">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
وزارت امور خارجه فرانسه: حملات اخیر علیه عربستان سعودی منجر به زخمی شدن جدی یک شهروند فرانسوی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/152277" target="_blank">📅 14:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152276">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d96f3612.mp4?token=QYMeGd5jd6Aa5Mq56LYSy3uAitly4aWWEmXIQ9mwVPRtpxGTtqa3jn2Wbzheuyg6sXl2lNiq75lRe9CI5CRq_dPM-hsDsABERQfiP8cW6yELQg2o7Votoh1tYvI_xTgVQ8pboX0J4yf-tG72Vb35CjG2WchnvVkrzP7bFwMz3fsTtrPK0gp3FpmK8Wa24F5PrAy0duABXQs9jF7fWhutak_AA-qBry5VgfVJYwFUhzZ6o2o2UCaMJjfDWSK-l6elX7bPIs_6sa72FhkUd2jSngUhriLweQDbxFSYVs96squso_rgwdVcWmxbDvSRXcl_OYC1_e5fUGqCgK4ScCZb6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d96f3612.mp4?token=QYMeGd5jd6Aa5Mq56LYSy3uAitly4aWWEmXIQ9mwVPRtpxGTtqa3jn2Wbzheuyg6sXl2lNiq75lRe9CI5CRq_dPM-hsDsABERQfiP8cW6yELQg2o7Votoh1tYvI_xTgVQ8pboX0J4yf-tG72Vb35CjG2WchnvVkrzP7bFwMz3fsTtrPK0gp3FpmK8Wa24F5PrAy0duABXQs9jF7fWhutak_AA-qBry5VgfVJYwFUhzZ6o2o2UCaMJjfDWSK-l6elX7bPIs_6sa72FhkUd2jSngUhriLweQDbxFSYVs96squso_rgwdVcWmxbDvSRXcl_OYC1_e5fUGqCgK4ScCZb6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی از انفجار در اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/152276" target="_blank">📅 13:59 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152275">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82068f2d9c.mp4?token=d9Kb2E16e5J_zVNuEsI0U_LQ9jLnQn1rDdq4QJoH-3taNptZzuwb_oMOODkTIASzhbrgbXiwV1gwY86DPJrQV4CZuPuIpKtpselRrEM3Y2dkKtpVcKHKVHCyf9HfS70Lz4Fn-C-gezmCiYzGo-mkWsIuuxHLeNQFrqJvVttsvL7delUYQNKnvO8IiSZ1ovTcoUUI8nQHCmB8gMck_T3E31EUsl7vNk5JGoraXLl-OrTJxwxFKcjhX0K5krTZwIkrVvW-G_qZV5NqmbyT1KR9HEA9bmBZ5dhc-EGDR2mPVl68bRpfQsoc6j2cYqczr3W2H06cyy2kACAh__9mULPtzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82068f2d9c.mp4?token=d9Kb2E16e5J_zVNuEsI0U_LQ9jLnQn1rDdq4QJoH-3taNptZzuwb_oMOODkTIASzhbrgbXiwV1gwY86DPJrQV4CZuPuIpKtpselRrEM3Y2dkKtpVcKHKVHCyf9HfS70Lz4Fn-C-gezmCiYzGo-mkWsIuuxHLeNQFrqJvVttsvL7delUYQNKnvO8IiSZ1ovTcoUUI8nQHCmB8gMck_T3E31EUsl7vNk5JGoraXLl-OrTJxwxFKcjhX0K5krTZwIkrVvW-G_qZV5NqmbyT1KR9HEA9bmBZ5dhc-EGDR2mPVl68bRpfQsoc6j2cYqczr3W2H06cyy2kACAh__9mULPtzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هو شدن بقایی سخنگوی وزارت خارجه در اجرای ارکستر آرش در سالن اسپیناس تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/152275" target="_blank">📅 13:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152274">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
محمد بن سلمان، ولیعهد عربستان سعودی، از بیم احتمال تلاش انصارالله برای ترور وی، با تیمی امنیتی که شخصاً انتخاب کرده است، مدام از یک پناهگاه به پناهگاه دیگر جابه‌جا می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/152274" target="_blank">📅 13:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152272">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qIcAcUcWT2XJQSWtZINNXfUBRmAsmoJWaz2wM1pn6dCQQa_A1mxQSJWcHHtk5BRibC3T33jeJySU_dVNVZ-MYm5Ykb5T8Sa86HeeSH1n-aDmizk4i_-pVq_v26JwSo03vSzc-DO3jhgRIINdjA1YaZNcumqSS1W-2RUMyQvL28s1KSiZP4F2xORkW2tDl6A23wmQV2v3sYzVbRqh5G3Sg0E-VHZhuxjL7HMP4U4CxF6lszJqwl1T6SY65Qxd280nd4dnVMxgClcOgJeV2_LXhCoT9Kv98sfWl3A6IQAdxy-42gMAawQRiZJHrBCWkClMSEXOABSwTHbBUrNs5Rt-Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تانکرهای سوخت گازوئیل ایرانی در روسیه
🔴
میگن الان بخشی از گازوئیل روسیه رو ایران تامین میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/152272" target="_blank">📅 13:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152271">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
مدیرعامل شرکت آرامکو: پر کردن مجدد ذخایر نفت ممکن است حدود دو سال طول بکشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/152271" target="_blank">📅 13:38 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152270">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
رسانه عبری: ترامپ و نتانیاهو طی یک هفته بارها گفت‌‌وگو کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/152270" target="_blank">📅 13:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152269">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
سازمان غذا و دارو: هند حاضر به ارسال دارو با هواپیماهای ایرانی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/152269" target="_blank">📅 13:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152268">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
الجزیره: چین از پیامدهای جنگ علیه ایران، در دو سطح نظامی و اقتصادی بهره برد
🔴
این رویارویی فرصتی برای پکن فراهم کرد تا توانمندی‌های نظامی واشنگتن را زیر نظر بگیرد و امنیت انرژی خود را تقویت کند
🔴
چین از جنگ در چند حوزه سود برده؛ مانند رصد توانمندی‌های آمریکا با استفاده از اطلاعات ماهواره‌ای، خرید نفت تخفیف‌دار ایران، بهره‌گیری از ذخایر راهبردی و گسترش مبادلات با یوآن
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/152268" target="_blank">📅 13:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152267">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5731f75e44.mp4?token=m-mqTmb8bLePEKfi3Y68FACgVZ9bN6W204woigXhPlkYAhMvaEjbb3LezhamzR-8tpjDYox7MxJtlPzm8MYzlX0UgCjuVxVarUNCnpDEreQ3RJSi4jwhEWYtsKLhgq_xtesB2FVgJqDkTLzXxpv328xlUwZEri5Fg_BgFsMKrpvAdtBKTYRV0vGWzD6EXstqEGtRZYrvtvX1aNaBi9uEJWZZISAU5HmQ6Q6deduyENdbZYKTK6m_XDfjJueFRI5tG24mDfpvWqIsYj7ktDNxKyG8qddFwIxRDCHmQ0SQoqxWVCZsMw6Xcn4j4JD2f43dnrEPOXKKB5CjlyT4QJP54oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5731f75e44.mp4?token=m-mqTmb8bLePEKfi3Y68FACgVZ9bN6W204woigXhPlkYAhMvaEjbb3LezhamzR-8tpjDYox7MxJtlPzm8MYzlX0UgCjuVxVarUNCnpDEreQ3RJSi4jwhEWYtsKLhgq_xtesB2FVgJqDkTLzXxpv328xlUwZEri5Fg_BgFsMKrpvAdtBKTYRV0vGWzD6EXstqEGtRZYrvtvX1aNaBi9uEJWZZISAU5HmQ6Q6deduyENdbZYKTK6m_XDfjJueFRI5tG24mDfpvWqIsYj7ktDNxKyG8qddFwIxRDCHmQ0SQoqxWVCZsMw6Xcn4j4JD2f43dnrEPOXKKB5CjlyT4QJP54oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اولین تصاویر از ساختمان پلیس دیپلماتیک در میدان فردوسی پس از اصابت موشک در جنگ ۴۰ روزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/152267" target="_blank">📅 13:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152266">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cd8979df8.mp4?token=tmYO-VWJdDFYk_mi_Q0ZmL0VIMwRvlS233J-QGbp2tTgrEkzgOB6YXQI58UZYVFRfr8kg-bwKSrK2R3Ho_4WDrlDDxiScCzSwedULHbxPS32efZsCmLYCcLDfFiH6-eP8MDD6SgO4BdNGMKpIxAS4Xp7QB-EpYXxuNLnGgwkEq8UQK4Q_8mhQjHEGwodHP_NJao5mhrG5esMmIQFwUeoKHJqKj2OIURqzHmXK_kS_15EfqpAbJQEKJg8-8sOLrYOT4g_bOMl4Bc1WB7SneD0UzhqiJ9VMkW7hArR26Sxvlq-HH4rvNEcx4b8IeEEIE4XNgBqn8C2mf7sGBV28gGakg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cd8979df8.mp4?token=tmYO-VWJdDFYk_mi_Q0ZmL0VIMwRvlS233J-QGbp2tTgrEkzgOB6YXQI58UZYVFRfr8kg-bwKSrK2R3Ho_4WDrlDDxiScCzSwedULHbxPS32efZsCmLYCcLDfFiH6-eP8MDD6SgO4BdNGMKpIxAS4Xp7QB-EpYXxuNLnGgwkEq8UQK4Q_8mhQjHEGwodHP_NJao5mhrG5esMmIQFwUeoKHJqKj2OIURqzHmXK_kS_15EfqpAbJQEKJg8-8sOLrYOT4g_bOMl4Bc1WB7SneD0UzhqiJ9VMkW7hArR26Sxvlq-HH4rvNEcx4b8IeEEIE4XNgBqn8C2mf7sGBV28gGakg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر دوربین مدار بسته از لحظه وقوع سیل‌ ویران‌گر در شهرستان گرمی اردبیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/152266" target="_blank">📅 13:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152265">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba790289f2.mp4?token=QWqqVA_Uyyl7wwOgkJGdxemLrK1_iyayxgwB-kX52gRXWuPnZ2SmtOylF8B_FZnhMhDsV_CV3IUuBwea8k5TmaawHlp2tqgKEid95oUt6RA2_--vUmUN5qkL5OinmGVqopPY3wos1UYT-WxH1wqikc9gzTiH-jIJXeRWjznpR8FkHkL8TrUWD5-0TNsSAldhyK3zat1pxoB3IPOoI1wVxyP2L9R99622a24kNC5u3cULWOxNHUGPc5DdqyHGFnM9myEf0FHveKwayVqRfOSxv4mFb3WzP_zVfTi75DWDOAyQcIi2pUWx4h73XdyUASLSa9Z49C6Qq8-XBrtl1tRBuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba790289f2.mp4?token=QWqqVA_Uyyl7wwOgkJGdxemLrK1_iyayxgwB-kX52gRXWuPnZ2SmtOylF8B_FZnhMhDsV_CV3IUuBwea8k5TmaawHlp2tqgKEid95oUt6RA2_--vUmUN5qkL5OinmGVqopPY3wos1UYT-WxH1wqikc9gzTiH-jIJXeRWjznpR8FkHkL8TrUWD5-0TNsSAldhyK3zat1pxoB3IPOoI1wVxyP2L9R99622a24kNC5u3cULWOxNHUGPc5DdqyHGFnM9myEf0FHveKwayVqRfOSxv4mFb3WzP_zVfTi75DWDOAyQcIi2pUWx4h73XdyUASLSa9Z49C6Qq8-XBrtl1tRBuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خالق اشتغال با یک میلیون تومان:
اگر گرانی را در نظر نگیریم، هیچ مشکل اقتصادی در کشور نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/152265" target="_blank">📅 13:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152264">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/479ab143f8.mp4?token=UbNmgMTUEO62559JWoV2VUPsQT2Izcm3OX4ugFmCbFN9QCMyz_t7QSaK-FeziWlqrr0YSOAwsMxebb38V5VzmWJfbenJWAQUzv3Afr27quGzlII_-fuzt1YfYu93nN6ISdt27xQAEtJP2nRi2kO_NVNSdifhj1XOWNT9hLhfrUfSLR51CUEb8hbN5Cqmp_mmYYEZb7SyGHBp5WvRiAxEN2hjE8yi2ZfxyfIcLDYVWNvofNhr-AoZLU3ikPfEfqJMsJQJmCefz9X9Iz0NKGhM7BuVee1-UoOx-Rv-S-9bUXfnQjSGM4bp-GMHbXNe1QRWfjnXB68gs2ZgNrvGacQbpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/479ab143f8.mp4?token=UbNmgMTUEO62559JWoV2VUPsQT2Izcm3OX4ugFmCbFN9QCMyz_t7QSaK-FeziWlqrr0YSOAwsMxebb38V5VzmWJfbenJWAQUzv3Afr27quGzlII_-fuzt1YfYu93nN6ISdt27xQAEtJP2nRi2kO_NVNSdifhj1XOWNT9hLhfrUfSLR51CUEb8hbN5Cqmp_mmYYEZb7SyGHBp5WvRiAxEN2hjE8yi2ZfxyfIcLDYVWNvofNhr-AoZLU3ikPfEfqJMsJQJmCefz9X9Iz0NKGhM7BuVee1-UoOx-Rv-S-9bUXfnQjSGM4bp-GMHbXNe1QRWfjnXB68gs2ZgNrvGacQbpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اخیرا کماندوها و نیروهای نوپو تو سنندج رزمایش برگزار کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/152264" target="_blank">📅 13:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152261">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k7DPJmD2Yjj1YPyhcQIWqIgwHAVVV036QYhghsERLv9zS1TV8tvWl41YzucZ-LnFa-z_e2OHS-sleTvOI98I0-Dh_9bxWGmRjN5eB3B_pxXbjX4svHtAqlaGh13gAmp_QZcbPfYPm_ZH28cmXfEA-uJdrleLDh5o6wdh07SRQY_T8v10tQyVI_nD2Y9_LkMSD8TRxMBN-bBc-jti3vqO10KrUgeY7glDBdnXnjGQ5IsXSfGY57hwNL54tn6eCHbmOJedAXLpujxukWd7Lcpgu9L1_VVooZHxAxn0N-OJ1Q-H_wBfr_T25MiJPxiJAFq7h-C0_15r2PFM3g2o_VXgXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NrY51IC31ahPejAorSNNtSmISdYHArootNbayByvmDM3ncWC1e_Ce528EANJggimmSZ6pjO0WIjZqxcwn5rU-c9T7e5qmD20QjYyNbuXt-nogJ54eX4Z6qjn6PZV8wEMy2Ixd9AfU8q_sahFYk_JgFVcH_3_m8vPiNqDMQ3WkHMNP6fyHTKtTIMyrw3GRNkVAfRli7P-V0i4oPSD7JdryG6oVqISNDttFkRjPnxkK7lKQipdsQPx0XRpULKv9r3oDY-5U64Iys3slkPvn3Mj9qjLoBWvq3GHtjjXJV2aZQRZZScs0nHTt2OTJ-Zr0LhFNYrbxWuknx0WJsu_zj3QKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cbcdae22d.mp4?token=vSIwLowwadjyhdW0-8jU4OphpYvS5sNz1vfPUCZPw1HoUZfbC-eAlGGyIf9-N-szab1q-K9trWCB63w1odTweZL-B26VNdg0te9rw3Rv4yyjbGCaYr5JMoKTAR-4xQVeApFgQVsiksg5w51aa4p2k45PxgRNP0HWMqUCpzG_lxwWTYQjBFKTQiFQqrWi_J41gxiocwtAqBhYwhbPlMONUDGlSGWWpFDEzxKMWhdPtmLNRKBt8enIp-m90FtoFcUVAS8sDbm7EkMDe6VOzkv_lsQC6DleBlc77qurZ_wga_PRxyhwBCF68Rg9B36nuyq078ZwWiXvJicdXbs9EBD2Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cbcdae22d.mp4?token=vSIwLowwadjyhdW0-8jU4OphpYvS5sNz1vfPUCZPw1HoUZfbC-eAlGGyIf9-N-szab1q-K9trWCB63w1odTweZL-B26VNdg0te9rw3Rv4yyjbGCaYr5JMoKTAR-4xQVeApFgQVsiksg5w51aa4p2k45PxgRNP0HWMqUCpzG_lxwWTYQjBFKTQiFQqrWi_J41gxiocwtAqBhYwhbPlMONUDGlSGWWpFDEzxKMWhdPtmLNRKBt8enIp-m90FtoFcUVAS8sDbm7EkMDe6VOzkv_lsQC6DleBlc77qurZ_wga_PRxyhwBCF68Rg9B36nuyq078ZwWiXvJicdXbs9EBD2Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اعتراضات امروز دانشجویان دانشگاه بوعلی سیمای همدان به کیفیت پایین غذای دیروز که باعث شده بود خیلی از دانشجویان دیشب مسموم بشن و به بیمارستان مراجعه کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/152261" target="_blank">📅 12:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152260">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuW5nay6Grb70qWEA_t4Z39F4oydlOnsinnLo8o77wbq8ldY3sOFsSBld_gN3Tbb9FAepVuDA5Zg4IkuPe6J2MNnyZx7ZwmhXIpzNuyGPauIsZoiRYRIu6kcvzD9YLQRzt5gmlpMfcYnCCzPDuBm-Ic7XXg_TEP2wACiTUPGy3KR4lhoaWPXVBFarLwnKJwl5VRaKkBDOUwAvL53fsmMRkMb0-mwfCec3xCSXeXR8SjThzgZZ0sVUyfmiDLpPJ7x2M4rImCKcxrC3CkGI2ZGbSpeDBpmfR7UoJk08-XbSIC5jPGG9y8tzXZZpR2FAw_uMO1beBxvjUzfT8ftxoD9lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاور سابق دبیر شورای عالی امنیت ملی: مذاکرات ایران و آمریکا فاصله زیادی با توافق و فاصله نزدیک‌تری با تنش دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/152260" target="_blank">📅 12:56 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152259">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در اربیل
🔴
برخی منابع خبری از شنیده شدن صدای انفجارهای شدید در اربیل عراق خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/152259" target="_blank">📅 12:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152258">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
سازمان هواپیمایی کشوری عربستان سعودی اعلام کرد که فرودگاه بین‌المللی ملک خالد در پایتخت این کشور، ریاض، به دلیل شرایط خاص، همچنان بسته خواهد ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/152258" target="_blank">📅 12:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152257">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
پزشکیان: بنزین ۵۰۰۰ تومانی رو داریم ۱۵۰۰ میدیم،‌ باید ریشه‌ای درستش کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/152257" target="_blank">📅 12:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152256">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
کاملا هریس: گرانی ها در آمریکا تقصیر ترامپ و جنگش در ایرانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/152256" target="_blank">📅 12:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152255">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
چین حملات اخیر حوثی‌ها به عربستان سعودی را محکوم کرد.
🔴
مائو نینگ، سخنگوی وزارت امور خارجه چین، اعلام کرد این حملات تلفات سنگینی به‌جا گذاشته و تشدید درگیری‌ها مایه نگرانی جدی پکن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/152255" target="_blank">📅 12:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152254">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
سی‌ان‌ان: واشنگتن به کی‌یف هشدار داد اگر به حملات خود به تأسیسات انرژی روسیه ادامه دهد، اروپا برایش تسلیحات آمریکایی خریداری نخواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/152254" target="_blank">📅 11:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152253">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6980aa2533.mp4?token=WSoUlxSCbXRFsXUVfjcPtzlcnWucnkILJLr1FyyVMjoxB_mcofDqVvA_ffnstCpyXVvsBH-H8bzEetE0aJl3PSHQCO6SLlGN3BvXJCC6yxLix07p1rRJ8BsManFddF1zm3umnQVhhDwerzSr_kKdKP2ksIok6R_MdzMoscc2ha4CmgxEiFmyZ4NkWOArlDFaIfFEDK_1dI5Q66OWZ3wwAeF44wNy2w826Z0C3eofHn3VUIEZTQnxu2GKqxysy-wmShF2s8tFJQgSuJdZ2IFILrKKHlPqieJCi2XYQWI0YBJnz-rJn6PDEJvtSvx9Y1rGAzOstCL5ZboVW35aoa2WuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6980aa2533.mp4?token=WSoUlxSCbXRFsXUVfjcPtzlcnWucnkILJLr1FyyVMjoxB_mcofDqVvA_ffnstCpyXVvsBH-H8bzEetE0aJl3PSHQCO6SLlGN3BvXJCC6yxLix07p1rRJ8BsManFddF1zm3umnQVhhDwerzSr_kKdKP2ksIok6R_MdzMoscc2ha4CmgxEiFmyZ4NkWOArlDFaIfFEDK_1dI5Q66OWZ3wwAeF44wNy2w826Z0C3eofHn3VUIEZTQnxu2GKqxysy-wmShF2s8tFJQgSuJdZ2IFILrKKHlPqieJCi2XYQWI0YBJnz-rJn6PDEJvtSvx9Y1rGAzOstCL5ZboVW35aoa2WuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: آمریکا حتی کوه و محیط زیست ایران را هم هدف مشروع خودش می‌داند!
🔴
اظهارات وزیر خزانه داری درباره تحریم‌ها نفاق آشکار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/152253" target="_blank">📅 11:50 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152252">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3c311b17c.mp4?token=B2LubWqh-TNKioTacBJRKWfDlMgi8Uf_Y4G4hCZHjBDlJm38dvpeI87PiJCDGCrSoCQikytPu6VC3bn59qD2i7_1GezjzVRuY9ktTfOZbUDxM7LR4M2dOJOYZ-IzaAU9o7BTOLJe4_Pp3wLN2Q2di66QOXe9LLWf5z-3azrbkc3w5Nnk44Fx36t4rRK-a7_-uu63Di3mHnhcO7WXoZfBP5Z7Q9ebwoOA-Nc7f36P1yjEuxpsfw7U7FfqQNokov2mZ-VfXev5T8pUwZKtgqHGBKhTGQS7U2jFFxgljBiuuqhU4P8J1e-rrtWx6_oyyeSq0kMHiRtiD9-slJ-L3Yor3YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3c311b17c.mp4?token=B2LubWqh-TNKioTacBJRKWfDlMgi8Uf_Y4G4hCZHjBDlJm38dvpeI87PiJCDGCrSoCQikytPu6VC3bn59qD2i7_1GezjzVRuY9ktTfOZbUDxM7LR4M2dOJOYZ-IzaAU9o7BTOLJe4_Pp3wLN2Q2di66QOXe9LLWf5z-3azrbkc3w5Nnk44Fx36t4rRK-a7_-uu63Di3mHnhcO7WXoZfBP5Z7Q9ebwoOA-Nc7f36P1yjEuxpsfw7U7FfqQNokov2mZ-VfXev5T8pUwZKtgqHGBKhTGQS7U2jFFxgljBiuuqhU4P8J1e-rrtWx6_oyyeSq0kMHiRtiD9-slJ-L3Yor3YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعارای امروز عده‌ای الاف و بیکار دم در خونه روحانی:
🔴
نخ عبات که ماله انگلیسه ؛اون عبا رو باید سگ بلیسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/152252" target="_blank">📅 11:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152251">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‏
👈
بقایی: موضوع واگذاری ۱۱۰ هکتار زمین به افغانستان سوءتفاهم بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/152251" target="_blank">📅 11:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152250">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/722f4f3a8f.mp4?token=S8qAGc5lhLmdjeVDwbYR3m2-hPP60gmUEWBCBw5tZ53la3TYjhSCIV5ADQcrUDmTUhZtMpy9RiqNIS0LPTOHWptGtAZrT0j-nUZ8uL65wmY0fqheP--AvAHE-ym-4KkiH_Yej_lhTyy5ynKhP4y3_khGxAH9J6qqLW5lD4EWf32pK8qQz0-H8ZtEwoIZqjiCWzNMCSA-8LOXBrjx1kaeCXiy5DOnQO2-l34ls-dmp2EDlJVjpAsbW5vCtGq7B3tkV7QSLvTpwm-qkSXRlTQ_RbdXTy3QgtMPiJIQHUXPdNQEDhzSUrpTrJco1u_Sdmb-mUXK6hQm6e2S9ETo6IcoFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/722f4f3a8f.mp4?token=S8qAGc5lhLmdjeVDwbYR3m2-hPP60gmUEWBCBw5tZ53la3TYjhSCIV5ADQcrUDmTUhZtMpy9RiqNIS0LPTOHWptGtAZrT0j-nUZ8uL65wmY0fqheP--AvAHE-ym-4KkiH_Yej_lhTyy5ynKhP4y3_khGxAH9J6qqLW5lD4EWf32pK8qQz0-H8ZtEwoIZqjiCWzNMCSA-8LOXBrjx1kaeCXiy5DOnQO2-l34ls-dmp2EDlJVjpAsbW5vCtGq7B3tkV7QSLvTpwm-qkSXRlTQ_RbdXTy3QgtMPiJIQHUXPdNQEDhzSUrpTrJco1u_Sdmb-mUXK6hQm6e2S9ETo6IcoFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
بقایی: موضوع واگذاری ۱۱۰ هکتار زمین به افغانستان سوءتفاهم بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/152250" target="_blank">📅 11:28 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152249">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUzkVAcTlJktQ4WCehYBAdG87tZV72ivmXQJkXyO-EWbCO7WU0kwvy7em0_Bkvv_n7loy3TMO78qAiCOXlSJ-EJ7RShnfSc6PxUv0TedO2iPe3i63Yl2X3J3eYWFaBrSjSt02Fcw_KzD-yd_p5nLQhs3hzAVVV2KWKzYcxbAzKHZxlFrnaBqoJsFjASg53Ug77pA_Tb_vfBe8Gm2RbdIl9mk5m_2LiC9Kf7aNORyBFWKA3spHJzpydMSXawUWAciiNI12GuGz9B-0RoMIicsL20oBeZv4kl3J17jAYzLSJNZwhC21YgmAeqyQ4cdp6LkwGHJHQrvtiV44hDy2RJNWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال: محمد بن سلمان ، ولیعهد عربستان سعودی ، با احتیاط در میان کاخ های مستحکم و مجهز به پناهگاه های پناهگاهی ، همراه با نگهبانان امنیتی انتخاب شده ، حرکت می کند ، زیرا حملات حوثی ها افزایش می یابد.
🔴
مقامات سعودی می گویند که این پادشاهی در آستانه اتمام موشک های رهگیر است و در حفاظت از زیرساخت های انرژی و کاخ های سلطنتی خود مشکل دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/152249" target="_blank">📅 11:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152248">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
شبکه عبری کان : حدود ۲۰ فروند هواپیمای سوخت‌رسان آمریکایی از ایالات متحده به اروپا بازگردانده می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/152248" target="_blank">📅 11:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152247">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
فلایت رادار: تعطیلی فرودگاه ریاض تا ۲۴ ساعت دیگر تمدید شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/152247" target="_blank">📅 10:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152246">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وال‌استریت ژورنال: حملات حوثی ها، رؤیای اقتصادی بن‌سلمان را تهدید می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/152246" target="_blank">📅 10:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152245">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bea561a653.mp4?token=qyaDaaxl8n_JfXr65T6oQwDMig-JZwrD7t8ej9ClbJ27tO1QcgRo2MZQ7xnDZGfROoDwf5Ex41Qtq0LTr1cVQ4pUmIjpBWo6BrGGdrwJjVAfCUUwVrHXSWYEJ2fh_cHzWfXlZvgcyMh5GLl-OE1B-i1BgN7HGYg0oIWRzcfgEyZPtwpsrUqFXkywyXk6DgDnVLsTGiPwM5kubKPiBfX4UBeb0QjCTde1hYaKpk77at-45oRkCnvYwHy0hckAwj_ODKUeY9pugxCMnk_y-KmUqkzKGx_anhljQQhSX_dsC69xiiFgSULXWGxdiyN5ON6-OzuFyt3NeYSY7CEnEyOl4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bea561a653.mp4?token=qyaDaaxl8n_JfXr65T6oQwDMig-JZwrD7t8ej9ClbJ27tO1QcgRo2MZQ7xnDZGfROoDwf5Ex41Qtq0LTr1cVQ4pUmIjpBWo6BrGGdrwJjVAfCUUwVrHXSWYEJ2fh_cHzWfXlZvgcyMh5GLl-OE1B-i1BgN7HGYg0oIWRzcfgEyZPtwpsrUqFXkywyXk6DgDnVLsTGiPwM5kubKPiBfX4UBeb0QjCTde1hYaKpk77at-45oRkCnvYwHy0hckAwj_ODKUeY9pugxCMnk_y-KmUqkzKGx_anhljQQhSX_dsC69xiiFgSULXWGxdiyN5ON6-OzuFyt3NeYSY7CEnEyOl4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان در واکنش به پذیرش نظرات کارشناسی گفت: من مگر دیوانه‌ام که اگر حرف درستی را به من بگویند و من نپذیرم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/152245" target="_blank">📅 10:38 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152243">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e416bb3da2.mp4?token=HjRW6bzHHu64p02fXSAECNpm7YcH0dcaQAN0UksfHeVbGq1AJ4HTLGlG9LxiB9AicJ22WCINrdZ13hjPlCC_N8Jj5mpLLM-0x_fYLwlHXlhCbnERcN7cZFWMWlrDHQhyEJO4pipua5nXDAAaq8lDL1ZG7QSu4UdPH6WvZJPuzYOx6gHJ1Gx_LfuYdVzFLkP7h4qIY9PPAbAL6MxNQzZqOZHeEotmA-y3djFjjpvN_ldI1otUgXIG_BUpxTpU0h9MAXHTp-F6p4FDcxnN_7er_f-csKp7PyIcbmnZlQeChB4QEc_042Oz_XLW-BnORS2bFsl8qul2VBuQQhmTn42EHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e416bb3da2.mp4?token=HjRW6bzHHu64p02fXSAECNpm7YcH0dcaQAN0UksfHeVbGq1AJ4HTLGlG9LxiB9AicJ22WCINrdZ13hjPlCC_N8Jj5mpLLM-0x_fYLwlHXlhCbnERcN7cZFWMWlrDHQhyEJO4pipua5nXDAAaq8lDL1ZG7QSu4UdPH6WvZJPuzYOx6gHJ1Gx_LfuYdVzFLkP7h4qIY9PPAbAL6MxNQzZqOZHeEotmA-y3djFjjpvN_ldI1otUgXIG_BUpxTpU0h9MAXHTp-F6p4FDcxnN_7er_f-csKp7PyIcbmnZlQeChB4QEc_042Oz_XLW-BnORS2bFsl8qul2VBuQQhmTn42EHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ماهواره‌ها، وقوع یک آتش‌سوزی ناگهانی در میدان نفتی الشیبه در عربستان سعودی را ثبت کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/152243" target="_blank">📅 10:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152242">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b0d54ab6a.mp4?token=eRs130UelUZE2aswi9p0QqNsKJeRPU8Kri51_7HHHKT6gbZNGO6Z5MNUDxX1APEi6YbJX7MMNjh70eNlNXmjAk0IZjj4orwVeDo_VKcths3X0AQG4GFanDdnH0DFNifXa8MfXt_z8ttTLFBDZbpNw2Cd5jTOrU80SIMyv9JUCZCha_I0qsdusz-F7eaUWJFQ3U13R3PHpiLfMLwcVaUpy3jjbf70gjoZri-x2R72clLYva--vdekAkNBn2xNdHbQZAkgqPtdnqwdeRVLeOdwEwpleNAphDvmje0kuQPPY4OgROePPj_IFDOuipPfP02fizY-Zad09swrrzpLz73RWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b0d54ab6a.mp4?token=eRs130UelUZE2aswi9p0QqNsKJeRPU8Kri51_7HHHKT6gbZNGO6Z5MNUDxX1APEi6YbJX7MMNjh70eNlNXmjAk0IZjj4orwVeDo_VKcths3X0AQG4GFanDdnH0DFNifXa8MfXt_z8ttTLFBDZbpNw2Cd5jTOrU80SIMyv9JUCZCha_I0qsdusz-F7eaUWJFQ3U13R3PHpiLfMLwcVaUpy3jjbf70gjoZri-x2R72clLYva--vdekAkNBn2xNdHbQZAkgqPtdnqwdeRVLeOdwEwpleNAphDvmje0kuQPPY4OgROePPj_IFDOuipPfP02fizY-Zad09swrrzpLz73RWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: داریم در تهران آب زیرزمینی را استفاده می‌کنیم و اگر تهران هم با همین روند رشد کند از کجا باید آب بیاوریم؟!/ باید برای حل این موضوعات چاره‌اندیشی کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/152242" target="_blank">📅 10:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152241">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJ_d9BZHCPh5HTr29J9XUPZ-21CqBEh5rmLcLRL3xV0UaGx2ENDrBii6pBpBRcC0Sd1qqcfbg2D81Z6TVvYG-F3Do26uA-ItIhBC8x7SqCBTolhCM67icHRHaPrW6rUyC-WTTCDzFVy2VkW-pq24RyqH35LdOcow9YNNJybRxfETve3efl6xUUfukaXrHeKxI1N2ZA7OFei_x-aGTfJtjMV_Kf_tDZObGiG8Mv8UhZhoyNv_ZIEJa7dx3Lia_9x5mAFS18MYWFoiWu9GNUCxvyVvpR1Bqrg1BOWNKYqfonBrim7Pt5LUfReJtzW4WIdqCOpiH9fPHzwsBKSEGAjwXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عبدالمکلی، وزیر دولت رئیسی: اگه گرونی رو بزاریم کنار دیگه مشکلی تو کشور نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/152241" target="_blank">📅 10:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152240">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc3f945f51.mp4?token=H8gWa0KubXquYYiTyjST2NfUz1luU47eUHwUBF9086PdRyF8RcX2ZQq6lTPfYvsF_QGQaNBCpLQTYVZA7naObbHow-nhI5oC6bwpDGQgH64eMj3NmVrn6Vnzk7TVSfBBxXpCpD9mJKQdYAvHIfs2IHfRKCnjmaJqsztiDVH8PQyT7EQ6KiSEtLlvkxNPNxz8npKzkJSkxJXktmJQMpNb7DYmdzJ1aZqM9bKkPv2XpHeXL3tqGwTekje8jtjOP3NaGnWHRqpgPsNoV-W-A2lbrrvqaD1tf8HohgVreMPXEl0Qg0TU9arEeXIteprnHJyL1N_hFa43CD5x2oPCXKrIPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc3f945f51.mp4?token=H8gWa0KubXquYYiTyjST2NfUz1luU47eUHwUBF9086PdRyF8RcX2ZQq6lTPfYvsF_QGQaNBCpLQTYVZA7naObbHow-nhI5oC6bwpDGQgH64eMj3NmVrn6Vnzk7TVSfBBxXpCpD9mJKQdYAvHIfs2IHfRKCnjmaJqsztiDVH8PQyT7EQ6KiSEtLlvkxNPNxz8npKzkJSkxJXktmJQMpNb7DYmdzJ1aZqM9bKkPv2XpHeXL3tqGwTekje8jtjOP3NaGnWHRqpgPsNoV-W-A2lbrrvqaD1tf8HohgVreMPXEl0Qg0TU9arEeXIteprnHJyL1N_hFa43CD5x2oPCXKrIPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان:
به هر کس و هر جا بخواهیم دست بزنیم و وضعیت را درست کنیم برای ما مساله درست می‌کنند/ آیا من مقصرم که وارث چنین وضعیتی هستم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/152240" target="_blank">📅 10:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152239">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjlu7Ba1rAYjxh91AqKUyxhuPuyNxC1zEIRVzOawUcdNyqnZxzXVOzTFPlnH4OUZW1NEDGQyXxsghNBHHsrZX40VVpIlukEmJMCLRh1pB0NDtaDpfzSszQjBEwZ0vemOia5TCQB0r4xfjTUZv_R9UiHTx4jZ6Xf6ALK-vaN5ds1qup_wePqzsIY4FT7GLgsLx_1Wwhrm-paekDolFRmb0__VMJP9E6ZsEvnAEDqk6O1aQrRgdVmiH6GWiXDdOhmGD-XT5hGnAKm0T5oungPTiTBFZLVPF4eg-TAy9tMW4kD29QsNUEOuIm_gwrDUWLt236JVTldW6tR-M7iTDqRqdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ظریف:
وایسم تا صبح غُر بزنم قاسم زنده میشه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/152239" target="_blank">📅 10:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152238">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
هر لحظه احتمال جنگ و قطعی اینترنت وجود داره، کانفیگ‌های ووکس حتی تو قطع اینترنتم جوابه
https://t.me/voxnet_bot
https://t.me/voxnet_bot
قیمتا مفت و مورد اعتماد
✔️</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/152238" target="_blank">📅 10:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152235">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
وال‌استریت ژورنال: عربستان با کمبود موشک‌های رهگیر و سامانه‌های پدافند هوایی مواجه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/152235" target="_blank">📅 09:59 · 20 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
