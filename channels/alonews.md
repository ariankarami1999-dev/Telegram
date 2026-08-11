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
<img src="https://cdn4.telesco.pe/file/NOdS1mw16UxGbuWYo7rOaZQITdOdouWDHoROdzR9b2vpQS4lQ50uvoXfOZmsw_2YGeBkiVWnro3sSxwsV46qBNQM0ft2GI6JvrTOEG2zkFAWf9I7I24b3zeHSXDdKw_kaa5yg4iDXTJO-EAFHTYRwq0B2AjCVdU6L-4bW99TtaLQD99pECG-YnfoDp78-V6PrOcjjwyK1VZWMayC7BF6Hi7YW7cry6B3E-1Pv5Q247HEIQaxhUBn2ZiFCJxnaL8E90gqb1lxGh6-M5V4oLlnX_fFRZshV3df1YSVNQGRS1jOsq0iPAeHqbtP4ALdmE-0UESYTNYUcPbCyx0OR9ZNIQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 969K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-20 11:33:58</div>
<hr>

<div class="tg-post" id="msg-141113">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
داده‌های حمل‌ونقل دریایی نشان می‌دهد که تردد کشتی‌ها از تنگهٔ هرمز دیروز به ۶ فروند کاهش یافته است.
🔴
این درحالی‌ست که میانگین ۱۰ روزهٔ این آمار حدود ۱۱ کشتی بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/alonews/141113" target="_blank">📅 11:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141112">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
رسانه‌های عربی: یمن به یک کشتی عربستان حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/alonews/141112" target="_blank">📅 11:27 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141111">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/293e8a0f47.mp4?token=MoDtRA1M8OkObcKJeEkdNeg78bRUxklf1JeTC8V6ZiUVBUaUwolfPxLcnqd8VV75n1EZ8Y6-g_5uzfcYtRsWi-Ke3EA3z7jEwUxcBC9zjA_7Rf1_xHAGglhK_fBP7ERRwuYac74PRVFti6qle4H4RGl4hnR9a5cS72Xvwo4kX9aG1UmtyBDDmn4AG-hNOxbaL_lsI0ZDHhueIKj_XKWT357MeZEoO_ygqySZtbXTBZO43aReC8jj1nslXJpCRcn_PcVVMGnCPzOB_AH1359mgxGP52TnUGWMp8oQxfAXPBQRSKPO3dWj_4TVGhQJs1UQrungNnzNFvGVFCLhHgGRFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/293e8a0f47.mp4?token=MoDtRA1M8OkObcKJeEkdNeg78bRUxklf1JeTC8V6ZiUVBUaUwolfPxLcnqd8VV75n1EZ8Y6-g_5uzfcYtRsWi-Ke3EA3z7jEwUxcBC9zjA_7Rf1_xHAGglhK_fBP7ERRwuYac74PRVFti6qle4H4RGl4hnR9a5cS72Xvwo4kX9aG1UmtyBDDmn4AG-hNOxbaL_lsI0ZDHhueIKj_XKWT357MeZEoO_ygqySZtbXTBZO43aReC8jj1nslXJpCRcn_PcVVMGnCPzOB_AH1359mgxGP52TnUGWMp8oQxfAXPBQRSKPO3dWj_4TVGhQJs1UQrungNnzNFvGVFCLhHgGRFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
تصاویری ترسناک از زلزله بزرگ کلمبیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/alonews/141111" target="_blank">📅 11:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141110">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uz69vj2kR1PEy8JjyDL4-11TtSt1QJVpdMo2_-xoci0rj3uBS7ywlyCP37qCnchYZiEQ6pj6TNO64DRFZL7WI59VjM-rWTb-gqQk-5Y7sXxlIOc_TSQN5X9xpz7b1be2fnlPbWcMgmpyCrcPCD7a9C2nwvpDySVzGkjAqkzTTj5oMjBP0ceU-AWVwLgbPC-754j8IS3td-oqbMwrXypmyq___3tsZYYgQgtpdBqzFJn3fatanvl_DSGt0QSy3nj8OnSRcOGs71s55KNEj7qjXfzw1_N4jzjMc85XqwU5OTWpzCJEGLWLL9-arifTI6wdXm5MyK1EtZccXtRe0ZJ70w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توپخانه اسرائیلی شهر زواتر الشارقیه را در منطقه امنیتی جنوب لبنان هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/141110" target="_blank">📅 11:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141109">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/207604b3e3.mp4?token=V3coT6LZahnuYWMdXZnnIjAgLfLvg3bmyVTFHYKd7XbbGrN2ZLzg64LChvA9eDEeTqkmMyyp1CEhlBTLXFKn9LByPv2g4wMieFb_crD8iGKsNsIlsdFJG9Qry8ALQn2PoLMrONIpvXPOF6tjIijS1m9xj-UO3HrVBnCKDW-qei9NN21FxdEt-eU1uz4NYGu8d_r7STOMtt3G3HcQ1lDw7gmi7u0-gXC3NHHH2PKpkBjdU2uB6EXRE3tMoeh7EUJdLbYcpeGj6jhOepHztaGh7R6AyI039t14KGz7nXdNNSug1yB7OluwAah3EXpXgmnqdX_yZura7uxgVibIOT1QWoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/207604b3e3.mp4?token=V3coT6LZahnuYWMdXZnnIjAgLfLvg3bmyVTFHYKd7XbbGrN2ZLzg64LChvA9eDEeTqkmMyyp1CEhlBTLXFKn9LByPv2g4wMieFb_crD8iGKsNsIlsdFJG9Qry8ALQn2PoLMrONIpvXPOF6tjIijS1m9xj-UO3HrVBnCKDW-qei9NN21FxdEt-eU1uz4NYGu8d_r7STOMtt3G3HcQ1lDw7gmi7u0-gXC3NHHH2PKpkBjdU2uB6EXRE3tMoeh7EUJdLbYcpeGj6jhOepHztaGh7R6AyI039t14KGz7nXdNNSug1yB7OluwAah3EXpXgmnqdX_yZura7uxgVibIOT1QWoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله پهپادی اسرائیل چند دقیقه پیش به یک خودرو در النبطیه هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/141109" target="_blank">📅 11:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141108">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
رسانه‌های عربی: یمن به یک کشتی عربستان حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/141108" target="_blank">📅 11:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141107">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c02a0c926.mp4?token=a1cydcXAHL-zm1fMWPEjuk_TNqiGj51aF-F_avNdzqqPBALrdrLjUgCR0ccMDL_GUyzpo6PdfJtIBeo--AKad7Dm-gUPYgxpixvYu7-2lYdjPpIPpoMB-XgRMJ2oIOyMP5-Lg66Xrn2Ke4JTmtprQWsH7UXgQw5bTn-K1q6FxzJ2bZ7O6_CEZJUAkR4L_XhSjvzmosXTjJVWi3f9ak7Us2dhUs5oStFCsSFlG5oWW0fAyf8Imnz7iLtPMHhQoUy5pGPdI3tz5mfw3LJpDNJV0HHSNCXd71m7KV_zEaXKDSZk-62tCigUDgUXng53uDZs3YDk3KAgoP3fm1F17BHA1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c02a0c926.mp4?token=a1cydcXAHL-zm1fMWPEjuk_TNqiGj51aF-F_avNdzqqPBALrdrLjUgCR0ccMDL_GUyzpo6PdfJtIBeo--AKad7Dm-gUPYgxpixvYu7-2lYdjPpIPpoMB-XgRMJ2oIOyMP5-Lg66Xrn2Ke4JTmtprQWsH7UXgQw5bTn-K1q6FxzJ2bZ7O6_CEZJUAkR4L_XhSjvzmosXTjJVWi3f9ak7Us2dhUs5oStFCsSFlG5oWW0fAyf8Imnz7iLtPMHhQoUy5pGPdI3tz5mfw3LJpDNJV0HHSNCXd71m7KV_zEaXKDSZk-62tCigUDgUXng53uDZs3YDk3KAgoP3fm1F17BHA1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عراقچی: ترامپ که اول جنگ توئیت زد «تسلیم بدون قید و شرط» بعد از ۲۰ روز برای مذاکره التماس می‌کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/141107" target="_blank">📅 11:07 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141106">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f8cba287a.mp4?token=rh6PjWMI-P4yppQGiC2yLXNO1hLYxCyrN9U9wF8N2YljVPK6wCrrlp47jS3UnCuBb-wuDflVL6hlltpi7a6vSfIhX_0xXqPmXw0_kW1TAAg-ZobBZndOT5j_jQw127-lVwi7s_F9PEuoU6SHvHA6jzG5arzOPOyjgsSSVGM66RZ_f_tv4lxSm_dTziRzpMWlHGAaZmEiAhZbE1yz68f7avMrU86KQzeON7-Ti24v01cPJq83MPtnLOhEqutR23a8N6NH_z2mqrAWWXJPDn-dpOGy0VBImefpDY_mwWUoewWTA0vTleJRo-Dg8cL6f7mltqW5nPmQ11Lx1oyLy8Sebg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f8cba287a.mp4?token=rh6PjWMI-P4yppQGiC2yLXNO1hLYxCyrN9U9wF8N2YljVPK6wCrrlp47jS3UnCuBb-wuDflVL6hlltpi7a6vSfIhX_0xXqPmXw0_kW1TAAg-ZobBZndOT5j_jQw127-lVwi7s_F9PEuoU6SHvHA6jzG5arzOPOyjgsSSVGM66RZ_f_tv4lxSm_dTziRzpMWlHGAaZmEiAhZbE1yz68f7avMrU86KQzeON7-Ti24v01cPJq83MPtnLOhEqutR23a8N6NH_z2mqrAWWXJPDn-dpOGy0VBImefpDY_mwWUoewWTA0vTleJRo-Dg8cL6f7mltqW5nPmQ11Lx1oyLy8Sebg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عراقچی: به گفته مقامات کشورهای مختلف ما هم جنگ را بردیم، هم دیپلماسی را
🔴
به‌نظر من اخلاق، شرافت و عزت را هم بردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/141106" target="_blank">📅 11:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141104">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cb5c8ae2f.mp4?token=qwrWK6TtgXGj1Sn_KAjSOMbtIqO8VRHCOrNS8jFkqSCDJvD8wrlk6KFkcg67plq2K80MxK1UqjlXu5e5Jx_sbWIhHzebBSPIRS5swj39YBkvT1EwS4yuxtuvj7ka27doBBhtbczR41p9-hDsnz4Kd7MfS7Qi3kZfd1I7dnDz4wIUMb6bGXuCV9DhSEAweUvltU4YTMnumvkyUkFvOmz62vbRFWGbofliDTwTfUcxuaNOg-Z0B-9CLP0TF3OJEbd0IWWoRF03tOYyEVQG0ZCEbTFieXpqjFBkaDBd9SnB_bgDqsI-nKqPw67okRqv3nTul-Jiq2EYuhV1YOE_GNpgHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cb5c8ae2f.mp4?token=qwrWK6TtgXGj1Sn_KAjSOMbtIqO8VRHCOrNS8jFkqSCDJvD8wrlk6KFkcg67plq2K80MxK1UqjlXu5e5Jx_sbWIhHzebBSPIRS5swj39YBkvT1EwS4yuxtuvj7ka27doBBhtbczR41p9-hDsnz4Kd7MfS7Qi3kZfd1I7dnDz4wIUMb6bGXuCV9DhSEAweUvltU4YTMnumvkyUkFvOmz62vbRFWGbofliDTwTfUcxuaNOg-Z0B-9CLP0TF3OJEbd0IWWoRF03tOYyEVQG0ZCEbTFieXpqjFBkaDBd9SnB_bgDqsI-nKqPw67okRqv3nTul-Jiq2EYuhV1YOE_GNpgHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شواهدی وجود ندارد که اورانیوم غنی‌شده ایران زیر آوار باشد
🔴
جان برمن، مجری CNN: ایران اورانیوم غنی‌شده خودش را دارد؛ همان چیزی که در آغاز جنگ داشت. آن‌ها همچنان مقدار قابل‌توجهی اورانیوم با غنای بالا در اختیار دارند.
🔴
جیسون رانتز، تحلیلگر محافظه‌کار:
"زیر آوار دیگه؟"
🔴
جان برمن، مجری CNN:
"نه، هیچ اطلاعات و شواهدی نداریم که نشان بدهد اورانیوم‌های ایران زیر آوار است... و آن‌ها همچنان هر از گاهی چند موشک به سمت ما شلیک می‌کنند و همچنان توانمندی هسته‌ای دارند."
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/141104" target="_blank">📅 10:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141103">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
رئیس اتاق بازرگانی ایران و چین:
تبعات ادامه محاصره دریایی از جنگ نیز بیشتر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/141103" target="_blank">📅 10:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141102">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d987e3f89.mp4?token=FnIMu1gkxUjkXD9sKQjUDFCUGKaiZpiWN6hZfK8WmnshP2tTVzWTB3puVbUtpwGxY9NsxpbRda7gKIT71ScDom9fZhBTc2sDsLqfAli2hg2kXJ0GUC8vfh6Jt9FkQR0eLUEkEKnoFhH9ltmiVhFFYxHjvpYtfbp7LuSJntw42DQ0j-Zr1Hb1cfy7jlQiZ0ovKdbzpF3QjIYQ0078PJ3nkONFas8qjDPbRuaCMJijCrgTb9DeHyMHCY3Df_Jch_P6ZXjTGmL0-NlZc8HaOXzFctcqEU3MrNbx2abg1lgMmGxtr0r6cDKk2wnZaoxdCEbdvPLUwRamAhENFulB1Jee4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d987e3f89.mp4?token=FnIMu1gkxUjkXD9sKQjUDFCUGKaiZpiWN6hZfK8WmnshP2tTVzWTB3puVbUtpwGxY9NsxpbRda7gKIT71ScDom9fZhBTc2sDsLqfAli2hg2kXJ0GUC8vfh6Jt9FkQR0eLUEkEKnoFhH9ltmiVhFFYxHjvpYtfbp7LuSJntw42DQ0j-Zr1Hb1cfy7jlQiZ0ovKdbzpF3QjIYQ0078PJ3nkONFas8qjDPbRuaCMJijCrgTb9DeHyMHCY3Df_Jch_P6ZXjTGmL0-NlZc8HaOXzFctcqEU3MrNbx2abg1lgMmGxtr0r6cDKk2wnZaoxdCEbdvPLUwRamAhENFulB1Jee4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی از محل گروگان‌گیری صبح امروز در خیابان ولیعصر تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/141102" target="_blank">📅 10:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141101">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/285c35004b.mp4?token=oIoH4BXqhbc6fpmsdkVBwRh3LHHDGnevj40ZEHl09aqnl7PD4UiulBaOwqPbERwWhiv5ODIZdtfxn5eQu6YjWtsKfxa676mbwiR52XK6p5G1PHwNwaJhwejaDYymQ3bTuDvLpnwT9RV_Uwxmmkl4-GwnwAXO6EayVch2uXqWnX9wdiX9vC038_oQ3NTHzsxvP4EFXwlmWv5JMFjvVq1eJ7AxdLi_rImLiwJSBtl-M0GrTTPXG_LO7nQQC9idZZAgKO_hBSHr27Ih3AOXmlOx3JaKS6S5O8DluO65I1e_71C77i11-leWdMP_UQuzFkfWm7BvVDv0y9iJO7dV4uBQSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/285c35004b.mp4?token=oIoH4BXqhbc6fpmsdkVBwRh3LHHDGnevj40ZEHl09aqnl7PD4UiulBaOwqPbERwWhiv5ODIZdtfxn5eQu6YjWtsKfxa676mbwiR52XK6p5G1PHwNwaJhwejaDYymQ3bTuDvLpnwT9RV_Uwxmmkl4-GwnwAXO6EayVch2uXqWnX9wdiX9vC038_oQ3NTHzsxvP4EFXwlmWv5JMFjvVq1eJ7AxdLi_rImLiwJSBtl-M0GrTTPXG_LO7nQQC9idZZAgKO_hBSHr27Ih3AOXmlOx3JaKS6S5O8DluO65I1e_71C77i11-leWdMP_UQuzFkfWm7BvVDv0y9iJO7dV4uBQSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه انتقال گروگانگیر خیابان ولیعصر تهران توسط پلیس نوپو
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/141101" target="_blank">📅 10:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141100">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpBLgOPgXwpb5X94GSzo2JlkJx8dIv-h5LBt_euQVIUa-2Nfr4LcUhU0Rx5OrguGoUQGIcSErPA4LeASye2nNWA40ZSv6LlNJ0Xm6ZDEHfBv0BXSapJPFxGlROz-gbC03q_xTqDs_Sy53QWn3GxBzgh53UYp1WumwO8ve1DJqTp0teNwEA-j4iHVEqGzPJMBrHbb9pb4jovI6DRu030KOOv3c1ihYB_72tHEfac30PQ4MiDMebOneXKwwfcyWUlpLhsykBdz3ofGHtLfx93uAk72I8GIT67sXTms3SmqUh5SDhWjetdyBNkm69qHLzcnXM1Z8AR9Z20vjF2QeKbncA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیت هگست، وزیر جنگ آمریکا:لیندسی گراهام، مدافع بی‌قیدوشرط ارتش ما بود.
🔴
پایگاه مشترک لیندسی گراهام میراث او را برای نسل‌های آینده زنده نگه خواهد داشت.
🔴
آسوده بخواب، سناتور؛ ما نگهبانی را بر عهده داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/141100" target="_blank">📅 10:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141099">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
صبح امروز یک مورد گروگان‌گیری در خیابان ولیعصر، بالاتر از پارک ساعی، به پلیس گزارش شد. با حضور نیروهای تخصصی پلیس، گروگان آزاد و گروگان‌گیر مهار شد؛ اقدامات تکمیلی در محل ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/141099" target="_blank">📅 10:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141098">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ان‌بی‌سی: ایالات متحده معتقد است که اولویت ایران از سلاح‌های هسته‌ای به تنگه هرمز تغییر کرده است.
🔴
ترامپ به مشاوران خود اطلاع داده است که همچنان تمایل دارد تلاش خود را برای رسیدن به توافقی با ایران ادامه دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/141098" target="_blank">📅 10:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141097">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
مایک والتز، نماینده آمریکا در سازمان ملل: ایران در مذاکره‌ با ما، صحبتش فقط پول، پول، پول است؛ زیرا آنها بمباران‌ها را تحمل می‌کنند
🔴
آنها به دنبال دسترسی به پول نقد و دارایی‌هایشان هستند که ما مسدود کرده‌ایم؛ این همان نقطهٔ فشار است.
🔴
این فشار همراه با محاصره، چیزی است که در نهایت باعث می‌شود ایران عقب‌نشینی کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/141097" target="_blank">📅 10:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141096">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
کارولین لیویت، سخنگوی کاخ سفید: به لطف رئیس‌جمهور ترامپ، هزینه زندگی در کشور ما مقرون‌به‌صرفه‌تر شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/141096" target="_blank">📅 10:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141095">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
واشنگتن پست:در پاسخ به تهدیدهای ایران مبنی بر ترور، ترامپ به طور مخفیانه از ترکیه خارج شد و با یک هواپیمای نظامی دیگر سفر کرد، در حالی که کاخ سفید به دروغ ادعا کرد که او در هواپیمای ریاست جمهوری بوده است.
🔴
برای پنهان کردن تحرکات خود از رسانه‌ها، ترامپ به طور مخفیانه بین هواپیماها با استفاده از یک کامیون تدارکاتی متعلق به فرودگاه منتقل شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/141095" target="_blank">📅 10:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141094">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5XwuAgkrXgiysEJJIrwVn2aoh3CNfEk90ndDYtGj34iUkQ6R2GbWB0ANOkJGNbTJF6RA_elXMGjQ7d2YfP3CjFz6FrpRxvALFHIZQmJ85VjYn6vUZ1ogsAQ2Pi_HYGoroa--raixXftbkMQ7lnAS5KnjCR4KbvWNO7nDeboKkGqXorjqpmoESyNpYtuTEWBMF7GKXMrtg6iv0kCEn4CoZsCpket6_L9BGU1QXnWcnF2qkAyegkyUJU3IqxLrMH3HzO3LUZpozZdGNVvC99jcCpX3EmRysWePQDTtWzv9qYF_3ybU4VpOUoGeMZrWoFxJOYJAZGwomuFqnFtJMIbtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق ارزیابی اطلاعات نظامی ایالات متحده، اولویت استراتژیک ایران از برنامه هسته‌ای خود به تنگه هرمز تغییر کرده است، طبق گزارش شبکه خبری ان‌بی‌سی.
🔴
مسئولان نظامی به رئیس‌جمهور ترامپ هشدار داده‌اند که هر عملیاتی برای به دست گرفتن کنترل تنگه، طولانی، پرهزینه و مرگبار خواهد بود و هیچ تضمینی برای موفقیت وجود ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/141094" target="_blank">📅 09:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141093">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e070d14b5.mp4?token=CdAQVzljlXRMLoTTViz3wCQonI8Yn_zsKunY15XZauQ_65bQgCPl2IFtnKJd49Bi2x3J0hYby02Lx04swSw63mTrnc4r4AuLwMETNXg50aNN9uDI6holY86AfwHTIBLk3neLjygOAhvBBcrVWgEKvA1qDnEnjvs7D4uD_Zjc_WRgOyx0n5cNn2zhtE8Wl5Mua2cA9xHRSy8Qrf-1dlzEc7ipDPTq_Z5PsegCEtLncGooUPean7d7O0ppLrG3p3SywAjGHfY-nK8UHKPlMt4Anb9-oxPgxMVLyYpLx8WN2gEsuDlhj0Ri-S5NUgjxCuDourq1KVqymnmN4pEJoj42xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e070d14b5.mp4?token=CdAQVzljlXRMLoTTViz3wCQonI8Yn_zsKunY15XZauQ_65bQgCPl2IFtnKJd49Bi2x3J0hYby02Lx04swSw63mTrnc4r4AuLwMETNXg50aNN9uDI6holY86AfwHTIBLk3neLjygOAhvBBcrVWgEKvA1qDnEnjvs7D4uD_Zjc_WRgOyx0n5cNn2zhtE8Wl5Mua2cA9xHRSy8Qrf-1dlzEc7ipDPTq_Z5PsegCEtLncGooUPean7d7O0ppLrG3p3SywAjGHfY-nK8UHKPlMt4Anb9-oxPgxMVLyYpLx8WN2gEsuDlhj0Ri-S5NUgjxCuDourq1KVqymnmN4pEJoj42xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارولین لیویت، سخنگوی کاخ سفید: به لطف رئیس‌جمهور ترامپ، هزینه زندگی در کشور ما مقرون‌به‌صرفه‌تر شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/141093" target="_blank">📅 09:42 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141092">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pa0-eZU3-k08xOGXmjcLE0xi4_JgjaUoW2Sz4GpwNW1NfFczvtMnyvlYCsJwawe7cQoxH-n3DqEExJxZMVZhOHZXDGxDaGp3fZQ4cas_ovHI7j6xMllSGLm1XfQa2VW8uDhHSIi-vhT5-dk7AKmtV_60rrViKDwHkh03LC_no51ER_fZEIgDvrBynFJPDPj3qZiZt6gxR-dVgQsIFtgIctYU7V2EVfZNn1WEY9lM2cwtkYB4mbsLpazZUj8FpNW6q-K9t-nv4NY94GSpUbPIA1rjPBUXwwKHLY2w3g0Au-QVTjZ1_5JRRk6lcklcjzzoQpEeMH2GPqbeiUw5OyDy4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ درباره ال-سید و نامزدهای حزب سوسیالیست دموکرات: آن‌ها برای خانه‌ها و اموال شما می‌آیند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/141092" target="_blank">📅 09:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141091">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ترامپ: ما سه استراتژی برای برخورد با ایران داریم؛ نخستین آن‌ها زیر نظر داشتن میزان وخامت اوضاع این کشور و دومین آن‌ها ضربه شدید به آن است
🔴
استراتژی سوم فشار اقتصادی است و ما در هر صورت آن را اجرا می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/141091" target="_blank">📅 09:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141090">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
وال استریت ژورنال: کشورهای منطقه آماده پذیرش کنترل تهران بر تنگه هرمز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/141090" target="_blank">📅 09:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141089">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oexA236D3bjx0WBtwOAHsypw62w-pVccEe49Lo11OemYRFqAWIXnRcE5ocQhuSizLPDp9cBPVcPlJKf_WLJ0lLCQbfAT_C3opfXFi9syKbYzM1d-9XjPsasOkPHIBVnccb-gZ8TWD_nex-ta4oyM4VVCtGKMoTcLnUDDZVB-M2kZoT24SSKBD4pkkHjYHV-lP72rzvUR3Rof2UBVXFEV9YueQWw8CgfHGowMjJlBVSqeg5asxL13ge3YpNvHT41Q-XsXkWySH3mRE7whP3M3-Dq0Ci2pqLtZqM3P57WU6Apo8-klTR-sBoSa-7o8Coe0pZsi8u9ZywHqf1mDZ0DB7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نهاد مدیریت آبراه خلیج فارس:
آمریکا در فرآیند درخواست مجوز عبور از تنگه هرمز دخالت می‌کنه، از این به بعد از مرورگر فایرفاکس استفاده کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/141089" target="_blank">📅 09:07 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141088">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9HNedwpm-iOKnqFw3PidlzZw_nMRYoJsxPWOFCrjt6lldAldklzKAdnohYv6cDqH0VbIbQudnrJyJrKyLy9LOfZabZ-WggXuucRDGGa_xqgUUq0R7lqCi1x_OsKTgAoSacZ1IugGKBFku9l9yrHaHP1qiKdogwMjJvkiwIqFRgbEkxSx7seZHTRg2kBWnx2PPZknu7SbYHXVMqkpPPsiRxAHanJM2L83ybr3q-wwW7bfK_UNoWyrhVBvkaSr_7-VYFTERBw2bLoZNYtzDaJODtlDZECEuWGTcfj4_KTjL_299AqBn7H9NG1WEmYM6utA4w5s0ITlIJOr_MOAG3uZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقایسه برترین اقتصاد های جهان در سال های ۱۹۹۵ و ۲۰۲۶:
🔴
سقوط رتبه ژاپن، فرانسه و ایتالیا
🔴
صعود قابل توجه چین
🔴
رشد اقتصادی خوب هند
🔴
خارج شدن برزیل از هشت اقتصاد برتر دنیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/141088" target="_blank">📅 09:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141087">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8PEOd_9mrLIwzmTvrL1Kh__bym5BvgaX5bk_skU8CEw9mQNz0Vaj4rrjA0RjhkfyBq0cD7nmWwMVGRaG5WxPnFAV39Cv6fLL_wZvLjHxh4AI4lGSm7Mwsue_3uGXXqeAkoyvDkim_4z4TfktmJHlm-e4x74bNnpRzuqE7gAr6ffMkwwqwsBe4ImTRp2VvuOLB2tuBiu0q_t7X6MSL9n62PSG4pXip6NCaewTHuJOZ_sJlBwx6rpdHanGAXnQXKj4DLQ_VidUslH4THbd6yTsqwzxu9EGjVu4LiwyvNv_LPagtgrWRUcwyVEB1DOOBn7CG1tqSDgnw7flMQDnucvBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، آخر هفته در زمین گلف خود در بدمینستر، تحت تدابیر امنیتی در کنار یک سامانه پدافند هوایی کوتاه‌برد AN/TWQ-۱ اونجر (SHORAD)، گلف بازی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/141087" target="_blank">📅 08:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141086">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3946ed98ea.mp4?token=Ggb3wb7Z-VcecbCyrqgHbhToQlkT6IMxwMHqzDAjtA7f1maG3pQpfyoAVQ6oNfB48O93MiD7cnzCOtCugsjs-Y2GRV2wR4WrzOH6evs55TvAHuo_M99ImNEE34qh9xQVQTQ8v9pi8_8UsDlqEVNf5sjYfoW31RYVuuGQ4jMPmMDURV-zLVdAOcIPFtRU48bE2jz8VreQT99MN9RTIXxgPKoy658YMctwhff6TEBqGb0bfKeU1AS1FYXBu7kkXWMSFR7HBR_vTA5iMQHw7gi_H7d5ZvhEXil27_IfUjC7M-cqr3BbETAIkx_Qg6Ds2_JpNFfoGpBigV9WVjIurscCvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3946ed98ea.mp4?token=Ggb3wb7Z-VcecbCyrqgHbhToQlkT6IMxwMHqzDAjtA7f1maG3pQpfyoAVQ6oNfB48O93MiD7cnzCOtCugsjs-Y2GRV2wR4WrzOH6evs55TvAHuo_M99ImNEE34qh9xQVQTQ8v9pi8_8UsDlqEVNf5sjYfoW31RYVuuGQ4jMPmMDURV-zLVdAOcIPFtRU48bE2jz8VreQT99MN9RTIXxgPKoy658YMctwhff6TEBqGb0bfKeU1AS1FYXBu7kkXWMSFR7HBR_vTA5iMQHw7gi_H7d5ZvhEXil27_IfUjC7M-cqr3BbETAIkx_Qg6Ds2_JpNFfoGpBigV9WVjIurscCvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حرکت عجیب رامین رضاییان و نمایش دادن تیپ و لباس ایرانی‌اش
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/141086" target="_blank">📅 08:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141085">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
سی‌ان‌ان / توقف مذاکرات اسرائیل و لبنان با میانجی‌گری آمریکا
🔴
تلاش‌های دیپلماتیک دولت ترامپ برای صلح خاورمیانه به بن‌بست خورد. منابع اسرائیلی تأیید کردند هیچ تاریخ مشخصی برای دور بعدی مذاکرات با لبنان تعیین نشده است.
🔴
تشدید حملات هوایی و اختلافات ارضی بر سر عقب‌نشینی از مناطق، مذاکرات رم را ناکامی‌ست
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/141085" target="_blank">📅 08:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141084">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
وال استریت ژورنال: ترامپ به راهبرد قدیمی «فشار اقتصادی» روی آورده، به امید اینکه در جنگ با ایران به نتیجه‌ای جدید برسد
🔴
او به مشاورانش گفته ترجیح می‌دهد دستور حملات بیشتر را صادر نکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/141084" target="_blank">📅 08:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141083">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ترامپ به شبکه «ریل آمریکا وویس»:
ایرانی‌ها بر سر مسئله‌ای توافق می‌کنند و سپس بیرون می‌آیند و به رسانه‌ها اعلام می‌کنند که چنین کاری نکرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/141083" target="_blank">📅 08:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141082">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7cvvDM6SJiUcMsozGDuSaQLmyNUThjQ-RZ1KeSdn-K110ZESBvxSGA_EaRjVEEC1U3aatJgf0oBPLiSX3UUGRfGFTIBQn7qrc7jYKUJFbYDL2kMJzynjnF42JLnnL4wLZ0617mSVBFIZYQTP1aCuh6WJPXkXXA2rBqcr4qctsA-EjNTPRHK9EQcFQaESaCNU9-XPzHuCxQ4X8i7mesT4Bmo9MHsKEmdUTfvYLkW5sA_CfTwvutXAaUyQYIoOKaDzUYTtcsOBYPBMqS8NrkAjT_WT6UQJDEBdLmq6Ul8oj3mC3Xp48x7JCqDCQSx43ZkaFlrBQBqDLZUrTejQUgPbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : اگر فدراسیون جهانی فوتبال (فیفا) به هر دلیلی به فکر برکناری و جایگزینی جیانی اینفانتینو بیفتد، مرتکب اشتباهی بزرگ خواهد شد.
🔴
او فوق‌العاده است و موفق‌ترین جام جهانی تاریخ را برگزار کرد که سود آن چهار برابر دوره‌های قبل بود.
🔴
اگر او برود، فیفا دیگر رنگ موفقیت و سودآوری را نخواهد دید! از توجه شما به این موضوع سپاسگزارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/141082" target="_blank">📅 08:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141081">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqTW44DCvJo23t4JONp-qzz9rhE6JllAbiOZR_ObznDL2pAdIB_ARXR5CBzHf-AxRLuycEZHpfxKV9-MY5A7AYW7fRHPgSA8RbO0PFBFgdc2UjyomvkiI_cpmyHY53G3rDkUzxcaKjjZVwlpU0OvV9js0Lshqoj4gRko0wBsfKvi-cnbXdFq0nmPl5ZtVaz9aId3ZaD5usARDM1D3o0Y5IlCTJ4rOYEHvPs81P2hMaFk3lDMU7NpvSNUj8hhW20tHlrwgVjTtC9BzXr52nMQsJ-ewpJjzjcVPzEMbTs1RGChNqQRIk_Noui6xr-DXukaMy-ULZeLMT9p_XqZE3C8bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه نویی: پاداش ۷۰میلیاردی در مقایسه با سرمربی‌های دیگه ناچیزه
🔴
مهم این بود افتخار آفرینی کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/141081" target="_blank">📅 07:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141080">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aaaa507a1.mp4?token=MAkNsa-_M8aIEFW5lwHBqsbCLfroNnf5s7jY3m7F-mWv3PDayBEHgIqIEH4-oyVVOMg4W-aDSYqPbW2o_4eHXI46O7c7AXUguhKCdex_BVjsuTK_rE34FbHQ5v7Ypa3Xkqq0ikJKouoYlFr45BLUsD1PfAw6VSlHz0enDzJ2YpNAqqVyzBN6yOoER_OkbwGw2A5PnpQT0g48MzGHrkgCQ4O3kp28_kAViUPxCqETOwoFvTksiox50v89tYKF1qFPYNKod-djk2v6kN9lHC0vyfiQtfwReDY-hdnM92Yo_yxm6OqxyGf6YRcfTIbO9d31LKKig4vXj_O3rR38Qzyq4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aaaa507a1.mp4?token=MAkNsa-_M8aIEFW5lwHBqsbCLfroNnf5s7jY3m7F-mWv3PDayBEHgIqIEH4-oyVVOMg4W-aDSYqPbW2o_4eHXI46O7c7AXUguhKCdex_BVjsuTK_rE34FbHQ5v7Ypa3Xkqq0ikJKouoYlFr45BLUsD1PfAw6VSlHz0enDzJ2YpNAqqVyzBN6yOoER_OkbwGw2A5PnpQT0g48MzGHrkgCQ4O3kp28_kAViUPxCqETOwoFvTksiox50v89tYKF1qFPYNKod-djk2v6kN9lHC0vyfiQtfwReDY-hdnM92Yo_yxm6OqxyGf6YRcfTIbO9d31LKKig4vXj_O3rR38Qzyq4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جانباز شدید شیمیایی: لعنت بهتون که با این وضع بدنم باید با تاکسی کار کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/alonews/141080" target="_blank">📅 07:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141079">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghoXeQYbH3MgkwIScDhitZNtVpACFAowqwim-CNg5LAxIyeZsuN4R2sqXuiqQBp-nTVsqSajzzYNqYTdCFc7p1wAVkY3i8BlOGPzlJEOwbeGbWXvF1t04PWEh6Q674lDKBOqDkI3WtHsd55x7yMnsdUPwRCKX6mKA5buaLln_4bOa6limrMMhF4cy71J0Io3PE4Hl8DNbL8dFwqOWlz0uRNz3HSFt0GCXW5GDgAGXnnkERMw68d_nqskgZV9RvikSN14BP9tUiLVKIcLCB8m0OAh_QN9A80Dax-4UzcMg4ysRCSEItDSTwv34tbE1Phi5Z5Dn55HnizhtZepywH60Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در حال گلف بازی کردن در تعطیلات آخر هفته
🔴
یه سیستم پدافند هوایی کوتاه برد AN/TWQ-1 Avenger هم گذاشته کنارش
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/141079" target="_blank">📅 07:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141078">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromربات هوشمند اطلس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4L6BYNpNpvcuWACe9S9_nvnJMQ60mdFvBxbOUlYKtKQN2J-5raqu4gqDqJnWc1F4n2Hcujqx5Il02UlPszGgFHwP_k44wDVRz10arUfjNlK9dtKw6Q0-gXRyBA82u4ffNGyDZ7S34ruBEhiRUYGG68qOKNklHYzXG_EjFJKFBxSrM5HAScxT45g2fykbqC5aZcJ2lQOTN4OmiLygUF33MtqcMbKZQPxi7xLMlP4PmFKKfFJynTPxUydkznhEmETrB9XqRYgO4hyWzmL-wyzuVqVImDnRclUZ94LBoulwGbni-HyKe8Zyvm8NRBI3zyZExiNBx3nrcsR5_RyK_9Dbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/141078" target="_blank">📅 01:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141077">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIfM1Hqc1NAZu4kSQVAz7Mqh8GaaVApXYxl4RTPaitcO2iP9uL13Sx8FEwxUA8etu9GLPfsrEj0KQhr-IyJaL7cJ_VHXuACOU1ZEfZszx1ugdcjTWx6XZOIwwpsiJlKV_jJYBa6FnowgrC1ETn1DlJfq0L8gozS0ZgUsSRwVRxrfSTQIl9HzTy-VWyt0ijuM0gXzAgYZ5LYe17YaYCbBhDuLcOG-Ke6RAxg-w7njnIV5d4iCrnlXxtaKiO4Fij0AFFOIE9DrjlO-u_GNQQwDEL0vKWx2xuIOqFfhIQ3A_UQY4K_mjVIIO1RNT_dy5JemtAM4oi-uY8uU3IJjacBa-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقایسه برترین اقتصاد های جهان در سال های ۱۹۹۵ و ۲۰۲۶:
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/141077" target="_blank">📅 01:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141076">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72fee31e98.mp4?token=PqufFp07WV7bcTDe2XXESA5pnutNnEBcbDWcajMUwkwXFqqXy90F1ZiM9xuXzrhOf7HjWEueuV4_ptRAobZt3c2m3oZr2iYqWnZ2DC-QFzTAmtVpWWGBA6df_KlSDU1sZyGjY7lDe6kkMHDxOEw0hnYPcTJEHpwl2FHeG_s4zIvJGFsxzrnxdivmnq8KTcmnlAh8OO3glwXHqsvn3101qGUddl5b3m4xbmlP3_qK9P9hcJPAYFXEyYSZlQdkIxtrFe5qYlgtPn_P3wTIEnZjrs4609Cs10O6NCNA2Cyq-Hp-71mmCC_4hqU5r6E95XiEPNfXrrb6mDeZ3i1Jlo4Uzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72fee31e98.mp4?token=PqufFp07WV7bcTDe2XXESA5pnutNnEBcbDWcajMUwkwXFqqXy90F1ZiM9xuXzrhOf7HjWEueuV4_ptRAobZt3c2m3oZr2iYqWnZ2DC-QFzTAmtVpWWGBA6df_KlSDU1sZyGjY7lDe6kkMHDxOEw0hnYPcTJEHpwl2FHeG_s4zIvJGFsxzrnxdivmnq8KTcmnlAh8OO3glwXHqsvn3101qGUddl5b3m4xbmlP3_qK9P9hcJPAYFXEyYSZlQdkIxtrFe5qYlgtPn_P3wTIEnZjrs4609Cs10O6NCNA2Cyq-Hp-71mmCC_4hqU5r6E95XiEPNfXrrb6mDeZ3i1Jlo4Uzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درگیری های شدید میان نیروهای وابسته به عربستان با حوثی های یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/141076" target="_blank">📅 01:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141075">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qu6m19MaBehHvniI5hLlGgBDoecV_R42kL6MwEs9fWHZrKLKH5vbqUVSIbmIYNJyijLn1EmKKHVRXV8HWBuKxqBsSBtSJyYLZOqMt9xk5J845cKie2nl7LEC91DQzWpw_YElfzjp4EdDwwys5fsuuo_iDhbaod646bhVHk5wiUMoYQY1wu38ZDY47a4Sx22C-BLMOBkS_jlFHVzUTYyBgOKJePMdcNPEytbCbCV0op4utNyH897rv0BMIUUmXqfCAQu6EVC4YawqYIqFypWKogBT35rtNv6cW5VwgU-iiR7cc5u3TLTumI6oqyGJTyHXrpqDAK603HuupK1Q_0XiBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رامین رضاییان یقه باز اومده بود شبکه سه و بعد 2 دقیقه تذکر گرفت که تحریک کننده هست و یقشو بست
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/141075" target="_blank">📅 01:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141074">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd53e67cc8.mp4?token=eUwKcfRPYadscOQ1E-VI02Mb2G5mgqwdelnHSlH8yoXTdHwDwT25DfnwN89gHnqrqI7kHhsH3neoHJsP6zj8dNqOJYqcq-jZdkmkbZfaeGIcGuCNk3RIY3WEBvwmIgFMpQIC1apmaIAwxYgi6iFMKdKoO0Bj48ILQOzE7Mw5_zsfSDZwjOiHlHTiFRp6uj-hYMKPLPnaz-emcJV3wb8jTelKeLItuC9z2SN5gPnnBkrK-J1_MB1uPyXuvAdCCk4pkhVHGRhy1Zh-p-bjdknWOZymYGPdJPj5zuzNOianc6Sun2hvPe6EGqy_X0ucjBJvvj5KymBEETpLHJJh8Tnbzk5WFFOakWxqW_FzOmEmr9pzOarxUfraJDmoSD8m9c647uZ437b6KiYBcsn6ISNEgksI5_6mzZtZ0X1fvIOMR8YpKL3CbWxK2TO5CYUTCo9a4_3o-oXJgTSfK4omaGpnaRbA23Bw5cNoesKjbknsljJ10dD5f-YUbSbscrAiM1OFguMXllCW4XzczP6wD7Tila5GomHHwFL-7phbwcY8hTqWoq55aAmvLC7I_qGec1FlcViL4zs6SXP_wHIkBmu_Bu7iTwKjWvYzTLY6Aet5_pLJBufJF1QyER2HVG_wa_SxrghFXdIYIUpDxECAWxNpdw1EA0hzDyoZ0smAOEyfP-I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd53e67cc8.mp4?token=eUwKcfRPYadscOQ1E-VI02Mb2G5mgqwdelnHSlH8yoXTdHwDwT25DfnwN89gHnqrqI7kHhsH3neoHJsP6zj8dNqOJYqcq-jZdkmkbZfaeGIcGuCNk3RIY3WEBvwmIgFMpQIC1apmaIAwxYgi6iFMKdKoO0Bj48ILQOzE7Mw5_zsfSDZwjOiHlHTiFRp6uj-hYMKPLPnaz-emcJV3wb8jTelKeLItuC9z2SN5gPnnBkrK-J1_MB1uPyXuvAdCCk4pkhVHGRhy1Zh-p-bjdknWOZymYGPdJPj5zuzNOianc6Sun2hvPe6EGqy_X0ucjBJvvj5KymBEETpLHJJh8Tnbzk5WFFOakWxqW_FzOmEmr9pzOarxUfraJDmoSD8m9c647uZ437b6KiYBcsn6ISNEgksI5_6mzZtZ0X1fvIOMR8YpKL3CbWxK2TO5CYUTCo9a4_3o-oXJgTSfK4omaGpnaRbA23Bw5cNoesKjbknsljJ10dD5f-YUbSbscrAiM1OFguMXllCW4XzczP6wD7Tila5GomHHwFL-7phbwcY8hTqWoq55aAmvLC7I_qGec1FlcViL4zs6SXP_wHIkBmu_Bu7iTwKjWvYzTLY6Aet5_pLJBufJF1QyER2HVG_wa_SxrghFXdIYIUpDxECAWxNpdw1EA0hzDyoZ0smAOEyfP-I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز اولین مراسم «World Naked Bike Ride» تو برلین برگزار شد
🔴
صدها نفر از طرفدارای برهنگی تو برلین آلمان ، بدون لباس و لخت مادرزاد فقط با کلاه ایمنی، سوار دوچرخه شدن و بیش از 30 کیلومتر تو خیابون‌های شهر رکاب زدن و کون نمایی کردن‌.
🔴
بیشتر شرکت کننده‌های این مراسم گی‌ها و لزبین ها بودن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/141074" target="_blank">📅 01:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141073">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f50d827cb.mp4?token=apYlH6-8uEvovXqB3hqDP5Pmbdkxp3plg8Hm4xR9K6M9gn9itlUJX-1luCrtVk6seHtIkHRNe2kKS3Bt7MawI63tY-B76EVicSM87HIM0WypwN2FjJTyUtWpm0wBxV_-hQHGghLKmdZcjHvdroWHZrYSuQabA8Wga-QOF2e0UQ3lC_tQxw_Qp4_gvepVt6zcC0PaUHLtUESicGJ48DgzMBd0x2zzPFxIIhIshhbYN7WPMULjEXruoZXUTiXVcayS1Z6ZxgMGHFxWyvcKsbH3RjUul9ltFw6ykCDa6Qz80g4GNeXp635V5kLUk-A0WXGo7IexgzwsQsiJG4smgoLKZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f50d827cb.mp4?token=apYlH6-8uEvovXqB3hqDP5Pmbdkxp3plg8Hm4xR9K6M9gn9itlUJX-1luCrtVk6seHtIkHRNe2kKS3Bt7MawI63tY-B76EVicSM87HIM0WypwN2FjJTyUtWpm0wBxV_-hQHGghLKmdZcjHvdroWHZrYSuQabA8Wga-QOF2e0UQ3lC_tQxw_Qp4_gvepVt6zcC0PaUHLtUESicGJ48DgzMBd0x2zzPFxIIhIshhbYN7WPMULjEXruoZXUTiXVcayS1Z6ZxgMGHFxWyvcKsbH3RjUul9ltFw6ykCDa6Qz80g4GNeXp635V5kLUk-A0WXGo7IexgzwsQsiJG4smgoLKZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یادی کنیم از صحبت‌های شخصی که مسئول امنیت فعلی کشور است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/141073" target="_blank">📅 00:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141072">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
قاآنی وارد بغداد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/141072" target="_blank">📅 00:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141071">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23ea8c6877.mp4?token=WV3s3W709bPrfYuJ8HjOEKrrqsKvIGYEmHvo74t0VgKEqcStq6OTZtVwBzD-OjTcWT73qinawEbvRO3DKSeEK9E5T0L6GTQ0dvitQ5mgONpXBEqIXGxEVpD3HtiztAkIMf7VLsEH42ZT1mfRMAjM3CZJOSS8MkK__AC07U_i6Cxb96ogcEYyUKk9_qJw2rOUPjK1SFnXt2i0Bkw0ucBCcRPgj2KSOZ6bQhQStxAROjR_6H7wvhnlQAgSXY5zt4-xOAhZmwM277is9rVm2ahe87VqOBeQKfPtsPBLFaTClNoUdRQShgSiNaTbfPSQFFzhbmfCu6IUN5TDPbjI7UtluA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23ea8c6877.mp4?token=WV3s3W709bPrfYuJ8HjOEKrrqsKvIGYEmHvo74t0VgKEqcStq6OTZtVwBzD-OjTcWT73qinawEbvRO3DKSeEK9E5T0L6GTQ0dvitQ5mgONpXBEqIXGxEVpD3HtiztAkIMf7VLsEH42ZT1mfRMAjM3CZJOSS8MkK__AC07U_i6Cxb96ogcEYyUKk9_qJw2rOUPjK1SFnXt2i0Bkw0ucBCcRPgj2KSOZ6bQhQStxAROjR_6H7wvhnlQAgSXY5zt4-xOAhZmwM277is9rVm2ahe87VqOBeQKfPtsPBLFaTClNoUdRQShgSiNaTbfPSQFFzhbmfCu6IUN5TDPbjI7UtluA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اولین تصاویر از ۶ متهم پرونده قتل حمیدرضا رجب‌زاده
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/141071" target="_blank">📅 00:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141070">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">جهالت و حماقت چیست؟
یعنی با فیلترشکن بیای تلگرام و اینستا و از تفکری دفاع کنی که این پلتفرم هارو فیلتر کرده!
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/141070" target="_blank">📅 00:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141069">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
گویا بساط تجمعات شبانه و ایستگاه صلواتی‌ها بعد ماه صفر جمع خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/141069" target="_blank">📅 00:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141068">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ken1K4SLU5Q_aXxmFrt_T2CfHeccxxMYa2adUkZ9DAYO1_fAgYuPRwEGBSPE9bx1_rFpz3bsLPbk3tacrXkKdTZu-jYMRG_9q-y4mOvBHZRmjif1jHz--5qvw0Om7NUvrr5PktNkieft4quqZYiDNOwFHYVclQfc8b810bCkqiG_9ZhNJHIs2ijylrjueXaKoZpCnRyaBYf6r6QxShdq82hFRzuMBAN0Sj9PRBkLWFQnHeEyxBpfeDuFt5DWIr08gcOnbgNSXnqOIdChvinlPyyWHYeBEl-fvOb4syji2LCPp81VhH9u4STqpZQmTODNHxrAKt4OHD8BqsjyKcKK6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم‌اکنون، فعالیت هواپیما های سوخت‌رسان عربستان و آمریکا در منطقه!
🔴
همچنین یک آواکس آمریکایی درحال فعالیت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/141068" target="_blank">📅 00:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141065">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d274135cb9.mp4?token=HrneXvK57cG6pPAUc0_djks9wd8KprDgKNp8h4HRRZ9YtekyFrI27QAiqz79E8_1j1rT3NeZWFPbf8VEcVUB10uwdgtHja5-pzlOV0hFDz0W8LXCI_kVMuWqB2bK1ZNn-VD1AQq0ie7VuTxla3qQrOBR35a_z2jBDkI4MeKaZfhYWqGoAWVPdnoiE2QlXGKhWGLEMpcEM1qv4oRB2Ly8SFB4rMGVho0MB1gF4S-041kfsd9X06LhoMneIhnAzrE802KhHZ0BL1WXjtdj87A5vNwAWsPZ8YfPIxwZ5EByvgozcgxfRnnhyXGtcZloLgQN6_ROpSzvLT7lNcBt7e4WdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d274135cb9.mp4?token=HrneXvK57cG6pPAUc0_djks9wd8KprDgKNp8h4HRRZ9YtekyFrI27QAiqz79E8_1j1rT3NeZWFPbf8VEcVUB10uwdgtHja5-pzlOV0hFDz0W8LXCI_kVMuWqB2bK1ZNn-VD1AQq0ie7VuTxla3qQrOBR35a_z2jBDkI4MeKaZfhYWqGoAWVPdnoiE2QlXGKhWGLEMpcEM1qv4oRB2Ly8SFB4rMGVho0MB1gF4S-041kfsd9X06LhoMneIhnAzrE802KhHZ0BL1WXjtdj87A5vNwAWsPZ8YfPIxwZ5EByvgozcgxfRnnhyXGtcZloLgQN6_ROpSzvLT7lNcBt7e4WdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه انفجار تو تأسیسات ذخیره نفت الزاویه در لیبی رخُ داده
🔴
در پی این انفجار، یکی از مخازن سوخت آتیش گرفته
🔴
علت انفجار هنوز مشخص نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/141065" target="_blank">📅 00:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141064">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81c239e89f.mp4?token=kvL90In_TMOr0L-pnSJc43zBaGoQoIytBS4bgNvPUbLYKxonI3UacGWAVJ1XQXtFtl41i3xhhuGg4BuVhqTTrEkXzotn8MDcn5brqXQG9PA9SnODOb9MJz7Potl3Xcd4SlLM1bGh63gORzAFTBwcnoklq5NtKug6-nOCNyuoHWUQEKTR58q7FhQbK2pJVs7l0KwNmRFWFwJvORRfUv2Sb2y9QvI34NfSTkFSbNzCF2RQ74k2jATfxc8z0wUO3d2IFM740XSuK2LBsexHbidd7c--P8A3Y9goRpkdwXNG_UwEzrw3lmKZSx8V5toD8Pa_B7kKHEtt-fjkbMPRUYRVAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81c239e89f.mp4?token=kvL90In_TMOr0L-pnSJc43zBaGoQoIytBS4bgNvPUbLYKxonI3UacGWAVJ1XQXtFtl41i3xhhuGg4BuVhqTTrEkXzotn8MDcn5brqXQG9PA9SnODOb9MJz7Potl3Xcd4SlLM1bGh63gORzAFTBwcnoklq5NtKug6-nOCNyuoHWUQEKTR58q7FhQbK2pJVs7l0KwNmRFWFwJvORRfUv2Sb2y9QvI34NfSTkFSbNzCF2RQ74k2jATfxc8z0wUO3d2IFM740XSuK2LBsexHbidd7c--P8A3Y9goRpkdwXNG_UwEzrw3lmKZSx8V5toD8Pa_B7kKHEtt-fjkbMPRUYRVAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هانتر بایدن: اگر اشاره به این موضوع که بنیامین نتانیاهو تجسم شرارت است، مصداق یهودستیزی محسوب می‌شود، من نمی‌دانم دیگر چه بگویم.
🔴
فقط کافی است چشمان خود را باز کنید. فقط یک دقیقه قلب خود را به روی این موضوع باز کنید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/141064" target="_blank">📅 00:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141063">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cb641b316.mp4?token=XySP4zxmqmNEjlpgCXRGwiYg7muVrAO0s13b1LR65fUCcwU3Wxr6dF4Y3CDEsGbpeg1s-7HWHsPNBJTplfdk449hJ6I-LrZU8L_K2wGlE5iqkiXUuhMXNpMnJ7RqKSj5lCQ-TPzGkCE-mDDv2uDD75tkX5LH_NgN0mFaOxAUG5BUYCltU_ZYdNg-iexhYVv5IymMSyZSG-D78orXv2_PZU_3UkBSKul0LzN1gMB394zqb7LsE9y0ywgEj47IQHBuIxtHqjvWU4pC_lvJc7l4Gp3PKcmTc8UcN5AEGK0rmhToHQFE_u-NnOMd-DvLKUWnpTx6S69aJbN8PCv1TCx28k8OuJaXLKsIx4SbCc8RVrCMYYDbaKfT7to-W25QdYTOVZ0s63ka768EsrW1V9X22Sh9YxxJ1E8Mp4W_PeMg1rPeLwQTF50AdvGI42WLW2-ReAsztmQM4l7y523FbauyVtN9qk2AF8QjjQGahATMuA7SeBxtWh7n5jeUZNa8NA5PwIPYHfh7j8LAdyDPlg3ObTHRbzcYhpZqqMR-wiKeu3KDyCGvKZJqBWvxGSJyhpy7jJANUdaL0-PJpqPhPE6MaAf8mmavjjB6RgyEuJpM8FtfwSegOEpOiN3U2vY5HDrfWnAaRou5DAhGyjgeW2twMRbRoqONyz7kNOKBJNF56Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cb641b316.mp4?token=XySP4zxmqmNEjlpgCXRGwiYg7muVrAO0s13b1LR65fUCcwU3Wxr6dF4Y3CDEsGbpeg1s-7HWHsPNBJTplfdk449hJ6I-LrZU8L_K2wGlE5iqkiXUuhMXNpMnJ7RqKSj5lCQ-TPzGkCE-mDDv2uDD75tkX5LH_NgN0mFaOxAUG5BUYCltU_ZYdNg-iexhYVv5IymMSyZSG-D78orXv2_PZU_3UkBSKul0LzN1gMB394zqb7LsE9y0ywgEj47IQHBuIxtHqjvWU4pC_lvJc7l4Gp3PKcmTc8UcN5AEGK0rmhToHQFE_u-NnOMd-DvLKUWnpTx6S69aJbN8PCv1TCx28k8OuJaXLKsIx4SbCc8RVrCMYYDbaKfT7to-W25QdYTOVZ0s63ka768EsrW1V9X22Sh9YxxJ1E8Mp4W_PeMg1rPeLwQTF50AdvGI42WLW2-ReAsztmQM4l7y523FbauyVtN9qk2AF8QjjQGahATMuA7SeBxtWh7n5jeUZNa8NA5PwIPYHfh7j8LAdyDPlg3ObTHRbzcYhpZqqMR-wiKeu3KDyCGvKZJqBWvxGSJyhpy7jJANUdaL0-PJpqPhPE6MaAf8mmavjjB6RgyEuJpM8FtfwSegOEpOiN3U2vY5HDrfWnAaRou5DAhGyjgeW2twMRbRoqONyz7kNOKBJNF56Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مهدی تاج: به قلعه‌نویی ۷۰ میلیارد تومان پاداش جام جهانی دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/141063" target="_blank">📅 00:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141062">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uo-otE9wIfXDHNu2sHHe1LxfHrxySubjIZt8JPzHaP1RyqfVVYYElDOzHwN_5NEVpSOe-iJM-LxugWP2GWf_zk5_lDP3qcuTUoaeib3V80cjne7wFK1vJygv-PwvZZ3XxLe-7Hjz1TQOCWCqgWlZG2bRxEsJtL1Og-PyBVpKeE3my0ymj4d4hqdxNQUHbGC-vwUF_OeJdp1f-0nv-T2pc3fvmMz3DnfU4n7Fw0_Q062wE0Vui652W4JK2eeqh4-j3aa7XccqE15tWWMzGrRnGfmGugtOmF7B7Z01d_y0AlkCGzpXL4ee4Ul0mZS5zsVLG8MBa-e4gmwdVV0BDv9WoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
احتمال برنده شدن نامزد دموکرات ها در ایالت اوهایو هم از جمهوری خواهان عبور کرد!
🔴
تا الان در این ایالت شانس برنده شدن جمهوری خواهان بیشتر بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/141062" target="_blank">📅 00:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141061">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVthZJROrxdc4HDrHa-LZAh1P6aPMKozJKU0rZnP8ZBFlkAxxnfvFhuAFmsau9Kysa0lM43D301lcZOqo2CcjTFiv6zO6C9PDQRv2OShZ6oqGeAGW335AI3sey4KNFQzEuMUa1dxxRiFaJbiasCc97gcENBbVI34Y98uz0c--vVEaNU3GY1lrC36aFJqSQ2rvcnU1m17XlQkc0Tnbg1gXeKrLmvB_v7uhoLh6gElAglpcj9Blsu_nF5m2YjW0cdSQ8MYYsQ60t6p0SsePMYySSrQCDw3bolzimuEFFtG_p6PU0HVLo4aBQydLM3zH3A5exsUVOU6oFh9NMVjvrYKOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حوا رئیسی بخاطر یه جرعه آب دستش توسط تمساح از بدنش جدا شد.
🤔
خدمات جمهوری اسلامی به غزه، لبنان، عراق و مراسم عربعین میرسه ولی به مردم تشنه خودمون نمیرسه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/141061" target="_blank">📅 00:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141060">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
اسرائیل قصد دارد در صربستان کارخانه تولید پهپاد راه‌اندازی کند.
🔴
شبکه ۱۲ تلویزیون اسرائیل در گزارشی اعلام کرد که این مسئله را رئیس‌جمهور صربستان هم رسما اعلام و تاکید کرده است که این کارخانه بین ۱۵ تا ۲۰ سپتامبر راه اندازی خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/141060" target="_blank">📅 00:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141059">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
یدیعوت آحارونوت: توقف عملیات‌های بزرگ علیه ایران ممکن است تا بعد از انتخابات نوامبر آمریکا ادامه یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/141059" target="_blank">📅 00:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141058">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
عراقچی: جهان آمریکا را به خاطر انسداد تنگه هرمز مؤاخذه کند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/141058" target="_blank">📅 00:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141057">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل: حمله هوایی اسرائیل به منطقه منصوری در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/141057" target="_blank">📅 00:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141056">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IezPqUA7U3zXMFrJYtvEd5wypudwyiTRtZ-2H9dGMeDcbqebbALp1OgepvdM5XdTRcMU25IXRHThU48ugoipLHrlaCEysJFThWhuI-7IiTs-FilzMf5h4Z3VshCPQCml8mdIxX8LrC4Y8mpGTpGHGPW34u3PWcQXTdTYpk5qi_Um1jnX72_Gw3Mkjo33b8iPHbU4vwYymgGxbuYcji5HOEWTd9HnnvrO6mBgoqxnUmC785TRNlkzAZxb7rpVqKHLC8Jw5IBtUZxhduLjMM9aUIjxReXV3lCpsbZw9yVAz89ZIRoJd6xFxsuhwMBXsCmzquDr0B24hIpnFgfi2KdTJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش منابع شبکه سعودی العربیه، اسماعیل قاآنی، فرمانده نیروهای قدس سپاه به بغداد سفر کرده است
✅
@AloNewd</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/141056" target="_blank">📅 23:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141055">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOJJWvgByJWnu9MuoN8t8YNNbTq-2mM6MyYnnvYvKtgXixzvOkeDOIG2r1FWS-DS9AyZuLRzSaAj7MYIUmFFxM-HfAjodYsuc9uYfRJSSSdDnJCbDUhgFl1-3ttK1zCkuCtf-OENjR8mLNp5Gc7F5tOfk2RtKYXsczyNxQ4L6z0J1P8znKiTJnY8zUjx8YmkLK6otU7iylgSBqeQCvUd2l_XlshyQAK9rVadffqmiuFegA654ZM86iA6g7x2qEidDcrIAceTFTotsVUq62jpEZhnMkdDcz_dro6DwqBxaL8fc1B35XBOVOL7j0FzJtffoKu7HSV8X4Aq_oTWT4JGOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بقایی: وزیر خزانه‌داری ایالات متحده با افتخار از "خفه کردن" ایران از طریق تحریم‌های اقتصادی صحبت کرده است.
🔴
این ادعا، فراتر از جنبه‌های احساسی آن، گواهی آشکاری بر اعتیاد اجباری آمریکا به تحریم‌ها است.
🔴
این دیگر یک "سیاست" نیست، بلکه یک "عادت" است؛ و خطرناک‌تر از آن، این یک اعتیاد است که خود تفکر را تحت‌الشعاع قرار داده است.
🔴
ایران در طول دهه‌ها نشان داده است که تسلیم این تکرارهای بی‌فایده نخواهد شد.
🔴
خطر واقعی این است که سیاستمداران آمریکایی، که به این عادت بد چسبیده‌اند، به جای آن، فرصت‌های باقی‌مانده خود را برای خروج با عزت از بحرانی که خودشان ایجاد کرده‌اند، از دست خواهند داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/141055" target="_blank">📅 23:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141054">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7692dfa701.mp4?token=AHwZ8iCstwQVWwgvvISvg1UOdpzC96g6fOa_6gTuGjaMV6Dw2JTd3SIidRmGKZH_mA-PqqACfalBaYIAozPZm3eWgGMzTEorA0HnMSXbNMJ0tWFbvV-5L8Q9yvaA66SFt4955HKtklIKG2n9w_LXLDmho65ldQZSIHkWDU5GQBC2JWESdnJ5bcTnAWgzpJ_IzAnAYw6Xn8KRSpg6CgqxDfBf25nuPyb9GqtZJqBFFK9Qr2keJZahM75su2_nERMduvHcqmItzFRF5aYXBIIEgTYxItXzXDGa5XLTQHypGHw6qjQQ3Wb5HlcPX_zPckIwly5bNO--DotRrVRrNzZC6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7692dfa701.mp4?token=AHwZ8iCstwQVWwgvvISvg1UOdpzC96g6fOa_6gTuGjaMV6Dw2JTd3SIidRmGKZH_mA-PqqACfalBaYIAozPZm3eWgGMzTEorA0HnMSXbNMJ0tWFbvV-5L8Q9yvaA66SFt4955HKtklIKG2n9w_LXLDmho65ldQZSIHkWDU5GQBC2JWESdnJ5bcTnAWgzpJ_IzAnAYw6Xn8KRSpg6CgqxDfBf25nuPyb9GqtZJqBFFK9Qr2keJZahM75su2_nERMduvHcqmItzFRF5aYXBIIEgTYxItXzXDGa5XLTQHypGHw6qjQQ3Wb5HlcPX_zPckIwly5bNO--DotRrVRrNzZC6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شبکه ۱۵ عبری به نقل از یک افسر ارشد سابق موساد: ما باید از یک موضوع اطمینان حاصل کنیم؛ اینکه اسرائیل در صورت تلاش ایرانی‌ها برای ازسرگیری پروژه هسته‌ای، آزادی عمل داشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/141054" target="_blank">📅 23:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141053">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
فردا، آژیر هشدار آزمایشی در جاسک هرمزگان به صدا در می‌آید
🔴
به منظور آمادگی و ارزیابی عملکرد تجهیزات، تست آژیر هشدار توسط نیروهای نظامی از ساعت ۱۰ صبح سه‌شنبه در سطح شهر جاسک انجام می‌شود.
🔴
این اقدام صرفاً یک مانور و تست فنی است و هیچ ارتباطی با وقوع حادثه یا شرایط اضطراری ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/141053" target="_blank">📅 23:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141052">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ql_6WnRAxoYw7KwncoNf3Q4DdYqvtstSyT4aGzn4ytQrG-yWVwTKRrpDScHjqaIdx1Z9Q5NfJhFpxO3H82NWiUF3n8Uwbds93gYQqIrsndi4SOrtpnr4iUdbWO9pH2EAur1apsR1SmkC976RVWvPPxJXHSl9DUsY-NNW5AQ63pO1FurFvwpa8EZleWrzg5HBCQsWpjcfWnvL_TP0nq_ijioYnOm3Jx6OuEgk12WTyiSIClklVy5NcsmnM1UGc5XaGxmSJMrqlYPV6zNnhp6PJHQHKw3T4KhZMRvEAPdx6yxzzsOiK2XuE99VAwYuS_ZZ9wTSC6y7O4GqFBMVTmEd7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سربازی هایی که چند سال طول کشیدن و علتش
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/141052" target="_blank">📅 23:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141051">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihB8amc8krEYu1-Bk6L00RD80KVyrK_0X3b_QSOuR9KzvvZ610-K-Oc4mJfqz9KSgai6WOVskp1Qbi-yenygRthBHVK-ByY9yOlTNaY0qUtDMTBTSyLlmpIa3kv2JphYwRG2XdzpKGsPI08HSck8jmze9fex1UBT03eoJlak8gnDMh_JrtusWvmWqBThOI3Obl4a2aVYVRVrVCOnyL2cHq6eFZ-rWynQ-eN2zT8i9k9xYOHQxTv0Jl0NfyXD24OxVZmI0hYWGCAeP4sYu-iS6Jb1Dg9Kw2vxJJRXvou7YvdS08-SJOUA0TE0xiF26zSDNQAUVWQsd3tjLc-Qloz9HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
با ثبت‌نام توی طلاسی، ۳ سوت طلا هدیه بگیر!
یه شروع خوب برای ورود به دنیای طلا
✨
فقط کافیه ثبت‌نام کنی و احراز هویتت رو انجام بدی تا
۳ سوت طلا
هدیه بگیری.
🔸
سریع
🔸
ساده
🔸
مناسب شروع سرمایه‌گذاری
🔗
لینک ثبت‌نام:
https://talasea.ir/sh/kxy</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/141051" target="_blank">📅 23:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141050">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
آکسیوس: آژانس بین‌المللی انرژی اتمی به زودی مواد هسته‌ای ذخیره‌شده در یک سایت مخفی در سوریه را خارج می‌کند.
🔴
خروج مواد هسته‌ای از خاک سوریه پس از تفاهمات آمریکا با دمشق و تل‌آویو صورت می‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/141050" target="_blank">📅 23:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141049">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc00115491.mp4?token=MGnB9PGZwGkzJuB-HFzr8xhRWDCxcGrN0u_lxNJ4ly5upedjdBx6HBcTfhZI6ZRu_fXt-yVnyCq4_1rAZcTdxmlkJXZ0Rr0g4IYyWzjhkxybTiCBElV8_3i4BJK52iMHfomwEzKg7ngnm-Uj1xkP7PAfWAtb76Y5QV886QbzDerlM2sfO9ScyvNsaTtZvP746khx0oEm9hWdhPIUTRlytajxWZOA9CWjfbAwfhTdJ3D7VjP5QwsC-jq2WqvbU4yEiDm9Nwq3ySnQjA8ZArx9Fj-sOh-ipeNZ7ugQ6UQHxQAZ9TixFxL1ABb1aCtr75UwWuXrg73qB-S-I6lGcfQ6dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc00115491.mp4?token=MGnB9PGZwGkzJuB-HFzr8xhRWDCxcGrN0u_lxNJ4ly5upedjdBx6HBcTfhZI6ZRu_fXt-yVnyCq4_1rAZcTdxmlkJXZ0Rr0g4IYyWzjhkxybTiCBElV8_3i4BJK52iMHfomwEzKg7ngnm-Uj1xkP7PAfWAtb76Y5QV886QbzDerlM2sfO9ScyvNsaTtZvP746khx0oEm9hWdhPIUTRlytajxWZOA9CWjfbAwfhTdJ3D7VjP5QwsC-jq2WqvbU4yEiDm9Nwq3ySnQjA8ZArx9Fj-sOh-ipeNZ7ugQ6UQHxQAZ9TixFxL1ABb1aCtr75UwWuXrg73qB-S-I6lGcfQ6dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: پاسخی به نتانیاهو دارید؟
🔴
ترامپ
:
«امروز پاسخم را در تروث منتشر کردم. پاسخ دارم، پاسخ خوبی هم هست. روابط ما بسیار خوب است، بله.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/141049" target="_blank">📅 23:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141048">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e4c4e561.mp4?token=HPixPyL404sBSHOUU5N5SA-LVi4oMeOOjyIupNAOPpE-bBnk10SQJvTLAAgmFWDyT3cF4oXhHPD2smpXTNgggTnOD6w40DeoEYetSngTEF0yRntt_rbE3BVw_PtLVUFP66nfo2EgtgE5JvZgSg0I5bscj2gqjAd-o1G7f350vJKAy0PH5sEFvRhR-AiA-Syc80byxvPpI0CPW7i4xxE0aMDl-HLjMC4LbpScTFO3TuUx2oScB30i9lgWgayjhoop05-6OFrSarRW5gy5nl1r0SLVkCZKrYOE_4o3t0Ew-hYYIxjH7ShYdMKJmUk1l4bBFYTaJzVZOeaYoCiUbUXGYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e4c4e561.mp4?token=HPixPyL404sBSHOUU5N5SA-LVi4oMeOOjyIupNAOPpE-bBnk10SQJvTLAAgmFWDyT3cF4oXhHPD2smpXTNgggTnOD6w40DeoEYetSngTEF0yRntt_rbE3BVw_PtLVUFP66nfo2EgtgE5JvZgSg0I5bscj2gqjAd-o1G7f350vJKAy0PH5sEFvRhR-AiA-Syc80byxvPpI0CPW7i4xxE0aMDl-HLjMC4LbpScTFO3TuUx2oScB30i9lgWgayjhoop05-6OFrSarRW5gy5nl1r0SLVkCZKrYOE_4o3t0Ew-hYYIxjH7ShYdMKJmUk1l4bBFYTaJzVZOeaYoCiUbUXGYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران
:
«آن‌ها می‌توانند دردسر ایجاد کنند، اما ورشکسته‌اند و پولی ندارند.
🔴
ایران کاملاً ورشکسته است؛ حتی حقوق نیروهای نظامی‌اش را هم پرداخت نمی‌کند، نرخ تورم آن‌ها ۳۰۹ درصد است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/141048" target="_blank">📅 23:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141047">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ترامپ: تنگه هرمز در حال حاضر باز است و ما بر آن تسلط داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/141047" target="_blank">📅 23:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141046">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ترامپ: تنگه هرمز در حال حاضر باز است و ما بر آن تسلط داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/141046" target="_blank">📅 23:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141045">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7beecea37.mp4?token=lx_d_v3DFvrIzWMaToQEC-qiyvWqq1ZqvbDv8QXa09OCZxc5wiIdkPrnj8X6TkjF8VJNXVHzeOfL6KeV26bhQuM_O8pOTPQY_f6_48UnL5x4bVjMmgmE5MKT_OD2YqTaNqIGPIm3u-6I4TZ1ephQySxAJVZXWHXa9j9Q76CwmJXoM0utNyJA7rq8ykRrVzvWV6mD4npGMZaNkFhQF1vCKZO87TiN_NHovdGtho79wbOIBQqdAuapnPWfsp6VcUZP7jf5Pq1DKpY1W0fwhWVHuZde2xV5LvXeglTwSB8n0wPymCwsvs11SNxl8sujLBpDIipdfoh3BUWeijngpzZPN7EqJjM-4JTvQWA9XfVdA4r3q068ujXQo1MjxAGg92K_B4FMlTrjhL0R3mo05mT4W0Ljbd0FSi8LTZno7zgl6JlxCtXYe1fISlj2f6NGCAqvD86Xes439lAAIquHJ5e4kVsg4bRvwaBKYsLuWmw8h32Bm3skxnxyddLpMjQxyONY4AJIxUGF_R6qHv2VBEiwLwtrDpJplGLKgbVZi7mJRoWJ__I-FB6-j0FopH_MdxZUxAtID3OEaua9xhuENN6m5u9r4WyqwQBpRlYE77YcrlmWYdYWKoUvmQuVr7AsYAifS01KEqBFdY_kKE2jwf1kZQN_au1RTuNwK7H8VrZnOSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7beecea37.mp4?token=lx_d_v3DFvrIzWMaToQEC-qiyvWqq1ZqvbDv8QXa09OCZxc5wiIdkPrnj8X6TkjF8VJNXVHzeOfL6KeV26bhQuM_O8pOTPQY_f6_48UnL5x4bVjMmgmE5MKT_OD2YqTaNqIGPIm3u-6I4TZ1ephQySxAJVZXWHXa9j9Q76CwmJXoM0utNyJA7rq8ykRrVzvWV6mD4npGMZaNkFhQF1vCKZO87TiN_NHovdGtho79wbOIBQqdAuapnPWfsp6VcUZP7jf5Pq1DKpY1W0fwhWVHuZde2xV5LvXeglTwSB8n0wPymCwsvs11SNxl8sujLBpDIipdfoh3BUWeijngpzZPN7EqJjM-4JTvQWA9XfVdA4r3q068ujXQo1MjxAGg92K_B4FMlTrjhL0R3mo05mT4W0Ljbd0FSi8LTZno7zgl6JlxCtXYe1fISlj2f6NGCAqvD86Xes439lAAIquHJ5e4kVsg4bRvwaBKYsLuWmw8h32Bm3skxnxyddLpMjQxyONY4AJIxUGF_R6qHv2VBEiwLwtrDpJplGLKgbVZi7mJRoWJ__I-FB6-j0FopH_MdxZUxAtID3OEaua9xhuENN6m5u9r4WyqwQBpRlYE77YcrlmWYdYWKoUvmQuVr7AsYAifS01KEqBFdY_kKE2jwf1kZQN_au1RTuNwK7H8VrZnOSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
گاهی دلم می‌خواد از شر سنا هم خلاص بشم، ولی اینو نمی‌گم، این کار رو انجام نمی‌دم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/141045" target="_blank">📅 23:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141044">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ترامپ: رئیس‌جمهور بعدی بابت کارهایی که من انجام داده‌ام، اعتبار زیادی به دست خواهد آورد
🔴
لطفاً یادتان باشد که این کارها را من انجام دادم، نه آن‌ها.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/141044" target="_blank">📅 23:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141043">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb622841e7.mp4?token=fKK5fVixd0fwRYItXDU19it_qzFeHlv7pwOWENyB2oj7oJOnmKSTrFZsWAH0551hSGW5AcxTI3xi3ye79-qGnxxf-APHELiOrLvDzFhdzVjsYd4eshXfOrwaDKwCqewbs4ehnVwHJ3t37vn-WDAGQLCWPeSlHdqDD58gKIeySb5d9dWOOvMK3aTqDHobg-2C9WwxiE7Bfd5kaA_GfQPS-ofm6or6nzSzWGJAvFkxVh8ueYkZKyrlNamGEI2ztny0dxfAdf8oTCqfJsTS0vXNWIen6-lMsPIDe0r6fTcNBo6qDuY7ZhLbD_nUOrthdx3VGOdeplbswS2Y7U1NGD9LGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb622841e7.mp4?token=fKK5fVixd0fwRYItXDU19it_qzFeHlv7pwOWENyB2oj7oJOnmKSTrFZsWAH0551hSGW5AcxTI3xi3ye79-qGnxxf-APHELiOrLvDzFhdzVjsYd4eshXfOrwaDKwCqewbs4ehnVwHJ3t37vn-WDAGQLCWPeSlHdqDD58gKIeySb5d9dWOOvMK3aTqDHobg-2C9WwxiE7Bfd5kaA_GfQPS-ofm6or6nzSzWGJAvFkxVh8ueYkZKyrlNamGEI2ztny0dxfAdf8oTCqfJsTS0vXNWIen6-lMsPIDe0r6fTcNBo6qDuY7ZhLbD_nUOrthdx3VGOdeplbswS2Y7U1NGD9LGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
«از کاری که ما انجام می‌دهیم، هیچ اتفاق بدی نمی‌تواند رخ دهد؛ هیچ اتفاق بدی.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/141043" target="_blank">📅 23:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141042">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ: تشدید شدید تنش‌ها همچنان یک گزینه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/141042" target="_blank">📅 23:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141041">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ترامپ: اگر قرار باشد خسارتی پرداخت شود، ایران باید آن را بپردازد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/141041" target="_blank">📅 22:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141040">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
خبرنگار
:
گفتید این آخرین فرصت ایران بود، حالا چی می‌شه؟
🔴
ترامپ : خودتون خواهید فهمید
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/141040" target="_blank">📅 22:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141039">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
هم اکنون حملات سنگین ارتش اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/141039" target="_blank">📅 22:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141038">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
سازمان رسانه اسرائیل به نقل از برخی منابع: تعیین موعد دور جدید مذاکرات لبنان و اسرائیل به دلیل تنش بین طرفین به تعویق افتاده است.
🔴
لبنان با برگزاری دور جدید مذاکرات در اعتراض به عدم گسترش عقب‌نشینی اسرائیل مخالفت کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/141038" target="_blank">📅 22:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141036">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJqro5e2SNWGMCIwvo3htr3DRKI0C03WemKwImv6xwVolKFoP5ESAvJn4h4_8q4-DifdXt3bSrH-IXbnAkvG7mL3U5_IwjeQPl-Z3UmuQelDtRQzfFhFz8nMNcnvbEBw7BN-IfBAtN2FBxfKWeZvJGf5llD4CWmMzBsUxpZ0LAIpYnmjmLSolQpg8Va21eCeoR7QeHt852J_mbneopKNuYNr_UanJLdO0esex6P3wksvVu-9FBwKF9wf9Fxbs6x_6N9ZcP98NmXFSUeE-tNvKCE0o-pe61RhlwSQ6y0w8B68Z9ilA82VIFQvI8p9hzXMdV54CDiN5hi6KmM65XI1uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28c154e97.mp4?token=lp_Ybbag7dxbXJL2IzIX6N7gAjhrWIYYS7P2Y5gwquKa9VT9tzMwUvMrL5m47VA4KwqMaohGB71k7wtKH5q8dR5_1SeUaXZDiFgySuIgNvz1Jm1XjlcOES0ZL48NYF1nU28wvHEYp1yDrj84_w89SQNE8eivT7TpDUsf5AWAMr6qmCXfyF9LT2r2zqQ6wmH5K9bBSB7vzeb-iqx049pWXmK6x14_10mCFgbVae9VFfflOvGCrgn0KRMTwu33zDm8STM5NG1VYDGHgALX3SYDNBHcKOt-RQ7-VVzNeK5k5zVQEohSrLa5CHIOwSWicDJyTn7_iElsQ5VyDlWT9JXDNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28c154e97.mp4?token=lp_Ybbag7dxbXJL2IzIX6N7gAjhrWIYYS7P2Y5gwquKa9VT9tzMwUvMrL5m47VA4KwqMaohGB71k7wtKH5q8dR5_1SeUaXZDiFgySuIgNvz1Jm1XjlcOES0ZL48NYF1nU28wvHEYp1yDrj84_w89SQNE8eivT7TpDUsf5AWAMr6qmCXfyF9LT2r2zqQ6wmH5K9bBSB7vzeb-iqx049pWXmK6x14_10mCFgbVae9VFfflOvGCrgn0KRMTwu33zDm8STM5NG1VYDGHgALX3SYDNBHcKOt-RQ7-VVzNeK5k5zVQEohSrLa5CHIOwSWicDJyTn7_iElsQ5VyDlWT9JXDNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده میگ-۲۹ اوکراین سقوط کرد
🔴
نیروی هوایی اوکراین: یک جت جنگنده میگ-۲۹ نیروی هوایی اوکراین شامگاه دوشنبه در جریان یک ماموریت جنگی در استان اودسا سقوط کرد و خلبان زنده ماند.
🔴
گزارش‌های اولیه از نیروی هوایی اوکراین نشان می‌دهد که در جریان شلیک یک موشک هوایی، این حادثه‌ رخ داده است.
🔴
علت این حادثه در حال بررسی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/141036" target="_blank">📅 22:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141035">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ترامپ: بعضی گروه‌ها تقریباً هیچ مشکلی با اوتیسم ندارند؛ این‌ها گروه‌هایی هستند که در زمینه واکسن‌ها فعالیت زیادی دارند.
🔴
یک مشکلی وجود دارد. هر سال آمار اوتیسم بالاتر و بالاتر می‌رود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/141035" target="_blank">📅 22:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141034">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2eda49a77d.mp4?token=t_3qNROU-ADj01Ybu6hAons8tnt_wZ1vJ6ir1PUfANlm664vL3-XpMpHRsFOo3990IEUVlnYtOGKJhDyTrg9NzlzHFnmDL0aGR7g6wl3m_OX6GR__6GxknMtixyaz8GcykOVmnl5UoYMIC5V-O4KtLKwEuJ4zP7M4ZEOkXCArzcS0K1az9babEX30xIorGzw12bf5VAWyPEHff4eg2aeZW42IABd-Mpz2t5CKRQcZQVGRnC20vXD74ntv7SmE5hR-sA6mb2lhDcJnWVufMb83tVAubKC54TmWyPNmOnXLgvyFYYRWDbl4tfJ5IR3yn9AyOl1Y6er9zcdiBJMKQgsDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2eda49a77d.mp4?token=t_3qNROU-ADj01Ybu6hAons8tnt_wZ1vJ6ir1PUfANlm664vL3-XpMpHRsFOo3990IEUVlnYtOGKJhDyTrg9NzlzHFnmDL0aGR7g6wl3m_OX6GR__6GxknMtixyaz8GcykOVmnl5UoYMIC5V-O4KtLKwEuJ4zP7M4ZEOkXCArzcS0K1az9babEX30xIorGzw12bf5VAWyPEHff4eg2aeZW42IABd-Mpz2t5CKRQcZQVGRnC20vXD74ntv7SmE5hR-sA6mb2lhDcJnWVufMb83tVAubKC54TmWyPNmOnXLgvyFYYRWDbl4tfJ5IR3yn9AyOl1Y6er9zcdiBJMKQgsDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: دهه‌ها پیش، کودکان فقط بخش کوچکی از واکسن‌هایی را که امروزه لازم است دریافت کنند، دریافت می‌کردند.
🔴
در آن زمان، مردم خیلی سالم‌تر بودند و طبیعتاً نرخ بالای اوتیسمی که امروز مشاهده می‌شود وجود نداشت.
🔴
دلیلی برای چنین نرخ‌های همه‌گیرِ اوتیسم وجود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/141034" target="_blank">📅 22:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141033">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ab68747c4.mp4?token=YjUOshxS6_2uMJA8wRvgIDWmXXdSMhuHqaCT8XmYYpraNcUzEqpvMYJXulSl9Yc5IIe6qJreODcVZx5cix1Q4VOx-ofKtfgl54ijxUppcugrnC3BNO3ZDrIYLkx_aBpyqfJtyAxNeb9Z-Cri-JOwysVkr9tXQJQOpBx6VnJ4TtoYKMCsaFO_TRsQO3IXzYO8bq5hFo8FhCcMmQpdFPjMM0LliKYJFfrhgLz-BFWlz_H1FTPWz1TfUEa7C6NkvHvSA0WLiN4xQw-NLNCO2eNXYD-e_rUxdPxicMVB83WxsFiy0GHNvXe7BhBJCE271qns2pYc1pdxMOur24DpPBs_IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ab68747c4.mp4?token=YjUOshxS6_2uMJA8wRvgIDWmXXdSMhuHqaCT8XmYYpraNcUzEqpvMYJXulSl9Yc5IIe6qJreODcVZx5cix1Q4VOx-ofKtfgl54ijxUppcugrnC3BNO3ZDrIYLkx_aBpyqfJtyAxNeb9Z-Cri-JOwysVkr9tXQJQOpBx6VnJ4TtoYKMCsaFO_TRsQO3IXzYO8bq5hFo8FhCcMmQpdFPjMM0LliKYJFfrhgLz-BFWlz_H1FTPWz1TfUEa7C6NkvHvSA0WLiN4xQw-NLNCO2eNXYD-e_rUxdPxicMVB83WxsFiy0GHNvXe7BhBJCE271qns2pYc1pdxMOur24DpPBs_IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: من وارد [کاخ سفید] شدم و گفتم: می‌خواهم بفهمم چه اتفاقی درباره اوتیسم در حال رخ دادن است.
🔴
امروزه تعداد موارد خیلی خیلی بیشتر از سال‌های گذشته است. این وضعیت به‌تدریج بدتر می‌شود و هم‌زمان، ما روزبه‌روز واکسن‌های بیشتری داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/alonews/141033" target="_blank">📅 22:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141032">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
مهاجرانی: گرانی‌های موجود، ناشی از فشار اقتصادی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/141032" target="_blank">📅 22:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141031">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21e62cdc03.mp4?token=L9VeyB5GDI7JbweWiFtKj8v9g79W2f7ldSI8T458qZZw6e9ARLcECS5xyW1HgSERZYZMnaFqkwJ0FtELxTd7HzC2fzXj7n3woWeQGY3TqN1MGTte1q4r9gQy8hyaWPdR0iaBF1ebDT7rr8EkXZSqF1cNAG01b4zFHiSLTg1OERkyIMaZS9r8Hob9O0Q1bdAK6_EJ7NrkNRgdNzLa6hkxTIPygSyWmKU_U2FObFrX-GijRpb1mO4ChORrSKiq0PMvYMv4NmRBO9NWL4BAwFVzJ3yfKBp0U_h32FM9Kd3HDXP43w28WHCuSS8Sgu5fAFnvGBHXCZhaFtUeJvJZ-Sy2DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21e62cdc03.mp4?token=L9VeyB5GDI7JbweWiFtKj8v9g79W2f7ldSI8T458qZZw6e9ARLcECS5xyW1HgSERZYZMnaFqkwJ0FtELxTd7HzC2fzXj7n3woWeQGY3TqN1MGTte1q4r9gQy8hyaWPdR0iaBF1ebDT7rr8EkXZSqF1cNAG01b4zFHiSLTg1OERkyIMaZS9r8Hob9O0Q1bdAK6_EJ7NrkNRgdNzLa6hkxTIPygSyWmKU_U2FObFrX-GijRpb1mO4ChORrSKiq0PMvYMv4NmRBO9NWL4BAwFVzJ3yfKBp0U_h32FM9Kd3HDXP43w28WHCuSS8Sgu5fAFnvGBHXCZhaFtUeJvJZ-Sy2DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برخورد خودرو با یک هواپیما در فرودگاه میلان
🔴
یک خودروی خدمات فرودگاهی حین مانور در فرودگاه «لیناته» میلان، با بخش جلویی بدنه یک هواپیما برخورد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/141031" target="_blank">📅 22:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141030">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
کانال ۱۵ اسرائیل: هر شب ایران حملاتی را علیه نیروهای آمریکایی در منطقه تنگه هرمز انجام می‌دهد، در حالی که واشنگتن سکوت خبری را انتخاب و ابهام را حفظ کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/141030" target="_blank">📅 22:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141029">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
رئیس‌جمهور کلمبیا در پی زلزله ۷.۴ ریشتری اعلام وضعیت فوق‌العاده کرد
🔴
این زمین لرزه تا الان ۱۱۱ کشته و ۸۷ زخمی داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/141029" target="_blank">📅 22:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141028">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ff6a59fa9.mp4?token=KzD5HoU8s3rjhSSDy6niwT61kGG5fvPn-SlAqdRcqm7FR1Iyxl1j4nQ4kOoLslGIw8f7mTtktpoMbvuinsLwd8IUmoYcafQcdPpnC3KCTqkB8_IrDrJZBR2MIdXbBOYPIRQKvJzGNzK-FHH-1Ybsk7yrSW0prW275NchE1CFbGBSRvncYKiSpmz88zkiDK-1hzzsj4sBSGv-Bsbee1BOecGNTc4Ff47R0ChPHMm0h9XZxXtTy3ca6vrXYgAQ0J_-1fsMc3bXiKTMshyOzAigt5iosvh3Le6aUtCZcBXl9rtNvNIkXRPTy2T3E6zg-FG3YEvHqOISIdgfON2NWMThmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ff6a59fa9.mp4?token=KzD5HoU8s3rjhSSDy6niwT61kGG5fvPn-SlAqdRcqm7FR1Iyxl1j4nQ4kOoLslGIw8f7mTtktpoMbvuinsLwd8IUmoYcafQcdPpnC3KCTqkB8_IrDrJZBR2MIdXbBOYPIRQKvJzGNzK-FHH-1Ybsk7yrSW0prW275NchE1CFbGBSRvncYKiSpmz88zkiDK-1hzzsj4sBSGv-Bsbee1BOecGNTc4Ff47R0ChPHMm0h9XZxXtTy3ca6vrXYgAQ0J_-1fsMc3bXiKTMshyOzAigt5iosvh3Le6aUtCZcBXl9rtNvNIkXRPTy2T3E6zg-FG3YEvHqOISIdgfON2NWMThmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار در مخزن سوخت پالایشگاه الزاویه لیبی
🔴
منابع آگاه به رویترز گفتند چند انفجار در یکی از مخازن سوخت پالایشگاه «الزاویه» در لیبی رخ داده است.
🔴
هنوز جزئیات دقیقی درباره ماهیت این حادثه منتشر نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/141028" target="_blank">📅 22:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141027">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc9a5d1a48.mp4?token=jGeE3JAVXVrSAXIO4bvg_qf6s0hmA4uIJ2DwQ4XSeHst8N1ZyyM-9vU7dcU_PLXAmpienVgU0rfHqDUphyqnI4j6AaJiM-8FUQdPbG_QjyhQY2OeO0UK9TWc1-0f7u4PsxfnEvXrKhySPHZcN0vw_2IjRGlWcN6Oj-r0jrA0K3JoPOPGhgVgBr_r_-wUOlePwaD4cuJL1v0C2CInRhCTWNOf-DzBJcquPg9vwbMVj1lxMQeqopJg9bEiBuOGi5I1Vl6LUjFYz1UA-sGvSh6PIY6qRQMX1jaZ_Dd0DusSP-cvYDITmomB8EegWvThLM6mLdCRdZIhzkGEbeLOXNdS3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc9a5d1a48.mp4?token=jGeE3JAVXVrSAXIO4bvg_qf6s0hmA4uIJ2DwQ4XSeHst8N1ZyyM-9vU7dcU_PLXAmpienVgU0rfHqDUphyqnI4j6AaJiM-8FUQdPbG_QjyhQY2OeO0UK9TWc1-0f7u4PsxfnEvXrKhySPHZcN0vw_2IjRGlWcN6Oj-r0jrA0K3JoPOPGhgVgBr_r_-wUOlePwaD4cuJL1v0C2CInRhCTWNOf-DzBJcquPg9vwbMVj1lxMQeqopJg9bEiBuOGi5I1Vl6LUjFYz1UA-sGvSh6PIY6qRQMX1jaZ_Dd0DusSP-cvYDITmomB8EegWvThLM6mLdCRdZIhzkGEbeLOXNdS3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت بزرگراه تهران شمال، امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/141027" target="_blank">📅 21:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141026">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
مقام ایرانی به المیادین:
تهران تا زمانی که واشنگتن شرایط تفاهم‌نامه ماه ژوئن، به ویژه لغو توقیف دارایی‌های ایران و پایان دادن به جنگ در لبنان را که هر دو از الزامات کلیدی هستند، برآورده نکند، تنگه هرمز را بازگشایی نخواهد کرد.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/141026" target="_blank">📅 21:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141025">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
یک مقام ایرانی به MSNOW گفت:
تهران تا زمانی که واشنگتن شرایط تفاهم‌نامه ماه ژوئن، به ویژه لغو توقیف دارایی‌های ایران و پایان دادن به جنگ در لبنان را که هر دو از الزامات کلیدی هستند، برآورده نکند، تنگه هرمز را بازگشایی نخواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/141025" target="_blank">📅 21:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141024">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d6e98827d.mp4?token=QUv92cYyKCE8qfQuyLN5Hwg4vl21FtqnsPKY8RpcYsplef0oYsIYeF-4olD2CjC5RU-KYeQ1NQNdLP_HlSnURbXlBosx6CPupWb7PzkEQpH8LdeYAQm_S1qg-Epgq5V_AHax25kd-ZTu0EhD9uMFZeuSBizhlOYZl6quiv-vb07zl4Z04jZxAVuJ4DeiuWB0W8H_hWax9dJx_CZAYu1E6WBmz0OrZCOwZGOYjo74MoRN-cNcWTSThO7Pre77cRibrlE-wlY3TSwxxZRewhm2EeUV_iSne37RRur5PhSePl_mPbLO9Tcwlu2pJcL_zdE1EYUuC2Sani0pvIn0a1t6WnH0gVfHMAff6nf-Tn301tTefnZjycbpelFhVcOmqJpJ5AQdGj14SgX3M0djsxpVcitg3-n4jIqNcV5aK1tNnM8gFAnB5uQqIms15ibMz0N2TTG-muouvYj7mge5Ii8xbWYBts8OgJs684LmeaYvEYXlVuaoa1dPCtQlB7XHQYy04bswxD8am-e5_4QpYhHA-rVVfoe4qteucbD8lJL6gGjGjoaqYCHYEqSRdD2ugJxCB1iKpg3tFc812hJb4-hJg_ANIA04I5XIJgo_resVUCqpia3CKyWOZfneiR8tk3i8AQ0wSZrQ2wjYSHTjnVC7-cul3y6w57k6aP3Z2a2oNhc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d6e98827d.mp4?token=QUv92cYyKCE8qfQuyLN5Hwg4vl21FtqnsPKY8RpcYsplef0oYsIYeF-4olD2CjC5RU-KYeQ1NQNdLP_HlSnURbXlBosx6CPupWb7PzkEQpH8LdeYAQm_S1qg-Epgq5V_AHax25kd-ZTu0EhD9uMFZeuSBizhlOYZl6quiv-vb07zl4Z04jZxAVuJ4DeiuWB0W8H_hWax9dJx_CZAYu1E6WBmz0OrZCOwZGOYjo74MoRN-cNcWTSThO7Pre77cRibrlE-wlY3TSwxxZRewhm2EeUV_iSne37RRur5PhSePl_mPbLO9Tcwlu2pJcL_zdE1EYUuC2Sani0pvIn0a1t6WnH0gVfHMAff6nf-Tn301tTefnZjycbpelFhVcOmqJpJ5AQdGj14SgX3M0djsxpVcitg3-n4jIqNcV5aK1tNnM8gFAnB5uQqIms15ibMz0N2TTG-muouvYj7mge5Ii8xbWYBts8OgJs684LmeaYvEYXlVuaoa1dPCtQlB7XHQYy04bswxD8am-e5_4QpYhHA-rVVfoe4qteucbD8lJL6gGjGjoaqYCHYEqSRdD2ugJxCB1iKpg3tFc812hJb4-hJg_ANIA04I5XIJgo_resVUCqpia3CKyWOZfneiR8tk3i8AQ0wSZrQ2wjYSHTjnVC7-cul3y6w57k6aP3Z2a2oNhc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: باید موضوع هسته‌ای مشخص بشه، آقای جلیلی با شعار دادن نمیشه کشور رو اداره کرد
🔴
این اصلا اسمش مقاومت نیست و کشور دچار فرسایش شده
🔴
برشی از مناظرات سال 92
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/141024" target="_blank">📅 21:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141023">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9waVU3zqOS7k-0db_Qr8aaIbuwtdTVi5AUBxqDrI89YeLOg4AkY_58CZTx8KR3K5sC3NczAYpzDE7aS0OYGRG6KREZ3qcCqzUyKUDqGgVfMzJoPZ3YiB9YhbcNS7eU505Ajpn9C9wQNFdYre20Sap462kAXsDvRzBsq_USq4VcJ7rNDWwaJQkGeTEPprLXHGXfUgQ7mvMrSTXHJvmUyGb1-yFR0AbUXaBFaOhoacDyc56U6Jh5_3d9ATM44uWqnl86C7PKamq02oYKE2WxAkGmg7p5gdl_Tm57s2bCQbcDoGI8eMsASiyUmEvnzFvTYuK_v7ocMY8sg_I9-OwS3_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
همچنین ایران در مذاکرات باید مسئولیت خساراتی که به مردم لبنان، سوریه، یمن و غزه وارد کرد، بپذیرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/141023" target="_blank">📅 21:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141022">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4425ba840c.mp4?token=Qrm--wfUjmYVVy47QNwMc4MPy_bcaXA5lJ1RU1vwAJ2XI7PmlGKo_kA5IePP4r3EviWg_UZwgTUgAw1Arkb1pkgAKVu1-6yAMZuQXuLNk1sxFiXjSnY72-jhDSn6GSnOWmszCJQQB0vzsS4EwRLU3qmnp5pE-vqKs0KVropagOBioTwDnePwKB4AVF0_U9BMs1vgrEGEJce5eE6aLI13w06UaX0rM9A_Tb3QpP6rNAtw075AZ6drQytlNT2Z6arnZBreOGPNMX5OQdysmVKvqVwVHMGI-_-EE4cH7tSlSX2J7EvkdoZW7PuLwdtuzPBKWtV47m67Gq8OFBit4b3MYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4425ba840c.mp4?token=Qrm--wfUjmYVVy47QNwMc4MPy_bcaXA5lJ1RU1vwAJ2XI7PmlGKo_kA5IePP4r3EviWg_UZwgTUgAw1Arkb1pkgAKVu1-6yAMZuQXuLNk1sxFiXjSnY72-jhDSn6GSnOWmszCJQQB0vzsS4EwRLU3qmnp5pE-vqKs0KVropagOBioTwDnePwKB4AVF0_U9BMs1vgrEGEJce5eE6aLI13w06UaX0rM9A_Tb3QpP6rNAtw075AZ6drQytlNT2Z6arnZBreOGPNMX5OQdysmVKvqVwVHMGI-_-EE4cH7tSlSX2J7EvkdoZW7PuLwdtuzPBKWtV47m67Gq8OFBit4b3MYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مرعشی: دست از سر مردم بردارید، مردم دنبال شهادت و این چیزا نیستن، اونا فقط دنبال زندگی آروم و راحت هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/141022" target="_blank">📅 21:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141021">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQmKp9AKoh8Wg2cexYAKWwN0kjW_oPtCS8XGoTzlgFE6Di_R-D4WIx5qcppFovrdNHIIqCf4pCl2E16LDhrWM1diMWNy1cHy1rtmxdOvExTIAgSjcFRa05OR4bBLPmHf978Zvfsbu4j-x0lyrS2lzC4fa9gzXXkQCmgnT3idPlS5AFLcg4if04U7jQENHqbZEzKqcYfkm9Ab4MUyGDP4usZ6CLGEydpDwglq2-o3bYTlFEaiLzw1gXmGP1qs7rL0es2sr8CTcfS75yHiktSzFUH_sf4yC8wAcwcnlzkZZ3qYFRQBRI8OwGgY5YGTr1ILXVKCLC-VkiAboxsFnd4ebQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شهرداری تهران از آغاز خرید خانه های سانتی متری خبر داد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/141021" target="_blank">📅 20:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141020">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
شبکه ۱۲ عبری گزارش داد ارتش آمریکا روند خروج و کاهش تعداد هواپیماهای سوخت‌رسان خود از فرودگاه بن‌گوریون را با شتاب بیشتری ادامه می‌دهد.
🔴
گزارش‌ها نشان می‌دهد شمار هواپیماهای سوخت‌رسان آمریکایی مستقر در این فرودگاه، به عدد دوران آتش‌بس (حدود ۲۰ فروند) نزدیک شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/141020" target="_blank">📅 20:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141019">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏
👈
سفیر سابق ایران در آذربایجان:
تعلق ۵۰ درصدی دریای خزر به ایران، هیچ مبنای حقوقی و تاریخی ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/141019" target="_blank">📅 20:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141014">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/leU4DyAal9xCOWtJdidgjxkCKx_qbtUwdngz1-RyURBSgN87pmxUnCLIxGtdcowDz-7C0SxGQaYMGm1toKYTEPZ2UDm1ruJISalgUq7h-Hi6-OE8WxYGBee7KIHP7d438HlVbS8msDkI9VQBwZer0BGW79WlEZe9BNRXF7Y_JeqC7XukpBrK7xzmhKz15KvSowsWOk-SdxbbL9U9Hg3olfwLclf2j2vFhDm4XHhKIKNo9rNxCDs8Hrc_9ROakABtWZ1Y80XoS_1gvoKWkV5tI-kFnLVhXlE-m31KuUQ4gqVRa7NyQqvSXMP7NsOWWuVbXEn2iU6uyh8jCsQbqppB9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pbK7PSUYGBIY3MRpiTbmI--X97rPaegNqPSY2DjRSzDlKQvkj0PKoDdV-9OBKbSPZtI-DGWI9Wn3ngVUGut_nIKPEk-vj6erKNpa2ULbbarD5dUccWcavdhlKzhP6Vb53eqXDkZRUGiuRn8dac__kFytVvmfwW8fABuxeuOTsDP6heXMBFDk8PfIs6VUZlv96cefH_qJyYJZuYFSqACSrhSQi6OAc1twaOn1zJriMuvso4ExgZ_6HgiRMRR7QTdaeL58EK9FSdFKztYd8BQaICGliTwWUEqTq8cH-PoDriWgRYbvjiMheLDqengn7SARfrNNIHJzJLS6NuLZ3WywJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RATnqpScbYgjyp68BVIFmaYaLsnY7lu166SvThMz8Zx2jzXqSXMihsu4EJ3qU0UIKVdjIgEBfsEkdzY7BWjKaROGZcQooZUX7QdlbCoNHHB5EM1pWTdvAuGr95DTPEOflFuac_2SkqNuomtXf8ClBacdRo_ETdm4U-9kGGskZ6BXQ0wvjgRjN3Mut1uU4N8XbuCMDFi5dnIOh9OPevmRn95Ng0lnq1XKEfq6grErfI5HvW3c4V3BKuQlZLwgsEzhkfCnVSXc3AL053Ls7ik05mCLTvjzIfiMh-4qQ2suqtGG9IkAdZO_UBibuqmqvG4LXZxLibxtPm_aP5bp7QRrpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MRTCpnojIOBNDoXpRSZ2SJ_JxrQSV-4vsUNq9A8MC2RJ469uRNg0cTKu1OGptcmS-i-FBRHFWcSPzXBs1q5fu-6KTJ-hznea-2KKPLV_qHdIuvW-Nk7doLV_Nk3GWI5oZUhfepsTOdA0vkU26m11Mfgly9jAtvQM9UGsc3E4_ROrYpnjcFI1MK1r-IXxTDemkJq4Yv-CZwJLXhvrc-4Um1ZMbGA1P3vD26RpgU3hUAwMBVPAfScvY3YY_XOGUpuluJU7UyM6ul2OPvuOS68nmCQ-pVrlfsrBKehhzczwg9Mth_D-wohxIu_9wXb-X7iQAKjckSvC-6c7U4GgULT4HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m3a6kIibzNs4t4yPZ9sUClxyOZQpebjnxH6jgCj-w3eXh9Q7oCUEuSyZdy9UlQQpnOrtZUumsQ1GPxuLOkVbYEgeP-ZdRW23dQ32JTs6sB6UE58VhFjrgZcReBtDowxshGWucDx_BnnmaeE2via4ahwyG7MfWJVB1jcngV4uBUeCgYT_ZDvAs-FvbrvBO41c_HvhZNaaeD95XTN4I4E7pkFTZS0rL8zB8smj7lyuUz7_vrgasqQC11CGWbp5rvirNfCjnlGMeAxYbFe39qFS9VLOPeNku_iafPyrrFHASueTfE9COIOlWl8ICbXaLS31za3HlEb_mOYwPryFjodVVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟢
ادمین صفحه طرفداری خیبر خرم‌آباد بازداشت شد!
در این صفحه، طرح‌هایی برای ۱۸ و ۱۹ دی، رشید مظاهری علیه ضحاک ماردوش، و رونمایی از لباس باشگاه با مدل‌های زن بدون حجاب اجباری، منتشر شده بود.
@AloSport</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/141014" target="_blank">📅 20:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141013">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4754071911.mp4?token=WitblavDiziKre39j5KAjOpmdBdTkGfpKSgLg0ZPvUyfyKnniNSY9Viu6fZk9y6WP1JbZTlBElOseYs5Fxgwu27zc6caaVy1vRdd2_mK4dILwTWGeZM6sTG8UgG37HECClnpe4QKe3Tle5Up9ADC16-xIs_g2URbN9sJ_E3pk-b9nPOHk2to6L1FOKNIeePOQRA-GC8xJw8blogHdqVcVvuAAu9m6UEsW7b1PNWgs5K9x0UjtZOJ2yZdd7koEIrV8bpyWbn_tl16JmOeJBko4cx_NWoUchLqX1jgANYp-n26t3XAnKR1MuqJ9743Jp-NQPEqRII-ah7CxfYrZqb44Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4754071911.mp4?token=WitblavDiziKre39j5KAjOpmdBdTkGfpKSgLg0ZPvUyfyKnniNSY9Viu6fZk9y6WP1JbZTlBElOseYs5Fxgwu27zc6caaVy1vRdd2_mK4dILwTWGeZM6sTG8UgG37HECClnpe4QKe3Tle5Up9ADC16-xIs_g2URbN9sJ_E3pk-b9nPOHk2to6L1FOKNIeePOQRA-GC8xJw8blogHdqVcVvuAAu9m6UEsW7b1PNWgs5K9x0UjtZOJ2yZdd7koEIrV8bpyWbn_tl16JmOeJBko4cx_NWoUchLqX1jgANYp-n26t3XAnKR1MuqJ9743Jp-NQPEqRII-ah7CxfYrZqb44Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خرازی: انگلیسی را از چپ به راست می نویسند، چون زبان شیطانی است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/141013" target="_blank">📅 20:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141012">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ترامپ :  می‌بینم که نماینده‌های ایران برای خسارت‌هایی که تو جنگ پنج‌ماهه اخیر بهشون وارد شده، درخواست غرامت می‌کنند؛ در حالی که این موضوع اصلاً توی هیچ‌کدوم از مذاکرات و دیدارهای ما مطرح نشده بود!
🔴
خب، حالا که این‌طوره، من هم از ایران غرامت می‌خوام
🔴
بابت…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/141012" target="_blank">📅 20:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141011">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-n4UgQbI_hWw4IaMWZVrcidHcyw3LwB8j8huv7A2LS10MyNjYbFB16IF7MVQdu7T5C9TAoJXhOsz8Zpkj9lNFuUfVqapCXUM3boHkFpHqp3G35hwHr7M4URz6-m2bnieAgPUK1-kUT9A3Rbxa4vTcgpBhJdQICjvauEuuEgf2iYNomY-dph681enIt4XooQoxIFzsknMssSK36YhZ0hPmxBqAdJMGVhm5A7GQcpYCfNmJuzdbFGIwc0kVEFjztyh6ndfsWF-Jifwu_nVqBUBigtIyGzFNgOeiYJf-R7mUO1p1GJ4_ZUxhvsIWiUy2E3xmmF5Z1NdgMhlS_EnhWZlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ :
می‌بینم که نماینده‌های ایران برای خسارت‌هایی که تو جنگ پنج‌ماهه اخیر بهشون وارد شده، درخواست غرامت می‌کنند؛ در حالی که این موضوع اصلاً توی هیچ‌کدوم از مذاکرات و دیدارهای ما مطرح نشده بود!
🔴
خب، حالا که این‌طوره، من هم از ایران غرامت می‌خوام
🔴
بابت تمام آمریکایی‌هایی که در درگیری‌های مختلف کُشته یا به‌شدت زخمی شدند، من به نماینده‌هام دستور دادم این موضوع رو در همه مذاکرات آینده با ایران به‌طور جدی مطرح کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/141011" target="_blank">📅 20:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141010">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qen6OTDI34TckSLvi0dS91YhJWO3OnJSNe-1qDcyg65VCOYwJyHoaRbYcPtX0UEiUJYYRz2NUVb2qmu-iCuEidT9WHLsBK640CzTqw6e1V5dGk-97nsoUAj9hmG-hhU0Q0nKGZR4-ymI9BinqCIFgyh48Ew4K_mE-R4hmDbsW6hynHgyPHGy-ACHdLy8V_uOZXRe_BV5CHfZw9geNOeIJG62--C97GIWsAw3kPgdnsJDV69Pmgrhf3d67wQiF04X0VU3vnkubGaJhBsYRKIUNrmvlRk05FrpRd1Jz998oXezUr7TyJtmCaeMwdZHUDABOJihJBS8VCXqBBmidGGCJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد مرندی: ایران آگاه است که نیروهای رژیم ترامپ در کویت، امارات متحده عربی، قطر، عربستان سعودی، بحرین و اردن در حال بسیج برای یک حمله برق‌آسای بالقوه احتمالاً در کنار نیروهای اسرائیلی علیه مردم ایران هستند
🔴
جمهوری اسلامی با پاسخی سریع و کوبنده آماده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/141010" target="_blank">📅 20:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141009">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNlMG8wHGvVdC5HtV5HExrOmI5xs1EayVbOOXGWmIL4UveOb17pZurBb9TXF2B6sCn5MQTTD7MgJZpKx7Dl3PcrtmEvCqBhPNKLhJ0f8JxYYzBEY5FEQZK1u7uLHxZccyu7gW1mwnkp8KlT_vKl-9H-eLeim8wcgZEwh6wcl6VEs-a0DUNYD5sFnbci_AUepNRP8D_tp1MAvbowDa4lTQUxqf2z76lnPfHo1oVIoqMNdz_e2YHRawLAQ9TqkI_FVNGr8CrbY21QGZhc1ffWZi4PUQYDkE4wEu0szKh1tBuTnzmJtmihtH_4am6b9vHtXo3aPqfARbBYyvtFwXPPIog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: آقا مجتبی سالم و رو فرم هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/141009" target="_blank">📅 19:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141008">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiYhKZxKprk-8IhQl44ZjKQxkoz-y0URH9K64IGctV7-n9KbywjYw9mcjwi04HB2OA7Z4-7vztLFCFByeZVtqDgI1OAdu2Biyuol2hABHcSisXCAc7c4vxZa3FkJB3ueJwQPvrc5kUrJI3mETvVpsdVNcfMkOXt07Ix4j9JimH-hhzHd-AWV9Pt5xi7tKtGibzkL1MKVp20lgvoTHXWUYu7cItDgI_0v5gmuXULEcxqrIkZRFl3RrLIYyRYhO6WB7sEBPs3afaQxkMmkZ4wC3S8zNkXVMhrfacv3YIKUUASXFJaSHHMYhRyeIJoQr7pXIx0oSZnUzdy6U9CrxqjDjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال: ایران عبور ناوهای جنگی آمریکا از تنگه هرمز را برای همیشه ممنوع می‌کند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/141008" target="_blank">📅 19:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141007">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSM3J-Dy8y9oIMC4usw0DL5-q_KSW1P72s7FLsEwOuy683AbCY4AUzxM94os7wJq5DzYaIZA0ATNRTIuEvXhubzp0kMqytyi4uUpl30Eg9tmYMSNz4Lcsk2VuBF-6_8ygddAW-I4ivJFufnPpdfox0xwz0EjAgK19C6Dpw0AdviU1hXkMOvxZ-GF0Sehjj4jFyWq78JE-ssTz0dQVWPVkfWh9afhF0ZRXleQ_Dp4rKaoiDrMuZ5ptqt_Vo9OWExrBIunuuj0GAEpFPxLK4V-HigTnOpecZV1SJE-KRfzhvSOfVy3ZLReli1fUT4eaApl92g6V_eoZ2OVNsF46I0-sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
انقلابی در صنعت هوش مصنوعی
🔥
🔥
🔥
🚨
تاحالا شده دلت بخواد ترید انجام بدی درامد دلاری داشته باشی ولی علم کافیشو نداشته باشی؟
🔴
پلتفرم TimeTrade یه صرافی انگلیسیه که یه هوش مصنوعی در زمینه ی auto trade ساخته که باهاش دیگه نیاز نیس برای کسب درامد علم ترید بلد باشی
همه چیو به هوش مصنوعی بسپار خودش اتومات برات انجام میده
✅
با این صرافی با هر مقدار از علم و دانشی درامد دلاری و روزانه و لایو داشته باش
🔥
👇
https://t.me/+BO755zQm6VM1NDE8</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/141007" target="_blank">📅 19:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141006">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
براساس نظرسنجی جدید شبکه CNN، محبوبیت پیت هگست، وزیر جنگ آمریکا در پایین‌ترین سطح ممکن و در وضعیت منفی قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/alonews/141006" target="_blank">📅 19:47 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
